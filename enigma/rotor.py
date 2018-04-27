

def encipher(c, offset):
    in_idx = letter_to_idx(c)
    wire_idx = in_idx + offset % 26
    wire = wiring[wire_idx]
    out_idx = in_idx + wire % 26
    return idx_to_letter(out_idx)

def letter_to_idx(c):
    return ord(c) - 65

def idx_to_letter(i):
    return chr(i + 65)

alpha = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'

wiring = []
for i, c in enumerate(alpha):
    #print(i, letter_to_idx(c))
    #print(letter_to_idx(c) - i)
    wiring.append(letter_to_idx(c) - i)

print(encipher('Z', 0))
print(encipher('Z', 1))
