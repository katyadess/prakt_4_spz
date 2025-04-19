class Factory:
    def __init__(self, name, location, year_founded, num_employees, production_type, capacity_ped_day, is_working):
        self.name = name
        self.location = location
        self.year_founded = year_founded
        self.num_employees = num_employees
        self.production_type = production_type
        self.capacity_ped_day = capacity_ped_day
        self.is_working = is_working
        
    
    def __str__(self):
        return f"Factory Name: {self.name}\nLocation: {self.location}\nYear Founded: {self.year_founded}\nNumber of Employees: {self.num_employees}\nProduction Type: {self.production_type}\nCapacity per Day: {self.capacity_ped_day}\nIs Working: {self.is_working}"
    
    def calculate_annual_capacity(self):
        return self.capacity_ped_day * 365
    
    
    def working_status(self):
        if self.is_working:
            return f"{self.name} is currently operational."
        else:
            return f"{self.name} is not operational."
        
        
name = input("Enter the factory name: ")
location = input("Enter the factory location: ")
year_founded = int(input("Enter the year the factory was founded: "))
num_employees = int(input("Enter the number of employees: "))
production_type = input("Enter the type of production: ")
capacity_ped_day = int(input("Enter the capacity per day: "))
is_working = input("Is the factory currently operational? (yes/no): ").strip().lower() == 'yes'

factory = Factory(name, location, year_founded, num_employees, production_type, capacity_ped_day, is_working)

print(factory)
print(f"Annual Capacity: {factory.calculate_annual_capacity()}")
print(factory.working_status())