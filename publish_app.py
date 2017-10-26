#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import app_config
import yaml


def run(app_name, is_first_time=False):
    cfg = app_config.PiscesConfig.get_instance()
    root_dir = cfg.get_root_dir()
    docker_registry = cfg.get_docker_registry()

    if is_first_time:
        os.system('kubectl create -f {0}/workspace/{1}/'.format(root_dir, app_name))

    f = open('{0}workspace/{1}', root_dir, app_name)
    cfg = yaml.load(f)
    latest_version = cfg['latest_version']

    os.system('kubectl rolling-update {0} --image={1}/{0}:{2}'.format(app_name, docker_registry, latest_version))


if __name__ == '__main__':
    run()
