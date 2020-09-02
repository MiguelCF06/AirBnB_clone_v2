#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder
"""

from fabric.api import local
from os.path import isdir
from datetime import datetime

time_format = "%Y%m%d%H%M%S"


def do_pack():
    """Generation of the tgz file"""
    try:
        cur_date = datetime.now().strftime(time_format)
        if isdir("versions") is False:
            local("mkdir versions")
        file_tgz = "versions/web_static_{}.tgz".format(cur_date)
        local("tar -cvzf {} web_static".format(file_tgz))
        return file_tgz
    except:
        return None
