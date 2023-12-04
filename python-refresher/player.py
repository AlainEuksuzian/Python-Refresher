class player:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def setName(self,name_input: str):
        self.__name = name_input

    def getName(self):
        return self.__name
    
    def setAge(self, age_input):
        self.__age = age_input

    def getAge(self):
        return self.__age
