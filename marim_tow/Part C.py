import pyfiglet
import os

result = pyfiglet.figlet_format("MARIM")
output_path = os.path.join("lab_data", "output", "ascii_art.txt")

with open(output_path, "w") as f:
    f.write(result)
