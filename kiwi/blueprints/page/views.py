from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
	return render_template('page/home.html')


@page.route('/privacy.html')
def privacy():
	return render_template('page/privacy.html')


@page.route('/terms.html')
def terms():
	return render_template('page/terms.html')


@page.route('/contact.html')
def contact():
	return render_template('page/contact.html')


@page.route('/courses.html')
def courses():
	return render_template('page/courses.html')


@page.route('/library.html')
def library():
	return render_template('page/library.html')


@page.route('/community.html')
def community():
	return render_template('page/community.html')

