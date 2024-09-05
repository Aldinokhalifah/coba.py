class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.salary_per_hours = 0
        self.hours_worked = 0
        self.set_salary_per_hours()  # Panggil metode untuk menetapkan gaji per jam

    def set_salary_per_hours(self):
        if self.position == 'Directure':
            self.salary_per_hours = 1000
        elif self.position == 'Manager':
            self.salary_per_hours = 800
        elif self.position == 'Developer':
            self.salary_per_hours = 600
        else:
            self.salary_per_hours = 400

    def add_hours(self, hours):
        self.hours_worked += hours

    def calculate_salary(self):
        return self.salary_per_hours * self.hours_worked
    
    def __str__(self):
        return f'{self.name} - {self.position} : Gaji per jam {self.salary_per_hours}'
    
class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        if not self.employees:
            print("Tidak ada karyawan yang terdaftar.")
            return
        print("Daftar Karyawan:")
        for idx, employee in enumerate(self.employees, start=1):
            print(f"{idx}. {employee}")
    
    def remove_employee(self, name):
        self.display_employees()

        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                print(f"Karyawan dengan nama '{name}' telah dihapus.")
                return
        print(f"Karyawan dengan nama '{name}' tidak ditemukan.")

    def calculate_total_salary(self):
        total_salary = sum(employee.calculate_salary() for employee in self.employees)
        print(f"Total gaji yang harus dibayar oleh perusahaan: {total_salary}")

# Membuat objek Company
company = Company()

# Menambahkan karyawan
employee1 = Employee("Alice", "Manager")
employee2 = Employee("Bob", "Developer")
employee3 = Employee("Charlie", "Designer")
employee4 = Employee("Cesar", "Directure")

company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)
company.add_employee(employee4)

print("Daftar Karyawan Setelah Penambahan:")
company.display_employees()

# Menambahkan jam kerja untuk setiap karyawan
employee1.add_hours(160)
employee2.add_hours(150)
employee3.add_hours(140)
employee4.add_hours(170)

print("\nGaji Bulanan Karyawan:")
for employee in company.employees:
    print(f"{employee.name}: {employee.calculate_salary()}")

print("\nTotal Gaji Bulanan:")
company.calculate_total_salary()

# Menghapus karyawan
print("\nHapus Karyawan:")
company.remove_employee("Bob")
company.display_employees()
