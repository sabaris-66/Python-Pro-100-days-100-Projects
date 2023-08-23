def greet(name, location):
    print("hello coders")
    print(f"this is {name} from {location}")
    print("I'm awesome")


name = input("enter name: ")
greet(name, "blah")

name = input("enter name: ")
location = input("enter location: ")
greet(location=location, name=name)
