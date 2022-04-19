import re 
import nltk # natural language toolkit
import string
import heapq
from IPython.core.display import HTML

# I added the word machine at the end of the last sentence
original_text = """Artificial intelligence is human like intelligence. 
                   It is the study of intelligent artificial agents. 
                   Science and engineering to produce intelligent machines. 
                   Solve problems and have intelligence. 
                   Related to intelligent behavior. 
                   Developing of reasoning machines. 
                   Learn from mistakes and successes. 
                   Artificial intelligence is related to reasoning in everyday situations."""

# original_text
original_text = re.sub(r'\s+', ' ', original_text)
nltk.download('punkt')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
# print(stopwords)

def preprocess(text):
    text = re.sub(r'\s+', ' ', text)
    formatted_text = text.lower()
    tokens = []
    for token in nltk.word_tokenize(formatted_text):
        tokens.append(token)
    #print(tokens)
    tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]
    formatted_text = ' '.join(element for element in tokens)

    return formatted_text

def output(original_text, summary_sentence_count = 3):
    formatted_text = preprocess(original_text)

    word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))

    highest_frequency = max(word_frequency.values())

    for word in word_frequency.keys():
        word_frequency[word] = (word_frequency[word] / highest_frequency)

    sentence_list = nltk.sent_tokenize(original_text)

    score_sentences = {}
    for sentence in sentence_list:
        #print(sentence)
        for word in nltk.word_tokenize(sentence.lower()):
            #print(word)
            if sentence not in score_sentences.keys():
                score_sentences[sentence] = word_frequency[word]
            else:
                score_sentences[sentence] += word_frequency[word]

    
    best_sentences = heapq.nlargest(summary_sentence_count, score_sentences, key = score_sentences.get)

    summary = ' '.join(best_sentences)

    return summary