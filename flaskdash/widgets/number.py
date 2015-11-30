

import os
import json

from flaskdash.utils.decorators import add_data_processor


class NumberWidget(object):
    """ Simple widget for displaying a single number. """

    base_css_path = 'css/widgets'
    base_js_path = 'js/widgets'
    base_template_path = 'widgets'

    name = 'number'

    data_processors = {}

    def __init__(self, config):
        self.config = json.loads(config)

    @add_data_processor('Static Data')
    def get_data_static(self, config):

    def get_data(self):
        return self.config['data']

    def get_gridster_config(self):
        return self.config['gridster_config']

    def get_template_context(self):
        context = self.get_gridster_config()
        context.update(self.get_data())
        context.update(dict(widget_name=self.name))

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
