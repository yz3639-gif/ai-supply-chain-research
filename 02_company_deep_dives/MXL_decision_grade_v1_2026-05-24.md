# MXL 决策级攻破 v1

日期：2026-05-24  
标的：MaxLinear (`MXL`)  
结论先行：**现在不是无条件买入。只适合事件仓/回撤仓。若 Q2/Q3 把 optical data center revenue 从 $150M-$170M 上修到 $200M+，或 Rushmore/Annapurna 明确进入量产 socket，才升级。**

## 1. 投资命题

`MXL` 的命题不是“光模块涨所以 MXL 涨”，而是：

AI 数据中心的瓶颈从光模块成品继续往上游迁移到 **800G/1.6T optical DSP、200G TIA、224G copper retimer**。如果 `MXL` 能从 Keystone 800G ramp 过渡到 Rushmore 1.6T 和 Annapurna 224G scale-up retimer 量产，它会从旧通信芯片股重估为 AI interconnect platform。

但市场已经开始重估。`MXL` 60 日涨幅约 +453%，当前不是早期未发现阶段。

## 2. 官方证据底稿

### Q1 2026 数据

来源：[MXL Q1 2026 press release](https://investors.maxlinear.com/press-releases/detail/607/maxlinear-inc-announces-first-quarter-2026-financial)

- Q1 2026 revenue：$137.2M，同比 +43%。
- Infrastructure：$62.8M，同比 +136%，占收入 46%。
- Broadband：$43.6M，同比 +7%，占收入 32%。
- Connectivity：$18.6M，同比 -8%，占收入 14%。
- Industrial/multi-market：$12.2M，同比 +47%，占收入 9%。
- Q2 revenue guide：$160M-$170M。
- GAAP gross margin 57.5%，non-GAAP gross margin 61.3%。

### 10-Q 关键点

来源：[MXL Q1 2026 10-Q](https://investors.maxlinear.com/all-sec-filings/content/0001288469-26-000029/mxl-20260331.htm)

- Q1 revenue 包含 high-speed optical interconnect solutions sold into optical modules for data-center, metro and long-haul networks。
- Infrastructure 增长来自 high-performance analog products、optical、wireless backhaul/access products 的 shipment volume 上升。
- 2026Q1 一个客户占 revenue 13%，前十大客户合计 56%。
- 产品主要发往亚洲，2026Q1 shipped to Asia 占 77%，其中香港 48%、中国大陆 10%。
- 客户 qualification 通常 6 个月以上，volume production 往往还要再过 6 个月以上。
- 公司没有长期采购承诺，客户主要按 purchase order 采购。

## 3. 产品线拆解

| 产品 | 角色 | 当前阶段 | 对投资命题的意义 |
|---|---|---|---|
| Keystone | 400G/800G PAM4 DSP | 量产/ramp | 2026 revenue 的核心支撑 |
| Rushmore | 1.6T 200G/lane PAM4 DSP | sampling/commercial availability | 2027 bull case 核心 |
| Annapurna | 224G scale-up retimer | announced/sampling engagement | 决定 MXL 能否从 optical 切到 scale-up copper |
| Washington | 200G TIA | availability | 若与 DSP 形成 chipset attach，提升 ASP 和粘性 |

产品来源：

- [Keystone 800G DSP](https://investors.maxlinear.com/press-releases/detail/497/maxlinear-announces-production-availability-of-5nm-keystone)
- [Rushmore 1.6T DSP](https://www.maxlinear.com/news/press-releases/2025/maxlinear-unveils-rushmore%E2%84%A2-low-power-1-6t-pam4-dsp-for-ai-ml-and-data-center-networks)
- [Annapurna 224G retimer](https://www.maxlinear.com/news/press-releases/2026/maxlinear-unveils-annapurna-224g-scale-up-retimer-to-extend-copper-connectivity-in-ai-data-centers)
- [Washington 200G TIA](https://investors.maxlinear.com/press-releases/detail/608/maxlinear-announces-availability-of-washington-200g-tia-for)

## 4. Revenue Bridge

详表：[MXL_revenue_model_v1_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/MXL_revenue_model_v1_2026-05-24.csv)

### 2026E

| 情景 | Q1 | Q2 | Q3 | Q4 | FY Revenue | Optical DC Revenue | 判断 |
|---|---:|---:|---:|---:|---:|---:|---|
| Bear | 137.2 | 160 | 140 | 130 | 567.2 | <150 | Q2 仅达下限，ramp 失败 |
| Base | 137.2 | 165 | 185 | 205 | 692.2 | 150-170 | 当前指引兑现，无额外惊喜 |
| Bull | 137.2 | 165 | 230 | 275 | 807.2 | 200+ | H2 step-up，光互连上修 |

### 2027E

| 情景 | Revenue | Infrastructure | Optical DC | 判断 |
|---|---:|---:|---:|---|
| Bear | 600 | 240 | 150-180 | Keystone 成熟，1.6T/224G 无大 ramp |
| Base | 850 | 470 | 250-320 | Keystone + Rushmore ramp，Annapurna 初步贡献 |
| Bull | 1100 | 700 | 400+ | MXL 被市场定义为 AI interconnect platform |

## 5. 估值判断

当前市值约 $8.9B，TTM P/S 约 17.5x。

这意味着：

- 2026 base revenue $692M，对应 current P/S 约 12.8x。
- 2027 base revenue $850M，对应 current P/S 约 10.4x。
- 若 2027 bull revenue $1.1B，current P/S 约 8.1x，才显得合理甚至便宜。

所以，**MXL 当前价格要求 2027 至少进入 base-to-bull 之间**。只兑现 2026 指引不够。

## 6. 客户链与竞争格局

详表：[MXL_competitor_customer_map_v1_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/MXL_competitor_customer_map_v1_2026-05-24.csv)

关键事实：

- 公司未点名 hyperscaler。
- 2026Q1 单一客户占 13%，前十大客户 56%。
- 销售主要发往亚洲 ODM/模块/合约制造链。
- 客户没有长期采购承诺，按 PO 采购。
- qualification + production ramp 周期长。

主要竞争：

- Optical DSP：Broadcom、Marvell、Credo、客户自研。
- TIA/driver/PMD：Semtech、MACOM、Broadcom。
- AEC/retimer：Credo、Astera、Broadcom、Marvell。

**独供置信度：低。**  
MXL 的 bull case 不是独供，而是多客户设计赢单扩大。

## 7. 财务质量

Q1 working capital 初看比 ACMR 干净：

- Accounts receivable / Q1 revenue = 0.30x。
- DSO 粗算约 26.8 天。
- Inventory / Q1 COGS = 1.47x。
- DIO 粗算约 132.5 天。

解释：

- AR 没明显雷。
- Inventory 和 wafer prepayment 偏高，但 10-Q 解释为支持 data-center product demand。
- 下一季必须看 Q2 revenue 是否跳升，否则库存/预付款从正面信号变成风险。

## 8. 触发器

### 升级触发

1. 2026 optical data center revenue 从 $150M-$170M 上修到 $200M+。
2. Rushmore 1.6T 获明确 production customer / module program。
3. Annapurna 224G retimer 被 scale-up fabric / AEC 平台采用。
4. Infrastructure revenue 连续两季环比高增长。
5. 毛利保持 60% non-GAAP 附近，库存没有继续失控。

### 降级触发

1. Q2 revenue 低于 $160M 或 Q3 guide 不继续增长。
2. Optical DC revenue 仍停在 $150M-$170M，没有上修。
3. Infrastructure 增长被证明主要是 telecom/backhaul recovery，而不是 AI optical。
4. Inventory/wafer prepayment 继续升但 revenue 没跟。
5. Broadcom/Marvell/Credo/Astera 抢走关键 sockets。

## 9. 决策

### 当前评级：等待 / 事件仓，不追高

理由：

- 产业逻辑强。
- Q1 数据强。
- 产品线覆盖 optical + copper，方向对。
- 但股价已经提前重估。
- Base case 不能支撑显著上行。
- 客户链和 2027 ramp 还不够硬。

### 可以买的情况

- 回撤后 valuation 回到 2027 base revenue 8x sales 附近，同时 Q2/Q3 指引不坏。
- 或 Q2/Q3 明确上修 optical data center revenue 到 $200M+。

### 可以加仓的情况

- Rushmore/Annapurna 进入 production socket。
- Infrastructure revenue 连续两季超预期。
- 2027 revenue bridge 从 $850M base 向 $1.1B bull 迁移。

### 必须止错的情况

- Q2/Q3 guide 断档。
- Optical ramp 未上修。
- 库存继续堆积而 revenue 不跳。
- 竞争者公开拿走主要 1.6T/224G sockets。

## 10. 结论一句话

`MXL` 是 AI 供应链从光模块成品向 DSP/TIA/retimer 轮动的关键样本，但当前已经不是“低位提前埋伏”。  
**现在最理性的动作是：等待验证或回撤，保留事件仓，不升确认仓。**

