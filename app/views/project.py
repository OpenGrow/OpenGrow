# -*- coding: utf-8 -*-
import os
# System Imports
from xml.dom.minidom import parseString
# Flask Imports
from flask import render_template, redirect
from flask import url_for, request, send_from_directory, session
from werkzeug import secure_filename

# Local Imports
from app import app
from app.forms import NewProjectForm
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import desc

# Package Imports
from decorators import login_required
from models import Project
from models import db

#Image Processing
import PIL
from PIL import Image


@app.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():

    projects_all = Project.query.order_by(desc(Project.date)).all()
    print projects_all
    projects_dict = []
    for project in projects_all:
        print project.id, project.name, project.description, project.img_path
    

    form = NewProjectForm()
    if request.method == 'POST':
        if not form.validate():
            print "form not valid"
            return render_template("projects.html",title='OpenGrow', form=form)

        else:
            file = request.files['file']
            if file :
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                try :
                    fixe_size = 250
                    img = Image.open(path)
                    img = img.resize((fixe_size,fixe_size), PIL.Image.ANTIALIAS)
                    img.save(path)
                except :
                    print "Error when processing image"
                    return render_template('projects.html', title='OpenGrow', form=form, projects_all=projects_all)

            project = Project(name=form.name.data, description=form.description.data, img_path=str(path).replace("app/static/",""), date=None)
            db.session.add(project)
            db.session.commit()
            print "Project was commit"
            
    projects_all = Project.query.order_by(desc(Project.date)).all()
    return render_template('projects.html', title='OpenGrow', form=form, projects_all=projects_all)

@app.route('/new_project', methods=['GET', 'POST'])
@login_required
def new_project ():
    return render_template('projects.html', title='OpenGrow')

@app.route('/project_delete/<id>', methods=['GET', 'POST'])
@login_required
def del_project (id):
    project =  Project.query.filter_by(id=id).first()
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('projects'))
