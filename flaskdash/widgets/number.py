

from wtforms import IntegerField


class NumberWidget(object):
    """ Simple widget for displaying a single static number. """

    css_path = 'css/widgets/number.css'
    js_path = 'js/widgets/number.js'
    template_path = 'widgets/number.html'

    name = 'number'
    friendly_name = 'Static Number'

    form_config = {
        'number': IntegerField('Number'),
    }

    def __init__(self, widget_config):
        self.widget_config = widget_config

    def get_template_data(self):
        return {
            'value': self.widget_config['value'],
        }
