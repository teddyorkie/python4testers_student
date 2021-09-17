import wordcount as wc
import pytest
import sys

def main():
    # extract your arg here
    print('Extracted arg is ==> %s' % sys.argv[2])
    pytest.main([sys.argv[1]])      # python pytest filename.py args

# def test_main(monkeypatch):
#     monkeypatch.setattr("sys.argv", ["pytest", "--topcount", "E:/CodeProjects/python_for_testers/google-python-exercises/basic/small.txt"])
#     work.main()

@pytest.mark.parametrize("filename, expected", [
        ("E:/CodeProjects/python_for_testers/google-python-exercises/basic/small.txt", 
            [("--", 1), ("are", 3), ("at", 1), ("be", 3), ("but", 1), ("coach", 1),
            ("football", 1), ("least", 1), ("need", 1), ("not", 3), ("should", 1),
            ("to", 2), ("used", 1), ("we", 6), ("what", 3)]),
        # ("E:/CodeProjects/python_for_testers/google-python-exercises/basic/alice.txt", [])
    ])
def test_get_words(filename, expected):
    assert wc.get_words(filename) == expected

@pytest.mark.parametrize("filename, expected", [
        ("E:/CodeProjects/python_for_testers/google-python-exercises/basic/small.txt", 
            [("we", 6), ("are", 3), ("not", 3), ("what", 3), ("be", 3)]),
        ("E:/CodeProjects/python_for_testers/google-python-exercises/basic/alice.txt", 
            [("the", 1605), ("and", 766), ("to", 706), ("a", 614), ("she", 518)])
    ])
def test_get_top_words(filename, expected):
    assert wc.get_top_words(filename) == expected

if __name__ == '__main__':
    main()