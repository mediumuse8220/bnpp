# LLM-powered Term Sheet Reconciliation

## Overview

This project automates the extraction of key bond data fields from unstructured term sheets (PDF, TXT) using an open-source LLM, and reconciles them against structured booking system records (CSV, JSON). The goal is to simplify reconciliation, audit, and onboarding of new trades in capital markets workflows.

---

## Features

- Parse and extract term sheet text from PDF/TXT
- Use an LLM (Hugging Face API or local) to extract fields: ISIN, Issuer, Coupon, Notional, Currency, SettlementDate
- Parse structured booking data (CSV/JSON)
- Field normalization and robust comparison
- Generate `reconciliation_report.csv`, showing matches and mismatches

---

## Architecture Diagram

## Project Structure

├── parse_term_sheet.py        # Extract term fields from unstructured doc using LLM

├── parse_booking_extract.py   # Load structured record

├── reconcile.py               # Compare, normalize, and generate reconciliation CSV

├── utils_llm.py               # Utilities for calling LLM (Hugging Face API or local)

├── requirements.txt           # Python dependencies

├── README.md                  # This file!

├── sample_data/

│   ├── example_termsheet.pdf

│   ├── example_booking.json

│   └── example_booking.csv

---

## Setup

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd <your-repo-directory>
 
2. **Install dependencies**
  pip install -r requirements.txt

3. **Set your Hugging Face API token (required for LLM extraction)**
   export HF_API_TOKEN=your_token_here

## Usage
# Reconciliation (main workflow)
 python reconcile.py sample_data/example_termsheet.pdf sample_data/example_booking.json
or with a CSV booking extract:

 python reconcile.py sample_data/example_termsheet.pdf sample_data/example_booking.csv

| Field          | LLM_Extracted               | Booking_Extract              | Match |
|----------------|----------------------------|------------------------------|-------|
| ISIN           | NO0010894330               | NO0010894330                 | TRUE  |
| Issuer         | Genel Energy Finance Ltd    | Genel Energy Finance Ltd     | TRUE  |
| Coupon         | 9.25                       | 9.25                         | TRUE  |
| Notional       | 3000000                    | 3000000                      | TRUE  |
| Currency       | USD                        | USD                          | TRUE  |
| SettlementDate | 2020-10-14                 | 2020-10-14                   | TRUE  |


## Example Term Sheet and Booking Files
* Provided in sample_data/ folder for demonstration purposes.
  You can replace with your own files as needed.
## Notes
No cloud deployment instructions are provided; all scripts are designed for local machine execution.

For detailed workflow and design: See report.md.

Field normalization: Minor formatting differences (spaces, %, "USD" vs "usd", date formats) are handled automatically.

