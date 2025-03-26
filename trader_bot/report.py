import pandas as pd
from trader_bot.db import get_connection


def fetch_trades(report_type="executed", start_date=None, end_date=None):
    """
    讀取交易資料（實單 or 模擬）
    """
    table = "executed_trades" if report_type == "executed" else "simulated_trades"
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    query = f"""
        SELECT symbol, date, action, price, quantity, strategy
        FROM {table}
        WHERE date BETWEEN %s AND %s
        ORDER BY symbol, date
    """
    cursor.execute(query, (start_date, end_date))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows


def pair_trades(rows):
    """
    配對買賣，計算報酬率
    """
    df = pd.DataFrame(
        rows, columns=["symbol", "date", "action", "price", "quantity", "strategy"]
    )

    results = []
    grouped = df.groupby("symbol")

    for symbol, group in grouped:
        buys = []
        for _, row in group.iterrows():
            if row["action"] == "buy":
                buys.append(row)
            elif row["action"] == "sell" and buys:
                buy = buys.pop(0)  # FIFO 配對
                profit_pct = round(
                    (row["price"] - buy["price"]) / buy["price"] * 100, 2
                )

                results.append(
                    {
                        "股票代碼": symbol,
                        "買進日期": buy["date"],
                        "買進價格": buy["price"],
                        "賣出日期": row["date"],
                        "賣出價格": row["price"],
                        "數量（股）": row["quantity"],
                        "策略類型": row["strategy"],
                        "報酬率（%）": f"{profit_pct:.2f}%",
                    }
                )

        # 留下尚未賣出的部位（未平倉）
        for buy in buys:
            results.append(
                {
                    "股票代碼": symbol,
                    "買進日期": buy["date"],
                    "買進價格": buy["price"],
                    "賣出日期": "—",
                    "賣出價格": "—",
                    "數量（股）": buy["quantity"],
                    "策略類型": buy["strategy"],
                    "報酬率（%）": "—",
                }
            )

    return results
