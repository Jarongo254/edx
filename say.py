#import cowsay
import sys

#f len(sys.argv)==2:
#    cowsay.trex("hello, " + sys.argv[1])

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])