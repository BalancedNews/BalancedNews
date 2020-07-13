from googlesearch import search


query = "Coronavirus’s Spread Broadens Across U.S."

for j in search(query, tld="com", num=10, stop=10, pause=2):
    print(j)
