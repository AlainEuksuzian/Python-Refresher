"""Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate accessor and mutator methods. Also, write a program that creates 
three instances of the class. One instance should hold your information, and the other two 
should hold your friends’ or family members’ information."""


class Person:
    def __init__(self, name=None, address=None, age=None, phone=None):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, addy):
        self.__address = addy
    
    def set_age(self, age):
        self.__age = age
    
    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone

    def equals(self,obj):
        return (self.get_name() == obj.get_name()) and (self.get_address() 
                                                        == obj.get_address()) and (self.get_age() 
                                                                                   == obj.get_age()) and (self.get_phone() 
                                                                                                          == obj.get_phone())

    def __str__(self):
        return "the persons name: " + str(self.get_name()) + "\nthe persons address: " + str(self.get_address()) + "\nthe persons age: " + str(self.get_age()) + "\nthe pesons phone: " + str(self.get_phone())