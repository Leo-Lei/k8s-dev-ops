#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import app_config
import utils.io


def run():
    cfg = app_config.PiscesConfig.get_instance()
    root_dir = cfg.get_root_dir()
    docker_registry = cfg.get_docker_registry()

    if not os.path.exists('/etc/docker'):
        os.system('mkdir /etc/docker')

    utils.io.replace_str_in_file('{0}daemon.json.sample'.format(root_dir),
                                 {'${docker_registry}': docker_registry},
                                 '/etc/docker/daemon.json.sample')


if __name__ == '__main__':
    run()
