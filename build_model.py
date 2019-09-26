
from gensim.models import Word2Vec
import pandas as pd
from pyarabic.araby import strip_tashkeel, separate

# Data set can be downloaded from here
""" @MISC{PCD2018,
    author = {Waleed A. Yousef and Omar M. Ibrahime and Taha M. Madbouly and Moustafa A. Mahmoud and Ali H. El-Kassas and Ali O. Hassan and Abdallah R. Albohy},
    year   = 2018,
    title  = {Poem Comprehensive Dataset (PCD)},
    url   = {https://hci-lab.github.io/ArabicPoetry-1-Private/#PCD}
}"""

df = pd.read_csv('cleaned_arabic_dataset.csv')

Bigger_list = []
for i in df['Bayt_Text']:
    li = list(strip_tashkeel(i).split(" "))
    Bigger_list.append(li)

model = Word2Vec(Bigger_list, size=300, window=5, min_count=1, workers=4, sg=1)
model.save("model.bin")
