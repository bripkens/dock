import docker

container_name = 'zookeeper'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='jplock/zookeeper:3.4.7',
             name=container_name,
             publish=[2181, 2888, 3888])
