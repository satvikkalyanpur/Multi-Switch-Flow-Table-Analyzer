# Computer Networks SDN Mini-Net Orange Problem 

#### Name: Satvik Kalyanpur
#### SRN: PES1UG24CS617
#### Section: K

## Problem Statement

Question Number 8: Multi-Switch Flow Table Analyzer
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

## Steps for Demonstration

1. ./pox.py forwarding.l2_learning (T1 - /CNMN/pox)
2. sudo mn --topo linear,3 --mac --switch ovsk --controller=remote (T2 - /CNMN)
3. pingall
4. iperf h1 h2
5. python3 analyzer.py (T3 - /CNMN)
6. sh ovs-ofctl -O OpenFlow13 add-flow s1 priority=200,icmp,actions=drop
7. pingall

---

## Proof of Execution - Screenshots

<img width="1280" height="800" alt="1" src="https://github.com/user-attachments/assets/f8ecb592-5665-459b-83f6-b12ea987ffc5" />
<img width="1280" height="800" alt="2" src="https://github.com/user-attachments/assets/3794dd3b-bca9-4256-b2ad-51b35f68ecf3" />
<img width="1280" height="800" alt="3" src="https://github.com/user-attachments/assets/51db52ac-925c-4ce6-984e-cece9e01278e" />
<img width="1280" height="800" alt="4" src="https://github.com/user-attachments/assets/2df28778-ed4e-49f8-8787-078f968332be" />

---

## References
1. Mininet Documentation  
2. POX Controller Documentation  
3. Open vSwitch Documentation  
4. OpenFlow Specification
