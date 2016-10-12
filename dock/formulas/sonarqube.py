import docker

container_name = 'sonarqube'

def run(args):
  docker.force_stop(container_name)
  docker.run(image='sonarqube:5.2',
             name=container_name,
             publish=[9000])
  docker.msg('Admin user', 'admin')
  docker.msg('Admin password', 'admin')
