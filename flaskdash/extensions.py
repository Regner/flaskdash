

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.debugtoolbar import DebugToolbarExtension

from flaskdash.widgets import DashboardWidgets

db = SQLAlchemy()
debug_toolbar = DebugToolbarExtension()
db_widgets = DashboardWidgets()


def configure_extensions(app):
    """ Registers all relevant extensions. """

    db.init_app(app)
    debug_toolbar.init_app(app)
    db_widgets.init_app(app)

    return None
