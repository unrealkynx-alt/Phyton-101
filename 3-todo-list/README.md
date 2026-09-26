# To-Do List CLI

A simple command-line interface (CLI) to-do list manager that saves and loads tasks using a JSON file.

## How to Run

1. Make sure Python 3 is installed.
2. Open your terminal in this directory.
3. Run the script:
   ```bash
   python todo_list.py
   ```

## Features

- **View Tasks:** Lists all active tasks with 1-based indexing.
- **Add Tasks:** Adds new items and prevents empty task descriptions.
- **Remove Tasks:** Deletes tasks by their display number and updates the list.
- **Data Persistence:** Automatically saves tasks to `tasks.json` so data is preserved across sessions.
- **Safe Initialization:** Checks if `tasks.json` exists before attempting to read it, avoiding missing-file crashes.

## Concepts Practiced

- File I/O using Python's `open()` context manager (`with open(...)`)
- Working with the `json` module (`json.dump`, `json.load`)
- Using the `os` module to verify file existence (`os.path.exists`)
- List operations (`.append()`, `.pop()`, `enumerate()`, 0-based vs 1-based indexing)
- Input validation and string checking (`.isdigit()`)
- Chained comparison operators (`0 <= task_index < len(tasks)`)
- Infinite application loops (`while True`) with menu dispatching
