Title: Artwork: Custom Hive Tile Set 
Date: 2015-01-04 1:12 PM

Generally, I do better making gifts for people than I do with any of my other projects.  Usually I make gifts for christmas, and usually, under the pressure of the deadline, of saving money, and of appealing to the taste of the recipient, I come up with something cooler than I would have if I had just done any old thing that came to mind.  Engineers after all work better in general when they have constraints.  This year, I set out to make a game set for my brother Corey, and the game I chose to make was one that I enjoy playing myself,  [Hive](http://www.hivegame.com/)

<center>
![Hive Game](/images/hive-header.jpg)
</center>

The Game
--------
Hive is a simple tile game for two players in which hexagonal tiles are placed and moved in such a way as to create an ever changing "hive" of insects that form the both the playfield and the pieces.  The object of the game is to arrange the hive as to surround the opponent's queen, using the various moves that are available to the variety of bugs on your team.  [My wife](http://about.me/katherinekovach) is quick to point out that these bugs don't belong in a hive together, making the game unsuitable for children, to whom it might provide a false impression of structure of the social insect world.  I as an adult however, can ignore its inaccuracy for the sake of good gameplay.  Much like chess, each type of bug has a different style of movement that corresponds roughly to the real-world behavior of that bug.  For example, the grasshopper "hops" over the hive in large jumps, while the spider makes more versatile three-step moves.

The Art
-------
To make the tiles, I was determined to use my CNC, but I didn't want to simply copy the artwork on the original tiles.  The artwork on the tiles was designed for a constant-depth relief cut that is filled in with ink or paint on the plastic tiles, but the wooden tiles I intended to make were going to be carved with a V-bit much like you would use for carving text on a wooden sign.  Also, it feels lame to just make a duplicate of the game set when I have the opportunity to take some artistic liberties.  To that end, I got a sharpie and some card stock, and I drew out all the bugs that I intended to make tiles for:

[flickr:id=16171298436]

[flickr:id=15574733104]

[flickr:id=16011049259]

[flickr:id=16195252781]

[flickr:id=16009651608]

[flickr:id=16196323622]

These are the originals.  If you've played Hive before, you'll note that there are a few icons above that do not appear in the original set.  I will discuss these next.

New Bugs
--------
One of the fun things about making a set from scratch is the opportunity to make new tiles!  Katie and I came up with a few new tiles for the game a while back, and I selected a couple to include in this set.  These new tiles are _The Mantis_, _The Tree_, and _The Snail._  For those who are Hive players or just interested, I will include their descriptions below.

**The Snail**
> The snail moves like the queen bee, one space at a time, and cannot move on top of the hive.  The snail is distinguished from the queen bee in that she can move once on every turn _in addition to_ each players normal move.

**The Mantis**
> The mantis moves like the spider, exactly three spaces, without traversing the top of the hive.  The mantis is distinguished from the spider in that she can, instead of moving, _eliminate an adjacent bug from the game, if that bug belongs to the same team as the mantis_  In other words, you can use the mantis to remove one of your own tiles from the game, if that suits your advantage.  This is mainly a last-ditch strategy, but is handy in instances where you are pinned in by your opponent, and need to open up some breathing room for your queen.  The mantis cannot kill bugs of the opposing team, and the bugs thus removed are _removed from the game entirely_ and not elligible to be re-placed on a subsequent turn.

**The Tree**
> The tree is not acually our idea, but something I read on the [Board Game Geek](http://www.boardgamegeek.com/) forums. There is only one tree, and if used, it is the _first tile_ placed, not counting as a turn for either team.  This helps to ease the advantage that the first player has over the second. 

Creating the Tiles
------------------
In order to create the tiles themselves, I had to scan in my drawings as shown above, clean up the raster images, and generate toolpaths for my [ShopBot](http://www.shopbottools.com/) CNC.  I did the vectorization in [Inkscape](http://www.inkscape.org/) and generated the toolpaths using the V-Carve software that came with my ShopBot.

<center>
![Vectorized Bugs in Inkscape](/images/inkscape-screenshot-hive.png)
</center>

After tinkering with the vectorization, DXF export and toolpaths, I did some experimental cutting:

[flickr:id=15834278757]

The first cut (shown above) was out of some pine board I had lying around.  The pine actually carved pretty nicely, although the cut edges are a little rough.  I did a bad job zeroing the tool to the surface, and you can see that the edges of the bugs are not as crisp as I would have liked.  This was a good first test though, and it gave me an opportunity to try out different _tabbing_ strategies.  This is one of those designs that requires a lot of tabs, on account of being an array of tiny pieces.  Fine tuning was required to get tabs that sufficiently held the work in place, but also made it easy to break the finished tiles out of the stock material.

[flickr:id=15834462769]

My v-carving woes were resolved by doing a surfacing pass first to level the carving surface.  This is the sort of thing you can resolve mathematically if you have sufficiently sophisticated CNC software, but the "shortcut" is to simply surface the stock first so that the tool is at all times level with the material.  You can see in the picture above that the fidelity of the carving pass was improved substantially.  The wood used on this second attempt was poplar, which did not carve as well as the pine, but the cutouts were nicer, and the wood is harder overall, and in my opinion, prettier.

The Hive game set is composed of 17 tiles per player, including all of the official expansions as well as the custom bugs that Katie and I invented. The teams are distinguished from one another in the normal Hive game by the tile colors, which are white and black.  For my set, I chose light and dark stain colors for my poplar pieces.  After sanding the tiles, I used Minwax "Golden Oak" (210B) and "Espresso" (273) to color the light and dark tiles, respectively.  These were leftover stain cans I had lying around my shop.  The pieces **did not require much stain.**  I stained a few throwaway tiles first, and the best strategy I found was to moisten the tip of a shop towel with the stain and just rub it into the wood.  I didn't bother with getting stain in the relief cuts, because I intended to paint over them anyway.

[flickr:id=16032553532]

[flickr:id=16007459386]

After letting the stain set overnight, I painted the relief cuts by hand using acrylic paint and a teeny brush.  These are inexpensive hobby-store paints that can be had for about 60 cents a bottle.  The quality of the paint doesn't matter much here, because it's going on thick in the carved areas, and will be laqured over in any case.  One thing I can say about the poplar is that it made a relatively rough material to carve, relative to some of the other materials I have worked with subsequently.  I am told this is typical of the wood, and something like a maple, cherry, hickory, or mahogany would have produced a much smoother finish in the V-carved areas for the same speed and feed rate.  In the image below, you can see the rough surface of the carved areas of the pillbug, which are essentially too small and intricate to sand.  It made them more difficult to paint, but once the paint is down, it's not as obvious, and after the laquer is applied, it's virtually unnoticable.

[flickr:id=15852312228]

Painting these things was a real pain.  They are only 1.5" on a side, and with the rough cut of the carved areas, it was hard to "paint inside the lines."  still, they came out pretty smart, and I managed to get all of them done without screwing any of them up too badly.  Of course I see all the mistakes, but I won't point them out here.

[flickr:id=16039433692]

Finally a coat of laquer, of the high gloss variety typically used in preserving china and porcelain figurines.  It works well on wood, and gives everything a nice sheen, as shown above.

I went on some woodworking forums for some tips after this project was done, because the painting of the carved areas was so time consuming.  I didn't find a whole lot of information that applied well to this project, owing to it being composed of so many tiny pieces, but I did experimentally try slathering on paint before staining, and using a sanding block to remove excess so only the carved areas were painted.  This worked pretty well, but resulted in a painted but unstained tile.  You can stain the tiles after painting, but if you're not careful you can get a lot of stain in the carved areas, resulting in discoloration of the painted carving.  The magic of CNC is that you can "print" copies of a successful project, and overall, I would definitely do this one again, but I would spend considerable effort in the next iteration to make the job of painting and staining the tiles easier. 
