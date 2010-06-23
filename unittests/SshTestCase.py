# -*- coding: cp1252 -*-
'''
Created on 7 janv. 2010

@author: Thomas Lété
'''
# Import du module de UnitTests
import unittest
# Import de la classe Ssh créée pour l'application
from base.Ssh import Ssh

class Test(unittest.TestCase):
    """
     # PyUML: Do not remove this line! # XMI_ID:_D_YrsvtqEd68cOasAFD1Kg
    """

    # Test automatique d'une connexion simple à SSH
    def testSimpleConnection(self):
        # Informations de connexion au serveur
        host = '10.32.4.30'
        user = 'test'
        passwd = 'test'
        # La commande demande de renvoyer le login de l'utilisateur
        # Soit "test" suivi d'un retour à la ligne
        cmd = 'echo $USER'
        
        # Instanciation d'une connexion SSH
        client = Ssh(host, 22, "", 0)
        # Définition des login et password
        client.set_auth(user, passwd)
        # Connexion au serveur
        client.connect_thread()
        # Envoi de la commande et récupération du retour
        out = client.sendCommand(cmd)
        # Fermeture de la connexion
        client.close()
        
        # Vérification de la valeur récupérée
        # Si elle correspond à celle attendue (test\n)
        # Alors le test est correct
        # Sinon, il est négatif
        self.assertEqual(out, user + "\n")
        
    def testConcurrentConnections(self):
        host = '10.32.4.30'
        cmd = 'echo $USER'
        
        user1 = 'test'
        passwd1 = 'test'
        
        user2 = 'test2'
        passwd2 = 'test2'
        
        # Connection 1
        client = Ssh(host, 22, "", 0)
        client.set_auth(user1, passwd1)
        client.connect_thread()
        out1 = client.sendCommand(cmd)
        client.close()
        
        # Connection 2
        client2 = Ssh(host, 22, "", 0)
        client2.set_auth(user2, passwd2)
        client2.connect_thread()
        out2 = client2.sendCommand(cmd)
        client2.close()
        
        self.assertEqual(out1,  "%s\n" % user1)
        self.assertEqual(out2,  "%s\n" % user2)
        
    def testInteractiveCommand(self):
        host = '10.32.4.30'
        cmd = 'sudo -S echo $USER'
        #cmd = 'sudo -S adduser machin'
        user = 'test'
        passwd = 'test'
        
        client = Ssh(host, 22, "", 0)
        client.set_auth(user, passwd)
        client.connect_thread()
        out = client.sendInteractiveCommand(cmd, (passwd,))
        #out = client.sendInteractiveCommand(cmd, (passwd, 'ok', 'ok', '', '', '', '', '', 'O'))
        client.close()
        
        self.assertEqual(out, user + "\n")

# Si le script est exécuté seul, cette condition est remplie
if __name__ == "__main__":
    # Lancement du test unitaire
    # Toutes les fonctions de la classe commençant par "test"
    # seront exécutées
    unittest.main()
