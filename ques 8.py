queue = []
def enqueue():
    element = input("Enter element to enqueue: ")
    queue.append(element)
    print(f"{element} added to the queue.")
def dequeue():
    if not queue:
        print("Queue is empty. Nothing to dequeue.")
    else:
        removed = queue.pop(0)
        print(f"Dequeued element: {removed}")
def peek():
    if not queue:
        print("Queue is empty.")
    else:
        print(f"Front element is: {queue[0]}")
def display():
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue contents (front to rear):")
        for item in queue:
            print(item)
while True:
    print("\n--- Queue Operations Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display Queue")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
