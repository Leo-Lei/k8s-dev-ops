#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import app_config
import yaml
import utils.io
import sys


def run():
    if (len(sys.argv)) > 1:
        app_name = sys.argv[1]
        is_first_time = False
    if (len(sys.argv)) > 2:
        is_first_time = sys.argv[2]
    init(app_name)
    if is_first_time:
        first_time_publish(app_name)
    else:
        update(app_name)


def first_time_publish(app_name, env='develop'):
    cfg = app_config.PiscesConfig.get_instance()
    root_dir = cfg.get_root_dir()
    app = cfg.get_app(app_name)
    docker_registry = cfg.get_docker_registry()

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

    metadata_file_path = utils.io.join_path(workspace_dir, app_name, app_name + '.yaml')
    f = open(metadata_file_path)
    print yaml.load(f)
    f.close()

    for resource in app.get_resources():
        if resource['name'] == 'deployment':
            utils.io.replace_str_in_file(utils.io.join_path(root_dir, 'k8s', 'deployment.yaml.sample'),
                                         {'${APP_NAME}': app_name, '${DOCKER_REGISTRY}': docker_registry},
                                         utils.io.join_path(workspace_dir, app_name, 'k8s',
                                                            app_name + '-deployment.yaml'))
        if resource['name'] == 'service':
            node_port = resource['node_port']
            utils.io.replace_str_in_file(utils.io.join_path(root_dir, 'k8s', 'service.yaml.sample'),
                                         {'${APP_NAME}': app_name, '${DOCKER_REGISTRY}': docker_registry, '${NODE_PORT}': node_port},
                                         utils.io.join_path(workspace_dir, app_name, 'k8s', app_name + '-service.yaml'))

    # os.system('kubectl create -f {0}/{1}/k8s/'.format(workspace_dir, app_name))


def update(app_name, env='develop'):
    cfg = app_config.PiscesConfig.get_instance()
    docker_registry = cfg.get_docker_registry()

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

    metadata_file_path = utils.io.join_path(workspace_dir, app_name, app_name + '.yaml')

    f = open(metadata_file_path)
    metadata = yaml.load(f)
    latest_version = metadata['latest_version']
    f.close()

    new_image_name = '{0}/qibei/{1}:{2}'.format(docker_registry,app_name,latest_version)
    # os.system('kubelet rolling-update {0} --image={1}',app_name,new_image_name)


def init(app_name):
    cfg = app_config.PiscesConfig.get_instance()
    workspace_dir = cfg.get_workspace_dir()
    os.system('mkdir -p {0}/{1}/k8s'.format(workspace_dir,app_name))


if __name__ == '__main__':
    run()
