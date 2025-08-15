#classInstanceVariable

#classVariable คือ ตัวแปรที่ทำงานภายใน Class ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
#โดยไม่จำเป็นต้องสร้าง Object ขึ้นมา

#InstanceVariable คือ ตัวแปรที่อยู่ภายใน Object
#สามารถเข้าถึงข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง Object ขึ้นมา

class Employee:
    # class variable
    __minSalary = 12000
    __maxSalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self.__department = department


    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.getName())
        print('เงินเดือน = {}'+self.getSalary())
        print('แผนก = {}'+self.getDepartment())



emp1 = Employee('พัชราภา', 50000, 'นักเรียน')
# print('เงินเดือนขั้นต่ำ ='+str(Employee.__minSalary))
print(Employee._companyName)