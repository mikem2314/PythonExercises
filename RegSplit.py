#Written to solve https://www.hackerrank.com/challenges/re-split/problem

import re

regex_pattern = r"[.,]+"	
print("\n".join(re.split(regex_pattern, input())))