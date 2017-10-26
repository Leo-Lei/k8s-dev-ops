import yaml


class PiscesConfig(object):
    __instance = None

    def __init__(self):
        f = open('_config.yaml')
        cfg = yaml.load(f)

        # self.mysql = PiscesConfig.Mysql(cfg['mysql'])
        # self.dockerfile = PiscesConfig.Dockerfile(cfg['dockerfile'])
        self.docker_registry = cfg['docker-registry']
        self.root_dir = cfg['root_dir']
        # self.rds_mysql_sync = PiscesConfig.RdsMysqlSync(cfg['rds-mysql-sync'])

        apps = {}
        for app in cfg['apps']:
            name = app['name']
            apps[name] = PiscesConfig.PiscesApp(app)
        self.apps = apps

        # self.jar_dir = cfg['jar_dir']
        # self.logs_dir = cfg['logs_dir']
        # self.data_dir = cfg['data_dir']

    def get_mysql(self):
        """
        :rtype: PiscesConfig.Mysql
        """
        return self.mysql

    def get_docker_registry(self):
        """
        :rtype: str
        """
        return self.docker_registry

    def get_root_dir(self):
        """
        :rtype: str
        """
        return self.root_dir

    def get_rds_mysql_sync(self):
        """
        :rtype: PiscesConfig.RdsMysqlSync
        """
        return self.rds_mysql_sync

    def get_dockerfile(self):
        """
        :rtype: PiscesConfig.Dockerfile
        """
        return self.dockerfile

    def get_app(self, app):
        """
        :rtype: PiscesConfig.PiscesApp
        """
        return self.apps[app]

    def get_jar_dir(self):
        """
        :rtype: PiscesConfig.PiscesApp
        """
        return self.jar_dir

    def get_logs_dir(self):
        """
        :rtype: PiscesConfig.PiscesApp
        """
        return self.logs_dir

    def get_data_dir(self):
        return self.data_dir

    @staticmethod
    def get_instance():
        """
        :rtype: PiscesConfig
        """
        if PiscesConfig.__instance is None:
            PiscesConfig.__instance = PiscesConfig()
        return PiscesConfig.__instance

    class Dockerfile:
        def __init__(self, cfg):
            self.zookeeper_download_url = cfg['zookeeper']['download_url']
            self.disconf_download_url = cfg['disconf']['download_url']
            self.disconf_archive_top_dir = cfg['disconf']['archive_top_dir']
            self.disconf_host = cfg['disconf']['host']
            self.springboot_java_opts = cfg['springboot']['java_opts']

        def get_zookeeper_download_url(self):
            """
            :rtype: str
            """
            return self.zookeeper_download_url

        def get_disconf_download_url(self):
            """
            :rtype: str
            """
            return self.disconf_download_url

        def get_disconf_archive_top_dir(self):
            """
            :rtype: str
            """
            return self.disconf_archive_top_dir

        def get_disconf_host(self):
            """
            :rtype: str
            """
            return self.disconf_host

        def get_springboot_java_opts(self):
            """
            :rtype: str
            """
            return self.springboot_java_opts

    class DockerRegistry:
        def __init__(self, cfg):
            self.docker_registry = cfg['docker-registry']

        def get_docker_registry(self):
            """
            :rtype: str
            """
            return self.docker_registry

    class MysqlInitUsers:
        def __init__(self, user, password):
            self.user = user
            self.password = password

        def get_user(self):
            """
            :rtype: str
            """
            return self.user

        def get_password(self):
            """
            :rtype: str
            """
            return self.password

    class Mysql:
        def __init__(self, cfg):
            self.init_users = []
            for user in cfg['initial_users']:
                self.init_users.append(PiscesConfig.MysqlInitUsers(user['user'], user['password']))

        def get_init_users(self):
            """
            :rtype: list[PiscesConfig.MysqlInitUsers]
            """
            return self.init_users

    class RdsMysqlSync:
        def __init__(self, cfg):
            _list = []
            rds_list = cfg['rds']
            for rds in rds_list:
                _list.append(PiscesConfig.RdsMysqlSyncRds(rds))
            self.rds = _list
            self.merge_mysql = PiscesConfig.RdsMysqlSyncMerge(cfg['merge-mysql']['server_id'])

        def get_rds(self):
            """
            :rtype: PiscesConfig.RdsMysqlSyncRds
            """
            return self.rds

        def get_merge_mysql(self):
            """
            :rtype: PiscesConfig.RdsMysqlSyncMerge
            """
            return self.merge_mysql

    class RdsMysqlSyncMerge:
        def __init__(self, serverid):
            self.serverid = serverid

        def get_serverid(self):
            """
            :rtype: str
            """
            return self.serverid

    class RdsMysqlSyncRds:
        def __init__(self, cfg):
            self.name = cfg['name']
            self.backupurl = cfg['backup_url']
            self.serverid = cfg['server_id']
            self.host = cfg['host']
            self.user = cfg['user']
            self.password = cfg['password']

        def get_name(self):
            """
            :rtype: str
            """
            return self.name

        def get_backupurl(self):
            """
            :rtype: str
            """
            return self.backupurl

        def get_serverid(self):
            """
            :rtype: str
            """
            return self.serverid

        def get_host(self):
            """
            :rtype: str
            """
            return self.host

        def get_user(self):
            """
            :rtype: str
            """
            return self.user

        def get_password(self):
            """
            :rtype: str
            """
            return self.password

    class PiscesApp:
        def __init__(self, app):
            self.name = app['name']
            self.git_repo = app['git_repo']
            # self.dubbo_port = app['dubbo_port']
            # self.http_port = app['http_port']

        def get_name(self):
            """
            :rtype: str
            """
            return self.name

        def get_git_repo(self):
            """
            :rtype: str
            """
            return self.git_repo

        # def get_http_port(self):
        #     """
        #     :rtype: str
        #     """
        #     return self.http_port
        #
        # def get_dubbo_port(self):
        #     """
        #     :rtype: str
        #     """
        #     return self.dubbo_port
