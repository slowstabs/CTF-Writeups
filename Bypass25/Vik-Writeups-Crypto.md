# BypassCTF Writeups

## Crypto

### 1. Count the steps, not the stars

Bruteforced the n values using a python script as we knew the enc value of `B` from `BYPASS_CTF{`

```
from multiprocessing import Pool, Value, cpu_count
from functools import reduce
from itertools import product, islice

TARGET = 3827591716288630776540535668038365628871133898264070018792556815246012718335698404146173574751497387952867457629767297216012860845869627771721518203820241154212224
BASE = ord("B") ** 2

CHUNK = 120000
progress = Value('i', 0)
found = Value('b', False)

def ecv(v, a, b, c):
    return reduce(lambda v, s: (v << s) ^ s, (16, a, b, c), v)

def worker(chunk):
    for a, b, c in chunk:
        if found.value:
            return None

        if ecv(BASE, a, b, c) == TARGET:
            with found.get_lock():
                found.value = True
            return (a, b, c)

    with progress.get_lock():
        progress.value += len(chunk)
        if progress.value % 100000 == 0:
            print(f"testing {progress.value:,} combos")

    return None

def chunks(iterable, size):
    it = iter(iterable)
    while True:
        block = list(islice(it, size))
        if not block:
            break
        yield block

def main():
    combos = product(range(10, 100), range(10, 100), range(100, 1000))

    with Pool(cpu_count()) as p:
        for result in p.imap_unordered(worker, chunks(combos, CHUNK)):
            if result:
                print("\n match")
                print(result)
                return

    print("\nNo match")

if __name__ == "__main__":
    main()


```
We get values as 32,96, 384

Run a decode script, get the flag (idk why it had noise)

```
from functools import reduce

def ecv(v):
    n = [16, 32, 96, 384]
    return reduce(lambda v, s: (v << s) ^ s, n, v)


enc = [the enc goes here]

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}"


lookup = {}
for ch in charset:
    lookup[ecv(ord(ch)**2)] = ch


flag = "".join(lookup.get(v, "?") for v in enc)

print(flag)

```

flag: `BYPASS_CTF{pearl_navigated_through_dark_waters_4f92b}`

---






