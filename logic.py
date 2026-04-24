
def calculate_visibility(grass_density, player_speed, is_crouching, time_of_day):
    if player_speed == 2:
        return "VISIBLE"

    if grass_density >= 0.7 and is_crouching:
        return "HIDDEN"

    if player_speed == 1:
        if grass_density >= 0.7 and time_of_day == "night":
            return "SEMI_VISIBLE"
        return "VISIBLE"

    if player_speed == 0:
        if grass_density >= 0.5:
            return "SEMI_VISIBLE"
        return "VISIBLE"

    return "VISIBLE"
