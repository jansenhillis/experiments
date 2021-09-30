value = "206"
# value = str(value)

value = int(value, 8)
print (f"value: {value} {type(value)}")

value = '{:08b}'.format(value)
print (f"bin: {value} {type(value)}")

value = value[::-1]
print(f"reversed: {value} {type(value)}")
