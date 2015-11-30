

from flaskdash.widgets.number import NumberWidget


class DashboardWidgets(object):
    def __init__(self, app=None):
        self.app = app

        

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Config stuff here

        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        # if hasattr(app, 'teardown_appcontext'):
        #     app.teardown_appcontext(self.teardown)
        # else:
        #     app.teardown_request(self.teardown)
        pass

    def register_widget(self, widget):