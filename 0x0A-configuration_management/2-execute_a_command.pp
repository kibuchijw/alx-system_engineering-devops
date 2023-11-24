# Kills a process calle killmenow

exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}

