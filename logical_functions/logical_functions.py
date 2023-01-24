
def inverter(a):
    return 0 if a == 1 else 1

def and_gate(a, b):
    return 1 if a == 1 and b == 1 else 0

def nand_gate(a, b):
    return 0 if a == 1 and b == 1 else 1

def or_gate(a, b):
    return 1 if a == 1 or b == 1 else 0

def nor_gate(a, b):
    return 0 if a == 1 or b == 1 else 1

def xor_gate(a, b):
    return 1 if (a == 1 or b == 1) and (b != a) else 0


# Pass the values in integer form where :
# 1 -> True
# 0 -> False

# TEST CASES
 
# print(inverter(1))          # Should print 0
# print(and_gate(1, 0))       # Should print 0
# print(nand_gate(0, 1))      # Should print 1
# print(or_gate(1, 1))        # Should print 1
# print(nor_gate(0, 0))       # Should print 1
# print(xor_gate(1, 1))       # Should print 0