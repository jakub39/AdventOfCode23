#cast1
def da_sa(kocka, riadky):
    for riadok in riadky:
        pocet_farieb = [0, 0, 0]  
        for cast_kocky in riadok:
            pocet, farba = cast_kocky.split()
            farby = ['red', 'green', 'blue'].index(farba)
            pocet_farieb[farby] += int(pocet)
        if not all(kocka[i] >= pocet_farieb[i] for i in range(len(kocka))):
            return False
    return True

def mozne_hry(subor):
    max_pocet = [12, 13, 14] 
    vysledok = []

    with open(subor, 'r') as file:
        for radok in file:
            cislo_hry, riadky = radok.strip().split(': ')
            riadky = [riadok.split(', ') for riadok in riadky.split('; ')]
            
            if da_sa(max_pocet, riadky):
                vysledok.append(int(cislo_hry[5:]))

    return vysledok

# Cast 2
def najvacsie_cislo_v_riadku(riadky):
    max_pocet_v_riadku = [0, 0, 0]  

    for riadko in riadky:
        for cast_kocky in riadko:
            pocet, farba = cast_kocky.split()
            farby = ['red', 'green', 'blue'].index(farba)
            if int(pocet) > max_pocet_v_riadku[farby]:
                max_pocet_v_riadku[farby] = int(pocet)

        power = max_pocet_v_riadku[0] * max_pocet_v_riadku[1] * max_pocet_v_riadku[2]
    return power

subor = 'advent23_2.txt'
vysledok = mozne_hry(subor)
print(sum(vysledok))
with open(subor, 'r') as file:
    a = []
    for radok in file:
        cislo_hry, riadky = radok.strip().split(': ')
        riadky = [riadok.split(', ') for riadok in riadky.split('; ')]
        a.append(najvacsie_cislo_v_riadku(riadky))
    vysledok2 = sum(a)
print(vysledok2)