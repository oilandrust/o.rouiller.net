from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

from fabric.network import ssh

PRODUCTION_HOST = "ubuntu@ec2-54-154-123-179.eu-west-1.compute.amazonaws.com"

# ssh -i orouiller.net.pem ubuntu@c2-54-154-123-179.eu-west-1.compute.amazonaws.com

#production
env.hosts = [PRODUCTION_HOST]
env.key_filename = ["orouiller.net.pem"]
env.use_shell = True
env.port = 22


def test_alive():
    run("ls")

def test():
    with settings(warn_only=True):
        result = local('./manage.py test', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")
    
def prepare_deploy():
    test()
    commit()
    push()
    
def deploy():
    code_dir = 'orouiller.net/'

    with cd(code_dir):
        run('git pull')
        run("sudo service apache2 reload")
        
