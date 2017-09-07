import sys

count = 1
if __name__ == "__main__":
    for i in range(0, len(sys.argv), 1):
        print ("param ", sys.argv[i])
        count = count + 2
    print "exit"
    sys.exit(0)
