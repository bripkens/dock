import docker

container_name = 'postgres'

user = 'admin'
password = 'admin'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='postgres:9.5.0',
             name=container_name,
             publish=[5432],
             env={
              'POSTGRES_USER': user,
              'POSTGRES_PASSWORD': password
             })

  docker.msg('Admin user', user)
  docker.msg('Admin password', password)
