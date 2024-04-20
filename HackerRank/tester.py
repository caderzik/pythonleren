import math
import os
import random
import re
import sys

nw = "Not Weird"
w = "Weird"
n = int(input("Nene eine Zahl:"))

if n % 2 == 0:
    if 2 <= n <= 5:
        print(nw)
    elif 6 <= n <= 20:
        print(w)
    elif n >= 20:
        print(nw)
            
else:
    print(w)