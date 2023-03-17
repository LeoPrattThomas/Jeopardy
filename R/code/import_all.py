import subprocess
import os

#run r script
path = "R/code/Transform.R"

with open(path,'w') as f: f.write('#!/bin/sh\nexit 0')

assert os.path.isfile(path)
os.chmod(path, 0b111101101)
subprocess.call(path)

#subprocess.call ("/usr/bin/Rscript --vanilla R/code/Transform.R", shell=True)
import R.code.import_topic
import R.code.import_points
import R.code.import_qustions
