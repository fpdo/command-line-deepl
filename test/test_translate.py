from translate import Translator


def test_default_translation():
    en_sentence = ["this", "is", "a", "test"]
    en_sentence_str = " ".join(en_sentence)
    nl_response = "dit is een test"

    obj = Translator(en_sentence)
    rsp = obj.get_response()
    print_tool(en_sentence_str, nl_response, rsp)
    assert (rsp == nl_response)


def test_reverse_translation():
    nl_sentence = ["nl-en", "ik", "heb", "veel", "honger"]
    nl_sentence_str = " ".join(nl_sentence[1:])
    en_response = "i am very hungry"

    obj = Translator(nl_sentence)
    rsp = obj.get_response()
    print_tool(nl_sentence_str, en_response, rsp)
    assert (rsp == en_response)


def test_translate_pt_en():
    pt_sentence = ["pt-en", "estou", "com", "fome", "quero", "queijo"]
    pt_sentence_str = " ".join(pt_sentence[1:])
    en_response = "i'm hungry i want cheese"

    obj = Translator(pt_sentence)
    rsp = obj.get_response()
    print_tool(pt_sentence_str, en_response, rsp)
    assert (rsp == en_response)


def test_translate_pt_nl():
    pt_sentence = ["pt-nl", "estou", "com", "fome", "quero", "queijo"]
    pt_sentence_str = " ".join(pt_sentence[1:])
    nl_response = "ik heb honger, ik wil kaas."

    obj = Translator(pt_sentence)
    rsp = obj.get_response()
    print_tool(pt_sentence_str, nl_response, rsp)
    assert (rsp == nl_response)


def print_tool(src, dst, rsp):
    print(f"\nExpecting '{src}' to be translated to '{dst}'")
    print(f"'{src}' was translated to '{rsp}'\n")
