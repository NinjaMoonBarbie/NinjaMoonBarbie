# Modify the Ocean
# Initialize ocean_grid globally
ocean_grid = [[" " for _ in range(10)] for _ in range(10)]

# Define set_cell function to set content in the ocean grid
def set_cell(row, col, content):
    global ocean_grid
    ocean_grid[row][col] = content

# Define get_cell function to retrieve content from the ocean grid
def get_cell(row, col):
    global ocean_grid
    return ocean_grid[row][col]

# Define a function to check if there is an ice cube at a given position
def check_for_ice_cube(row, col):
    content = get_cell(row, col)
    if content == "🧊":
        return True
    else:
        return False

# Define autopilot to navigate ship away from ice cube
def auto_pilot_next_step(titanic_row, titanic_col, ocean_grid):
    # Main function to navigate Titanic away from ice cube
    iceberg_row, iceberg_col = get_iceberg_position(len(ocean_grid))
    if iceberg_row is None or iceberg_col is None:
        return "WEST" # If iceberg position not found

    # To check if ship and iceberg are in same row
    if titanic_row == iceberg_row:
        return "NORTH"
    else:
        return "SOUTH" # If iceberg not in same row

# Draw the ocean
def draw_ocean():
    global ocean_grid # Access global ocean grid

    # Loop through each row
    for row in range(10):
        # Loop through each column
        for col in range(10):
            # Set content of each cell to new character
            set_cell(row, col, "🟦")

    # Assuming an ice cube in position(3, 7)
    set_cell(3, 7, "🧊")

    # Print ocean grid
    for row in ocean_grid:
        print(" ".join(row))

# Call get_cell here -> in ()
val = check_for_ice_cube(3, 7)
if val:
    print("Titanic Saved!")
else:
    print("Titanic crashed!")

draw_ocean()
