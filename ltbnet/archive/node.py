""""PMU object definition for creating virtual PMU's at selected nodes"""

import logging

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import Intf
from mininet.cli import CLI


class Node():
    def __init__(self,params):
        self.RegNode = params['RegNode']
        self.typen = params['typen']
        self.ID = 0                         #Identifier
        self.IP = str()                     #IP
        self.coords = params['coords']      #Coordinate Location
        self.name = params['name']                      #Region+name
        self.region = params['region']
        self.switch = None               #Switch Name
        self.router_mac = None
        self.router_node = None
        self.node = None                 #Node Name
        # self.level = params['level']        #Level of switch connection
        # self.swcons = dict()                #Switch Connection (dict with key = int Val =(int level, string switch)
        self.set_ip()
        self.set_id()

    def set_ip(self):
        """Inherits router address from region or PDC, then adds IP"""
        ldigs = self.RegNode.router.split('.')
        self.IP = '.'.join((ldigs[0],ldigs[1],ldigs[2],str(len(self.RegNode.ip_list)+3)))
        # print('{} IP address is {}'.format(self.name,self.IP))

    def set_id(self):
        self.ID = self.RegNode.ID + '.' + str(len(self.RegNode.nodes[self.typen]))

        # for i, name in self.RegNode.ip_list.items():
        #     if i != IP:
        #         self.IP = i
        #         return True
        #     else:
        #         logging.error("IP {} currently in use by".format(i,name))
        #         return False

    def ip_change(self,ip,oct,num):
        """Changes chosen ip Octet to given num"""
        ldigs = ip.split('.')
        ldigs[oct] = str(num)
        self.IP = '.'.join(ldigs)