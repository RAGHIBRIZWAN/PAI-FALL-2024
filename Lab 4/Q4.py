class Employee:
    def get_data(self,name,salary,per_tax):
        self.name = name
        self.salary = salary
        self.per_tax = per_tax
        
    def salary_after_tax(self):
        self.salary -= self.salary * self.per_tax/100
        return self.salary

    def update_tax_percentage(self,tax):
        self.per_tax = tax
        self.salary -= self.salary * self.per_tax/100
        return self.salary

e = Employee()
e.get_data('Raghib',100,2)
print(e.salary_after_tax())
print(e.update_tax_percentage(3))
