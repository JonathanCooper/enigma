import enigma
import sys

start_pos, ciphertext = sys.argv[1], sys.argv[2].replace(' ', '')

machine = enigma.EnigmaMachine(start_pos)

print(machine.decipher(ciphertext))
#print(machine.decipher('G'))

#test_rotor = enigma.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')

#test_rotor.rotate(-1)
#print(test_rotor.transform_char('A'))
