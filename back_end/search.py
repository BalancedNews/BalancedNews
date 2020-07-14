from googlesearch import search


query = "Daily Kos"

for j in search(query, tld="com", num=1, stop=10, pause=2):
    print(j)
