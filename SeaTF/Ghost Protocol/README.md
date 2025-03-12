**Ghost Protocol**

300

_A series of mysterious ICMP packets have been intercepted, but their true message is hidden within the packet identifiers. Are they just noise, or do they carry a hidden signal?_

_Your task is to analyze the provided data and recover the hidden flag. The packets may be encoded in ways beyond the obvious, and you’ll need to think like a network analyst to uncover the truth._

Files: ghost_protocol_final.pcap, ghost_protocol_hint.txt

RED HERRING PARADISE.

This challenge had so many red herrings, I would lose my shit.

Going through TCP stream, you'll find 3 fake flags.
Going through the DNS, you'll come across chunks which is misleading due to the information in `ghost_protocol_hint.txt`

Where the real flag lies is in the 7th and 8th line of the hint. 

```
ICMP speaks more than it seems,
In its identity, secrets unfold.
```

It is referring to the ip id of the ICMP packets. On inspection of a few, I found that its either 100 or 500, which meant it was a binary code. Extract the ip id from the ICMP packets and replace the 100 and 500 with 0 and 1 respectively

```python
from scapy.all import rdpcap, IP, ICMP

# Load the pcap file
packets = rdpcap("ghost_protocol_final.pcap")  # Change this to your actual pcap file

# Iterate through packets and print the IP ID for ICMP packets
for pkt in packets:
    if IP in pkt and ICMP in pkt:
        print(f"{pkt[IP].id}") 
        with open("output.txt", "a") as f:
            f.write(f"{pkt[IP].id}\n")

```
(did the latter manually)

Then threw it into cyberchef and decoded the binary with byte length of 8 and found the flag.

Flag: SeaTF{n3tw0rk_f0r3ns1cs_m4st3r_0f_th3_h1dd3n_ch4nn3l}

