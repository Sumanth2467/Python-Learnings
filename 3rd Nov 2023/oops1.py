#Class and obj in python

class Person : #Attributes
    name = None
    age = None
    phone_no = None
    height = None
    gender = None
    proff = None


    #Methods
    def talk(self):
        print("Talk")

    def sleep(self):
        print("Sleep")

    def walk(self):
        return "I am Walking"

sumanth_object = Person()
sumanth_object.name = "Sumanth"
sumanth_object.gender = "Male"
print(sumanth_object)
sumanth_object.sleep()

