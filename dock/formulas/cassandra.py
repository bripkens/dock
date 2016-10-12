import docker

container_name = 'cassandra'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='cassandra:3.1.1',
             name=container_name,
             publish=[7000, 7001, 7199, 9042, 9160])
  docker.msg('Root user', 'cassandra')
  docker.msg('Root password', 'cassandra')
