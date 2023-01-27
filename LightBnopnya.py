import sys


encodings = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258',
             'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', 'cp869', 'cp874',
             'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1',
             'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2']

STARTSWITH = "ПРОЦ"
HAS = "ВЫВОД:"
HAS_NOT = "ОСОВЕННОСТИ"
ENDSWITH = "КНЦ;"


def check_text(txt, startswith, has, has_not, endswith):
    return txt.startswith(startswith) and endswith in txt and has in txt


def debnopnya(txt):

    def encode_criteria(c, encoding):
        return c[0].encode(encoding), c[1].encode(encoding), c[2].encode(encoding), c[3].encode(encoding)

    def decode_criteria(c, encoding):
        return c[0].decode(encoding), c[1].decode(encoding), c[2].decode(encoding), c[3].decode(encoding)

    criteria = encode_criteria(
        (STARTSWITH, HAS, HAS_NOT, ENDSWITH),
        "koi8-r"
    )

    for e_0 in encodings:
        try: c_0 = decode_criteria(criteria, e_0)
        except: continue

        for e_1 in encodings:
            try: c_1 = encode_criteria(c_0, e_1)
            except: continue

            for e_2 in encodings:
                try: c_2 = decode_criteria(c_1, e_2)
                except: continue

                for e_3 in encodings:
                    try: c_3 = encode_criteria(c_2, e_3)
                    except: continue

                    for e_4 in encodings:
                        try: c_4 = decode_criteria(c_3, e_4)
                        except: continue

                        if check_text(txt, c_4[0], c_4[1], c_4[2], c_4[3]):
                            print(txt.encode(e_4).decode(e_3).encode(e_2).decode(e_1).encode(e_0).decode("koi8-r"))
                            return


debnopnya(sys.stdin.read())
