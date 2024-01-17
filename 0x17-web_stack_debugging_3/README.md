# 0x17. Web stack debugging #3

| Task                     | File                                                       |
| ------------------------ | ---------------------------------------------------------- |
| 0. Strace is your friend | [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp) |

## Tasks

### 0. Strace is your friend

- Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
- Hint:
  - `strace` can attach to a current running process
  - You can use [tmux](https://hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) to run [strace](https://strace.io/) in one window and curl in another one
- Requirements:
  - Your `0-strace_is_your_friend.pp` file must contain Puppet code
  - You can use whatever Puppet resource type you want for you fix
