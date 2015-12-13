

import json

from wtforms import IntegerField


class NumberWidget(object):
    """ Simple widget for displaying a single number. """

    css_path = 'css/widgets/number.css'
    js_path = 'js/widgets/number.js'
    template_path = 'widgets/number.html'

    name = 'number'
    friendly_name = 'Static Number'

    form_config = {
        'number': IntegerField('Number'),
    }

    def __init__(self, widget_config, widget_data):
        self.gridster_config = json.loads(gridster_config)

    def get_data(self):
        return self.config['data']

    def get_template_context(self):
        context = self.gridster_config
        context.update(self.get_data())
        context.update(dict(widget_name=self.name))

        return context
