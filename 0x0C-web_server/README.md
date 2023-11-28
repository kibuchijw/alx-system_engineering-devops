# 0x0C. Web server

## Learning Objectives

### General

* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests

| Task | File |
| ---- | ---- |
| 0. Transfer a file to your server | [0-transfer_file](./0-transfer_file) |

## Tasks
### 0. Transfer a file to your server
* A Bash script that transfers a file from our client to a server:
* Requirements:
    * Accepts 4 parameters
        1. The path to the file to be tranfered
        2. The IP of the server we want to transfer the file to
        3. The username `scp` connects with
        4. The path to the SSH private key that `scp` uses
    * Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
    * `scp` must transfer the file to the useer home directory `~/`
    * Script host key checking must be disabled when using `scp`
### 1. Install nginx web server
* Installing a web server
* Requirements:
    * Install `nginx` on the `web-01` server
    * server
    * Nginx should be listening on port 80
    * When querying Nginx at its root `/` with a GET request(requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
    * As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
    * You can't use `systemctl` for restarting `nginx`
