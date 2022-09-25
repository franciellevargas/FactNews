#/usr/bin/python3.7
#encoding: utf-8

import pandas as pd
from pathlib import Path
import glob
import os 
import io
import charade 
import codecs #santa biblioteca - resolve o problema da acentuação


#lista apenas os arquivos txt da pasta
path = Path("/home/fvargas/Documents/FactNews-Dataset/Textos-Fonte")
letters_files = path.glob('*.txt')
news = []
for fle in letters_files:
    basename = os.path.basename(fle)
    file_name = os.path.splitext(basename)[0]
    with codecs.open(os.path.join(path, fle), "rb", "utf-8") as f:
        text = f.readlines()
        for sente in text:
            news.append([file_name,sente])

df = pd.DataFrame(news, columns=['files', 'sentences'])
df_final = df[df.sentences.str.contains(r' ')]

print(df_final)
#df_final.to_csv("/home/fvargas/Documents/FactNews-Dataset/factnews.csv")

