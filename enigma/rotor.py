class Rotor(object):
    
    def __init__(self, rotor_config):
        output_alphabet, notch = rotor_config.split('.')
        self.offset = 0
        if notch == '?':
            self.notch = None
        else:
            self.notch = self.letter_to_idx(notch)
        self.wiring = []
        self.output_alphabet = output_alphabet
        for i, c in enumerate(output_alphabet):
            self.wiring.append(self.letter_to_idx(c) - i)
    
    def in_notch_position(self):
        return self.offset == self.notch

    def output_letter_index(self, c):
        return self.output_alphabet.index(c)

    def letter_to_idx(self, c):
        return ord(c) - 65

    def idx_to_letter(self, i):
        return chr(i + 65)

    def transform_char(self, c, inverse=False):
        if inverse:
            in_idx = self.output_alphabet.index(c)
            return self.idx_to_letter(in_idx)
        else:
            in_idx = self.letter_to_idx(c)
            return self.output_alphabet[in_idx]
    
    def rotate(self, offset=1):
        """
        rotate the rotor and return True if this activates notch, else False
        """
        self.wiring = self.wiring[offset:] + self.wiring[:offset]
        self.output_alphabet = ''
        for i, wire in enumerate(self.wiring):
            out_idx = i + wire
            if out_idx > 25:
                out_idx %= 26
            if out_idx < 0:
                out_idx += 26
            self.output_alphabet += self.idx_to_letter(out_idx)
        self.offset += offset
        self.offset %= 26

    def __repr__(self):
        return '<Rotor {0}'.format(self.output_alphabet)
