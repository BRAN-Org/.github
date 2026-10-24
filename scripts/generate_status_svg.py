#!/usr/bin/env python3
"""
BRAN Org - Gerador do Calendário Mensal em SVG (Vibe Grade Mensal).
Renderiza a folha de calendário tradicional do mês atual no estilo de calendário de parede:
- Cabeçalho com Mês e Ano
- Faixa dos dias da semana (Domingo a Sábado)
- Grade completa com dias do mês anterior/posterior sombreados
- Destaque visual do dia de hoje (HOJE)
- Marcação das semanas e marcos de curadoria ativa da base
- Bloco inferior de notas e checklist para a equipe
"""

import os
import sys
import argparse
import calendar
from datetime import datetime, date
import xml.sax.saxutils as saxutils

from generate_calendar import load_schedule, get_active_tasks, DEFAULT_SCHEDULE_PATH

MONTH_NAMES_PT = [
    "", "Novembro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
# Fix month names index 1..12
MONTH_NAMES_PT = [
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

WEEKDAY_NAMES_PT = [
    "Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira",
    "Quinta-Feira", "Sexta-Feira", "Sábado"
]

DEFAULT_SVG_OUTPUT = os.path.join(os.path.dirname(__file__), "..", "assets", "curation-status.svg")


def escape_xml(text: str) -> str:
    return saxutils.escape(str(text))


def find_next_upcoming_tasks(schedule_data, current_year: int, current_month: int):
    """Encontra as tarefas da próxima janela futura quando o mês atual estiver livre."""
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


def render_calendar_grid_svg(schedule_data, year: int, month: int, today_date: date, output_path: str):
    active_tasks = get_active_tasks(schedule_data, year, month)
    month_name = MONTH_NAMES_PT[month]
    
    # Gerar grade do mês iniciando no domingo
    cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
    weeks = cal.monthdatescalendar(year, month)
    num_weeks = len(weeks)
    
    # Geometria e layout
    card_width = 860
    left_margin = 25
    right_margin = 25
    grid_width = card_width - left_margin - right_margin  # 810 px
    col_width = grid_width / 7.0                          # ~115.71 px
    cell_height = 80                                      # altura de cada dia
    header_top = 22
    header_title_height = 48
    weekday_bar_top = header_top + header_title_height     # y = 70
    weekday_bar_height = 28
    grid_top = weekday_bar_top + weekday_bar_height        # y = 98
    grid_height = num_weeks * cell_height
    
    notes_top = grid_top + grid_height + 16
    notes_height = 110 if active_tasks else 95
    total_height = notes_top + notes_height + 28
    
    # Paleta de cores inspirada na folha tradicional
    PRIMARY_RED = "#c5222f"
    GRID_BORDER = "#e8d5c4"
    BG_CURRENT_DAY = "#fffbf7"
    BG_OTHER_MONTH = "#f0e2d1"
    TEXT_OTHER_MONTH = "#a68d7c"
    TEXT_CURRENT_MONTH = "#c5222f"
    BG_TODAY_CELL = "#fff1f2"
    NOTES_BG = "#fffcf9"
    NOTES_BORDER = "#edd8c7"

    svg_lines = [
        f'<svg width="100%" height="{total_height}" viewBox="0 0 {card_width} {total_height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Calendário {month_name} {year}">',
        '  <defs>',
        '    <style>',
        '      .cal-bg { fill: #ffffff; stroke: #e0d0c0; stroke-width: 1.5; rx: 10px; }',
        '      .month-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 26px; font-weight: 700; fill: #c5222f; }',
        '      .cal-subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #8a7364; }',
        '      .weekday-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #ffffff; text-anchor: middle; }',
        '      .day-num { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 600; }',
        '      .event-strip { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 10px; font-weight: 600; }',
        '      .notes-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #c5222f; letter-spacing: 0.5px; }',
        '      .notes-body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12px; fill: #2c2520; }',
        '      .notes-sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 11px; fill: #7a6659; }',
        '      .footer-txt { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 11px; fill: #998375; }',
        '    </style>',
        '  </defs>',
        f'  <rect width="{card_width}" height="{total_height}" class="cal-bg" />',
        '',
        '  <!-- Top Header -->',
        f'  <text x="{left_margin}" y="{header_top + 30}" class="month-title">{month_name} {year}</text>',
    ]

    # Indicador / status pill no topo direito
    if active_tasks:
        pill_txt = f"● {len(active_tasks)} JANELA DE CURADORIA ATIVA"
        pill_bg = "#fde8e9"
        pill_stroke = "#c5222f"
        pill_color = "#c5222f"
    else:
        pill_txt = "● NENHUMA BASE EM JANELA CRÍTICA"
        pill_bg = "#e6f4ea"
        pill_stroke = "#137333"
        pill_color = "#137333"

    svg_lines.extend([
        f'  <g transform="translate({card_width - right_margin - 270}, {header_top + 10})">',
        f'    <rect width="270" height="26" rx="13" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1" />',
        f'    <text x="135" y="17" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="11px" font-weight="700" fill="{pill_color}">{pill_txt}</text>',
        '  </g>',
        '',
        '  <!-- Weekday Header Bar -->',
        f'  <rect x="{left_margin}" y="{weekday_bar_top}" width="{grid_width}" height="{weekday_bar_height}" fill="{PRIMARY_RED}" />',
    ])

    # Cabeçalhos dos dias da semana
    for i, wname in enumerate(WEEKDAY_NAMES_PT):
        col_cx = left_margin + (i * col_width) + (col_width / 2.0)
        svg_lines.append(f'  <text x="{col_cx:.1f}" y="{weekday_bar_top + 18}" class="weekday-text">{wname}</text>')

    # Divisórias verticais no header da semana
    for i in range(1, 7):
        vx = left_margin + (i * col_width)
        svg_lines.append(f'  <line x1="{vx:.1f}" y1="{weekday_bar_top}" x2="{vx:.1f}" y2="{weekday_bar_top + weekday_bar_height}" stroke="#e06670" stroke-width="1" />')

    svg_lines.append('\n  <!-- Grid Cells -->')

    # Identificar base ativa principal (para exibir os marcos na grade)
    main_task = active_tasks[0] if active_tasks else None
    main_name = main_task.get("short_name", main_task["name"]) if main_task else None

    # Renderizar cada dia da grade
    for r, week in enumerate(weeks):
        row_y = grid_top + (r * cell_height)
        for c, day_date in enumerate(week):
            col_x = left_margin + (c * col_width)
            is_cur_month = (day_date.month == month)
            is_today = (day_date == today_date)

            # Cor de fundo da célula
            if not is_cur_month:
                cell_bg = BG_OTHER_MONTH
                num_color = TEXT_OTHER_MONTH
            elif is_today:
                cell_bg = BG_TODAY_CELL
                num_color = PRIMARY_RED
            else:
                cell_bg = BG_CURRENT_DAY
                num_color = TEXT_CURRENT_MONTH

            svg_lines.append(f'  <rect x="{col_x:.1f}" y="{row_y:.1f}" width="{col_width:.1f}" height="{cell_height:.1f}" fill="{cell_bg}" stroke="{GRID_BORDER}" stroke-width="1" />')

            # Número do dia
            num_x = col_x + 8
            num_y = row_y + 17
            svg_lines.append(f'  <text x="{num_x:.1f}" y="{num_y:.1f}" class="day-num" fill="{num_color}">{day_date.day}</text>')

            # Badge do dia de hoje (HOJE)
            if is_today:
                today_badge_x = col_x + col_width - 44
                today_badge_y = row_y + 5
                svg_lines.append(f'  <rect x="{today_badge_x:.1f}" y="{today_badge_y:.1f}" width="38" height="15" rx="4" fill="{PRIMARY_RED}" />')
                svg_lines.append(f'  <text x="{(today_badge_x + 19):.1f}" y="{(today_badge_y + 11):.1f}" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9px" font-weight="700" fill="#ffffff">HOJE</text>')

            # Marcações e eventos da curadoria na grade
            if is_cur_month and main_task:
                # Milestone no dia 1: Abertura da janela
                if day_date.day == 1:
                    evt_w = col_width - 12
                    svg_lines.append(f'  <rect x="{(col_x + 6):.1f}" y="{(row_y + 24):.1f}" width="{evt_w:.1f}" height="20" rx="4" fill="#fde8e9" stroke="{PRIMARY_RED}" stroke-width="0.8" />')
                    svg_lines.append(f'  <text x="{(col_x + 10):.1f}" y="{(row_y + 38):.1f}" class="event-strip" fill="{PRIMARY_RED}">🚩 Início {main_name}</text>')
                
                # Milestone no dia 15: Validação
                elif day_date.day == 15:
                    evt_w = col_width - 12
                    svg_lines.append(f'  <rect x="{(col_x + 6):.1f}" y="{(row_y + 24):.1f}" width="{evt_w:.1f}" height="20" rx="4" fill="#fff3cd" stroke="#ffc107" stroke-width="0.8" />')
                    svg_lines.append(f'  <text x="{(col_x + 10):.1f}" y="{(row_y + 38):.1f}" class="event-strip" fill="#856404">⚙️ Auditoria</text>')
                
                # Milestone no último dia do mês: Fechamento / Zenodo
                elif day_date.day == calendar.monthrange(year, month)[1]:
                    evt_w = col_width - 12
                    svg_lines.append(f'  <rect x="{(col_x + 6):.1f}" y="{(row_y + 24):.1f}" width="{evt_w:.1f}" height="20" rx="4" fill="#e2e3e5" stroke="#6c757d" stroke-width="0.8" />')
                    svg_lines.append(f'  <text x="{(col_x + 10):.1f}" y="{(row_y + 38):.1f}" class="event-strip" fill="#383d41">📦 Zenodo</text>')
                
                # Se for dia de hoje e tiver tarefa
                elif is_today:
                    evt_w = col_width - 12
                    svg_lines.append(f'  <rect x="{(col_x + 6):.1f}" y="{(row_y + 24):.1f}" width="{evt_w:.1f}" height="20" rx="4" fill="#fde8e9" stroke="{PRIMARY_RED}" stroke-width="0.8" />')
                    svg_lines.append(f'  <text x="{(col_x + 10):.1f}" y="{(row_y + 38):.1f}" class="event-strip" fill="{PRIMARY_RED}">⚡ Curadoria</text>')

    # Borda externa da grade
    svg_lines.append(f'  <rect x="{left_margin}" y="{weekday_bar_top}" width="{grid_width}" height="{weekday_bar_height + grid_height}" fill="none" stroke="{PRIMARY_RED}" stroke-width="1.5" />')

    # Bloco inferior de notas / checklist da equipe
    svg_lines.extend([
        '',
        '  <!-- Notes / Operational Checklist Section -->',
        f'  <rect x="{left_margin}" y="{notes_top}" width="{grid_width}" height="{notes_height}" rx="8" fill="{NOTES_BG}" stroke="{NOTES_BORDER}" stroke-width="1.2" />',
    ])

    if active_tasks:
        task_names = ", ".join([f"{t.get('short_name', t['name'])} ({year})" for t in active_tasks])
        first_task = active_tasks[0]
        checklist_preview = " • ".join(first_task.get("checklist", [])[:3])
        if len(first_task.get("checklist", [])) > 3:
            checklist_preview += "..."

        svg_lines.extend([
            f'  <text x="{left_margin + 16}" y="{notes_top + 24}" class="notes-title">📌 ATIVIDADES DE CURADORIA EM DESTAQUE NESTE MÊS:</text>',
            f'  <text x="{left_margin + 16}" y="{notes_top + 46}" class="notes-body"><tspan font-weight="700">Base Ativa:</tspan> {escape_xml(task_names)} — Repositório: <tspan font-family="monospace">{escape_xml(first_task.get("repo", ""))}</tspan></text>',
            f'  <text x="{left_margin + 16}" y="{notes_top + 68}" class="notes-sub"><tspan font-weight="600">Checklist Operacional:</tspan> {escape_xml(checklist_preview)}</text>',
            f'  <text x="{left_margin + 16}" y="{notes_top + 90}" class="notes-sub"><tspan font-weight="600">Ação da Equipe:</tspan> Conferir issue aberta automaticamente no repositório <tspan font-family="monospace">BRAN-Org/.github</tspan> para registrar o progresso.</text>',
        ])
    else:
        next_year, next_month, next_tasks = find_next_upcoming_tasks(schedule_data, year, month)
        if next_tasks:
            next_m_name = MONTH_NAMES_PT[next_month]
            next_names = " e ".join([t.get("short_name", t["name"]) for t in next_tasks])
            next_msg = f"Próxima janela programada: {next_m_name} de {next_year} ({next_names})."
        else:
            next_msg = "Nenhuma verificação cadastrada para os próximos meses."

        svg_lines.extend([
            f'  <text x="{left_margin + 16}" y="{notes_top + 28}" class="notes-title">✅ STATUS DA CURADORIA: TUDO EM DIA</text>',
            f'  <text x="{left_margin + 16}" y="{notes_top + 52}" class="notes-body">Nenhuma base de dados da BRAN Org possui conferência de anais ou auditoria crítica programada para {month_name}.</text>',
            f'  <text x="{left_margin + 16}" y="{notes_top + 74}" class="notes-sub">📅 <tspan font-weight="600">{escape_xml(next_msg)}</tspan></text>',
        ])

    # Footer
    footer_y = total_height - 12
    svg_lines.extend([
        '',
        '  <!-- Footer -->',
        f'  <text x="{left_margin}" y="{footer_y}" class="footer-txt">Atualizado automaticamente via GitHub Actions • Fonte canônica: curation-schedule.yml</text>',
        f'  <text x="{card_width - right_margin}" y="{footer_y}" text-anchor="end" class="footer-txt">BRAN Org • Brazilian Research Archive Network</text>',
        '</svg>',
    ])

    svg_content = "\n".join(svg_lines)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Calendário em grade SVG gerado com sucesso em: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Gerador do Calendário Mensal em SVG (Grade Tradicional)")
    parser.add_argument("--schedule", default=DEFAULT_SCHEDULE_PATH, help="Caminho do curation-schedule.yml")
    parser.add_argument("--output", default=DEFAULT_SVG_OUTPUT, help="Caminho de saída do curation-status.svg")
    parser.add_argument("--year", type=int, help="Ano de referência (padrão: ano atual)")
    parser.add_argument("--month", type=int, help="Mês de referência 1-12 (padrão: mês atual)")
    parser.add_argument("--day", type=int, help="Dia de referência (padrão: dia atual)")
    
    args = parser.parse_args()
    
    now = datetime.now()
    year = args.year if args.year is not None else now.year
    month = args.month if args.month is not None else now.month
    day = args.day if args.day is not None else min(now.day, calendar.monthrange(year, month)[1])
    today_date = date(year, month, day)
    
    schedule_data = load_schedule(args.schedule)
    render_calendar_grid_svg(schedule_data, year, month, today_date, args.output)


if __name__ == "__main__":
    main()
