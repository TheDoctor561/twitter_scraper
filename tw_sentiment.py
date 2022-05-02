# Return sentiment of a particular tweet based on analysis made by the react team model 
# Returns a numpy.ndarray of the analysis with 0: negative 1: neutral 2: positive 
# "String" -> numpy.ndarry 

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

def sentimenter(tweet): 
    # precprcess tweet
    tweet_words = []

    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)

    # sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    # output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    """ 
    for i in range(len(scores)):
        
        l = labels[i]
        s = scores[i]
        print(l,s) 
    """

    return scores 

# Take in a dataframe and find the average score of a set amount of tweets using the sentimenter above 

def av_sentiment(df): 
    d = len(df.index)
    neg = 0 
    neu = 0 
    pos = 0 

    for tweet in df: 
        a = sentimenter(tweet)
        neg += a[0]
        neu += a[1]
        pos += a[2]
        
    print(neg/d)
    print(neu/d) 
    print(pos/d)
    
    


