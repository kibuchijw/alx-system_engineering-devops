# Puppet manifest using the pip provider to install Flask 2.1.0 and ensure Werkzeug 2.1.1 is installed
# Install Flask using the pip provider
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure Werkzeug is installed using the pip provider
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
