class TaskManager:
    def __init__(self):
        self.task_file = 'tasks.txt'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.task_file, 'r') as file:
                tasks = []
                for line in file:
                    line = line.strip()
                    if line:  # Only process non-empty lines
                        parts = line.rsplit('|', 1)
                        if len(parts) == 2:  # Ensure line is correctly formatted
                            task, status = parts
                            tasks.append({"task": task, "completed": status == "completed"})
                        else:
                            print(f"Warning: Skipping improperly formatted line: {line}")
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.task_file, 'w') as file:
            for task in self.tasks:
                status = "completed" if task["completed"] else "incomplete"
                file.write(f"{task['task']}|{status}\n")

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Here are your tasks:\n")
            for index, task in enumerate(self.tasks, start=1):
                status = "V" if task["completed"] else "X"  # Replace with simple characters
                completion_status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. [{status}] {task['task']} - Status: {completion_status}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f"Task deleted: {removed_task['task']}")
        else:
            print(f"Error: Task with index {index + 1} does not exist.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print(f"Task {index + 1} marked as complete.")
        else:
            print(f"Error: Task with index {index + 1} does not exist.")

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_description
            self.save_tasks()
            print(f"Task {index + 1} updated to: {new_description}")
        else:
            print(f"Error: Task with index {index + 1} does not exist.")
