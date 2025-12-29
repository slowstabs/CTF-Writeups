## BypassCTF Writeups Reverse Engineering

### 1. Dead Man's Riddle

The main logic of this was in the `consult_compass` function, where the input string is encrypted using the rolling global variable g_state. For each character, the program combined the character value and its index with part of g_state, producing a transformed byte. This transformed value was then compared against a hard-coded table in check_course(). Since the transformation was fully reversible and the expected values were stored in the binary, we could recreate the algorithm, reverse the math for each of the 30 positions, and recover the original passphrase.

script: 

```
def rol32(x, r):
    x &= 0xffffffff
    return ((x << r) | (x >> (32 - r))) & 0xffffffff

g = 0xDEADBEEF
g ^= 0x1337C0DE
g = rol32(g, 3) ^ 0x1337C0DE   # result: 0x7fe43150

vals = [
    18, 83, 60, 68, 32, 119, 168, 232, 82, 49,
    235, 147, 56, 40, 111, 103, 95, 46, 200, 222,
    116, 224, 121, 185, 72, 84, 241, 128, 203, 88
]

out = []

for pos, val in enumerate(vals):
    shift = pos % 5
    t = (g >> shift) & 0xffffffff

    c = (val ^ t) - pos
    c &= 0xff  # keep as byte

    out.append(c)

    # update g_state
    g = (31337 * g + c) & 0xffffffff

flag = bytes(out).decode()
print(flag)

```

flag: BYPASS_CTF{T1d3s_0f_D3c3pt10n}

---

### 2. Cursed Compass

The `calculate_wave_physics` was the function of interest as it had an pseudo rng gen and was XOR'ed with data from `g_tide_data`.

Reversing the algorithm, gave us the flag. 

Script:
```
g = [
0x4F,0x5D,0x21,0x4E,0x0A,0x5E,0x98,0x0D,0xFE,0xEA,
0xB2,0xB0,0xC8,0x57,0x9E,0xE8,0xB8,0x49,0x84,0x05,
0xCE,0x7E,0x49,0xEA,0xEF,0x6F,0x16,0xE3,0x8A,0x29,
0x70,0x44,0x83,0xA5,0x39,0x67
]

s = 195948557
flag = ""

for i in range(len(g)):
    # advance PRNG i times
    s = 195948557
    for _ in range(i):
        s = (1664525*s + 1013904223) & 0xffffffff

    decoded = ((s >> (i % 7)) ^ g[i]) & 0xff
    flag += chr(decoded)

print(flag)

```

flag: BYPASS_CTF{Fr4m3_By_Fr4m3_D3c3pt10n}
