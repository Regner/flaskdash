

import json


class NumberWidget(object):
    """ Simple widget for displaying a single number. """

    css_path = 'css/widgets/number.css'
    js_path = 'js/widgets/number.js'
    template_path = 'widgets/number.html'

    name = 'number'
    friendly_name = 'Static Number'

    def __init__(self, config):
        self.config = json.loads(config)

    def get_data(self):
        return self.config['data']

    def get_gridster_config(self):
        return self.config['gridster_config']

    def get_template_context(self):
        context = self.get_gridster_config()
        context.update(self.get_data())
        context.update(dict(widget_name=self.name))

        return context