from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db, Internships
from App.controllers import create_user, parse_internships

home_views = Blueprint('home_views', __name__, template_folder='../templates')

@home_views.route('/home', methods=['GET'])
def home_page():
    internships = Internships.query.all()
    return render_template('home.html', internships=internships)