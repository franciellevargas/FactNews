#encoding: utf-8
#!/usr/bin/env python3
#--------------------------
#Author: Francielle Vargas
#Data: 19/09/2022
#--------------------------

import pandas as pd
import spacy
from pathlib import Path
import glob
import os 
import io
import charade 
import codecs #santa biblioteca - resolve o problema da acentuação
nlp = spacy.load("pt_core_news_sm")


#lista apenas os arquivos txt da pasta
path = Path("/home/fvargas/Documents/FactNews-Dataset/Textos-Fonte")
letters_files = path.glob('*.txt')

news = []
for fle in letters_files:
	basename = os.path.basename(fle)
	file_name = os.path.splitext(basename)[0]
	with codecs.open(os.path.join(path, fle), "rb", "utf-8") as f:
		documento = f.readlines()
		for sente in documento:
			doc = nlp(sente) 
			for idi, sent_real in enumerate(doc.sents):
				if sent_real != None:
					news.append([file_name,sent_real])

df = pd.DataFrame(news, columns=['file', 'sentences'])
print(df)
#df_final = df[df.sentences.str.contains('')]
df.to_csv("/home/fvargas/Documents/FactNews-Dataset/factnews.csv")

