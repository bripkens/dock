import docker

container_name = 'mongodb'

def run():
  docker.force_stop(container_name)
  docker.run(image='mongo:3.2.0',
             name=container_name,
             publish=[27017, 27018])
