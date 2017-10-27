#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import app_config
import datetime
import yaml


def run001():
    print 'start'
    os.system('wget https://downloads.gradle.org/distributions/gradle-4.1-bin.zip -O gradle.zip')
    print 'end'


def run(app_name, env):
    cfg = app_config.PiscesConfig.get_instance()
    app = cfg.get_app(app_name)
    # 获取应用的git仓库地址
    git_repo = app.get_git_repo()
    # 克隆git仓库到本地
    print 'git clone -b {0} {1} /opt/k8s-dev-ops/workspace'.format(env, git_repo)
    # os.system('git clone -b {0} {1} /opt/k8s-dev-ops/workspace'.format(env, git_repo))
    # Gradle构建JAR包
    print 'gradle -b /opt/k8s-dev-ops/workspace/{0} clean build'.format(app_name)
    # os.system('gradle -b /opt/k8s-dev-ops/workspace/{0} clean build'.format(app_name))

    docker_registry_url = cfg.get_docker_registry()

    now = datetime.datetime.now()
    now_str = now.strftime('%Y.%m.%d.%H.%M.%S')

    # stream = file('/opt/k8s-dev-ops/workspace/{0}'.format(app_name), 'w')
    stream = file('workspace/{0}'.format(app_name), 'w')
    metadata = {'name': app_name, 'latest_version': now_str}
    yaml.dump(metadata, stream)

    build_cmd = 'docker build -t {0}/{1}:{2} /opt/k8s-dev-ops/dockerfile/{1}'.format(docker_registry_url, app_name,now_str)
    print build_cmd
    # os.system(build_cmd)


def build_img(app_name, env):
    cfg = app_config.PiscesConfig.get_instance()
    app = cfg.get_app(app_name)
    # 获取应用的git仓库地址
    git_repo = app.get_git_repo()
    # 克隆git仓库到本地
    os.system('git clone -b {0} {1} /opt/k8s-dev-ops/workspace'.format(env, git_repo))
    # Gradle构建JAR包
    os.system('gradle -b /opt/k8s-dev-ops/workspace/{0} clean build'.format(app_name))

    docker_registry_url = cfg.get_docker_registry()

    now = datetime.datetime.now()
    now_str = now.strftime('%Y.%m.%d.%H.%M.%S')

    stream = file('/opt/k8s-dev-ops/workspace/{0}'.format(app_name), 'w')
    metadata = {'name': app_name, 'latest_version': now_str}
    yaml.dump(metadata, stream)

    build_cmd = 'docker build -t {0}/{1}:{2} /opt/k8s-dev-ops/dockerfile/{1}'.format(docker_registry_url, app_name,now_str)
    os.system(build_cmd)

def test002():
    s = os.path.join(os.environ['HOME'],'tmp')
    print s
    # print os.environ['HOME']
    # print os.path.expandvars('$HOME')
    # print os.path.expanduser('~')

def test003():
    f = open('workspace/celltower.yaml','w')
    aproject = {'name': 'Silenthand Olleander',
                'race': 'Human',
                'traits': ['ONE_HAND', 'ONE_EYE']
                }

    yaml.dump(aproject,f)
    f.close()



def test004():
    foo = 8080
    bar = str(foo)
    print bar


if __name__ == '__main__':
    # run('celltower','develop')
    test004()
