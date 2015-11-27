

from flask import Blueprint, render_template

from flaskdash.widgets.number import NumberWidget

blueprint = Blueprint('public', __name__, static_folder='../static')

dashboard_options = {
    'columns': 4,
    'width': 350,
    'height': 350,
    'margins': 5,
}

@blueprint.route('/')
def home():
    widgets = [NumberWidget(), NumberWidget()]

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
