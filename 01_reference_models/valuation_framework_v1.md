# Valuation Framework v1

日期：2026-05-25  
用途：把入场价、目标价和估值方法绑定，避免只给价格不解释。  
说明：这是研究框架，不是个人投资建议。

## Tier 1

- `POWL`：EV/EBITDA 和 P/E 为主。$235-$245 bear/reset，$325-$360 base，$420-$480 bull。
- `MOD`：EV/EBITDA 为主。$220-$240 bear/reset，$300-$330 base，$380-$450 bull。
- `AAON`：EV/EBITDA 和 growth premium。$98-$105 reset，$155-$170 base，$190-$220 bull。
- `SMTC`：EV/Sales 和 gross margin 稳定性。$102-$115 reset，$180-$200 base，$230-$260 bull。
- `MTSI`：EV/Sales 和 high-margin analog premium。$280-$305 reset，$440-$480 base，$540-$600 bull。
- `COHU`：EV/Sales 和 operating recovery。$38-$40 reset，$55-$60 base，$70-$80 bull。

## Tier 2

使用目标区间，不用单点：FORM $100-$220、ONTO $225-$400、CAMT $145-$270、VECO $45-$95、KLIC $80-$165、AEHR $68-$190，具体区间见 `company_driver_based_models_v1.csv`。

## Tier 3

不做 DCF，不给单点 fair value。用里程碑概率 x payoff range；价格上涨但里程碑没发生，要减仓。
