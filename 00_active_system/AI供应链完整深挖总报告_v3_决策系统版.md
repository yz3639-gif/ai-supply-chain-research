# AI供应链完整深挖总报告 v3 决策系统版

日期：2026-05-25  
定位：把 v2 的方向判断升级为可量化、可回测、可复盘、可执行的 AI 供应链决策系统。  
说明：这是研究和交易框架，不是个人投资建议。

## 1. v3 的核心变化

### v3.2 有效性修正

v3.2 承认一个更重要的事实：这套系统尚未被证明能稳定提高投资准确率。`walk_forward_backtest_results_v1.csv` 的样本太少，只能说明部分主题方向可被公开信息解释，不能证明瓶颈指数、权重、三层 checklist 或机械仓位规则有效。

因此默认决策系统改为 lean 版本：

- `framework_validity_audit_v1.md`：审计哪些东西未被证明有效。
- `lean_decision_system_v1.md`：只保留 beat、raise、thesis evidence、margin/FCF、portfolio risk 五个问题。
- `simple_event_checklist_v1.csv`：不使用任意 5% 阈值，不使用机械分数。
- `decision_journal_simple_v1.md`：记录“我当时怎么想、什么会证明我错、后来错在哪”。

旧的瓶颈指数、权重校准、复杂 execution log 和 action lookup table 保留为研究辅助或审计痕迹，不再作为买入、加仓、减仓触发器。

v3 不再试图用不可得的数据构建伪精确模型。GPU 月度产能、hyperscaler 未公开订单、真实交付优先级无法稳定公开获得，因此本版采用三层结构：

1. 公开转折点：标记 GPU、HBM/AP、光通信、电力散热的已验证瓶颈迁移。
2. 固定权重瓶颈指数：在转折点之间监控趋势强弱，不声称提前预测不可见订单。
3. 执行系统：用公司模型、事件 checklist、execution log、walk-forward、相关性和压力测试约束买入、加仓、降级和退出。

## 2. Bottleneck Dashboard

核心文件：

- `bottleneck_turning_points_v1.md`
- `bottleneck_index_methodology_v1.md`
- `bottleneck_weight_calibration_v1.csv`
- `hard_data_ratio_rules_v1.md`
- `bottleneck_dashboard_v1.csv`
- `ai_datacenter_capex_bom_model_v1.csv`

四个公开转折点：

| 转折点 | 时间 | 含义 |
|---|---|---|
| TP1 | 2023Q4-2024Q2 | GPU 主瓶颈 |
| TP2 | 2024Q3 起 | HBM/先进封装接力 |
| TP3 | 2024Q4-2025 | 光通信升温 |
| TP4 | 2024Q4 至今 | 电力散热 backlog 拉长 |

指数固定权重：需求增速 30%、供给扩张 25%、交期/backlog 20%、Capex/BOM 15%、价格/毛利/ASP 10%。Q&A 只做备注。

关键规则：`hard_data_ratio <50%` 不得标记主瓶颈。`score_0_100` 由归一化后的 factor score 乘以权重得到，不把原始 YoY 增速直接相加。当前 `30/25/20/15/10` 权重已用 `bottleneck_weight_calibration_v1.csv` 对比替代权重 `35/25/15/15/10`，分类差异主要出现在 2024Q4 光通信边界点，但 hard-data 门槛会阻止过早标成主瓶颈。

v3.2 修正：瓶颈指数只提示研究方向，不触发交易。

## 3. Company Models

核心文件：

- `company_model_tier_map_v1.csv`
- `company_driver_based_models_v1.csv`
- `company_model_notes_v1.md`
- `POWL_driver_chain_detail_v1.md`
- `competition_tam_proxy_matrix_v1.md`
- `valuation_framework_v1.md`

分层：

| Tier | 公司 | 模型 |
|---|---|---|
| Tier 1 | POWL, MOD, AAON, SMTC, MTSI, COHU | 公开财报/guidance 支撑，bear/base/bull 有具体 target |
| Tier 2 | FORM, ONTO, CAMT, VECO, KLIC, AEHR | 公开数据 + 代理推导，输出 target 区间和 error band |
| Tier 3 | POET, LWLG, ALMU, PPSI, NEO.TO, IQE.L | 不做 DCF，只做 milestone option framework |

最重要的改变：Tier 3 不再写伪精确收入和 DCF。它们只靠样品、量产、复购、融资、客户、现金 runway 升级或降级。

POWL 的 `>$400M` 数据中心订单被拆为两层：订单存在是官方披露，高可信；交付节奏、产能利用率和毛利传导是模型假设。v3.1 不再假装知道内部产能利用率，而用 backlog、book-to-bill、gross margin 和 FCF 作为可观察代理。

## 4. Event Confirmation Checklist

核心文件：

- `simple_event_checklist_v1.csv`
- `event_confirmation_checklists_v1.csv`
- `event_threshold_detail_v1.md`
- `event_action_lookup_table_v1.csv`

三层结构：

1. 基本面信号：revenue、gross margin、backlog/order/bookings、AI/data-center 语言。
2. 管理层前景：下一季 guide、FY guide、具体产品/客户/产能、毛利解释。
3. 市场确认：VWAP/20DMA、分析师上修、同赛道验证。

v3.2 默认使用简单 checklist：是否 beat、是否 raise、thesis 是否有新证据、margin/FCF 是否健康、组合风险是否允许。旧三层表保留为资料库，不再用 “4/4 + 3项” 机械触发交易。第三层市场确认只影响执行节奏，不能单独触发买入。

阈值纠偏：SMTC 使用 Semtech 官方 Q1 FY2027 adjusted gross margin guide `52.8% +/-50bp`，不是 `31.5%/32%` 示例口径。MOD 使用 Q3 FY2026 Climate Solutions gross margin `24.8%` 和 data-center 未来两年 `50%-70%` growth target 做同口径阈值，不硬塞无来源的 29.5%。

仓位规则修正：删除机械 `+20%/+10%/+5%`。事件只决定“证据是否变强/变弱”；仓位大小由估值、相关性、已有暴露、流动性和风险预算决定。

## 5. Execution Log

核心文件：

- `execution_log_schema_v1.csv`
- `execution_log_v1.md`
- `decision_journal_simple_v1.md`

默认只回答五件事：我当时怎么想；什么事实会证明我错；事件后发生什么；我做了什么决定，为什么；30-90 天后错在哪。旧六段式日志降级为历史模板。

## 6. Walk-Forward

核心文件：

- `walk_forward_information_sets_v1.csv`
- `walk_forward_backtest_v1.py`
- `walk_forward_backtest_results_v1.csv`

约束：只使用预测日前公开信息。缺少 demand-side 数据时，置信度上限为 50%。不可见 hyperscaler 突发订单只标记 blind spot，不计入模型失败。

结论拆成两类：

- 公开信息可预测部分。
- 当时无法知道的信息导致的偏差。

这能防止“现在看起来很明显”的后见之明污染回测。

v3.2 修正：当前 walk-forward 只有 5 个主题窗口，不能证明准确率，也不能证明季度级择时有效。它只能作为“公开信息能否解释主题方向”的审计，不是模型有效性的证明。

## 7. Portfolio Risk

核心文件：

- `portfolio_correlation_risk_v1.csv`
- `stress_test_v1.md`
- `bear_case_debate_v1.md`

约束：

- 计算 60/120/252 日滚动相关性。
- 风险簇：optical、power_cooling、AP_HBM、cold_options、China_geopolitical、high_valuation。
- 同一风险簇暴露超过 35% 自动标红。
- SMTC/MTSI/MXL 相关性 >0.75 时，不允许同时升高权重。
- FORM/ONTO/CAMT 相关性 >0.70 时，AP/HBM 组必须降权或用 power/cooling 分散。

压力测试：

压力测试只作为风险语言，不作为收益承诺。此前任何“准确率 55%-60%”或机械目标收益都应视为未验证假设。

## 8. 当前执行含义

v3 的结论不是“买更多”，而是“减少凭感觉买”。

当前主线仍然是：

- 高胜率：光通信、power/cooling、精选 AP/HBM。
- 高赔率：POET/LWLG/ALMU/PPSI/NEO/IQE，但只按里程碑。
- 当前最重要事件：2026-05-26 SMTC、2026-05-26/27 MOD。

如果 SMTC/MOD 的第一层和第二层信号不够强，不能因为股价涨就加仓。如果第一层和第二层同时强，再用第三层决定执行节奏。

## 9. v3 文件清单

- `bottleneck_turning_points_v1.md`
- `bottleneck_index_methodology_v1.md`
- `bottleneck_weight_calibration_v1.csv`
- `hard_data_ratio_rules_v1.md`
- `bottleneck_dashboard_v1.csv`
- `ai_datacenter_capex_bom_model_v1.csv`
- `walk_forward_information_sets_v1.csv`
- `walk_forward_backtest_v1.py`
- `walk_forward_backtest_results_v1.csv`
- `company_model_tier_map_v1.csv`
- `company_driver_based_models_v1.csv`
- `company_model_notes_v1.md`
- `POWL_driver_chain_detail_v1.md`
- `competition_tam_proxy_matrix_v1.md`
- `valuation_framework_v1.md`
- `event_confirmation_checklists_v1.csv`
- `event_threshold_detail_v1.md`
- `event_action_lookup_table_v1.csv`
- `portfolio_correlation_risk_v1.csv`
- `stress_test_v1.md`
- `bear_case_debate_v1.md`
- `execution_log_schema_v1.csv`
- `execution_log_v1.md`
- `framework_validity_audit_v1.md`
- `lean_decision_system_v1.md`
- `simple_event_checklist_v1.csv`
- `decision_journal_simple_v1.md`

一句话：v3.2 把 AI 供应链研究从“复杂但未验证的控制感”压回“少数能持续执行、能复盘、能防止同主题过度下注的规则”。
