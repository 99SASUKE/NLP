import re

text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"

sent = re.findall(r'\s*([^.!?]+)', text)
    
    # TODO: Remove leading and trailing spaces from each sentence
sent = [s.strip() for s in sent if s.strip()]

print(sent)

