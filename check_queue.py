import subprocess


user = subprocess.check_output(['whoami']).strip('\n')
listwithprocess = subprocess.check_output(['squeue', '-p', 'normal']).split('\n')


for index, i in enumerate(listwithprocess[1:]):
    if user in i:
	jobname = i.split()[2]
	print("Job %s is at %i in the queue"% (jobname,index))


