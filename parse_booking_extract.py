# parse_booking_extract.py
import os
os.environ["HOME"] = "/tmp"
os.environ["XDG_CONFIG_HOME"] = "/tmp"
os.environ["STREAMLIT_CONFIG_DIR"] = "/tmp/.streamlit"
os.makedirs("/tmp/.streamlit", exist_ok=True)
import sys
import json
import csv

def parse_booking_file(file_path):
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif file_path.endswith(".csv"):
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows:
                return rows[0] # First record (customize as needed)
            return None
    else:
        raise NotImplementedError("File type not supported.")

if __name__ == "__main__":
    input_fp = sys.argv[1]
    print(parse_booking_file(input_fp))