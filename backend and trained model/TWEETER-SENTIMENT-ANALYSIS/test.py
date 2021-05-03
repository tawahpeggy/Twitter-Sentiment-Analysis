# sending a two text a positive and a negative to see if the model is working fine
from dataset import sentiment as s
print(s("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print(s("This movie was utter junk.There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
