import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
from textstat import syllable_count
from collections import Counter

# Function to extract article text from URL
def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find('article')
    if article:
        title = article.find('h1').text.strip()
        paragraphs = article.find_all('p')
        article_text = '\n'.join([p.text.strip() for p in paragraphs])
        return title, article_text
    else:
        return None, None


# Function to compute text analysis
def analyse_text(text):
    blob = TextBlob(text)
    words=word_tokenize(text)
    word_count=len(words)
    sentences=sent_tokenize(text)
    sentence_count = len(sentences)
    avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
    complex_words = [word for word in blob.words if syllable_count(word) > 2]
    complex_word_count = len(complex_words)
    percentage_complex_words = (complex_word_count / word_count) * 100 if word_count > 0 else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_word_length = sum(len(word) for word in words) / word_count
    syllable_per_word = syllable_count(text) / word_count if word_count > 0 else 0
    personal_pronouns = Counter([word.lower() for word, tag in nltk.pos_tag(word_tokenize(text)) if tag == 'PRP'])
    avg_word_length = sum(len(word) for word in blob.words) / word_count if word_count > 0 else 0
    
    positive_score = sum(1 for sentence in sentences if TextBlob(sentence).sentiment.polarity > 0)
    negative_score = sum(1 for sentence in sentences if TextBlob(sentence).sentiment.polarity < 0)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (word_count + 0.000001)
    

    return positive_score, negative_score, polarity_score, subjectivity_score, \
           avg_sentence_length, percentage_complex_words, fog_index, \
           avg_sentence_length, complex_word_count, word_count, syllable_per_word, \
           personal_pronouns['i'] + personal_pronouns['me'] + personal_pronouns['my'] + personal_pronouns['mine'] + personal_pronouns['myself'], \
           avg_word_length


input_df = pd.read_excel("Input.xlsx")

# Process each URL and perform data analysis
output_data = []
for index, row in input_df.iterrows():
    url = row['URL']
    title, article_text = extract_article_text(url)
    if article_text:
        # Compute text analysis variables
        variables = analyse_text(article_text)
        output_row = [row['URL_ID']] + list(variables)
        output_data.append(output_row)

# Create DataFrame for output data
output_df = pd.DataFrame(output_data, columns=['URL_ID', 'Positive_Score', 'Negative_Score', 'Polarity_Score',
                                               'Subjectivity_Score', 'Avg_Sentence_Length', 'Percentage_of_Complex_Words',
                                               'FOG_Index', 'Avg_Number_of_Words_Per_Sentence', 'Complex_Word_Count',
                                               'Word_Count', 'Syllable_Per_Word', 'Personal_Pronouns', 'Avg_Word_Length'])

# Write output data to Excel file
output_df.to_excel("Output_Data.xlsx", index=False)
