### data_engineering_etl
──────────────────────────────
📄 Script: data_pipeline_etl.py
──────────────────────────────
🔍 Description:
    End-to-end ETL pipeline for loading, transforming, and saving datasets.

🛠️ Key Features:
    - Reads raw files from local or cloud sources
    - Applies transformations (cleaning, filtering, enrichment)
    - Saves to database, CSV, or Excel
    - Logging and error handling included

✅ Use For:
    - Automating repeated ETL jobs
    - Daily/weekly pipeline execution

──────────────────────────────
📄 Script: sql_to_pandas.py
──────────────────────────────
🔍 Description:
    Pulls data from SQL databases directly into Pandas DataFrames.

🛠️ Key Features:
    - Supports MySQL, PostgreSQL, SQL Server
    - Parameterized queries
    - Secure credential loading

✅ Use For:
    - Replacing manual SQL exports
    - Seamless integration of SQL and Python

──────────────────────────────
📄 Script: csv_merger_batch.py
──────────────────────────────
🔍 Description:
    Merges multiple CSV files from a directory into one dataset.

🛠️ Key Features:
    - Auto-detects CSVs in a folder
    - Handles mismatched columns
    - Adds filename or timestamp metadata

✅ Use For:
    - Combining exports from multiple sources
    - Preprocessing large volumes of files

──────────────────────────────
📄 Script: data_validator.py
──────────────────────────────
🔍 Description:
    Validates dataset structure, schema, and values before processing.

🛠️ Key Features:
    - Checks for nulls, duplicates, outliers
    - Validates column types and expected values
    - Generates data quality reports

✅ Use For:
    - Ensuring clean inputs for ETL or ML
    - Catching data issues early

──────────────────────────────
📄 Script: excel_report_generator.py
──────────────────────────────
🔍 Description:
    Automates Excel report creation with multiple sheets and formatting.

🛠️ Key Features:
    - Summary and detail sheets
    - Pivot tables, charts (optional)
    - Styled Excel outputs with Pandas & openpyxl

✅ Use For:
    - Weekly or monthly business reporting
    - Creating Excel deliverables from pipelines
