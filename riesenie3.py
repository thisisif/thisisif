# 3. zadanie: zarovnaj
# autor: Matúš Gál
# datum: 6.11.2017


def vypis(meno_suboru, sirka):
    with open(meno_suboru, encoding='utf-8-sig') as f:
        words = f.read().split('\n')
    f.close()
    words = [x.strip(' ') for x in words]
    indices = list()
    for i in range(len(words)):
        words[i] = words[i].split()
    print(words)

    for i in range(len(words)):
        if words[i] == []:
            words[i] = ' '
    words = [j for i in words for j in i]

    for i in range(len(words)):
        if words[i] == ' ' and words[i - 1] == ' ':
            indices += [i]

    for i in indices:
        del words[i]
        indices[:] = [x - 1 for x in indices]
    if words[len(words) - 1] == ' ':
        del words[len(words) - 1]
    indices = list()
    for i in range(len(words)):
        if words[i] == ' ':
            indices += [i]
    par = ['' for _ in range(len(indices) + 1)]
    indices += [0, len(words)]
    indices.sort()
    x = 0
    y = 1
    for i in range(len(par)):
        for j in range(x, indices[y]):
            par[i] += words[j] + ' '
        x = indices[y] + 1
        y += 1
    if sirka > 0:
        for i in range(len(par)):
            str1 = ''.join(par[i])
            str1 = str1[:len(str1)-1]
            odd, medzery, pocet_slov = 0, 0, 0
            while len(str1) > sirka:
                odd = 0
                for j in range(sirka):
                    if str1[j] == ' ':
                        odd = j
                        pocet_slov += 1
                medz = list()
                if odd > 0:
                    riadok = list(str1[0:odd])
                else:
                    riadok = list(str1[0:sirka])
                for k in range(len(riadok)):
                    if riadok[k] == ' ':
                        medz += [k]
                p = (sirka - len(riadok))
                x = 0
                op = 0
                while p > 0:
                    if len(medz) > 0:
                        if op < len(medz):
                            riadok.insert(medz[op] + x, ' ')
                        else:
                            op = 0
                            riadok.insert(medz[op], ' ')
                        op += 1
                        p -= 1
                        x += 1
                    else:
                        riadok.insert(len(riadok), ' ')
                        p -= 1
                vysl = ''.join(riadok)
                print('{:<{sirka}}'.format(vysl, sirka=sirka))
                if odd > 0:
                    str1 = str1[odd + 1:len(str1)]
                else:
                    str1 = str1[sirka:len(str1)]
            print(str1)
            print()
vypis('subor1.txt', 60)
