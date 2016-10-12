import docker

container_name = 'rabbitmq'

user = 'admin'
password = 'admin'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='rabbitmq:3.6.0-management',
             name=container_name,
             publish=[4369, 5671, 5672, 15671, 15672, 25672],
             env={
               'RABBITMQ_DEFAULT_USER': user,
               'RABBITMQ_DEFAULT_PASS': password
             })
  docker.msg('Admin user', user)
  docker.msg('Admin password', password)
  docker.msg('Management Console', 'http://{}:15672'.format(docker.get_ip()))
