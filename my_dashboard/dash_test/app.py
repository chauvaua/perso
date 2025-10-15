import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

data0 = pd.DataFrame({
    "mpg": [21, 21, 22.8, 21.4, 18.7, 18.1, 14.3],
    "cyl": [6, 6, 4, 6, 8, 6, 8],
    "hp": [110, 110, 93, 110, 175, 105, 245],
    "model": ["Mazda RX4","Mazda RX4 Wag","Datsun 710","Hornet 4 Drive","Hornet Sportabout","Valiant","Duster 360"]
})

# Créer app avec thème bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H2("Dashboard Python Bootstrap"), width=12), className="my-3"),
    
    # Filtre cylindre
    dbc.Row(dbc.Col(
        dcc.Dropdown(
            id="cyl-dropdown",
            options=[{"label": "Tous", "value": "Tous"}] + [{"label": str(c), "value": c} for c in sorted(data0["cyl"].unique())],
            value="Tous"
        ),
        width=4
    ), className="mb-4"),
    
    # Indicateurs avec cards
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody(html.Div(id="nb")), color="primary", inverse=True), width=4),
        dbc.Col(dbc.Card(dbc.CardBody(html.Div(id="avg_mpg")), color="success", inverse=True), width=4),
        dbc.Col(dbc.Card(dbc.CardBody(html.Div(id="max_hp")), color="warning", inverse=True), width=4),
    ], className="mb-4"),
    
    # Graphique et table
    dbc.Row([
        dbc.Col(dcc.Graph(id="scatter"), width=8),
        dbc.Col(html.Div(id="table-container"), width=4)
    ])
], fluid=True)

# Callbacks
@app.callback(
    Output("nb", "children"),
    Output("avg_mpg", "children"),
    Output("max_hp", "children"),
    Output("scatter", "figure"),
    Output("table-container", "children"),
    Input("cyl-dropdown", "value")
)
def update_dashboard(cyl_value):
    df = data0 if cyl_value=="Tous" else data0[data0["cyl"]==cyl_value]
    
    # Indicateurs
    nb = f"Nombre d'observations : {len(df)}"
    avg_mpg = f"MPG moyen : {df['mpg'].mean():.2f}" if len(df)>0 else "N/A"
    max_hp = f"Puissance max (hp) : {df['hp'].max()}" if len(df)>0 else "N/A"
    
    # Scatter
    fig = px.scatter(df, x="hp", y="mpg", hover_data=["model"], labels={"hp":"Chevaux", "mpg":"MPG"})
    
    # Table HTML
    table_html = html.Table([
        html.Thead(html.Tr([html.Th(c) for c in ["model","mpg","hp","cyl"]])),
        html.Tbody([html.Tr([html.Td(df.iloc[i][c]) for c in ["model","mpg","hp","cyl"]]) for i in range(len(df))])
    ])
    
    return nb, avg_mpg, max_hp, fig, table_html

if __name__ == "__main__":
    app.run(debug=True)
