# 0x0F. Load balancer

| Task | File |
| ---- | ---- |
| 0. Double the number of webservers | [0-custom_http_response_header](./0-custom_http_response_header) |
| 1. Install your load balancer | [1-install_load_balancer](./1-install_load_balancer) |
| 2. Add a custom HTTP header with Puppet | [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp) |


## Tasks
### 0. Double the number of webservers
* Configure `web-02` to be identical to `web-01`.
* Requirements:
    * Configure Nginx so that its HTTP response contains a custom header(on `web-01` and `web-02`)
        * The name of the custom HTTP heder must be `X-Served-By`
        * The value of the custom HTTP header must be the hostname of the server Nginx is running on
    * Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
        * [Ignore](https://github.com/koalaman/shellcheck/wiki/Ignore)[SC2154](https://github.com/koalaman/shellcheck/wiki/SC2154) for `shellcheck`
### 1. Install your load balancer
* Install and configure HAproxy on your `lb-01` server.
* Requirements:
    * Configure HAproxy so that is sends traffic to `web-01` and `web-02`
    * Distribute requests using roundrobin algorithm
    * Make sure that HAproxy can be manage via an init script
    * Make sure that your servers are configured with the right hostanmes: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this [tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html)
### 2. Add a custom HTTP header with Puppet
* Automate the task of creating a custom HTTP header response, with Puppet.
    * The name of the custom HTTP header must be `X-Served-By`
    * The value of the custom HTTP header must be the hostname of the server Nginx is running on
