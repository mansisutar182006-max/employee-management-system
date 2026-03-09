import config
import mysql.connector

class Datastore:
    def __init__(self):
        if(config.storage == 'Dictionary'):
            self.empdata = {}
            print('Dictionary created...')
        else:
            self.connectDB()
            print('Database connected...')

    def addData(self, emp):
        if(config.storage == 'Dictionary'):
            self.empdata[emp.id] = emp.toTuple()
        else:
            sql = 'insert into emp(id, name, salary, dept) values(%s, %s, %s, %s)'
            values = (emp.id, emp.name, emp.sal, emp.dept)
            self.cursor.execute(sql, values)
            self.conn.commit()
        return 'Data added successfully.'

    def showAllData(self):
        if(config.storage == 'Dictionary'):
            return self.empdata.values()
        else:
            sql = 'select * from emp'
            self.cursor.execute(sql)
            empdata = self.cursor.fetchall()
            return empdata

    def getData(self,id):
        if(config.storage == 'Dictionary'):
            if(id in self.empdata):
                return self.empdata[id]
            else:
                return None
        else:
            sql = 'select * from emp where id = %s'
            self.cursor.execute(sql, (id, ))
            empdata = self.cursor.fetchone()
            return empdata
    
    def updData(self,emp):
        if(config.storage == 'Dictionary'):
            self.empdata[emp.id] = emp.toTuple()
        else:
            sql = 'update emp set name=%s, salary=%s, dept=%s where id=%s'
            values = (emp.name, emp.sal, emp.dept, emp.id)
            self.cursor.execute(sql, values)
            self.conn.commit()
        return 'Data updated successfully...'
    
    def delData(self, id):
        if(config.storage == 'Dictionary'):
            self.empdata.pop(id)
        else:
            sql = 'delete from emp where id=%s'
            self.cursor.execute(sql, (id,))
            self.conn.commit()
        return 'Data deleted successfully...'

    def connectDB(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root', 
                password = '1137',
                database = 'fbs'
            )
        except mysql.connector.errors.ProgrammingError as e:
            if('unknown database' in e.msg.lower()):
                conn = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = '1137'
                )

                sql = 'create database fbs'
                cursor = conn.cursor()
                cursor.execute(sql)
                cursor.close()
                conn.close()

                self.conn = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = '1137',
                    database = 'fbs'
                )

                self.cursor = self.conn.cursor()
                sql = 'create table emp(id varchar(10), name varchar(50), salary int, dept varchar(50))'
                self.cursor.execute(sql)
            else:
                print('Other error raised in mysql connection...')

        except Exception as e:
            print('Error:', e)

        else:
            self.cursor = self.conn.cursor()

if(__name__ == '__main__'):
    from emp import Employee
    emp = Employee(101, 'ABC', 76000, 'DA')
    ds = Datastore()
    print(ds.empdata)
    ds.addData(emp)
    print(ds.empdata)