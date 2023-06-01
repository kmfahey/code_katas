# CodeKata.com Kata #18: Transitive Dependencies

## Kata Source

Kata is drawn from codekata.com. Original code kata webpage is visible
[here](http://codekata.com/kata/kata18-transitive-dependencies/).

## Kata Text Selection

> Let’s write some code that calculates how dependencies propagate between
> things such as classes in a program.
>
> Highly coupled code is code where the dependencies between things are dense,
> lots of things depend on other things. This kind of program is hard to
> understand, tough to maintain, and tends to be fragile, breaking easily when
> things change.
>
> There are many different kinds of coupling in code. One of the easiest to work
> with programatically is static coupling, where we’re concerned with the
> relationships between chunks of source code. Simplisticly, we can say that
> class A is statically coupled to class B if the compiler needs the definition
> of B in order to compile
>
> In many languages, static dependencies can be determined by source code
> analysis. Tools such as makedepend (for C programs) and JDepend (for Java)
> look for explicit dependencies in the source and list them out.

See the above-linked page for full kata text.
