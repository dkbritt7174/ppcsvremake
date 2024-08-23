# !/usr/bin/python

"""
    Prime Number Finder
"""

import sys
import time
import pyprimesieve



print('\nUsage: python ppcsv.py (N) where N is the upper limit')
print('\nFor Example python ppcsv.py 10000\nPrimes found in primelist.txt\n','\n')



def main():
    """
    Usage: python ppcsv.py (N) where N is the upper limit.
    For Example python ppcsv.py 10000   Primes found in primelist.csv
    """


try:
    LIMIT_MAX = sys.argv[1]
except IndexError:
    print(main.__doc__)

LIMIT_MAX = sys.argv[1]
csvprime_list = [pyprimesieve.primes(int(LIMIT_MAX))]
start_time = time.perf_counter()

# If you wish to print to screen, uncomment next line.
# print(csvprime_list)

with open('primelist.txt', 'w', encoding='utf8') as fp:
    for item in csvprime_list:
        fp.write(str(item))
        
print(len(item),' Primes found')

run_time = (time.perf_counter() - start_time) * 1000
if run_time < 1000:
    print("\n", run_time, " milliseconds")
else:
    print("\n", run_time / 1000, " seconds")

if __name__ == "__main__":
    main()
