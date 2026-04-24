import logic
print(dir(logic))


from logic import calculate_visibility

print("QA TEST RUN STARTED\n")

print("Test 1:", calculate_visibility(0.8, 0, True, "day") == "HIDDEN")
print("Test 2:", calculate_visibility(0.8, 2, False, "night") == "VISIBLE")
print("Test 3:", calculate_visibility(0.8, 1, False, "night") == "SEMI_VISIBLE")
print("Test 4:", calculate_visibility(0.3, 0, False, "day") == "VISIBLE")

print("\nDONE")
