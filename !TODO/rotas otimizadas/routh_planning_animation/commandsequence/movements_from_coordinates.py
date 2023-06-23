sequence = {
    'P0': [2, 1],  # Initial position [x, y]
    'P1': [2, 2],  # Next position [x, y]
    'P2': [5, 2],  # Next position [x, y]
    'P3': [5, 3],  # Next position [x, y]
    'P4': [3, 3],  # Next position [x, y]
    'P5': [3, 5],  # Next position [x, y]
    'P6': [2, 5],  # Final position [x, y]
}

commands = {}
counter = 0
orientation = 0  # To keep track of the orientation of the robot and shift the cartesian plane accordingly
current_position = sequence['P0']  # Current position initialized to the starting position

for i in range(len(sequence) - 1):
    dx = sequence[f'P{i + 1}'][0] - sequence[f'P{i}'][0]  # Change in x-coordinate
    dy = sequence[f'P{i + 1}'][1] - sequence[f'P{i}'][1]  # Change in y-coordinate

    if dx != 0:  # If there is a change in the x-coordinate
        commands[f'C{counter}'] = {'F': abs(dx)}  # Move forward by |dx| units
        counter += 1

        if dx > 0:  # If the distance in the x-coordinate that the robot has to move is positive
            if orientation == 0:  # If the current orientation is 0 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            elif orientation == 90:  # If the current orientation is 90 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            elif orientation == 180:  # If the current orientation is 180 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            elif orientation == 270:  # If the current orientation is 270 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            orientation = (orientation + 90) % 360  # Update the orientation by adding 90 degrees
        else:  # If the distance in the x-coordinate that the robot has to move is negative
            if orientation == 0:  # If the current orientation is 0 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            elif orientation == 90:  # If the current orientation is 90 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            elif orientation == 180:  # If the current orientation is 180 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            elif orientation == 270:  # If the current orientation is 270 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            orientation = (orientation + 270) % 360  # Update the orientation by adding 270 degrees
        counter += 1
        current_position[0] += dx  # Update the current x-coordinate based on the change

    if dy != 0:  # If there is a change in the y-coordinate
        commands[f'C{counter}'] = {'F': abs(dy)}  # Move forward by |dy| units
        counter += 1

        if dy > 0:  # If the distance in the y-coordinate that the robot has to move is positive
            if orientation == 0:  # If the current orientation is 0 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            elif orientation == 90:  # If the current orientation is 90 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            elif orientation == 180:  # If the current orientation is 180 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            elif orientation == 270:  # If the current orientation is 270 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            orientation = (orientation + 90) % 360  # Update the orientation by adding 90 degrees
        else:  # If the distance in the y-coordinate that the robot has to move is negative
            if orientation == 0:  # If the current orientation is 0 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            elif orientation == 90:  # If the current orientation is 90 degrees
                commands[f'D{counter}'] = {'L': 90}  # Turn left 90 degrees
            elif orientation == 180:  # If the current orientation is 180 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            elif orientation == 270:  # If the current orientation is 270 degrees
                commands[f'D{counter}'] = {'R': 90}  # Turn right 90 degrees
            orientation = (orientation + 270) % 360  # Update the orientation by adding 270 degrees
        counter += 1
        current_position[1] += dy  # Update the current y-coordinate based on the change

print(commands)  # Print the generated dictionary commands