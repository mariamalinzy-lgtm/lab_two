import os
import shutil

notes_path = os.path.join("lab_data", "input", "notes.txt")
with open(notes_path, "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")

with open(notes_path, "r") as f:
    lines = f.readlines()
    print(len(lines))

summary_path = os.path.join("lab_data", "output", "summary.txt")
shutil.copy(notes_path, summary_path)