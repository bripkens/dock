import docker

container_name = 'mongo-express'

def run(args):
  docker.force_stop(container_name)
  docker.requires(dependent=container_name, dependency='mongodb')
  docker.run(image='knickers/mongo-express:0.29.3',
             name=container_name,
             link=[['mongodb', 'mongo']],
             publish=[8081])
