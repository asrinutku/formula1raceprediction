import requests
import sqlite3
import numpy as np
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt


url = 'https://tr.motorsport.com/f1/standings/'

r = requests.get(url)
soup = bs(r.content, 'html.parser')
print(soup.title.string)
gelenveri = soup.find_all('table', attrs={'class': 'ms-table ms-table--result'})
dartablo = (gelenveri[0].contents)[len(gelenveri[0].contents)-2]
isimtablosu = dartablo.find_all("tr")
namearray = []

for isim in isimtablosu:
    a = 0
    isimler = isim.find_all("span", {"class": "name"})
    name = isimler[0].text
    namearray.append(name)

print(namearray)

for i in range(0,20):
    if namearray[i].startswith(' ') and namearray[i].endswith(' '):
        namearray[i] = namearray[i][1:-1]
        namearray[i] = namearray[i]


print("------------------")

puantablosu = dartablo.find_all("tr")

numberarray = []

for point in puantablosu:
    puanlar = point.find_all("td", {"class": "ms-table_cell ms-table_field--total_points"})
    puan = puanlar[0].text
    numberarray.append(puan)

numberarray[19] = '0'
print("PUAN TABLOSU")
for i in range(20):
    numberarray[i] = int(numberarray[i])
print(numberarray)

print("--------------------")

totalpoints = sum(numberarray)
averagerating = totalpoints
print("TOTAL SCORE OF PİLOTS : ", totalpoints)
print("AVERAGE POİNT OF PİLOTS :", round(averagerating/20, 2))

print("--------------------")

averageratingpilots = []
print("PİLOTLARIN ORTALAMA PUANLARI (PUAN TABLOSU SIRASINA GORE)")
for i in range(20):
    averageratingpilots.append(round(numberarray[i]/21, 1))
print(averageratingpilots)

print("------------------")

lastthreerace = []
intlastthreerace = 0


for point in puantablosu:
    for i in range(3, 20):
        puanlar = point.find_all(("td", {"class": "ms-table_cell ms-table_field--race_points"}))
        lastthreerace.append(puanlar[i].text)

backupltr = lastthreerace.copy()
print(lastthreerace)
print(len(lastthreerace))

intnumbers = []
for i in range(14, 340, 17):
    for j in range(i, i+3):
        if(lastthreerace[j][0] == '-'):
            intnumbers.append(0)
        elif(lastthreerace[j][1] == '-'):
            intnumbers.append(0)
        else:
            lastthreerace[j] = lastthreerace[j].split("/")
            intnumbers.append(int(lastthreerace[j][0]))

# son uc yarıstaki bahsedilen son yarıs japonya yarısı


lastthreeraceaverages = []
intnumbers_np = np.array(intnumbers)
intnumbers_np = intnumbers_np.reshape(20, 3)

for i in range(0, 20):
    lastthreeraceaverages.append(round((intnumbers_np[i:i+1].mean()), 1))

nonnumpylist  = []
for i in lastthreeraceaverages:
    nonnumpylist.append(float(i))


print("\n")
xpuanlari = []
for t in range(0, 13):

    url = ['https://tr.motorsport.com/f1/results/2019/azerbaycan-gp-418609/',
           'https://tr.motorsport.com/f1/results/2019/ispanya-gp-418610/',
           'https://tr.motorsport.com/f1/results/2019/monaco-gp/',
           'https://tr.motorsport.com/f1/results/2019/kanada-gp-418612/',
           'https://tr.motorsport.com/f1/results/2019/fransa-gp-418613/',
           'https://tr.motorsport.com/f1/results/2019/avusturya-gp-418614/',
           'https://tr.motorsport.com/f1/results/2019/britanya-gp-418615/',
           'https://tr.motorsport.com/f1/results/2019/almanya-gp-418616/',
           'https://tr.motorsport.com/f1/results/2019/macaristan-gp-418617/',
           'https://tr.motorsport.com/f1/results/2019/belcika-gp-418618/',
           'https://tr.motorsport.com/f1/results/2019/italya-gp-418619/',
           'https://tr.motorsport.com/f1/results/2019/singapur-gp-418620/',
           'https://tr.motorsport.com/f1/results/2019/rusya-gp-418621/']

    ulkeler = ['azerbaycan','ispanya','monaco','kanada','fransa','avusturya','britanya'
               ,'almanya','macaristan','belcika','italya','singapur','rusya']

    r = requests.get(url[t])
    soup = bs(r.content, 'html.parser')

    gelenveri = soup.find_all('table', attrs={'class': 'ms-table ms-table--result'})

    dartablo = (gelenveri[0].contents)[len(gelenveri[0].contents)-4]
    isimtablosu = dartablo.find_all('tr')
    isimtablo = []


    for isim in isimtablosu:
        isimler = isim.find_all('span' , attrs={'class' : 'name'})
        isimtablo.append(isimler[0].text)

    print(ulkeler[t],"YARIS SONUCU(ESLESME PUANLARI , X PUANI 0 DAN 100 E)")

    for i in range(0,20):
        if isimtablo[i].startswith(' ') and isimtablo[i].endswith(' '):
            isimtablo[i] = isimtablo[i][1:-1]
            isimtablo[i] = isimtablo[i]


    backupltr1 = backupltr.copy()
    uclugruplarlistesi = []
    for i in range(t, 340, 17):
        for j in range(i, i+3):
            if(backupltr1[j][0] == '-'):
                uclugruplarlistesi.append(0)
            elif(backupltr1[j][1] == '-'):
                uclugruplarlistesi.append(0)
            else:
                backupltr1[j] = backupltr1[j].split("/")
                uclugruplarlistesi.append(int(backupltr1[j][0]))



    ucluortalamalistesi = []
    uclugruplarlistesi_np = np.array(uclugruplarlistesi)
    uclugruplarlistesi_np = uclugruplarlistesi_np.reshape(20, 3)

    for i in range(0, 20):
       ucluortalamalistesi.append(round((uclugruplarlistesi_np[i:i+1].mean()), 1))

    tahminlist = []
    eslesmeoranlari = []
    i = 0

    for x in range(0, 100):
        eslesme = 0
        for y in range(0,20):

            isimvenumaralist = []
            zpuani = averageratingpilots[y]*x+ (100-x)*ucluortalamalistesi[y]
            zpuani = round(zpuani,0)

            isimvenumaralist.append(zpuani)
            isimvenumaralist.append((namearray[y]))
            tahminlist.append(isimvenumaralist)
            tahminlist.sort()
            tahminlist.reverse()

        for z in range(0,20):
            if(isimtablo[z] == tahminlist[z][1]):
                eslesme +=1
        eslesmeoranlari.append(eslesme*5)
        tahminlist.clear()

    print(ulkeler[t],eslesmeoranlari)
    print("\n")

    besliler = []
    for i in range(0, 96):
        beslitoplam = 0
        beslitoplam = eslesmeoranlari[i] + eslesmeoranlari[i + 1] + eslesmeoranlari[i + 2] + eslesmeoranlari[i + 3] + eslesmeoranlari[i + 4]
        besliler.append(beslitoplam)

    ilkindex = besliler.index(max(besliler))
    xpuanlari.append(ilkindex)

print("\n")
print("X PUANLARI (X PUANI HER ULKEDEKİ YARIS İCİN ESLESME ORANININ EN YUKSEK OLDUGU ARALIĞIN ORTALAMASINI KABUL EDER)\n",xpuanlari )
url = 'https://tr.motorsport.com/f1/results/2019/meksika-gp-418623/'

r = requests.get(url)
soup = bs(r.content, 'html.parser')

gelenveri = soup.find_all('table', attrs={'class': 'ms-table ms-table--result'})

dartablo = (gelenveri[0].contents)[len(gelenveri[0].contents) - 4]
isimtablosu = dartablo.find_all('tr')
sonisimtablo = []

for isim in isimtablosu:
    isimler = isim.find_all('span', attrs={'class': 'name'})
    sonisimtablo.append(isimler[0].text)

print("MEKSİKA YARIS SONUCU")
print(sonisimtablo)

sontanhminlist = []

for i in range(0,20):
    isimvenumaralist = []

    a = averageratingpilots[i]*sum(xpuanlari)/13+ (100-sum(xpuanlari)/13)*lastthreeraceaverages[i]
    a = round(a,0)
    isimvenumaralist.append(a)
    isimvenumaralist.append(namearray[i])
    sontanhminlist.append(isimvenumaralist)
    sontanhminlist.sort()
    sontanhminlist.reverse()

soneslesme = 0

print("-----------")
print(sontanhminlist)

for z in range(0,20):

    if(sonisimtablo[z] == sontanhminlist[z][1]):
        soneslesme +=1

    elif(z!=19 and sonisimtablo[z+1] == sontanhminlist[z][1]):
        soneslesme +=1

    elif(z!=0 and sonisimtablo[z-1] == sontanhminlist[z][1]):
        soneslesme +=1


print("BASARI ORANI :%",soneslesme*5)











