FROM centos:7
MAINTAINER Lei Wei <leiwei2094@gmail.com>
ENV REFRESHED_AT 2017-04-17
RUN yum install -y java-1.8.0-openjdk.x86_64
RUN yum install -y curl
COPY app.sh /opt/app.sh
RUN chmod +x /opt/app.sh
ENTRYPOINT ["/opt/app.sh"]