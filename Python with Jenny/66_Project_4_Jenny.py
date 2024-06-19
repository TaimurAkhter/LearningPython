# Date: 24th Dec 2023 Sunday
# Start Time: 10 : 17 PM

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position+shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the text after encryption: {cipher_text}")
    
def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position-shift_key)%26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here's the text after decryption: {plain_text}")

repeat = False
while not repeat:
    what_to_do = int(input("Type '0' for encryption, type '1' for decryption:\n"))
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if what_to_do == 0:
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == 1:
        decryption(cipher_text=text, shift_key=shift)
    again = input("Type '1' if you want to go again. Otherwise press any key.")
    if again == '1':
        repeat = False
    else:
        repeat = True
        print("Exit")

# Date: 24th Dec 2023 Sunday
# End Time: 10 : 43 PM