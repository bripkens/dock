import docker

container_name = 'consul'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='voxxit/consul:latest',
             name=container_name,
             publish=[8300, 8301, 8302, 8400, 8500, 8600])
