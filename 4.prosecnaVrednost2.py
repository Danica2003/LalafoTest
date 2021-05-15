# suknje u opsegu cena od 1-500,500-1000 itd...
x=2102
y=1341
z=962
g=17
o=1
w=2
sum=(x+y+z+g+o+w) # dobila sam zbir 4425 (ostalo su artikli bez cene na dogovor)
print('Na Lalafo ima ukupno sukanja sa istaknutom cenom: ',sum)

ukupnoSukanja=4545
print('Na Lalafo ima ukupno sukanja',ukupnoSukanja)
# bez cene 120
BezCene=(ukupnoSukanja-sum)
print('Na sajtu Lalafo ima sukanja bez cene:',BezCene)

# obzirom da sam izlistala opsege cena, na prvoj i poslednjoj pretrazi sam nasla
#najjeftiniju i najskuplju suknju jer mi je pocetna vrednost bila 1 dinar, a krajnja 20000
# sajt je izlistao hronosloski
najjeftinijasuknja=50
print('Najjeftinija suknja iznosi samo: ',najjeftinijasuknja,'dinara.')
najskupljasuknja=19500
srednjaVrednostsuknje=((najskupljasuknja+najjeftinijasuknja)/2)
print('Srednja vrednost suknje u proseku je oko: ',srednjaVrednostsuknje,'dinara, mada upadaju u opseg izmedju 5001 i 10000 dinara a njih ima ukupno 17')
print('Najskuplja suknja iznosi: ',najskupljasuknja,'dinara')
print('Na sajtu Lalafo u opsegu cena od 1-500 dinara ima',x,'sukanja sto je procentualno: ')
print((x*100)/sum)
print('Na sajtu Lalafo u opsegu cena od 501-1000 dinara ima',y,'sukanja sto je procentualno: ')
print((y*100)/sum)
print('Na sajtu Lalafo u opsegu cena od 1001-5000 dinara ima',z,'sukanja sto je procentualno: ')
print((z*100)/sum)
print('Na sajtu Lalafo u opsegu cena od 5001-10000 dinara ima',g,'sukanja sto je procentualno: ')
print((g*100)/sum)
print('Na sajtu Lalafo u opsegu cena od 10001-15000 dinara ima',o,'sukanja procentualno: ')
print((o*100)/sum)
print('Na sajtu Lalafo u opsegu cena od 15001-20000 dinara ima sukanja ',w,'sto je procentualno: ')
print((w*100)/sum)

print('ZAKLJUCAK JE DA DANAS SVAKO MOŽE DA BUDE RIBA U MINICU I DA SU CENE PRISTUPACNE :)')