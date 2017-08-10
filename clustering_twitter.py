"""
Written by Benyamin Bashari
represent data with Word2Vec
and use clustering methods to seperate tweets
first find the number of clusters with affinity propagation on small data
then use k-means to cluster all of data
"""
from gensim.models import Word2Vec
import file_reader
import os
from variables import *
from text_preprocessor import TextPreprocessor
import numpy as np
import plot_clusters
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import AffinityPropagation

"""
input:
    parameters of word2vec
    and write path of model

make a word2vec model based on all english twitter data

output:
    saves the model on the path
"""


def make_model(size=100, window=75, min_count=5, iter=100, path=TWITTER_WORD2VEC_MODEL1):
    sentence = []
    for f in os.listdir(TWITTER_DATA_PATH):
        tweets = file_reader.read_csv(TWITTER_DATA_PATH+'/'+f)
        for i in range(0, len(tweets), 5):
            if len(tweets[i]) > 6 and tweets[i][6] != 'NULL' and tweets[i][3] != 'NULL' and tweets[i][3] == 'en':
                sentence.append(TextPreprocessor.preprocess(tweets[i][6]))

    model = Word2Vec(sentence, size=size, window=window, min_count=min_count, workers=4, iter=iter)
    model.save(path)

"""
input:
    a list of posts
    Word2Vec model
    size of vectors in Word2Vec

compute average of vectors for each post

output:
    returns a 2d numpy array (len(posts), vec_size)

"""


def make_word2vec_vector(posts, model, vec_size):
    ret = np.zeros((len(posts), vec_size), dtype=float)

    for ind, post in enumerate(posts):
        clean_post = TextPreprocessor.preprocess(post, ret_lst=False)
        tot = 0
        for word in clean_post:
            if model.__contains__(word):
                word_vec = model[word]
            else:
                continue

            word_vec = np.array(word_vec, dtype=float)
            f = clean_post[word]
            tot += f

            word_vec *= f
            ret[ind] += word_vec

        if tot != 0:
            ret[ind] /= (tot * 1.0)


    return ret


model = Word2Vec.load(TWITTER_WORD2VEC_MODEL1)

#reading all posts of G5--2016-5-27--0
sentences = []
tweets = file_reader.read_format_file(TWITTER_DATA_PATH+'/G5--2016-5-27--0.csv')
for i in range(0, len(tweets), 5):
    if len(tweets[i]) > 6 and tweets[i][6] != 'NULL' and tweets[i][3] != 'NULL' and tweets[i][3] == 'en':
        sentences.append(tweets[i][6])


vectors = make_word2vec_vector(sentences, model, 100)
"""knn = NearestNeighbors(algorithm='auto', leaf_size=30, n_neighbors=10, p=1, radius=1.0)
knn.fit(vectors)

while 1:
    print("input your tweets")
    tweet = input()
    lst = knn.kneighbors(make_word2vec_vector([tweet], model, 100), return_distance=False)
    print("Similar Tweets:")
    for ind in lst[0]:
        print(sentences[ind])
    print("Do you want to continue?(y/n)")
    x = input()
    if x == 'n':
        break"""


#find the number of clusters with affinity propagation
"""ap = AffinityPropagation()
ap.fit(vectors[:10000])
mx = 0
for label in ap.labels_:
    mx = max(mx, label)
print(mx+1)
#961
"""
kmeans = KMeans(init='k-means++', n_clusters=1000)

kmeans.fit(vectors[:10000])

lst = [[] for x in range(10)]

for ind, label in enumerate(kmeans.labels_):
    if label < 10:
        lst[label].append(sentences[ind])

for i in range(10):
    for row in lst[i]:
        print(row)
    print('\n\n')










