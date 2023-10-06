import time
import random
import os
import webbrowser

keywords = open(r'C:\Users\shafi\OneDrive\Desktop\BingSearch\keywords.txt','r')
data = keywords.read()
# when newline ('\n') is seen.
words = data.split("\n")
random_word = random.sample(words,34)


# Starting to capture the time
st = time.time()


for i in range(0, len(random_word)):
    query=random_word[i].replace(' ','')
    url = f'https://www.bing.com/search?q={str(query)}'
    webbrowser.open(url)
    
    # This will indicate how many searches done, in the Terminal for reference.
    print("Search number :",i+1,"done!")
    time.sleep(3)
    
    

ed = time.time()
# Showing the time after calculation on terminal
print(f"That took {round(ed-st)} seconds ")
time.sleep(5)