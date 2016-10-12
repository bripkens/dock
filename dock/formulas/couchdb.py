import docker

container_name = 'couchdb'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='klaemo/couchdb:1.6.1',
             name=container_name,
             publish=[5984])
  # Define username and password via environment vars once
  # https://github.com/klaemo/docker-couchdb/issues/43
  # has been resolved.
  #docker.msg('Authentication', 'See auth information in docker logs dock-couchdb')
