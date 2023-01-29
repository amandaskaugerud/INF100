def dot_product(a,b):
    # lager en løpende sum variabel
    dot_product = 0
    # løper gjennom indeks til listen
    for i in range(len(a)):
        # regner ut prikk produktet
        dot_product += a[i] * b[i]
    return dot_product
