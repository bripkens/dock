import docker

container_name = 'elasticsearch'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='elasticsearch:2.1.1',
             name=container_name,
             publish=[9200, 9300])
