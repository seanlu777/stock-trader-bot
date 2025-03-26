from dotenv import load_dotenv
from trader_bot.db import get_connection
from trader_bot.report import pair_trades

load_dotenv()

conn = get_connection()
if conn:
    print("✅ 連線資料庫成功")
    conn.close()
else:
    print("❌ 連線資料庫失敗")


# scripts/test_pair.py


sample_data = [
    ("0056", "2025-03-01", "buy", 36.0, 1000, "ta"),
    ("0056", "2025-03-10", "sell", 38.0, 1000, "ta"),
    ("00878", "2025-03-05", "buy", 21.5, 2000, "ml"),
]

result = pair_trades(sample_data)

for row in result:
    print(row)
