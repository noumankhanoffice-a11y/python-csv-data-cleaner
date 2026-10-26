# CSV Data Cleaning & Report Generator

A lightweight Python automation tool that cleans CSV datasets, identifies data-quality issues, and generates a summary report. Designed to reduce repetitive manual data-cleaning work.

## Features

- Removes duplicate rows
- Detects and reports missing values
- Trims extra whitespace from text fields
- Exports cleaned data to a new CSV file
- Generates a readable text summary report

## Technologies

- Python
- Pandas

## Project Structure

```text
Python-Automation-Portfolio/
├── clean_data.py
├── sample_data.csv
├── README.md
└── .gitignore
```

## Installation

1. Install Python 3.
2. Open a terminal in the project folder.
3. Install the required library:

   ```bash
   pip install pandas
   ```

## How to Run

Run the script from the project folder:

```bash
python clean_data.py
```

The script reads `sample_data.csv` and generates the output files.

## Output Files

| File | Description |
|---|---|
| `cleaned_data.csv` | Cleaned dataset |
| `summary_report.txt` | Summary of the cleaning process |

## Sample Test Results

Tested with the included sample dataset.

| Metric | Result |
|---|---:|
| Original rows | 5 |
| Rows after cleaning | 4 |
| Duplicate rows removed | 1 |
| Missing cells detected | 1 |

*These results apply to the sample dataset and are not a benchmark for larger datasets.*

## Limitations

- Missing values are reported, not automatically filled.
- Rows are considered duplicates when all column values match.
- The tool is designed for CSV files and has been tested with the included sample data.
- Always keep a backup before processing important business data.

## Potential Use Cases

- Cleaning customer or contact lists
- Removing duplicate spreadsheet records
- Preparing datasets for analysis
- Automating repetitive CSV-cleaning tasks

## Future Improvements

- Add Excel (`.xlsx`) file support
- Add configurable missing-value handling
- Generate reports in additional formats

## Author

**Nouman Khan**

GitHub: [@noumankhanoffice-a11y](https://github.com/noumankhanoffice-a11y)
