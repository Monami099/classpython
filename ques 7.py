stack = []
def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(f"{element} pushed onto stack.")
def pop():
    if not stack:
        print("Stack is empty. Nothing to pop.")
    else:
        popped = stack.pop()
        print(f"Popped element: {popped}")
def peek():
    if not stack:
        print("Stack is empty.")
    else:
        print(f"Top element is: {stack[-1]}")
def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack contents (top to bottom):")
        for item in reversed(stack):
            print(item)
while True:
    print("\n--- Stack Operations Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

Output:
--- Stack Operations Menu ---
1. Push
2. Pop
3. Peek
4. Display Stack
5. Exit
Enter your choice (1-5): 1
Enter element to push: apple
apple pushed onto stack.
