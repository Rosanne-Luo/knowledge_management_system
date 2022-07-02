from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

@blueprint.route('/transaction', methods=['GET', 'POST'])
@login_required
def transcation():
    return render_template('investment/transcation.html', segment='transcation')