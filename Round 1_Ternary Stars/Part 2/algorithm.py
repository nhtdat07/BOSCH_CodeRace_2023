from hashlib import sha256
import math

# Get K0
def getK0(key):
    length = math.floor(len(key)*0.5)
    if(length == 64):
        return key
    if(length > 64):
        hash = sha256(bytes.fromhex(key))
        key = hash.hexdigest()
        for i in range(32):
            key += "00"
        return key 
    for i in range(length,64):
        key += "00"
    return key

# Xor
def xor_hex_strings(str1, str2):
    str1 = format(int(str1,16), '0>256b')
    str2 = format(int(str2,16), '0>256b')
    len_diff = abs(len(str1) - len(str2))
    if len(str1) < len(str2):
        str1 = '0' * len_diff + str1
    elif len(str2) < len(str1):
        str2 = '0' * len_diff + str2
    result = ''
    for bit1, bit2 in zip(str1, str2):
        xor_result = int(bit1) ^ int(bit2)
        result += str(xor_result)
    return result

def init_oipad(str):
    res = ""
    for i in range(64):
        res += str 
    return res

Key = "0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"
Data = "4869205468657265"

def algorithm(Key, Data):
    ipad = init_oipad("36")
    opad = init_oipad("5c")

    # Step 1,2,3
    key_zero = getK0(Key)

    # Step 4
    step4_hex = xor_hex_strings(key_zero, ipad)
    step4_result = format(int(step4_hex, 2), 'X')
    
    # Step 5
    step5_result = step4_result + Data

    # Step 6
    hash = sha256(bytes.fromhex(step5_result))
    step6_result = hash.hexdigest()

    # Step 7
    step7_hex = xor_hex_strings(key_zero, opad)
    step7_result = format(int(step7_hex, 2), 'X')

    # Step 8
    step8_result = step7_result + step6_result

    # Step 9
    hash = sha256(bytes.fromhex(step8_result))
    step9_result = hash.hexdigest()
    return step9_result

print(algorithm(Key, Data))
