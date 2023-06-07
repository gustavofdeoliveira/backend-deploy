import numpy as np
from PIL import Image, ImageDraw
import json

def interpolate_points(start, end, num_points):
    # Interpolate between start and end points
    x = np.linspace(start[0], end[0], num_points)
    y = np.linspace(start[1], end[1], num_points)
    return list(zip(x, y))


def create_robot_path_gif(image_path, graph, path, dot_color=(0, 0, 0), dot_radius=5, output_path="robot_path.gif", duration=500):
    # Load the vent image
    image = Image.open(image_path)

    # Get the size of the image
    image_width, image_height = image.size

    # Create a new image sequence for the GIF
    image_sequence = []

    # Iterate over each point in the path
    for i in range(len(path) - 1):
        # Get the coordinates of the current and next points
        start = graph[path[i]]['coordinates']
        end = graph[path[i + 1]]['coordinates']

        # Interpolate points between the current and next coordinates
        interpolated_points = interpolate_points(start, end, 50)

        # Create frames for each interpolated point
        for coord in interpolated_points:
            # Create a copy of the original image
            frame = image.copy()

            # Create a draw object
            draw = ImageDraw.Draw(frame)

            # Calculate the pixel coordinates from the given coordinates
            pixel_coord = (int(coord[0]), int(coord[1]))

            # Draw the dot on the frame
            draw.ellipse((pixel_coord[0] - dot_radius, pixel_coord[1] - dot_radius,
                          pixel_coord[0] + dot_radius, pixel_coord[1] + dot_radius), fill=dot_color)

            # Append the frame to the image sequence
            image_sequence.append(frame)

    # Save the image sequence as a GIF
    image_sequence[0].save(output_path, save_all=True, append_images=image_sequence[1:], duration=duration, loop=0)

    print("GIF animation created and saved as", output_path)

    return None

def convert_json_to_graph(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Create a mapping dictionary for ID conversion
    id_mapping = {str(i + 1): chr(ord('A') + i) for i in range(len(data))}

    vents_graph = {}

    # Convert the JSON data to the desired format
    for index, item in enumerate(data):
        id = chr(ord('A') + index)
        x = float(item['x'])
        y = float(item['y'])
        connections = [id_mapping[conn.strip()] for conn in item['connections'].split(',')]

        vents_graph[id] = {
            'coordinates': (x, y),
            'connections': connections
        }

    return vents_graph

def get_path_list(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    return data