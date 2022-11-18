# Execution:
- Go to part_b directory
  - `cd part_b`
- Run `sudo python3 myRIP.py`
  - This will create the topology and run RIP on all routers. It will print all routing tables.
- To get traceroute output, run the following command from mininet
  - `> H1 traceroute H2`
  - `> H2 traceroute H1`
- To bring down the link between R1 and R2 (or R3), run:
  - `mininet> link R1 R2 down` (or replace R2 with R3).
  - Now run the command to get traceroute again (same as above).

# Output:
````
----------PART B1-----------
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

router R1: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        0.0.0.0         255.255.255.0   U     0      0        0 r1-interface-0
10.0.1.0        0.0.0.0         255.255.255.0   U     32     0        0 r1-interface-0
10.0.2.0        0.0.0.0         255.255.255.0   U     0      0        0 r1-interface-1
10.0.2.0        0.0.0.0         255.255.255.0   U     32     0        0 r1-interface-1
10.0.3.0        0.0.0.0         255.255.255.0   U     0      0        0 r1-interface-2
10.0.3.0        0.0.0.0         255.255.255.0   U     32     0        0 r1-interface-2
10.0.4.0        10.0.2.1        255.255.255.0   UG    32     0        0 r1-interface-1
10.0.5.0        10.0.3.1        255.255.255.0   UG    32     0        0 r1-interface-2
10.0.6.0        10.0.2.1        255.255.255.0   UG    32     0        0 r1-interface-1
router R2: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        10.0.2.2        255.255.255.0   UG    32     0        0 r2-interface-0
10.0.2.0        0.0.0.0         255.255.255.0   U     0      0        0 r2-interface-0
10.0.2.0        0.0.0.0         255.255.255.0   U     32     0        0 r2-interface-0
10.0.3.0        10.0.2.2        255.255.255.0   UG    32     0        0 r2-interface-0
10.0.4.0        0.0.0.0         255.255.255.0   U     0      0        0 r2-interface-1
10.0.4.0        0.0.0.0         255.255.255.0   U     32     0        0 r2-interface-1
10.0.5.0        10.0.4.2        255.255.255.0   UG    32     0        0 r2-interface-1
10.0.6.0        10.0.4.2        255.255.255.0   UG    32     0        0 r2-interface-1
router R3: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        10.0.3.2        255.255.255.0   UG    32     0        0 r3-interface-0
10.0.2.0        10.0.3.2        255.255.255.0   UG    32     0        0 r3-interface-0
10.0.3.0        0.0.0.0         255.255.255.0   U     0      0        0 r3-interface-0
10.0.3.0        0.0.0.0         255.255.255.0   U     32     0        0 r3-interface-0
10.0.4.0        10.0.5.2        255.255.255.0   UG    32     0        0 r3-interface-1
10.0.5.0        0.0.0.0         255.255.255.0   U     0      0        0 r3-interface-1
10.0.5.0        0.0.0.0         255.255.255.0   U     32     0        0 r3-interface-1
10.0.6.0        10.0.5.2        255.255.255.0   UG    32     0        0 r3-interface-1
router R4: Routing table information
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.1.0        10.0.4.1        255.255.255.0   UG    32     0        0 r4-interface-1
10.0.2.0        10.0.4.1        255.255.255.0   UG    32     0        0 r4-interface-1
10.0.3.0        10.0.5.1        255.255.255.0   UG    32     0        0 r4-interface-2
10.0.4.0        0.0.0.0         255.255.255.0   U     0      0        0 r4-interface-1
10.0.4.0        0.0.0.0         255.255.255.0   U     32     0        0 r4-interface-1
10.0.5.0        0.0.0.0         255.255.255.0   U     0      0        0 r4-interface-2
10.0.5.0        0.0.0.0         255.255.255.0   U     32     0        0 r4-interface-2
10.0.6.0        0.0.0.0         255.255.255.0   U     0      0        0 r4-interface-0
10.0.6.0        0.0.0.0         255.255.255.0   U     32     0        0 r4-interface-0
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
*** Starting CLI:
mininet> H1 traceroute H2
traceroute to 10.0.6.2 (10.0.6.2), 30 hops max, 60 byte packets
 1  10.0.1.1 (10.0.1.1)  0.037 ms  0.009 ms  0.007 ms
 2  10.0.3.1 (10.0.3.1)  0.019 ms  0.010 ms  0.010 ms
 3  10.0.5.2 (10.0.5.2)  0.022 ms  0.014 ms  0.012 ms
 4  10.0.6.2 (10.0.6.2)  0.024 ms  0.016 ms  0.018 ms
mininet> H2 traceroute H1
traceroute to 10.0.1.2 (10.0.1.2), 30 hops max, 60 byte packets
 1  10.0.6.1 (10.0.6.1)  0.035 ms  0.009 ms  0.009 ms
 2  10.0.5.1 (10.0.5.1)  0.019 ms  0.011 ms  0.010 ms
 3  10.0.3.2 (10.0.3.2)  0.021 ms  0.014 ms  0.013 ms
 4  10.0.1.2 (10.0.1.2)  0.031 ms  0.017 ms  0.015 ms
mininet> link R1 R3 down
mininet> H1 traceroute H2
traceroute to 10.0.6.2 (10.0.6.2), 30 hops max, 60 byte packets
 1  10.0.1.1 (10.0.1.1)  0.040 ms  0.009 ms  0.008 ms
 2  10.0.2.1 (10.0.2.1)  0.022 ms  0.011 ms  0.010 ms
 3  10.0.4.2 (10.0.4.2)  0.023 ms  0.015 ms  0.012 ms
 4  10.0.6.2 (10.0.6.2)  0.023 ms  0.016 ms  0.016 ms
mininet> H2 traceroute H1
traceroute to 10.0.1.2 (10.0.1.2), 30 hops max, 60 byte packets
 1  10.0.6.1 (10.0.6.1)  0.052 ms  0.008 ms  0.008 ms
 2  10.0.4.1 (10.0.4.1)  0.018 ms  0.010 ms  0.009 ms
 3  10.0.2.2 (10.0.2.2)  0.022 ms  0.012 ms  0.013 ms
 4  10.0.1.2 (10.0.1.2)  0.056 ms  0.017 ms  0.014 ms

````