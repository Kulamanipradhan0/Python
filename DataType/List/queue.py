queue=[]

def enqueue():
    queue.append(input("Enter item to add in queue : ").strip())
    print("Item Added")
def dequeue():
    item = queue.pop(queue[0])
    print(item,"Item Removed")
def view():
    print(queue)


def welcome():
    print("""Welcome to Queue. Please choose one option.
    Enqueue(E)
    Dequeue(D)
    View(V)
    Quit(Q)
    """)
    choice=input("Please enter your choice : ")
    while True:
        if choice.lower() not in 'edvq':
            print("Invalid Choice !!!")
            welcome()
        else:
            if choice.lower() == 'q':
                print("Exiting ....")
                exit()
            elif choice.lower() == 'e':
                enqueue()
                welcome()
            elif choice.lower() == 'd':
                dequeue()
                welcome()
            elif choice.lower() == 'v':
                view()
                welcome()
            else:
                welcome()


welcome()


