# Execution:
- Go to part_c directory
  - `cd part_c`
- Run `sudo python3 MyIperf.py` to build the topology and configure bandwidth, delay and buffer size.
- This will open the mininet CLI. Then we have to open xterm for H1 and H2.
  - `mininet> xterm H1`
  - `mininet> xterm H2`
- Start server on H2 and connect through H1 as client.
  - `H2> iperf3 -s`
  - `H1> iperf3 -c 10.0.6.2`
- This will perform the test for buffer size specified in MyIperf.py (10kb). 
- Update the value to 5mb and 25mb for other two cases and rerun.
- To compute the RTT:
`mininet> H1 ping -c 10 H2`

# Output:
- The screenshots of results and calculations are shown in the report under root directory.
- BIRD config files are present in directories for each router under `part_c/R1`, `part_c/R2`, `part_c/R3` and `part_c/R4`.  
- JSON output files for each run are also provided under `part_c/json_results`.
