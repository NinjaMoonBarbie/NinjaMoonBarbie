def auto_pilot_next_step(titanic_row, titanic_col, ocean_size):
    iceberg_row, iceberg_col = None, None
    # Find the iceberg position
    for row in range(ocean_size):
        for col in range(ocean_size):
            if get_cell(row, col) == "🧊":
                iceberg_row, iceberg_col = row, col

    if iceberg_row is None:
        return "WEST"

    if titanic_row == 0 and iceberg_row == 0:
        return "SOUTH"
    elif titanic_row == iceberg_row and iceberg_row >= 0:
        return "NORTH"
    else:
        return "WEST"


# This made the quiz in Sprint 3 pass!