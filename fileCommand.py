import bpy
#bpy.ops.mesh.primitive_cube_add()
#obj = bpy.context.active_object
#mesh = obj.data
walls = [[obj.name,obj.BIMObjectProperties.ifc_definition_id] for obj in bpy.context.scene.objects if obj.name.startswith("Ifc")]
#print(obj.name)
print(walls)