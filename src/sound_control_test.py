#!/usr/bin/python3
import sys
import os
import io
import subprocess
from espeakng import ESpeakNG

# TODO shortened mapping to commands
# TODO reject malformed lines
# TODO reject low confidence reads

def main():
    esng = ESpeakNG()
    esng.voice ='german'
    esng.say('startup complete')

    #tmux_pre = ['tmux', 'new', 'd']
    tmux_pre = 'tmux new -d '
    while(1):
        try:
            try:
                #in_str = str(sys.stdin.readline()).rstrip()
                in_str = sys.stdin.readline()
                if(not in_str.isascii):
                    continue
                print("type is " + str(type(in_str)))
            except Exception as e:
                print("ERR: Mangled input")
                print(e)
                continue

            #in_str = in_str.rstrip().split(' ')
            in_str = in_str.rstrip()
            print(type(in_str))
            print("INTPUT IS: " + str(tmux_pre + in_str))

            try:
                ret_val = subprocess.call(tmux_pre + in_str, shell=True)
                #ret_val = subprocess.Popen(tmux_pre + in_str, shell=True)
                #ret_val = subprocess.popen(in_str,
               # esng.say("running command" + in_str)
            except Exception as e:
                print("ERR running command")
                print(e)
                #esng.say("error running command")
                continue
        except KeyboardInterrupt:
            esng.say("goodbye")
            sys.exit()
        except Exception as E:
            print(E)
            print("Error parsing input")
            sys.stdin.readline()
           # esng.say("error parsing input")
    return

if __name__ == "__main__":
    main()
