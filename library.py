def cm_to_inches(length_cm):
    if length_cm < 0:
        return -1 * length_cm
    else:
        conversion_factor = 0.393701
        length_inches = length_cm * conversion_factor
        rounded_length_inches = round(length_inches, 2)
        return rounded_length_inches


# length_in_cm = 20
# result = cm_to_inches(length_in_cm)
# print(f'{length_in_cm} sm = {result} inch.')
