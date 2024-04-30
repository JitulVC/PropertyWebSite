from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus

from modelview.index import IndexModelView
from modelview.projects import ProjectsModelView
from modelview.testimonial import TestimonialModelView

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    indexModelView = IndexModelView()
    data = indexModelView.loaddata()
    return render_template('index.html', idata=data)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/projects', methods=['GET'])
def projects():
    projectsModelView = ProjectsModelView()
    data = projectsModelView.loaddata()
    return render_template('projects.html',pdata=data)

@app.route('/testimonial', methods=['GET'])
def testimonial():
    testimonialModelView = TestimonialModelView()
    data = testimonialModelView.loaddata()
    return render_template('testimonial.html', tdata=data)

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

