import pandas as pd
from pathlib import Path

INPUT_FILE = Path("sample_data.csv")
OUTPUT_FILE = Path("cleaned_data.csv")
REPORT_FILE = Path("summary_report.txt")


def clean_csv():
    if not INPUT_FILE.exists():
        print(f"Error: {INPUT_FILE} not found.")
        return

    df = pd.read_csv(INPUT_FILE)

    original_rows = len(df)
    missing_before = int(df.isna().sum().sum())

    # Remove duplicate records
    df = df.drop_duplicates()
    duplicates_removed = original_rows - len(df)

    # Clean column names and text fields
    df.columns = df.columns.str.strip()
    for column in df.select_dtypes(include="str").columns:
        df[column] = df[column].map(
            lambda value: value.strip() if isinstance(value, str) else value
        )

    # Save cleaned data without inventing missing values
    df.to_csv(OUTPUT_FILE, index=False)

    report = [
        "CSV DATA CLEANING REPORT",
        "=" * 30,
        f"Input file: {INPUT_FILE}",
        f"Original rows: {original_rows}",
        f"Rows after cleaning: {len(df)}",
        f"Duplicate rows removed: {duplicates_removed}",
        f"Missing cells detected: {missing_before}",
        "",
        "Missing values by column:",
        df.isna().sum().to_string(),
        "",
        f"Cleaned file: {OUTPUT_FILE}",
    ]

    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    clean_csv()

