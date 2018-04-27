from enigma import enigmamachine
import sys

start_pos, ciphertext = sys.argv[1], sys.argv[2].replace(' ', '')

machine = enigmamachine.EnigmaMachine(start_pos)

print(machine.decipher(ciphertext))
