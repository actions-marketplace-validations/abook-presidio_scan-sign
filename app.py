from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)
tasks = [
  {
    'id': 1, 
    'title': u'Buy groceries',
    'description': u'Milk, Cheese, Pizza',
    'done': False
  },
  {
    'id': 2, 
     'title': u'Learn Python', 
     'description': u'Need to find a good tutorial',
     'done': False
  }
]

# curl -i -H "Content-Type: application/json" -X POST -d '{"cloud":"Azure"}' http://localhost:5000/sss/v1
# curl -i -H "Content-Type: application/json" -X POST -d '{"cloud":"AWS"}' http://localhost:5000/sss/v1
@app.route ('/sss/v1', methods=['POST'])
def check_entries():
    if not request.json or not 'cloud' in request.json:
        abort(400)
    cloud = request.json['cloud']
    sss = {
       'cloud': cloud,
       'done': False
    }
    return jsonify({'sss': sss}), 201

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    

if __name__ == '__main__':
    app.run(debug=True)
