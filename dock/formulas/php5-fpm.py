import docker
import os

cwd = os.getcwd()
container_name = 'php5-fpm'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='php:5-fpm',
             name=container_name,
             volume={
               os.getcwd(): '/var/www/html'
             },
             publish=[9000])
  docker.msg('Volume', '{} mounted to /var/www/html'.format(os.getcwd()))
