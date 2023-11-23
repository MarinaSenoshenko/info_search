from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, logout_user, login_user, LoginManager, UserMixin, current_user

from student_form import StudentForm
from university_form import UniversityForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwerty@localhost:5432/userdata"
app.config['SECRET_KEY'] = "very long key very long key very long key very long key very long key"
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = Users.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect('/')
        return "Invalid username or password"
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    small_name = db.Column(db.String)
    date = db.Column(db.Date)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.Date)
    university = db.Column(db.Integer, db.ForeignKey('university.id'))
    year = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


with app.app_context():
    db.create_all()
    db.session.commit()


@app.route('/')
def index():
    universities = University.query.all()
    students = Student.query.all()
    student_form = StudentForm()
    university_form = UniversityForm()

    if current_user.is_authenticated:
        login_logout_link = 'logout'
    else:
        login_logout_link = 'login'

    return render_template('main_page.html', universities=universities, students=students,
                           student_form=student_form,
                           university_form=university_form,
                           login_logout_link=login_logout_link)


@app.route('/add_university', methods=['GET', 'POST'])
@login_required
def add_university():
    if request.method == 'POST':
        full_name = request.form.get("full_name")
        small_name = request.form.get("small_name")
        date = request.form.get("date")

        latest_university = University.query.order_by(University.id.desc()).first()
        new_id = latest_university.id + 1 if latest_university else 1

        university = University(id=new_id, full_name=full_name, small_name=small_name, date=date)
        university.save()

        return redirect('/')

    return "Invalid request method"


@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        name = request.form.get("name")
        date = request.form.get("date")
        university = request.form.get("university")
        year = request.form.get("year")

        if University.query.filter_by(id=university).first() is None:
            return "University does not exist"

        latest_student = Student.query.order_by(Student.id.desc()).first()
        new_id = latest_student.id + 1 if latest_student else 1

        student = Student(id=new_id, name=name, date=date, university=university, year=year)
        student.save()

        return redirect('/')

    return "Invalid request method"


@app.route('/update_student/<int:student_id>', methods=['POST'])
@login_required
def update_student(student_id):
    if request.method == 'POST':
        data = request.json
        field_name = data.get('field')
        new_value = data.get('value')

        student = Student.query.get(student_id)

        if field_name == 'name':
            student.name = new_value
        elif field_name == 'date_born':
            student.date = new_value
        elif field_name == 'university':
            student.university = new_value
        elif field_name == 'year':
            student.year = new_value

        student.save()

        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


@app.route('/update_university/<int:university_id>', methods=['POST'])
@login_required
def update_university(university_id):
    if request.method == 'POST':
        data = request.json
        field_name = data.get('field')
        new_value = data.get('value')

        university = University.query.get(university_id)

        if field_name == 'full_name':
            university.full_name = new_value
        elif field_name == 'small_name':
            university.small_name = new_value
        elif field_name == 'date_create':
            university.date = new_value

        university.save()

        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


@app.route('/delete_student/<int:student_id>', methods=['GET', 'POST'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        student.delete()
        return redirect('/')
    return "Student not found"


@app.route('/delete_university/<int:university_id>', methods=['GET', 'POST'])
def delete_university(university_id):
    university = University.query.get(university_id)
    if university:
        students = Student.query.filter_by(university=university.id).all()
        if students:
            return "University has students"
        university.delete()
        return redirect('/')
    return "University not found"


if __name__ == '__main__':
    app.run(debug=True)

