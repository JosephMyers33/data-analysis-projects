# 1. Declare and assign the variables here:
name_of_shuttle = "Determination"
shuttle_speed_mph = 17500
Dist_to_mars_km = 225000000
Dist_to_moon_km = 384400
Mile_per_kilo = .621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(name_of_shuttle))
print(type(shuttle_speed_mph))
print(type(Dist_to_mars_km))
print(type(Dist_to_moon_km))
print(type(Mile_per_kilo))
# Code your solution to exercises 3 and 4 here:
miles_to_mars = Dist_to_mars_km * Mile_per_kilo
hours_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hours_to_mars / 24
print (name_of_shuttle, "will take", days_to_mars, "days to reach Mars.")
# Code your solution to exercise 5 here
miles_to_moon = Dist_to_moon_km * Mile_per_kilo
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print (name_of_shuttle, "will take", days_to_moon, "days to reach the Moon.")