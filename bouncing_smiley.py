"""
Bouncing Smiley Face - Blender Script
======================================
Abre Blender, ve a Scripting > New, pega este script y presiona "Run Script".
La animacion tiene 120 frames. Presiona Space para reproducirla.
"""

import bpy
import math

# ---------------------------------------------------------------------------
# 1. Limpiar la escena
# ---------------------------------------------------------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Eliminar materiales huerfanos
for mat in bpy.data.materials:
    if mat.users == 0:
        bpy.data.materials.remove(mat)

# ---------------------------------------------------------------------------
# 2. Materiales
# ---------------------------------------------------------------------------
def create_material(name, color):
    """Crea un material con el color RGBA dado."""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = color
    return mat

mat_yellow = create_material("Yellow", (1.0, 0.85, 0.0, 1.0))
mat_black  = create_material("Black",  (0.02, 0.02, 0.02, 1.0))
mat_white  = create_material("White",  (1.0, 1.0, 1.0, 1.0))
mat_red    = create_material("Red",    (0.9, 0.15, 0.15, 1.0))

# ---------------------------------------------------------------------------
# 3. Construir la cara (smiley)
# ---------------------------------------------------------------------------

# --- Cabeza (esfera amarilla) ---
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0), segments=64, ring_count=32)
head = bpy.context.active_object
head.name = "Smiley_Head"
head.data.materials.append(mat_yellow)
bpy.ops.object.shade_smooth()

# --- Ojo izquierdo (esfera blanca + pupila negra) ---
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.18, location=(-0.32, -0.85, 0.25), segments=32, ring_count=16)
eye_l_white = bpy.context.active_object
eye_l_white.name = "Eye_L_White"
eye_l_white.data.materials.append(mat_white)
bpy.ops.object.shade_smooth()

bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(-0.32, -0.93, 0.25), segments=32, ring_count=16)
eye_l_pupil = bpy.context.active_object
eye_l_pupil.name = "Eye_L_Pupil"
eye_l_pupil.data.materials.append(mat_black)
bpy.ops.object.shade_smooth()

# --- Ojo derecho ---
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.18, location=(0.32, -0.85, 0.25), segments=32, ring_count=16)
eye_r_white = bpy.context.active_object
eye_r_white.name = "Eye_R_White"
eye_r_white.data.materials.append(mat_white)
bpy.ops.object.shade_smooth()

bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(0.32, -0.93, 0.25), segments=32, ring_count=16)
eye_r_pupil = bpy.context.active_object
eye_r_pupil.name = "Eye_R_Pupil"
eye_r_pupil.data.materials.append(mat_black)
bpy.ops.object.shade_smooth()

# --- Sonrisa (torus cortado / curva) ---
bpy.ops.curve.primitive_bezier_circle_add(radius=0.5, location=(0, -0.82, -0.2))
smile_curve = bpy.context.active_object
smile_curve.name = "Smile"

# Ajustar la curva para que sea un arco (sonrisa)
smile_curve.data.bevel_depth = 0.045
smile_curve.data.bevel_resolution = 4

# Editar los puntos de control para formar una sonrisa
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.curve.select_all(action='SELECT')
bpy.ops.object.mode_set(mode='OBJECT')

# Acceder a los puntos y modificarlos para crear un arco de sonrisa
spline = smile_curve.data.splines[0]
points = spline.bezier_points

# Configurar 4 puntos como arco de sonrisa (semicirculo inferior)
points[0].co = (-0.5, 0.0, 0.0)
points[0].handle_left = (-0.5, 0.25, 0.0)
points[0].handle_right = (-0.5, -0.25, 0.0)

points[1].co = (0.0, -0.35, 0.0)
points[1].handle_left = (-0.25, -0.35, 0.0)
points[1].handle_right = (0.25, -0.35, 0.0)

points[2].co = (0.5, 0.0, 0.0)
points[2].handle_left = (0.5, -0.25, 0.0)
points[2].handle_right = (0.5, 0.25, 0.0)

# El 4to punto lo ocultamos arriba para cerrar la curva visualmente
points[3].co = (0.0, 0.15, 0.0)
points[3].handle_left = (0.25, 0.15, 0.0)
points[3].handle_right = (-0.25, 0.15, 0.0)

# Hacer la curva abierta (no cerrada) - solo mostrar el arco inferior
spline.use_cyclic_u = False

# Solo necesitamos los 3 primeros puntos (arco)
smile_curve.data.materials.append(mat_red)

# Rotar para que mire al frente
smile_curve.rotation_euler = (math.radians(90), 0, 0)

# ---------------------------------------------------------------------------
# 4. Emparentar todo a la cabeza
# ---------------------------------------------------------------------------
parts = [eye_l_white, eye_l_pupil, eye_r_white, eye_r_pupil, smile_curve]
for part in parts:
    part.parent = head

# ---------------------------------------------------------------------------
# 5. Animacion de rebote
# ---------------------------------------------------------------------------
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 120
scene.render.fps = 24

# Posiciones clave para el rebote
# El smiley cae desde arriba, rebota en el "suelo" (Z=1) con squash & stretch
bounce_keyframes = [
    # (frame, z_position, scale_z, scale_xy)
    (1,   5.0, 1.0, 1.0),    # Arriba
    (20,  1.0, 0.65, 1.3),   # Impacto 1 (squash)
    (24,  1.0, 1.0, 1.0),    # Recupera forma
    (40,  3.5, 1.1, 0.95),   # Rebote 1 (stretch)
    (55,  1.0, 0.7, 1.25),   # Impacto 2
    (59,  1.0, 1.0, 1.0),    # Recupera
    (72,  2.5, 1.08, 0.96),  # Rebote 2
    (84,  1.0, 0.75, 1.2),   # Impacto 3
    (87,  1.0, 1.0, 1.0),    # Recupera
    (96,  1.8, 1.05, 0.97),  # Rebote 3
    (105, 1.0, 0.8, 1.15),   # Impacto 4
    (108, 1.0, 1.0, 1.0),    # Recupera
    (114, 1.3, 1.02, 0.99),  # Rebote 4
    (120, 1.0, 1.0, 1.0),    # Reposo final
]

for frame, z, sz, sxy in bounce_keyframes:
    head.location = (0, 0, z)
    head.scale = (sxy, sxy, sz)
    head.keyframe_insert(data_path="location", frame=frame)
    head.keyframe_insert(data_path="scale", frame=frame)

# Hacer las curvas de animacion mas suaves (ease in/out)
if head.animation_data and head.animation_data.action:
    for fcurve in head.animation_data.action.fcurves:
        for kf in fcurve.keyframe_points:
            kf.interpolation = 'BEZIER'
            kf.easing = 'AUTO'

# Rotacion ligera durante el rebote (giro divertido)
rotation_keyframes = [
    (1,   0.0),
    (20,  math.radians(10)),
    (40,  math.radians(-8)),
    (55,  math.radians(6)),
    (72,  math.radians(-4)),
    (84,  math.radians(3)),
    (96,  math.radians(-2)),
    (120, 0.0),
]

for frame, rot_y in rotation_keyframes:
    head.rotation_euler = (0, rot_y, 0)
    head.keyframe_insert(data_path="rotation_euler", frame=frame)

# ---------------------------------------------------------------------------
# 6. Suelo
# ---------------------------------------------------------------------------
bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, 0))
floor = bpy.context.active_object
floor.name = "Floor"
mat_floor = create_material("Floor_Gray", (0.35, 0.35, 0.4, 1.0))
floor.data.materials.append(mat_floor)

# ---------------------------------------------------------------------------
# 7. Iluminacion y camara
# ---------------------------------------------------------------------------

# Luz principal
bpy.ops.object.light_add(type='SUN', location=(3, -3, 8))
sun = bpy.context.active_object
sun.name = "Sun"
sun.data.energy = 3.0
sun.rotation_euler = (math.radians(40), math.radians(15), math.radians(-20))

# Luz de relleno
bpy.ops.object.light_add(type='AREA', location=(-3, -4, 4))
fill = bpy.context.active_object
fill.name = "Fill_Light"
fill.data.energy = 50
fill.data.size = 3

# Camara
bpy.ops.object.camera_add(location=(0, -7, 3.5))
cam = bpy.context.active_object
cam.name = "Camera"
cam.rotation_euler = (math.radians(75), 0, 0)
scene.camera = cam

# ---------------------------------------------------------------------------
# 8. Configuracion de render
# ---------------------------------------------------------------------------
scene.render.engine = 'BLENDER_EEVEE_NEXT' if bpy.app.version >= (4, 0, 0) else 'BLENDER_EEVEE'
scene.render.resolution_x = 1280
scene.render.resolution_y = 720

# Fondo de color cielo
scene.world = bpy.data.worlds.get("World") or bpy.data.worlds.new("World")
scene.world.use_nodes = True
bg_node = scene.world.node_tree.nodes.get("Background")
if bg_node:
    bg_node.inputs["Color"].default_value = (0.4, 0.6, 0.9, 1.0)
    bg_node.inputs["Strength"].default_value = 1.0

# Ir al frame 1 y poner en modo vista previa
scene.frame_set(1)

print("=" * 50)
print("  Smiley Face Rebotando - Listo!")
print("  Presiona SPACE para reproducir la animacion.")
print("  Frames: 1-120 | FPS: 24")
print("=" * 50)
