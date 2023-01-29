def rotate_string(s,k):
    # fikk hjelp av Ragnhild Klette til å finne ut av oppdelingen
    # bruker modulo til å finne resten av k delt på lengden av s, og bruker svaret til å rotere bokstavene
    k = k%len(s)
    return s[k:] + s[:k]
