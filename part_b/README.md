# Execution:
- Go to part_b directory
  - `cd part_b`
- Run `sudo python3 myRIP.py`
  - This will create the topology and run RIP on all routers. It will print all routing tables.
- To get traceroute output, run the following command from mininet
  - `> H1 traceroute H2`
  - `> H2 traceroute H1`
- To bring down the link between R1 and R2, run:
  - `mininet> link R1 R2 down`
  - Now run the command to get traceroute again (same as above).

# Output:
````
````