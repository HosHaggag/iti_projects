
import auth.register as register , auth.login as login , auth.activate as activate
import setting
import  project.delete , project.modify ,project.create , project.show , project.search







def main_menu():
    print('Welcome to the main menu ( press q to end the program) .')
    print('1. view all projects')
    print('2. create project')
    print('3. delete project')
    print('4. modify project')
    print('5. search for project')
    choice = input('Enter your choice: ')
    if choice == 'q':
        return None
    if choice == '1':
        project.view.show_all_projects()
    elif choice == '2':
        project.create.create_project()
    elif choice == '3':
        project.delete.delete_project()
    elif choice == '4':
        project.modify.modify_project() 
    elif choice == '5':
        project.search.search_for_project_by_date()
    else:
        print('Invalid input. Please try again.')
        main_menu()
choice = input('Do you have an account? (y/n) ')





print('Welcome to the log-in page')

if choice == 'y':
    res = login.login()
    if not res:
        main_menu()
    else :
        if res == 'Account is not active.':
            active = input('do you want to activate your account (y/n)')
            if active == 'y':
                activate.activate_account(input('enter your mail : '))
        print(res)    

elif choice == 'n':
    try:
        res = register.sign_up()
    except Exception as error:
        print(error)

else:
    print('Invalid input. Please try again.')




