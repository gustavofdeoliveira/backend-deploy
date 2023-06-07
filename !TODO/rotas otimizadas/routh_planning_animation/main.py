import pathplanner.pathplanner as pp
from pprint import pprint
import pathpainter.pathpainter as ppaint

#json_file = 'routh_planning_animation/caminho_robo.json'
json_file = "static/trajetoria/points.json"
start_point = 'A'
end_point = 'H'

# Image paths
image_path = "static/images/user_image.png"
animation_output_path = "routh_planning_animation/robot_path.gif"

# Animation parameters
dot_color = (0, 0, 0)
dot_radius = 10
duration = 50

# Convert the JSON file to a graph
graph_vents = pp.convert_json_to_graph(json_file)
print("\nGraph representing the possible paths in vents".upper())
pprint(graph_vents)

# Plan the path
vents_planned_path = pp.plan_path(graph_vents, start_point)
print("\nThe optmized path".upper())
print(vents_planned_path)

# Create the animation
ppaint.create_robot_path_gif(image_path, graph_vents, vents_planned_path, dot_color, dot_radius, animation_output_path, duration)