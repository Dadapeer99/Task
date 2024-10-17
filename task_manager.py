import json
class Task:
    def __init__(self, Manager_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.id}. {self.title} - {status}"

# Function to add a new task
def add_task(task_list, task_title):
    task_id = len(task_list) + 1  # Assign a new task ID
    new_task = Task(task_id, task_title)
    task_list.append(new_task)
    print(f"Task '{task_title}' added successfully!")

# Function to view all tasks
def view_tasks(task_list):
    """
    Display all tasks in the task list.
    :param task_list: The current list of tasks.
    """
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(task)

# Function to delete a task by ID
def delete_task(task_list, task_id):
    """
    Delete a task from the task list by its ID.
    :param task_list: The current list of tasks.
    :param task_id: The ID of the task to delete.
    """
    updated_list = [task for task in task_list if task.id != task_id]
    if len(updated_list) != len(task_list):
        task_list[:] = updated_list  # Update the task list in place
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"No task found with ID {task_id}.")

# Function to mark a task as complete
def complete_task(task_list, task_id):
    """
    Mark a task as completed.
    :param task_list: The current list of tasks.
    :param task_id: The ID of the task to mark as complete.
    """
    for task in task_list:
        if task.id == task_id:
            task.completed = True
            print(f"Task {task_id} marked as completed!")
            break
    else:
        print(f"No task found with ID {task_id}.")

# Save the list of tasks to a JSON file
def save_tasks_to_file(task_list, filename="tasks.json"):
    """
    Save tasks to a JSON file.
    :param task_list: The current list of tasks.
    :param filename: The name of the file to save the tasks (default: tasks.json).
    """
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in task_list], file)
    print(f"Tasks saved to {filename}")

# Load tasks from a JSON file
def load_tasks_from_file(filename="tasks.json"):
    """
    Load tasks from a JSON file.
    :param filename: The name of the file to load the tasks from (default: tasks.json).
    :return: A list of loaded Task objects.
    """
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []  # Return an empty list if no file exists

# Dummy login credentials for testing
VALID_EMAIL = "test@example.com"
VALID_PASSWORD = "password123"

# Function to handle user login
def login():
    """
    Prompt the user to enter email and password for authentication.
    """
    print("Please log in to access the Task Manager.")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

# Display the CLI menu options
def display_menu():
    """
    Display the options for the Task Manager CLI.
    """
    print("\nTask Manager CLI")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Save and Exit")

# Main function to run the application
def main():
    """
    Main function to run the Task Manager CLI application.
    """
    if not login():
        return  # Exit if login fails

    task_list = load_tasks_from_file()  # Load tasks at the start of the program

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':  # Add Task
            title = input("Enter task title: ")
            add_task(task_list, title)
        
        elif choice == '2':  # View Tasks
            view_tasks(task_list)
        
        elif choice == '3':  # Delete Task
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_list, task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        
        elif choice == '4':  # Mark Task as Complete
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                complete_task(task_list, task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        
        elif choice == '5':  # Save and Exit
            save_tasks_to_file(task_list)
            print("Exiting the application...")
            break
        
        else:
            print("Invalid option. Please choose a valid option from the menu.")

if __name__ == "__main__":
    main()
