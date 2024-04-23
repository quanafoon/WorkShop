from flask import Blueprint, redirect, render_template, request, jsonify, url_for, flash
from App.controllers import findApplication, findInternship, getApplications, getShortlists, getAppsForInternship, addToShortlist, getShortlistForInternship, getUserShortlistedApplications, deleteFromShortlist
from flask_jwt_extended import jwt_required, current_user
import os


shortlist_views = Blueprint('shortlist_views', __name__, template_folder='../templates')

@shortlist_views.route('/adminShortlist/<int:id>', methods=['GET'])
def admin_page(id):
    applications = getAppsForInternship(id)
    shortlist = getShortlistForInternship(id)
    return render_template('shortlist.html', applications=applications, shortlist=shortlist)


@shortlist_views.route('/companyShortlist/<int:id>', methods=['GET'])
def company_page(id):
    shortlist = getShortlistForInternship(id)
    internship= findInternship(id)
    return render_template('shortlist.html', shortlist=shortlist, internship=internship)


@shortlist_views.route('/details/<int:appID>,<int:internshipID>', methods=['GET'])
def details_view(appID, internshipID):
    applications = getAppsForInternship(internshipID)
    shortlist = getShortlistForInternship(internshipID)
    selected = findApplication(appID)
    internship= findInternship(internshipID)
    return render_template('shortlist.html', internship=internship, applications=applications, selected=selected, shortlist=shortlist)


@shortlist_views.route('/addShortlist/<int:appID>,<int:internshipID>', methods=['POST'])
def addShortlist(appID, internshipID):
    shortlist = addToShortlist(appID, internshipID)
    if shortlist:
        flash("Added to shortlist!")
    else:
        flash("Already added")
    return redirect(url_for('shortlist_views.admin_page', id=internshipID))

@shortlist_views.route('/removeFromShortlist/<int:id>', methods=['POST'])
def delete_action(id):
    shortlist = deleteFromShortlist(id)
    if shortlist:
        flash("Sucessfully Deleted!")
    else:
        flash("Error")
    return redirect(url_for('shortlist_views.admin_page', id=internshipID))
