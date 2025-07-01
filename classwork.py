age = 5
is_student = True
name = "Awwal"
height = 4.65

word = "I am {}. It is {} that I am a student. I am {} years old, my height is {}m"


print(f"I am{name}. It is {is_student} that I am a student. I am {age} years old, my height is {height}m")
print(word.format(name, is_student, age, height))
print("I am " + name + "It is " + str(is_student) + "that I am a student. I am " + str(age) + "years old, my height is " + str(height) + "m")

temperature = 29.5
is_raining = False
no_of_cats = 7
name = "Zainab"
mood = "happy"
location = "Lagos"

print("Hello, my name is {}. I live in {} and i have {} cats. It is {} that it is raining today,"
" and the temperature is {}°C. I am feeling {}.".format(name, location, no_of_cats, is_raining, 
                                                        temperature, mood))
print(f"Hello, my name is {name}. I live in {location} and i have {no_of_cats}. It is {is_raining} today and the temperature is{temperature}°C. I am feeling {mood} ")
print("Hello, my name is" + name + ". I live in " + location + "and i have" + no_of_cats + "cats" + ". It is" + is_raining + "that it is raining today," + "and the tempearture is" + temperature + "°C" + ". I am feeling" + mood + ".")


# 5-14-2025
means_of_transport = ["car", "bus", "broom", "lorry", "ship", "boat", "aircraft"]
car, bus, broom, lorry, ship, boat, aircraft = means_of_transport
print("car", car)
print("bus", bus)
print("broom", broom)
print("lorry", lorry)
print("ship", ship)
print("boat", boat)
print("aircraft", aircraft) 
