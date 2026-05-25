# Bottleneck Index Methodology v1

日期：2026-05-25  
用途：定义瓶颈指数的固定权重、数据质量和降级规则。  
说明：这是研究框架，不是个人投资建议。

## v3.2 状态修正

瓶颈指数降级为研究仪表盘，不再作为买入、加仓、减仓触发器。  
原因：当前权重没有经过足够大样本验证；`walk_forward_backtest_results_v1.csv` 只说明部分主题方向可以被公开信息解释，不能证明指数有稳定择时能力。

使用边界：

- 可以用来提示“哪个供应链环节值得继续研究”。
- 不可以用来决定仓位。
- 不可以把 `score >=70` 解释为交易信号。
- 不可以声称固定权重已证明有效。

## 固定权重

| 因子 | 权重 | 数据类型 | 说明 |
|---|---:|---|---|
| 需求增速 | 30% | revenue/orders/capex demand | 使用公开收入、订单、订单语言、行业需求报告做代理 |
| 供给扩张 | 25% | capacity/capex/supply | 使用 capex、产能扩张、产线、交付计划做代理 |
| 交期/backlog/order coverage | 20% | backlog/book-to-bill/orders | 电力和设备链优先使用 backlog；光通信使用订单/guide/产品放量语言 |
| Capex/BOM 占比 | 15% | capex mix/BOM mix | 使用公开 capex 指引、行业 BOM 区间和管理层 capex commentary |
| 价格/毛利/ASP 信号 | 10% | GM/ASP/pricing | 使用毛利、ASP、价格压力、产品 mix 指标 |

Q&A 语言只写在 `qualitative_note`，不单独加权。若未来需要量化，必须从价格/毛利项中拆出，最高 5%。

## 权重校准

当前权重不是声称唯一正确，而是先固定成可复盘版本，再用公开转折点做稳定性校准。`bottleneck_weight_calibration_v1.csv` 对比了当前 `30/25/20/15/10` 与替代 `35/25/15/15/10`：

- 2023Q4 和 2024Q2 GPU 期，两套权重均识别为主瓶颈。
- 2024Q3 HBM/AP 期，两套权重均识别为潜在瓶颈，但因为 `hard_data_ratio <70%` 不升为主瓶颈。
- 2024Q4 光通信期，替代权重会让分数刚过 70，但 `hard_data_ratio=58%` 阻止其被标为主瓶颈。
- 2026Q1 光通信和电力散热因公开订单、guide、backlog 更硬，才允许标记主瓶颈。

因此当前权重的作用是保持信号稳定，不是追求最高后验拟合。若未来改权重，必须新增同样格式的校准文件，不能只口头调整。

## Factor score 与贡献分

每个因子先归一化到 0-100，再乘以固定权重得到贡献分。原始数据不能直接相加。

例：NVDA 或供应链 guide 的高增长若处在历史极端分位，需求因子可以归一化为 85-95 分；它不是把 YoY 增速 40% 直接填成 40 分。

贡献分计算：

`factor_contribution = normalized_factor_score × factor_weight`

最终：

`score_0_100 = demand_contribution + supply_contribution + backlog_contribution + capex_bom_contribution + price_margin_contribution`

详见 `bottleneck_weight_calibration_v1.csv` 的贡献列。

## 评分和主瓶颈判定

- `score >= 70` 且 `hard_data_ratio >= 70%`：强瓶颈。
- `score >= 70` 且 `50% <= hard_data_ratio < 70%`：潜在强瓶颈。
- `55 <= score < 70`：观察瓶颈。
- `score < 55`：非主瓶颈或衰退。
- `hard_data_ratio < 50%`：不得标记为主瓶颈。

`hard_data_ratio` 按因子硬度加权计算，不按资料数量计算。官方收入、毛利、订单、backlog、book-to-bill、明确 guidance 的硬度为 1.0；官方但无法完全拆分的代理数据为 0.5；传闻、泛泛 Q&A 和无来源 market share 为 0。详见 `hard_data_ratio_rules_v1.md`。

## 盲区处理

GPU 月度产能、真实 hyperscaler 内部订单、真实交付优先级不可稳定公开获得，因此不构建 GPU 月度供需缺口，不用不可见订单惩罚 walk-forward 模型。
