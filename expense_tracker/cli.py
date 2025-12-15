import argparse
from datetime import datetime
from . import db

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
        # TODO: insert into DB
    elif args.cmd == "summary":
        print(f"Summary for {args.month}")
        # TODO: query DB and show totals
    elif args.cmd == "export":
        summary = monthly_summary(args.month)
        if args.format == "pdf":
            path = export_pdf(summary, args.month)
            print(f"PDF exported to {path}")


if __name__ == "__main__":
    db.init_db()
    main()
