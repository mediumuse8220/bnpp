# utils_llm.py

import os
import json
import re
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL = "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def extract_fields_with_llm(term_sheet_text):
    prompt = f"""
Extract and return only a valid JSON object with the following fields from the term sheet text:
ISIN, Issuer, Coupon, Notional, Currency, SettlementDate.
If a field is missing, use null. Do not include any explanation. Use the exact keys specified.

Term Sheet Text:
\"\"\"{term_sheet_text}\"\"\"
"""
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": MODEL
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if not response.ok:
        raise RuntimeError(f"LLM API Error: {response.status_code} {response.text}")
    response_json = response.json()
    # Expected to be a dict with ["choices"][0]["message"]["content"]
    content = response_json["choices"][0]["message"]["content"]

    # Extract JSON block from model output
    json_match = re.search(r"\{[\s\S]+\}", content)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except Exception as exc:
            print("Could not parse JSON:", exc)
            print("Model output:", content)
            return None
    print("Could not find JSON in LLM output.")
    print("Model output:", content)
    return None

if __name__ == "__main__":
    # For direct testing: python utils_llm.py <txt_file>
    import sys
    if len(sys.argv) < 2:
        print("Usage: python utils_llm.py <path_to_text_file>")
        exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        text = f.read()
    result = extract_fields_with_llm(text)
    print(json.dumps(result, indent=2))
