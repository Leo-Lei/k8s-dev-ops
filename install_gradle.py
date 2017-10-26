#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os


def run():
    if(len(sys.argv)) > 1:
        gradle_home = sys.argv[1]
        print gradle_home
        tmp_dir = sys.argv[2]
        print tmp_dir
        gradle_version = '4.1'
        print 'start to download gradle'
        os.system('wget https://downloads.gradle.org/distributions/gradle-{0}-bin.zip -O {1}/gradle.zip'.format(gradle_version,tmp_dir))
        print 'finish download gradle'
        os.system('rm -rf {0}'.format(tmp_dir))
        os.system('mkdir -p {0}'.format(tmp_dir))
        os.system('unzip {0}/gradle.zip -d {0}/gradle'.format(tmp_dir))
        os.system('cp -r {0}/gradle/gradle-{1}/* {2}'.format(tmp_dir,gradle_version,gradle_home))

if __name__ == '__main__':
    run()
