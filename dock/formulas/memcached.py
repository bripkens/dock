import docker

container_name = 'memcached'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='memcached:1.4.25',
             name=container_name,
             publish=[11211])
