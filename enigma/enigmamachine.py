from .rotor import Rotor

class EnigmaMachine(object):

    rotor_one_config = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ.Q'
    rotor_two_config = 'AJDKSIRUXBLHWTMCQGZNPYFVOE.E'
    rotor_three_config = 'BDFHJLCPRTXVZNYEIWGAKMUSQO.V'
    reflector_config = 'YRUHQSLDPXNGOKMIEBFZCWVJAT.?'

    def __init__(self, key):
        if len(key) != 3:
            raise Exception('Key length must be 3')
        self.rotors = {
            1: Rotor(self.rotor_one_config),
            2: Rotor(self.rotor_two_config),
            3: Rotor(self.rotor_three_config),
            'R': Rotor(self.reflector_config),
        }
        
        for i in range(0, 3):
            rotor = self.rotors[i + 1]
            offset = self.letter_to_position(key[i])
            rotor.rotate(offset)
            
    def letter_to_position(self, c):
        '''convert letter to its 0-indexed position in the alphabet'''
        return ord(c) - 65

    def step(self):
        if self.rotors[2].in_notch_position():
            rotate_rotors = [1, 2, 3]
        elif self.rotors[3].in_notch_position():
            rotate_rotors = [2, 3]
        else:
            rotate_rotors = [3]
        for i in rotate_rotors:
            self.rotors[i].rotate()

    def decipher(self, ciphertext):
        plaintext = ''
        for character in ciphertext:
            self.step()
            for rotor_idx in [3 ,2, 1, 'R']:
                character = self.rotors[rotor_idx].transform_char(character)
            for rev_rotor_idx in [1, 2, 3]:
                character = self.rotors[rev_rotor_idx].transform_char(
                    character,
                    inverse=True
                )
            plaintext += character
        return plaintext
    
    def __repr__(self):
        return str(self.rotors)
