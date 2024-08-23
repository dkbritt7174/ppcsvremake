# !/usr/bin/python

"""    Prime Number Finder list in file primelist.txt
"""

import sys
import time
import pyprimesieve


<<<<<<< HEAD

print('\nUsage: python ppcsv.py (N) where N is the upper limit')
print('\nFor Example python ppcsv.py 10000\nPrimes found in primelist.txt\n','\n')
=======
__copyright__ = "Copyright (C) 9-7-2023 David Kevin Britt"
__license__ = "GPL 3.1"
__version__ = "2.0"
__maintainer__ = "David Kevin Britt"
__email__ = "dkbritt7174@gmail.com"
__status__ = "Production"
>>>>>>> 5fcc692ed9567c3c737cccae36fc56ef9c84d109


def main():
    """     Usage: python ppcsv.py (N) where N is the upper limit.
            For Example python ppcsv.py 10000   Primes found in primelist.csv
    """

LIMIT_MAX = sys.argv[1]
txtPrimelist = [pyprimesieve.primes(int(LIMIT_MAX))]
start_time = time.perf_counter()

# If you wish to print to screen, uncomment next line.
# print(csvprime_list)

with open('primelist.txt', 'w', encoding='utf8') as fp:
    for item in txtPrimelist:
        fp.write(str(item))

print(len(item), ' primes found.\n')

run_time = (time.perf_counter() - start_time) * 1000
if run_time < 1000:
    print("\n", run_time, " milliseconds")

else:
    print("\n", run_time / 1000, " seconds")

if __name__ == "__main__":
    main()
