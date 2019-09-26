from gensim.models import Word2Vec

model = Word2Vec.load("model.bin")
wv = model.wv

del model

print(wv.similarity('عبلة', 'عنتر'))
print(wv.most_similar(positive=['بانت', 'ودع'], negative=['سعاد']))
print(wv.most_similar('رقة'))
print(wv.doesnt_match("عبلة عنترة الحرب أحمد".split()))
