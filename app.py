from flask import Flask, render_template, jsonify
import random
from datetime import datetime
import socket

app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/datapoint')
def api_datapoint():
    command = """
import bpy
#obj = bpy.context.active_object
#mesh = obj.data
walls = [[obj.name,obj.BIMObjectProperties.ifc_definition_id] for obj in bpy.context.scene.objects if obj.name.startswith("IfcWall")]
print(walls)
"""
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 5235))
    clientsocket.sendall(command.encode())
    while True:
        res = clientsocket.recv(4096)
        if not res:
            break
        random_number = res.decode()
    clientsocket.close()
    double_random_number = random_number * 2
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    dictionary_to_return = {
        'random_number': random_number,
        'double_random_number': double_random_number,
        'timestamp': timestamp
    }

    return jsonify(dictionary_to_return)




@app.route('/api/datapointSlab')
def api_datapointSlab():
    command = """
import bpy
#obj = bpy.context.active_object
#mesh = obj.data
walls = [[obj.name,obj.BIMObjectProperties.ifc_definition_id] for obj in bpy.context.scene.objects if obj.name.startswith("IfcSlab")]
print(walls)
"""
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 5235))
    clientsocket.sendall(command.encode())
    while True:
        res = clientsocket.recv(4096)
        if not res:
            break
        random_number = res.decode()
    clientsocket.close()
    double_random_number = random_number * 2
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    dictionary_to_return = {
        'random_number': random_number,
        'double_random_number': double_random_number,
        'timestamp': timestamp
    }

    return jsonify(dictionary_to_return)

app.run(host='0.0.0.0', port=8080, debug=True)


#mesh = obj.data
#print(len(mesh.polygons))