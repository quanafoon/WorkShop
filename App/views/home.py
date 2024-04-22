from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for, flash
from App.controllers import apply, getInternships, findInternship, getApplications, addProject
from flask_jwt_extended import jwt_required, current_user
import os
from werkzeug.utils import secure_filename


home_views = Blueprint('home_views', __name__, template_folder='../templates')

@home_views.route('/home', methods=['GET'])
def home_page():
    internships = getInternships()
    applications = getApplications()
    return render_template('home.html', internships=internships, applications=applications)

@home_views.route('/home/<int:id>', methods=['GET'])
def selectInternship(id):
    selected = findInternship(id)
    return render_template('home.html', selected=selected)

@home_views.route('/apply/<int:id>', methods=['POST'])
@jwt_required()
def apply_action(id):
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    dob = request.form.get('dob')
    email = request.form.get('email')
    phone = request.form.get('phone')
    transcript = request.files['transcript']
    resume = request.files['resume']
    user_id = current_user.id

    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)

    transcript_filename = secure_filename(transcript.filename)
    transcript_path = os.path.join(upload_folder, transcript_filename)
    transcript.save(transcript_path)

    resume_filename = secure_filename(resume.filename)
    resume_path = os.path.join(upload_folder, resume_filename)
    resume.save(resume_path)

    application = apply(firstname, lastname, dob, email, phone, transcript_path, resume_path, user_id, id)
    if application:
        flash("Application sent!")
    else:
        flash("Error")
    return redirect(url_for('home_views.home_page'))

@home_views.route('/submitProject/<int:id>', methods=['POST'])
def submit_action(id):
    title = request.form.get('title')
    company = request.form.get('company')
    location = request.form.get('location')
    start = request.form.get('start')
    duration = request.form.get('duration')
    stipend = request.form.get('stipend')

    project = addProject(title, company, id, location, start, duration, stipend)
    if project:
        flash("project submitted!")
    else:
        flash("Error")
    return render_template('home.html')