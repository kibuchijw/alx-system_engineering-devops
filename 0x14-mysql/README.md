# 0x14. MySQL
## Learning Objectives

### General

* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

| Task | File |
| ---- | ---- |
| 0. Install MySQL |

## Tasks
### 0. Install MySQL
* Install MySQL on both your web-01 and web-02 servers.
    * MySQL distribution must be 5.7.x
    * Make sure that task #3 of your SSH project is completed for `web-01` and `web-02`. The checker will connect to your servers to check MySQL status
    * Please make sure you have your `README.md` pushed to GitHub.
### 1. Let us in!
* In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.
    * Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
    * Make sure that `holberton_user` has permission to check the primary/replica status of your databases.
    * In addition to that, make sure that task #3 of your SSH project is completed for `web-01` and `web-02`. **You will likely need to add the public key to web-02 as you only added it to web-01 for this project.** The checker will connect to your servers to check MySQL status
