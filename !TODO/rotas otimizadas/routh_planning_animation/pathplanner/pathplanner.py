import json

def depth_first_search(graph, current_point, end_point, path, visited):
    # Add the current point to the path
    path.append(current_point)
    
    # Mark the current point as visited
    visited.add(current_point)
    
    # Base case: If the current point is the end point, return
    if current_point == end_point:
        return
    
    # Get the connections of the current point
    connections = graph[current_point]['connections']
    
    # Iterate through the connections
    for next_point in connections:
        # If the next point has not been visited, recursively explore it
        if next_point not in visited:
            depth_first_search(graph, next_point, end_point, path, visited)
            
            # If the end point is found, no need to continue iterating connections
            if path[-1] == end_point:
                return
    
    # If all connections have been visited, go back to the previous point
    if len(visited) != len(graph):
        path.append(path[-2])

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


def plan_path(graph, start_point):
    # Initialize an empty path
    path = []
    
    # Create a set to keep track of visited points
    visited = set()

    # Find the point with the highest alphabetical order
    end_point = max(graph.keys())
    
    # Perform depth_first_search to generate the path
    depth_first_search(graph, start_point, end_point, path, visited)
    
    return path
