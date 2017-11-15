# 3. zadanie: zarovnaj
# autor: Matúš Gál
# datum: 15.11.2017


def vypis(meno_suboru, sirka):
    with open(meno_suboru, encoding='utf-8') as f:                  # subor treba otvorit cez with, inak testovac vypise chybu
       words = f.read().split('\n')                                 # precita cely subor po znakoch a spravi split na konci riadkov
    f.close()
    words = [x.strip(' ') for x in words]                           # pre vsetky riadky odstrani medzery na zaciatku a na konci riadku
    indices = list()
    for i in range(len(words)):                                     # pre vsetky riadky vytvori zoznam slov v riadku
        words[i] = words[i].split()

    for i in range(len(words)):                                     # nahradi prazdny zoznam vo words ' '
        if words[i] == []:
            words[i] = ' '
    words = [j for i in words for j in i]                           # spoji list of lists do 1 zoznamu

    for i in range(len(words)):
        if words[i] == ' ' and words[i - 1] == ' ':                 # ked su za sebou 2 medzery ulozi index do zoznamu indices
            indices += [i]

    for i in indices:                                               # toto odstrani prebytocne medzery
        del words[i]
        indices[:] = [x - 1 for x in indices]                       # toto asi nieco robi :D

    if words[len(words) - 1] == ' ':                                # ak je na konci zoznamu medzera
        del words[len(words) - 1]                                   # tak ju odstrani

    indices = list()
    for i in range(len(words)):                                     # najde indexy medzier v zozname
        if words[i] == ' ':                                         # medzery su teraz uz len na konci kazdeho odstavca
            indices += [i]

    par = ['' for _ in range(len(indices) + 1)]                     # vytvori prazdny zoznam pre kazdy odstavec

    indices += [0, len(words)]                                      # prida do zoznamu indexov 1 a posledny index zoznamu words
    indices.sort()                                                  # utriedi zoznam

    x = 0                                                           # toto vytvori retazec pre kazdy odstavec v subore
    y = 1                                                           
    for i in range(len(par)):
        for j in range(x, indices[y]):
            par[i] += words[j] + ' '
        x = indices[y] + 1
        y += 1


    if sirka > 0:                                                   # toto tam nemusi byt, len tak pre istotu
        for i in range(len(par)):
            str = par[i][:-1]                                       # str = odstavec bez posledneho znaku

            while len(str) > sirka:                                 # blok sa vykonava kym dlzka retazca > zadana sirka
                odd = 0
                for i in range(sirka + 1):                          # najde poslednu medzeru medzi str[0: sirka]
                    if str[i] == ' ':
                        odd = i
                if odd == 0:                                        # ked nenajde tam vyhladame mimo sirku, slova > sirka sa maju vypisat cele
                    odd = str.find(' ')

                if odd > 0:                                         # ked odd > 0, takze nie sme na poslednom slove odstavca
                    medz = list()
                    riadok = list(str[0:odd])                       # naseka riadok do zoznamu
                    for i in range(len(riadok)):                    # vyhlada vsetky medzery v riadku a zapamata si indexy
                        if riadok[i] == ' ':
                            medz += [i]
                    p = (sirka - len(riadok))                       # vypocet kolko medzier este treba doplnit medzi slova

                    x = 0
                    op = 0                                          # pomocna premenna: pocet opakovani
                    while p > 0 and len(medz) > 0:                  # ked je pocet medzier > 0 a mame v riadku viac ako 1 slovo
                        if op < len(medz):                          # ked ma op hodnoty < ako je pocet medzier medzi slovami
                            riadok.insert(medz[op], ' ')            # na poziciu op vlozi medzeru
                            medz = medz[:op] + [x + 1 for x in medz[op:]]       # pre vsetky indexy od aktualnej pozicie zvysi kazdy index o 1,
                            op += 1                                             # pretoze sa predlzil zoznam o 1 prvok, op sa zvysi o 1
                        else:                                       # ak op >= len(medz) treba vynulovat premennu op, vlozi sa medzera na poziciu 1,
                            op = 0                                  # ak je p > 0 tak sa v dalsom priebehu cyklu vykona predchadzajuci blok prikazov (66-69)
                            riadok.insert(medz[op], ' ')
                            medz = medz[:op] + [x + 1 for x in medz[op:]]
                            op += 1
                        p -= 1                                      # znizi p pri kazdom pridani medzery

                    vysl = ''.join(riadok)                          # vytvori
                    print(vysl)                                     # a vypise konecny retazec
                    str = str[odd + 1:len(str)]                     # vytvori novy retazec od pozicie poslednej medzery + 1 do konca retazca
                else:
                    print(str, end='')                              # toto sa vypise ked sme na poslednom slove retazca, ale toto slovo je dlhsie ako sirka
                    str = ''                                        #do str priradime prazdny retazec, ktory zabezpeci ukoncenie cyklu

            print(str)                                              # vypise zvysok retazca ked len(str) < sirka
            print()                                                 # vypise prazdny riadok na konci odstavca
vypis('subor1.txt', 60)
