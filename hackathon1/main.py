from itertools import combinations
import unittest
from easy import basic
from medium import ceasar, iban, medium
from hard import hard, vietlott

# 15 bài tập : gồm 8 bài rất dễ,  4 bài trung bình, 3 bài nâng cao. (mỗi bài nâng cao 1 điểm)
class CheckEasySolutions(unittest.TestCase):
    def test_approx_pi(self):
        self.assertAlmostEqual(basic.approx_pi(1), 4.0)
        self.assertAlmostEqual(basic.approx_pi(6), 3.466666666666667)
        self.assertAlmostEqual(basic.approx_pi(1000), 3.13959265558978)

    def test_basic_anagram_number(self):
        self.assertTrue(basic.anagram_number(121121))
        self.assertFalse(basic.anagram_number(12134))
        self.assertTrue(basic.anagram_number(8888888888888888))

    def test_basic_combine_list(self):
        list_one = [10, 20, 23, 11, 17]
        list_two = [13, 43, 24, 36, 12]
        self.assertEqual(basic.combine_list(list_one, list_two), [23, 11, 17, 24, 36, 12])

    def test_basic_day_diff(self):
        self.assertEqual(basic.day_diff("19/12/2021","2021-17-05"), 216)
        self.assertEqual(basic.day_diff("10/05/2021","2021-01-03"), 70)

    def test_basic_dict_from_keys(self):
        self.assertEqual(basic.dict_from_keys({"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}, ["name", "salary"]), 
                                                {'name': 'Kelly', 'salary': 8000})
        self.assertEqual(basic.dict_from_keys(dict(a=1, b=2, c=3, z=26), ['c', 'z']), {"c":3, "z":26})

    def test_basic_reverse_and_swapcase(self):
        self.assertEqual(basic.reverse_and_swap("tHE fOX iS cOMING fOR tHE cHICKEN"), "Chicken The For Coming Is Fox The")

    def test_basic_alpha_num(self):
        self.assertEqual(basic.alpha_num("Emma25 is Data scientist50 and AI Expert"), ["Emma25", "scientist50"])
        self.assertEqual(basic.alpha_num("tHE1 fOX iS cOMING2 fOR tHE4 cHICKEN"), ['tHE1', 'cOMING2', 'tHE4'])

    def test_sortlist_last(self):
        self.assertEqual(basic.sort_list_last([(1, 2, 2), (9, 1, 2), (6, 4, 4), (3, 2, 4), (10, 2, 1)]), 
                        [(6, 4, 4), (3, 2, 4), (1, 2, 2), (9, 1, 2), (10, 2, 1)])
        self.assertEqual(basic.sort_list_last([('Tom', 5, 8), ('John', 9, 10), ('Jonny', 8, 10), ('Jason', 10, 10), ('Anna', 3, 8)]), 
                        [('Jason', 10, 10), ('John', 9, 10), ('Jonny', 8, 10), ('Tom', 5, 8), ('Anna', 3, 8)])

class CheckMediumSolutions(unittest.TestCase):
    def test_str_process(self):
        self.assertEqual(medium.str_process("hello world and practice makes perfect and hello world again"),
                            "again and hello makes perfect practice world")

    def test_roman_to_int(self):
        self.assertEqual(medium.roman_to_int("LVIII"), 58)
        self.assertEqual(medium.roman_to_int("IX"), 9)
        self.assertEqual(medium.roman_to_int("MCMXCIV"), 1994)

    def test_ceasar(self):
        self.assertEqual(ceasar.encrypt_message("I have an apple"), "JIBWFBOBQQMF")
        self.assertEqual(ceasar.decrypt_message("WJFUOBNDIJFOUIBOHDPWJE"), "VIETNAMCHIENTHANGCOVID")

    def test_iban_num(self):
        self.assertTrue(iban.validator_IBAN("GB72HBZU70067212125300"))
        self.assertFalse(iban.validator_IBAN("DE021001001001515617108"))

class CheckHardSolutions(unittest.TestCase):
    def test_sort_letter_digit(self):
        self.assertEqual(hard.sort_letter_digit("Sorting1234"), "ginortS1324")
        self.assertEqual(hard.sort_letter_digit("adfTKMAASWase944852mdk"), "aaddefkmsAAKMSTW592448")

    def test_mortgage_calc(self):
        self.assertAlmostEqual(hard.mortgage_calc(4e5, 30, 4), 1909.66)
        self.assertAlmostEqual(hard.mortgage_calc(8e8, 15, 11), 9092775.48)

    def test_max_water_area(self):
        self.assertEqual(hard.max_water_area([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(hard.max_water_area([1,1]), 1)
        self.assertEqual(hard.max_water_area([4,3,2,1,4]), 16)
        self.assertEqual(hard.max_water_area([1,2,1]), 2)

    from itertools import combinations
    def test_power_6_45_ticket(self):
        user_panel = [3, 5, 7, 8, 13, 23, 42]
        ans = vietlott.power_6_45_ticket(7, user_panel)
        verified_results = combinations(user_panel, 6)
        self.assertListEqual(ans, list(verified_results))

        user_panel = [4, 7, 9, 20, 21, 29, 30, 35, 37, 38, 40]
        ans = vietlott.power_6_45_ticket(11, user_panel)
        verified_results = combinations(user_panel, 6)
        self.assertListEqual(ans, list(verified_results))

        user_panel = [4, 7, 9, 20, 21]
        ans = vietlott.power_6_45_ticket(5, user_panel)
        self.assertEqual(len(ans), 40)
        checker = set()
        for panel in ans:
            checker = checker.union(set(panel).difference(user_panel))
        self.assertSetEqual(checker, set(range(1,46)).difference(user_panel))


if __name__ == "__main__":
    unittest.main()