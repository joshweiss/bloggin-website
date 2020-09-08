from flask import Blueprint, render_template, request
from mafia_flask.models import Post

main = Blueprint('main', __name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@main.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/mafia')
def mafia():
    return render_template('webpage.html')
