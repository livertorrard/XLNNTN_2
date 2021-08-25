import nltk
from nltk.stem import 	WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
data = """
stranded and unable to return home due to covid-19, many foreign tourists have run out of money but manage to get along due to the kindness of locals.
for over two months now since hcmc imposed more stringent social distancing measures, a 29-year-old australian woman, who asked only to be identified as wendy, has been receiving bread, vegetables and other items from her landlady and neighbors.
when the english teaching center where she worked as a part-timer closed in june, she was out of a job and has been staying inside her room in district 10 to avoid contact with outsiders.
every three days her landlady puts food in front of her room and knocks on the door to inform her. sometimes some neighbors, mostly students with whom she had barely spoken earlier, give her bread, milk, medical masks, and hand sanitizers.
she says: "i am deeply touched by their acts of kindness. all i can say to them is thank you. i love vietnam and hope everyone would be safe and the outbreak would quickly be contained so that everything could return to normal."
she came to vietnam on a tourist visa in february last year and was stranded after vietnam closed its borders and suspended international flights a month later.
she has been extending her visa and managed to survive by teaching english, earning vnd15 million ($660) a month, but the resurgence of the coronavirus left her jobless.
a group of stranded indian tourists who were unable to return home since repatriation tickets were too expensive cannot hide their gratitude to a vietnamese man, tran thien phuong, who employed them as parking attendants in hcmc’s district 1.
they too came to vietnam on tourist visas and were stranded. when they ran out of money and could not afford to pay their rents, they were thrown out of their rented places. luckily they met phuong, manager of a parking service company, who decided to employ them after knowing their financial situation despite language barriers.
"the pandemic put everyone in a difficult situation, but these men are far from home, so they face more challenges," phuong told vnexpress international. he also wanted foreigners to have a good impression of vietnamese people.
now the indians have been unemployed for nearly two months after hcmc shut down bars and coffees shops, but phuong gives them free food and other necessities to help them survive the dark days of lockdown.
anthony, a german tourist, who too refused to reveal his full name, has been offered free stay at a homestay in hoi an for more than a year now.
after being stranded in march last year he managed to survive by teaching online english courses though his income was only enough to buy food and cover basic expenses.
luckily his homestay owner has waived free rent and only collects electricity and water bills.
he says: "sometimes my landlady invites me to have dinner with her family. i am totally moved by her act of kindness and hospitality. i consider hoi an as my second home and i will tell my family and friends everything about [it] after returning home."
according to quang nam province authorities, over 900 foreign tourists are still stranded in hoi an. landlords have offered most of them free stay or reduced rents.
for wendy and anthony, the biggest desire now is that countries reopen their borders and restart commercial flights so that they can return home after a long time.
but their dreams remain distant since vietnam is currently grappling with its most challenging covid outbreak so far, and no one knows when a semblance of normalcy will return.
"""
tokenization = nltk.word_tokenize(data)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))  