# I. Introduction
The `nlu_preprocessing` is the Backend of Lex Bot. It can be combined with NLU in Amazon Lex to correct miss typing input from user thereby impove the user experience. In addition, it also makes the definition of Lex Bot easly.


# II. Problems & Solution
In the conversation with Ria, the user ask the Ria by entering a input sentence to do any task. He can enter the idea input as an sample utterance which is defined in Ria. In other cases, he can also enters the non-idea input which are variants of the idea input. 
They are:
1. Capitalization
2. Without Space
3. Special Character
4. Inflected From 
5. Acronym
6. Spelling Mistake 

In the practice, Ria can not understand all of the variants. And Ria can understand more better if the variants are converted to unique variant. In NLU preprocessing module here are sex applied methods which includes:
1. Decapitalization 
2. Text Segmentation
3. Remove special characters
4. Lemmatization 
5. Acronym Converter
6. Spell Correction


# III. Install & Usage
## 1. Install 
Our module use some free open-sources as wordninja, symspell, nltk.
All of them is listed in the requirement.txt file.. Create your enviroment and run the bellow code
````
pip install -r requirment.txt
````

or activate the created enviroment `venv` by using the bellow code:

````
source venv/bin/activate
````
## 2. Usage
The usage of the NLU preprocess module is detail in `notebook_nlu_preproces_demo.ipynb`.


# IV. References
1. https://github.com/nltk/nltk
2. https://github.com/keredson/wordninja
3. https://github.com/wolfgarbe/symspell










































