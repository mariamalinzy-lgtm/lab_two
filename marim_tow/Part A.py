import os

folder_name = "lab_data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

subfolders = ["input", "output", "logs"]
for sub in subfolders:
    path = os.path.join(folder_name, sub)
    if not os.path.exists(path):
        os.makedirs(path)

for item in os.listdir(folder_name):
    item_path = os.path.join(folder_name, item)
    if os.path.isdir(item_path):
        print(f"{item} - Directory")
    else:
        print(f"{item} - File")

old_path = os.path.join(folder_name, "logs")
new_path = os.path.join(folder_name, "history")
if os.path.exists(old_path):
    os.rename(old_path, new_path)