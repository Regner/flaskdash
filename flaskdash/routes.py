

import json

from datetime import datetime

from flask import Blueprint, render_template

from flaskdash.extensions import db_widgets

blueprint = Blueprint('public', __name__, static_folder='../static')


dashboards_db = {
    0: {
        'name': 'TEST DASHBOARD!',
        'num_cols': 3,
        'box_size': 300,
        'margins': 10,
    }
}

widgets_db = {
    0: [
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
        {
            'name': 'number',
            'pos_x': 1,
            'pos_y': 1,
            'size_x': 1,
            'size_y': 1,
            'title': 'YAY! TEST!',
            'more_info': 'More info!',
            'updated_at': datetime.now().strftime('%Y-%m-%d'),
            'config': {
                'value': 1,
            },
        },
    ],
}


@blueprint.route('/dashboards/<int:dashboard_id>/')
def dashboard(dashboard_id):
    dashboard_config = dashboards_db[dashboard_id]
    widget_configs = widgets_db[dashboard_id]

    grid = ''
    css = set()
    js = set()

    for wc in widget_configs:
        grid += db_widgets.render_widget(wc)

        css.add(db_widgets.widget_css_path(wc['name']))
        js.add(db_widgets.widget_js_path(wc['name']))

    context = {
        'css_files': css,
        'js_files': js,
        'grid_elements': grid,
    }

    context.update(dashboard_config)

    return render_template('home.html', context=context)

@blueprint.route('/admin/')
def admin():
    dashboards = []

    for board in dashboards_db:
        dashboards.append({
            'name': board['name'],
            'max_cols': '',
            'num_widgets': '',
        })
