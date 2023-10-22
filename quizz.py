print('Witajcie parafianie!')
print('Zapraszam Was do mjego zaduuuuszystego quizu')
print('No to co, pierwsze pytanie na temat Halloween')
print('UWAGA! WSZYSTKIE ODPOWIEDZI PROSZĘ PISAĆ W WIELKIEJ LITERY!')
print('PRZED KAŻDĄ ODPOWIEDZIĄ PROSZĘ WSTAWIAĆ SPACJĘ!!!')
punkty = 0
q1 = input('Co wysysa Ci krew, kiedy śpisz?')
if q1 == ' Wampir':
    print('Okej, jest git')
    punkty += 1
else:
    print('Zła odpowiedź.')
print('Pytanie 2 (1/5 za nami)')
q2 = input('Jak nazywa się wielki potwór, który ma śruby w uszach?')
if q2 == ' Frankenstein':
    print('Okej, to było easy!')
    punkty += 1
else:
    print('Miiiiip...Źle!')
print('Nadchodzi numer 3 - kategoria łatwe')
q3 = input('Kiedy przypada Halloween (miesiąc proszę pisać z małych)?')
if q3 == ' 31 października':
    print('Nice one')
    punkty += 1
else:
    print('...EEEEH...')
print('Pytanko nr czwarte - 2/5 za nami...')
q4 = input('Jak jest tradycja Halloweenowa, która przyszła do Polski z Ameryki?')
if q4 == ' Zbieranie cukierków':
    print('Nieźle')
    punkty += 1
else:
    print('Okej, to już nie było tak łatwe')
print('Już w połowie!!!')
q5 = input('Co jest pomarańczowe i wystawiane przed domy w Halloween?')
if q5 == ' Dynia':
    print('Jej! Dobrze!')
    punkty += 1
else:
    print('Ajajajaj...')
print("Już jesteśmy w 3/5. Wytrzymaj!")
q6 = input('Który z poniższych NIE jest postacią z horroru: Wednesday, Jason Worhees, Freddy Krueger :)')
if q6 == ' Wednesday':
    print('Okej, widzę że nie próżnujesz...')
    punkty += 1
else:
    print('No co ty? Nie wiedziałeś?!')
print('Pytanko nr 7 nadchodzi!!!')
q7 = input('Co najczęściej straszy w nawiedzonych domach?')
if q7 == ' Duch':
    print('Duuuuuuuuchastycznie')
    punkty += 1
else:
    print('Ojjjj...No przeciesz to proste!')
print('Pytanie nr.8 - tu zacznie się zabawa...')
q8 = input('Co budzi się z martwych bez mózgu, i w górze piachu?')
if q8 == ' Mumia':
    print('Wow! Impressing!')
    punkty += 1
else:
    print('Spoko, nie każdy jest Halloweenowym fanem...')
print('Przedostatnie pytanie. Gotowy?')
q9 = input('Jak nazywa się tradycyjne Polskie Halloween?')
if q9 == ' Dziady':
    print('Okayyyyy...Zaskoczyłeś mnie...')
    punkty += 1
else:
    print('Okej, nic się nie stało')
print('Ostanie pytanie!!! Jest ekstrymalneeeeeeee!!!')
q10 = input('Z jakiego plemienia wywyodzi się Halloween???')
if q10 == ' Celtów':
    print('Brawoooooo!!!Suuuuper się spisałeś!!!')
    punkty += 1
else:
    print('Nie gniewam się...To było ekstrymalnie trudne...')
print('SUPER! UDAŁO CI SIĘ!!! JESTEM PRZEKONANY, ŻE POSZŁO CI DUCHASTYYYYYYYYCZNIEEEEE!!!')
print('Uzyskałeś', punkty, 'na 10 punktów...')