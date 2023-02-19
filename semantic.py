# Task 38.1

import spacy

nlp = spacy.load('en_core_web_md')

# Code extract 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("")

# Code extract 2
tokens = nlp('boat river bus road')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("")

# Code extract 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


#******************************************************************************************************************************************
# NOTE 1
# Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own.
#******************************************************************************************************************************************
# 0.59 Cat and Monkey seems to be similar because they are both animals.
# 0.40 Banana and Monkey have a higher similarity than Banana and cat so it assumed that the model already recognises that monkeys likes to
# eat bananas.
# 0.22 Banana and Cat seems to be dissimilar as it can be assumed that cats do not really like to eat bananas according to the model.
#
# In the Code extract 2, an example of my own was used to see how spaCy's NLP would perform using md core model and different inputs.
#
# 0.46 Boat and River has decently average similarity so the model seems to recognise that boats rides in the river.
# 0.40 Boat and Bus has decently average similarity which is assumed to be because they are both vehicles.
# 0.20 River and Bus are pretty dissimilar which means the model probably recognises that a bus has close to no relation to the river.
# 0.37 Boat and Road has just below average similarities as it can be assumed the boat can be travelled on the road if it has wheels.
# 0.56 River and Road has a pretty high similarity rating as it can be assumed they are are different ways that can be travelled.
# 0.50 Bus and Road has a decent similarity rating which can only be assumed that the model reocngises that the bus rides along the roads.
#******************************************************************************************************************************************



#******************************************************************************************************************************************
# NOTE 2
# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model
# 'en_core_web_md'.
#******************************************************************************************************************************************
# en_core_web_sm seems to load and maybe even perform faster than en_core_web_md and upon research this seems to be true because the
# default en_core_web_sm model uses less memory than that of en_core_web_md as it is not trained with vectors. However, en_core_web_md
# seems to provide more accurate results as it uses vectors.
#******************************************************************************************************************************************