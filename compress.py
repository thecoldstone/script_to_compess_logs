import os
import tarfile
from datetime import datetime

def compress(path, format):

    # os.chdir(path)

    name = "LOGS" + str(datetime.timestamp(datetime.now())).replace('.', '')

    print(os.getcwd())

    tar = tarfile.open(name + format, "w:gz")
    tar.add(path, arcname=name)
    tar.close()

    # print(path, name)

compress('/var/log', '.tar.gz')