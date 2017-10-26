class AppMetadata:
    def __init__(self, cfg):
        self.name = cfg['name']
        self.latest_version = cfg['latest_version']

    def get_name(self):
        """
        :rtype: str
        """
        return self.name

    def get_latest_version(self):
        """
        :rtype: str
        """
        return self.latest_version