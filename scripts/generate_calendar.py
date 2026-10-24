#!/usr/bin/env python3
"""
BRAN Org - Gerador de Calendário de Curadoria e Utilitário de Notificação.
Lê curation-schedule.yml e:
1. Gera calendar.ics (RFC 5545) para assinatura no Google Agenda / Apple Calendar.
2. Fornece CLI para o GitHub Actions inspecionar tarefas ativas em um dado mês/ano.
"""

import sys
import os
import argparse
import json
import calendar
from datetime import datetime, timezone
import yaml

DEFAULT_SCHEDULE_PATH = os.path.join(os.path.dirname(__file__), "..", "curation-schedule.yml")
DEFAULT_OUTPUT_ICS = os.path.join(os.path.dirname(__file__), "..", "calendar.ics")


def load_schedule(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def is_active_for_year(cadence: str, year: int) -> bool:
    if cadence == "annual":
        return True
    elif cadence == "biennial-even":
        return year % 2 == 0
    elif cadence == "biennial-odd":
        return year % 2 != 0
    return False


def escape_ics_text(text: str) -> str:
    if not text:
        return ""
    # RFC 5545 escaping
    text = text.replace("\\", "\\\\")
    text = text.replace(";", "\\;")
    text = text.replace(",", "\\,")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\n", "\\n")
    return text


def generate_ics(schedule_data, output_path, start_year=2024, end_year=2032):
    settings = schedule_data.get("settings", {})
    databases = schedule_data.get("databases", [])
    
    cal_title = settings.get("calendar_title", "BRAN Org - Calendário de Curadoria")
    cal_desc = settings.get("calendar_description", "Ciclos de verificação e curadoria de dados da BRAN Org.")
    now_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//BRAN Org//Data Curation Calendar//PT-BR",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{cal_title}",
        f"X-WR-CALDESC:{cal_desc}",
        "X-WR-TIMEZONE:America/Sao_Paulo",
    ]
    
    for db in databases:
        db_id = db["id"]
        db_name = db.get("short_name", db["name"])
        cadence = db.get("cadence", "annual")
        check_months = db.get("check_months", [])
        url = db.get("url", "")
        repo = db.get("repo", "")
        summary_text = db.get("summary", f"Curadoria {db_name}")
        description_raw = db.get("description", "")
        checklist = db.get("checklist", [])
        
        # Build description
        desc_parts = [description_raw]
        if repo:
            desc_parts.append(f"Repositório: https://github.com/{repo}")
        if url:
            desc_parts.append(f"Fonte Oficial: {url}")
        if checklist:
            desc_parts.append("\nChecklist Operacional:")
            for item in checklist:
                desc_parts.append(f"- [ ] {item}")
        full_desc = "\n\n".join([p for p in desc_parts if p.strip()])
        escaped_desc = escape_ics_text(full_desc)
        
        for year in range(start_year, end_year + 1):
            if not is_active_for_year(cadence, year):
                continue
            
            for month in check_months:
                _, last_day = calendar.monthrange(year, month)
                dtstart = f"{year:04d}{month:02d}01"
                # DTEND in all-day events is exclusive, so next month 1st or next day
                if month == 12:
                    dtend = f"{year+1:04d}0101"
                else:
                    dtend = f"{year:04d}{month+1:02d}01"
                
                uid = f"bran-curation-{db_id}-{year}-{month:02d}@bran.org"
                
                lines.extend([
                    "BEGIN:VEVENT",
                    f"UID:{uid}",
                    f"DTSTAMP:{now_stamp}",
                    f"DTSTART;VALUE=DATE:{dtstart}",
                    f"DTEND;VALUE=DATE:{dtend}",
                    f"SUMMARY:[BRAN Curadoria] {summary_text} ({year})",
                    f"DESCRIPTION:{escaped_desc}",
                ])
                if url:
                    lines.append(f"URL:{url}")
                
                # Add Alarm 7 days before
                lines.extend([
                    "STATUS:CONFIRMED",
                    "TRANSP:TRANSPARENT",
                    "BEGIN:VALARM",
                    "TRIGGER:-P7D",
                    "ACTION:DISPLAY",
                    f"DESCRIPTION:Lembrete: {summary_text} ({year})",
                    "END:VALARM",
                    "END:VEVENT"
                ])
                
    lines.append("END:VCALENDAR")
    
    content = "\r\n".join(lines) + "\r\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Calendário gerado com sucesso em: {output_path}")


def get_active_tasks(schedule_data, year: int, month: int):
    """Retorna a lista de tarefas ativas para um ano e mês específicos."""
    databases = schedule_data.get("databases", [])
    active = []
    for db in databases:
        cadence = db.get("cadence", "annual")
        check_months = db.get("check_months", [])
        if is_active_for_year(cadence, year) and month in check_months:
            active.append({
                "id": db["id"],
                "name": db["name"],
                "short_name": db.get("short_name", db["name"]),
                "repo": db.get("repo", ""),
                "url": db.get("url", ""),
                "summary": db.get("summary", ""),
                "description": db.get("description", ""),
                "checklist": db.get("checklist", []),
                "labels": db.get("labels", ["curation"]),
                "year": year,
                "month": month,
            })
    return active


def main():
    parser = argparse.ArgumentParser(description="BRAN Org Curation Calendar Generator")
    parser.add_argument("--schedule", default=DEFAULT_SCHEDULE_PATH, help="Caminho para curation-schedule.yml")
    parser.add_argument("--output", default=DEFAULT_OUTPUT_ICS, help="Caminho para saída do calendar.ics")
    parser.add_argument("--check-year", type=int, help="Ano para verificar tarefas ativas")
    parser.add_argument("--check-month", type=int, help="Mês para verificar tarefas ativas (1-12)")
    
    args = parser.parse_args()
    schedule_data = load_schedule(args.schedule)
    
    if args.check_month is not None:
        year = args.check_year if args.check_year is not None else datetime.now().year
        tasks = get_active_tasks(schedule_data, year, args.check_month)
        print(json.dumps(tasks, ensure_ascii=False, indent=2))
        return
    
    generate_ics(schedule_data, args.output)


if __name__ == "__main__":
    main()
