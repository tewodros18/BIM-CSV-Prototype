#bpy.ops.screen.screenshot(filepath=r"C:\Users\Teddy\Documents\vs_code\GSOC2024\prototype\BIM-CSV-Prototype\static\image\sc.png")
import bpy
from bpy import context
vparea = None
for window in bpy.context.window_manager.windows:
    screen = window.screen
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            vparea = area
            break
with context.temp_override(area=vparea):
    bpy.ops.screen.screenshot_area(filepath=r"C:/Users/Teddy/Documents/vs_code/GSOC2024/prototype/BIM-CSV-Prototype/static/image/snaps/5.png")