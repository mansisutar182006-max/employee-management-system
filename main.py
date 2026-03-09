from admin import Admin

def main():
    ch = 0
    while(ch != '2'):
        print('''---------EMPLOYEE MANAGEMENT SYSTEM--------
        1. Login
        2. Exit
        ''')
        ch = input('Enter choice:')
        if(ch == '1'):
            print('---------Login Page--------')
            uname = 'admin'
            passw = '1234'
            username = input('Enter username:')
            password = input('Enter password:')
            if(uname == username and passw == password):
                print('Login successful...')
                ad = Admin()
            else:
                print('Invalid credentials...')

        elif(ch == '2'):
            print('Thank you for choosing us!')
        else:
            print('Invalid choice...')

if(__name__ == '__main__'):
    main()