# Creates a custom HTTP header
exec { 'command':
  command  => 'apt-get update;
  apt-get install nginx -y;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
