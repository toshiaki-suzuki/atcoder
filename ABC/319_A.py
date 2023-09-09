ranking = [
    {"name": "tourist", "score": 3858},
    {"name": "ksun48", "score": 3679},
    {"name": "Benq", "score": 3658},
    {"name": "Um_nik", "score": 3648},
    {"name": "apiad", "score": 3638},
    {"name": "Stonefeang", "score": 3630},
    {"name": "ecnerwala", "score": 3613},
    {"name": "mnbvmar", "score": 3555},
    {"name": "newbiedmy", "score": 3516},
    {"name": "semiexp", "score": 3481}
]

S = input()

for r in ranking:
    if S == r["name"]:
        print(r["score"])
        break
