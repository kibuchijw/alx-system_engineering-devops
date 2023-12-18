# Puppet script to make changes to a configurations file
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => "
    Host your_server
      HostName 107.22.143.169
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
