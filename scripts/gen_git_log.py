import os
import sys
import argparse
import subprocess

debug = True

def dprint(*arg):
  global debug
  if debug:
    print arg

class cd:
  def __init__(self, newPath):
    self.newPath = newPath

  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)

  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)


def gen_log(all_java_file):
  git_cmd = "git log --ignore-all-space --function-context --patch --no-merges  --date=short "
  print all_java_file
  dir_name = os.path.dirname(all_java_file)
  file_name = os.path.basename(all_java_file)
  dprint("dir_name ---> ", dir_name)
  dprint("file_name ---> ", file_name)

  with cd(dir_name):
    # we are in dir_name
    for line in open(file_name):
      java_file = line.strip()
      patch_file, extension = os.path.splitext(java_file)
      patch_file += ".patch"
      shell_cmd = git_cmd + "{0} >> {1}".format(java_file , patch_file)
      #shell_cmd = git_cmd + java_file
      '''
      print shell_cmd
      proc = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE)
      for log in proc.stdout:
        print line
      '''
      os.system(shell_cmd)

    #subprocess.call("ls")

def main(argv=None):
  if argv is None:
    argv = sys.argv

  parser = argparse.ArgumentParser(description='Github log generation tool')
  parser.add_argument('inputFile',help="Input File containing all java files")
  args = parser.parse_args()

  input_file = args.inputFile

  if os.path.isfile(input_file):
    try:
      inf = open(input_file, 'r')
      for line in inf:
        gen_log(line.strip())

    except IOError:
      print 'Oh dear!! ', input_file , " does not exist"


if __name__=="__main__":
  sys.exit(main())
