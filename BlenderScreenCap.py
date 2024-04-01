BlenderScreenCapcommand = """
import bpy
from bpy import context
a = []
for window in bpy.context.window_manager.windows:
    screen = window.screen
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == "WINDOW":
                    a = [window,screen,area,region,bpy.context.scene]
with context.temp_override(window = a[0],screen = a[1],area = a[2]):
    bpy.ops.screen.screenshot_area(filepath=r"C:/Users/Teddy/Documents/vs_code/GSOC2024/prototype/BIM-CSV-Prototype/static/image/snaps/{}")"""