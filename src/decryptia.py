import base64


class Base64(object):
    @staticmethod
    def Encode(base_input: str) -> str:
        base_encode = base_input.encode("ascii")

        base64_bytes = base64.b64encode(base_encode)
        base64_string = base64_bytes.decode("ascii")

        return base64_string

    @staticmethod
    def Decode(base_input: str) -> str:
        base64_bytes = base_input.encode("ascii")
        decoded_string_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_string_bytes.decode("ascii")

        return decoded_string


class MorseCode(object):
    @staticmethod
    def Encode(morse_input: str) -> str:
        morse_code = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            "'": '.----.',
            '!': '-.-.--',
            '/': '-..-.',
            '(': '-.--.',
            ')': '-.--.-',
            '&': '.-...',
            ':': '---...',
            ';': '-.-.-.',
            '=': '-...-',
            '+': '.-.-.',
            '-': '-....-',
            '_': '..--.-',
            '"': '.-..-.',
            '$': '...-..-',
            '@': '.--.-.',
            ' ': '/'
        }

        encoded_string = []
        for char in morse_input:
            if char.upper() in morse_code:
                encoded_string.append(morse_code[char.upper()])
        encoded_morse = ' '.join(encoded_string)

        return encoded_morse

    @staticmethod
    def Decode(morse_input: str) -> str:
        morse_code = {
            '.-': 'A',
            '-...': 'B',
            '-.-.': 'C',
            '-..': 'D',
            '.': 'E',
            '..-.': 'F',
            '--.': 'G',
            '....': 'H',
            '..': 'I',
            '.---': 'J',
            '-.-': 'K',
            '.-..': 'L',
            '--': 'M',
            '-.': 'N',
            '---': 'O',
            '.--.': 'P',
            '--.-': 'Q',
            '.-.': 'R',
            '...': 'S',
            '-': 'T',
            '..-': 'U',
            '...-': 'V',
            '.--': 'W',
            '-..-': 'X',
            '-.--': 'Y',
            '--..': 'Z',
            '-----': '0',
            '.----': '1',
            '..---': '2',
            '...--': '3',
            '....-': '4',
            '.....': '5',
            '-....': '6',
            '--...': '7',
            '---..': '8',
            '----.': '9',
            '.-.-.-': '.',
            '--..--': ',',
            '..--..': '?',
            '.----.': "'",
            '-.-.--': '!',
            '-..-.': '/',
            '-.--.': '(',
            '-.--.-': ')',
            '.-...': '&',
            '---...': ':',
            '-.-.-.': ';',
            '-...-': '=',
            '.-.-.': '+',
            '-....-': '-',
            '..--.-': '_',
            '.-..-.': '"'
        }

        decoded_string = []
        morse_words = morse_input.split('/')
        for word in morse_words:
            morse_chars = word.split()
            decoded_word = ''
            for char in morse_chars:
                if char in morse_code:
                    decoded_word += morse_code[char]
            decoded_string.append(decoded_word)

        decoded_text = ' '.join(decoded_string)

        return decoded_text


class BinaryCode(object):
    @staticmethod
    def Encode(binary_input: str) -> str:
        binary_code = {
            'A': '01000001',
            'B': '01000010',
            'C': '01000011',
            'D': '01000100',
            'E': '01000101',
            'F': '01000110',
            'G': '01000111',
            'H': '01001000',
            'I': '01001001',
            'J': '01001010',
            'K': '01001011',
            'L': '01001100',
            'M': '01001101',
            'N': '01001110',
            'O': '01001111',
            'P': '01010000',
            'Q': '01010001',
            'R': '01010010',
            'S': '01010011',
            'T': '01010100',
            'U': '01010101',
            'V': '01010110',
            'W': '01010111',
            'X': '01011000',
            'Y': '01011001',
            'Z': '01011010',
            '0': '00110000',
            '1': '00110001',
            '2': '00110010',
            '3': '00110011',
            '4': '00110100',
            '5': '00110101',
            '6': '00110110',
            '7': '00110111',
            '8': '00111000',
            '9': '00111001',
            '.': '00101110',
            ',': '00101100',
            '?': '00111111',
            "'": '00100111',
            '!': '00100001',
            '/': '00101111',
            '(': '00101000',
            ')': '00101001',
            '&': '00100110',
            ':': '00111010',
            ';': '00111011',
            '=': '00111101',
            '+': '00101011',
            '-': '00101101',
            '_': '01011111',
            '"': '00100010',
            '$': '00100100',
            '@': '01000000',
            ' ': ' '
        }

        encoded_string = []
        for char in binary_input:
            if char.upper() in binary_code:
                encoded_string.append(binary_code[char.upper()])
        encoded_binary = ' '.join(encoded_string)

        return encoded_binary

    @staticmethod
    def Decode(binary_input: str) -> str:
        binary_code = {
            '01000001': 'A',
            '01000010': 'B',
            '01000011': 'C',
            '01000100': 'D',
            '01000101': 'E',
            '01000110': 'F',
            '01000111': 'G',
            '01001000': 'H',
            '01001001': 'I',
            '01001010': 'J',
            '01001011': 'K',
            '01001100': 'L',
            '01001101': 'M',
            '01001110': 'N',
            '01001111': 'O',
            '01010000': 'P',
            '01010001': 'Q',
            '01010010': 'R',
            '01010011': 'S',
            '01010100': 'T',
            '01010101': 'U',
            '01010110': 'V',
            '01010111': 'W',
            '01011000': 'X',
            '01011001': 'Y',
            '01011010': 'Z',
            '00110000': '0',
            '00110001': '1',
            '00110010': '2',
            '00110011': '3',
            '00110100': '4',
            '00110101': '5',
            '00110110': '6',
            '00110111': '7',
            '00111000': '8',
            '00111001': '9',
            '00101110': '.',
            '00101100': ',',
            '00111111': '?',
            '00100111': "'",
            '00100001': '!',
            '00101111': '/',
            '00101000': '(',
            '00101001': ')',
            '00100110': '&',
            '00111010': ':',
            '00111011': ';',
            '00111101': '=',
            '00101011': '+',
            '00101101': '-',
            '01011111': '_',
            '00100010': '"',
            '00100100': '$',
            '01000000': '@',
        }

        binary_list = binary_input.split(' ')
        decoded_string = []
        for binary in binary_list:
            if binary in binary_code:
                decoded_string.append(binary_code[binary])
        decoded_text = ''.join(decoded_string)

        return decoded_text


class VinegereCipher(object):
    @staticmethod
    def Encrypt(plain_text: str, key: str) -> str:
        encrypted_text = ""
        key_length = len(key)
        for i, char in enumerate(plain_text):
            char_code = ord(char.upper())
            if char.isalpha():
                key_char = key[i % key_length].upper()
                key_code = ord(key_char) - 65
                encrypted_code = (char_code + key_code) % 26
                encrypted_char = chr(encrypted_code + 65)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    @staticmethod
    def Decrypt(encrypted_text: str, key: str) -> str:
        decrypted_text = ""
        key_length = len(key)
        for i, char in enumerate(encrypted_text):
            char_code = ord(char.upper())
            if char.isalpha():
                key_char = key[i % key_length].upper()
                key_code = ord(key_char) - 65
                decrypted_code = (char_code - key_code) % 26
                decrypted_char = chr(decrypted_code + 65)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text
