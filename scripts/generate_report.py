import os
import csv
from datetime import date
from trader_bot.report import fetch_trades, pair_trades


def generate_csv_report(report_type="executed", start_date="2025-01-01", end_date=None):
    if not end_date:
        end_date = date.today().isoformat()

    print(f"📊 產生 {report_type} 報表：{start_date} → {end_date}")
    rows = fetch_trades(report_type, start_date, end_date)
    if not rows:
        print("⚠️ 查無交易資料")
        return

    paired = pair_trades(rows)

    # 建立 reports 資料夾
    os.makedirs("reports", exist_ok=True)
    filename = f"reports/{date.today().isoformat()}_交易報表.csv"

    with open(filename, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=paired[0].keys())
        writer.writeheader()
        writer.writerows(paired)

    print(f"✅ 已匯出報表：{filename}")


if __name__ == "__main__":
    # CLI 預設執行
    generate_csv_report()
