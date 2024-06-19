# Date: 20th Dec 2023 Wednesday
# Time: 12 : 02 PM
# Watch  Time: 07 : 52 PM
# Start  Time: 08 : 01 PM
# End Time : 10 : 54 PM ---------- Not Include digits
# End: ---------Time: 12 : 29 PM Date: 21th Dec 2023 Thursday-------- Include digits 0 to 9
# ----------------------------Project 4 Caesar Cipher ----------------------

# Encrypt = (X+shift)mod52
# Decrypt = (X-shift)mod52
# --------------------------52 letters 10 digits 32 symbols and 1 space total 95----------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
            '0', '1', ' ', ',', '2', '.', '+', '3', '-', '*', '4', '/', '~', '!', '@', '#',
           '5', '$', '%', '6', '^', '&', '7', '<', '>', '8', '_', '9', '=', '?', ':', ';', '"',
            "'", '`', '\\', '|', '}', '{', ']', '[', ')', '(']

repeat = False
while not repeat:
    # ------------------User inputs------------
    convert = int(input("Type '0' for encryption, type '1' for decryption:\n"))
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    # -----------Empty strings and lists-----------
    cipher_text = ""
    plain_text = ""
    encrypted_list = []
    decrypted_list = []

    for i in message:
        if convert == 0:
            index = letters.index(i)
            encrypt = (index+shift)%95
            encrypted_text = letters[encrypt]
            # print(encrypt)
            encrypted_list.append(encrypted_text)
            cipher_text += encrypted_text

        elif convert == 1:
            index = letters.index(i)
            decrypt = (index-shift)%95
            decrypted_text = letters[decrypt]
            # print(decrypt)
            decrypted_list.append(decrypted_text)
            plain_text += decrypted_text
        else:
            print("Invalid!")
    if convert == 0:
        print(f"Here's the encrypted result: {cipher_text}")
    else:
        print(f"Here's the decrypted result: {plain_text}")
    
    again = input("Type '0' if you want to go again. Otherwise press any key.")
    if again == '0':
        repeat = False
    else:
        repeat = True
        print("Exit")
        

# Time: 09 : 52 PM I remove space problem and it works fine