

import json
from datetime import datetime

from flask import Blueprint, render_template

from flaskdash.widgets.number import NumberWidget

blueprint = Blueprint('public', __name__, static_folder='../static')

dashboard_options = {
    'num_cols': 6,
    'box_size': 300,
    'margins': 10,
}

mock_widget_config = {
    'gridster_config': {
        'pos_y': 1,
        'pos_x': 1,
        'size_x': 1,
        'size_y': 1,
    },
    'data': {
        'title': 'YAY TEST!',
        'value': 1,
        'more_info': 'More info!',
        'updated_at': datetime.now().strftime('%Y-%m-%d'),
    }
}

@blueprint.route('/')
def home():
    widgets = [NumberWidget(json.dumps(mock_widget_config)) for x in xrange(18)]

    grid = ''
    css = set()
    js = set()

    for widget in widgets:
        context = widget.get_template_context()

        grid += render_template(widget.path_template, context=context)

        css.add(widget.path_css)
        js.add(widget.path_js)

    context = {
        'css_files': css,
        'js_files': js,
        'grid_elements': grid,
    }

    context.update(dashboard_options)

    return render_template('home.html', context=context)
