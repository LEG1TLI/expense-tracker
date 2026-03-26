import pandas as pd 
import matplotlib.pyplot as plt 
from .db import get_connection
from weasyprint import HTML, CSS
from pathlib import Path

def montly_summary_chart(year_month):
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM expenses", conn) 
    conn.close()

    mdf = df[df['date'].str.startswith(year_month)]
    g = mdf.groupby('category')['amount'].sum()

    g.plot(kind='bar', title=f"Expense summary for ({year_month})")
    plt.tight_layout()
    plt.savefig(f"reports/{year_month}_summary.png")

def build_report(summary, year_month):
    total = sum(summary.values())

    rows = ""
    for category, amount in summary.items():
        rows += f"""
        <tr>
            <td>{category}</td>
            <td class="amount">${amount:,.2f}</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <div class="page">
            <div class="report-card">
                <div class="header">
                    <h1>Expense Report</h1>
                    <p>Monthly summary for {year_month}</p>
                </div>

                <div class="content">
                    <div class="summary-box">
                        <div class="summary-label">Total Expenses</div>
                        <div class="summary-total">${total:,.2f}</div>
                    </div>

                    <table>
                        <thead>
                            <tr>
                                <th>Category</th>
                                <th class="amount">Amount</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

def make_pdf(summary, year_month):
    html = build_report(summary, year_month)
    output_path = Path("reports") / f"{year_month}_report.pdf"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(output_path)
    return output_path
