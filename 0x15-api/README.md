# 0x15. API

## Learning Objectives

### General

* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

| Task | File |
| ---- | ---- |
| 0. Gather data from an API | [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py) |
| 1. Export to CSV | [1-export_to_CSV.py](./1-export_to_CSV.py) |

## Tasks
### 0. Gather data from an API
* Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.
* Requirements:
    * You must use `urllib` or `requests` module
    * The script must accept an integer as a parameter, which is the employee ID
    * The script must display on the standard output the employee TODO list progress in this exact format:
        * First line: `Employee EMPLOYEE_NAME is done with
        tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
        * `EMPLOYEE_NAME`: name of the employee
        * `NUMBER_OF_DONE_TASKS`: number of completed Tasks
        * `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
    * Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE)`
### 1. Export to CSV
* Using what you did in the task #0, extend your Python script to export data in the CSV format.
* Requirements:
    * Records all tasks that are owned by this employee
    * Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
    * File name must be: `USER_ID.csv`