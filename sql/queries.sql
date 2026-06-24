-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Funds with Expense Ratio below 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 3. Top 5 Funds by Sharpe Ratio

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 4. Top 5 Funds by Alpha

SELECT
    scheme_name,
    alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- 5. Highest AUM Fund House

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 6. Average 1-Year Return by Category

SELECT
    category,
    AVG(return_1yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

-- 7. Average Transaction Amount by State

SELECT
    state,
    AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY state
ORDER BY avg_amount DESC;

-- 8. Transaction Count by Type

SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Investors by KYC Status

SELECT
    kyc_status,
    COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Top States by Investment Amount

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;