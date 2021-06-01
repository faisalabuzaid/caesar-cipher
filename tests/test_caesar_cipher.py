from caesar_cipher.caesar_cipher import encrypt,decrypt,crack
import re

def test_decrypt():
    actual = encrypt("Cat is animal ! hsdfo # rr5",500)
    expected = "igz oy gtosgr  nyjlu  xx"
    assert actual == expected

def test_encrypt():
    actual = decrypt("igz oy gtosgr  nyjlu  xx",500)
    expected = "cat is animal hsdfo rr"
    assert actual == expected

def test_crack():
    actual = crack("igz oy gtosgr  nyjlu  xx")
    expected = decrypt("igz oy gtosgr  nyjlu  xx",500)
    assert actual == expected

def test_encrypt_1():
    encrypted_test = encrypt('It was the best of times, it was the worst of times.', 5)
    expected = decrypt(encrypted_test, 5)
    actual = crack(encrypted_test)
    assert actual == expected




