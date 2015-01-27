from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.api import local, warn_only
from fabric.network import ssh

PRODUCTION_HOST = "ubuntu@ec2-54-154-123-179.eu-west-1.compute.amazonaws.com"

#production
env.hosts = [PRODUCTION_HOST]
env.key_filename = ["admin/orouiller.net.pem"]
env.use_shell = True
env.port = 22

def connect():
    local("ssh -i admin/orouiller.net.pem ubuntu@ec2-54-154-123-179.eu-west-1.compute.amazonaws.com")

def test_alive():
    run("ls")

def test():
    with settings(warn_only=True):
        result = local('./manage.py test', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    with settings(warn_only=True):
        local("git add -p && git commit", capture=False)

def push():
    local("git push")
    
def prepare():
    test()
    commit()
    push()
    
def deploy():
    code_dir = 'orouiller.net/'

    with cd(code_dir):
        run('git pull')
        with prefix('workon orouiller'):
            run('python manage.py migrate')
            run('echo "yes\n" | python manage.py collectstatic')
            run('sudo cp -r static/ /var/www/orouiller.net/')
        run("sudo service apache2 reload")
        
