# This is problem to convert all the negative coordinates to a positive coordinates;
# The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
# We can add or delete any number from the coordinates ; however graph should not be changed;

# Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
# Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]

def convert_to_positive_coordinates(coordinates):
    # Find the minimum x-coordinate and y-coordinate
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)

    # Shift the coordinates to positive values
    shifted_coordinates = [(coord[0] + abs(min_x), coord[1] + abs(min_y)) for coord in coordinates]

    return shifted_coordinates

# Test the function with the provided input
input_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coordinates = convert_to_positive_coordinates(input_coordinates)
print(output_coordinates)
