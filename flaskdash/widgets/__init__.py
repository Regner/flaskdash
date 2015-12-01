

import logging

from flaskdash.widgets.number import NumberWidget

logger = logging.getLogger(__name__)


class WidgetAlreadyRegistered(Exception):
    pass


class DashboardWidgets(object):
    def __init__(self, app=None):
        self.widget_registry = {}

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Config stuff here

        # Register default widgets
        self.register_widget(NumberWidget())

        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        # if hasattr(app, 'teardown_appcontext'):
        #     app.teardown_appcontext(self.teardown)
        # else:
        #     app.teardown_request(self.teardown)
        pass

    def register_widget(self, widget):
        """ Stores a widget in the internal registry for working with later.

        :param widget:
        :return:
        """
        if widget.name not in self.widget_registry:
            raise WidgetAlreadyRegistered('A widget by the name of {} is already registered.'.format(widget.name))

        else:
            self.widget_registry[widget.name] = widget
