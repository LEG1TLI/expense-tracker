import argparse
from datetime import datetime
from . import db
from . import reports

def get_monthly_summary(year_month):
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT category, SUM(amount) as total FROM expenses WHERE date LIKE ? GROUP BY category",
        (f"{year_month}%",)
    )
    summary = {row[0]: row[1] for row in cur.fetchall()}
    conn.close()
    return summary

def main():
    parser = argparse.ArgumentParser(prog="expenses")
    sub = parser.add_subparsers(dest="cmd", required=True)

    addp = sub.add_parser("add")
    addp.add_argument("--date", required=True)
    addp.add_argument("--amount", type=float, required=True)
    addp.add_argument("--category", required=True)
    addp.add_argument("--notes", default="")

    monthly_summary = sub.add_parser("summary")
    monthly_summary.add_argument("--month", required=True)

    export_pdf = sub.add_parser("export")
    export_pdf.add_argument("--month", required = True)
    export_pdf.add_argument("--format", choices = ["pdf"], default="pdf")

    args = parser.parse_args()

    if args.cmd == "add":
        print(f"Adding expense: {args.amount} in {args.category} on {args.date}")
        db.add_expense(args.date, args.amount, args.category, args.notes)
    elif args.cmd == "summary":
        print(f"Summary for {args.month}")
        summary = get_monthly_summary(args.month)
        for category, total in summary.items():
            print(f"{category}: {total}")
    elif args.cmd == "export":
        summary = get_monthly_summary(args.month)
        if args.format == "pdf":
            path = reports.make_pdf(summary, args.month)
            print(f"PDF exported to {path}")


if __name__ == "__main__":
    db.init_db()
    main()
