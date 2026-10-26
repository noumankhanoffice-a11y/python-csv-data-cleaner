# CSV Data Cleaning & Report Generator

A Python automation tool that cleans CSV files and generates a summary report.

## Features
- Removes duplicate rows
- Detects missing values
- Trims extra spaces from text fields
- Exports cleaned CSV data
- Generates a readable summary report

## Technologies
- Python
- Pandas

## How to Run

1. Install Python.
2. Install pandas:

   pip install pandas

3. Place your input file in the project folder as `sample_data.csv`.
4. Run:

   python clean_data.py

## Output Files
- `cleaned_data.csv` — cleaned dataset
- `summary_report.txt` — cleaning summary

## Sample Test Results
- Input rows: 5
- Output rows: 4
- Duplicate rows removed: 1
- Missing cells detected: 1

## Limitations
- Missing values are reported, not automatically filled.
- Duplicate rows are removed only when all column values match.
- Use a backup before processing important business data.
