#! /usr/bin/bash

##################################################
#           使用以下命令来一键安装:
# curl -s "https://raw.githubusercontent.com/Leo-Lei/k8s-dev-ops/master/install.sh" | bash
##################################################

ROOT_DIR=/opt/k8s-dev-ops
mkdir -p ${ROOT_DIR}.bak
mkdir -p ${ROOT_DIR}.tmp

cp ${ROOT_DIR}/_config.yaml ${ROOT_DIR}.bak/_config.yaml

rm -rf ${ROOT_DIR}
mkdir -p ${ROOT_DIR}

wget https://codeload.github.com/Leo-Lei/k8s-dev-ops/zip/master -O ${ROOT_DIR}.bak/k8s-dev-ops.zip
unzip ${ROOT_DIR}.bak/k8s-dev-ops.zip -d ${ROOT_DIR}.tmp
cp -r ${ROOT_DIR}.tmp/k8s-dev-ops-master/* ${ROOT_DIR}
rm -rf ${ROOT_DIR}.tmp

chmod 744 ${ROOT_DIR}/*.py