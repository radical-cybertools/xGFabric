# Usage python deleteme.py 3.8 0 0 --file angled_test_fixing


import os
import sys
from argparse import ArgumentParser



def update_by_val(vx, vy, vz, core_folder_path):
    if not os.path.exists(core_folder_path):
        raise Exception(f"Provided path '{core_folder_path}' does not exist")
    if not os.path.exists(os.path.join(core_folder_path, "0", "U")):
        raise Exception(f"Provided path '{core_folder_path}' does not contain U file")
    with open(os.path.join(core_folder_path, "0", "U"), "rt") as f:
        text = f.read()
    inlet_loc = text.find("inlet")
    if inlet_loc == -1:
        raise Exception("No inlet found")
    uniform_loc = text.find("uniform", inlet_loc)
    if uniform_loc == -1:
        raise Exception("No uniform found")
    start = text.find("(", uniform_loc)
    end = text.find(")", uniform_loc)
    if start == -1 or end == -1:
        raise Exception("No brackets found")
    start += 1
    text = text[:start] + f"{vx} {vy} {vz}" + text[end:]
    with open(os.path.join(core_folder_path, "0", "U"), "wt") as f:
        f.write(text)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("vx", type=float, help="X component of velocity")
    parser.add_argument("vy", type=float, help="Y component of velocity")
    parser.add_argument("vz", type=float, help="Z component of velocity")
    
    parser.add_argument("-f", "--file", dest="filename",
                        help="write report to FILE", metavar="FILE")
    
    args = parser.parse_args()
    update_by_val(args.vx, args.vy, args.vz, args.filename)

