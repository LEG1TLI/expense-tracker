import pandas as pd 
import matplotlib.pyplot as plt 
from .db import get_connection

def montly_summary_chart(year_month):
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT * FROM expenses"
        ,Conn
        ) 
    conn.close()

    mdf = df[fd['date'].str.startswith(year_month)]
    g = mdf.groupby('category')['amount'].sum()

    g.plot(kind='bar', title=f"Expense summary for ({year_month})")
    plt.tight_layout()
    plt.savefig(f"reports/{year_month}_summary.png")