import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import Thuchanh2
import re
from textblob import TextBlob

# word_tokenize accepts
# a string as an input, not a file.
stop_words = set(stopwords.words('english'))
with open("NoiDung.txt") as names_file:
    file1 = open("NoiDung.txt")

    # Use this to read file content as a stream:
    line = file1.read()
    determineLanguage = TextBlob(f"{line}")
    print(determineLanguage.detect_language())
    res = re.sub(r'[^\w\s]', '', line)
    words = res.split()
    for r in words:
        if not r in stop_words:
            appendFile = open('filteredtext.txt', 'a')
            appendFile.write(" " + r)
            appendFile.close()
