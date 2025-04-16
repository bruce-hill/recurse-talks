#!/bin/env slides

# Paradoxes

*Bruce Hill*

-------------

# Warning

🚨 This is a no-meta-jokes talk. 🚨

This talk is **not** a paradox.

-------------

# What Is a Paradox?

A paradox occurs when two things you **know** to be true
contradict each other.

A paradox means that one or both of the things you know
to be true are actually **false.**

Paradoxes are a way to fix your understanding of the world.

*Paradoxes aren't something to marvel at, like how big the
universe is, or how weird Quantum Mechanics is.*

**Paradoxes are a *you* problem, not a universe problem**

-------------

# Obligatory Etymology Slide

> Greek "paradoxos":  "contrary to expectation, incredible,"
  from para- "contrary to" (see para- (1)) + doxa "opinion,"

-------------

# Baby's First Paradox

## The Liar's Paradox

> This sentence is false.

(Originally "All Cretans are liars", spoken by a Cretan)

I think this paradox is pretty lame. If anything, the two
contradictory premises are:

1. All grammatically correct sentences are either **true** or **false**
2. The sentence `This sentence is false.` is grammatically correct.

I think it's pretty obvious that (1) is false. Lots of
sentences just don't have coherent "truthy" interpretations.
The sentence is just incoherent.

-------------

# Zeno's Paradoxes

## Achilles and the Tortoise

Achilles is a fast runner and he's racing against a
tortoise. Since he's faster, he gives the tortoise a small
head start.

In order to run past the tortoise, Achilles first has to
catch up to where the tortoise is now.

In the time it takes Achilles to catch up to where the
tortoise was, the tortoise has moved ahead by a bit.

Repeat ad infinitum. Achilles will never pass the tortoise
because he's constantly stuck catching up.

-------------

# Achilles and the Tortoise

**False Premise:** it takes infinitely long to do an
infinite number of things.

Zeno didn't know about calculus. You can have an infinite
sum that adds up to a finite quantity.

**See also:** Zeno's Arrow, where an arrow has to get
halfway from its current position to its target infinitely
many times.

-------------

# Easy Mode: Over

Okay, those are some of the simple paradoxes.
I don't think anyone here is confused by them.
We live in a post-Zeno world.

From here on out, shit's gonna get real.

-------------

# Envelope Paradox

There are two envelopes with money in them.
One envelope has twice as much money as the other.
You are allowed to pick one envelope to take.

**If you have a chance to change your mind, and pick the other
envelope, should you?**

If your envelope holds **$X**, you have:
- **50% chance** to double your money and get **$2X**
- **50% chance** to halve your money and get **$0.5X**
`E(value) = 0.5 * 2X + 0.5 * 0.5X = 1.25X`
So, it seems like you would make more money by switching!

Would you like to switch again? **Infinite money!**

-------------

# Envelope Paradox Resolution

The mathematical formulation is bad.
Another way to frame the calculations is:

There is **$X** in one envelope and **$2X** in the other.
If you switch envelopes:
- There is a **50% chance** you had the big envelope and lose **-$X** by switching
- There is a **50% chance** you had the small envelope and gain **+$X** by switching
`E(gain) = 0.5 * -X + 0.5 * +X = 0`

-------------

# Raven Paradox

Consider the hypothesis:

> All ravens are black.

If this is true, then it must be true that:

> If something is not black, it's not a raven.

If you see a black raven, this should bolster your
confidence in the hypothesis, right?

If you see something yellow and it's not a raven, that
should **also** bolster your confidence in the hypothesis.
**Every non-black, non-raven you see makes you more
confident in the hypothesis.**

"Look, a blueberry! I guess all ravens really are black, huh?"

This is obviously absurd.

-------------

# Raven Paradox Resolution

The paradox all along was the idea that this is absurd.

Actually, you **should** increase your confidence when you
see non-black non-ravens. It's just that you've already seen
a ton of non-black non-ravens.

Imagine you visit a foreign country and you have a theory
that every word for an animal ends in `-mo`. A cat is a
`blorpmo`, a dog is a `squeemo`.

You flip to a random page in a translation dictionary and
see a word that ends in `-snoz`. You guess that it therefore
must not be an animal, and sure enough, it means "bottle".
You do this a few times and every random word that doesn't
end in `-mo` is, sure enough, not an animal. Your theory
seems more plausible.

In the raven case, it's just that we've **already seen too
many non-black non-ravens**. At this point, each additional
one we see only nudges the probability a teeny tiny bit.

-------------

# The Friendship Paradox

This is a fact from graph theory:

> On average, each person's friends have more friends than
  that person does.

Our intuition is that:
"Some of my friends are more X than me, some are less"
and on balance, that averages out.

It would be true if you were talking about being good
looking or being tall or skill at pinball machines, but not
"having friends"!

What's going on?

-------------

# The Friendship Paradox Resolution

The issue is **sampling bias**.

Assume there are:
- **10 people with 1 friends**
- **10 people with 15 friends**
- **10 people with 29 friends**
The average person has **15 friends**

However, everyone has at least 10 friends who are friends
with everyone, a few people who are friends with half of
people, and most people aren't friends with any loners.

If you have an average number of friends, you're probably
friends with a lot of people who are more social than you
and not very many people who have no friends.

-------------

# The Twin Paradox

Facts from Einstein's theory of Special Relativity:

- Time passes more slowly as you approach the speed of light
- Velocity is relative and no perspective is privileged

Imagine you have two twins on Earth.

One twin (Sigourney) goes on a round trip journey to Beta Hydri,
traveling 24.38 light years at 99.9999% the speed of light.

The other twin (Eartha) stays home.

From Eartha's perspective, Sigourney is traveling at near the
speed of light, and must, therefore, be aging more slowly.
After about 48 years, Sigourney will return home, having aged
only 24 days.

However, from Sigourney's perspective, it looks like Eartha
and the rest of the planet Earth was whizzing away at
99.9999% the speed of light. As distances contract at high
speed as well, it looks like Beta Hydri is only 12 light
days away, so after reaching the destination 12 days later,
Sigourney turns the ship around and makes the 12 light day
journey back to Earth. From his perspective, Eartha must
have aged only about 49 minutes because she was traveling at
relativistic speeds.

Who is right?

-------------

# The Twin Paradox Resolution

It turns out that the **acceleration** matters. Sigourney is
turned into jelly by the relativistic acceleration on her
trip, and that's a big difference that is **absolute** and
not purely in the eye of the beholder. Sigourney doesn't think
that Eartha is undergoing intense acceleration.

When Sigourney reaches the turnaround point in her journey, any
signals sent from Eartha would catch up to him "all at once",
and as she decelerates, she sees message after message coming
from Eartha all in rapid succession. Sigourney knows that Eartha
has aged years as soon as Sigourney slows down.

It's almost as if the acceleration is what makes the
universe realize that Eartha is going to be older than Sigourney
when they reunite.

If Sigourney never accelerated, the paradox would be unresolved.

-------------

# Simultaneity

What if Sigourney wasn't Eartha's twin, but was actually born
"at the same time" as Eartha, thirty years ago on a spaceship
mid-flight on its way past Earth to Beta Hydri?

What does it mean for Eartha and Sigourney to be the same age?
It means they were born at the same time.

What is "the same time"?

Turns out that's a whole can of worms and [the universe does
not care what you think.](https://en.wikipedia.org/wiki/Ladder_paradox)

-------------

# Takeaways

Paradoxes help us understand when we're wrong:
- When our intuitions are at odds with the universe
- When we screwed up our math
- When we aren't actually making sense

You can't **cause** a paradox in a time-travel movie, you
can only uncover when the screenwriter is contradicting
their own worldbuilding rules.
