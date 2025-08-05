# reconcile.py
import os
from parse_term_sheet import extract_term_sheet_fields
from parse_booking_extract import parse_booking_file
import csv
import sys

FIELDS = ["ISIN", "Issuer", "Coupon", "Notional", "Currency", "SettlementDate"]

def reconcile_records(llm_data, booking_data):
    results = []
    for field in FIELDS:
        llm_val = llm_data.get(field) if llm_data else None
        book_val = booking_data.get(field) if booking_data else None
        results.append({
            "Field": field,
            "LLM_Extracted": llm_val,
            "Booking_Extract": book_val,
            "Match": str(llm_val == book_val)
        })
    return results

def write_report(matches, out_path='reconciliation_report.csv'):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=matches[0].keys())
        writer.writeheader()
        writer.writerows(matches)

if __name__ == "__main__":
    ts_fp = sys.argv[1]
    booking_fp = sys.argv[2]
    llm_fields = extract_term_sheet_fields(ts_fp)
    booking_fields = parse_booking_file(booking_fp)
    results = reconcile_records(llm_fields, booking_fields)
    write_report(results)
    print(f"Reconciliation complete. Output: reconciliation_report.csv")
