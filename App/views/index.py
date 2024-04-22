from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db, Applications, Shortlist
from App.controllers import create_user #, parse_internships

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_user('admin','adminpass', 'admin')
    #parse_internships()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/applicationsList', methods=['GET'])
def list():
    applications = Applications.query.all()
    application_list = []
    for application in applications:
        application_data = {
            'id': application.id,
            'firstname': application.firstname,
            'lastname': application.lastname,
            'dob': application.dob,
            'email': application.email,
            'phone': application.phone,
            'transcript': application.transcript,
            'resume': application.resume,
            'user_id': application.user_id
        }
        application_list.append(application_data)
    return jsonify(application_list)


@index_views.route('/shortlistList', methods=['GET'])
def list2():
    shortlist = Shortlist.query.all()
    shortlist_list = []
    for item in shortlist:
        shortlist_data = {
            'id': item.id,
            'application_id': item.application_id,
            'internship_id': item.internship_id,
        }
        shortlist_list.append(shortlist_data)
    return jsonify(shortlist_list)