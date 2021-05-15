import sys

print("The length of command line arguments : ", len(sys.argv) - 1 , "The arguments are " , *(sys.argv[1:]))