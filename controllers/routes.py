from main import app 
from flask import render_template, request, session, flash, redirect
from controllers.models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if 'admin' in session.get('user_role', None):
        if request.method == 'GET':
            return render_template('add_doctor.html')
        elif request.method == 'POST':
            name = request.form.get('name', None)
            specialization = request.form.get('Specialization', None)
            yoe = request.form.get('yoe', None)

            #data validation
            
    else:
        flash('Access denied. Admins only.', 'danger')
        return redirect('/')
