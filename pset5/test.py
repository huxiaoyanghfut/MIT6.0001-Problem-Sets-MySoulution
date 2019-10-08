import string
import datetime
trigger_file = open('triggers.txt', 'r')
lines = []
for line in trigger_file:
    line = line.rstrip()
    if not (len(line) == 0 or line.startswith('//')):
        lines.append(line)
print(lines) # for now, print it so you see what it contains!
trigger_dict ={}
for line in lines:
    t = line.split(',')
    trigger_dict[t[2]] = t[1]
print(trigger_dict)
triggerlist = []
for key,value in trigger_dict.items():
    print(key,value.capitalize())
print(triggerlist)




