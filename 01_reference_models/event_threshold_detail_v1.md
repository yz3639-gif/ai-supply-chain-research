# Event Threshold Detail v1

日期：2026-05-25  
用途：把事件 checklist 的阈值落到公司级数字，避免用同一条毛利线套所有公司。  
说明：这是研究和执行框架，不是个人投资建议。

## 阈值原则

1. 如果公司给出 gross margin guide，用 guide midpoint 做 pass 线，guide low-end 做警戒线。
2. 如果公司没有给出可比 guide，用最近公开披露的同口径 segment/company margin 做基线，低于基线 100bp 以上必须解释。
3. 如果毛利压力来自扩产、启动成本、短期 mix，标记 `temporary_margin_pressure`，交易动作最多降一档。
4. 如果毛利压力来自价格竞争、客户议价、结构性 mix 恶化，标记 `structural_margin_pressure`，不允许因为 headline beat 加仓。
5. 第三层市场确认只能影响执行节奏，不允许替代第一层和第二层的基本面信号。

## SMTC: 2026-05-26 Q1 FY2027

来源：

- Semtech FY2026 Q4 results：Q1 FY2027 guide 为 net sales `$283M +/- $5M`，adjusted gross margin `52.8% +/- 50bp`。
- Semtech Q1 FY2027 event notice：2026-05-26 盘后发布并开 call。

阈值：

| 项目 | Pass | Caution | Fail | 说明 |
|---|---:|---:|---:|---|
| Revenue | `>$288M` | `$283M-$288M` | `<$283M` | $288M 是 Q1 guide 上沿 |
| Adjusted GM | `>=52.8%` | `52.3%-52.8%` | `<52.3%` | 52.8% 是 guide midpoint，52.3% 是 low-end |
| Order/backlog | 公开披露 1.6T/3.2T 或 Signal Integrity 增强 | 只给泛泛 demand strong | 无增强或弱化 | SMTC 不稳定披露 1.6T/3.2T backlog，所以不能编造 backlog 增速 |
| AI/data-center language | 明确提到 800G/1.6T/3.2T optical/copper interconnect 加速 | 语言持平 | 语言弱化 | 只算第一层一项 |

重要纠偏：`31.5%/32%` 不是 Semtech 的适用阈值。SMTC 使用官方 adjusted GM guide 口径，即 `52.8%` pass，`52.3%` fail line。若财报只披露 GAAP GM，则必须转回公司 non-GAAP adjusted GM 口径再比较。

交易含义：

- `Revenue >$288M + GM >=52.8% + Q2 guide 强 + 无结构性毛利压力`：证据变强，有资格考虑加仓；仓位大小另由估值、相关性和风险预算决定。
- `Revenue beat 但 GM 52.3%-52.8%`：只有在 call 明确为 temporary capacity cost 时才允许继续观察或小幅调整，不机械加仓。
- `GM <52.3% 且解释为 pricing/mix`：降级或保持，不因股价上涨追买。

## MOD: 2026-05-26/27 Q4 FY2026

来源：

- Modine Q3 FY2026 results：Climate Solutions sales `$544.6M`，data center sales `+78% YoY`，Climate Solutions gross margin `24.8%`，公司称未来两年 data center sales 目标为 `50%-70%` 年增长。
- Modine Q4 FY2026 event notice：2026-05-26 盘后发布，2026-05-27 9:00am CT call。

阈值：

| 项目 | Pass | Caution | Fail | 说明 |
|---|---:|---:|---:|---|
| Data-center growth/outlook | FY2027 outlook >=50% growth 或 Q4 data-center growth >=50% YoY | 增速 35%-50% 但 FY2027 仍强 | FY2027 data-center outlook <50% | 50% 来自公司 Q3 披露的未来两年目标下沿 |
| Climate Solutions GM | 不低于 24.8% 基线 100bp 以上 | 低 50-100bp 且为 temporary expansion cost | 低于 23.8% 且为 pricing/mix | 用 Q3 公开同口径 baseline；不硬塞 29.5% |
| Backlog/order | backlog/order 或 capacity expansion commentary 增强 | 语言持平 | 明确订单延迟或客户推迟 | 只用公开披露，不估算未披露 backlog 月数 |
| FCF/working capital | 不因扩产导致 FCF 持续恶化 | 季度性库存/AR 升高 | FCF 明显恶化且无交付解释 | 数据中心扩产常伴随 working capital 拉升，需区分短期和结构性 |

重要纠偏：`29.5%` 只有在公司披露了可比 segment/company gross margin 指标且其历史基线支持时才可使用。目前 v3.1 使用 Modine Q3 FY2026 披露的 Climate Solutions gross margin `24.8%` 作为同口径基线。

交易含义：

- `FY2027 data-center growth >=50% + margin 压力为 temporary + backlog/order 增强`：证据变强，有资格考虑加仓；仓位大小另由组合风险决定。
- `增长强但 margin 明确受价格/mix 压制`：不加仓，优先等待下一季验证。
- `data-center outlook <50% 或 FCF 恶化无解释`：降级，事件仓不释放。
