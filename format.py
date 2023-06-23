#!/usr/bin/env python3

import re

def format(s, pattern, replacement):
    # Capture the groups from the pattern and replace them in the replacement string
    return re.sub(pattern, replacement, s)


if __name__ == '__main__':
    with open("README_RAW.md", "r") as f:
        lines = f.readlines()
        
        patterns = [
            r"\| ([0-9]+) \|",
            r"\| (https\:\/\/github\.com.*) \|",
            r"\| (https\:\/\/.*) \|"
        ]
        
        replacements = [
            r'| <a href="https://pubmed.ncbi.nlm.nih.gov/\1/" target="_blank">\1</a> |',
            r'| <a href="\1" target="_blank">GitHub</a> |',
            r'| <a href="\1" target="_blank">Link</a> |'
        ]
        
        for j in range(len(lines)):
            for i in range(len(patterns)):
                lines[j] = format(lines[j], patterns[i], replacements[i])
            
        with open("README.md", "w") as f:
            f.write("".join(lines))
