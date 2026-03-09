from emp import Employee
from datastore import Datastore

class Admin:
    def __init__(self):
        self.ds = Datastore()

        ch = 0
        while(ch != '6'):
            print('''----------ADMIN----------
            1. Add employee
            2. Show all employees
            3. Search employee
            4. Update employee
            5. Delete employee
            6. Logout
            ''')
            ch = input('Enter choice:')
            if(ch == '1'):
                self.addEmp()
            elif(ch == '2'):
                self.showAllEmp()
            elif(ch == '3'):
                self.searchEmp()
            elif(ch == '4'):
                self.updEmp()
            elif(ch == '5'):
                self.delEmp()
            elif(ch == '6'):
                print('Logout successful...')
            else:
                print('Invalid choice...')
    
    def addEmp(self):
        id = input('Enter ID:')
        name = input('Enter NAME:')
        sal = float(input('Enter SALARY:'))
        dept = input('Enter DEPT:')
        emp = Employee(id, name, sal, dept)
        res = self.ds.addData(emp)
        print(res)

    def showAllEmp(self):
        data = self.ds.showAllData()
        if(data):
            for e in data:
                columns = ('ID', 'NAME', 'SALARY', 'DEPT')
                for col, val in zip(columns, e):
                    print(f'{col} : {val}')
                print('#######################')
        else:
            print('Data not found...')

    def searchEmp(self):
        id = input('Enter ID:')
        res = self.ds.getData(id)
        if(res):
            print('ID:', res[0])
            print('NAME:', res[1])
            print('SALARY:', res[2])
            print('DEPT:', res[3])
        else:
            print('Employee not found...')
    
    def updEmp(self):
        id = input('Enter ID:')
        res = self.ds.getData(id)
        if(res):
            print('NOTE: Leave the field blank if you do not want to change...')
            name = input(f'Enter NAME({res[1]}):') or res[1]
            sal = input(f'Enter SALARY({res[2]}):') or res[2]
            dept = input(f'Enter DEPT({res[3]}):') or res[3]
            emp = Employee(id, name, sal, dept)
            res = self.ds.updData(emp)
            print(res)
        else:
            print('Employee not found...')

    def delEmp(self):
        id = input('Enter ID:')
        res = self.ds.getData(id)
        if(res):
            res = self.ds.delData(id)
            print(res)
        else:
            print('Employee not found...')

if(__name__ == '__main__'):
    ad = Admin()