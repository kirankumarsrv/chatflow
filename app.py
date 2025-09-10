from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# from flask import request
# from markupsafe import escape

# @app.route("/hello")
# def helllo():
#     name = request.args.get("name", "<body><h1>Hello, World!</h1></body>")
#     return f"Hello, {escape(name)}!"
#     # return "<body><h1>Hello, World!</h1></body>"
    
# @app.route('/')
# def index():
#     return 'Index Page'

# # @app.route('/hello')
# # def hello():
# #     return 'Hello, World'


# # from markupsafe import escape

# # @app.route('/user/<username>')
# # def show_user_profile(username):
# #     # show the user profile for that user
# #     return f'User {escape(username)}'

# # @app.route('/post/<int:post_id>')
# # def show_post(post_id):
# #     # show the post with the given id, the id is an integer
# #     return f'Post {post_id}'

# # @app.route('/path/<path:subpath>')
# # def show_subpath(subpath):
# #     # show the subpath after /path/
# #     return f'Subpath {escape(subpath)}'


# from flask import url_for

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


# from flask import render_template

# @app.route('/hello/')
# # @app.route('/hello/<name>')
# # def hello(name=None):
# #     return render_template('index.html', person=name)
# from flask import request, render_template
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# from flask import render_template

# from flask import abort, redirect, url_for

# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.errorhandler(404)
# def not_found(error):
#     return  404