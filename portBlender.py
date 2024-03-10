import socket


def send_command(command):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 5235))
    clientsocket.sendall(command.encode())
    while True:
        res = clientsocket.recv(4096)
        if not res:
            break
        print(res.decode())
    clientsocket.close()

send_command("""
import bpy
#bpy.ops.mesh.primitive_cube_add()
#obj = bpy.context.active_object
#mesh = obj.data
walls = [[obj.name,obj.BIMObjectProperties.ifc_definition_id] for obj in bpy.context.scene.objects if obj.name.startswith("Ifc")]
#print(obj.name)
print(walls)
""")