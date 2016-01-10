import docker

container_name = 'neo4j'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='neo4j:2.3.1',
             name=container_name,
             publish=[7474],
             env={'NEO4J_AUTH': 'none'})
  docker.msg('Authentication', 'Disabled')
