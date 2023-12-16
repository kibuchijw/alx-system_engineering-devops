# 0x11. What happens when you type google.com in your browser and press Enter

| Task | File |
| ---- | ---- |
| 0. What happens when... | [0-blog_post](./0-blog_post) |
| 1. Everything's better with a pretty diagram | [1-what_happen_when_diagram](./1-what_happen_when_diagram) |

## Tasks
### 0. What happens when...
* Write a blog post explaining what happens when you type `https://www.google.com` in your browser and press `Enter`.
* Requirements, your post must cover:
    * DNS request
    * TCP/IP
    * Firewall
    * HTTPS/SSL
    * Load-balancer
    * Web server
    * Application server
    * Database
### 1. Everything's better with a pretty diagram
* AddAdd a schema to your blog post illustrating the flow of the request created when you type `https://www.google.com` in your browser and press `Enter`.
* The diagram should show:
    * DNS resolution
    * that the request hitting server IP on the appropriate port
    * that the traffic is encrypted
    * that the traffic goes through a Firewall
    * that the request is distributed via a load balancer
    * that the web server answers the request by serving a web page
    * that the application server generates the web page
    * that the application server request data from the database
