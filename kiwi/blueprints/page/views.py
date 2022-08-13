from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
	return render_template('page/home.html')

@page.route('/privacy')
def privacy():
	return render_template('page/privacy.html')

