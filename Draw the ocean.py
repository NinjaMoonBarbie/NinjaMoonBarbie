# Draw the ocean
def draw_ocean():
    ocean = "█" # Define block character

    ocean_grid = "" # Create an empty string to store ocean grid

    # Loop through each row
    for _ in range(10):
        # Loop through each column
        for _ in range(10):
            # Add full block character instead of empty ocean grid
            ocean_grid += ocean + " "
        # Add a newline character at the end of each row
        ocean_grid += '\n'

    # Print ocean grid
    print(ocean_grid)

# Call draw_ocean to print ocean grid
draw_ocean()



