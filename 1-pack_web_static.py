#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static
folder of your AirBnB Clone repo,
using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    time = datetime.now()
    filename = f"web_static_{time.year}{time.month:02d}{time.day:02d}{time.hour:02d}{time.minute:02d}{time.second:02d}.tgz"
    local("tar -zcvf {0} ./web_static ;\
          mkdir versions ;\
          mv {0} versions/ ".format(filename))
    location = f"versions/{filename}"
    return location

do_pack()