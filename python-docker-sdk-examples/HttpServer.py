from flask import Flask, jsonify, request, abort
app = Flask(__name__)
tasks = [ { 'id': 1, 'title': 'Buy groceries', 'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 'done': 'False' },
          { 'id': 2, 'title': 'Learn Python', 'description': 'Need to find a good Python tutorial on the web', 'done': 'False' } ]
@app.route('/tasks', methods=['GET']) # end point1 ( Displayall)
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET']) # endpoint-2
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == "__main__":
     app.run(debug=True)