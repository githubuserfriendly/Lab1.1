from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response
    
    
@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied
    

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

@app.route('/stats')
def get_stats():
    chicken = 0
    fish = 0
    cs = 0
    it = 0
    cs_special = 0
    it_special = 0
    for student in data:
        if student['pref'] == 'Chicken':
            chicken += 1
        elif student['pref'] == 'Fish':
            fish += 1
        if student['programme'] == 'Computer Science (Special)':
            cs_special += 1
        elif student['programme'] == 'Information Technology (Special)':
            it_special += 1
        if student['programme'] == 'Computer Science (Major)':
            cs += 1
        elif student['programme'] == 'Information Technology (Major)':
            it += 1
    return jsonify({
        'Chicken': chicken,
        'Fish': fish,
        'Computer Science (Special)': cs_special,
        'Information Technology (Special)': it_special,
        'Computer Science': cs,
        'Information Technology': it
    })

app.run(host='0.0.0.0', port=8080, debug=True)
