# Company Model Notes v1

日期：2026-05-25  
用途：解释 v3 公司模型的可信度分层和使用限制。  
说明：这是研究框架，不是个人投资建议。

## Tier 1

`POWL / MOD / AAON / SMTC / MTSI / COHU` 有较明确的财报、guidance、订单、backlog 或收入桥。可以做 bear/base/bull，并输出具体 target。target 仍是研究区间，不是保证收益。

## Tier 2

`FORM / ONTO / CAMT / VECO / KLIC / AEHR` 有强订单或行业逻辑，但客户份额、订单分配、转收入节奏需要推导。模型必须带 error band，不能把客户转单或份额变化写成事实。

## Tier 3

`POET / LWLG / ALMU / PPSI / NEO.TO / IQE.L` 是期权仓。用里程碑概率和生存概率管理，不做 DCF，不预测精确 2026 revenue。

## 使用原则

- 所有 target 都必须回到 trigger 和 falsification signal。
- 如果 trigger 没发生，不因股价上涨而上调模型。
- 如果 falsification signal 出现，先降仓再重算。
- POWL 的 `>$400M` 数据中心订单是官方披露；交付节奏、毛利传导和估值重估是模型假设，必须用 backlog、book-to-bill、gross margin 和 FCF 后续验证。
- SMTC/MOD 的事件阈值必须使用公司自身披露口径：SMTC 用 adjusted GM `52.8% +/-50bp`；MOD 用 Climate Solutions GM `24.8%` 和 data-center `50%-70%` growth target，不使用无来源的统一毛利阈值。

## v3.2 降级说明

`company_driver_based_models_v1.csv` 中的 bear/base/bull 概率和 target 区间保留为历史研究材料，不再作为默认决策依据。  
默认使用 `lean_decision_system_v1.md`：先判断事件是否 beat、outlook 是否 raise、thesis 是否有新证据、margin/FCF 是否健康、组合风险是否允许。只有这些问题通过后，估值模型才进入第二步。
