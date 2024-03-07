#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static
folder of your AirBnB Clone repo,
using the function do_pack.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Function used to
    pack files to .tgz"""

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None

"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web server"""

from os.path import exists
env.hosts = ['100.25.181.103', '54.160.70.20']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
    """Final deployment
    to web servers"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)

