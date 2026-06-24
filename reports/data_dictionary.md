# Mutual Fund Analytics Platform - Data Dictionary

## 1. Fund Master (01_fund_master.csv)

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company name |
| scheme_name | Text | Name of mutual fund scheme |
| category | Text | Equity, Debt, etc. |
| sub_category | Text | Large Cap, Mid Cap, Small Cap, etc. |
| plan | Text | Direct or Regular |
| risk_category | Text | Risk level of scheme |

---

## 2. NAV History (02_nav_history.csv)

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme identifier |
| date | Date | NAV date |
| nav | Decimal | Net Asset Value |

---

## 3. Investor Transactions (08_investor_transactions.csv)

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Integer | Investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme identifier |
| transaction_type | Text | SIP, Lumpsum, Redemption |
| amount_inr | Decimal | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| kyc_status | Text | KYC verification status |

---

## 4. Scheme Performance (07_scheme_performance.csv)

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme identifier |
| return_1yr_pct | Decimal | One year return |
| return_3yr_pct | Decimal | Three year return |
| return_5yr_pct | Decimal | Five year return |
| alpha | Decimal | Excess return over benchmark |
| beta | Decimal | Market sensitivity |
| sharpe_ratio | Decimal | Risk adjusted return |
| sortino_ratio | Decimal | Downside risk adjusted return |
| expense_ratio_pct | Decimal | Annual expense ratio |
| aum_crore | Decimal | Assets under management |

---

## Source References

- AMFI India
- mfapi.in
- Bluestock Mutual Fund Dataset