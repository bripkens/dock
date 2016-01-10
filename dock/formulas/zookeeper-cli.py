import docker

def run(args):
  docker.run(image='jplock/zookeeper:3.4.7',
             name='zookeeper-cli',
             auto_remove=True,
             detach=False,
             interactive=True,
             link=[['zookeeper', 'zookeeper']],
             silent=True,
             entrypoint='sh',
             command=['-c', './bin/zkCli.sh -server "$ZOOKEEPER_PORT_2181_TCP_ADDR":"$ZOOKEEPER_PORT_2181_TCP_PORT"'])
