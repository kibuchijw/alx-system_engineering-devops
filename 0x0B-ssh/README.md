# 0x0B. SSH

## Learning Objectives

### General

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using  `#!/usr/bin/env bash` instead of `/bin/bash`

| Task | File |
| ---- | ---- |
| 0. Use a private key | [0-use_a_private_key](./0-use_a_private_key) |
| 1. Create an SSH key pair | [1-create_ssh_key_pair](./1-create_ssh_key_pair) |

## Tasks
### 0. Use a private key
* Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.
* Requirements:
	* Only use `ssh` single-character flags
	* You cannot use `-l`
	* You do not need to handle the case of a private key protected by a passphrase
### 1. Create an SSH key pair
* A Bash script that creates an RSA key pair.
* Requirements:
	* Name of the created private key must be `school`
	* Numbeer of bits in the created key to be created 4096
	* The created key must be protected by the passphrase `betty`
