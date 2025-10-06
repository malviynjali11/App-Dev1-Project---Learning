from main import app 
from flask import render_template, request, session, flash, redirect, url_for
from controllers.models import *

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        # check if user is already logged in then redirect to dashboard
        if 'user_email' in session:
            # Redirect to Home Page
            return redirect('/')
        return render_template('login.html')
    
    if request.method == 'POST':
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        # Data Validation 
        if not email or not password:
            flash("Email and Password are required !")
            return render_template('login.html')
        
        if '@' not in email:
            flash("Invalid Email !")
            return render_template('login.html')
        
        # we can add more validation like password length, special characters, etc.

        # Query the DB to check if user exists 
        user = User.query.filter_by(user_email = email).first()
        if not user:
            flash("User does not exist ! Please Register .")
            return render_template('login.html')
        if user.password != password:
            flash("Incorrect Password !")
            return render_template('login.html')
        
        session['user_email'] = user.user_email 
        session['user_role'] = [role.name for role in user.roles]

        flash("Login Successfully !")
        # Redirects to Home Page
        return redirect(url_for('home'))
    
@app.route('/logout')
def logout():
    if 'user_email' not in session:
        flash("You are not logged in !")
        return redirect(url_for('login'))
    
    session.pop('user_email')
    session.pop('user_role')
    flash("Logged out Successfully !")
    return redirect(url_for('login'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':
        email = request.form.get('email', None)
        password = request.form.get('password', None)
        confirm_password = request.form.get('confirm_password', None)
        user_name = request.form.get('user_name', None)
        role = request.form.get('role', None)

        # Data Validation
        if not email or not password or not confirm_password or not user_name or not role:
            flash("All fields are required !")
            return render_template('register.html')
        if '@' not in email:
            flash("Invalid Email !")
            return render_template('register.html')
        if password != confirm_password:
            flash("Passwords do not match !")
            return render_template('register.html')
        if len(password) < 8:
            flash("Password must be at least 8 characters long !")
            return render_template('register.html')
        
        user = User.query.filter_by(user_email = email).first()
        if user:
            flash("User already exists ! Please Login .")
            return render_template('register.html')
        
        role = Role.query.filter_by(name=role).first()
        if not role:
            flash("Invalid Role !")
            return render_template('register.html')
        user = User(
            user_email = email,
            password = password,
            user_name = user_name,
            roles = [role]
        )
        db.session.add(user)
        db.session.commit()
        flash("Registered Successfully ! Please Login .")
        return redirect(url_for('login'))