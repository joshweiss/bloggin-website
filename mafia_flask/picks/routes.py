from flask import render_template, url_for, flash, redirect, request, Blueprint
from mafia_flask.picks.forms import PickForm
from flask_login import login_required

picks = Blueprint('picks', __name__)


@picks.route('/picks/new', methods=['GET', 'POST'])
@login_required
def new_pick():
    form = PickForm()
    return render_template('create_pick.html', title='New Pick test', form=form, legend='New Pick')
