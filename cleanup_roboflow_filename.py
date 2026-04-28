import os
import re
from tqdm import tqdm

folder = "dataset"

for root, _, files in os.walk(folder):
    for filename in tqdm(files, desc=root):
        new_name = re.sub(r"\.rf\.[^.]+", "", filename)

        if new_name != filename:
            os.rename(
                os.path.join(root, filename),
                os.path.join(root, new_name)
            )

print("Done!")