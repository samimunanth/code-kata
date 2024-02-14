import requests
import sys

def fetch_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    even_todo_ids = [i for i in range(2, 41, 2)]  # Generating IDs for even numbered TODOs
    todo_count = 0
    for todo_id in even_todo_ids:
        todo = fetch_todo(todo_id)
        if todo:
            print(f"Title: {todo['title']}")
            print(f"Completed: {'Yes' if todo['completed'] else 'No'}")
            todo_count += 1
            if todo_count == 20:  # Exit loop when 20 TODOs are fetched
                break

if __name__ == "__main__":
    main()