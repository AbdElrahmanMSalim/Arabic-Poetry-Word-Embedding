# Arabic-Poetry-Word-Embedding
Word Embedding for Arabic Poetry using Word2Vec

## Building Word2Vec model:
### 1- Firstly, you need to install the following packages:
#### a- "pip install gensim"
#### b- "pip install pandas"
#### c- "pip install pyarabic"

### 2- Run in cmd "python build_model.py"
This should take from 15 min to 30 min depending on your PC



## Testing the model:
### 1- open "test_model.py" file.
for best experience try working with jupyter or python interactive so that you don't load the whole model every time you test.

### 2- change the words

### 3- Run in cmd "python test_model.py"



## Visualizing the model:
### 1- You need to install the following packages:
#### a- "pip install sklearn"
#### b- "pip install python-bidi"
#### c- "pip install arabic_reshaper"
#### d- "pip install matplotlib"

### 2- Run in cmd "python load_and_visualize_model.py" 
This will visualize the first 100 words

#### I recommend you to visualize the model with work of MR. Amr Salama in here
Arabic-Word-Embeddings-Word2vec
https://github.com/rozester/Arabic-Word-Embeddings-Word2vec


## Many thanks to Dataset Authors:

""" @MISC{PCD2018,
    author = {Waleed A. Yousef and Omar M. Ibrahime and Taha M. Madbouly and Moustafa A. Mahmoud and Ali H. El-Kassas and Ali O. Hassan and Abdallah R. Albohy},
    year   = 2018,
    title  = {Poem Comprehensive Dataset (PCD)},
    url   = {https://hci-lab.github.io/ArabicPoetry-1-Private/#PCD}
}"""
