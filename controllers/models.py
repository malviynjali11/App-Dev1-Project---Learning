from controllers.database import db 

class User(db.Model):

    # __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)

    patients_details = db.relationship('Patient', backref='user', lazy=True, uselist=False)
    doctor_details = db.relationship('Doctor', backref='user', lazy=True, uselist=False)

##################################### Example ###################################
# doctor = Doctor(specialization='Cardiology')
# user = User(user_email, password, user_name, doctor_details=doctor)
# db.session.commit()

class Role(db.Model):

    # __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

class UserRole(db.Model):

    # __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class Doctor(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    specialization = db.Column(db.String(100), nullable=False)

class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    medical_history = db.Column(db.Text, nullable=True)