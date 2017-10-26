#! /usr/bin/bash

# Install Java 8
yum install -y java-1.8.0-openjdk-devel.x86_64

# Install sdkman to install Gradle
GRADLE_VERSION=4.1
curl -s "https://get.sdkman.io" | bash
sdk install gradle ${GRADLE_VERSION}

ROOT_DIR=/opt/k8s-dev-ops
mkdir -p ${ROOT_DIR}.bak
cp ${ROOT_DIR}/_config.yaml ${ROOT_DIR}.bak/_config.yaml

rm -rf ${ROOT_DIR}

mkdir -p ${ROOT_DIR}
mkdir -p ${ROOT_DIR}.tmp
wget https://codeload.github.com/Leo-Lei/k8s-dev-ops/zip/master -O ${ROOT_DIR}.bak/k8s-dev-ops.zip
unzip ${ROOT_DIR}.bak/k8s-dev-ops.zip -d ${ROOT_DIR}.tmp
cp -r ${ROOT_DIR}.tmp/k8s-dev-ops-master/* ${ROOT_DIR}
rm -rf ${ROOT_DIR}.tmp

