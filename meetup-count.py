import csv

with open("member.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)   
    header = next(reader)   # skip first row
    
    # Count Number of Stundents and Times They Attended
    # Dictionary created named count to hold stundent number: times attended 
    count={}
    location_city={}
    location_state={}
    
    for row in reader:
        value = row[10]

        #Count Students
        if value in count:
            count[value]+= 1
        else:
            count[value] = 1

        # If Attendance of a Student is over 1 find City and State
        if int(row[10]) >= 1:
            value = row[3]
            value = value.split(',')
            city = value[0]
            try:
                state = value[1]
            except:
                pass
            if city in location_city:
                location_city[city]+=1
            else:
                location_city[city]=1

            if state in location_state:
                location_state[state]+=1
            else:
                location_state[state]=1
      
    # Print In Columns of Attendance
    # Find Total number of student sessions
    i=0
    total=0
    print('Students\tCount' )
    while i <= len(count):
        for key, value in count.items():
            if int(key) == i:
                print(f'{key}\t\t{value}')
                if int(key) != 0 and int(key) != len(count):
                    total+=value * int(key)
        i+=1
    print(f'Total Sessions Delivered: {total}\n')

    #Sort City and State Dictionaries Based on Count
    location_city = dict(sorted(location_city.items(), key=lambda item: item[1], reverse=True))
    location_state = dict(sorted(location_state.items(), key=lambda item: item[1], reverse=True))

    #Print City and State Counts
    print('City\t\t\tCount')
    for key, value in location_city.items():
        if len(key) < 8:
            print(f'{key}\t\t\t{value}')
        else:
            print(f'{key}\t\t{value}')

    print(f'Total Cities: {len(location_city)}\n')

    print('State\tCount')
    for key, value in location_state.items():
        print(f'{key}\t{value}')
    print(f'Total States: {len(location_state)}\n')