# YAML scan

Finds thing in files with a given YAML rule.

This project is similar to YARA but made in Python. It can be used for finding malware in files or string in files.

## Example of rule

```yaml
meta:
    name: "Name of the rule"  
    # type: "name" # <-- Optional type of the rule (Vulnerability, Malware, etc.)
    author: "Author"
    version: "V1.0"
    description: "What the rule finds"
    date: "The date of the rule"

rules:
  - name: "Hello world!"
    description: "Finds the string 'Hello world!' in a file"
    type: "string" # <-- The type of the rule (string or regex)
    report: # <- Optional style for the report
      colour: "blue" # <-- The colour of the message when found (red, yellow, green, blue, purple, cyan, white, magenta)
      text: "FOUND:" # <-- The message when found
    if: "CONTAINS" # <-- The condition of the rule (CONTAINS, STARTS, ENDS)
    find: "Hello world!"
    
  - name: "Find number in file"
    description: "Finds a number in a file using regex"
    type: "regex"
    if: "CONTAINS"
    find: "[0-9]+" # <-- Regex to find a number in a file
```

## Usage

```bash
python3 -m YAMLscan <file_to_scan> <rule_file>
```

Or to scan files in a directory and subdirectories:

```bash
python3 -m YAMLscan - <rule_file>
```