import os
import sys

sim_folder=sys.argv[1]
exec_folder=sys.argv[2]

os.chdir(sim_folder)
simulations = next(os.walk('.'))[1]

for i in simulations:
    os.system("cd " + i + " && "+ exec_folder + "SU2_SOL cfg/sosu2.cfg")


