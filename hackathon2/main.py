import unittest
# from easy import basic
# from medium import ceasar, iban, medium
from hard import football, logparser

# 15 bài tập : gòm 8 bài rất dễ,  4 bài trung bình, 3 bài nâng cao. (mỗi bài nâng cao 1 điểm)
# class CheckEasySolutions(unittest.TestCase):
#     def test_basic_print_star(self):
#         pass

#     def test_basic_anagram_number(self):
#         self.assertTrue(basic.anagram_number(121121))
#         self.assertFalse(basic.anagram_number(12134))
#         self.assertTrue(basic.anagram_number(8888888888888888))

#     def test_basic_combine_list(self):
#         list_one = [10, 20, 23, 11, 17]
#         list_two = [13, 43, 24, 36, 12]
#         self.assertEqual(basic.combine_list(list_one, list_two), [23, 11, 17, 24, 36, 12])

#     def test_basic_day_diff(self):
#         self.assertEqual(basic.day_diff("19/12/2021","2021-17-05"), 216)
#         self.assertEqual(basic.day_diff("10/05/2021","2021-01-03"), 70)

#     def test_basic_dict_from_keys(self):
#         self.assertEqual(basic.dict_from_keys({"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}, ["name", "salary"]), 
#                                                 {'name': 'Kelly', 'salary': 8000})
#         self.assertEqual(basic.dict_from_keys(dict(a=1, b=2, c=3, z=26), ['c', 'z']), {"c":3, "z":26})

#     def test_basic_reverse_and_swapcase(self):
#         self.assertEqual(basic.reverse_and_swap("tHE fOX iS cOMING fOR tHE cHICKEN"), "Chicken The For Coming Is Fox The")

#     def test_basic_alpha_num(self):
#         self.assertEqual(basic.alpha_num("Emma25 is Data scientist50 and AI Expert"), ["Emma25", "scientist50"])
#         self.assertEqual(basic.alpha_num("tHE1 fOX iS cOMING2 fOR tHE4 cHICKEN"), ['tHE1', 'cOMING2', 'tHE4'])

#     def test_basic_unique_value_dict(self):
#         self.assertEqual(basic.unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]),
#                             {'S009', 'S007', 'S002', 'S001', 'S005'})
#         self.assertEqual(basic.unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]), 
#                             {22, 25, 26, 27, 38})

# class CheckMediumSolutions(unittest.TestCase):
#     def test_str_process(self):
#         self.assertEqual(medium.str_process("hello world and practice makes perfect and hello world again"),
#                             "again and hello makes perfect practice world")

#     def test_ceasar(self):
#         self.assertEqual(ceasar.encrypt_message("I have an apple"), "JIBWFBOBQQMF")
#         self.assertEqual(ceasar.decrypt_message("WJFUOBNDIJFOUIBOHDPWJE"), "VIETNAMCHIENTHANGCOVID")

#     def test_iban_num(self):
#         self.assertTrue(iban.validator_IBAN("GB72HBZU70067212125300"))
#         self.assertFalse(iban.validator_IBAN("DE021001001001515617108"))

#     def test_approx_pi(self):
#         self.assertAlmostEqual(medium.approx_pi(1), 4.0)
#         self.assertAlmostEqual(medium.approx_pi(6), 3.466666666666667)
#         self.assertAlmostEqual(medium.approx_pi(1000), 3.13959265558978)

class CheckHardSolutions(unittest.TestCase):
    def test_get_total_goals(self):
        self.assertEqual(football.get_total_goals("Barcelona", 2011), 35)
        self.assertEqual(football.get_total_goals("AC Milan", 2011), 90)
        self.assertEqual(football.get_total_goals("AC Milan", 2014), 56)

if __name__ == "__main__":
    unittest.main()