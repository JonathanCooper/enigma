from .rotor import Rotor

class EnigmaMachine(object):

    rotor_one_alphabet = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    rotor_two_alphabet = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    rotor_three_alphabet = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    reflector_alphabet = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

    def __init__(self, key):
        if len(key) != 3:
            raise Exception('Key length must be 3')
        #offsets = [ self.letter_to_position(c) for c in key ]
        self.rotors = {
            1: Rotor(self.rotor_one_alphabet),
            2: Rotor(self.rotor_two_alphabet),
            3: Rotor(self.rotor_three_alphabet),
            'R': Rotor(self.reflector_alphabet),
        }
        
        for i in range(0, 3):
            rotor = self.rotors[i + 1]
            offset = self.letter_to_position(key[i])
            rotor.rotate(offset)
            #print(self.rotors[rotor_idx])
            
    def letter_to_position(self, c):
        '''convert letter to its 0-indexed position in the alphabet'''
        return ord(c) - 65

    def decipher(self, ciphertext):
        plaintext = ''
        for character in ciphertext:
            #print(self.rotors[3])
            self.rotors[3].rotate(1)
            #print(self.rotors)
            #print(character)
            for rotor_idx in [3 ,2, 1, 'R']:
                #print(character)
                character = self.rotors[rotor_idx].transform_char(character)
                #print(character)
            for rev_rotor_idx in [1, 2, 3]:
                character = self.rotors[rev_rotor_idx].transform_char(
                    character,
                    True
                )
                #print(character)
            plaintext += character
            #print()
        return plaintext
            
    #def step(self):
    #    if self.rotors[2].input_alphabet[0

    def __repr__(self):
        return str(self.rotors)
