# 0x0F. Load balancer

| Task | File |
| ---- | ---- |
| 0. Double the number of webservers | [0-custom_http_response_header](./0-custom_http_response_header) |

## Tasks
### 0. Double the number of webservers
* Configure `web-02` to be identical to `web-01`.
* Requirements:
    * Configure Nginx so that its HTTP response contains a custom header(on `web-01` and `web-02`)
        * The name of the custom HTTP heder must be `X-Served-By`
        * The value of the custom HTTP header must be the hostname of the server Nginx is running on
    * Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
        * [Ignore](https://github.com/koalaman/shellcheck/wiki/Ignore)[SC2154](https://github.com/koalaman/shellcheck/wiki/SC2154) for `shellcheck`
