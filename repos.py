"""
Git repository manager.

Install, update, and uninstall multiple Git repositories
"""
from os import listdir
from os.path import join

from fabric.api import local, lcd as cd, task


@task
def install(path, repo):
    """
    Install a git repo in the directory.

        path: path of directory to install in
        repo: name of git repo to clone
    """
    with cd(path):
        local('git clone %s' % repo)


@task
def update(path, repo=None):
    """
    Update a git repo in the directory or all of them.

        path: path to git repos
        repo: name of git repo to update
    """
    if repo is None:
        for repo in listdir(path):
            update(path, repo)
    else:
        with cd(join(path, repo)):
            local('git pull')


@task
def uninstall(path, repo=None):
    """
    Uninstall a git repo in the directory.

        path: path to git repos
        repo: name of git repo to remove
    """
    if repo is None:
        for repo in listdir(path):
            uninstall(path, repo)
    else:
        with cd(path):
            local('rm -fr %s' % repo)


@task
def from_config(path, name):
    """
    Install git repos from a config file in the directory.

        path: path of directory to install in
        name: name of the config file

    The config file should contain single repo name on each line.
    """
    with open(name) as f:
        for repo in f:
            install(path, repo)
