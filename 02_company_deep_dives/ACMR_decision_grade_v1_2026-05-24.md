# ACMR 决策级攻破 v1

日期：2026-05-24  
标的：ACM Research (`ACMR`)  
结论先行：**可以放入观察仓/小仓候选，但还不能做确认仓。ACMR 的 AI 先进封装逻辑正在变硬，尤其是 ECP、wafer-level/panel-level packaging 和非中国客户订单；但当前收入仍几乎全来自中国，应收和库存过重，现金流质量不足。真正的升级点不是收入高增长，而是“非中国 advanced packaging repeat orders + shipments 转收入 + OCF 转正”。**

## 1. 投资命题

`ACMR` 的核心命题不是普通“半导体设备国产替代”，而是：

**AI 芯片从 GPU/HBM 瓶颈继续扩散到 CoWoS、2.5D/3D、fan-out、panel-level packaging 时，湿法清洗、ECP、电镀、去胶/湿蚀刻、flux cleaning、panel-level cleaning/plating 等工艺步骤变成先进封装良率瓶颈。**

如果 `ACMR` 能把中国 wet-clean 基本盘扩展成全球 advanced packaging 设备平台，公司会从“中国 WFE 折价股”重估为“AI advanced packaging equipment supplier”。  
但这条路现在只走到 **早期验证**，还没有走到确认阶段。

## 2. 官方证据底稿

### Q1 2026 数据

来源：[ACMR Q1 2026 results](https://ir.acmr.com/news-releases/news-release-details/acm-research-reports-first-quarter-2026-results)

- Revenue：$231.3M，同比 +34.2%。
- Shipments：$240.7M，同比 +53.6%。
- Growth driven by ECP and advanced packaging applications。
- 2026 revenue outlook：$1.08B-$1.175B，维持不变。
- Gross margin：46.4%，处于长期目标 42%-48% 的上半区间。
- Operating income：$36.2M，同比 +40.3%，operating margin 15.6%。
- Cash/restricted cash/short-term time deposits：$1.25B。
- Net cash：$924.2M。

### 产品收入拆分

来源：[ACMR Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1680062/000162828026032842/acmr-20260331.htm)

| 产品类别 | 2026Q1 | 2025Q1 | YoY | 判断 |
|---|---:|---:|---:|---|
| Single wafer cleaning / Tahoe / semi-critical cleaning | $122.5M | $129.6M | -5.5% | 基本盘短期不增长 |
| ECP / furnace / other technologies | $84.2M | $27.6M | +205% | 最强增长点，但 ECP 与其他技术合并披露 |
| Advanced packaging excluding ECP / services / spares | $24.5M | $15.1M | +62% | AP 线索增强 |

这张表很关键：ACMR 不是所有产品都在增长，真正拉动 Q1 的是 ECP/furnace/other 与 AP/services/spares。  
所以投资判断要盯产品 mix，而不是只看总收入。

## 3. 全球 advanced packaging 证据

来源：[ACMR Feb 2026 advanced packaging orders](https://ir.acmr.com/news-releases/news-release-details/acm-research-receives-multiple-advanced-packaging-equipment)

ACMR 披露收到多个全球客户先进封装设备订单：

- Singapore-based leading global OSAT：multiple wafer-level advanced packaging systems，计划 Q1 2026 交付。
- Mainland China 之外的 leading global semiconductor packaging manufacturer：panel-level advanced packaging vacuum cleaning tool，计划 Q1 2026 交付。
- North America-based technology customer：multiple wafer-level advanced packaging systems，计划 2026 稍晚交付。
- 覆盖 coating、developing、wet etching、stripping、cleaning、electroplating。

Q1 2026 业绩稿进一步确认：

- Ultra C vac-p panel-level advanced packaging vacuum cleaning system 已按期交付给 mainland China 之外的 leading global semiconductor packaging manufacturer。
- wafer-level advanced packaging systems 已交付给 Singapore leading OSAT。

这不是传闻，是官方订单/交付证据。  
但仍不是决策级确认，因为还缺：

1. 客户没有点名。
2. 未披露金额。
3. 未证明 repeat orders。
4. 未证明这些订单已形成可持续非中国 revenue。

## 4. 产业卡点位置

行业背景来源：[TrendForce advanced packaging / AI supply chain](https://www.trendforce.com/presscenter/news/20260430-13028.html)、[TrendForce warpage / PLP](https://insights.trendforce.com/p/warpage-in-advanced-packaging)

AI 先进封装瓶颈正在从单纯 CoWoS capacity 扩散到：

- 2.5D/3D packaging capacity。
- substrates、T-glass、PCB、HBM、SSD 等配套资源。
- fan-out / panel-level packaging 的良率与 warpage 控制。
- large package、fine-pitch interconnect、RDL、多层材料带来的清洗/电镀/去胶/残留控制。

ACMR 站的位置：

| 卡点 | ACMR 暴露 | 价值 |
|---|---|---|
| Wafer-level AP wet process | clean / wet etch / strip / ECP | 直接受益于先进封装步骤增多 |
| Panel-level packaging | Ultra C vac-p flux cleaning | 若 FOPLP 从试产走向 AI 量产，弹性大 |
| Panel-level plating | Ultra ECP ap-p | 更远期 bull case |
| HBM / chiplet cleaning | Ultra C vac-p / wet cleaning legacy | 清洗良率约束增强 |
| Global OSAT/foundry AP capex | Singapore OSAT / non-China packaging customer / North America tech customer | 去中国单一暴露的关键路径 |

## 5. 竞争地图

详表：[ACMR_competitor_customer_map_v1_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/ACMR_competitor_customer_map_v1_2026-05-24.csv)

主要竞争不是小公司，而是一线设备厂：

- Lam Research：SABRE/SABRE 3D ECD、SP/DV-Prime/Da Vinci wet clean、Kallisto/Phoenix panel wet processing。
- Tokyo Electron：LITHIUS Pro AP coater/developer、CELLESTA/EXPEDIUS cleaning、Synapse/Ulucus bonding/debonding/thinning。
- SCREEN：single-wafer/batch cleaning。
- Applied Materials、SEMES、SUSS MicroTec、NAURA、Kingsemi 等在相邻步骤或区域市场竞争。

ACMR 的潜在优势：

- 中国本土供应链和服务能力。
- 成本/性能和快速定制。
- wet clean + ECP + AP tools 产品组合扩张。
- 全球客户初始订单打破“只会做中国成熟制程”的叙事。

ACMR 的弱点：

- 在全球先进制程/先进封装大客户中的服务网络和历史信任弱于 Lam/TEL/SCREEN。
- 很多产品仍处于 first-tool / evaluation / acceptance 阶段。
- Panel-level AI packaging 尚未大规模量产，时间可能比股价预期更慢。
- 中国设备厂价格竞争可能压毛利。

## 6. 财务质量排雷

来源：[ACMR Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1680062/000162828026032842/acmr-20260331.htm)

| 指标 | 2026Q1 | 判断 |
|---|---:|---|
| Accounts receivable, net | $526.5M | 对 $231.3M 季度收入而言偏重 |
| Inventories, net | $738.0M | 极重 |
| First-tools at customer locations | $119.5M | 比 2025 年底 $145.5M 下降，但仍大 |
| Operating cash flow | -$29.5M | 负面 |
| Free cash flow | -$52.1M | 负面 |
| Advances from customers | $168.8M | 从 2025 年底 $187.8M 下降 |
| Deferred revenue | $11.0M | 从 2025 年底 $17.4M 下降 |
| Allowance for credit losses | $35.1M | 需持续观察 |

粗算：

- AR / quarterly revenue：约 2.28x。
- Inventory / quarterly COGS：约 5.95x。
- DSO：约 205 天。
- DIO：约 536 天。

解释要公平：设备公司存在 first tool、验收、客户产线导入和发货/收入确认错配，不能按消费品库存逻辑直接判死刑。  
但投资上必须承认：**这不是高质量现金流增长。**

所以 ACMR 的确认仓条件必须比 MXL/HPS 更苛刻：收入增长不够，现金转换必须改善。

## 7. 中国风险和少数股东权益

10-Q 明确披露：

- 2026Q1 substantially all revenue derived from mainland China customers。
- ACM Research 持有 ACM Shanghai 73.6% outstanding shares。
- ACM Shanghai 的 minority holders 分享净利润，公司需要列示 net income attributable to non-controlling interests。

这带来两个估值修正：

1. **中国折价**：如果收入仍几乎全来自 mainland China，即使增长快，也不能给全球 AI advanced packaging multiple。
2. **归母经济折价**： consolidated revenue 不是 100% 归属于 ACMR 股东，做 P/S 时要看 consolidated P/S 和 attributable P/S 两套。

粗略估值：

- 市值约 $4.9B-$5.2B，取中值 $5.0B。
- 2026 base revenue：$1.14B，consolidated P/S 约 4.4x。
- 若按 ACM Shanghai 73.6% 近似归属，2026 attributed sales 约 $839M，attributed P/S 约 6.0x。
- 2027 base revenue：$1.37B，consolidated P/S 约 3.6x。
- 2027 attributed sales 约 $1.01B，attributed P/S 约 5.0x。

结论：ACMR 不再是极低估值。它需要证明 2027 base 以上情景，并且证明全球 AP 订单不是一次性事件。

## 8. Revenue Bridge

详表：[ACMR_revenue_model_v1_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/ACMR_revenue_model_v1_2026-05-24.csv)

### 2026E

| 情景 | Single-wafer clean | ECP/furnace/other | AP/services/spares | Revenue | 判断 |
|---|---:|---:|---:|---:|---|
| Bear | $480M | $350M | $170M | $1.00B | 中国成熟制程为主，现金流继续恶化 |
| Base | $500M | $430M | $210M | $1.14B | 指引兑现，AP 有初步贡献 |
| Bull | $520M | $540M | $240M | $1.30B | 非中国 AP repeat，ECP/PLP 强劲 |

### 2027E

| 情景 | Revenue | 条件 | 判断 |
|---|---:|---|---|
| Bear | $1.05B | 中国 capex 放缓，全球 AP 不 repeat | 避免/退出 |
| Base | $1.37B | ECP/AP 成为更大增长引擎，全球客户部分 repeat | 可中等置信 |
| Bull | $1.65B | 非中国 AP revenue 明确、panel-level 工具生产验证、OCF 改善 | 可升级确认 |

## 9. 决策仪表盘

详表：[ACMR_decision_dashboard_v1_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/ACMR_decision_dashboard_v1_2026-05-24.csv)

### 升级触发

1. Non-China advanced packaging orders 在 Q2/Q3 重复出现，最好来自同一客户追加订单。
2. Shipments-to-revenue 转换正常，first-tools at customer locations 不继续堆高。
3. ECP/furnace/other 和 AP/services/spares 连续两季保持高增长。
4. OCF 转正，或至少 AR/inventory 增速显著低于 revenue 增速。
5. 公司披露 non-China revenue 或 global customer contribution。
6. Gross margin 保持 45%+，没有被中国设备价格战拖下去。

### 降级触发

1. 2026 revenue guide 下修，或 Q2/Q3 显示 back-half 兑现困难。
2. Global AP 订单没有 repeat，只停留在一次性 demo/first-tool。
3. AR、inventory、first-tool inventory 继续上升，OCF 连续两个季度显著为负。
4. gross margin 跌破 42%。
5. 地缘/出口管制/审计/中美风险升级影响客户采购或估值。
6. 竞争者 Lam/TEL/SCREEN 在同类 AP/PLP 工艺中明显压制 ACMR。

## 10. 当前评级

### 当前评级：观察仓 / 小仓候选，不是确认仓

正面足够强：

- Q1 revenue +34.2%，shipments +53.6%。
- ECP/furnace/other +205%，AP/services/spares +62%。
- 全球 AP 订单覆盖 Singapore OSAT、非中国 packaging manufacturer、North America tech customer。
- 先进封装卡点真实存在，ACMR 产品正好踩在湿法/ECP/cleaning/plating 工艺节点上。
- 现金储备强，短期生存风险低。

负面也足够硬：

- 2026Q1 revenue 仍 substantially all mainland China。
- AR 和 inventory 太重。
- OCF/FCF 为负。
- 少数股东权益导致 consolidated revenue 不能 100% 归属于 ACMR。
- 当前估值已经不便宜，市场开始给 AI AP option value。

## 11. 可执行规则

### 可以买的情况

- 只用观察仓/小仓，前提是接受中国风险和营运资本风险。
- 股价回撤到接近 2027 base attributed sales 4x-4.5x，且 Q2/Q3 没有业务恶化。
- 或 Q2/Q3 出现全球 AP repeat order，但价格尚未完全反映。

### 可以加仓的情况

- 非中国 AP 客户 repeat order 明确。
- Q2/Q3 OCF 改善，AR/inventory 不再跑赢收入。
- ECP/AP 两条收入线持续高增长。
- 管理层明确披露 global customer revenue 或 customer acceptance progress。

### 必须止错的情况

- OCF 连续恶化，AR/inventory 继续堆。
- global AP 订单 2-3 个季度没有 follow-up。
- gross margin 进入 42% 以下。
- 2026 guide 下修。
- 中国客户 capex 或监管风险导致订单/回款异常。

## 12. 一句话结论

`ACMR` 是 AI 先进封装湿法/ECP/面板级封装链条里的真实候选，但现在仍是 **“强产业逻辑 + 弱现金流质量 + 中国折价未解除”**。  
**可以观察仓，不可确认仓；确认仓要等全球 AP repeat 与现金转换改善同时出现。**
