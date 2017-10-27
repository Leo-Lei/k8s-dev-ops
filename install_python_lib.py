#! /usr/bin/python
# -*- coding: utf-8 -*-

import os


def run():
    # Install Python pip
    os.system('easy_install pip')
    # Install yaml
    os.system('pip install pyyaml')


if __name__ == '__main__':
    run()
