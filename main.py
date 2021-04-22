import csv


list_clients = {}
with open(r'test.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        if row and len(row)==2:
            row[0] = row[0].strip('"').strip(',')
            try:
                row[1] = int(row[1])
            except ValueError:
                row[1] = int(row[2])
            if row[0] not in list_clients:
                list_clients.update({row[0]: row[1]})
            elif row[0] in list_clients:
                list_clients[row[0]] += row[1]
print(list_clients)
