

import logging

from flask import render_template

from flaskdash.widgets.number import NumberWidget

logger = logging.getLogger(__name__)


class WidgetAlreadyRegistered(Exception):
    pass


class NoSuchWidget(Exception):
    pass


class DashboardWidgets(object):
    def __init__(self, app=None):
        self.widget_registry = {}

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Config stuff here

        # Register default widgets
        self.register_widget(NumberWidget)

        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        # if hasattr(app, 'teardown_appcontext'):
        #     app.teardown_appcontext(self.teardown)
        # else:
        #     app.teardown_request(self.teardown)

    def register_widget(self, widget):
        """ Stores a widget in the internal registry for working with later. """

        if widget.name in self.widget_registry:
            raise WidgetAlreadyRegistered('A widget by the name of {} is already registered.'.format(widget.name))

        else:
            self.widget_registry[widget.name] = widget

    def render_widget(self, widget_name, widget_data):
        """ Returns the HTML for a given widget and it's data. """

        if widget_name not in self.widget_registry:
            raise NoSuchWidget('There is no registered widget by the name of {}'.format(widget_name))



    def widget_css_path(self, widget_name):
        """ Returns the path for a widgets CSS file. """

        if widget_name not in self.widget_registry:
            raise NoSuchWidget('There is no registered widget by the name of {}'.format(widget_name))

        return self.widget_registry[widget_name].css_path

    def widget_js_path(self, widget_name):
        """ Returns the path for a widgets JS file. """

        if widget_name not in self.widget_registry:
            raise NoSuchWidget('There is no registered widget by the name of {}'.format(widget_name))

        return self.widget_registry[widget_name].js_path
