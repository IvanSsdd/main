import manual

def test_reverse_hello():
    if manual.reverse_string("Hello") == "olleH":
        print("Test reverse_string(Hello) is OK")
    else:
        print("Test reverse_string(Hello) is Fail")

def test_reverse_car():
    if manual.reverse_string("Car") == "raC":
        print("Test reverse_string(Car) is OK")
    else:
        print("Test reverse_string(Car) is Fail")

def test_reverse_tools():
    if manual.reverse_string("Tools") == "slooT":
        print("Test reverse_string(Tools) is OK")
    else:
        print("Test reverse_string(Tools) is Fail")

def test_reverse_world():
    if manual.reverse_string("World") == "dlroW":
        print("Test reverse_string(World) is OK")
    else:
        print("Test reverse_string(World) is Fail")

def test_reverse_dogs():
    if manual.reverse_string("Dogs") == "sgoD":
        print("Test reverse_string(Dogs) is OK")
    else:
        print("Test reverse_string(Dogs) is Fail")

def test_palindrome_anna():
    if manual.is_palindrome("Anna") == "Anna":
        print("Test is_palindrome(Anna) is OK")
    else:
        print("Test is_palindrome(Anna) is Fail")

def test_palindrome_stats():
    if manual.is_palindrome("stats") == "stats":
        print("Test is_palindrome(stats) is OK")
    else:
        print("Test is_palindrome(stats) is Fail")

def test_palindrome_refer():
    if manual.is_palindrome("refer") == "refer":
        print("Test is_palindrome(refer) is OK")
    else:
        print("Test is_palindrome(refer) is Fail")

def test_palindrome_madam():
    if manual.is_palindrome("madam") == "madam":
        print("Test is_palindrome(madam) is OK")
    else:
        print("Test is_palindrome(madam) is Fail")

def test_palindrome_level():
    if manual.is_palindrome("level") == "level":
        print("Test is_palindrome(level) is OK")
    else:
        print("Test is_palindrome(level) is Fail")

def test_glass_w_shla():
    if manual.glass_w("Шла") == 1:
        print("Test glass_w(Шла) is OK")
    else:
        print("Test glass_w(Шла) is Fail")

def test_glass_w_mashina():
    if manual.glass_w("Машина") == 3:
        print("Test glass_w(Машина) is OK")
    else:
        print("Test glass_w(Машина) is Fail")

def test_glass_w_sobaka():
    if manual.glass_w("Собака") == 3:
        print("Test glass_w(Собака) is OK")
    else:
        print("Test glass_w(Собака) is Fail")

def test_vowels_koshka():
    if manual.glass_w("Кошка") == 2:
        print("Test glass_w(Кошка) is OK")
    else:
        print("Test glass_w(Кошка) is Fail")

def test_glass_w_shkola():
    if manual.glass_w("Школа") == 2:
        print("Test glass_w(Школа) is OK")
    else:
        print("Test glass_w(Школа) is Fail")

def test_duplicates_hello_world():
    if manual.remove_duplicates("Hello world") == "Helo wrd":
        print("Test remove_duplicates(Hello world) is OK")
    else:
        print("Test remove_duplicates(Hello world) is Fail")

def test_duplicates_he_knows():
    if manual.remove_duplicates("he knows Inglish") == "he knows gli":
        print("Test remove_duplicates(he knows Inglish) is OK")
    else:
        print("Test remove_duplicates(he knows Inglish) is Fail")

def test_duplicates_qwe():
    if manual.remove_duplicates("qweqweqwe") == "qwe":
        print("Test remove_duplicates(qweqweqwe) is OK")
    else:
        print("Test remove_duplicates(qweqweqwe) is Fail")

def test_duplicates_asd():
    if manual.remove_duplicates("asdasdasd") == "asd":
        print("Test remove_duplicates(asdasdasd) is OK")
    else:
        print("Test remove_duplicates(asdas