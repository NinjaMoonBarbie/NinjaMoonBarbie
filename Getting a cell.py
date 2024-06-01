# Initialize ocean_grid globally
ocean_grid = [[" " for _ in range(10)] for _ in range(10)]

# Define set_cell function to set content in the ocean grid
def set_cell(row, col, content):
    global ocean_grid
    ocean_grid[row][col] = content

# Define get_cell function to retrieve content from ocean grid
def get_cell(row, col):
    global ocean_grid
    return ocean_grid[row][col]

# Define the autopilot function to navigate the ship away from iceberg
def auto_pilot_next_step(titanic_row, titanic_col, ocean_size):
    # Main function to navigate the Titanic away from iceberg
    iceberg_row, iceberg_col = get_iceberg_position(ocean_size)
    if iceberg_row is None or iceberg_col is None:
        return "WEST" # If iceberg position not found, head west

    # Check if ship and iceberg are in the same row
    if titanic_row == iceberg_row:
        if titanic_col < iceberg_col:
            return "EAST"
        else:
            return "NORTH"
    else:
        if titanic_col < iceberg_col:
            return "EAST"
        else:
            return "SOUTH"

# Function to get the position of the iceberg (for simulation purpose)
def get_iceberg_position(ocean_size):
    iceberg_row = ocean_size[0] - 1 # Iceberg always on the bottom row
    iceberg_col = ocean_size[1] - 1 # Iceberg always on the far right side
    return iceberg_row, iceberg_col

# Draw ocean
def draw_ocean():
    global ocean_grid # Access global ocean grid

    # Loop through each row
    for row in range(10):
        # Loop through each column
        for col in range(10):
            # Set content of each cell to new character
            set_cell(row, col, "🟦")

    # Print ocean grid
    for row in ocean_grid:
        print(" ".join(row))

# Call check_for_ice_cube to detect ice cube at (3, 7)
val = get_cell(3, 7) # Assuming checking for ice cube at this position
if val == "🧊":
    print("The Titanic was saved and successfully avoided the Iceberg!")
    # Assuming the Titanic starts at a random position
    titanic_row = 0
    titanic_col = 0
    ocean_size = (10, 10) # Assuming ocean size is (10, 10)
    while titanic_col < ocean_size[1] - 1:
        next_step = auto_pilot_next_step(titanic_row, titanic_col, ocean_size)
        if next_step == "NORTH":
            titanic_row -= 1
        elif next_step == "SOUTH":
            titanic_row += 1
        elif next_step == "WEST":
            titanic_col -= 1
        elif next_step == "EAST":
            titanic_col += 1
        else:
            print("Invalid direction")

        draw_ocean() # Draw the ocean after each move
        print(f"Titanics's position: Row {titanic_row}, Column {titanic_col}")
    else:
        print("The Titanic crashed")

    # Draw ocean with updated ice cube position
    draw_ocean()







