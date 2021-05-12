
encode = ''
decode = ''
message = input("Enter the message to be decode: ")

#Simple Decode----
for i in range(len(message)):
    to_ascii = ord(message[i]) - 7
    decode += chr(to_ascii)

print('The decoded message is: ', decode)

#Simple Encode----
to_encode = input('Paste the decoded message and press enter: ')
for i in range(len(to_encode)):
    to_ascii = ord(to_encode[i]) + 7
    if chr(to_ascii) == '↚':
        to_ascii = 32
    encode += chr(to_ascii)

print('The decoded message is: ', encode)