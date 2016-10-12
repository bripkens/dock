import docker

container_name = 'rethinkdb'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='rethinkdb:2.2.2',
             name=container_name,
             publish=[8080, 28015, 29015])

  docker.msg('Admin Interface', 'http://{}:8080'.format(docker.get_ip()))
