# CodeKata.com Kata #5: Bloom Filters

## Kata Source

Kata is drawn from codekata.com. Original code kata webpage is visible
[here](http://codekata.com/kata/kata05-bloom-filters/).

## Kata Instructions Excerpt

> There are many circumstances where we need to find out if something is a
> member of a set, and many algorithms for doing it. If the set is small, you
> can use bitmaps. When they get larger, hashes are a useful technique. But when
> the sets get big, we start bumping in to limitations. Holding 250,000 words
> in memory for a spell checker might be too big an overhead if your target
> environment is a PDA or cell phone. Keeping a list of web-pages visited might
> be extravagant when you get up to tens of millions of pages. Fortunately,
> there’s a technique that can help.
>
> Bloom filters are a 30-year-old statistical way of testing for membership in a
> set. They greatly reduce the amount of storage you need to represent the set,
> but at a price: they’ll sometimes report that something is in the set when
> it isn’t (but it’ll never do the opposite; if the filter says that the
> set doesn’t contain your object, you know that it doesn’t). And the nice
> thing is you can control the accuracy; the more memory you’re prepared to
> give the algorithm, the fewer false positives you get. I once wrote a spell
> checker for a PDP-11 which stored a dictionary of 80,000 words in 16kbytes,
> and I very rarely saw it let though an incorrect word. (Update: I must have
> mis-remembered these figures, because they are not in line with the theory.
> Unfortunately, I can no longer read the 8” floppies holding the source, so
> I can’t get the correct numbers. Let’s just say that I got a decent sized
> dictionary, along with the spell checker, all in under 64k.)

See the above-linked page for full kata text.
