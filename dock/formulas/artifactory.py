import docker

container_name = 'artifactory'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='jfrog-docker-registry.bintray.io/jfrog/artifactory-oss',
             name=container_name,
             publish=[8081])
  docker.msg('Admin user', 'admin')
  docker.msg('Admin password', 'password')
