import subprocess
import os
import sys

#run r script
path = "R/code/Transform.R"
os.chmod(path, 0b111101101)
res = subprocess.call(f"Rscript {path}", shell=True)


#Import into database
import R.code.import_topic
import R.code.import_points
import R.code.import_qustions

#exit pythone
sys.exit()
