class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def bio_data(self):
        print(f"{self.name} is the student of age {self.age}")
        
s = Student('Raghib',19)
s.bio_data()
