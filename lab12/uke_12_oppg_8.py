def tid_nok_til_egenkapital():
    aarslønn = float(input("Hva er årslønn? "))
    prosent_lønn = float(input("Hvor mange prosent spares? "))
    kostnad = int(input("Hvor mye koster boligen? "))
    måned_lønn = aarslønn/12
    egenkapital = 0.25 * kostnad
    # spart_beløp = (aarslønn * 0.2) + (måned_lønn* utbetalt_måned)
    spart_av_månedslønn = måned_lønn * 0.2 * (prosent_lønn*0.01)
    spart_av_årslønn = aarslønn * 0.2
    # aarlig_rente = 1.04
    # måned_rente = aarlig_rente/12
    # antall_måneder = 0
    # while egenkapital < enough_capital:
    #     egenkapital += egenkapital *måned_rente
    #     egenkapital += egenkapital 

