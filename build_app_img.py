#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import app_config
import datetime
import yaml
import utils.io
import sys


def run():
    if (len(sys.argv)) > 1:
        app_name = sys.argv[1]
    if (len(sys.argv)) > 2:
        env = sys.argv[2]

    init(app_name)
    build(app_name, env)


def build(app_name, env='develop'):
    cfg = app_config.PiscesConfig.get_instance()
    root_dir = cfg.get_root_dir()
    app = cfg.get_app(app_name)
    # 获取应用的git仓库地址
    git_repo = app.get_git_repo()

    workspace_dir = cfg.get_workspace_dir()

    # workspace_dir
    #    + my-app
    #          + source
    #                 + my-app
    #                       - build.gradle
    #                       + build
    #                           + libs
    #                               - my-app.jar
    #          + dockerfile
    #                 - Dockerfile
    #          + k8s
    #                 - my-app-deployment.yaml
    #                 - my-app-service.yaml
    #          - my-app.yaml

    # 克隆git仓库到本地
    source_dir = utils.io.join_path(workspace_dir,app_name,'source')
    dockerfile_dir = utils.io.join_path(workspace_dir,app_name, 'dockerfile')
    metadata_file_path = utils.io.join_path(workspace_dir,app_name,app_name + '.yaml')

    os.system('mkdir -p {0}'.format(dockerfile_dir))

    os.system('git clone -b {0} {1} {2}'.format(env, git_repo, source_dir))
    # Gradle构建JAR包
    os.system('gradle -b {0} clean build'.format(utils.io.join_path(source_dir,'build.gradle')))

    docker_registry_url = cfg.get_docker_registry()
    now = datetime.datetime.now()
    now_str = now.strftime('%Y.%m.%d.%H.%M.%S')

    # stream = file('{1}workspace/{0}'.format(app_name,root_dir), 'w')
    f = open(metadata_file_path, 'w')
    metadata = {'name': app_name, 'latest_version': now_str}
    yaml.dump(metadata, f, default_flow_style=False)
    f.close()

    # 构建docker镜像
    utils.io.replace_str_in_file(utils.io.join_path(root_dir, 'dockerfile', 'app', 'Dockerfile.sample'),
                                 {'${WORKSPACE_DIR}': workspace_dir, '${APP_NAME}': app_name},
                                 utils.io.join_path(dockerfile_dir, "Dockerfile"))

    utils.io.replace_str_in_file(utils.io.join_path(root_dir, 'dockerfile', 'app', 'app.sh.sample'),
                                 {'${APP_NAME}': app_name,'${ENV}': env},
                                 utils.io.join_path(dockerfile_dir, "app.sh"))

    utils.io.copyfile(utils.io.join_path(workspace_dir,app_name,'source','build','libs',app_name + '.jar'),
                      utils.io.join_path(workspace_dir,app_name,'dockerfile',app_name + '.jar'))
    image_name = '{0}/qibei/{1}:{2}'.format(docker_registry_url,app_name,now_str)
    latest_image_name = '{0}/qibei/{1}:latest'.format(docker_registry_url,app_name)
    build_cmd = 'docker build -t {0} {1}'.format(image_name, dockerfile_dir)
    os.system(build_cmd)

    # 将镜像push到docker仓库
    os.system('docker tag {0} {1}'.format(image_name, latest_image_name))
    os.system('docker push {0}'.format(image_name))
    os.system('docker push {0}'.format(latest_image_name))


def init(app_name):
    cfg = app_config.PiscesConfig.get_instance()
    workspace_dir = cfg.get_workspace_dir()
    source_dir = utils.io.join_path(workspace_dir, app_name, 'source')
    os.system('rm -rf {0}'.format(source_dir))


if __name__ == '__main__':
    run()
