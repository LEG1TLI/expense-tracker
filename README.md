Hey! This is a super basic python app made for tracking daily expenses, with the abilities to generate summaries and visualize spending habits. 
Features:
- add and list expenses
- monthly spending summaries as PDF files
- charts displaying categories and months
- storage in an SQLite database

SETUP:

bash
python -m venv .venv
source .venv/bin/activate

Windows
.venv\scripts\activate

pip install -r requirements.txt

TO USE:
initialize SQLite3 db:
python-m expense_tracker.db

python -m expense_tracker.cli add --date 2026-01-27 --amount 25.00 --category transport --notes "gas"
python -m expense_tracker.cli add --date 2026-01-26 --amount 50.00 --category groceries

*The --notes tag is OPTIONAL, not adding it will default to an empty string

TO GENERATE EXPENSE CHART:

python -m expense_tracker.cli export --month YYYY-MM