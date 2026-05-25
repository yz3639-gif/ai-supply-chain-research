# Optimization Plan v3.3

日期：2026-05-25  
目标：把 AI 供应链研究包从“看起来完整的报告系统”优化为“可验证、可持续、可删错”的前瞻决策流程。  
说明：这是研究框架，不是个人投资建议。

## 1. 总原则

v3.3 不再增加复杂度，先验证有效性。

核心原则：

1. 不新增未经验证的指数、权重和机械仓位规则。
2. 不用单一财报优化整套系统。
3. 不用事后解释证明自己当初对了。
4. 每个判断必须在事件发生前记录。
5. 每 10 个事件复盘一次，没用的规则删掉。
6. 在 20-30 个前瞻事件之前，不声称系统有准确率。

## 2. 优化目标

### 2.1 短期目标

把系统压缩成四个可执行工具：

- `lean_decision_system_v1.md`：最小决策规则。
- `simple_event_checklist_v1.csv`：事件后只回答 5 个问题。
- `decision_journal_simple_v1.md`：写清楚当时怎么想、什么会证明错。
- `prospective_event_ledger_v1.csv`：前瞻事件账本。

### 2.2 中期目标

积累 20-30 个前瞻事件样本，评估：

- 是否比简单 `beat + raise` 基准更好。
- 是否比持有主题篮子更好。
- 是否能降低回撤。
- 是否能避免同主题过度下注。
- 哪些 checklist 项没有预测价值。

### 2.3 长期目标

如果系统有效，再考虑恢复部分模型化工具。  
如果系统无效，只保留它作为风险纪律，不把它当交易 edge。

## 3. 阶段计划

## Phase 0: 冻结旧复杂系统

时间：立即执行。  
目标：防止旧 v2/v3 文件继续制造假确定性。

动作：

- 总报告明确 v3.2/v3.3 为默认规则。
- 旧 target price、方向置信度、机械仓位只作历史研究，不作执行依据。
- `bottleneck_dashboard_v1.csv` 降级为主题温度计。
- `company_driver_based_models_v1.csv` 降级为研究素材，不作买入触发。
- `event_action_lookup_table_v1.csv` 不再含机械 `+20%/+10%` 仓位。

完成标准：

- README 和总报告都指向 lean system。
- 新增事件默认进入前瞻账本，而不是继续写大报告。

## Phase 1: 建立前瞻事件账本

新增文件：`prospective_event_ledger_v1.csv`

字段：

| 字段 | 说明 |
|---|---|
| ticker | 公司代码 |
| theme | optical / power_cooling / AP_HBM / cold_option / other |
| event_date | 事件日期 |
| event_type | earnings / order / guide / product / financing / customer |
| thesis_before_event | 事件前 thesis |
| what_would_prove_wrong | 什么事实会证明错 |
| expected_direction | bullish / neutral / bearish |
| action_before_event | buy / add / hold / reduce / watch |
| result_1d | 事件后 1 日表现 |
| result_20d | 事件后 20 日表现 |
| result_60d | 事件后 60 日表现 |
| result_120d | 事件后 120 日表现 |
| thesis_validated | yes / partial / no / unknown |
| error_type | demand / competition / valuation / execution / timing / unobservable |
| benchmark_result | QQQ / SMH / theme basket 对比 |
| lesson | 下一次要改什么 |

规则：

- 事件前必须填前 8 个字段。
- 事件后再填表现和复盘字段。
- 不允许事件后回写事件前 thesis。

## Phase 2: 简化事件 checklist

每个事件只回答 5 个问题：

1. 结果是否 beat 公司 guide 或市场一致预期？
2. Outlook 是否 raise 或明确变强？
3. Thesis 是否出现新证据？
4. Margin/FCF 是否健康？
5. 组合风险是否允许？

判断原则：

- 不使用固定 `5%` 这类任意阈值。
- 只使用公司 guide、同口径历史数据、市场一致预期或明确披露。
- 如果 3 分钟内写不清“证据为何变强”，默认不加仓。

## Phase 3: 建立基准组

每个事件必须同时记录四个基准：

| 基准 | 用途 |
|---|---|
| Benchmark A: beat + raise | 看 lean system 是否比最简单财报规则更好 |
| Benchmark B: theme basket | 看个股判断是否优于持有主题 |
| Benchmark C: QQQ/SMH | 看是否有市场超额收益 |
| Benchmark D: no action | 看交易是否真的必要 |

核心问题：

如果 lean system 不能跑赢简单基准，就不能称为 edge。

## Phase 4: 20-30 个事件验证

样本要求：

- 至少 20 个事件才做第一次严肃评价。
- 事件覆盖至少 4 个主题：optical、power_cooling、AP_HBM、cold_options。
- 单一主题不超过样本 40%。
- 单一公司不超过 3 个事件。

评价指标：

- 事件后 20/60/120 日相对 QQQ/SMH 表现。
- 正确识别 thesis validation 的比例。
- 避免错误加仓的次数。
- 因相关性约束而避免的损失。
- 与 `beat + raise` 基准相比的差异。

注意：

这里不先设“目标准确率”。  
先收集数据，再看系统有没有用。

## Phase 5: 每 10 个事件删减一次

复盘问题：

- 哪个 checklist 问题最有预测力？
- 哪个问题只是噪音？
- 哪类 bear case 最常成真？
- 错误主要来自基本面误判，还是估值已经反映？
- 是系统有用，还是主题 beta 带来的收益？

删减规则：

- 连续 10 个事件没有贡献的字段删除。
- 无法稳定填写的字段删除。
- 只能事后解释、不能事前记录的字段删除。
- 让决策更慢但没有改善结果的字段删除。

## 4. 模块保留/降级/删除标准

| 模块 | 当前状态 | 保留条件 | 删除/降级条件 |
|---|---|---|---|
| Lean checklist | 默认使用 | 能帮助避免错误加仓 | 如果与简单 beat+raise 没差异 |
| Decision journal | 默认使用 | 能解释错误来源 | 如果不持续填写 |
| Correlation guardrail | 默认使用 | 能减少同主题集中损失 | 如果只是提示但不改变行为 |
| Bear case | 默认使用 | 能提前发现失败路径 | 如果变成形式主义 |
| Bottleneck index | 研究辅助 | 能提示主题研究方向 | 如果被误用为交易信号 |
| Driver model | 研究素材 | 能帮助理解 revenue bridge | 如果继续产生伪精确 |
| Target price | 次要辅助 | 与估值分位和事件证据结合 | 如果替代了事件判断 |

## 5. 下一个具体动作

1. 新建 `prospective_event_ledger_v1.csv`。
2. 把未来 30-60 天内可观察事件放进去。
3. 先跑 5 个事件作为试运行，不评价准确率。
4. 到 10 个事件时做第一次小复盘。
5. 到 20-30 个事件时决定系统是否有 edge。

## 6. 成功标准

v3.3 成功不是因为文件更多，而是因为：

- 事件前记录变得更诚实。
- 错误能被归因。
- 同主题过度下注减少。
- 不再被伪精确数字诱导。
- 系统能被证伪。

如果做不到这些，就说明它不是决策系统，只是研究笔记。
