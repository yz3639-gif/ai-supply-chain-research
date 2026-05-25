# CAMT 决策级攻破 v1

日期：2026-05-24  
标的：Camtek (`CAMT`)  
结论先行：**CAMT 是比 ACMR 更接近“决策级 AI 先进封装设备标的”的公司，但当前不是舒服买点。公司证据很硬：AI/HPC 约 50% 收入，先进封装合计约 70%，Q1 2026 OSAT 订单超过 $90M，Hawk 从 tier-1 IDM 拿到 $45M AI 应用订单；问题是市值约 $7.7B，2026 base P/S 已接近 13x，必须要求 2026H2 强兑现和 2027 接近 $750M target model。**

## 1. 投资命题

`CAMT` 的命题是：

**AI 先进封装从“有没有 CoWoS/HBM 产能”进一步进入“每一层、每一个微凸点、每一次混合键合/堆叠都要检测和计量”的良率瓶颈。**

在高价值 AI package 里，一个坏 die 或一个微凸点异常就会毁掉昂贵封装。  
因此 inspection/metrology 从后段辅助工具升级为 known-good-die / known-good-package 的关键控制点。

与 ACMR 相比：

- ACMR 押的是湿法/ECP/PLP 工艺扩张，弹性大但中国和现金流质量折价重。
- CAMT 押的是先进封装检测/计量，证据更清晰、客户更全球化、利润率更高，但估值已经显著重估。

## 2. 官方证据底稿

### Q1 2026

来源：[Camtek Q1 2026 results](https://www.camtek.com/news-and-events/camtek-announces-results-for-the-first-quarter-of-2026/)

- Q1 revenue：$121.7M，同比 +2.5%。
- Q2 revenue guide：$129M-$131M。
- 公司预计 2026H2 revenue 较 2026H1 增长超过 25%。
- GAAP gross margin：50.1%；non-GAAP gross margin：51.0%。
- GAAP operating margin：22.4%；non-GAAP operating margin：25.5%。
- Cash/deposits/marketable securities：$849.7M。
- Q1 operating cash flow：$3.1M。
- 管理层称 Q1 incoming orders unprecedented，并显著提高对 2026 剩余时间和 2027 的信心。

### 20-F 业务证据

来源：[Camtek 2025 Form 20-F](https://www.sec.gov/Archives/edgar/data/1109138/000117891326001561/zk2634678.htm)

- 约 50% revenue 来自支持 AI applications 的产品。
- 增长来自 HBM 和 advanced packaging 相关 equipment demand。
- Camtek systems 覆盖 Advanced Packaging、Chiplets、HBM、compound semiconductors、memory、CIS、power、RF、MEMS。
- 对 HBM，Camtek 表述为提供 stack 组件的 100% inspection and metrology，以确保 known-good-package。
- 2025 年 Asia Pacific 占 revenue 91%，China 占 49%。
- 2025 年一个客户占 revenue 11%；2024 年三个客户分别占 15%、10%、10%。

### Investor deck 关键点

来源：[Camtek May 2026 investor presentation](https://www.camtek.com/wp-content/uploads/Camtek_Investors_MAY26.pdf)

- AI/HPC 约 50% revenue。
- Non-AI advanced packaging 约 20% revenue。
- Other applications 约 30% revenue。
- Advanced packaging 合计约 70% revenue。
- Advanced packaging market expected growth rate 30%-40%。
- Hawk 设计用于 Chiplets、HBM、Hybrid Bonding；支持 150nm defect detection 和 500M micro-bumps inspection/metrology。
- Hawk 2026 revenue 占比预计超过 50%。
- 中期 target model：revenue $750M、gross margin 54%-55%、operating margin 33%-35%。

## 3. 订单验证

来源：[Camtek $31M OSAT order](https://www.camtek.com/news-and-events/camtek-receives-31-million-multi-system-order-from-a-leading-osat/)

- 2026 年 3 月，Camtek 获得 leading OSAT 的 $31M multi-system order。
- 订单主要用于 CoWoS-like packaging supporting AI applications。
- 加上该订单，Q1 2026 来自 leading OSATs 的订单已超过 $90M，多数用于类似应用。
- 系统预计 2026 年内交付。

来源：[Camtek $25M Hawk IDM order](https://www.camtek.com/news-and-events/camtek-receives-multiple-hawk-systems-order-of-approximately-25-million-from-an-idm-for-ai-applications/)

- 2026 年 2 月，Camtek 获得 tier-1 IDM 的 $25M Hawk systems order。
- 同一 IDM 近几个月已有一系列 smaller repeating orders，累计 Hawk orders 达 $45M。
- Hawk 面向 HBM、chiplets、hybrid bonding、front-end applications 和最高 500M micro-bumps wafers。

这两组订单是 CAMT 最硬的证据：

1. OSAT 订单验证 CoWoS-like AI packaging。
2. IDM repeat orders 验证 Hawk 高端平台。
3. 订单指向 2026H2 revenue step-up。

但还缺两个关键点：

1. 客户没有点名。
2. 订单强度是否可延续到 2027 还需验证。

## 4. Revenue Bridge

详表：[CAMT_revenue_model_v1_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/CAMT_revenue_model_v1_2026-05-24.csv)

### 2026E

| 情景 | Q1 | Q2 | Q3 | Q4 | FY Revenue | 判断 |
|---|---:|---:|---:|---:|---:|---|
| Bear | 121.7 | 130 | 135 | 140 | 526.7 | H2 兑现弱，订单转收入慢 |
| Base | 121.7 | 130 | 155 | 170 | 576.7 | H2 较 H1 增约 29%，符合公司“>25%”信号 |
| Bull | 121.7 | 131 | 175 | 205 | 632.7 | Hawk/OSAT 订单显著拉动，H2 超预期 |

### 2027E

| 情景 | Revenue | 条件 | 判断 |
|---|---:|---|---|
| Bear | $600M | 2026 订单潮正常化，AP/China 周期回落 | 不足以支撑当前估值 |
| Base | $700M | 接近但未达到 $750M target model，AI/AP 维持 ~70% | 好公司，取决于买入价格 |
| Bull | $800M | Hawk 多客户扩散，软件/服务 attach 增强，operating margin 34% | 可确认，但当前估值已在预支 |

## 5. 估值判断

来源：[StockAnalysis CAMT quote](https://stockanalysis.com/stocks/camt/)

- 2026-05-22 收盘价：$167.37。
- Market cap：约 $7.71B。
- Shares outstanding：约 46.04M。
- TTM revenue：约 $499M。
- Q1 2026 cash/securities：$849.7M。
- 2025 年底 convertible notes net：约 $520M。

粗略 EV：$7.71B + $0.52B - $0.85B = $7.38B。

| 情景 | Revenue | Market cap / sales | EV / sales | 判断 |
|---|---:|---:|---:|---|
| 2026 bear | $527M | 14.6x | 14.0x | 太贵 |
| 2026 base | $577M | 13.4x | 12.8x | 需要强兑现 |
| 2026 bull | $633M | 12.2x | 11.7x | 仍不便宜 |
| 2027 base | $700M | 11.0x | 10.5x | 高质量 premium，但空间有限 |
| 2027 bull | $800M | 9.6x | 9.2x | 才开始显得合理 |

结论：CAMT 是高质量 AI 先进封装设备股，但价格已经不是“市场没理解”。  
它需要持续 beat，并且 2027 接近/超过 $750M target model 才能支撑更大上行。

## 6. 客户链与竞争

详表：[CAMT_competitor_customer_map_v1_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/CAMT_competitor_customer_map_v1_2026-05-24.csv)

客户证据：

- OSAT：Q1 2026 >$90M orders，主要 CoWoS-like AI packaging。
- IDM：tier-1 IDM Hawk repeat orders，累计 $45M。
- 2025 年一个客户占 revenue 11%，说明有大客户但不是极端单一客户。

竞争：

- Onto Innovation：Dragonfly/G5 advanced packaging/HBM inspection/metrology。
- KLA：更大规模 process control/inspection/metrology 平台。
- Nova：advanced metrology。
- Lasertec/其他 niche inspection。
- 中国/台湾本地低端检测设备商在较低端应用价格竞争。

CAMT 的优势：

- 更纯的 advanced packaging/HBM/AI revenue mix。
- Hawk/Eagle G5 产品已形成高端订单。
- 毛利率 50%+，非 GAAP operating margin 25%+。
- 现金充足，业务不像 ACMR 那样被应收/库存严重拖住。

CAMT 的风险：

- 估值已高。
- 2026Q1 revenue 只同比 +2.5%，真正增长要靠 H2。
- China 49%、Asia Pacific 91%，仍有地缘/出口管制/区域冲突风险。
- H2 order-to-revenue conversion 必须顺畅。
- 竞争者资源更强。

## 7. 决策触发器

### 升级触发

1. Q2 revenue 达到或超过 $131M，且 Q3 guide 明确 step-up 到 $150M+。
2. 2026H2 revenue 确认比 H1 增长超过 25%，最好接近 35%-45%。
3. 新增 OSAT/IDM orders 继续出现，尤其是 Hawk repeat orders。
4. management 继续确认 AI/HPC + advanced packaging 约 70% revenue mix。
5. non-GAAP gross margin 保持 51%+，operating margin 从 Q1 25.5% 回升到 28%-30%。
6. Visual Layer / AI software 变成实际产品或服务收入，而不是叙事。

### 降级触发

1. Q3 guide 低于 $145M，说明 H2 step-up 不够。
2. H2 revenue 没达到 H1 +25%。
3. Hawk orders 没有 repeat，OSAT orders 停在 Q1。
4. gross margin 低于 50%，operating margin 继续低于 26%。
5. China/APAC 风险导致订单取消、发货延迟或回款异常。
6. CAMT 继续上涨但 2027 revenue bridge 没有上修，估值脱离基本面。

## 8. 当前评级

### 当前评级：好公司，等待买点；只适合回撤仓/强催化仓

为什么比 ACMR 更接近决策级：

- AI/AP revenue mix 明确。
- 订单金额明确。
- 客户类型明确：leading OSAT、tier-1 IDM。
- 毛利和利润率高。
- 资产负债表强。

为什么仍不直接确认仓：

- 市值约 $7.7B，估值已高。
- 2026Q1 本身增长很低，H2 才是关键。
- 当前价格已经假设 H2 强兑现和 2027 高增长。
- China/APAC 暴露仍然大。

## 9. 可执行规则

### 可以买的情况

- 回撤到 2027 base EV/S 8x-9x 附近，同时 Q2/Q3 guide 不变坏。
- 或 Q2/Q3 新订单继续超预期，且估值没有进一步扩张。

### 可以加仓的情况

- Q3/Q4 revenue step-up 兑现。
- Hawk orders repeat 至第二个/第三个 tier-1 customer。
- operating margin 恢复到 30% 左右。
- 公司把 $750M target model 的时间表从中期拉近到 2027。

### 必须止错的情况

- Q3 guide 不支持 H2 >25%。
- OSAT/IDM orders 没有后续。
- 毛利/运营利润率下滑，说明竞争或成本压力出现。
- 估值继续扩张但收入桥不上修。

## 10. 一句话结论

`CAMT` 是 AI 先进封装检测/计量链条里证据最硬的一批中小型公司之一。  
**但它已经被市场理解了：现在不能用“挖到冷门小公司”的框架买，只能用“强兑现 + 回撤纪律 + 订单延续”的框架买。**
