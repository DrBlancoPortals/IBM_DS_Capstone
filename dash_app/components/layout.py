from dash import dcc, html, Dash
import dash_bootstrap_components as dbc
from pandas import DataFrame

from .success_rate_pie import render_component as render_0
from .success_rate_version_by_site import render_component as render_1
from .payload_to_orbit import render_component as render_2
from .payload_orbit_by_launch import render_component as render_3


def create_layout(app: Dash, dataframe: DataFrame, template: str):
    title_div = html.Div(
        [
            html.H1("SpaceX Launch Records Dashboard"),
            html.Hr(),
        ]
    )
    col0 = render_0(app, dataframe, template)
    col1 = render_1(app, dataframe, template)
    col2 = render_2(app, dataframe, template)
    col3 = render_3(app, dataframe, template)

    row_pies = dbc.Row(children=[col0, col1])
    row_graphs = dbc.Row(children=[col2, col3])

    return html.Div(
        children=[
            title_div,
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [row_pies],
                        title="Filtering by launch Site",
                    ),
                    dbc.AccordionItem(
                        [row_graphs],
                        title="Filtering by payload mass to orbit",
                    ),
                ],
            ),
        ]
    )
