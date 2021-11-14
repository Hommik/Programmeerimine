import requests
# Avab faili katastritunnused.txt
lst = []

def fail(failinimi):
    with open(failinimi, mode = 'r+', encoding = 'utf8') as kat:
        for i in kat:
            lst.append(i.strip('\n'))
        #print(lst)
fail("katastritunnused.txt")
kooslist = []
# Teeb Maa-ameti geoportaali päringu
# Töötleb päringut ning leiab kõikide maatükkide pindala
def req(list):
    for kataster in list:
        r = requests.get('https://geoportaal.maaamet.ee/url/xgis-ky.php?ky='+ kataster +'&out=json')
        r = r.json()
        r = r.pop('1')
        #kooslist.append(req(lst))
        print(teisendaja(r['Pindala']))
        return kooslist
        #return r
#funktsioon mis teisendab hektarid ruutmeetriteks
#v]tab aluseks dict
def teisendaja(j):
#käib ühe kaupa listi läbi
#kontrollib kas ha on liikmes
    if 'ha' in j:
#kui on siis eemaldab ha, teeb floatiks, ja korrutab 10k
        newfloat = float(j.replace(' ha', ''))
        newfloat *= 10000
#gprint(str(newfloat))
        return newfloat
    else:
#kui ei siis eeldame et on m2 ja eemaldame selle, ning tagastame floatina            
        newfloat = float(j.replace(' m²',''))
        return newfloat

#kooslist.append(req(lst))
print(kooslist)
req(lst)
# Tekitab listi, kus sees on listid, milles on katastritunnus ja pindala (pindala on m2
#või ha, lihtsustamiseks vali neist üks)

# Sorteerib listi pindala järgi suurimast väiksemani (võite kasutada bubblesorti)


# Väljastab csv faili, kus on katastritunnus ja pindala (kasutada sorteeritud listi)
