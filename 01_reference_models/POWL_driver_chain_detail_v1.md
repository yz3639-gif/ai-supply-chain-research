# POWL Driver Chain Detail v1

日期：2026-05-25  
用途：把 Powell Industries 的数据中心订单从“故事”拆成可验证 driver chain。  
说明：这是研究和交易框架，不是个人投资建议。

## 1. Trigger Event

事实：

- Powell FY2026 Q2 release 披露：Q2 revenue `$297M`，gross profit `$88M` 或 revenue 的 `29.6%`，new orders `$490M`，backlog `$1.8B`。
- 同一公告披露：Q2 获得一个超过 `$75M` 的 data center mega order；季度结束后又获得一个超过 `$400M` 的 data center mega order，涉及 behind-the-meter on-site generation assets。
- 同一公告也提示 backlog 可能因合同调整、取消或 scope reduction 而不完全等同未来收入。

来源：<https://powellindustriesinc.gcs-web.com/news-releases/news-release-details/powell-industries-announces-second-quarter-fiscal-2026-results>

可信度：

| 项目 | 可信度 | 原因 |
|---|---:|---|
| >$400M order 存在 | 高 | 官方新闻稿披露 |
| order 最终转收入 | 中 | backlog 有取消/调整风险 |
| 18-24 个月交付节奏 | 低到中 | 模型假设，非公司明确披露 |
| 毛利提升 | 低到中 | 受项目 mix、扩产成本、执行效率影响 |

## 2. Driver Chain

### Driver 1: 订单转收入周期

披露事实：订单金额超过 `$400M`，但公司没有披露具体 delivery schedule。  
模型假设：base case 按 18-24 个月分批转收入，bull case 转化更快且有 follow-on orders，bear case 因客户交付、scope、成本或工程周期延迟。

执行监控：

- Q3 FY2026 backlog 是否明确纳入该订单。
- book-to-bill 是否维持 `>1.2x`。
- 管理层是否披露交付窗口、项目 milestone、客户 scope 变化。

### Driver 2: 产能与执行

不可声称：公司没有披露“产能利用率 85% 到 92%”这种内部数据。  
可用代理：

- backlog 增速。
- book-to-bill。
- gross margin。
- working capital 与项目 milestone 收款。
- management 对 capacity investment 的 return discipline 描述。

base case：backlog 可见性改善，但扩产成本与项目复杂度抵消一部分规模收益。  
bull case：新增产能和 mix 改善同时发生，gross margin 保持 `>=30%`。  
bear case：扩产和工程成本吞掉规模收益，gross margin 跌破 `27%`。

### Driver 3: 毛利桥

起点：Q2 FY2026 gross margin `29.6%`。  
base case：高 20% 区间维持，模型用 `27%-30%`。  
bull case：项目 mix 和产能吸收优于预期，`>=30%`。  
bear case：项目成本、扩产启动、供应链或客户议价导致 `<27%`。

关键点：订单大不自动等于毛利上升。只有当 backlog 转收入且毛利没有恶化，才算真正验证。

## 3. Bear/Base/Bull 方向

| 情景 | 触发 | 证伪 |
|---|---|---|
| Bear | 订单转化延迟、项目成本超预期、GM 跌破公司近期同口径水平 | backlog/order conversion 弱化 |
| Base | >$400M 订单纳入 backlog/revenue bridge，GM 维持近期高 20% 水平 | GM 明显恶化或管理层提示 scope/cancellation |
| Bull | follow-on data-center orders，book-to-bill 继续强，GM 没被扩产成本吞掉 | 两季内无 repeat validation |

估值使用原则：

- EV/EBITDA：对比 MOD、AAON、VRT、ETN、FIX 的数据中心电力/散热相关重估区间，但给小公司执行折扣。
- P/E：用于校验周期性订单兑现后的 normalized earnings。
- FCF yield：用于防止 backlog 增长但现金流被 working capital 长期吞噬。
- 不把单点 target price 当成决策依据；只有当 trigger 被验证、估值仍合理、组合风险允许时，才讨论仓位。

## 4. 决策规则

加仓条件：

- Q3 把 `>$400M` 订单纳入 backlog 或给出交付 schedule。
- book-to-bill `>1.2x` 或 backlog 继续增长。
- gross margin `>=27%`，且管理层不把 margin pressure 解释为结构性 pricing/mix。

降级条件：

- gross margin `<27%` 且非 temporary。
- backlog/order language 弱化。
- 管理层明确提示 cancellation、scope reduction 或客户延迟。
- FCF 连续恶化且无法用项目 milestone 解释。
