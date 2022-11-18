# Execution:
- Go to part_a directory
  - `cd part_a`
- Run `sudo python3 MyTopo.py`
  - This will create the topology, configure static routing tables and print all routing tables. 
- To get traceroute output, run the following command from mininet
  - `> H1 traceroute H2`
  - `> H2 traceroute H1`

# Output:
````
----------PART A1-----------
*** Creating network
*** Adding controller
*** Adding hosts:
H1 H2 R1 R2 R3 R4 
*** Adding switches:

*** Adding links:
(H1, R1) (H2, R4) (R1, R2) (R1, R3) (R2, R4) (R3, R4) 
*** Configuring hosts
H1 H2 R1 R2 R3 R4 
*** Starting controller
c0 
*** Starting 0 switches

----------PART A2-----------
router R1: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        0.0.0.0         255.255.255.0   U     0      0        0 r1-interface-0
10.0.2.0        0.0.0.0         255.255.255.0   U     0      0        0 r1-interface-1
10.0.3.0        0.0.0.0         255.255.255.0   U     0      0        0 r1-interface-2
10.0.4.0        10.0.2.1        255.255.255.0   UG    0      0        0 r1-interface-1
10.0.5.0        10.0.3.1        255.255.255.0   UG    0      0        0 r1-interface-2
10.0.6.0        10.0.2.1        255.255.255.0   UG    0      0        0 r1-interface-1
router R2: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        10.0.2.2        255.255.255.0   UG    0      0        0 r2-interface-0
10.0.2.0        0.0.0.0         255.255.255.0   U     0      0        0 r2-interface-0
10.0.3.0        10.0.2.2        255.255.255.0   UG    0      0        0 r2-interface-0
10.0.4.0        0.0.0.0         255.255.255.0   U     0      0        0 r2-interface-1
10.0.5.0        10.0.4.2        255.255.255.0   UG    0      0        0 r2-interface-1
10.0.6.0        10.0.4.2        255.255.255.0   UG    0      0        0 r2-interface-1
router R3: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        10.0.3.2        255.255.255.0   UG    0      0        0 r3-interface-0
10.0.2.0        10.0.3.2        255.255.255.0   UG    0      0        0 r3-interface-0
10.0.3.0        0.0.0.0         255.255.255.0   U     0      0        0 r3-interface-0
10.0.4.0        10.0.5.2        255.255.255.0   UG    0      0        0 r3-interface-1
10.0.5.0        0.0.0.0         255.255.255.0   U     0      0        0 r3-interface-1
10.0.6.0        10.0.5.2        255.255.255.0   UG    0      0        0 r3-interface-1
router R4: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        10.0.4.1        255.255.255.0   UG    0      0        0 r4-interface-1
10.0.2.0        10.0.4.1        255.255.255.0   UG    0      0        0 r4-interface-1
10.0.3.0        10.0.5.1        255.255.255.0   UG    0      0        0 r4-interface-2
10.0.4.0        0.0.0.0         255.255.255.0   U     0      0        0 r4-interface-1
10.0.5.0        0.0.0.0         255.255.255.0   U     0      0        0 r4-interface-2
10.0.6.0        0.0.0.0         255.255.255.0   U     0      0        0 r4-interface-0
host H1: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         10.0.1.1        0.0.0.0         UG    0      0        0 h1-interface-0
10.0.1.0        0.0.0.0         255.255.255.0   U     0      0        0 h1-interface-0
host H2: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         10.0.6.1        0.0.0.0         UG    0      0        0 h2-interface-0
10.0.6.0        0.0.0.0         255.255.255.0   U     0      0        0 h2-interface-0

Check connectivity between all nodes
*** Ping: testing ping reachability
H1 -> H2 R1 R2 R3 R4 
H2 -> H1 R1 R2 R3 R4 
R1 -> H1 H2 R2 R3 R4 
R2 -> H1 H2 R1 R3 R4 
R3 -> H1 H2 R1 R2 R4 
R4 -> H1 H2 R1 R2 R3 
*** Results: 0% dropped (30/30 received)
0.0*** Starting CLI:
mininet> H1 traceroute H2
traceroute to 10.0.6.2 (10.0.6.2), 30 hops max, 60 byte packets
 1  10.0.1.1 (10.0.1.1)  0.035 ms  0.008 ms  0.007 ms
 2  10.0.2.1 (10.0.2.1)  0.018 ms  0.010 ms  0.010 ms
 3  10.0.4.2 (10.0.4.2)  0.022 ms  0.013 ms  0.012 ms
 4  10.0.6.2 (10.0.6.2)  0.023 ms  0.017 ms  0.015 ms
mininet> H2 traceroute H1
traceroute to 10.0.1.2 (10.0.1.2), 30 hops max, 60 byte packets
 1  10.0.6.1 (10.0.6.1)  0.043 ms  0.009 ms  0.007 ms
 2  10.0.4.1 (10.0.4.1)  0.023 ms  0.012 ms  0.011 ms
 3  10.0.2.2 (10.0.2.2)  0.021 ms  0.012 ms  0.012 ms
 4  10.0.1.2 (10.0.1.2)  0.022 ms  0.015 ms  0.015 ms
````