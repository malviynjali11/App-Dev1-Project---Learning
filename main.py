from flask import Flask, render_template
from controllers.database import db
from controllers.config import config
from controllers.models import User, Role, UserRole, Doctor, Patient

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db.init_app(app)

with app.app_context():
    db.create_all()

    admin_role = Role.query.filter_by(name='admin').first()
    if not admin_role:
        admin_role = Role(name='admin')
        db.session.add(admin_role)
    patient_role = Role.query.filter_by(name='patient').first()
    if not patient_role:
        patient_role = Role(name='patient')
        db.session.add(patient_role)
    doctor_role = Role.query.filter_by(name='doctor').first()
    if not doctor_role:
        doctor_role = Role(name='doctor')
        db.session.add(doctor_role)

    # admin_user = User.query.filter_by(user_email = 'admin@gmail.com').first()
    # if not admin_user:
    #     admin_user = User(
    #         user_email = 'admin@gmail.com',
    #         password = 'admin123',
    #         user_name = 'Admin'
    #     )
    #     db.session.add(admin_user)
    #     # print(admin_user.id)
    #     admin_user_details = User.query.filter_by(user_email = 'admin@gmail.com').first()
    #     admin_role = Role.query.filter_by(name='admin').first()

    #     user_id = admin_user_details.user_id 
    #     role_id = admin_role.id

    #     user_role = UserRole(user_id=user_id, role_id=role_id)
    #     db.session.add(user_role)

    admin_user = User.query.filter_by(user_email = 'admin@gmail.com').first()
    if not admin_user:
        admin_role = Role.query.filter_by(name='admin').first()
        admin_user = User(
            user_email = 'admin@gmail.com',
            password = 'admin123',
            user_name = 'Admin',
            roles = [admin_role]
        )
        db.session.add(admin_user)

    db.session.commit()

from controllers.auth_routes import *
from controllers.routes import *

if __name__ == '__main__':
    app.run(debug=True)