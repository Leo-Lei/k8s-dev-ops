自己写的一些Python脚本，基于k8s这个容器管理平台，来构建，发布镜像。并发布应用。


# 安装

```bash
curl -s "https://raw.githubusercontent.com/Leo-Lei/k8s-dev-ops/master/install.sh" | bash
```
执行该命令会从github上下载项目到本地某个目录。默认是`/opt/k8s-dev-ops`。如果想安装到别的目录，可以下载该脚本，修改sh脚本里面的ROOT_PATH变量，然后执行即可。

发布应用的脚本需要本机安装了`kubectl`工具来和k8s集群通信。

# 如何使用
* _config.yaml: 工程的配置文件
* install_java.py: 安装java
* install_docker.py: 安装 docker
* build_app_img: 构建docker镜像，并push到私有仓库
* publish_app.py: 发布应用到k8s

