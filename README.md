# Multi-Switch Flow Table Analyzer using Mininet and POX

## Problem Statement
This project implements an SDN-based Multi-Switch Flow Table Analyzer using Mininet and the POX OpenFlow controller. The objective is to analyze switch flow tables and display rule usage by retrieving flow entries, displaying rule details, identifying active versus unused rules, and updating dynamically in real time.

The project also demonstrates:
- Controller-switch interaction
- Explicit OpenFlow match-action flow rules
- Packet_in handling through controller logic
- Network behavior observation using ping and iperf
- Two test scenarios: allowed traffic and blocked traffic

---

## Setup / Execution Steps

### Prerequisites
- Ubuntu VM
- Mininet
- Open vSwitch
- Python3
- Git

### Install dependencies
```bash
sudo apt update
sudo apt install mininet openvswitch-switch git python3 -y
```

### Clone POX
```bash
git clone https://github.com/noxrepo/pox.git
```

### Start POX controller
```bash
cd pox
./pox.py forwarding.l2_learning
```

### Start Mininet topology (new terminal)
```bash
sudo mn --topo linear,3 --mac --switch ovsk --controller=remote
```

### Test connectivity
```bash
pingall
iperf h1 h2
```

### Add explicit OpenFlow rule
```bash
sh ovs-ofctl -O OpenFlow13 add-flow s1 priority=100,icmp,actions=normal
```

### Run analyzer (new terminal)
```bash
python3 analyzer.py
```

### Test blocked scenario
```bash
sh ovs-ofctl -O OpenFlow13 add-flow s1 priority=200,icmp,actions=drop
pingall
```

---

## Expected Output

### Scenario 1: Allowed / Normal
- pingall shows 0% dropped
- iperf shows successful throughput
- Analyzer displays ACTIVE flow rules
- Flow tables show n_packets increasing

Example:
```text
Status   : ACTIVE
Packets  : 15
Bytes    : 1200
Action   : NORMAL
```

### Scenario 2: Blocked / Failure
- ICMP blocked using drop rule
- pingall fails or shows packet loss
- Flow tables reflect drop rule

---

## Proof of Execution
See screenshots in /screenshots:
- pox-controller.png
- mininet-pingall.png
- iperf-result.png
- flow-table-s1.png
- analyzer-output.png
- blocked-scenario.png
- wireshark-capture.png (optional)

---

## References
1. Mininet Documentation  
2. POX Controller Documentation  
3. Open vSwitch Documentation  
4. OpenFlow Specification
