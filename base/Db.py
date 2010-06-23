# -*- coding: utf-8 -*-
import sqlite3

class Db:
    """
    Class created by PyUML
    # PyUML: Do not remove this line! # XMI_ID:_9UaAgPqwEd6nNqLO14QYJA

    # PyUML: Associations of this class:
    # PyUML: Association (being 'src') to class ServersPool (being 'dst') in package /base/ 
"""

    def __init__(self):
        # Chemin d'accès au fichier de base de données
        self.filename = '../db/sshmngr.sqlite'
        # Connexion à la base de données
        self.sql = sqlite3.connect(self.filename)
        # Défintition du type de base des arguments des requêtes SQL
        self.sql.text_factory = str
        # Définition du type de retour des lignes de la base de données
        self.sql.row_factory = sqlite3.Row
        # Création d'un curseur
        self.cursor = self.sql.cursor()
        
    def __del__(self):
        # Fermeture de la base de données à la destruction
        self.close()

    def getServers(self):
        out = []
        results = self.execute("SELECT id,host,port,type,defaultlogin_id FROM servers ORDER BY id ASC")
        for result in results:
            res = {
                   'id' : result['id'],
                   'host' : result['host'],
                   'port' : result['port'],
                   'type' : result['type'],
                   'defaultlogin_id' : result['defaultlogin_id']
                   }
            if result['defaultlogin_id'] != 0:
                loginpass = self.getAuthById(result['defaultlogin_id'])
                res['login'] = loginpass['login']
                res['password'] = loginpass['password']
            else:
                res['login'] = 'rsa'
                res['password'] = 'rsa'
            out.append(res)
            
        return out
    
    # Renvoie 0, 1 ou plusieurs résultats
    def getServersByDefaultId(self, id):
        # Récupère la liste des serveurs dont le login par défaut est celui précisé en argument
        return self.execute("SELECT id,host,port,type FROM servers WHERE defaultlogin_id=? ORDER BY id ASC", [str(id)])
    
    # Renvoie 0 ou 1 résultat
    def getDefaultLoginIdByServer(self, id):
        cursor = self.sql.cursor()
        # Récupère le login par défaut d'un serveur donné
        db_query = cursor.execute("SELECT defaultlogin_id FROM servers WHERE id=?", [str(id)])
        return db_query.fetchone()

    def getServer(self, id):
        cursor = self.sql.cursor()
        db_query = cursor.execute("SELECT id,host,port,type,defaultlogin_id FROM servers WHERE id=?", [str(id)])
        result = db_query.fetchone()
        
        res = {
               'id' : result['id'],
               'host' : result['host'],
               'port' : result['port'],
               'type' : result['type'],
               'defaultlogin_id' : result['defaultlogin_id']
               }
        if result['defaultlogin_id'] != 0:
            loginpass = self.getAuthById(result['defaultlogin_id'])
            res['login'] = loginpass['login']
            res['password'] = loginpass['password']
        else:
            res['login'] = 'rsa'
            res['password'] = 'rsa'
            
        return res
        #db_query = self.cursor.execute("SELECT s.id,s.host,s.port,s.type,s.defaultlogin_id,u.login,u.password FROM servers s, users u WHERE s.id=? AND s.defaultlogin_id=u.id", [str(id)])
        #return db_query.fetchone()

    #def getAuth(self, server):
    #    return self.execute("SELECT login,password FROM users WHERE id = (SELECT defaultlogin_id FROM servers WHERE host=?)", [str(server.server.host)])

    def getAuthById(self, id):
        cursor = self.sql.cursor()
        db_query = cursor.execute("SELECT login,password FROM users WHERE id = ?", [str(id)])
        return db_query.fetchone()

    def getAuths(self):
        return self.execute("SELECT id,login,password FROM users ORDER BY id ASC")

    def getServerType(self):
        """ Created by PyUML """

    def addServer(self, host, port, type, defaultlogin_id):
        args = (str(host), str(port), str(type), str(defaultlogin_id))
        self.cursor.execute("INSERT INTO servers (host,port,type,defaultlogin_id) VALUES (?,?,?,?)", args)
        self.sql.commit()
        return self.cursor.lastrowid

    def getActions(self):
        """ Created by PyUML """

    def close(self):
        self.sql.close()

    def addUser(self, login, password):
        self.cursor.execute("INSERT INTO users (login,password) VALUES (?,?)", (str(login), str(password)))
        self.sql.commit()
        return self.cursor.lastrowid

    def removeServer(self, id):
        self.cursor.execute("DELETE FROM servers WHERE id=?", [str(id)])
        self.sql.commit()

    def removeUser(self, id):
        self.cursor.execute("DELETE FROM users WHERE id=?", [str(id)])
        self.sql.commit()

    def execute(self, command, args = None):
        if args == None:
            return self.cursor.execute(command)
        else:
            return self.cursor.execute(command, (args))
        
    def editServer(self, id, host, port, type, defaultlogin_id):
        self.cursor.execute("UPDATE servers SET host=?,port=?,type=?,defaultlogin_id=? WHERE id=?", (str(host), str(port), str(type), str(defaultlogin_id), str(id)))
        self.sql.commit()
        
    def editUser(self, id, login, password):
        self.cursor.execute("UPDATE users SET login=?,password=? WHERE id=?", (str(login), str(password), str(id)))
        self.sql.commit()

    def getBookmarks(self):
        return self.execute("SELECT id,command,label FROM stored_commands")

    def getBookmarkById(self, id):
        db_query = self.execute("SELECT command,label FROM stored_commands WHERE id = ?", [str(id)])
        return db_query.fetchone()
    
    def addBookmark(self, command, label):
        self.cursor.execute("INSERT INTO stored_commands (command,label) VALUES (?,?)", (str(command), str(label)))
        self.sql.commit()
        return self.cursor.lastrowid
    
    def editBookmark(self, id, command, label):
        self.cursor.execute("UPDATE stored_commands SET command=?,label=? WHERE id=?", (str(command), str(label), str(id)))
        self.sql.commit()
    
    def removeBookmark(self, id):
        self.cursor.execute("DELETE FROM stored_commands WHERE id=?", ([str(id)]))
        self.sql.commit()
        
