import os

history_path = os.path.join("lab_data", "history")
if os.path.exists(history_path):
    os.rmdir(history_path)