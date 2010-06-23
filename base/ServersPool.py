# -*- coding: utf-8 -*-

from base.Ssh import Ssh

class ServersPool(object):
    """
    Class created by PyUML
    # PyUML: Do not remove this line! # XMI_ID:_2Rl2UPq2Ed6nNqLO14QYJA

    # PyUML: Associations of this class:
    # PyUML: Association (being 'dst') to class Db (being 'src') in package /base/ 
    # PyUML: Association (being 'dst') to class Ssh (being 'src') in package /base/ 
"""

    def __init__(self):
        self.servers = {}  # created by PyUML
        self.currentEl = 0
        
    def __iter__(self):
        return self
    
    def __len__(self):
        return len(self.servers)
    
    def __setitem__(self, key, item):
        self.servers[key] = item
        
        self.rewind()

    """
    Sends a command to the server's pool
    """
    def sendCommand(self, command):
        output = []
        for serv in self.servers:
            output.append(serv.sendCommand(command))
        return output

    """
    Adds a user
    """
    def addUser(self, login, password):
        raise NotImplementedError

    """
    Add a server into the pool
    """
    def add(self, id, host, port, type, login, password):
        connection = Ssh(host, port, type, id)
        connection.set_auth(login, password)
        self.servers[id] = connection
        
        self.rewind()

    """
    Edit a server into the pool
    """
    def edit(self, id, host, port, type, login, password):
        self.servers[id].close()
        connection = Ssh(host, port, type, id)
        connection.set_auth(login, password)
        self.servers[id] = connection
        
        self.rewind()

    """
    Delete a server from the pool
    """
    def delete(self, server):
        return self.servers.remove(server)

    """
    Delete a server from the pool at the given index
    """
    def deleteAt(self, index):
        return self.servers.pop(index)

    """
    Returns next server of the enumerable
    """
    def next(self):
        return self.iter.next()

    """
    Returns previous server of the enumerable
    """
    def prev(self):
        return self.iter.prev()

    """
    Rewinds the iterator
    """
    def rewind(self):
        self.iter = self.servers.iteritems()

    """
    Returns the current server of the enumerable
    """
    def current(self):
        if(len(self.servers) == 0):
            raise ReferenceError
        else:
            print self.currentEl
            return self.servers[self.currentEl]

    """
    Returns the server at the given index
    """
    def __getitem__(self, index):
        if(self.servers.has_key(index)):
            return self.servers[index]
        else:
            raise ReferenceError

    """
    Returns the server at the given index
    """
    def has_key(self, index):
        return self.servers.has_key(index)

    """
    Returns the server at the given index
    """
    def __delitem__(self, index):
        if(self.servers.has_key(index)):
            self.servers[index].close()
            del self.servers[index]
        else:
            raise ReferenceError

    """
    Returns the latest added server
    """
    def last(self):
        if(len(self.servers) == 0):
            raise ReferenceError
        else:
            print len(self.servers)-1
            return self.servers[len(self.servers)-1]
