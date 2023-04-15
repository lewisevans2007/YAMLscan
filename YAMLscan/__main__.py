# YAMLScan - A tool for scanning files and 
#

import os
import sys
import re
import yaml
from colorama import init, Back, Style

def scan_file(yaml,file):
    with open(file, "rb") as f:
        data = f.read()
    
    for rule in yaml["rules"]:
        if rule["type"] == "string":
            find = rule["find"].encode()
            if rule["if"] == "CONTAINS":
                if find in data:
                    print(Back.RED + "FOUND: " + Style.RESET_ALL + rule["name"] + " in " + file)
            if rule["if"] == "STARTS":
                if data.startswith(find):
                    print(Back.RED + "FOUND: " + Style.RESET_ALL + rule["name"] + " in " + file)
            if rule["if"] == "ENDS":
                if data.endswith(find):
                    print(Back.RED + "FOUND: " + Style.RESET_ALL + rule["name"] + " in " + file)
        elif rule["type"] == "regex":
            if rule["if"] == "CONTAINS":
                if re.search(rule["find"], data.decode()):
                    print(Back.RED + "FOUND: " + Style.RESET_ALL + rule["name"] + " in " + file)
            if rule["if"] == "STARTS":
                if re.search("^" + rule["find"], data.decode()):
                    print(Back.RED + "FOUND: " + Style.RESET_ALL + rule["name"] + " in " + file)
            if rule["if"] == "ENDS":
                if re.search(rule["find"] + "$", data.decode()):
                    print(Back.RED + "FOUND: " + Style.RESET_ALL + rule["name"] + " in " + file)
        else:
            print("Error: Invalid type in rule set")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 -m YAMLscan <file> <rule set>")
        sys.exit(1)
    else:
        file = sys.argv[1]
        rule_set = sys.argv[2]

    with open(rule_set, "r") as f:
        rule_set = yaml.safe_load(f)
    
    scan_file(rule_set,file)