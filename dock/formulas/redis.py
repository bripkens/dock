import docker

container_name = 'redis'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='redis:3.0.6',
             name=container_name,
             publish=[6379])
