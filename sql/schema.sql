-- Dimension Table: Fund

CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT
);

-- Dimension Table: Date

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE UNIQUE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);

-- Fact Table: NAV

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

-- Fact Table: Transactions

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    date_id INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

-- Fact Table: Performance

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

-- Fact Table: AUM

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    aum_crore REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);