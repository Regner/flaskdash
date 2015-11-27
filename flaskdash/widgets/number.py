

import os
from datetime import datetime

class NumberWidget(object):
    """ Simple widget for displaying a single number. """

    base_css_path = 'css/widgets'
    base_js_path = 'js/widgets'
    base_template_path = 'widgets'

    name = 'number'

    def get_data(self):
        return {
            'title': 'YAY TEST!',
            'value': 1,
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
        }

    def get_gridster_config(self):
        return {
            'pos_y': 1,
            'pos_x': 1,
            'size_x': 1,
            'size_y': 1,
        }

    def get_template_context(self):
        context = self.get_gridster_config()
        context.update(self.get_data())
        context.update({
            'widget_name': self.name,
        })

        return context

    @property
    def path_css(self):
        return '{}.css'.format(os.path.join(self.base_css_path, self.name))

    @property
    def path_js(self):
        return '{}.js'.format(os.path.join(self.base_js_path, self.name))

    @property
    def path_template(self):
        return '{}.html'.format(os.path.join(self.base_template_path, self.name))
