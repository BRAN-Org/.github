#!/usr/bin/env python3
"""
BRAN Org - Gerador do Widget SVG de Status de Curadoria do Mês.
Inspeciona curation-schedule.yml para o mês atual e renderiza um card SVG
elegante no padrão GitHub Dark Mode para exibição no CALENDAR.md e README.md.
"""

import os
import sys
import argparse
from datetime import datetime
import xml.sax.saxutils as saxutils

from generate_calendar import load_schedule, get_active_tasks, is_active_for_year, DEFAULT_SCHEDULE_PATH

MONTH_NAMES_PT = [
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

DEFAULT_SVG_OUTPUT = os.path.join(os.path.dirname(__file__), "..", "assets", "curation-status.svg")


def escape_xml(text: str) -> str:
    return saxutils.escape(str(text))


def find_next_upcoming_tasks(schedule_data, current_year: int, current_month: int):
    """Encontra as tarefas da próxima janela futura."""
    year = current_year
    month = current_month
    
    for _ in range(1, 13):
        month += 1
        if month > 12:
            month = 1
            year += 1
        tasks = get_active_tasks(schedule_data, year, month)
        if tasks:
            return year, month, tasks
    return None, None, []


def render_svg(schedule_data, year: int, month: int, output_path: str):
    active_tasks = get_active_tasks(schedule_data, year, month)
    month_name = MONTH_NAMES_PT[month]
    
    # Dimensões dinâmicas
    card_width = 820
    header_height = 80
    footer_height = 42
    
    if active_tasks:
        task_height = 70
        content_height = len(active_tasks) * task_height + 15
        total_height = header_height + content_height + footer_height
    else:
        content_height = 75
        total_height = header_height + content_height + footer_height

    # Cores e Status
    if active_tasks:
        status_pill_bg = "#382800"
        status_pill_border = "#bb8009"
        status_pill_text = "#e3b341"
        status_dot_color = "#e3b341"
        count_str = f"{len(active_tasks)} {'BASE' if len(active_tasks) == 1 else 'BASES'}"
        status_text = f"JANELA ATIVA • {count_str}"
        card_accent_border = "#bb8009"
    else:
        status_pill_bg = "#0d2818"
        status_pill_border = "#238636"
        status_pill_text = "#3fb950"
        status_dot_color = "#3fb950"
        status_text = "EM DIA • SEM BASES EM JANELA CRÍTICA"
        card_accent_border = "#30363d"

    svg_lines = [
        f'<svg width="100%" height="{total_height}" viewBox="0 0 {card_width} {total_height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Status de Curadoria - {month_name} {year}">',
        '  <defs>',
        '    <style>',
        '      .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 12px; }',
        '      .title-sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; font-weight: 700; fill: #8b949e; letter-spacing: 1px; }',
        '      .title-main { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 700; fill: #f0f6fc; }',
        '      .status-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; }',
        '      .item-box { fill: #161b22; stroke: #30363d; stroke-width: 1; rx: 8px; }',
        '      .item-name { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; fill: #c9d1d9; }',
        '      .item-desc { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #8b949e; }',
        '      .badge-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; font-weight: 600; }',
        '      .footer-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; fill: #484f58; }',
        '    </style>',
        '  </defs>',
        f'  <rect width="{card_width}" height="{total_height}" class="bg" />',
        '',
        '  <!-- Header -->',
        '  <g transform="translate(24, 20)">',
        '    <!-- Calendar Icon -->',
        '    <g transform="translate(0, 4)">',
        '      <rect x="0" y="0" width="34" height="34" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.2" />',
        '      <path d="M9 7h16M9 13h16M9 18h10" stroke="#58a6ff" stroke-width="2" stroke-linecap="round" />',
        '      <circle cx="21" cy="18" r="2" fill="#e3b341" />',
        '    </g>',
        '    <g transform="translate(46, 12)">',
        '      <text class="title-sub">BRAN ORG • RADAR DE CURADORIA E GOVERNANÇA</text>',
        f'      <text y="22" class="title-main">{month_name} de {year}</text>',
        '    </g>',
        '',
        '    <!-- Status Pill -->',
        f'    <g transform="translate({card_width - 325}, 8)">',
        f'      <rect width="275" height="30" rx="15" fill="{status_pill_bg}" stroke="{status_pill_border}" stroke-width="1.2" />',
        f'      <circle cx="16" cy="15" r="4.5" fill="{status_dot_color}" />',
        f'      <text x="30" y="19" class="status-text" fill="{status_pill_text}">{status_text}</text>',
        '    </g>',
        '  </g>',
        '',
        '  <!-- Divider -->',
        f'  <line x1="24" y1="{header_height}" x2="{card_width - 24}" y2="{header_height}" stroke="#21262d" stroke-width="1" />',
        '',
        '  <!-- Content Body -->',
    ]

    curr_y = header_height + 15
    if active_tasks:
        for task in active_tasks:
            short_name = escape_xml(task.get("short_name", task["name"]))
            name = escape_xml(task["name"])
            summary = escape_xml(task.get("summary", ""))
            repo = escape_xml(task.get("repo", ""))
            
            svg_lines.extend([
                f'  <g transform="translate(24, {curr_y})">',
                f'    <rect width="{card_width - 48}" height="58" class="item-box" />',
                '',
                '    <!-- Tag Badge -->',
                '    <rect x="14" y="14" width="70" height="28" rx="6" fill="#1f6feb22" stroke="#388bfd66" stroke-width="1" />',
                f'    <text x="49" y="32" text-anchor="middle" class="badge-text" fill="#58a6ff">{short_name}</text>',
                '',
                '    <!-- Info -->',
                f'    <text x="96" y="27" class="item-name">{name}</text>',
                f'    <text x="96" y="44" class="item-desc">Ação: {summary} • Repositório: {repo}</text>',
                '',
                '    <!-- Action Indicator -->',
                f'    <g transform="translate({card_width - 150}, 16)">',
                '      <rect width="90" height="26" rx="13" fill="#23863622" stroke="#238636" stroke-width="1" />',
                '      <text x="45" y="17" text-anchor="middle" class="badge-text" fill="#3fb950">VERIFICAR</text>',
                '    </g>',
                '  </g>',
            ])
            curr_y += 70
    else:
        next_year, next_month, next_tasks = find_next_upcoming_tasks(schedule_data, year, month)
        if next_tasks:
            next_m_name = MONTH_NAMES_PT[next_month]
            next_names = " e ".join([t.get("short_name", t["name"]) for t in next_tasks])
            next_msg = f"Próxima janela: {next_m_name} de {next_year} ({next_names})"
        else:
            next_msg = "Nenhuma janela cadastrada para os próximos meses."
            
        svg_lines.extend([
            f'  <g transform="translate(24, {curr_y})">',
            f'    <rect width="{card_width - 48}" height="58" class="item-box" />',
            '    <g transform="translate(18, 17)">',
            '      <circle cx="12" cy="12" r="10" fill="#23863622" stroke="#238636" stroke-width="1.5" />',
            '      <path d="M7 12l3 3 7-7" stroke="#3fb950" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />',
            '    </g>',
            '    <text x="54" y="27" class="item-name">Nenhuma base requer verificação ativa neste mês.</text>',
            f'    <text x="54" y="44" class="item-desc">{escape_xml(next_msg)}</text>',
            '  </g>',
        ])
        curr_y += 70

    # Footer
    footer_y = total_height - 16
    svg_lines.extend([
        '',
        '  <!-- Footer -->',
        f'  <text x="24" y="{footer_y}" class="footer-text">Atualizado automaticamente via GitHub Actions • Fonte canônica: curation-schedule.yml</text>',
        f'  <text x="{card_width - 24}" y="{footer_y}" text-anchor="end" class="footer-text">BRAN Org Data Network</text>',
        '</svg>',
    ])

    svg_content = "\n".join(svg_lines)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Widget SVG de curadoria gerado com sucesso em: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Gerador do SVG de status de curadoria")
    parser.add_argument("--schedule", default=DEFAULT_SCHEDULE_PATH, help="Caminho do curation-schedule.yml")
    parser.add_argument("--output", default=DEFAULT_SVG_OUTPUT, help="Caminho de saída do curation-status.svg")
    parser.add_argument("--year", type=int, help="Ano de referência (padrão: ano atual)")
    parser.add_argument("--month", type=int, help="Mês de referência 1-12 (padrão: mês atual)")
    
    args = parser.parse_args()
    
    now = datetime.now()
    year = args.year if args.year is not None else now.year
    month = args.month if args.month is not None else now.month
    
    schedule_data = load_schedule(args.schedule)
    render_svg(schedule_data, year, month, args.output)


if __name__ == "__main__":
    main()
