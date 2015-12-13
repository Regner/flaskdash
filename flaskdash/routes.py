

import json

from datetime import datetime

from flask import Blueprint, render_template

from flaskdash.extensions import db_widgets

blueprint = Blueprint('public', __name__, static_folder='../static')


dashboards = {
    0: {
        'num_cols': 6,
        'box_size': 300,
        'margins': 10,
    }
}

widgets = {
    0: [
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'config': json.dumps({'value': 1}),
            'data': json.dumps({
                'title': 'YAY! TEST!',
                'more_info': 'More info!',
                'updated_ad': datetime.now().strftime('%Y-%m-%d'),
            }),
        },
    ],
}


@blueprint.route('/<int:dashboard_id>/')
def dashboard(dashboard_id):
    dashboard_config = dashboards[dashboard_id]
    widget_configs = widgets[dashboard_id]

    grid = ''
    css = set()
    js = set()

    for wc in widget_configs:
        grid += db_widgets.render_widget(wc['name'], wc['config'], wc['data'])

        css.add(db_widgets.widget_css_path(wc['name']))
        js.add(db_widgets.widget_js_path(wc['name']))

    context = {
        'css_files': css,
        'js_files': js,
        'grid_elements': grid,
    }

    context.update(dashboard_config)

    return render_template('home.html', context=context)
