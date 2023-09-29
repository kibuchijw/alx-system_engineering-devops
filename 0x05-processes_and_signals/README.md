# Project: 0x05. Processes and signals


| Task | File |
| ---- | ---- |
| 0. What is my PID | [0-what-is-my-pid](./0-what-is-my-pid) |
| 1. List your processes | [1-list_your_processes](./1-list_your_processes) |
| 2. Show your Bash PID | [2-show_your_bash_pid](./2-show_your_bash_pid) |
| 3. Show your Bash PID made easy | [3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy) |
| 4. To infinity and beyond | [4-to_infinity_and_beyond](./4-to_infinity_and_beyond) |
| 5. Don't stop me now! | [5-dont_stop_me_now](./5-dont_stop_me_now) |
| 6. Stop me if you can | [6-stop_me_if_you_can](./6-stop_me_if_you_can) |
| 7. Highlander | [7-highlander](./7-highlander) |
| 8. Beheaded process | [8-beheaded_process](./8-beheaded_process) |

## Tasks
### 0. What is my PID
* Bash script that displays its own PID
### 1. List your processes
* Bash script that displays a list of currently running processes
	* Must show all processes, for all users, including those which might not have a TTY
	* Display in a user-oriented format
	* Show process hierachy
### 2. Show your Bash PID
* Using the command in `1. list your process`, write a Bash script that displays lines containing the `bash` word.
### 3. Show your Bash PID made easy
* Bash script that displays the PID, along with the process name, of the processes whose name contain the word `bash`.
### 4. To infinity and beyond
* Bash script that displays `To infinity and beyond` indefinitely
	* In between each iteration of the loop, add a `sleep 2`
### 5. Don't stop me now!
* Bash script to terminate `4-to_infinity_and_beyond` using `kill`
### 6. Stop me if you can
* Bash script to terminate `4-to_infinity_and_beyond` using `pfkill`
### 7. Highlander
* Bash script that displays:
	* `To infinity and beyond` indefinitely
	* With a `sleep 2` in between each iteration
	* Displays `I am invincible!!!` when receiving a SIGTERM signal
### 8. Beheaded process
* Bash script that kills the process `7-highlander`
