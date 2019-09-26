from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt
from bidi.algorithm import get_display
import arabic_reshaper

print("Loading model...")
model = Word2Vec.load('model.bin')

vocab = list(model.wv.vocab)
X = model[vocab]

del model

print("Visulalizing some words...")
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X[:100])

df = pd.DataFrame(X_tsne, index=vocab[:100], columns=['x', 'y'])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'])
for word, pos in df.iterrows():
    word = arabic_reshaper.reshape(word)
    word = get_display(word)
    ax.annotate(word, pos, size=8)
