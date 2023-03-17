import subprocess
import os

#run r script
path = "R/code/Transform.R"
assert os.path.isfile(path)
with open(path, "r") as f:
    pass
subprocess.call (path)

#subprocess.call ("/usr/bin/Rscript --vanilla R/code/Transform.R", shell=True)
import R.code.import_topic
import R.code.import_points
import R.code.import_qustions