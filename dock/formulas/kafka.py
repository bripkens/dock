import docker

container_name = 'kafka'

def run(args):
  docker.force_stop(container_name)
  docker.requires(dependent=container_name, dependency='zookeeper')
  docker.run(image='ches/kafka:0.8.2.1',
             name=container_name,
             link=[['zookeeper', 'zookeeper']],
             env={
               'KAFKA_ADVERTISED_HOST_NAME': docker.get_ip()
             },
             publish=[7203, 9092])
