from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login required for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
