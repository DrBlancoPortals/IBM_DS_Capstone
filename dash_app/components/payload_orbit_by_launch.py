from pandas import DataFrame
from dash import Dash, no_update, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

import plotly.express as px
import numpy as np


def render_component(app: Dash, df: DataFrame, template: str) -> dbc.Col:

    min_payload = df["Payload Mass (kg)"].min()
    max_payload = df["Payload Mass (kg)"].max()

    # Adding some customization to the marks - Colour scale ....
    marks_styled = {
        int(el): {"label": f"{int(el)}", "style": {"color": "#000000"}}
        for el in np.linspace(0, 10000, 5)
    }
    marks_styled[int(min_payload)] = {
        "label": f"Minimum : {int(min_payload)}",
        "style": {"color": "#228B22"},
    }
    marks_styled[int(max_payload)] = {
        "label": f"Maximum : {int(max_payload)}",
        "style": {"color": "#DC143C"},
    }

    @app.callback(
        Output("success-payload-by-time-scatter-chart", "figure"),
        Input("payload-slider-2", "value"),
        # prevent_initial_call=True,
    )
    def update_scatter_figure(selected_payloadRange):
        """
        Callback method that renders a scatter chart.
        The graph shows the successfull launches filtered by the
        range of payload mass [in kg] selected
        """
        if selected_payloadRange is None:
            # Safeguard in case of breaking the slider somehow
            return no_update

        # Not and else required, given that the return is hit previously
        filtered_df = df[df["Payload Mass (kg)"].isin(range(*selected_payloadRange))]
        return px.scatter(
            filtered_df,
            x="Flight Number",
            y="Payload Mass (kg)",
            color="Launch Site",
            title="Correlation between Payload and Flight number",
            template=template,
        )

    container = dbc.Col(
        [
            dcc.Graph(id="success-payload-by-time-scatter-chart"),
            dcc.RangeSlider(
                id="payload-slider-2",
                min=0,
                max=10000,
                step=1000,
                marks=marks_styled,
                value=[min_payload, max_payload],
                tooltip={"placement": "top", "always_visible": True},
            ),
        ]
    )

    return container
