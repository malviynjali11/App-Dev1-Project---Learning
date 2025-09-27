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

    db.session.commit()
@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/about')
def about():
    return "About Page"

if __name__ == '__main__':
    app.run(debug=True)