# Hard Data Ratio Rules v1

日期：2026-05-25  
用途：明确 `hard_data_ratio` 如何计算，避免瓶颈指数被定性语言漂移。  
说明：这是研究框架，不是个人投资建议。

## 计算公式

`hard_data_ratio = Σ(因子权重 × 因子硬度) / Σ(因子权重)`

因子权重固定为：

- 需求增速：30
- 供给扩张：25
- 交期/backlog/order coverage：20
- Capex/BOM 占比：15
- 价格/毛利/ASP：10

因子硬度：

| 硬度 | 定义 | 例子 |
|---:|---|---|
| 1.0 | 官方可复算硬数据 | 财报收入、毛利、FCF、backlog、book-to-bill、官方订单金额、明确 guidance |
| 0.5 | 官方/行业代理数据 | capex/BOM 区间、行业报告、产品出货占比、无法完全拆分的 segment proxy |
| 0.0 | 定性或不可复算 | 管理层泛泛 Q&A、传闻、无来源 market share、未公开客户订单 |

例：如果某主题的五项硬度分别为 `1.0 / 0.5 / 1.0 / 0.5 / 1.0`，则：

`hard_data_ratio = (30×1 + 25×0.5 + 20×1 + 15×0.5 + 10×1) / 100 = 80%`

## 主瓶颈限制

- `hard_data_ratio < 50%`：不得标记主瓶颈。
- `50% <= hard_data_ratio < 70%`：最多标记潜在强瓶颈。
- `hard_data_ratio >= 70%` 且 `score >= 70`：才允许标记主瓶颈。

## 重要修正

指数中的 factor score 是 0-100 归一化分数，不是原始 YoY 增速。  
例如 NVDA guide +40% YoY 不等于 demand factor 40 分；如果它处在历史极端分位，可能归一化为 85-95 分。这样避免把不同单位的变量直接相加。

## 权重校准结论

`bottleneck_weight_calibration_v1.csv` 显示，当前权重与一个合理替代权重 `35/25/15/15/10` 在主要公开转折点上的分类基本一致。唯一边界点是 2024Q4 光通信：替代权重会使分数略过 70，但 `hard_data_ratio=58%` 仍阻止其被标为主瓶颈。这正是 hard data 规则的价值。
