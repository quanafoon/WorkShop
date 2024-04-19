from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')