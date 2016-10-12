import docker

# see
# https://github.com/orientechnologies/docker-docs/blob/master/orientdb/content.md
# https://github.com/orientechnologies/orientdb-docker/issues/4
# https://hub.docker.com/r/orientdb/orientdb/~/dockerfile/

container_name = 'orientdb'

password = 'root'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='orientdb/orientdb:2.1.5',
             name=container_name,
             publish=[2424, 2480],
             env={
               'ORIENTDB_ROOT_PASSWORD': password
             })

  docker.msg('Root password', password)
