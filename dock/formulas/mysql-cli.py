import docker

def run(args):
  docker.run(image='mysql:5.7.10',
             name='mysql-cli',
             auto_remove=True,
             detach=False,
             interactive=True,
             link=[['mysql', 'mysql']],
             silent=True,
             command=['sh', '-c', 'mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -proot'])
