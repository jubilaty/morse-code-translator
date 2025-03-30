from final import encoder, decoder, validate_morse

def test_encoder_basic():
    assert encoder("SOS") == "... --- ..."
    assert encoder("HELLO") == ".... . .-.. .-.. ---"

def test_decoder_basic():
    assert decoder("... --- ...") == "SOS"
    assert decoder(".... . .-.. .-.. ---") == "HELLO"

def test_spaces():
    assert encoder("A B") == ".- / -..."
    assert decoder(".- / -...") == "A B"

def test_unsupported_chars():
    assert encoder("hello#") == ".... . .-.. .-.. --- ?"

def test_validate_morse():
    assert validate_morse("... --- ...") == True
    assert validate_morse("... --- ?") == False
