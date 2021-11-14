def mullisort(lst):
#vajame listi pikkust
    n = len(lst)
    
    for i in range(n):
# Kõige pealt vajame nö lippu
        kas_järjestatud = True

#Hakake loendi igat üksust ükshaaval vaatama,
#võrreldes seda naaber väärtusega.
#Iga korduse korral väheneb listi see osa, mida te vaatate.
#Sest ülejäänud listi liikmed  on juba sorteeritud.
        for j in range(n - i - 1):
            
#  Kui vasakul olev  väärtus on suurem kui paremal , siis vahetame need 
            if lst[j] > lst[j + 1]:   
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                kas_järjestatud = False

# Kui rohkem vahetus pole, siis on list sorteeritud ja katkestame funktsiooni
        
        if kas_järjestatud == True:
            break

    return lst

print(mullisort([8,2,6,4,5,2,2,1]))