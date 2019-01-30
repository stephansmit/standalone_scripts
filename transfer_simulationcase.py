import argparse
import os
parser = argparse.ArgumentParser(description='Create a hostfile for Slurm batchjob')
parser.add_argument('--casename', help="the filename of the hostfile")
args = parser.parse_args()

casename = args.casename

simdir = os.environ['SIMULATION_DIR']
archdir = "/archive/stephans/simulations/"
saracasedir = os.path.join(archdir,casename)
os.system('rsync -a --delete stephans@surfsara:%s %s' % (saracasedir, simdir))
