import os
import time
import re

def get_switches():
    return os.popen("sudo ovs-vsctl list-br").read().split()

def parse_flow(line):
    return dict(re.findall(r'(\w+)=([^, ]+)', line))

def analyze_switch(sw):
    print(f"\n===== SWITCH: {sw} =====")
    output = os.popen(f"sudo ovs-ofctl -O OpenFlow13 dump-flows {sw}").read()

    for line in output.split('\n'):
        if "n_packets" not in line:
            continue

        flow = parse_flow(line)

        packets=int(flow.get("n_packets",0))
        bytes_=int(flow.get("n_bytes",0))
        duration=flow.get("duration","0")
        actions=flow.get("actions","UNKNOWN")

        status="ACTIVE" if packets>0 else "UNUSED"

        print(f"""
Rule:
 Status   : {status}
 Packets  : {packets}
 Bytes    : {bytes_}
 Duration : {duration}
 Action   : {actions}
""")

while True:
    os.system("clear")
    print("=== FLOW TABLE ANALYZER ===")

    for sw in get_switches():
        analyze_switch(sw)

    time.sleep(5)
