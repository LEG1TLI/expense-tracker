import pandas as pd 
import matplotlib.pyplot as plt 
from db import get_connection
from weasyprint import HTML
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
    rows = ""
    for category, amount in summary.items():
        rows += f"<tr><td>{category}<\td><td>{amount:.2f}</td></tr>"
        
        return f"""
        <html>
        <head>
            <style src = "styles.css"></style>
        </head>
        <body>
            <h1> Expense Report for {year_month} </h1>
            <table>
                <tr><th>Category</th><th>Tirak</th></tr>
                {rows}
            </table>
        </body>
        </html>
        """
def make_pdf(summary, year_month):
    html = build_report(summary, year_month)
    output_path = Path("reports") / f"{year_month}_report.pdf"
    HTML(string=html).write_pdf(output_path)
    return output_path