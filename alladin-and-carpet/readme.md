Aladdin wants to travel around the world and will
choose a circular. path to fly on his magical carpet. The
carpet needs enough magic to take him from one
place to another. He kpows that after traveling some
distance, he can find a magic source that will enable
the carpet to travel a further distance.
There are n magical sources along the circular path
numbered from 0 to n-1. Initially, the carpet has no
magic and Aladdin can use a portal to jump to any
magical source and start his journey. The carpet
consumes units of magic equal to the units of distance
travelled. He needs to choose a point to start his
journey that will allow him to complete his journey.
Determine the lowest index of the starting points from
which Aladdin can start his journey and visit all of the
places in the circular path in order. If there is no solution, return -1

For example, there are n = 4 sources of magic along his
route: <br/>
magic = [3, 2, 5, 4] and <br/>
dist = [2, 3, 4, 2]. <br/>
Thefirst attempt is starting at the first source, magic[0]
3. 
<br/>He transports there without cost and collects 3 units
of magic. 
<br/>The distance to the next point is dist[0] = 2.
<br/>It takes 2 units of magic to get there and he collects
magic[1] = 2 units upon arrival, so he has 3 - 2 + 2 =
3 units of magic after making his first carpet ride.
Continuing along the journey:
<br/>
• 3 - dist[1] + magic(2] = 3 - 3 + 5 = 5<br/>
• 5 - dist[2] + magic|3] = 5 - 4 + 4 = 5<br/>
• 5 - dist|3] = 5 - 2 = 3<br/>
At this point, he is back to the first source. Because he
can complete his journey starting at source magic[O],
there is no reason to continue with the analysis so its
index, 0, is returned. To illustrate a point from the same
example, if he starts at position 2, where magic(1]
2 and dist[1] = 3, he will not be able to proceed to the
next point because the distance is greater than his
magic units. Note that the list is circular, so from
magic|3] in this example, the next source on the path is
magic(0].


<br/>
Function Description<br/>
Complete the function optimalPoint in the editor
below. The function must return an integer that
denotes the minimum index of magic from which he
can start a successful journey. If no such starting point
exists, return - 1.<br/>
optimalPoint has the following parameter(s):<br/>
magic[magic[0],…..magic[n-11]: an array of integers<br/>
where magic[il denotes the amount of magic in the th
source<br/>
dist[dist[O]….dist[n-11]: an array of integers where<br/>
dist[i] denotes the distance to the next magical source

