class Cipher:
    def _init_(self, keyword):
        self.keyword = keyword
        self.alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet_lower = self.alphabet_upper.lower()
        self.cipher_alphabet_upper = self.generate_cipher_alphabet(keyword.upper())
        self.cipher_alphabet_lower = self.cipher_alphabet_upper.lower()

    def generate_cipher_alphabet(self, keyword):
        seen = set()
        unique_keyword = "".join([x for x in keyword if not (x in seen or seen.add(x))])
        remaining_alphabet = "".join([x for x in self.alphabet_upper if x not in set(unique_keyword)])
        return unique_keyword + remaining_alphabet

    def encode_char(self, char):
        if char.isupper():
            index = self.alphabet_upper.find(char)
            return self.cipher_alphabet_upper[index] if index != -1 else char
        elif char.islower():
            index = self.alphabet_lower.find(char)
            return self.cipher_alphabet_lower[index] if index != -1 else char
        else:
            return char

    def decode_char(self, char):
        if char.isupper():
            index = self.cipher_alphabet_upper.find(char)
            return self.alphabet_upper[index] if index != -1 else char
        elif char.islower():
            index = self.cipher_alphabet_lower.find(char)
            return self.alphabet_lower[index] if index != -1 else char
        else:
            return char

    def encode(self, data):
        return ''.join([self.encode_char(char) for char in data])

    def decode(self, data):
        return ''.join([self.decode_char(char) for char in data])