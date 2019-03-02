from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'pew'}
	posts = [
		{
			'author': {'username': 'i can\'t do names'},
			'body': 'ugh'
		},
		{
			'author': {'username': 'ugh'},
			'body': 'pewpewpew'
		}
	]
	return render_template('index.html', title='pep', user=user, posts=posts)