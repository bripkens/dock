#!/usr/local/opt/python/bin/python2.7

import argparse
import importlib
import os
import os.path
import re
import subprocess

HERE = os.path.abspath(os.path.dirname(__file__))
FORMULA_DIR = os.path.join(HERE, 'formula')

with open(os.path.join(HERE, '..', 'VERSION')) as f:
  VERSION = f.read().strip()


def print_version():
  print 'dock {} by Ben Ripkens and contributors'.format(VERSION)
  print 'https://github.com/bripkens/dock'


def list_available_formulas():
  print ':: Built-In Formulas'
  for formula in sorted(os.listdir(FORMULA_DIR)):
    if formula.endswith('.py') and not formula == '__init__.py':
      match = re.search('([^.]+)\\.', formula)
      print match.group(1)


def print_unknown_formula_contribution_hint(formula):
  print 'Unknown formula: {}'.format(formula)
  print ''
  print 'If you feel like {} should be supported by dock, please'.format(formula)
  print 'consider opening an issue or sending a pull request to'
  print ''
  print '       https://github.com/bripkens/dock'
  print ''
  print 'Thanks!'


def ensure_docker_usage_is_possible():
  returnCode = subprocess.call(['docker', 'ps'], stdout=open(os.devnull, 'w'))
  if not returnCode == 0:
    print 'It seems like there are issues with your Docker setup.'
    sys.exit(1)


def execute_formulas(formulas):
  ensure_docker_usage_is_possible()
  for formula in formulas:
    print ''
    module_name = 'formula.' + formula
    try:
      mod = importlib.import_module(module_name)
      path_to_module = os.path.join(FORMULA_DIR, formula + '.py')
      mod.run()
    except ImportError as e:
      if e.message.endswith(module_name):
        print_unknown_formula_contribution_hint(formula)
      else:
        raise


def main():
  parser = argparse.ArgumentParser(prog='dock',
                                   usage='%(prog)s [options] [formulas...]',
                                   description='easily bootstrap development tools with Docker')
  parser.add_argument('formulas',
                      help='Execute the given formulas in the order in which they are defined on the command line.',
                      nargs='*')
  parser.add_argument('-v', '--version',
                      action='store_true',
                      help='Display current script version')
  parser.add_argument('-l', '--list',
                      action='store_true',
                      help='List available formulas')
  args = parser.parse_args()

  if args.version:
    print_version()
  elif args.list:
    list_available_formulas()
  elif len(args.formulas) == 0:
    parser.print_help()
  else:
    execute_formulas(args.formulas)


if __name__ == '__main__':
  main()
