#! /usr/bin/bash

# Install Java 8
yum install -y java-1.8.0-openjdk-devel.x86_64

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

GRADLE_HOME=/opt/gradle


${ROOT_DIR}/install_gradle.py ${GRADLE_HOME} ${ROOT_DIR}.tmp