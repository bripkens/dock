import docker

container_name = 'mongo-express'

def run(args):
  docker.force_stop('mongo-express')
  docker.requires(dependent='mongo-express', dependency='mongodb')
  docker.run(image='knickers/mongo-express:latest',
             name='mongo-express',
             link=[['dock-mongodb', 'mongo']],
             publish=[8081])
