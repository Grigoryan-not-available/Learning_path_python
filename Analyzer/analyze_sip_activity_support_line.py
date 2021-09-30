from datetime import datetime, timedelta

def getIntDay(string):
    return int(str(string).split(' ')[0].split('-')[-1])

def differentTime(firstDate, secondDate):
    try:
        obj1 = datetime.strptime(firstDate, '%Y-%m-%d %H:%M:%S')
        obj2 = datetime.strptime(secondDate, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return 0
    if getIntDay(datetime.today()) - getIntDay(obj2) == 0:
        return (obj1 - obj2).total_seconds()
    else:
       return 0

def print_result(dictEmployee):
    print(datetime.today())
    for key in dictEmployee:
        print('{} \nTOTAL_time = {} | '
              'INCOMING_time = {} | '
              'OUTGOING_time = {}\n'.format(key, timedelta(seconds=dictEmployee[key][0] + dictEmployee[key][1]), timedelta(seconds=dictEmployee[key][1]), timedelta(seconds=dictEmployee[key][0])))

listStatus = ['ANSWERED', 'NO ANSWER', 'BUSY']
dictEmployee = {"776": [0, 0], "777": [0, 0], "778": [0, 0], "779": [0, 0]} #[0 = total outgoing, 0 = totalincoming]

def main(path='/var/log/asterisk/cdr-csv/Master.csv'):
    with open(path, 'r') as file:
        for line in file:
            second_column = line.split(',')[1].strip('"') # Номер сотрудника исходящего вызова
            try:
                sixth_column = line.split(',')[6].split('/')[1].split('-')[0] # Номер сотрудника который принял вызов
            except IndexError:
                sixth_column = ''
            endTime = ""
            beginTime = ""
            if second_column in dictEmployee:  ##Outgoing
                if line.split(',')[14].strip('"') == listStatus[0]:
                    endTime = line.split(',')[11].strip('"')
                    beginTime = line.split(',')[10].strip('"')
                dictEmployee[second_column][0] += differentTime(endTime, beginTime)
            elif sixth_column in dictEmployee:                            ##Incoming
                if line.split(',')[14].strip('"') == listStatus[0]:
                    endTime = line.split(',')[11].strip('"')
                    beginTime = line.split(',')[10].strip('"')
                dictEmployee[sixth_column][1] += differentTime(endTime, beginTime)
    print_result(dictEmployee)

main()
