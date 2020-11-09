# TF_IDF

Python Implementation of [Term Frequency Inverse Document Frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) using the NLTK library.

Given a Corpus from the NLTK library, computes the TF_IDF value between every pair of documents. 

Allows various options to customize the values reported.

## Built With

+ Python 3
+ [NLTK](https://www.nltk.org/)
+ [Scipy](https://www.scipy.org/)

# Preparation Steps:

## Installing Python 3
Run this command to verify Python 3 is installed
    ```
    python3 --version
    ```    
If Python 3 is not installed follow these instructions to install

## Ubuntu
```
sudo apt update
sudo apt install python3
```

## OSX / 11
```
brew install python3
```

## Windows
Download [here](https://www.python.org/downloads/) and follow install instructions.

## Installing NLTK
NLTK performs much of the heavy lifing of this application. It contains the various corpus that are used for training as well as the Stemmers.

Run the following commands to install NLTK:
```
pip3 install nltk
python3
import nltk
nltk.download()
```
A GUI should appear. Click to download all data.

## Installing Scipy
Scipy is used for performing various mathematical computations.
```
pip3 install scipy
```

# Example
While you can use CorpusReader_TFIDF youself, I have also bundled an example runner to show how to use the class.

In order to run the example:
```
python3 generator.py
```

The example program calculates and prints the TF_IDF of the Brown corpus, then the Shakespearean texts, then the state of the union.

# CorpusReader_TFIDF

## Constructor

      corpus: the corpus that documents will be grabbed from
      tf: indicating how the term frequency will be calculated
          raw -- indicates that the raw score will be used
          log -- indicates that the score will be log normalized
          binary -- indicates that the score will be binary in output
              1 indicates that the term is present in the document
              0 indicates that the term is not present in the document
      idf: indicates how the inverse document frequency will be calculated
          base: simply the default
          smooth: the frequency is smoothed
          prob: probabilistic inverse document frequency
      stopword: what the stopwords will be
          standard -- use the default English stopwords
          anything else -- a fileName to read the stopwords from
      stemmer: the stemmer for the words
          Porter or Snowball allowed
      ignorecase: indicates if case should be ignored
          no -- do not ignore case
          yes -- do ignore case

## Example

TF_IDF of Brown Corpus log normalized, smoothed, standard stop words, porter stemmer, and ignores case.
```
CorpusReader_TFIDF("Brown", "log", "smooth", "standard","Porter", "yes")
```
# Author
+ [Ian Laird](https://github.com/i-laird)

# Other Cool Stuff
If you like this project be sure to check out my other NLTK projects! The sentiment analyzer actually uses this project as a subroutine!

+ [Spell Checker](https://github.com/i-laird/Spell_Checker)
+ [Document Sentiment Analyzer](https://github.com/i-laird/Sentiment_Analyzer)
