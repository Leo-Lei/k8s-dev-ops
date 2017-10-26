#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import app_config
import datetime
import yaml


def run(app_name, env):
    cfg = app_config.PiscesConfig.get_instance()
    root_dir = cfg.get_root_dir()
    app = cfg.get_app(app_name)
    # 获取应用的git仓库地址
    git_repo = app.get_git_repo()
    # 克隆git仓库到本地
    os.system('git clone -b {0} {1} {2}workspace'.format(env, git_repo, root_dir))
    # Gradle构建JAR包
    os.system('gradle -b {1}workspace/{0} clean build'.format(app_name, root_dir))

    docker_registry_url = cfg.get_docker_registry()

    now = datetime.datetime.now()
    now_str = now.strftime('%Y.%m.%d.%H.%M.%S')

    stream = file('{1}workspace/{0}'.format(app_name,root_dir), 'w')
    metadata = {'name': app_name, 'latest_version': now_str}
    yaml.dump(metadata, stream)

    # 构建docker镜像
    build_cmd = 'docker build -t {0}/{1}:{2} {3}dockerfile/{1}'.format(docker_registry_url, app_name, now_str, root_dir)
    os.system(build_cmd)

    # 将镜像push到docker仓库
    os.system('docker tag {0}/{1}:{2} {0}/{1}:latest'.format(docker_registry_url,app_name,now_str))
    os.system('docker push {0}/{1}:{2}'.format(docker_registry_url, app_name, now_str))
    os.system('docker push {0}/{1}:latest'.format(docker_registry_url, app_name))


if __name__ == '__main__':
    run()
