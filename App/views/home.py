from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for, flash
from App.controllers import get_all_users
from flask_jwt_extended import jwt_required, current_user
import os
from werkzeug.utils import secure_filename


home_views = Blueprint('home_views', __name__, template_folder='../templates')


@home_views.route('/', methods=['GET'])
def home_page():
    users = get_all_users()
    return render_template('home.html', users = users)