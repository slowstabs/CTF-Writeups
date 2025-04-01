## Newlines

Points: 359

> Description: Some secrets hide in plain sight, while others lurk between the lines. Can you find what’s hidden in this seemingly ordinary text file?

We're given a folder which consists of a lot of text files labelled from 1 to 69. Each of them has a bunch of newlines, then finally a `#` at the end.

On inspection of a few files, we see that the amount of newlines in the files seem to be around 100 give or take, which meant ASCII. 

Then I made a script that counted new lines from each of the files and gave the number in `line_count.txt`

```python
import os

def count_lines_before_hash(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if line.strip() == "#":
                break
            count += 1
        return count

def main():
    output_file = "line_counts.txt"
    with open(output_file, "w") as out:
        for i in range(70):  # From 0 to 69
            filename = f"{i}.txt"
            if os.path.exists(filename):
                line_count = count_lines_before_hash(filename)
                out.write(f"{filename}: {line_count}\n")

if __name__ == "__main__":
    main()

```

After getting the ACSII numbers here, I converted it into text and we get our flag

Flag: `saic{s0_m4ny_n3wl1n35_b7w_7h15_15_4_v3ry_l0ng_fl4g_y0u_wr073_5cr1p7!!}`
