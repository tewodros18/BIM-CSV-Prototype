from flask import Flask, render_template, jsonify, send_file
from datetime import datetime
import socket
import base64
import os

app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html')
@app.route('/loadIFC')
def load_ifc():
  return render_template('ifc_csv_load.html')
@app.route('/ganttChart')
def ganttChart():
  return render_template('gantt.html')
@app.route('/getpic', methods=['GET'])
def getpic():
   filpath = "./static/image/snaps/"
   imgs = []
   for file_names in os.listdir(filpath):
      with open(filpath+file_names, "rb") as image_file:
        data = base64.b64encode(image_file.read())
        data = data.decode()
        imgs.append('"data:image/png;base64,{}"'.format(data))
   
   return jsonify(imgs)

@app.route('/takesnap')
def takeSnap():
    #print('{}'.format(img))
    filpath = "./static/image/snaps/"
    img = "0.png"
    for file_names in os.listdir(filpath):
        img = file_names
    img = str(int(img.split(".")[0]) + 1) + ".png"
    command = """
import bpy
bpy.ops.screen.screenshot(filepath=r"C:/Users/Teddy/Documents/vs_code/GSOC2024/prototype/BIM-CSV-Prototype/static/image/snaps/{}")
""".format(img)
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 5232))
    clientsocket.sendall(command.encode())
    while True:
        res = clientsocket.recv(4096)
        if not res:
            break
    clientsocket.close()
    return ""

@app.route('/getnewpic', methods=['GET'])
def getnewpic():
    filpath = "./static/image/snaps/"
    img = "0.png"
    for file_names in os.listdir(filpath):
        img = file_names
    with open(filpath+img, "rb") as image_file:
        data = base64.b64encode(image_file.read())
    data = data.decode()
    return '"data:image/png;base64,{}"'.format(data)
@app.route('/api/datapoint')
def api_datapoint():
    command = """
import bpy
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



    

app.run(host='0.0.0.0', port=8080, debug=True)

#mesh = obj.data
#print(len(mesh.polygons))