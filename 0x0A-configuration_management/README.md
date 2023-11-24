# 0x0A. Configuration management

| Task | File |
| ---- | ---- |
| 0. Create a file | [0-create_a_file.pp](./0-create_a_file.pp) |
| 1. Install a package | [1-install_a_package.pp](./1-install_a_package.pp) |

## Tasks
### 0. Create a file
* Using Puppet, create a file in `/tmp`.
* Requirements:
	* File path is `/tmp/school`
	* File permission is `0744`
	* File owner is `www-data`
	* File group is `www-data`
	* File contains `I love Puppet` 
### 1. Install a package
* Using Puppet, install `flask` from `pip3`.
* Requirements:
	* Install `flask`
	* Version must be `2.1.0`
