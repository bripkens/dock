import docker

container_name = 'nexus'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='sonatype/nexus:latest',
             name=container_name,
             publish=[8081])
  docker.msg('Admin user', 'admin')
  docker.msg('Admin password', 'admin123')
