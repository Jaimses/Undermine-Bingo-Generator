import csv
import random
import json
E = 16
M = 6
H = 3
bingodict = {"name":[]}
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
                    bingodict["name"].append(row[0])
                    bingodict["name"].append(row[1])
                    bingodict["name"].append(row[2])
                    print("123")
               elif line_count in EGoals and line_count in MGoals:
                    bingodict["name"].append(row[1])
                    bingodict["name"].append(row[0])
                    print("12")
               elif line_count in HGoals and line_count in EGoals:
                    bingodict["name"].append(row[2])
                    bingodict["name"].append(row[0])
                    print("13")
               elif line_count in HGoals and line_count in MGoals:
                    bingodict["name"].append(row[1])
                    bingodict["name"].append(row[2])
                    print("23")
               elif line_count in HGoals:
                    bingodict["name"].append(row[2])
                    print("3")
               elif line_count in MGoals:
                    bingodict["name"].append(row[1])
                    print("2")
               elif line_count in EGoals:
                    bingodict["name"].append(row[1])
                    print("1")
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
