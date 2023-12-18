# 0x13. Firewall

| Task | File |
| ---- | ---- |
| 0. Block all incoming traffic but | [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but) |

## Tasks
### 0. Block all incoming traffic but
* Install the `ufw` Firewall and setup a few rules on `web-01`.
* Requirements:
    * Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
        * `22` (SSH)
        * `443` (HTTPS SSL)
        * `80` (HTTP)
    * Share the `ufw` commands in the answer file
