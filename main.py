import os

output_dir = "/output"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w") as f:
    f.write("7")