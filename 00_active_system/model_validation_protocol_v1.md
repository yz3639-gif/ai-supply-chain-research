# Model Validation Protocol v1

日期：2026-05-25  
用途：定义如何判断 AI 供应链模型是否真的有效。  
说明：这是研究框架，不是个人投资建议。

## 1. 三层有效性

不要再问“模型准不准”这种过大的问题。拆成三层：

| 层级 | 问题 | 通过标准 |
|---|---|---|
| Direction | 主题方向是否有效？ | 主题篮子在 20/60/120 日跑赢 QQQ 或 SMH |
| Company Alpha | 公司选择是否有效？ | 个股跑赢同主题篮子，且 thesis 被验证 |
| Execution | 执行时点是否有效？ | 事件前/后动作改善收益或降低回撤 |

只有三层都通过，才可以说模型有投资 edge。

## 2. 每个事件必须记录的收益

`prospective_event_ledger_v2.csv` 必须补齐：

- individual_return
- theme_basket_return
- QQQ_return
- SMH_return
- alpha_vs_theme

计算：

`alpha_vs_theme = individual_return - theme_basket_return`

如果个股上涨但 `alpha_vs_theme <= 0`，不能说公司选择有效，只能说主题 beta 有效。

## 3. 信息质量规则

| 等级 | 信息类型 | 是否可触发投资动作 |
|---|---|---|
| A | 官方订单、backlog、guide、10-Q/10-K | 可以进入事件账本 |
| B | 客户/供应商交叉验证、行业报告、产品认证、样品/量产 | 可以进入事件账本或强观察 |
| C | 管理层泛泛语言、媒体报道、sell-side 评论 | 只能观察 |
| D | 论坛、传闻、无来源 market share | 不进入决策 |

## 4. 样本门槛

在以下条件满足前，不允许声称模型有准确率：

- 至少 20 个前瞻事件。
- 至少 4 个主题。
- 单一主题不超过样本 40%。
- 单一公司不超过 3 个事件。
- 每个事件都有事前 thesis 和证伪条件。

## 5. 10 个事件复盘

每 10 个事件做一次小复盘：

- 哪些 no-trade 条件真正避免了损失？
- 哪些 early signals 被确认？
- 哪些 early signals 是噪音？
- 哪些事件只是主题 beta，不是公司 alpha？
- 是否出现 thesis drift？
- 哪些字段没有被持续填写？

## 6. 删除规则

删除不是失败，是模型优化。

- 连续 10 个事件没有贡献的字段删除。
- 经常事后才填的字段删除。
- 不能改变行为的字段删除。
- 只会制造确定感的字段删除。
