# Initialize application and empty roster
print("Welcome to my Basketball Roster Program")
my_roster = []

# Collect starting lineup input from user
point_guard = input("Who is your point guard: ").title()
my_roster.append(point_guard)
shooting_guard = input("Who is your shooting guard: ").title()
my_roster.append(shooting_guard)
small_forward = input("Who is your small forward: ").title()
my_roster.append(small_forward)
power_forward = input("Who is your power forward: ").title()
my_roster.append(power_forward)
center = input("Who is your center: ").title()
my_roster.append(center)


# Display initial roster
print("\n\tYour Starting 5 for the upcoming Basketball season")
print(f"\tPoint guard:\t{my_roster[0]}")
print(f"\tShooting Guard:\t{my_roster[1]}")
print(f"\tSmall Forward:\t{my_roster[2]}")
print(f"\tPower Forward:\t{my_roster[3]}")
print(f"\tCenter:\t\t{my_roster[4]}")


# Handle player injury simulation
injured_player = my_roster.pop(2) 
print(f"\nOh no, {injured_player} is injured")
print("Your roster only has 4 players now")

# Process replacement player
added_player = input(f"Who will take {injured_player}'s spot? ").title()
my_roster.insert(2, added_player)  # Insert the new player at index 2

# Display final roster and closing messages
print("\n\tYour New Starting 5 for the upcoming Basketball season")
print(f"\tPoint guard:\t{my_roster[0]}")
print(f"\tShooting Guard:\t{my_roster[1]}")
print(f"\tSmall Forward:\t{my_roster[2]}")
print(f"\tPower Forward:\t{my_roster[3]}")
print(f"\tCenter:\t\t{my_roster[4]}")

print(f"\nGood Luck {my_roster[2]} you will do great! ")
print("Your roster now has 5 players ")
print("Thank you for testing my app!")


