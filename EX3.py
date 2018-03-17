import string
alphabet = ' ' + string.ascii_lowercase
j = dict(enumerate(alphabet))
positions = {v: k for k, v in j.items()}
message = "hi my name is caesar"

n = []
z = []
for j in range(len(message)):
    for v,k in positions.items():
        if v == message[j]:
            z = k+1%27
            
            for v,k in positions.items():
                if z == k:
                    n.append(v)
                    encoded_message = ''.join(n)
encoding_list = []
def encoding(int,key):
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string
encoded_message = encoding(message, 3)
print (encoded_message)

