import csv
import random
import json
E = 16
M = 6
H = 3
bingodict = {}
with open('UMGoals.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    csv_lines = sum(1 for line in csv_reader)
    print(csv_lines)
    csv_file.close()

Egoal = random.sample(range(1,csv_lines+1), E)
EGoals = set(Egoal)
Mgoal = random.sample(range(1,csv_lines+1), M)
MGoals = set(Mgoal)
Hgoal = random.sample(range(1,csv_lines+1), H)
HGoals = set(Hgoal)
     
with open('UMGoals.csv') as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     line_count = 0
     for row in csv_reader:
          if line_count == 0:
               line_count += 1
               print("oh no")
          else:
               if line_count in EGoals and line_count in MGoals and line_count in HGoals:
                    bingodict["name"+str(line_count)+"EMH"] = (row[0])
                    bingodict["name"+str(line_count)+"MEH"] = (row[1])
                    bingodict["name"+str(line_count)+"HEM"] = (row[2])
                    print("EMH")
               elif line_count in EGoals and line_count in MGoals:
                    bingodict["name"+str(line_count)+"ME"] = (row[1])
                    bingodict["name"+str(line_count)+"EM"] = (row[0])
                    print("EM")
               elif line_count in HGoals and line_count in EGoals:
                    bingodict["name"+str(line_count)+"HE"] = (row[2])
                    bingodict["name"+str(line_count)+"EH"] = (row[0])
                    print("EH")
               elif line_count in HGoals and line_count in MGoals:
                    bingodict["name"+str(line_count)+"MH"] = (row[1])
                    bingodict["name"+str(line_count)+"HM"] = (row[2])
                    print("MH")
               elif line_count in HGoals:
                    bingodict["name"+str(line_count)+"H"] = (row[2])
                    print("H")
               elif line_count in MGoals:
                    bingodict["name"+str(line_count)+"M"] = (row[1])
                    print("M")
               elif line_count in EGoals:
                    bingodict["name"+str(line_count)+"E"] = (row[0])
                    print("E")
               else:
                    print(line_count)
               line_count += 1
               print(line_count)
        
print(bingodict)        
print(EGoals)
print(MGoals)
print(HGoals)

print(f'Goals Selected!')

data = open('UMbingo.json', 'w')
with data as outfile:
     json.dump(bingodict, outfile,indent=2)
data.close()
