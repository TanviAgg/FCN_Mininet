from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.examples.linuxrouter import LinuxRouter
from mininet.log import setLogLevel, info


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


def ip_with_subnet(ip):
    return '{}/{}'.format(ip, 24)


class Topology(Topo):
    def build(self, **_opts):
        # create router nodes
        r1 = self.addNode(router1['name'], cls=LinuxRouter, ip=None)
        r2 = self.addNode(router2['name'], cls=LinuxRouter, ip=None)
        r3 = self.addNode(router3['name'], cls=LinuxRouter, ip=None)
        r4 = self.addNode(router4['name'], cls=LinuxRouter, ip=None)

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
        # self.addLink(h2, r4,
        #              intfName1=host2['interfaces'][0]['name'],
        #              intfName2=router4['interfaces'][0]['name'],
        #              params1={'ip': ip_with_subnet(host2['interfaces'][0]['ipaddress'])},
        #              params2={'ip': ip_with_subnet(router4['interfaces'][0]['ipaddress'])})

        # # link routers
        # # r1 and r2
        # self.addLink(r1, r2,
        #              intfName1=router1['interfaces'][1]['name'],
        #              intfName2=router2['interfaces'][0]['name'],
        #              params1={'ip': ip_with_subnet(router1['interfaces'][1]['ipaddress'])},
        #              params2={'ip': ip_with_subnet(router2['interfaces'][0]['ipaddress'])})
        # # r1 and r3
        # self.addLink(r1, r3,
        #              intfName1=router1['interfaces'][2]['name'],
        #              intfName2=router3['interfaces'][0]['name'],
        #              params1={'ip': ip_with_subnet(router1['interfaces'][2]['ipaddress'])},
        #              params2={'ip': ip_with_subnet(router3['interfaces'][0]['ipaddress'])})
        # # r2 and r4
        # self.addLink(r2, r4,
        #              intfName1=router2['interfaces'][1]['name'],
        #              intfName2=router4['interfaces'][1]['name'],
        #              params1={'ip': ip_with_subnet(router2['interfaces'][1]['ipaddress'])},
        #              params2={'ip': ip_with_subnet(router4['interfaces'][1]['ipaddress'])})
        # # r3 and r4
        # self.addLink(r3, r4,
        #              intfName1=router3['interfaces'][1]['name'],
        #              intfName2=router4['interfaces'][2]['name'],
        #              params1={'ip': ip_with_subnet(router3['interfaces'][1]['ipaddress'])},
        #              params2={'ip': ip_with_subnet(router4['interfaces'][2]['ipaddress'])})


def configure_static_routes(net):
    # routes for R1: R1-R2 via R2, R1-R4 via R2 and R1-R3 via R3
    net[router1['name']].cmd("ip route add {} via {} dev {}".format(
        router2['interfaces'][1]['subnet'],
        router2['interfaces'][0]['ipaddress'],
        router1['interfaces'][1]['name']))
    net[router1['name']].cmd("ip route add {} via {} dev {}".format(
        router4['interfaces'][0]['subnet'],
        router2['interfaces'][0]['ipaddress'],
        router1['interfaces'][1]['name']))
    net[router1['name']].cmd("ip route add {} via {} dev {}".format(
        router3['interfaces'][1]['subnet'],
        router3['interfaces'][0]['ipaddress'],
        router1['interfaces'][2]['name']))

    # routes for R4: R4-R3 via R3, R4-R2 via R2 and R4-R1 via R2
    net[router4['name']].cmd("ip route add {} via {} dev {}".format(
        router3['interfaces'][0]['subnet'],
        router3['interfaces'][1]['ipaddress'],
        router4['interfaces'][2]['name']))
    net[router4['name']].cmd("ip route add {} via {} dev {}".format(
        router2['interfaces'][0]['subnet'],
        router2['interfaces'][1]['ipaddress'],
        router4['interfaces'][1]['name']))
    net[router4['name']].cmd("ip route add {} via {} dev {}".format(
        router1['interfaces'][0]['subnet'],
        router2['interfaces'][1]['ipaddress'],
        router4['interfaces'][1]['name']))

    # routes for R2: R2-H1 via R1, R2-R3 via R1, R2-R3 via R4, R2-H2 via R4
    net[router2['name']].cmd("ip route add {} via {} dev {}".format(
        router1['interfaces'][0]['subnet'],
        router1['interfaces'][1]['ipaddress'],
        router2['interfaces'][0]['name']))
    net[router2['name']].cmd("ip route add {} via {} dev {}".format(
        router1['interfaces'][2]['subnet'],
        router1['interfaces'][1]['ipaddress'],
        router2['interfaces'][0]['name']))
    net[router2['name']].cmd("ip route add {} via {} dev {}".format(
        router4['interfaces'][0]['subnet'],
        router4['interfaces'][1]['ipaddress'],
        router2['interfaces'][1]['name']))
    net[router2['name']].cmd("ip route add {} via {} dev {}".format(
        router4['interfaces'][2]['subnet'],
        router4['interfaces'][1]['ipaddress'],
        router2['interfaces'][1]['name']))

    # routes for R3: R3-H1 via R1, R3-R2 via R1, R3-R2 via R4, R3-H2 via R4
    net[router3['name']].cmd("ip route add {} via {} dev {}".format(
        router1['interfaces'][0]['subnet'],
        router1['interfaces'][2]['ipaddress'],
        router3['interfaces'][0]['name']))
    net[router3['name']].cmd("ip route add {} via {} dev {}".format(
        router1['interfaces'][1]['subnet'],
        router1['interfaces'][2]['ipaddress'],
        router3['interfaces'][0]['name']))
    net[router3['name']].cmd("ip route add {} via {} dev {}".format(
        router4['interfaces'][0]['subnet'],
        router4['interfaces'][2]['ipaddress'],
        router3['interfaces'][1]['name']))
    net[router3['name']].cmd("ip route add {} via {} dev {}".format(
        router4['interfaces'][1]['subnet'],
        router4['interfaces'][2]['ipaddress'],
        router3['interfaces'][1]['name']))


def show_routing_tables(net):
    node_names = [router1, router2, router3, router4, host1, host2]
    for node in node_names:
        info('{} {}: Routing table information\n'.format(node['type'], node['name']))
        info(net[node].cmd('route'))


def show_traceroute(net):
    # info(net[router].cmd('route'))
    pass


def ping_all(net):
    info('\nPinging all nodes and routers\n')
    info(net.pingAll())


if __name__ == "__main__":
    setLogLevel('info')

    # part A1
    info('----------PART A1-----------\n')
    my_topology = Topology()
    my_topology.build()

    # part A2
    info('----------PART A2-----------\n')
    net = Mininet(topo=my_topology)
    net.start()

    ping_all(net)

    # configure_static_routes(net)
    # show_routing_tables(net)
    # show_traceroute(net)
    #
    # ping_all(net)

    CLI(net)
    net.stop()
