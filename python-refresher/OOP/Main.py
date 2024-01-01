from Question1 import Pet
from Question3 import Person


def question_one():
    name, the_type, age = get_user_input()
    create_animal(name, the_type, age)


def get_user_input():
    name = input('enter the name of your animal: ')
    animal_type = input('enter the type of animal: ')
    age = int(input('enter the age of your animal: '))
    return name, animal_type, age

def create_animal(name: str, animal_type: str, age: int):
    my_pet = Pet(name, animal_type, age)
    print(my_pet)

 #------------------------------------------------------------------------------
    

def question_three():
    name = input('enter your name: ')
    addess = input('enter your address: ')
    age = input("enter your age: ")
    phone = input('enter your phone: ')

    Person_one = Person('alain', '1234 addy', 30, '123456789')
    Person_two = Person(name, addess, age, phone)

    print(Person_one.equals(Person_two))


question_three()