import json
import os
import subprocess

devnull = open(os.devnull, 'w')


def add_name_prefix(container_name):
  return 'dock-' + container_name


def force_stop(name):
  name = add_name_prefix(name)
  subprocess.call(['docker', 'stop', name],
                  stdout=devnull,
                  stderr=devnull)
  subprocess.call(['docker', 'rm', name],
                  stdout=devnull,
                  stderr=devnull)


def run(image, name=None, publish=[]):
  if (name == None):
    name = image

  name = add_name_prefix(name)

  # combine args to Docker run CLI args
  args = ['docker', 'run', '--detach', '--name', name]
  for publishedPort in publish:
    args.extend(['--publish', '{}:{}'.format(publishedPort, publishedPort)])
  args.append(image)
  print 'Starting image {} as container {}'.format(image, name)
  subprocess.call(args)

  print_run_data(name)


def print_run_data(name):
  output = subprocess.check_output(['docker', 'inspect', name])
  data = json.loads(output)[0]
  print data['NetworkSettings']['Ports']
  # print data
