Given a linked list and a value n, remove the nth to last node and return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null

I had 11 minutes and then I decided to take 2 of the minutes to restructure how I'm organizing...

So this seems pretty simple. Brute force being something like:

Iterate through the list until we get to the nth element
  Redo the plumbing (In order to do this we will need to keep track of the last element we tracked over)


I think that in the future I would want to do better planning than this but for now I'm going to work on getting some code down in the limited time remaining.

I'm not even sure how to do a linked list with Python. Probalby just a dict...

So I have a Node class set up that I'm pretty sure is right. I'm a little bit surprised at how rusty I feel with Python. Even just what I've done so far is pretty good. I think I'm going to change this to be a just getting a list set up.

I have a rudimentary list set up but I think it is missing some crucial elements.

I think I'm supposed to have a List class that stores the head and I can use to add elements.

Definitely something weird going... never mind I'm just expecting the line to be ran when it hasn't (second didn't have a next when I was thinking it should.)

It all works as expected! I'm going to call this a success for today and move onto the next task!