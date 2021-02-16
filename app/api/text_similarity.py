# everything in the text_similarity notebook, but in a python file. 

# importing regex and other python modules

import re
from collections import Counter
import math
import os

# loading and establishing stop words

current_dir = os.path.dirname(os.path.abspath(__file__))
stopwords_file = os.path.join(current_dir, 'stopwords.txt')

with open(stopwords_file, 'r') as s:
    stop_words = s.read()

# function to pre-process the data
def text_processing(sample):
    """
    A function to pre-process the text

    - Lower the text
    - Remove punctuation from the text
    - remove stop words
    - tokenize the text
    """
    # Can't do accurate lemmetization or stemming without a library or spending months accounting for every vocabulary, So no lemmetization or stemming technique used. 
    
    # lower the text
    sample = sample.lower()

    # use regex to remove anything that is not words and numbers
    sample = re.sub(r"[^a-zA-Z0-9]", " ", sample) 

    # tokenize text
    sample = sample.split()

    # remove stop words
    sample = [word for word in sample if word not in stop_words]

    return sample

#  A function for calculating term frequency

def term_frequency(processed_text):
    """
    This function will calculate the term frequency of every word in the document

    The input is the pre-process text that is already tokenized

    The output is the frequency of each word divided by total number of words 
    """

    total_word_count = len(processed_text)

    # individual word count
    word_count = dict(Counter(processed_text))

    # calculating term frequency (tf)
    tf = {}

    for word, count in word_count.items():
        tf[word] = round(count/total_word_count, 4)

    return tf

# Function to calculate Inverse Document Frequency for 2 documents. 
# doing IDF for all 3 samples doesn't make sense because the final 
# product will calculate IDF for only 2 samples inputed as the "POST Method"

def idf(doc1, doc2):
    """
    Calculate the inverse document frequency assuming only 2 documents
    
    Input is the 2 documents in questions

    Output will be the IDF of the words in both documents
    """

    # convert each document into a set. 
    set_1 = set(doc1)
    set_2 = set(doc2)

    # find word that occurs in both documents
    words_in_both_docs = set_1 & set_2

    # find word that occurs only once in either document
    words_in_only_one_doc = set_1 ^ set_2

        # number of documents. In this case, we know only 2 documents will be used for comparison. No need to account for comparing more than 2 documents. 

    number_of_doc = 2

    # creating a dictionary of the document frequency of the term
    # document frequency is number_of_doc/term_frequency_in_document
    # inverse document frequency is log(document frequency)

    doc_freq = {}

    for word in words_in_both_docs:
        doc_freq[word] = round(math.log(number_of_doc/2), 2)

    for word in words_in_only_one_doc:
        doc_freq[word] = round(math.log(number_of_doc/1), 4)

    return doc_freq


# assuming calculating the TF-IDF for only 2 documents of interest and not the entire sample set. 

def tf_idf(tf, idf):
    
    tf_idf = {}
    
    for word, value in tf.items():
        tf_idf[word] = round(value * idf[word], 4)

    return tf_idf

# function for calculating cosine similarity

def cosine(tf_idf1, tf_idf2):
    """
    The input value are the 2 tf-idf dictionary for each sample. 

    the values from dictionary values which are the vectors will be used
    to calculate the dot product of both vectors and the magnitude of each 
    vector in order to get the cosine similarity value. 

    The output will be the cosine similarities between the 2 samples
    """
    # get the values from the tf_idf dictionary
    v1 = list(tf_idf1.values())
    v2 = list(tf_idf2.values())

    # calculate dot product from both vectors
    dotproduct=0

    for a,b in zip(v1,v2):
        dotproduct = dotproduct+a*b

    # calculate magnitude of each vector

    # magnitude of v1
    mag_v1 = math.sqrt(sum(pow(element, 2) for element in v1))
    
    # magnitude of v2
    mag_v2 = math.sqrt(sum(pow(element, 2) for element in v2))

    # now combine dot product and magnitude to get cosine similarity value

        # check to prevent zero division

    if (mag_v1 * mag_v2) > 0:
        cosine_similarity = round(dotproduct/(mag_v1 * mag_v2), 2)
    else:
        cosine_similarity = 1.0

    return cosine_similarity

def similarity_comparison(sample1, sample2):
    """"
    Using all the functions above to write one function
    for similarity comparison.

    """
    # pre-processing the text
    processed_text1 = text_processing(sample1)
    processed_text2 = text_processing(sample2)

    # calculating term frequency of each document
    tf1 = term_frequency(processed_text1)
    tf2 = term_frequency(processed_text2)

    # calculate the inverse_document frequency using the pre-processed text
    inverse_doc_freq = idf(processed_text1, processed_text2)

    # calculating term-frequency-inverse-document-frequency (TFIDF) for each document set
    tfidf1 = tf_idf(tf1, inverse_doc_freq)
    tfidf2 = tf_idf(tf2, inverse_doc_freq)

    # caculating similarity score using cosine method
    similarity_score = cosine(tfidf1, tfidf2)

    return similarity_score


if __name__ == "__main__":
    sample1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."

    sample2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

    score = similarity_comparison(sample1, sample2)
    print(score)