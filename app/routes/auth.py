from flask import redirect, url_for, flash, request, session, Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'admin',
    'password': '1234'
}

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    # if already logged in → go to tasks
    if 'user' in session:
        return redirect(url_for('tasks.view_tasks'))

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash('Login Successfully', 'success')
            return redirect(url_for('tasks.view_tasks'))   # 🔥 important

        else:
            flash('Invalid username or password', 'danger')  # lowercase

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out Successfully', 'info')
    return redirect(url_for('auth.login'))