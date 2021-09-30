# use of readlines to parse each line in as a list item
# each line represents a class of data

try:
    file = open("values.txt", mode='r', encoding='utf-8')
    for index, line in enumerate(file.readlines()):
        fields = line.strip().split()
        
        for field in fields:
            print(float(field))
        

finally:
    file.close()