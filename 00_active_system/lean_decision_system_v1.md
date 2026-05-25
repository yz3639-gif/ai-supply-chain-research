# Lean Decision System v1

日期：2026-05-25  
用途：把 AI 供应链研究系统压缩成可持续执行的最小决策框架。  
说明：这是研究框架，不是个人投资建议。

## 核心原则

1. 不使用无法验证的精确数字。
2. 不使用任意阈值，除非来自公司 guide、历史同口径数据或市场一致预期。
3. 不让任何单一财报主导整套系统。
4. 不用机械仓位百分比代替判断。
5. 所有买入、加仓、减仓都必须能写成一句话：为什么现在证据更强或更弱。

## 最小事件 Checklist

每个事件只回答 5 个问题：

| 问题 | Pass | Fail | 说明 |
|---|---|---|---|
| 结果是否 beat？ | 高于公司 guide 或市场一致预期 | 低于 guide 或 consensus | 使用当时公开口径，不自设阈值 |
| Outlook 是否 raise？ | 下一季/FY guide 上调，或管理层明确提高需求/订单展望 | guide 下调或语言转弱 | 不用固定 5% |
| Thesis 是否被验证？ | 出现订单、backlog、客户、产品、量产、复购等新证据 | 核心 thesis 没有新证据或被反证 | 主题语言不等于公司证据 |
| Margin/FCF 是否健康？ | 符合公司 guide/历史口径，或压力明确为短期 | 结构性价格/mix/成本压力，或现金流恶化无解释 | 毛利阈值必须公司化 |
| 组合风险是否允许？ | 同主题不过度集中，估值不极端 | 相关性/估值/流动性风险过高 | 防止同一风险簇叠仓 |

## 决策规则

| 事件结果 | 默认动作 |
|---|---|
| beat + raise + thesis 新证据 + margin/FCF 没坏 + 组合风险允许 | 有资格加仓，但仓位大小另行由组合风险决定 |
| beat 但没有 raise 或没有 thesis 新证据 | 保持或小幅调整，不追 |
| miss 或 guide 下调 | 降级复查 |
| thesis 被反证 | 减仓或退出 |
| 只有股价强、分析师上修、VWAP 守住 | 不构成买入理由，只影响执行节奏 |

## 使用方式

每次财报或订单事件后，只填一行 `simple_event_checklist_v1.csv`，再在 `decision_journal_simple_v1.md` 写一段复盘。  
如果 3 分钟内写不清“为什么证据更强”，就默认不加仓。

## 对旧 v3 系统的处理

- `bottleneck_dashboard_v1.csv`：只用于看主题温度，不用于交易。
- `bottleneck_weight_calibration_v1.csv`：只说明权重敏感性，不说明预测有效。
- `event_confirmation_checklists_v1.csv`：保留为详细资料库，但默认执行使用 `simple_event_checklist_v1.csv`。
- `event_action_lookup_table_v1.csv`：不再使用机械仓位百分比。
- `execution_log_schema_v1.csv`：降级为历史模板，默认用简单日志。
