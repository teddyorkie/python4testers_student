import unittest
from easy import basic
from medium import ceasar, iban
# import hard

class CheckMediumSolutions(unittest.TestCase):
    def test_ceasar_encrypt(self):
        self.assertEqual(ceasar.encrypt_message("I have an apple"), "JIBWFBOBQQMF")

    def test_ceasar_decrypt(self):
        self.assertEqual(ceasar.decrypt_message("WJFUOBNDIJFOUIBOHDPWJE"), "VIETNAMCHIENTHANGCOVID")

    def test_iban_num(self):
        self.assertTrue(iban.validator_IBAN("GB72HBZU70067212125300"))
        self.assertFalse(iban.validator_IBAN("DE021001001001515617108"))

if __name__ == "__main__":
    unittest.main()