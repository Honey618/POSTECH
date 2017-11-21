import json


def example():

    a={"name": "KAIST/TEDX", "place": "KAIST N1", "date": "2017/11/30", "detail": "abcdefghijklmnopqrstuvwxyz"}
    b=json.dumps(a, ensure_ascii=False, indent="\t")
    return b


