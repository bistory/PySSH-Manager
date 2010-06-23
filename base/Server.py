# -*- coding: utf-8 -*-

class Server:
    """
    Class created by PyUML
    # PyUML: Do not remove this line! # XMI_ID:_9UaAgfqwEd6nNqLO14QYJA

    # PyUML: Associations of this class:
    # PyUML: Association (being 'src') to class Ssh (being 'dst') in package /base/ 
"""

    def __init__(self, host, port = 22, type = 'Server', id = 0):
        """ Created by PyUML """
        self.host = host  # created by PyUML
        self.port = port  # created by PyUML
        self.type = type  # created by PyUML
        self.os = ''  # created by PyUML
        self.id = id  # created by PyUML
        self.hostname = ''  # created by PyUML

    def set_hostname(self, hostname):
        self.hostname = hostname

    def set_os(self, os):
        self.os = os