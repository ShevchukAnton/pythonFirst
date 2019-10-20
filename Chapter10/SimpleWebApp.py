from flask import Flask, session

import Chapter10.checkerDecorator as check

app = Flask(__name__)
app.secret_key = '2h6uwPXTsnjsDodK823n'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/page1')  # Order of decorators is very important as actually theses are functions that are executing by provided order
@check.check_logged_in
def page1() -> str:
    return 'This is page 1.'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


# Such order want work properly, it will give access to page in any way
# @check.check_logged_in
# @app.route('/page2')
@app.route('/page2')
@check.check_logged_in
def page2() -> str:
    return 'This is page 2.'


@app.route('/page3')
@check.check_logged_in
def page3() -> str:
    return 'This is page 3.'


if __name__ == '__main__':
    app.run(debug=True)
