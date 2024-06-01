# Ocean functions

def get_cell(row, col):
    # Function to get the content of a cell in the ocean grid
    pass  # Placeholder for actual implementation

def get_all_positions():
    # Function to iterate over all positions in the ocean grid
    pass  # Placeholder for actual implementation

def get_iceberg_position():
    # Function to get the position of the iceberg in the ocean grid
    for row, col in get_all_positions():
        if get_cell(row, col) == '🧊':
            return row, col
    return None, None

def is_in_danger(titanic_row, titanic_col, iceberg_row, iceberg_col):
    # Function to determine if the Titanic is in danger of colliding with the iceberg
    return abs(titanic_row - iceberg_row) <= 1 and abs(titanic_col - iceberg_col) <= 1

def avoid_iceberg(titanic_row, titanic_col, iceberg_row, iceberg_col):
    # Function to calculate the safest direction to navigate away from the iceberg
    if titanic_row < iceberg_row:
        return 'SOUTH'
    elif titanic_row > iceberg_row:
        return 'NORTH'
    elif titanic_col < iceberg_col:
        return 'EAST'
    else:
        return 'WEST'

def auto_pilot_next_step(titanic_row, titanic_col, ocean_size):
    # Main function to navigate the Titanic away from the iceberg
    iceberg_row, iceberg_col = get_iceberg_position()
    if iceberg_row is None or iceberg_col is None:
        return 'WEST'  # If iceberg position not found, head west
    elif is_in_danger(titanic_row, titanic_col, iceberg_row, iceberg_col):
        return avoid_iceberg(titanic_row, titanic_col, iceberg_row, iceberg_col)
    else:
        return 'WEST'  # Move towards the west side of the ocean

# Testing the function
# Replace the function calls with actual values when testing
# Example:
# direction = auto_pilot_next_step(titanic_row, titanic_col, ocean_size)




