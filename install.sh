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

wget https://codeload.github.com/Leo-Lei/k8s-dev-ops/zip/master -O /opt/k8s-dev-ops.zip
unzip /opt/k8s-dev-ops.zip -d ROOT_DIR
rm -rf /opt/k8s-dev-ops.zip

