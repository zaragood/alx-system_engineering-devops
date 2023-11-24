# Using Puppet, install flask from pip3

package { 'flask':
  ensure          => 'installed',
  provider        => 'pip3',
  install_options => ['--upgrade', 'flask==2.1.0'],
}
