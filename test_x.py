from main import ( 
     reverse_string
 )

def test_reverse(): 
    assert reverse_string("Привет, мир!") == "!рим ,тевирП"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("qwerty12345") == "54321ytrewq"
    assert reverse_string("!hi!") == "!ih!"
    assert reverse_string("2 DAYS") == "SYAD 2"
    assert reverse_string("IT_TI") == "IT_TI"
    assert reverse_string("") == ""
    assert reverse_string("ВЫДРА") == "АРДЫВ"
    assert reverse_string("cucunber") == "rebnucuc"
    assert reverse_string("hello") == "olleh"