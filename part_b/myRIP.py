from mininet.log import setLogLevel, info
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.examples.linuxrouter import LinuxRouter
from mininet.node import Node


host1 = {
    'name': 'H1',
    'interfaces': [
        {
            'ipaddress': '10.0.1.1',
            'subnet': '10.0.1.0/24',
            'name': 'h1-interface-0'
        }
    ],
    'type': 'host',
}

host2 = {
    'name': 'H2',
    'interfaces': [
        {
            'ipaddress': '10.0.6.2',
            'subnet': '10.0.6.0/24',
            'name': 'h2-interface-0'
        }
    ],
    'type': 'host',
}

router1 = {
    'name': 'R1',
    'interfaces': [
        {
            'ipaddress': '10.0.1.2',
            'subnet': '10.0.1.0/24',
            'name': 'r1-interface-0'
        },
        {
            'ipaddress': '10.0.2.1',
            'subnet': '10.0.2.0/24',
            'name': 'r1-interface-1'
        },
        {
            'ipaddress': '10.0.3.1',
            'subnet': '10.0.3.0/24',
            'name': 'r1-interface-2'
        }
    ],
    'type': 'router',
}

router2 = {
    'name': 'R2',
    'interfaces': [
        {
            'ipaddress': '10.0.2.2',
            'subnet': '10.0.2.0/24',
            'name': 'r2-interface-0'
        },
        {
            'ipaddress': '10.0.5.1',
            'subnet': '10.0.5.0/24',
            'name': 'r2-interface-1'
        }
    ],
    'type': 'router',
}

router3 = {
    'name': 'R3',
    'interfaces': [
        {
            'ipaddress': '10.0.3.2',
            'subnet': '10.0.3.0/24',
            'name': 'r3-interface-0'
        },
        {
            'ipaddress': '10.0.4.1',
            'subnet': '10.0.4.0/24',
            'name': 'r3-interface-1'
        }
    ],
    'type': 'router',
}

router4 = {
    'name': 'R4',
    'interfaces': [
        {
            'ipaddress': '10.0.6.1',
            'subnet': '10.0.6.0/24',
            'name': 'r4-interface-0'
        },
        {
            'ipaddress': '10.0.5.2',
            'subnet': '10.0.5.0/24',
            'name': 'r4-interface-1'
        },
        {
            'ipaddress': '10.0.4.2',
            'subnet': '10.0.4.0/24',
            'name': 'r4-interface-2'
        }
    ],
    'type': 'router',
}


class MyRouter(Node):
    def config(self, **params):
        # config base class
        super(MyRouter, self).config(params)
        # enable forwarding
        self.cmd('sysctl net.ipv4.ip_forward=1')
        # change directory to bird.conf
        self.cmd('cd %s' % self.name)
        # start bird process
        self.cmd('bird -l')

    def terminate(self):
        # disable forwarding
        self.cmd('sysctl net.ipv4.ip_forward=0')
        # stop bird process
        self.cmd('birdc -l down')
        # terminate
        super(MyRouter, self).terminate()


def ip_with_subnet(ip):
    return '{}/{}'.format(ip, 24)


class Topology(Topo):
    def build(self, **_opts):
        # create router nodes
        r1 = self.addNode(router1['name'], cls=MyRouter)
        r2 = self.addNode(router2['name'], cls=MyRouter)
        r3 = self.addNode(router3['name'], cls=MyRouter)
        r4 = self.addNode(router4['name'], cls=MyRouter)

        # create host nodes
        h1 = self.addHost(name=host1['name'],
                          ip=ip_with_subnet(host1['interfaces'][0]['ipaddress']),
                          defaultRoute='via {}'.format(router1['interfaces'][0]['ipaddress']))
        h2 = self.addHost(name=host2['name'],
                          ip=ip_with_subnet(host2['interfaces'][0]['ipaddress']),
                          defaultRoute='via {}'.format(router4['interfaces'][0]['ipaddress']))

        # link hosts and edge routers
        self.addLink(h1, r1,
                     intfName1=host1['interfaces'][0]['name'],
                     intfName2=router1['interfaces'][0]['name'],
                     params1={'ip': ip_with_subnet(host1['interfaces'][0]['ipaddress'])},
                     params2={'ip': ip_with_subnet(router1['interfaces'][0]['ipaddress'])})
        self.addLink(h2, r4,
                     intfName1=host2['interfaces'][0]['name'],
                     intfName2=router4['interfaces'][0]['name'],
                     params1={'ip': ip_with_subnet(host2['interfaces'][0]['ipaddress'])},
                     params2={'ip': ip_with_subnet(router4['interfaces'][0]['ipaddress'])})

        # link routers
        # r1 and r2
        self.addLink(r1, r2,
                     intfName1=router1['interfaces'][1]['name'],
                     intfName2=router2['interfaces'][0]['name'],
                     params1={'ip': ip_with_subnet(router1['interfaces'][1]['ipaddress'])},
                     params2={'ip': ip_with_subnet(router2['interfaces'][0]['ipaddress'])})
        # r1 and r3
        self.addLink(r1, r3,
                     intfName1=router1['interfaces'][2]['name'],
                     intfName2=router3['interfaces'][0]['name'],
                     params1={'ip': ip_with_subnet(router1['interfaces'][2]['ipaddress'])},
                     params2={'ip': ip_with_subnet(router3['interfaces'][0]['ipaddress'])})
        # r2 and r4
        self.addLink(r2, r4,
                     intfName1=router2['interfaces'][1]['name'],
                     intfName2=router4['interfaces'][1]['name'],
                     params1={'ip': ip_with_subnet(router2['interfaces'][1]['ipaddress'])},
                     params2={'ip': ip_with_subnet(router4['interfaces'][1]['ipaddress'])})
        # r3 and r4
        self.addLink(r3, r4,
                     intfName1=router3['interfaces'][1]['name'],
                     intfName2=router4['interfaces'][2]['name'],
                     params1={'ip': ip_with_subnet(router3['interfaces'][1]['ipaddress'])},
                     params2={'ip': ip_with_subnet(router4['interfaces'][2]['ipaddress'])})


def show_routing_tables(net):
    node_names = [router1, router2, router3, router4, host1, host2]
    for node in node_names:
        info('{} {}: Routing table information\n'.format(node['type'], node['name']))
        info(net[node['name']].cmd('route'))


def ping_all(net):
    info('\nCheck connectivity between all nodes\n')
    info(net.pingAll())


if __name__ == "__main__":
    setLogLevel('info')

    # part B1
    info('----------PART B1-----------\n')
    my_topology = Topology()

    net = Mininet(topo=my_topology)
    net.start()
    show_routing_tables(net)

    ping_all(net)

    CLI(net)
    net.stop()
