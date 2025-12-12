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

    sump = sub.add_parser("summary")
    sump.add_argument("--month", required=True)

    args = parser.parse_args()

    if args.cmd == "add":
        print(f"Adding expense: {args.amount} in {args.category} on {args.date}")
        # TODO: insert into DB
    elif args.cmd == "summary":
        print(f"Summary for {args.month}")
        # TODO: query DB and show totals

if __name__ == "__main__":
    db.init_db()
    main()
