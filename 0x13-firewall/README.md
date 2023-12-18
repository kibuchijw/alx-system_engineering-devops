# 0x13. Firewall

| Task | File |
| ---- | ---- |
| 0. Block all incoming traffic but | [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but) |
| 1. Port forwarding | [100-port_forwarding](./100-port_forwarding) |

## Tasks
### 0. Block all incoming traffic but
* Install the `ufw` Firewall and setup a few rules on `web-01`.
* Requirements:
    * Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
        * `22` (SSH)
        * `443` (HTTPS SSL)
        * `80` (HTTP)
    * Share the `ufw` commands in the answer File
### 1. Port forwarding
* Firewalls can not only filter requests, they can also forward them.
* Requirements:
    * Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`.
    * Your answer file should be a copy of the `ufw` configuration file that you modified to make this happen
