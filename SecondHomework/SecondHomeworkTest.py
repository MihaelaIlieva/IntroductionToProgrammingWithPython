import unittest 
from SecondHomework import plugboard,rotor,enigma_encrypt,enigma_decrypt

plugboard_position = [{'a', 'c'}, {'t', 'z'}]
rotor_position = {'v': 'd', 'd': 'v', 'y': 'u', 'n': 'n', 'i': 'w', 'z': 'p',
                  's': 'e', 'x': 's', 'h': 'f', 'b': 'x', 'u': 'c', 'p': 'q',
                  'r': 'g', 'q': 'j', 'e': 't', 'l': 'y', 'o': 'z', 'g': 'o',
                  'k': 'b', 't': 'h', 'j': 'm', 'a': 'a', 'w': 'i', 'f': 'l',
                  'm': 'r', 'c': 'k'}

@enigma_encrypt(plugboard_position, rotor_position)
def encrypt_decorated(text):
    """Helper to test the encryption decorator."""
    return text


@enigma_decrypt(plugboard_position, rotor_position)
def decrypt_decorated(text):
    """Helper to test the decryption decorator."""
    return text

class TestSecondHomework(unittest.TestCase):
    def setUp(self):
        self.value = 'hmmmm'
        print(self.value)
    def tearDown(self):
        del self.value
    def test_plugboard(self):
        """Tests the plugboard function."""
        self.assertEqual(plugboard("enigma", plugboard_position), "enigmc")
        self.assertEqual(plugboard("aarcetzot", plugboard_position), "ccraeztoz")
        self.assertEqual(plugboard("", plugboard_position),"")
        self.assertEqual(plugboard("t", plugboard_position),"z")
        self.assertEqual(plugboard("c", plugboard_position),"a")
        self.assertEqual(plugboard("tctatctzac", plugboard_position), "zazczaztca")
        self.assertEqual(plugboard("a t", plugboard_position),"c z")
        self.assertEqual(plugboard(" a t ", plugboard_position)," c z ")


    def test_rotor(self):
        """Tests the rotor function."""
        self.assertEqual(rotor("enigmc", rotor_position),"tnwork")
        self.assertEqual(rotor("e", rotor_position),"t")
        self.assertEqual(rotor("e c", rotor_position),"t k")
        self.assertEqual(rotor("", rotor_position),"")
        self.assertEqual(rotor("eeee", rotor_position),"tttt")
        self.assertEqual(rotor("abcdefghijklmopqrstuvwxyz", rotor_position),"axkvtlofwmbyrzqjgehcdisup")

    def test_enigma_encrypt(self):
        self.assertEqual(encrypt_decorated("enigma"),"tnwork")
        self.assertEqual(encrypt_decorated("abcdefghijklmopqrstuvwxyz"),"kxavtlofwmbyrzqjgepcdisuh")
        self.assertEqual(encrypt_decorated("a"),"k")
        self.assertEqual(encrypt_decorated(""),"")
        self.assertEqual(encrypt_decorated("cat"),"akp")


    def test_enigma_decrypt(self):
        self.assertEqual(decrypt_decorated("tnwork"),"enigma")
        self.assertEqual(decrypt_decorated("kxavtlofwmbyrzqjgepcdisuh"), "abcdefghijklmopqrstuvwxyz")
        self.assertEqual(decrypt_decorated("k"),"a")
        self.assertEqual(decrypt_decorated(""), "")
        self.assertEqual(decrypt_decorated("akp"),"cat")


if __name__ == '__main__':
    unittest.main()