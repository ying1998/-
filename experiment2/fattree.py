#!/usr/bin/python

"""Custom topology example
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController,CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
        L1 = 1
        L2 = 4
        c = []
        a = []


        # add core ovs
        sw = self.addSwitch( 'c{}'.format( 1 ) )
        c.append( sw )

        # add aggregation ovs
        for i in range( L2 ):
                sw = self.addSwitch( 'a{}'.format( L1 + i + 1 ) )
                a.append( sw )

        # add links between core and aggregation ovs
        for i in range( L1 ):
                sw1 = c[i]
                for sw2 in a[i/2::1]:
                # self.addLink(sw2, sw1, bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
			            self.addLink( sw2, sw1 )

        e = []
        e.append(a[0])
	e.append(a[-1])

        count = 1
        for sw1 in e:
                for i in range(2):
                	host = self.addHost( 'h{}'.format( count ) )
                	self.addLink( sw1, host )
                	count += 1
topos = { 'mytopo': ( lambda: MyTopo() ) }
