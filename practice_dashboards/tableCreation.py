import dash
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
df_all_sep = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/carrier_all_sep.csv', sep=',')
df_all_sep = df_all_sep.transpose()

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='All Swedish carriers'),
    generate_table(df_all_sep)
])

if __name__ == '__main__':
    app.run_server(debug=True)