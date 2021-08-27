stack=[]
def stackpush():
    item=input("Enter your stack item to add : ")
    stack.append(item)
    print(item," has been added to stack")

def stackpop():
    item=stack.pop()
    print(item," has been removed from stack")

def stackview():
    print("Stack : ", stack)

choice_dict={'u':'stackpush','o':'stackpop','v':'stackview'}
def welcome():
    print('''Welcome to stack. Please choose an option(u/o/v/e)
                P(u)sh
                P(o)p
                (V)iew
                (E)xit''')
    choice=input("Enter your option(u/o/v/e) : ")
    while True :
        if choice not in 'uove' :
            print("Invalid choice")
        else:
            if choice == 'u':
                stackpush()
                welcome()
            elif choice == 'o' :
                stackpop()
                welcome()
            elif choice == 'v' :
                stackview()
                welcome()
            else :
                print('Exiting ......')
                exit()



welcome()