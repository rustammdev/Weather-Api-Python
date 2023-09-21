from datetime import datetime


class Employee:

    def __init__(self, name, surname, birth_date, rate, salary, come_date) -> None:
        self.name = name
        self.surname = surname
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
        self.rate = rate
        self.salary = salary
        self.come_date = datetime.strptime(come_date, "%d-%m-%Y")
        self.age = datetime.now().year - self.birth_date.year
        self.staj = datetime.now().year - self.come_date.year

    def __str__(self) -> str:
        return f"{self.surname} {self.name} | {self.birth_date.strftime('%d-%m-%Y')} | Rating: {self.rate} | Salary: {self.salary} | Since: {self.come_date.strftime('%d-%m-%Y')}"

    def get_rate_employee(self):
        return f"The rate of {self.name} {self.surname}: {self.rate}"

    def get_age_employee(self):
        current_year = datetime.now().year
        year_of_birth = self.birth_date.year
        age = current_year - year_of_birth
        return f"{self.surname} {self.name}'s age: {age}"

    def get_salary_employee(self):
        yearly_salary = self.salary * 12
        return f"{self.surname} {self.name}'s total salary for a whole year: ${yearly_salary:,.2f}"

    def get_staj_employee(self):
        current_year = datetime.now().year
        year_of_hire = self.come_date.year
        staj = current_year - year_of_hire
        return f"{self.surname} {self.name} have been working for {staj} years now"


class Company:

    def __init__(self, employees: list):
        self.comp_name = input("Input a name of a company: ")
        self.chef = input(f"Input a director of the company {self.comp_name}: ")
        self.month_income = float(input(f"Input a monthly income of the company: "))
        self.employees = employees

    def __str__(self) -> str:
        employee_names = [employee.name for employee in self.employees]
        employee_names_string = ", ".join(employee_names)
        return f"Company name: {self.comp_name}, Chef executive: {self.chef}\nMonthly income: {self.month_income:,.2f}\nEmployers: '{employee_names_string}'"

    def add_employee(self, name, surname, birth_date, rate, salary, come_date):
        new_employee = Employee(name, surname, birth_date, rate, salary, come_date)
        self.employees.append(new_employee)

    def sort_employee(self):
        self.employees.sort(key=lambda employee: employee.surname)

    def delete_employee(self, name: str):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                self.employees.remove(employee)
                return "success"
        return f"An employee with the name {name} does not exist!"

    def get_youngest_employee(self):
        youngest_employee = int(self.employees[0].age)
        name = ""
        for employee in self.employees:
            if employee.age < youngest_employee:
                youngest_employee = employee
                name = employee.name
        return f"The youngest employee of the company: {name}, age: {youngest_employee}"

    def get_oldest_employee(self):
        oldest_employee = self.employees[0]
        name = ""
        for employee in self.employees:
            if employee.staj > oldest_employee.staj:
                oldest_employee = employee
                name = employee.name
        return f"An employee with the longest work-year: {name}\nHave been working for {oldest_employee.staj} years"

    def sort_by_rate(self):
        rates = {}
        for name in self.employees:
            rate = name.get_rate_employee()
            rates[name] = rate
        sorted_rates = sorted(rates.items(), key=lambda item: item[1], reverse=True)
        for name, rate in sorted_rates:
            print(f"{name}, Rate: {rate}")


if __name__ == "__main__":
    n = int(input("How many employers you want to add?: "))
    lst = []
    for i in range(n):
        name = input("Input a name of an employee: ")
        surname = input("Input a surname of an employee: ")
        birth_date = input(f"Input a birth date of {name}(format: dd-mm-yyyy): ")
        rate = float(input("Input rate: "))
        salary = float(input("Input monthly salary: $"))
        come_date = input(f"Date {name} came(format: dd-mm-yyyy): ")
        result = Employee(name, surname, birth_date, rate, salary, come_date)
        lst.append(result)
    answer = Company(lst)
    print(answer.sort_employee())
    print(str(answer))
    print(answer.get_youngest_employee())
    print(answer.get_oldest_employee())
    print(answer.sort_by_rate())
