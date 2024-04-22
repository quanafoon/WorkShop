from flask import Blueprint, redirect, render_template, request, jsonify, url_for, flash
from App.controllers import findApplication, getApplications, getShortlists, getAppsForInternship, addToShortlist
from flask_jwt_extended import jwt_required, current_user
import os


shortlist_views = Blueprint('shortlist_views', __name__, template_folder='../templates')

@shortlist_views.route('/adminShortlist/<int:id>', methods=['GET'])
def admin_page(id):
    applications = getAppsForInternship(id)
    return render_template('shortlist.html', applications=applications)


@shortlist_views.route('/details/<int:appID>,<int:internshipID>', methods=['GET'])
def admin_view(appID, internshipID):
    applications = getAppsForInternship(internshipID)
    selected = findApplication(appID)
    return render_template('shortlist.html', applications=applications, selected=selected)


@shortlist_views.route('/addShortlist/<int:appID>,<int:internshipID>', methods=['POST'])
def addShortlist(appID, internshipID):
    shortlist = addToShortlist(appID, internshipID)
    if shortlist:
        flash("Added to shortlist!")
    else:
        flash("Already added")
    return redirect(url_for('shortlist_views.admin_page', id=internshipID))
