class BancoDeDados:
    def __init__(self, user, passwd):
        # DB credenciais
        self.username = user
        self.passwd = passwd

        # Server string connection
        self.server = ''
        self.schema = ''
        self.port = 0
        self.table = ''

    def set_server(self, value):
        self.server = value

    def set_schema(self, value):
        self.schema = value

    def set_port(self, value):
        self.port = value

    def set_table(self, value):
        self.table = value