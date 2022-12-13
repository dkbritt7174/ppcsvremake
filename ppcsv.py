# !/usr/bin/python
# - * -coding: utf - 8 - * -

import sys
import csv
import time
from pyprimesieve import primes

__copyright__ = "Copyright (C) 10-28-2018 David Kevin Britt"
__license__ = "GPL 3.1"
__version__ = "1.1.1"
__maintainer__ = "David Kevin Britt"
__email__ = "dkbritt64118@gmail.com"
__status__ = "Production"


#    This program is free software and can be edited and modified.
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


def main():
    """
    Usage: python ppcsv.py (N) where N is the upper limit.
    For Example python ppcsv.py 10000   Primes found in primelist.csv
    """


try:
    limit_max = sys.argv[1]
except IndexError:
    print(main.__doc__)

limit_max = sys.argv[1]
csvprime_list = [primes(int(limit_max))]
start_time = time.perf_counter()

# If you wish to print to screen, uncomment next line.
# print(csvprime_list)

with open("primelist.csv", "w", 1000000000) as file_iter:
    writer = csv.writer(file_iter)
    writer.writerows(csvprime_list)
run_time = (time.perf_counter() - start_time) * 1000
if run_time < 1000:
    print("\n", run_time, " milliseconds")
else:
    print("\n", run_time / 1000, " seconds")
SystemExit()

if __name__ == "__main__":
    main()
