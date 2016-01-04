from os import chdir, listdir
from os.path import expanduser, exists, join
from argparse import ArgumentParser
from subprocess import call
import importlib


VERSION = '1.4.0'
REMOTE_REPO='https://github.com/bripkens/dock.git'
LOCAL_REPO = expanduser('~/.dock-formulas')
FORMULA_DIR = join(LOCAL_REPO, 'src', 'formula')

def print_version():
  print 'dock {} by Ben Ripkens and contributors'.format(VERSION)
  print 'https://github.com/bripkens/dock'
  print 'local formula location: {}'.format(LOCAL_REPO)


def clone():
  call(['git', 'clone', REMOTE_REPO, LOCAL_REPO])


def ensure_local_repo_exists():
  if (not exists(LOCAL_REPO)):
    clone()


def upgrade():
  if (exists(LOCAL_REPO)):
    chdir(LOCAL_REPO)
    call(['git', 'pull', REMOTE_REPO, 'master'])
  else:
    clone()


def execute_formulas(formulas):
  ensure_local_repo_exists()
  for formula in formulas:
    print ''
    try:
      mod = importlib.import_module('formula.' + formula)
      path_to_module = join(FORMULA_DIR, formula + '.py')
      print 'Starting {} (using {})'.format(formula, path_to_module)
      mod.run()
    except ImportError:
      print_unknown_formula_contribution_hint(formula)


def print_unknown_formula_contribution_hint(formula):
  print 'Unknown formula: {}'.format(formula)
  print ''
  print 'If you feel like {} should be supported by dock, please'.format(formula)
  print 'consider opening an issue or sending a pull request to'
  print ''
  print '       https://github.com/bripkens/dock'
  print ''
  print 'Thanks!'



def list_available_formulas():
  ensure_local_repo_exists()

  print ':: Built-In Formulas'
  for formula in sorted(listdir(FORMULA_DIR)):
    print formula


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('formulas',
                      help='Execute the given formulas in the order in which they are defined on the command line.',
                      nargs='*')
  parser.add_argument('-v', '--version',
                      action='store_true',
                      help='Display current script version')
  parser.add_argument('-u', '--upgrade',
                      action='store_true',
                      help='Upgrade list of available formulas')
  parser.add_argument('-l', '--list',
                      action='store_true',
                      help='List available formulas')
  args = parser.parse_args()

  if (args.version):
    print_version()
  elif (args.upgrade):
    upgrade()
  elif (args.list):
    list_available_formulas()
  elif (len(args.formulas)) == 0:
    parser.print_help()
  else:
    execute_formulas(args.formulas)
