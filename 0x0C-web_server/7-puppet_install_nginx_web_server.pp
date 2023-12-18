# Install Nginx package
package { 'nginx': # Ensure the Nginx package is installed
  ensure => installed,
}

# Define Nginx configuration
file { '/etc/nginx/sites-available/default': # Modify the default Nginx site configuration
  ensure  => file,
  content => "
    server {
    listen 80;
    server_name localhost;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
    }
    error_page 404 /404.html;
    location /404 {
            root /var/www/html;
            internal;
    }
  ",
  notify  => Service['nginx'], # Notify the Nginx service when this file changes
}

# Ensure Nginx service is running and enabled
service { 'nginx': # Manage the Nginx service
  ensure  => running,
  enable  => true,
  require => Package['nginx'], # Make sure the Nginx package is installed before starting the service
}
