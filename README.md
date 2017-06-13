# cwinter
Collaborative writing interactions

## downloading wikipedia

To download XML history of a wikipedia article, first use the browser to navigate to the desired article, lets say we are want to download the article of Donald Trump.

In the browser, the wikipedia article:
https://en.wikipedia.org/wiki/Donald_Trump

To download it using the command line:

`curl -d "" 'https://en.wikipedia.org/w/index.php?title=Special:Export&pages=Donald_Trump&history&action=submit'> donald_trump.xml`

The wikipedia article discussion:
https://en.wikipedia.org/wiki/Talk:Donald_Trump

To download it using the command line:

`curl -d "" 'https://en.wikipedia.org/w/index.php?title=Special:Export&pages=Talk:Donald_Trump&history&action=submit'> talk_donald_trump.xml`

Spanish wikipedia: https://es.wikipedia.org/wiki/Donald_Trump

`curl -d "" 'https://es.wikipedia.org/w/index.php?title=Special:Export&pages=Donald_Trump&history&action=submit'> es_donald_trump.xml`

Spanish wikipedia discussion: https://es.wikipedia.org/wiki/Discussión:Donald_Trump

`curl -d "" 'https://es.wikipedia.org/w/index.php?title=Special:Export&pages=Discussión:Donald_Trump&history&action=submit'> es_talk_donald_trump.xml`