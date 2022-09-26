from models import *


# route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_task():
    '''Function to get all the task in the database'''
    return jsonify({'Tasks': Tasks.get_all_tasks()})


# route to get task by id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    return_value = Tasks.get_task(id)
    return jsonify(return_value)


# route to add new task
@app.route('/tasks', methods=['POST'])
def add_task():
    """function to add new task to our database"""
    request_data = request.get_json()
    Tasks.add_task(request_data["name"], request_data["parent_link"], request_data["dependence"],
                   request_data["executor"], request_data["term"], request_data["status"])
    response = Response("Task added", 201, mimetype='application/json')
    return response


# route to update task with PUT method
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """function to edit task in our database using task id"""
    request_data = request.get_json()
    Tasks.update_task(id, request_data["name"], request_data["parent_link"], request_data["dependence"],
                      request_data["executor"], request_data["term"], request_data["status"])
    response = Response("Task Updated", status=200, mimetype='application/json')
    return response


# route to delete task using the DELETE method
@app.route('/tasks/<int:id>', methods=['DELETE'])
def remove_task(id):
    """function to delete task from our database"""
    Tasks.delete_task(id)
    response = Response("Task Deleted", status=200, mimetype='application/json')
    return response

# route to task dependence
@app.route('/task_dependence', methods=['GET'])
def task_dependence():
    """function to get list of dependent tasks"""
    return jsonify({'Tasks': Tasks.get_task_dependence()})


# route to task parent
@app.route('/task_parent', methods=['GET'])
def task_parent():
    """function to get list of parent tasks"""
    return jsonify({'Tasks': Tasks.get_task_parent()})


# route to get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    """Function to get all the employees inthe database"""
    return jsonify({'Employees': Employees.get_all_employees()})


# route to get employee by id
@app.route('/employees/<int:id>', methods=['GET'])
def get_employees_by_id(id):
    return_value = Employees.get_employees(id)
    return jsonify(return_value)


# route to add new employee
@app.route('/employees', methods=['POST'])
def add_employees():
    """function to add new employee to our database"""
    request_data = request.get_json()
    Employees.add_employees(request_data["last_name"], request_data["first_name"],
                            request_data["middle_name"], request_data["function"])
    response = Response("Employee added", 201, mimetype='application/json')
    return response


# route to update employee with PUT method
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employees(id):
    """function to edit employee in our database using task id"""
    request_data = request.get_json()
    Employees.update_employees(id, request_data["last_name"], request_data["first_name"],
                               request_data["middle_name"], request_data["function"])
    response = Response("Employee Updated", status=200, mimetype='application/json')
    return response


# route to delete employee using the DELETE method
@app.route('/employees/<int:id>', methods=['DELETE'])
def remove_employees(id):
    """function to delete employee from our database"""
    Employees.delete_employees(id)
    response = Response("Employees Deleted", status=200, mimetype='application/json')
    return response
