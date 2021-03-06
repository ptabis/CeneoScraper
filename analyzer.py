#import bibliotek
import os
import pandas as pd

#wyświetlić zawartość katalogu z opiniami
print(*os.listdir('./opinions_json'))

#wczytanie id produktu, którego opinie będą analizowane
product_id = input('Podaj kod produktu: ')

#wczytanie do ramki danych opinii z pliku
opinions = pd.read_json('./opinions_json/'+product_id+'.json')
opinions = opinions.set_index('opinion_id')

print(opinions)