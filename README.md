# Arabic-Poetry-Word-Embedding

Word Embedding for Arabic Poetry using Word2Vec

![](https://media.giphy.com/media/LpG34AskA447Wy7icY/giphy.gif)

## Building Word2Vec model:

### 1- Firstly, you need to install the following packages:

    pip install gensim
    pip install pyarabic

### 2- Run in cmd "python build_model.py"

This should take from 15 min to 30 min depending on your PC

## Testing the model:

### 1- Open "test_model.py" file.

for best experience try working with jupyter or python interactive so that you don't load the whole model every time you test.

### 2- Change the words in the file

### 3- Run in cmd "python test_model.py"

## Visualizing the model:

I have set the NUMBER_OF_WORDS_TO_VISUALIZE to 10000 word, If you want you can change this in visualize.py file, this embedding has around 900000 words.

### 1- You need to install the following packages:

    pip install tensorflow==1.14.0 // this is the tested version on tensorflow-gpu
    pip install tensorboard

### 2- If you want to start the embedding I built run in cmd directly:

    tensorboard --logdir=visualize_result

### 3- If you have built a model your self run:

    python visualize.py word2vec_format visualize_result
    tensorboard --logdir=visualize_result

### 4- Go to your browser and type:

    http://localhost:6006/

### 5- Select projector from the drop down list on the top right corner.

you may need to refresh the page after loading

## Many thanks to Dataset Authors:

    @MISC{PCD2018,
        author = {Waleed A. Yousef and Omar M. Ibrahime and Taha M. Madbouly and Moustafa A. Mahmoud and Ali H. El-Kassas and Ali O.     Hassan     and Abdallah R. Albohy},
        year   = 2018,
        title  = {Poem Comprehensive Dataset (PCD)},
        url   = {https://hci-lab.github.io/ArabicPoetry-1-Private/#PCD}
    }
