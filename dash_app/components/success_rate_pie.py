from pandas import DataFrame
from dash import Dash, no_update, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

import plotly.express as px


def render_component(app: Dash, df: DataFrame, template: str) -> dbc.Col:

    dropdown_options = [
        {"label": "All Sites", "value": "ALL"},
    ]
    dropdown_options.extend(
        [{"label": lsite, "value": lsite} for lsite in df["Launch Site"].unique()]
    )

    @app.callback(
        Output("pie-chart", "figure"),
        Input("launch-selected", "value"),
        # prevent_initial_call=True,
    )
    def update_pie_figure(selected_launchSite):
        """
        Callback method that renders a pie chart.

        If the option All Sites is selected (keyword ALL) ->
        the success rate for each site is rendered

        If an specific site  is selected (keyword Name of site) ->
        the % success vs % failure is rendered
        """
        if selected_launchSite is None:
            # Safeguard in case of breaking the dropdown somehow
            return no_update

        if selected_launchSite == "ALL":
            # No filtering needed here
            return px.pie(
                data_frame=df,
                names="Launch Site",
                values="class",
                title=f"Total Success Launches by site",
                template=template,
            )

        # Not and else required, given that the return is hit previously
        filtered_df = df[df["Launch Site"] == selected_launchSite]
        return px.pie(
            data_frame=filtered_df,
            names="class",
            title=f"Total Success Launches for site {selected_launchSite}",
            template=template,
        )

    container = dbc.Col(
        [
            dcc.Dropdown(
                options=dropdown_options,
                value="ALL",
                multi=False,
                id="launch-selected",
            ),
            dcc.Graph(id="pie-chart"),
        ]
    )

    return container
