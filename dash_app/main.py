import logging

from dash import Dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from config import ALLOWED_TEMPLATES
from components.layout import create_layout
from data import DATASET

logger = logging.Logger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(logging.StreamHandler())

TITLE = "SpaceX Dashboard for Landing success"

TEMPLATE = "MINTY"
load_figure_template(TEMPLATE)


def configure_app(app: Dash):

    df = DATASET
    logger.debug("Loaded dataframe")
    logger.debug(df.shape)
    app.layout = create_layout(app, dataframe=df, template=TEMPLATE)
    return app


if __name__ == "__main__":
    dashapp = Dash(title=TITLE, external_stylesheets=[ALLOWED_TEMPLATES[TEMPLATE]])
    dashapp.config["suppress_callback_exceptions"] = True
    logger.debug("Initialized DashApp")
    app = configure_app(dashapp)
    logger.debug("App configured")
    app.run_server(debug=True, use_reloader=True)
