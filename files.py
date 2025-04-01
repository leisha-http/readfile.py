file = open("example.txt", "r")
data = file.read() 
print(data)
with open("example.txt", "w") as file:
    file.write("hello to my new world")
    print(data)

try:
    file = open("world.txt", "r")
    data = file.read()
    print("new world:", world)
except FileNotFoundError:
    print("Sorry, this file does not exist")