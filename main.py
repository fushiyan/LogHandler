# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import re


def print_hi(name):
    file = open('iptables.log', 'r')
    Lines = file.readlines()

    for line in Lines:
        print("{0:30} {1}".format("OS Family", 'centos kernel'))
        SPT = ""
        if(re.search('SPT=(.+?) ', line) != None):
            SPT = re.search('SPT=(.+?) ', line).group(1)

        print("{0:30} {1}".format("Source Port",SPT))
        DPT = ""
        if (re.search('DPT=(.+?) ', line) != None):
           DPT = re.search('DPT=(.+?) ', line).group(1)
        print("{0:30} {1}".format("Destination Port", DPT))

        SRC = re.search('SRC=(.+?) ', line).group(1)
        print("{0:30} {1}".format("Source IP", SRC))
        DST = re.search('DST=(.+?) ', line).group(1)
        print("{0:30} {1}".format("Destination Port", DST))

        ACTION = re.search('centos kernel: (.+?):', line).group(1)
        print("{0:30} {1}".format("Action", ACTION ))
        PROTO = re.search('PROTO=(.+?) ', line).group(1)
        print("{0:30} {1}".format("Protocol", PROTO))

        print("{0:30}".format("----------------------------------------------"))
    # OS Family
    # Source Port
    # Destination Port
    # Source IP
    # Destination IP
    # Action
    # Protocol


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
