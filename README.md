# Data-Extraction-and-NLP
This is an open source project in this project data extraction, NLP and text analysis are done. 
# Content
1. Objective
2. Data extraction
3. Data analysis
4. Variables
5. Derivatives Of Variables
6. Final output
# Objective
The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below. 
# Data Extraction
Input.xlsx
For each of the articles, given in the input.xlsx file, extract the article text and save the extracted article in a text file with URL_ID as its file name.
While extracting text, the program extracts only the article title and the article text. It should not extract the website header, footer, or anything other than the article text. 
# Data Analysis
For each of the extracted texts from the article, perform textual analysis and compute variables, save in the output.xlsx.
# Variables
The definition of each of the variables given in the “Text Analysis.docx” file.
Look for these variables in the analysis document (Text Analysis.docx):
1.	POSITIVE SCORE
2.	NEGATIVE SCORE
3.	POLARITY SCORE
4.	SUBJECTIVITY SCORE
5.	AVG SENTENCE LENGTH
6.	PERCENTAGE OF COMPLEX WORDS
7.	FOG INDEX
8.	AVG NUMBER OF WORDS PER SENTENCE
9.	COMPLEX WORD COUNT
10.	WORD COUNT
11.	SYLLABLE PER WORD
12.	PERSONAL PRONOUNS
13.	AVG WORD LENGTH
# Derivatives of variables
1. Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
2. Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
3. Polarity Score: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 
Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1
4. Subjectivity Score: This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: 
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
Range is from 0 to +1
5. Average Sentence Length = the number of words / the number of sentences
6. Percentage of Complex words = the number of complex words / the number of words 
7. Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)
8. Average Number of Words Per Sentence = the total number of words / the total number of sentences
9. Average Word Length = Sum of the total number of characters in each word/Total number of words
# Final Output
The final program is 'Final.py'
The output file is 'Output_data.xlsx'
# Contact
If their is any query related to program. Feel free to ask nitinsatya@gmail.com
