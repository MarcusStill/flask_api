from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# creating an instance of the flask app
app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initializing our database
db = SQLAlchemy(app)


# the class Tasks will inherit the db.Model of SQLAlchemy
class Tasks(db.Model):
    __tablename__ = 'tasks'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(64), nullable=False, comment='Название')
    parent_link = db.Column(db.String(64), nullable=True, comment='Родительская задача')
    dependence = db.Column(db.Boolean, default=False, comment='Зависимая задача: yes=да')
    executor = db.Column(db.String(64), nullable=False, comment='Исполнитель')
    term = db.Column(db.Date, comment='Срок')
    status = db.Column(db.String(20), nullable=False, comment='Статус')

    def json(self):
        return {'id': self.id, 'name': self.name, 'parent_link': self.parent_link, 'dependence': self.dependence,
                'executor': self.executor, 'term': self.term, 'status': self.status}

    def add_task(_name, _parent_link, _dependence, _executor, _term, _status):
        """function to add task to database using"""
        if _dependence == '':
            _dependence = False
        elif _dependence == 'да' or _dependence == 't' or _dependence == 'true' or _dependence == 'True':
            _dependence = True
        if _status == '':
            _status = 'новая'
        if _parent_link == '':
            _parent_link = 'None'
        new_task = Tasks(name=_name, parent_link=_parent_link, dependence=_dependence,
                         executor=_executor, term=_term, status=_status)
        db.session.add(new_task)
        db.session.commit()

    def get_all_tasks():
        """function to get all tasks in our database"""
        return [Tasks.json(task) for task in Tasks.query.all()]

    def get_task(_id):
        """function to get task using the id of the task as parameter"""
        return [Tasks.json(Tasks.query.filter_by(id=_id).first())]

    def update_task(_id, _name, _parent_link, _dependence, _executor, _term, _status):
        """function to update the details of a task"""
        task_to_update = Tasks.query.filter_by(id=_id).first()
        task_to_update.name = _name
        task_to_update.parent_link = _parent_link
        task_to_update.dependence = _dependence
        task_to_update.executor = _executor
        task_to_update.term = _term
        task_to_update.status = _status
        db.session.commit()

    def delete_task(_id):
        """function to delete a task from our database"""
        Tasks.query.filter_by(id=_id).delete()
        db.session.commit()

    def get_task_dependence():
        """function generates a list of tasks that depend on
        from others and not recruited"""
        return [Tasks.json(task) for task in Tasks.query.filter_by(
            dependence='True',
            status='новая'
        )]

    def get_task_parent():
        """function generates a list of tasks that have parent subtasks and are not taken into work"""
        return [Tasks.json(task) for task in Tasks.query.filter_by(
            parent_link='None',
            status='новая'
        )]


# the class Employees will inherit the db.Model of SQLAlchemy
class Employees(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), nullable=False, comment='Фамилия')
    first_name = db.Column(db.String(64), nullable=False, comment='Имя')
    middle_name = db.Column(db.String(64), comment='Отчество')
    function = db.Column(db.String(20), nullable=False, comment='Должность')

    def json(self):
        return {'id': self.id, 'last_name': self.last_name,
                'first_name': self.first_name, 'middle_name': self.middle_name,
                'function': self.function}

    def add_employees(_last_name, _first_name, _middle_name, _function):
        """function to add employees to database"""
        new_employees = Employees(last_name=_last_name, first_name=_first_name, middle_name=_middle_name,
                                  function=_function)
        db.session.add(new_employees)
        db.session.commit()

    def get_all_employees():
        """function to get all employees in our database"""
        return [Employees.json(employees) for employees in Employees.query.all()]

    def get_employees(_id):
        """function to get employee using the id of the employee as parameter"""
        return [Employees.json(Employees.query.filter_by(id=_id).first())]

    def update_employees(_id, _last_name, _first_name, _middle_name, _function):
        """function to update the details of a employees"""
        employees_to_update = Employees.query.filter_by(id=_id).first()
        employees_to_update.last_name = _last_name
        employees_to_update.first_name = _first_name
        employees_to_update.middle_name = _middle_name
        employees_to_update.function = _function
        db.session.commit()

    def delete_employees(_id):
        """function to delete a employees from our database"""
        Employees.query.filter_by(id=_id).delete()
        db.session.commit()


db.create_all()
