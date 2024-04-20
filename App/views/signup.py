from flask import Blueprint, redirect, flash, render_template, request, send_from_directory, jsonify
from App.controllers import create_user

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@signup_views.route('/signup', methods=['POST'])
def signup_action():
    data = request.form
    check = create_user(data['username'], data['password'])
    if check:
        flash(f"User {data['username']} created!")
        return render_template('index.html')
    else:
        flash(f"User {data['username']} already exists!")
        return render_template('signup.html')

    return redirect(url_for('user_views.get_user_page'))
