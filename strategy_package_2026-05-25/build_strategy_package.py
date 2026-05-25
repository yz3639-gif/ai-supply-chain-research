#!/usr/bin/env python3
from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "strategy_package_2026-05-25"
CHARTS = PACKAGE / "charts"
DATA = PACKAGE / "data_snapshot"
PROCESSED = ROOT / "realtime_data_pipeline" / "data" / "processed"


ALLOCATION = [
    ("核心确认仓", 45, "#2563eb"),
    ("光通信事件仓", 20, "#0891b2"),
    ("回撤等待现金", 27, "#64748b"),
    ("冷门期权仓", 8, "#f59e0b"),
]

ACTION_ROWS = [
    ("SMTC", "光通信事件", "财报前不追；财报后看 beat/raise/margin/FCF", "高预期"),
    ("MOD", "电力散热", "等待 Q4/FY2026，强确认后优先", "中性位置"),
    ("POWL", "电力电气", "事实强但不追，等订单兑现或回撤", "质量观察"),
    ("FORM", "AP/HBM test", "等企稳，低于 EMA20 后看重新站回", "active watch"),
    ("VECO", "InP/设备", "订单强验证，等收入和毛利传导", "active watch"),
    ("POET", "光通信期权", "只按里程碑小仓，等样品/量产/复购", "期权仓"),
    ("AXTI", "InP 材料", "位置过热，不追，等冷却和风险确认", "高波动"),
    ("PPSI", "微型电力", "只观察订单转收入和现金流", "不追"),
]


def main() -> None:
    CHARTS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)

    global_summary = read_csv(PROCESSED / "global_market_theme_summary_latest.csv")
    global_context = read_csv(PROCESSED / "global_market_context_latest.csv")
    technicals = read_csv(PROCESSED / "technical_indicators_latest.csv")
    prices = read_csv(PROCESSED / "prices_latest.csv")

    copy_snapshot("global_market_theme_summary_latest.csv")
    copy_snapshot("global_market_context_latest.csv")
    copy_snapshot("technical_indicators_latest.csv")
    copy_snapshot("prices_latest.csv")
    copy_snapshot("model_ingest_latest.csv")

    write_global_chart(global_summary)
    write_technical_chart(technicals)
    write_allocation_chart()
    write_execution_matrix()
    write_report(global_summary, global_context, technicals, prices)
    write_index()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def copy_snapshot(filename: str) -> None:
    src = PROCESSED / filename
    dst = DATA / filename
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")


def num(value: Any, default: float = 0.0) -> float:
    try:
        if value in {None, ""}:
            return default
        return float(value)
    except ValueError:
        return default


def pct(value: Any) -> str:
    value_num = num(value)
    return f"{value_num:+.2f}%"


def fmt(value: Any, digits: int = 2) -> str:
    return f"{num(value):.{digits}f}"


def svg_header(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,"Noto Sans CJK SC",sans-serif;} .title{font-size:24px;font-weight:700;fill:#0f172a}.sub{font-size:13px;fill:#475569}.label{font-size:12px;fill:#334155}.small{font-size:11px;fill:#64748b}.value{font-size:12px;font-weight:600;fill:#0f172a}</style>',
    ]


def write_global_chart(rows: list[dict[str, str]]) -> None:
    fresh_rows = [row for row in rows if row.get("freshness") == "fresh_today"]
    fresh_rows.sort(key=lambda row: num(row.get("avg_pct_from_prev_close")), reverse=True)
    chart_rows = fresh_rows[:10]
    width, height = 1120, 620
    left, top, bar_h, gap = 260, 92, 26, 14
    max_value = max([num(row.get("avg_pct_from_prev_close")) for row in chart_rows] + [1])
    scale = 720 / max_value
    svg = svg_header(width, height)
    svg.append('<text x="32" y="42" class="title">全球市场外部确认强度</text>')
    svg.append('<text x="32" y="66" class="sub">只统计 fresh_today 的市场组；条形为相对前收平均涨跌。</text>')
    for idx, row in enumerate(chart_rows):
        y = top + idx * (bar_h + gap)
        value = num(row.get("avg_pct_from_prev_close"))
        color = "#16a34a" if row.get("interpretation") == "positive_external_confirmation" else "#64748b"
        svg.append(f'<text x="32" y="{y + 18}" class="label">{escape(row.get("group", ""))}</text>')
        svg.append(f'<rect x="{left}" y="{y}" width="{max(2, value * scale):.1f}" height="{bar_h}" rx="5" fill="{color}"/>')
        svg.append(f'<text x="{left + value * scale + 10:.1f}" y="{y + 18}" class="value">{value:+.2f}%</text>')
        svg.append(f'<text x="900" y="{y + 18}" class="small">{escape(row.get("theme_signal", ""))}</text>')
    svg.append('</svg>')
    (CHARTS / "global_theme_confirmation.svg").write_text("\n".join(svg), encoding="utf-8")


def write_technical_chart(rows: list[dict[str, str]]) -> None:
    sorted_rows = sorted(rows, key=lambda row: num(row.get("close_vs_ema20_pct")), reverse=True)
    width, height = 1120, 620
    left, top, bar_h, gap = 180, 94, 26, 15
    values = [num(row.get("close_vs_ema20_pct")) for row in sorted_rows]
    max_abs = max([abs(value) for value in values] + [1])
    zero_x = 520
    scale = 500 / max_abs
    svg = svg_header(width, height)
    svg.append('<text x="32" y="42" class="title">技术位置：相对 EMA20 的偏离</text>')
    svg.append('<text x="32" y="66" class="sub">红色表示 BOLL %b ≥ 0.9 或相对 EMA20 偏离过大，适合触发 no-trade 检查。</text>')
    svg.append(f'<line x1="{zero_x}" y1="86" x2="{zero_x}" y2="{height - 40}" stroke="#cbd5e1" stroke-width="1"/>')
    for idx, row in enumerate(sorted_rows):
        y = top + idx * (bar_h + gap)
        ticker = row.get("ticker", "")
        value = num(row.get("close_vs_ema20_pct"))
        boll_b = num(row.get("boll20_percent_b"))
        risk = boll_b >= 0.9 or value >= 20
        color = "#dc2626" if risk else "#2563eb" if value >= 0 else "#64748b"
        x = zero_x if value >= 0 else zero_x + value * scale
        w = abs(value * scale)
        svg.append(f'<text x="32" y="{y + 18}" class="label">{escape(ticker)}</text>')
        svg.append(f'<rect x="{x:.1f}" y="{y}" width="{max(2, w):.1f}" height="{bar_h}" rx="5" fill="{color}"/>')
        svg.append(f'<text x="{zero_x + value * scale + (10 if value >= 0 else -78):.1f}" y="{y + 18}" class="value">{value:+.2f}%</text>')
        svg.append(f'<text x="910" y="{y + 18}" class="small">BOLL %b {boll_b:.2f} / {escape(row.get("trend_state", ""))}</text>')
    svg.append('</svg>')
    (CHARTS / "technical_position_ema_boll.svg").write_text("\n".join(svg), encoding="utf-8")


def write_allocation_chart() -> None:
    width, height = 900, 420
    x0, y0 = 52, 116
    total_width = 700
    svg = svg_header(width, height)
    svg.append('<text x="32" y="42" class="title">AI 供应链风险预算配置</text>')
    svg.append('<text x="32" y="66" class="sub">这是主题风险预算，不是总资产配置；核心思想是留出现金等事件确认和回撤。</text>')
    current_x = x0
    for label, value, color in ALLOCATION:
        w = total_width * value / 100
        svg.append(f'<rect x="{current_x:.1f}" y="{y0}" width="{w:.1f}" height="58" rx="8" fill="{color}"/>')
        svg.append(f'<text x="{current_x + 12:.1f}" y="{y0 + 35}" fill="#ffffff" font-size="15" font-weight="700">{escape(label)} {value}%</text>')
        current_x += w
    legend_y = 235
    for idx, (label, value, color) in enumerate(ALLOCATION):
        y = legend_y + idx * 34
        svg.append(f'<rect x="54" y="{y - 16}" width="18" height="18" rx="4" fill="{color}"/>')
        svg.append(f'<text x="84" y="{y}" class="label">{escape(label)}：{value}%</text>')
    svg.append('</svg>')
    (CHARTS / "strategy_allocation.svg").write_text("\n".join(svg), encoding="utf-8")


def write_execution_matrix() -> None:
    width, height = 1180, 520
    svg = svg_header(width, height)
    svg.append('<text x="32" y="42" class="title">标的执行矩阵</text>')
    svg.append('<text x="32" y="66" class="sub">先判断证据，再判断价格；市场表现只决定执行节奏，不构成买入理由。</text>')
    headers = ["Ticker", "方向", "动作", "当前标签"]
    xs = [40, 160, 350, 920]
    y = 105
    svg.append(f'<rect x="32" y="{y - 26}" width="1100" height="36" rx="6" fill="#f1f5f9"/>')
    for x, header in zip(xs, headers, strict=False):
        svg.append(f'<text x="{x}" y="{y}" class="value">{escape(header)}</text>')
    for idx, row in enumerate(ACTION_ROWS):
        y = 150 + idx * 42
        fill = "#ffffff" if idx % 2 == 0 else "#f8fafc"
        svg.append(f'<rect x="32" y="{y - 25}" width="1100" height="34" fill="{fill}"/>')
        for x, value in zip(xs, row, strict=False):
            svg.append(f'<text x="{x}" y="{y}" class="label">{escape(value)}</text>')
    svg.append('</svg>')
    (CHARTS / "execution_matrix.svg").write_text("\n".join(svg), encoding="utf-8")


def write_report(
    global_summary: list[dict[str, str]],
    global_context: list[dict[str, str]],
    technicals: list[dict[str, str]],
    prices: list[dict[str, str]],
) -> None:
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tech_by_ticker = {row["ticker"]: row for row in technicals}
    price_by_ticker = {row["ticker"]: row for row in prices}
    hot = [
        row for row in technicals
        if num(row.get("boll20_percent_b")) >= 0.9 or num(row.get("close_vs_ema20_pct")) >= 20
    ]
    hot_names = ", ".join(row["ticker"] for row in hot) or "无"
    lines = [
        "# AI 供应链综合策略包",
        "",
        f"生成时间：{generated_at}  ",
        "定位：把实时事件、全球市场上下文、EMA/BOLL 技术位置和 v3.4 no-trade 纪律合成一份可执行策略。  ",
        "说明：这是研究框架，不是个人投资建议。",
        "",
        "## 一句话结论",
        "",
        "方向继续看多 `光通信上游 + 电力/散热 + AP/HBM test`，但执行上不追最热票。当前最优动作是保留现金，等 SMTC/MOD 财报和美股恢复交易后的价格确认。",
        "",
        "## 图 1：全球市场外部确认",
        "",
        "![全球市场外部确认](charts/global_theme_confirmation.svg)",
        "",
        "解读：日本半导体设备、测试、光纤线缆，以及台湾 AI 硬件是今天最强外部确认。韩国和欧洲数据如果是 `stale`，不能当作当天新信号。",
        "",
        "## 图 2：EMA/BOLL 技术位置",
        "",
        "![技术位置](charts/technical_position_ema_boll.svg)",
        "",
        f"当前需要特别防追高的标的：`{hot_names}`。这些标的不是方向错，而是位置已经不便宜，需要事件确认或回撤。",
        "",
        "## 图 3：风险预算配置",
        "",
        "![风险预算配置](charts/strategy_allocation.svg)",
        "",
        "建议把 AI 供应链主题风险预算拆成：核心确认仓 45%、光通信事件仓 20%、回撤等待现金 27%、冷门期权仓 8%。同一风险簇超过 35% 自动降权。",
        "",
        "## 图 4：标的执行矩阵",
        "",
        "![执行矩阵](charts/execution_matrix.svg)",
        "",
        "## 当前分层策略",
        "",
        "| 桶 | 标的/方向 | 当前动作 |",
        "|---|---|---|",
        "| 核心确认仓 | MOD, POWL, FORM, VECO | 等公司级确认和合适技术位置，优先处理 MOD/VECO/FORM |",
        "| 光通信事件仓 | SMTC, VECO, POET, MTSI/MXL watch | SMTC 财报前不追；财报后看 beat/raise/margin/FCF |",
        "| 回撤等待现金 | 全部高热标的 | 等回到 EMA20 或 BOLL %b 0.4-0.7 |",
        "| 冷门期权仓 | POET, AXTI, PPSI | 小仓/观察，只有 milestone 才升级 |",
        "",
        "## 技术纪律",
        "",
        "- 高于或接近 BOLL 上轨，且没有新的 A/B 级公司事实：不加仓。",
        "- 距 EMA20 超过 20%：默认触发 `NT01 valuation/price extension`。",
        "- 低于 EMA20 但基本面未破坏：进入等待企稳区，而不是立刻否定 thesis。",
        "- 冷门票只按里程碑处理，不按故事补仓。",
        "",
        "## 最新价格与技术表",
        "",
        "| Ticker | Close | EMA20偏离 | BOLL %b | Trend | 动作 |",
        "|---|---:|---:|---:|---|---|",
    ]
    action_map = {
        "SMTC": "财报前不追",
        "MOD": "等财报确认",
        "POWL": "等回撤/兑现",
        "FORM": "等企稳",
        "VECO": "active watch",
        "POET": "期权仓",
        "AXTI": "不追",
        "PPSI": "不追",
    }
    for ticker in ["SMTC", "MOD", "POWL", "FORM", "VECO", "POET", "AXTI", "PPSI"]:
        tech = tech_by_ticker.get(ticker, {})
        price = price_by_ticker.get(ticker, {})
        lines.append(
            f"| {ticker} | {price.get('close', tech.get('close', ''))} | "
            f"{pct(tech.get('close_vs_ema20_pct'))} | {fmt(tech.get('boll20_percent_b'))} | "
            f"{tech.get('trend_state', '')} | {action_map.get(ticker, '')} |"
        )
    lines.extend(
        [
            "",
            "## 全球市场摘要",
            "",
            "| 主题组 | 新鲜度 | 平均前收涨跌 | 解读 |",
            "|---|---:|---:|---|",
        ]
    )
    for row in global_summary:
        lines.append(
            f"| {row.get('group','')} | {row.get('fresh_count','')}/{row.get('count','')} | "
            f"{pct(row.get('avg_pct_from_prev_close'))} | {row.get('interpretation','')} |"
        )
    lines.extend(
        [
            "",
            "## 数据快照",
            "",
            "本 folder 已保存生成时使用的数据快照：",
            "",
            "- `data_snapshot/global_market_theme_summary_latest.csv`",
            "- `data_snapshot/global_market_context_latest.csv`",
            "- `data_snapshot/technical_indicators_latest.csv`",
            "- `data_snapshot/prices_latest.csv`",
            "- `data_snapshot/model_ingest_latest.csv`",
        ]
    )
    (PACKAGE / "综合策略报告_2026-05-25.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index() -> None:
    lines = [
        "# Strategy Package 2026-05-25",
        "",
        "打开 `综合策略报告_2026-05-25.md` 查看连图带字的综合策略。",
        "",
        "## 文件结构",
        "",
        "- `综合策略报告_2026-05-25.md`：主报告。",
        "- `charts/`：SVG 图表。",
        "- `data_snapshot/`：生成报告时使用的数据快照。",
        "- `build_strategy_package.py`：重新生成本 folder 的脚本。",
    ]
    (PACKAGE / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def escape(value: Any) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


if __name__ == "__main__":
    main()
