# -*- coding: utf-8 -*-

# System Imports
from xml.dom.minidom import parseString

# Flask Imports
from flask import render_template, redirect
from flask import url_for, request, send_from_directory, session
from werkzeug import secure_filename

# Local Imports
from app import app
from app.forms import *

# Package Imports
from decorators import login_required

from models import db

#Dashboard projet (changer de fichier dashboard.py !!)
@app.route('/opengrow/<id>', methods=['GET', 'POST'])
@login_required
def opengrow(id):
    print "Project "+str(id)+" selected"
    return render_template('opengrow.html', title='OpenGrow', project_id=id)


#Historique photos (changer de fichier dashboard.py !!)
@app.route('/stream', methods=['GET', 'POST'])
@login_required
def stream():
    return render_template('camera.html', title='OpenGrow')

#Future page de settings
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('settings.html', title='OpenGrow', settings=globalsettings, form=form, ips=ips)



