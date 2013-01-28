mylists - My bookmark keeper, by email
=======
 
I use this to solve a problem I have, and that I wanted to solve by myself:
save bookmarks from my smartphone.

I'm browsing the web on the smartphone and I get to a page or article that:

- Looks promising, but is better read on a desktop
- Looks promising, I should read it later
- Is great, I should save this for future reference

The first solution was to email it to myself.
Yeah, not very fancy.
__So I'm building this bookmark keeper in Python / Django, and it gets it's data from email:__

>I email the article to an email I own.
The application fetches all of it's mail, parses content and saves each email as a data object.

It's starting with only collecting links (URLs).
The goal is to have a list of several things:
Links, TO-DOs, places to check, books to read...

