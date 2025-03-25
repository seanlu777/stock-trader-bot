-- 1. 股價歷史資料
CREATE TABLE IF NOT EXISTS price_history (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume BIGINT
);

-- 2. 技術指標資料
CREATE TABLE IF NOT EXISTS technical_signals (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    date DATE NOT NULL,
    rsi FLOAT,
    macd FLOAT,
    signal_macd FLOAT,
    ema20 FLOAT,
    ema60 FLOAT,
    bb_upper FLOAT,
    bb_lower FLOAT,
    label_class SMALLINT
);

-- 3. 策略實單交易紀錄
CREATE TABLE IF NOT EXISTS executed_trades (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    date DATE NOT NULL,
    action VARCHAR CHECK (action IN ('buy', 'sell')),
    price FLOAT,
    quantity FLOAT,
    profit_pct FLOAT,
    strategy VARCHAR
);

-- 4. 模擬交易紀錄
CREATE TABLE IF NOT EXISTS simulated_trades (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    date DATE NOT NULL,
    action VARCHAR CHECK (action IN ('buy', 'sell')),
    price FLOAT,
    quantity FLOAT,
    profit_pct FLOAT,
    strategy VARCHAR
);
