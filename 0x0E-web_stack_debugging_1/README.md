# 0x0E. Web stack debugging #1

| Task | File |
| ---- | ---- |
| 0. Nginx likes port 80 | [0-nginx_likes_port_80](./0-nginx_likes_port_80) |
| 1. Make it sweet and short | [1-debugging_made_short](./1-debugging_made_short) |

## Tasks
### 0. Nginx likes port 80
* Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port `80`. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.
* Requirements:
    * Nginx must be running, and listen on port `80` of all the server's active IPv4 IPs
    * Write a Bash script that configures a server to the above requirements
