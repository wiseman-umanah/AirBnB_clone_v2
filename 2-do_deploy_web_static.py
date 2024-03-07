#!/usr/bin/python3
"""a Fabric script
(based on the file 1-pack_web_static.py)
that distributes an archive
to your web servers,
using the function do_deploy"""
from fabric.api import *
from os import path


env.user = "ubuntu"
env.hosts = ['100.25.181.103', '54.160.70.20']
def do_deploy(archive_path):
    if archive_path is None:
        returun False
    try:
        tmp = archive.split("/")
        file_ext = tmp[-1]
        ext, file_name = path.splitext(file_ext)
        put(archive_path, "/tmp/")
        unbundle_path = f"/data/web_static/releases/{file_name}/"
        run(f"mkdir -p {unbundle_path}")
        run(f"tar -xzf /tmp/{file_ext} -C {unbundle_path}")
        #delete archive from web_server
        run(f"rm /tmp/{filename}")
        run(f"mv {unbundle_path}web_static/* {unbundle_path}")
        run(f"rm -rf {unbundle_path}web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {unbundle_path} /data/web_static/current")
        print("New version deployed!")
        print("\nDone")
        return True
    except:
        return False

