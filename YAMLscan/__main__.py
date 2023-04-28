# YAMLScan
# Finds thing in files with a given YAML rule.
# Github: https//www.github.com/awesomelewis2007/YAMLscan
# Licence: GPL-3.0
# By: Lewis Evans

import os
import sys
import re
import yaml
from colorama import init, Back, Style


def info(rule_set):
    try:
        print("Rule name:\t\t" + rule_set["meta"]["name"])
    except KeyError:
        pass
    try:
        print("Rule author:\t\t" + rule_set["meta"]["author"])
    except KeyError:
        pass
    try:
        print("Rule description:\t" + rule_set["meta"]["description"])
    except KeyError:
        pass
    try:
        print("Rule version:\t\t" + rule_set["meta"]["version"])
    except KeyError:
        pass
    try:
        print("Rule license:\t\t" + rule_set["meta"]["license"])
    except KeyError:
        pass
    try:
        print("Rule date:\t\t" + rule_set["meta"]["date"])
    except KeyError:
        pass
    try:
        print("Rule references:\t" + rule_set["meta"]["references"])
    except KeyError:
        pass
    try:
        print("Rule tags:\t\t" + rule_set["meta"]["tags"])
    except KeyError:
        pass
    try:
        print("Rule type:\t\t" + rule_set["meta"]["type"])
    except KeyError:
        pass
    try:
        print("Rule severity:\t\t" + rule_set["meta"]["severity"])
    except KeyError:
        pass
    rule_count = 0
    for rule in rule_set["rules"]:
        rule_count += 1
    print("Rule count:\t\t" + str(rule_count))


def report_findings(yaml, rule, file, line_number):
    """
    Report findings to the user
    Opens the rule file and then prints the description and the line number
    yaml: The rule file
    rule_number: The rule number
    file: The file that was scanned
    line_number: The line number that was found
    """
    if "report" in rule:
        if rule["report"]["colour"] == "red":
            print(
                Back.RED
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
        elif rule["report"]["colour"] == "green":
            print(
                Back.GREEN
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
        elif rule["report"]["colour"] == "yellow":
            print(
                Back.YELLOW
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
        elif rule["report"]["colour"] == "blue":
            print(
                Back.BLUE
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
        elif rule["report"]["colour"] == "magenta":
            print(
                Back.MAGENTA
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
        elif rule["report"]["colour"] == "cyan":
            print(
                Back.CYAN
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
        elif rule["report"]["colour"] == "white":
            print(
                Back.WHITE
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
        else:
            print(
                Back.RED
                + rule["report"]["text"]
                + Style.RESET_ALL
                + " "
                + rule["name"]
                + " in "
                + file
                + ":"
                + str(line_number)
            )
    else:
        print(
            Back.RED
            + "FOUND:"
            + Style.RESET_ALL
            + " "
            + rule["name"]
            + " in "
            + file
            + ":"
            + str(line_number)
        )


def scan_file(yaml, file):
    print("========== [" + file + "] ==========")

    with open(file, "rb") as f:
        data = f.read()

    for rule in yaml["rules"]:
        if rule["type"] == "string":
            if rule["if"].upper() == "CONTAINS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if rule["find"].encode() in line:
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )

            if rule["if"].upper() == "STARTS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if line.startswith(rule["find"].encode()):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )

            if rule["if"].upper() == "ENDS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if line.endswith(rule["find"].encode()):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )

        elif rule["type"] == "regex":
            if rule["if"].upper() == "CONTAINS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if re.search(rule["find"], line.decode()):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )

            if rule["if"].upper() == "STARTS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if re.search("^" + rule["find"], line.decode()):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )

            if rule["if"].upper() == "ENDS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if re.search(rule["find"] + "$", line.decode()):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )

        elif rule["type"] == "bytes":
            if rule["if"].upper() == "CONTAINS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if (
                            bytes.fromhex(
                                rule["find"]
                                .replace(" ", "")
                                .replace(",", "")
                                .replace("0x", "")
                            )
                            in line
                        ):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )
            if rule["if"].upper() == "STARTS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if line.startswith(
                            bytes.fromhex(
                                rule["find"]
                                .replace(" ", "")
                                .replace(",", "")
                                .replace("0x", "")
                            )
                        ):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )
            if rule["if"].upper() == "ENDS":
                try:
                    for line_number, line in enumerate(data.splitlines()):
                        if line.endswith(
                            bytes.fromhex(
                                rule["find"]
                                .replace(" ", "")
                                .replace(",", "")
                                .replace("0x", "")
                            )
                        ):
                            report_findings(yaml, rule, file, line_number + 1)
                except UnicodeDecodeError:
                    print(
                        Back.RED
                        + "ERROR:"
                        + Style.RESET_ALL
                        + " "
                        + rule["name"]
                        + " in "
                        + file
                        + ":"
                        + str(line_number + 1)
                        + " (UnicodeDecodeError)"
                    )
        else:
            print("Error: Invalid type in rule set")
            sys.exit(1)


if __name__ == "__main__":
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("Usage:\tpython3 -m YAMLscan <file> <rule set>")
        print("\tpython3 -m YAMLscan --info <rule set>")
        print("\tpython3 -m YAMLscan - <rule set>")
        print("\tpython3 -m YAMLscan --help")
        print("\tpython3 -m YAMLscan -h")
        sys.exit(0)

    if len(sys.argv) < 3:
        print("Usage: python3 -m YAMLscan <file> <rule set>")
        sys.exit(1)

    else:
        file = sys.argv[1]
        rule_set = sys.argv[2]

    with open(rule_set, "r") as f:
        rule_set = yaml.safe_load(f)

    if file == "-":
        for root, dirs, files in os.walk("."):
            for file in files:
                scan_file(rule_set, root + "/" + file)
    if file == "--info":
        info(rule_set)

    else:
        scan_file(rule_set, file)
