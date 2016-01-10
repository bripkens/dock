import docker

container_name = 'mysql'

root_password = 'root'
database = 'dock-db'
user = 'user'
password = 'user'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='mysql:5.7.10',
             name=container_name,
             publish=[3306],
             env={
              'MYSQL_ROOT_PASSWORD': root_password,
              'MYSQL_DATABASE': database,
              'MYSQL_USER': user,
              'MYSQL_PASSWORD': password
             })

  docker.msg('Root password', root_password)
  docker.msg('Database', database)
  docker.msg('User name', user)
  docker.msg('User password', password)
