# Python 3 Datatypes

# 1. Numeric
#   1a. int
#   1b. float
#   1c. complex
# 2. Sequence
#   2a. tuple
#   2b. list
#   2c. string
# 3. boolean
# 4. set
# 5. dict
# 6. bytes
# 7. bytearray
# 8. frozenset

### Numerics ###
print("NUMERICS")
print(1, "is a", type(1), "with id", id(1))
value = -1
print(value, "is a", type(value), "with id", id(value))

# "Unlimited" precision: based on available memory
value = 324987435928543927834598734598739784587345987345345345
print(value, "is a ", type(value), "with id:", id(value))

# Binary
value = 0b111010
print(bin(value), value, "is a", type(value), "with id:", id(value))

# Octal
value = 0o12
print(oct(value), value, "is a", type(value), "with id:", id(value))

# Hexadecimal
value = 0x10c
print(hex(value), value, "is a", type(value), "with id:", id(value))

print("\nSCIENTIFIC NOTATION - 64bit precision")
value = 1e2
value2 = 1.1e2
value3 = 1.79e308
value4 = 1.80e308
value5 = 5e-324
value6 = 2e-324
print(value, "is a", type(value), "with id:", id(value))
print(value2, "is a", type(value2), "with id:", id(value2))
print(value3, "is a", type(value3), "with id:", id(value3))
print(value4, "is a", type(value4), "with id:", id(value4))
print(value5, "is a", type(value5), "with id:", id(value5))
print(value6, "is a", type(value6), "with id:", id(value6))

print("\nCOMPLEX NUMBERS")
value = 1 + 2j
value2 = 2j
print(value, "is a", type(value), "with id:", id(value))
print(value2, "is a", type(value2), "with id:", id(value2))

print("\nSEQUENCE TYPES")
print("STRING - MUTABLE, ORDERED")
value = "hello"
value2 = 'hi'
value3 = '''hi
multiline'''
print(value, "is a", type(value), "with id:", id(value))
print(value2, "is a", type(value2), "with id:", id(value2))
print(value3, "is a", type(value3), "with id:", id(value3))

print(value[1])
print(value3[3:8])
print(value[-2:])

total = 0
for ch in value:
    total += 1
print("Sequence loop total", total)

print("\nLIST - MUTABLE, ORDERED")
list1 = [1, "hello", 2+3j, 0x10c]
print(list1, "is a", type(list1), "with id:", id(list1))
print(list1[1], "is a", type(list1[1]), "with id:", id(list1[1]))
print(list1[1:3], "is a", type(list1[1:3]), "with id:", id(list1[1:3]))

print("\nTUPLE - IMMUTABLE, ORDERED")
tuple1 = (1, "hello", 2+3j, 0x10c)
tuple2 = (1,)
print(tuple1, "is a", type(tuple1), "with id:", id(tuple1))
print(tuple2, "is a", type(tuple2), "with id:", id(tuple2))
print(tuple1[1], "is a", type(tuple1[1]), "with id:", id(tuple1[1]))
print(tuple1[1:3], "is a", type(tuple1[1:3]), "with id:", id(tuple1[1:3]))

print("\nBOOL - IMMUTABLE")
b = True
b1 = False
b2 = True == 1
b3 = False == 0
print(b, "is a", type(b), "with id:", id(b))
print(b1, "is a", type(b1), "with id:", id(b1))
print(b2, "is a", type(b2), "with id:", id(b2))
print(b3, "is a", type(b3), "with id:", id(b3))

print("\nSET - MUTABLE, UNORDERED")
s = {1, 3, 5, 7, 7, 7}
print(s, "is a", type(s), "with id:", id(s))
print("Set is NOT subscriptable! s[1], s[1:3]")

print("\nDICT - MUTABLE, ORDERED")
d = {"hello": 1.0, True: 2+3j, 0x10c:'a'}
print(d, "is a", type(d), "with id:", id(d))
print(d["hello"], "is a", type(d["hello"]), "with id:", id(d["hello"]))

print("\nCONSTRUCTORS")
print("str(value)")
print("int(value)")
print("float(value)")
print("complex(value)")
print("list((value, value))")
print("tuple((value, value))")
print("bool(value)")
print("set((value, value))")
print("dict((key=value, key=value))")
