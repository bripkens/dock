import docker

container_name = 'jenkins'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='jenkins',
             name=container_name,
             publish=[8080, 50000])
