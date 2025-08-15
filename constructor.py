# Constructor
# เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง Constructor
# def __init__(self):
#     pass

# Destructor
# เป็น method พิเศษที่ตรงข้างกับ constructor จะถูกใช้งานเมื่อ
# สิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย object
# ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
# โครงสร้าง
# def __del__(self):
#   pass

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))



emp1 = Employee('พรชนก', 50000, 'นักศึกษา')
emp1.showData()

emp2 = Employee('เพ็ขรนาม', 25000, 'วิทยาลัยเทคโนโลยีพระมหาไถ่')
emp2.showData()

emp3 = Employee('แชมป์', 10000, 'ปวส2')
emp3.showData()

emp4 = Employee('jelly', 15000, 'pre1')
emp4.salary = 210000
emp4.showData()
