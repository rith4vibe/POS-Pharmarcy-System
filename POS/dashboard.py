import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
def show_charts():
    """
    Daily chart analysis
    """
    df = pd.read_csv("sales.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Period"] = df["Date"].dt.date.astype(str)
    revenue = df.groupby("Period")["Total"].sum().reset_index()
    top_medicine = df.groupby("MedicineName")["Quantity"].sum().reset_index()
    sales_dist = df.groupby("MedicineName")["Total"].sum().reset_index()
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "domain"}],
               [{"colspan": 2, "type": "xy"}, None]],
        subplot_titles=("Daily Revenue", "Sales Distribution", "Top Selling Medicines")
    )
    fig.add_trace(go.Scatter(x=revenue["Period"], y=revenue["Total"], mode="lines+markers", name="Revenue"), row=1, col=1)
    fig.add_trace(go.Pie(labels=sales_dist["MedicineName"], values=sales_dist["Total"], name="Sales Distribution"), row=1, col=2)
    fig.add_trace(go.Bar(x=top_medicine["MedicineName"], y=top_medicine["Quantity"], name="Top Selling"), row=2, col=1)
    fig.update_layout(height=700, width=900, title_text="Pharmacy POS Daily Analytics Dashboard")
    fig.show()
