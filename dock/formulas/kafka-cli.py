import docker

def run(args):
  print('Starting an interactive Docker container which contains the')
  print('Kafka CLI tools. Inspect the env to learn about IPs and ports.')
  print('Kafka is located at $KAFKA_HOME.')

  docker.run(image='ches/kafka:0.8.2.1',
             name='kafka-cli',
             auto_remove=True,
             detach=False,
             interactive=True,
             link=[['kafka', 'kafka']],
             silent=True,
             command=['bash'])
