# Chapter 11 Relativity (Kinematics)

We now come to Einstein's theory of relativity. This is where we find out that everything we've done so far in this book has been wrong. Well, perhaps "incomplete" would be a better word. The important point to realize is that Newtonian physics is a limiting case of the more correct relativistic theory. Newtonian physics works perfectly fine when the speeds we're dealing with are much less than the speed of light, which is about  $3 \cdot 10^8$  m/s. It would be silly, to put it mildly, to use relativity to solve a problem involving the length of a baseball trajectory. But in problems involving large speeds, or in problems where a high degree of accuracy is required, we must use the relativistic theory.<sup>1</sup> This is the subject of the remainder of this book.

The theory of relativity is certainly one of the most exciting and talked-about topics in physics. It is well known for its "paradoxes," which are quite conducive to discussion. There is, however, nothing at all paradoxical about it. The theory is logically and experimentally sound, and the whole subject is actually quite straightforward, provided that you proceed calmly and keep a firm hold of your wits.

The theory rests upon certain postulates. The one that most people find counterintuitive is that the speed of light has the same value in any inertial (that is, nonaccelerating) reference frame. This speed is much greater than the speed of everyday objects, so most of the consequences of this new theory aren't noticeable. If we instead lived in a world identical to ours except for the fact that the speed of light was 50 mph, then the consequences of relativity would be ubiquitous. We wouldn't think twice about time dilations, length contractions, and so on.

I have included a large number of puzzles and "paradoxes" in the problems and exercises. When attacking these, be sure to follow them through to completion, and don't say, "I could finish this one if I wanted to, but all I'd have to do would be such-and-such, so I won't bother," because the essence of the paradox may

<sup>1</sup> You shouldn't feel too bad about having spent so much time learning about a theory that's just the limiting case of another theory, because you're now going to do it again. Relativity is also the limiting case of another theory (quantum field theory). And likewise, quantum field theory is the limiting case of yet another theory (string theory). And likewise . . . well, you get the idea. Who knows, maybe it really *is* turtles all the way down.

very well be contained in the such-and-such, and you will have missed out on all the fun. Most of the paradoxes arise because different frames of reference *seem* to give different results. Therefore, in explaining a paradox, you not only need to give the correct reasoning, you also need to say what's wrong with incorrect reasoning.

There are two main topics in relativity. One is Special Relativity (which doesn't deal with gravity), and the other is General Relativity (which does). We'll deal mostly with the former, but Chapter 14 contains some of the latter. Special Relativity may be divided into two topics, *kinematics* and *dynamics*. Kinematics deals with lengths, times, speeds, etc. It is concerned only with the space and time coordinates of an abstract particle, and not with masses, forces, energy, momentum, etc. Dynamics, on the other hand, does deal with these quantities. This chapter covers kinematics. Chapter 12 covers dynamics. Most of the fun paradoxes fall into the kinematics part, so the present chapter is the longer of the two. In Chapter 13, we'll introduce the concept of 4-vectors, which ties much of the material in Chapters 11 and 12 together.

### 11.1 Motivation

Although it was obviously a stroke of genius that led Einstein to his theory of relativity, it didn't just come out of the blue. A number of things going on in nineteenth-century physics suggested that something was amiss. There were many efforts made by many people to explain away the troubles that were arising, and at least a few steps had been taken toward the correct theory. But Einstein was the one who finally put everything together, and he did so in a way that had consequences far beyond the realm of the specific issues that people were trying to understand. Indeed, his theory turned our idea of space and time on its head. But before we get into the heart of the theory, let's look at two of the major problems in late nineteenth-century physics.<sup>2</sup>

![Diagram showing two coordinate systems, S and S', illustrating Galilean transformations. System S has axes x, y, and z. System S' has axes x', y', and z'. An arrow labeled v points from the origin of S to the origin of S' along the x-axis, indicating the relative velocity of the frames.](ba0b85e515ee52be9ced828556097e4f_img.jpg)

Diagram showing two coordinate systems, S and S', illustrating Galilean transformations. System S has axes x, y, and z. System S' has axes x', y', and z'. An arrow labeled v points from the origin of S to the origin of S' along the x-axis, indicating the relative velocity of the frames.

**Fig. 11.1**

#### 11.1.1 Galilean transformations, Maxwell's equations

Imagine standing on the ground and watching a train travel by with constant speed  $v$  in the  $x$  direction. Let the train frame be  $S'$  and the ground frame be  $S$ , as shown in Fig. 11.1. Consider two events that happen on the train. For example, one person claps her hands, and another person stomps his feet. If the space and time separations between these two events in the frame of the train are  $\Delta x'$  and  $\Delta t'$ , what are the space and time separations,  $\Delta x$  and  $\Delta t$ , in the frame of the ground? Ignoring what we'll be learning about relativity in this chapter, the answers are “obvious” (well, in that incorrectly obvious sort of way, as we'll see

<sup>2</sup> If you can't wait to get to the postulates and results of Special Relativity, you can go straight to Section 11.2. The present section can be skipped on a first reading.

in Section 11.4.1). The time separation,  $\Delta t$ , is the same as on the train, so we have  $\Delta t = \Delta t'$ . We know from everyday experience that nothing strange happens with time. When you see people exiting a train station, they're not fiddling with their watches, trying to recalibrate them with a ground-based clock.

The spatial separation is a little more exciting, but still nothing too complicated. The train is moving, so everything in it (in particular, the second event) gets carried along at speed  $v$  during the time  $\Delta t'$  between the two events. So we have  $\Delta x = \Delta x' + v\Delta t'$ . As a special case, if the two events happen at the same place on the train (so that  $\Delta x' = 0$ ), then we have  $\Delta x = v\Delta t'$ . This makes sense, because the spot on the train where the events occur simply travels a distance  $v\Delta t$  by the time the second event happens. The *Galilean transformations* are therefore

$$\begin{aligned}\Delta x &= \Delta x' + v\Delta t', \\ \Delta t &= \Delta t'.\end{aligned}\tag{11.1}$$

Also, nothing interesting happens in the  $y$  and  $z$  directions, so we have  $\Delta y = \Delta y'$  and  $\Delta z = \Delta z'$ .

The principle of *Galilean invariance* says that the laws of physics are invariant under the above Galilean transformations. Alternatively, it says that the laws of physics hold in all inertial frames.<sup>3</sup> This is quite believable. For example, Newton's second law holds in all inertial frames, because the constant relative velocity between any two frames implies that the acceleration of a given particle is the same in all frames.

**REMARKS:** Note that the Galilean transformations aren't symmetric in  $x$  and  $t$ . This isn't automatically a bad thing, but it turns out that it will in fact be a problem in Special Relativity, where space and time are treated on a more equal footing. We'll find in Section 11.4.1 that the Galilean transformations are replaced by the *Lorentz transformations* (at least in the world we live in), and the latter are indeed symmetric in  $x$  and  $t$  (up to factors of the speed of light,  $c$ ).

Note also that Eq. (11.1) deals only with the *differences* in  $x$  and  $t$  between two events, and not with the values of the coordinates themselves. The values of the coordinates of a single event depend on where you pick your origin, which is an arbitrary choice. The coordinate differences between two events, however, are independent of this choice, and this allows us to make the physically meaningful statement in Eq. (11.1). It makes no sense for a physical result to depend on the arbitrary choice of origin, and so the Lorentz transformations we derive later on will also involve only differences in coordinates. ♣

One of the great triumphs of nineteenth-century physics was the theory of electromagnetism. In 1864, James Clerk Maxwell wrote down a set of equations that collectively described everything that was known about the subject. These equations involve the electric and magnetic fields through their space and time derivatives. We won't worry about the specific form of the equations here,<sup>4</sup> but it

<sup>3</sup> It was assumed prior to Einstein that these two statements say the same thing, but we will soon see that they do not. The second statement is the one that remains valid in relativity.

<sup>4</sup> Maxwell's original formulation involved a large number of equations, but these were later written more compactly, using vectors, as four equations.

turns out that if you transform them from one frame to another via the Galilean transformations, they end up taking a different form. That is, if you've written down Maxwell's equations in one frame (where they take their standard nice-looking form), and if you then replace the coordinates in this frame by those in another frame, using Eq. (11.1), then the equations look different (and not so nice). This presents a major problem. If Maxwell's equations take a nice form in one frame and a not-so-nice form in every other frame, then why is one frame special? Said in another way, Maxwell's equations predict that light moves with a certain speed  $c$ . But which frame is this speed measured with respect to? The Galilean transformations imply that if the speed is  $c$  with respect to a given frame, then it is *not*  $c$  with respect to any other frame. The proposed special frame where Maxwell's equations are nice and the speed of light is  $c$  was called the frame of the *ether*. We'll talk in detail about the ether in the next section, but what experiments showed was that light surprisingly moved with speed  $c$  in every frame, no matter which way the frame was moving through the supposed ether.

There were therefore two possibilities. Either something was wrong with Maxwell's equations, or something was wrong with the Galilean transformations. Considering how "obvious" the latter are, the natural assumption in the late nineteenth century was that something was wrong with Maxwell's equations, which were quite new, after all. However, after a good deal of effort by many people to make Maxwell's equations fit with the Galilean transformations, Einstein finally showed that the trouble was in fact with the latter. More precisely, in 1905 he showed that the Galilean transformations are a special case of the Lorentz transformations, valid only when the speed involved is much less than the speed of light.<sup>5</sup> As we'll see in Section 11.4.1, the coefficients in the Lorentz transformations depend on both  $v$  and the speed of light  $c$ , where the  $c$ 's appear in various denominators. Since  $c$  is quite large (about  $3 \cdot 10^8$  m/s) compared with everyday speeds  $v$ , the parts of the Lorentz transformations involving  $c$  are negligible, for any typical  $v$ . This is why no one prior to Einstein realized that the transformations had anything to do with the speed of light. Only the terms in Eq. (11.1) were noticeable.

As he pondered the long futile fight  
To make Galileo's world right,  
In a new variation  
On the old transformation,  
It was Einstein who first saw the light.

<sup>5</sup> It was well known that Maxwell's equations were invariant under the Lorentz transformations (in contrast with their noninvariance under the Galilean transformations), but Einstein was the first to recognize the full meaning of these transformations. Instead of being relevant only to electromagnetism, the Lorentz transformations replaced the Galilean transformations universally.

In short, the reasons why Maxwell's equations were in conflict with the Galilean transformations are: (1) The speed of light is what determines the scale on which the Galilean transformations break down; (2) Maxwell's equations inherently involve the speed of light, because light is an electromagnetic wave.

#### 11.1.2 Michelson–Morley experiment

As mentioned above, it was known in the late nineteenth century, after Maxwell wrote down his equations, that light is an electromagnetic wave and that it moves with a speed of about  $3 \cdot 10^8$  m/s. Now, every other wave that people knew about at the time needed a medium to propagate in. Sound waves need air, ocean waves need water, waves on a string of course need the string, and so on. It was therefore natural to assume that light also needed a medium to propagate in. This proposed medium was called the *ether*. However, if light propagates in a given medium, and if the speed in this medium is  $c$ , then the speed in a reference frame moving relative to the medium will be different from  $c$ . Consider, for example, sound waves in air. If the speed of sound in air is  $v_{\text{sound}}$ , and if you run toward a sound source with speed  $v_{\text{you}}$ , then the speed of the sound waves with respect to you (assuming it's a windless day) is  $v_{\text{sound}} + v_{\text{you}}$ . Equivalently, if you are standing downwind and the speed of the wind is  $v_{\text{wind}}$ , then the speed of the sound waves with respect to you is  $v_{\text{sound}} + v_{\text{wind}}$ .

If this ether really exists, then a reasonable thing to do is to try to measure one's speed with respect to it. This can be done in the following way (we'll work in terms of sound waves in air here).<sup>6</sup> Let  $v_s$  be the speed of sound in air. Imagine two people standing on the ends of a long platform of length  $L$  that moves at speed  $v_p$  with respect to the reference frame in which the air is at rest. One person claps, the other person claps immediately when he hears the first clap (assume that the reaction time is negligible), and then the first person records the total time elapsed when she hears the second clap. What is this total time? Well, the answer is that we can't say without knowing in which direction the platform is moving. Is it moving parallel to its length, or transverse to it (or somewhere in between)? Let's look at these two basic cases. For both of these, we'll view the setup and do the calculation in the frame in which the air is at rest.

Consider first the case where the platform moves parallel to its length. In the frame of the air, assume that the person at the rear is the one who claps first. Then it takes a time of  $L/(v_s - v_p)$  for the sound to reach the front person. This is true because the sound must close the initial gap of  $L$  at a relative speed of  $v_s - v_p$ ,

<sup>6</sup> As we'll soon see, there is no ether, and light travels at the same speed with respect to any frame. This is a rather bizarre fact, and it takes some getting used to. It's hard enough to get away from the old way of thinking, even without any further reminders, so I can't bring myself to work through this method in terms of light waves in an ether. I'll therefore work in terms of sound waves in air.

![Diagram illustrating the kinematics of sound propagation on a moving platform. A platform of length L moves to the right with velocity v_p. A sound wave is emitted from the front of the platform (top stick figure) and travels diagonally down to the rear of the platform (bottom stick figure). The sound velocity relative to the air is v_s. The platform's motion is indicated by dashed outlines at the start and end of the sound's path. Arrows show the direction of v_p, v_s, and the sound's path.](f1bdb3344e1dfb52bbd951365f3c9805_img.jpg)

Diagram illustrating the kinematics of sound propagation on a moving platform. A platform of length L moves to the right with velocity v\_p. A sound wave is emitted from the front of the platform (top stick figure) and travels diagonally down to the rear of the platform (bottom stick figure). The sound velocity relative to the air is v\_s. The platform's motion is indicated by dashed outlines at the start and end of the sound's path. Arrows show the direction of v\_p, v\_s, and the sound's path.

Fig. 11.2

as viewed in the air frame.<sup>7</sup> By similar reasoning, the time for the sound to return to the rear person is  $L/(v_s + v_p)$ . The total time is therefore

$$t_1 = \frac{L}{v_s - v_p} + \frac{L}{v_s + v_p} = \frac{2Lv_s}{v_s^2 - v_p^2}. \quad (11.2)$$

This correctly equals  $2L/v_s$  when  $v_p = 0$ , and infinity when  $v_p \rightarrow v_s$ .

Now consider the case where the platform moves perpendicular to its length. In the frame of the air, we have the situation shown in Fig. 11.2. Since the sound moves diagonally,<sup>8</sup> the “vertical” component is (by the Pythagorean theorem)  $\sqrt{v_s^2 - v_p^2}$ . This is the relevant component as far as traveling the length of the platform goes, so the total time is

$$t_2 = \frac{2L}{\sqrt{v_s^2 - v_p^2}}. \quad (11.3)$$

Again, this correctly equals  $2L/v_s$  when  $v_p = 0$ , and infinity when  $v_p \rightarrow v_s$ .

The times in Eqs. (11.2) and (11.3) are not equal. As an exercise, you can show that of all the possible orientations of the platform relative to the direction of motion,  $t_1$  is the largest possible time, and  $t_2$  is the smallest. Therefore, if you are on a large surface that is moving with respect to the air, and if you know the values of  $L$  and  $v_s$ , then if you want to figure out what  $v_p$  is (assume that it doesn’t occur to you to toss a little piece of paper to at least find the direction of the wind), all you have to do is repeat the above setup with someone standing at various points along the circumference of a given circle around you. If you take the largest total time that occurs and equate it with  $t_1$ , then Eq. (11.2) will give you  $v_p$ . Alternatively, you can equate the smallest time with  $t_2$ , and Eq. (11.3) will yield the same  $v_p$ . Note that if  $v_p \ll v_s$ , we can apply Taylor series approximations to the above two times. For future reference, these approximations give the difference in times as

$$\Delta t = t_1 - t_2 = \frac{2L}{v_s} \left( \frac{1}{1 - v_p^2/v_s^2} - \frac{1}{\sqrt{1 - v_p^2/v_s^2}} \right) \approx \frac{Lv_p^2}{v_s^3}. \quad (11.4)$$

The above setup is the general idea that Michelson and Morley used in 1887 to measure the speed of the earth through the supposed ether.<sup>9</sup> There is, however, a major complication with light that doesn’t arise with sound – the speed of light is so large that any time intervals that are individually measured will have inevitable measurement errors that are far larger than the difference

<sup>7</sup> Alternatively, relative to the initial back of the platform, the position of the sound wave is  $v_s t$ , and the position of the front person is  $L + v_p t$ . Equating these gives  $t = L/(v_s - v_p)$ .

<sup>8</sup> The sound actually moves in all directions, of course, but it’s only the part of the wave that moves in a particular diagonal direction that ends up hitting the other person.

<sup>9</sup> See Handschy (1982) for the data and analysis of the experiment.

between  $t_1$  and  $t_2$ . Therefore, individual time measurements give essentially no information. Fortunately, there is a way out of this impasse.

Consider two of the above “platform” scenarios arranged to be at right angles with respect to each other, with the same starting point. This can be arranged by having a (monochromatic) light beam encounter a beam splitter that sends two beams off at  $90^\circ$  angles. The beams then hit mirrors and bounce back to the beam splitter where they (partially) recombine before hitting a screen, as shown in Fig. 11.3. The fact that light is a wave, which is what got us into this mess in the first place, is now what saves the day. The wave nature of light implies that the recombined light beam produces an interference pattern on the screen. At the center of the pattern, the beams will constructively or destructively interfere (or something in between), depending on whether the two light beams are in phase or out of phase when they recombine. This interference pattern is extremely delicate. The slightest change in travel times of the beams will cause the pattern to noticeably shift.

![Diagram of a Michelson-Morley interferometer setup. A light source emits a beam that hits a beam splitter. The beam splitter divides the light into two perpendicular paths. One path goes up to a mirror and back down to the beam splitter. The other path goes right to a mirror and back left to the beam splitter. The two beams recombine at the beam splitter and then travel down to a screen.](1ac5d5f5a91102977fa90f09677b466d_img.jpg)

The diagram illustrates a Michelson-Morley interferometer. A light source on the left emits a beam that strikes a diagonal beam splitter. The beam splitter reflects a portion of the light upwards towards a horizontal mirror and transmits another portion to the right towards a vertical mirror. Both beams reflect back to the beam splitter, where they recombine. The recombined beam then travels downwards to a screen. Arrows indicate the direction of light travel along each path.

Diagram of a Michelson-Morley interferometer setup. A light source emits a beam that hits a beam splitter. The beam splitter divides the light into two perpendicular paths. One path goes up to a mirror and back down to the beam splitter. The other path goes right to a mirror and back left to the beam splitter. The two beams recombine at the beam splitter and then travel down to a screen.

Fig. 11.3

If the whole apparatus is rotated around, so that the experiment is performed at various angles, then the maximum amount that the interference pattern changes can be used to determine the speed of the earth through the ether ( $v_p$  in the platform setup above). In one extreme case, the time in one arm is longer than the time in the other by  $Lv^2/c^3$ , where we have changed notation in Eq. (11.4) so that  $v_p \rightarrow v$  is the speed of the earth, and  $v_s \rightarrow c$  is the speed of light. But in the other extreme case, the time in this arm is shorter by  $Lv^2/c^3$ . So the maximal interference shift corresponds to a time difference of  $2Lv^2/c^3$ .

However, when Michelson and Morley performed their experiment, they observed no interference shift as the apparatus was rotated around. Their setup did in fact allow enough precision to measure a nontrivial earth speed through the ether, if such a speed existed. So if the ether did exist, their results implied that the speed of the earth through it was zero. This result, although improbable, was technically fine; it might simply have been the case that they happened to do their experiment when the relative speed was zero. However, when they performed their experiment half a year later, when the earth’s motion around the sun caused it to be moving in the opposite direction, they still measured zero speed. It wasn’t possible for both of these results to be zero (assuming that the ether exists), so something must have been wrong with the initial reasoning. Many people over the years tried to explain this null result, but none of the explanations were satisfactory. Some led to incorrect predictions in other setups, and some seemed to work fine but were a bit *ad hoc*.<sup>10</sup> The correct explanation, which followed from

<sup>10</sup> The most successful explanation (and one that was essentially correct, although the reason why it was correct wasn’t known until Einstein fully explained things) was the Lorentz–FitzGerald contraction. These two physicists independently proposed that lengths are contracted in the direction of the motion by precisely the right factor, namely  $\sqrt{1 - v^2/c^2}$ , to make the travel times in the two arms of the Michelson–Morley setup equal, thus yielding the null result.

Einstein's 1905 theory of relativity, was that the ether doesn't exist.<sup>11</sup> In other words, light doesn't need a medium to propagate in; it doesn't move with respect to a certain special reference frame, but rather it moves with respect to whoever is looking at it.

The findings of Michelson–Morley  
 Allow us to say very surely,  
 “If this ether is real,  
 Then it has no appeal,  
 And shows itself off rather poorly.”

##### REMARKS:

1. We assumed above that the lengths of the two arms in the apparatus were equal. In practice, there is absolutely no hope of constructing the lengths to be equal, up to an error that is sufficiently small compared with the wavelength of the light. But fortunately this doesn't matter. We're concerned not with the difference in the travel times associated with the two arms, but rather with the *difference in these differences* as the apparatus is rotated around. Using Eqs. (11.2) and (11.3) with different lengths  $L_1$  and  $L_2$ , you can quickly show that the maximum interference shift corresponds to a time of  $(L_1 + L_2)v^2/c^3$ , assuming  $v \ll c$ .
2. Assuming that the lengths of the arms are approximately equal, let's plug in some rough numbers to see how much the interference pattern shifts. The Michelson–Morley setup had arms with lengths of about 10 m. And we'll take  $v$  to be on the order of the speed of the earth around the sun, which is about  $3 \cdot 10^4$  m/s. We then obtain a maximal time change of  $t = 2Lv^2/c^3 \approx 7 \cdot 10^{-16}$  s. The large negative exponent here might make us want to throw in the towel, thinking that the effect is hopelessly small. But we should be careful about calling a dimensionful quantity “small.” We need to know what other quantity with the dimensions of time we're comparing it with. The distance that light travels in the time  $t$  is  $ct = (3 \cdot 10^8 \text{ m/s})(7 \cdot 10^{-16} \text{ s}) \approx 2 \cdot 10^{-7}$  m, and this happens to be a perfectly reasonable fraction of a wavelength of visible light, which is around  $\lambda = 6 \cdot 10^{-7}$  m, give or take. So we have  $ct/\lambda \approx 1/3$ . The time we want to compare  $2Lv^2/c^3$  with is therefore the time it takes light to travel one wavelength, namely  $\lambda/c$ , and these two times turn out to be roughly the same size. The interference shift of about a third of a cycle was well within the precision of the Michelson–Morley setup. So if the ether had really existed, they definitely would have been able to measure the speed of the earth through it.
3. One proposed explanation of the observed null effect was “frame dragging.” Perhaps the earth drags the ether along with it, thereby yielding the observed zero relative speed. This frame dragging is quite plausible, because in the platform example above, the platform drags a thin layer of air along with it. And more mundanely, a car completely drags the air in its interior along with it. But it turns out that frame dragging is inconsistent with *stellar aberration*, which is the following effect.

Depending on the direction of the earth's instantaneous velocity as it orbits around the sun, a given star might (depending on its location) appear at slightly different places in the sky when viewed at two times, say, six months apart. This is due to the fact that your telescope must be aimed at a slight angle relative to the actual direction to the star, because as the star's light travels down the telescope, the telescope moves slightly in the direction of the earth's motion. The ratio of the earth's speed around the sun to the speed of light is about  $10^{-4}$ , so the effect is small. But it is large enough to be noticeable, and it has

<sup>11</sup> Although we've presented the Michelson–Morley experiment here for pedagogical purposes, the consensus among historians is that Einstein actually wasn't influenced much by the experiment, except indirectly through Lorentz's work on electrodynamics. See Holton (1988).

indeed been measured. Note that it is the velocity of the telescope that matters here, and not its position.<sup>12</sup>

However, if frame dragging were real, then the light from the star would get dragged along with the earth and would therefore travel down a telescope that was pointed directly at the star, in disagreement with the observed fact that the telescope must point at the slight angle mentioned above. Or even worse, the dragging might produce a boundary layer of turbulence which would blur the stars. The existence of stellar aberration therefore implies that frame dragging doesn't occur. ♣

### 11.2 The postulates

Let's now start from scratch and see what the theory of Special Relativity is all about. We'll take the route that Einstein took and use two postulates as the basis of the theory. We'll start with the speed-of-light postulate:

- *The speed of light has the same value in any inertial frame.*

I don't claim that this statement is obvious, or even believable. But I do claim that it's easy to understand what the statement says (even if you think it's too silly to be true). It says the following. Consider a train moving along the ground at constant velocity. Someone on the train shines a light from one point on the train to another. Let the speed of the light with respect to the train be  $c$  ( $\approx 3 \cdot 10^8 \text{ m/s}$ ). Then the above postulate says that a person on the ground also sees the light move at speed  $c$ .

This is a rather bizarre statement. It doesn't hold for everyday objects. If a baseball is thrown on a train, then the speed of the baseball is different in the different frames. The observer on the ground must add the velocity of the ball (with respect to the train) and the velocity of the train (with respect to the ground) to obtain the velocity of the ball with respect to the ground.<sup>13</sup>

The truth of the speed-of-light postulate cannot be demonstrated from first principles. No statement with any physical content in physics (that is, one that isn't purely mathematical, such as, "two apples plus two apples gives four apples") can be proven. In the end, we must rely on experiment. And indeed, all the consequences of the speed-of-light postulate have been verified countless

<sup>12</sup> This aberration effect is not the same as the *parallax* effect in which the direction of the actual position of an object changes, depending on the location of the observer. For example, people at different locations on the earth see the moon at different angles (that is, they see the moon in line with different distant stars). Although stellar parallax has been measured for nearby stars (as the earth goes around the sun), its angular effect is much smaller than the angular effect from stellar aberration. The former decreases with distance, whereas the latter doesn't. For further discussion of aberration, and of why it is only the earth's velocity (or rather, the change in its velocity) that matters, and not also the star's velocity (since you might think, based on the title of this chapter, that it is the relative velocity that matters), see Eisner (1967).

<sup>13</sup> Actually, this isn't quite true, as the velocity-addition formula in Section 11.5.1 shows. But it's true enough for the point we're making here.

times during the past century. As discussed in the previous section, the most well-known of the early experiments on the speed of light was the one performed by Michelson and Morley. And in more recent years, the consequences of the postulate have been verified continually in high-energy particle accelerators, where elementary particles reach speeds very close to  $c$ . The collection of all the data from numerous experiments over the years allows us to conclude with near certainty that our starting assumption of an invariant speed of light is correct (or is at least the limiting case of a more accurate theory).

There is one more postulate in the Special Relativity theory, namely the “relativity” postulate (also called the Principle of Relativity). It is much more believable than the speed-of-light postulate, so you might just take it for granted and forget to consider it. But like any postulate, of course, it is crucial. It can be stated in various ways, but we’ll simply word it as:

- *All inertial frames are “equivalent.”*

This postulate basically says that a given inertial frame is no better than any other. There is no preferred reference frame. That is, it makes no sense to say that something is moving; it makes sense only to say that one thing is moving with respect to another. This is where the “Relativity” in Special Relativity comes from. There is no absolute frame; the motion of any frame is defined only relative to other frames.

This postulate also says that if the laws of physics hold in one inertial frame (and presumably they do hold in the frame in which I now sit),<sup>14</sup> then they hold in all others. It also says that if we have two frames  $S$  and  $S'$ , then  $S$  should see things in  $S'$  in exactly the same way as  $S'$  sees things in  $S$ , because we can just switch the labels of  $S$  and  $S'$  (we’ll get our money’s worth out of this statement in the next few sections). It also says that empty space is homogeneous (that is, all points look the same), because we can pick any point to be, say, the origin of a coordinate system. It also says that empty space is isotropic (that is, all directions look the same), because we can pick any axis to be, say, the  $x$  axis of a coordinate system.

Unlike the first postulate, this second one is entirely reasonable. We’ve gotten used to having no special places in the universe. We gave up having the earth as the center, so let’s not give any other point a chance, either.

Copernicus gave his reply  
 To those who had pledged to deny.  
 “All your addictions  
 To ancient convictions  
 Won’t bring back your place in the sky.”

<sup>14</sup> Technically, the earth is spinning while revolving around the sun, and there are also little vibrations in the floor beneath my chair, etc., so I’m not *really* in an inertial frame. But it’s close enough for me.

The second postulate is nothing more than the familiar principle of Galilean invariance, assuming that the latter is written in the “The laws of physics hold in all inertial frames” form, and not in the form that explicitly mentions the Galilean transformations, which are inconsistent with the speed-of-light postulate.

Everything we’ve said here about the second postulate refers to empty space. If we have a chunk of mass, then there is certainly a difference between the position of the mass and a point a meter away. To incorporate mass into the theory, we would have to delve into General Relativity. But we won’t have anything to say about that in this chapter. We will deal only with empty space, containing perhaps a few observant souls sailing along in rockets or floating aimlessly on little spheres. Though it may sound boring at first, it will turn out to be more exciting than you’d think.

**REMARK:** Given the second postulate, you might wonder if we even need the first. If all inertial frames are equivalent, shouldn’t the speed of light be the same in any frame? Well, no. For all we know, light might behave like a baseball. A baseball certainly doesn’t have the same speed with respect to different frames, and this doesn’t ruin the equivalence of the frames.

It turns out (see Section 11.10) that nearly all of Special Relativity can be derived by invoking *only* the second postulate. The first postulate simply fills in the last bit of necessary information by stating that *something* has the same finite speed in every frame. It’s actually not important that this thing happens to be light. It could be mashed potatoes or something else (well, it has to be massless, as we’ll see in Chapter 12, so they’d have to be massless potatoes, but whatever), and the theory would come out the same. So to be a little more minimalistic, it’s sufficient to state the first postulate as, “There is something that has the same speed in any inertial frame.” It just so happens that in our universe this thing is what allows us to see.<sup>15</sup> ♣

### 11.3 The fundamental effects

The most striking effects of our two postulates are (1) the loss of simultaneity, (2) length contraction, and (3) time dilation. In this section, we’ll discuss these three effects using some time-honored concrete examples. In the following section, we’ll derive the Lorentz transformations using these three results.

#### 11.3.1 Loss of simultaneity

Consider the following setup. In  $A$ ’s reference frame, a light source is placed midway between two receivers, a distance  $\ell'$  from each (see Fig. 11.4). The light source emits a flash. From  $A$ ’s point of view, the light hits the two receivers at the same time,  $\ell'/c$  seconds after the flash. Now consider another observer,  $B$ , who travels to the left at speed  $v$ . From her point of view, does the light hit the receivers at the same time? We will show that it does not.

![Diagram of a light source between two receivers in frame A, and an observer B moving left relative to frame A.](29f60a3e9928502bf399bb221c9bf752_img.jpg)

The diagram illustrates a thought experiment in special relativity. At the top, a horizontal line represents a reference frame. On the left end of this line is a stick figure labeled  $A$ . In the middle of the line is a sun-like symbol representing a light source. On the right end of the line is another stick figure. Above the line, two arrows point away from the central light source towards the left and right figures, each labeled with the letter  $c$ , representing the speed of light. Below the line, the distance from the light source to the left figure is labeled  $\ell'$ , and the distance to the right figure is also labeled  $\ell'$ . Below the right figure, there is another stick figure labeled  $B$ . To the left of figure  $B$ , there is a horizontal arrow pointing to the left, labeled with the letter  $v$ , indicating that observer  $B$  is moving to the left relative to the frame containing  $A$ .

Diagram of a light source between two receivers in frame A, and an observer B moving left relative to frame A.

Fig. 11.4

<sup>15</sup> To go a step further, it’s actually not even necessary for there to exist something that has the same speed in any frame. The theory will still come out the same if we write the first postulate as, “There is a limiting speed of an object in any frame.” (See Section 11.10 for a discussion of this.) There’s no need to have something that actually travels at this speed. It’s conceivable to have a theory that contains no massless objects, so that everything travels slower than this limiting speed.

![Diagram of a light source between two receivers in frame B.](4a71262751de08203180f09784b046cc_img.jpg)

The diagram shows a horizontal line representing a reference frame. At the left end is a stick figure labeled 'A'. At the right end is a stick figure labeled 'B'. In the center of the line is a light source, represented by a sun-like symbol. Two wavy arrows represent light beams traveling from the source towards A and B. Above the line, there are four velocity vectors: a vector 'v' pointing right from A, a vector 'c' pointing left from the source, a vector 'c' pointing right from the source, and a vector 'v' pointing right from B. Below the line, the distance from A to the source is labeled 'l', and the distance from the source to B is also labeled 'l'.

Diagram of a light source between two receivers in frame B.

Fig. 11.5

In  $B$ 's reference frame, the situation looks like that in Fig. 11.5. The receivers (along with everything else in  $A$ 's frame) move to the right at speed  $v$ , and the light travels in both directions at speed  $c$  with respect to  $B$  (not with respect to the light source, as measured in  $B$ 's frame; this is where the speed-of-light postulate comes into play). Therefore, the relative speed (as viewed by  $B$ ) of the light and the left receiver is  $c + v$ , and the relative speed of the light and the right receiver is  $c - v$ .

REMARK: Yes, it's legal to just add and subtract these speeds to obtain the relative speeds *as viewed by  $B$* . If  $v$  equals, say,  $2 \cdot 10^8$  m/s, then in one second the left receiver moves  $2 \cdot 10^8$  m to the right, while the left ray of light moves  $3 \cdot 10^8$  m to the left. This means that they are now  $5 \cdot 10^8$  m closer than they were a second ago. In other words, the relative speed (as measured by  $B$ ) is  $5 \cdot 10^8$  m/s, which is simply  $c + v$ . (Note that this implies that it's perfectly legal for the relative speed of two things, as measured by a third, to take any value up to  $2c$ .) Both the  $v$  and  $c$  here are measured with respect to the *same* person, namely  $B$ , so our intuition works fine. We don't need to use the "velocity-addition formula," which we'll derive in Section 11.5.1, and which is relevant in a different setup. I include this remark here just in case you've seen the velocity-addition formula and think it's relevant in this setup. But if it didn't occur to you, then never mind. ♣

Let  $\ell$  be the distance from the source to the receivers, as measured by  $B$ .<sup>16</sup> Then in  $B$ 's frame, the light hits the left receiver at  $t_l$  and the right receiver at  $t_r$ , where

$$t_l = \frac{\ell}{c + v}, \quad \text{and} \quad t_r = \frac{\ell}{c - v}. \quad (11.5)$$

These are not equal if  $v \neq 0$ . (The one exception is when  $\ell = 0$ , in which case the two events happen at the same place and same time in all frames.) The moral of this exercise is that it makes no sense to say that one event happens at the same time as another, unless you state which frame you're talking about. Simultaneity depends on the frame in which the observations are made.

Of the many effects, miscellaneous,  
 The loss of events, simultaneous,  
 Allows  $B$  to claim  
 There's no pause in  $A$ 's frame,

##### REMARKS:

1. The invariance of the speed of light was used in saying that the two relative speeds above were  $c + v$  and  $c - v$ . If we were talking about baseballs instead of light beams, then the relative speeds wouldn't look like this. If  $v_b$  is the speed at which the baseballs are thrown

<sup>16</sup> We'll see in Section 11.3.3 that  $\ell$  is not equal to  $\ell'$ , due to length contraction. But this won't be important for what we're doing here. The only fact we need for now is that the light source is equidistant from the receivers, as measured by  $B$ . This is true because space is homogeneous, which implies that the length-contraction factor must be the same everywhere. More on this in Section 11.3.3.

- in  $A$ 's frame, then  $B$  sees the balls move at speeds  $v_b - v$  to the left and  $v_b + v$  to the right.<sup>17</sup> These are not equal to  $v_b$ , as they would be in the case of the light beams. The relative speeds between the balls and the left and right receivers are therefore  $(v_b - v) + v = v_b$  and  $(v_b + v) - v = v_b$ . These are equal, so  $B$  sees the balls hit the receivers at the same time, as we know very well from everyday experience.
- It is indeed legal in Eq. (11.5) to obtain the times by simply dividing  $\ell$  by the relative speeds,  $c + v$  and  $c - v$ . But if you want a more formal method, then you can use this reasoning: In  $B$ 's frame, the position of the right photon is given by  $ct$ , and the position of the right receiver (which had a head start of  $\ell$ ) is given by  $\ell + vt$ . Equating these two positions gives  $t_r = \ell/(c - v)$ . Likewise for the left photon.
- There is always a difference between the time an event happens and the time someone *sees* the event happen, because light takes time to travel from the event to the observer. What we calculated above were the times at which the events really happen. If we wanted to, we could calculate the times at which  $B$  *sees* the events occur, but such times are rarely important, and in general we won't be concerned with them. They can easily be calculated by adding on a (distance)/ $c$  time difference for the path of the photons to  $B$ 's eye. Of course, if  $B$  actually did the above experiment to find  $t_r$  and  $t_l$ , she would do it by writing down the times at which she saw the events occur, and then subtracting off the relevant (distance)/ $c$  time differences to find when the events really happened.

To sum up, the  $t_r \neq t_l$  result in Eq. (11.5) is due to the fact that the events truly occur at different times in  $B$ 's frame. *It has nothing to do with the time it takes light to travel to your eye.* In this chapter, we will often use sloppy language and say things like, "What time does  $B$  see event  $Q$  happen?" But we don't really mean, "When do  $B$ 's eyes register that  $Q$  happened?" Instead, we mean, "What time does  $B$  *know* that event  $Q$  happened in her frame?" If we ever want to use "see" in the former sense, we will explicitly say so (as in Section 11.8 on the Doppler effect). ♣

Where this last line is not so extraneous.

**Example (Rear clock ahead):** Two clocks are positioned at the ends of a train of length  $L$  (as measured in its own frame). They are synchronized in the train frame. The train travels past you at speed  $v$ . It turns out that if you observe the clocks at simultaneous times in your frame, you will see the rear clock showing a higher reading than the front clock (see Fig. 11.6). By how much?

**Solution:** As above, let's put a light source on the train, but let's now position it so that the light hits the clocks at the ends of the train at the same time in *your frame*. As above, the relative speeds of the photons and the clocks are  $c + v$  and  $c - v$  (as viewed in your frame). We therefore need to divide the train into lengths in this ratio, in your frame. But since length contraction (discussed in Section 11.3.3) is independent of position, this must also be the ratio in the train frame. So in the train frame, you can quickly show that two numbers that are in this ratio, and that add up to  $L$ , are  $L(c + v)/2c$  and  $L(c - v)/2c$ .

The situation in the train frame therefore looks like that in Fig. 11.7. The light must travel an extra distance of  $L(c + v)/2c - L(c - v)/2c = Lv/c$  to reach the rear clock. The light travels at speed  $c$  (as always), so the extra time is  $Lv/c^2$ . Therefore, the rear

![Diagram of a train moving to the right at speed v. A person stands below the train. Two clocks are at the ends of the train, separated by distance L. The rear clock is on the left and the front clock is on the right.](d091279c3a0abe5fb341989cc49813bd_img.jpg)

Diagram of a train moving to the right at speed v. A person stands below the train. Two clocks are at the ends of the train, separated by distance L. The rear clock is on the left and the front clock is on the right.

Fig. 11.6

![Diagram of the train in its own frame. A light source is at the center. Light waves travel to the left and right. The distance to the rear clock is L(c+v)/2c and the distance to the front clock is L(c-v)/2c.](3a99e394b53dd135de04140c32aa046f_img.jpg)

Diagram of the train in its own frame. A light source is at the center. Light waves travel to the left and right. The distance to the rear clock is L(c+v)/2c and the distance to the front clock is L(c-v)/2c.

Fig. 11.7

<sup>17</sup> The velocity-addition formula in Section 11.5.1 shows that these formulas aren't actually correct. But they're close enough for our purposes here.

clock reads  $Lv/c^2$  more when it is hit by the backward photon, compared with what the front clock reads when it is hit by the forward photon.

Now, let the instant you look at the clocks be the instant the photons hit them (that's why we chose the hittings to be simultaneous in your frame). Then from the previous paragraph, you observe the rear clock reading more than the front clock by an amount,

$$(\text{difference in readings}) = \frac{Lv}{c^2}. \quad (11.6)$$

Note that the  $L$  that appears here is the length of the train in its own frame, and not the shortened length that you observe in your frame (see Section 11.3.3). Appendix G gives a number of other derivations of Eq. (11.6), although they rely on material yet to come in this chapter and Chapter 14.

##### REMARKS:

1. This  $Lv/c^2$  result has nothing to do with the fact that the rear clock takes more time to pass you.
2. The result does *not* say that you see the rear clock ticking at a faster rate than the front clock. They run at the same rate (both have the same time-dilation factor relative to you; see Section 11.3.2). The rear clock is simply a fixed time ahead of the front clock, as seen by you.
3. The fact that the rear clock is *ahead* of the front clock in your frame means that in the train frame the light hits the rear clock *after* it hits the front clock.
4. It's easy to forget which of the clocks is the one that is ahead. But a helpful mnemonic for remembering "rear clock ahead" is that both the first and fourth letters in each word form the same acronym, "rca," which is an anagram for "car," which is sort of like a train. Sure. ♣

![Diagram of a light beam bouncing between a mirror on the ceiling and a source on the floor of a train car. Observer A is standing on the floor. The height of the car is labeled h.](d29ec2f9dcfb1540af0479b9b3532173_img.jpg)

The diagram shows a rectangular box representing a train car. At the top center, there is a horizontal line labeled 'mirror'. At the bottom center, there is a light source symbol (a circle with radiating lines). A vertical line with arrows pointing both up and down connects the light source to the mirror, representing the path of a light beam. On the left side of the box, a stick figure labeled 'A' is standing. To the right of the box, the letter 'h' indicates the height of the car.

Diagram of a light beam bouncing between a mirror on the ceiling and a source on the floor of a train car. Observer A is standing on the floor. The height of the car is labeled h.

Fig. 11.8

#### 11.3.2 Time dilation

We present here the classic example of a light beam traveling vertically on a train. Let there be a light source on the floor of the train and a mirror on the ceiling, which is a height  $h$  above the floor. Let observer  $A$  be at rest on the train, and let observer  $B$  be at rest on the ground. The speed of the train with respect to the ground is  $v$ .<sup>18</sup> A flash of light is emitted. The light travels up to the mirror, bounces off it, and then heads back down. Assume that after the light is emitted, we replace the source with a mirror, so that the light keeps bouncing up and down indefinitely.

In  $A$ 's frame, the train is at rest. The path of the light is shown in Fig. 11.8. It takes the light a time  $h/c$  to reach the ceiling and then a time  $h/c$  to return to

<sup>18</sup> Technically, the words, "with respect to ...," should always be included when talking about speeds, because there is no absolute reference frame, and hence no absolute speed. But in the future, when it's clear what we mean (as in the case of a train moving with respect to the ground), we'll occasionally be sloppy and drop the "with respect to ..."

the floor. The roundtrip time is therefore

$$t_A = \frac{2h}{c}. \quad (11.7)$$

In  $B$ 's frame, the train moves at speed  $v$ . The path of the light is shown in Fig. 11.9. The crucial fact to remember is that the speed of light in  $B$ 's frame is still  $c$ . This means that the light travels along its diagonally upward path at speed  $c$ . (The vertical component of the speed is *not*  $c$ , as would be the case if light behaved like a baseball.) Since the horizontal component of the light's velocity is  $v$ ,<sup>19</sup> the vertical component must be  $\sqrt{c^2 - v^2}$ , as shown in Fig. 11.10.<sup>20</sup> The time it takes to reach the mirror is therefore  $h/\sqrt{c^2 - v^2}$ ,<sup>21</sup> so the roundtrip time is

$$t_B = \frac{2h}{\sqrt{c^2 - v^2}}. \quad (11.8)$$

Dividing Eq. (11.8) by Eq. (11.7) gives

$$t_B = \gamma t_A, \quad (11.9)$$

where

$$\gamma \equiv \frac{1}{\sqrt{1 - v^2/c^2}}. \quad (11.10)$$

This  $\gamma$  factor is ubiquitous in Special Relativity. Note that it is always greater than or equal to 1. This means that the roundtrip time is longer in  $B$ 's frame than in  $A$ 's frame.

What are the implications of this? For concreteness, let  $v/c = 3/5$ , so  $\gamma = 5/4$ . Then we may say the following. If  $A$  is standing next to the light source, and if  $B$  is standing on the ground, and if  $A$  claps his hands at  $t_A = 4$  second intervals, then  $B$  observes claps at  $t_B = 5$  second intervals (after having subtracted off the time for the light to travel to her eye, of course). This is true because both  $A$  and  $B$  must agree on the number of roundtrips the light beam takes between claps. If we assume, for convenience, that a roundtrip takes one second in  $A$ 's frame (yes, that would be a tall train), then the four roundtrips between claps take five seconds in  $B$ 's frame, using Eq. (11.9).

**REMARK:** We just made the claim that both  $A$  and  $B$  must agree on the number of roundtrips between claps. However, since  $A$  and  $B$  disagree on so many things (whether two events are

![Figure 11.9: A diagram showing the path of light in frame B. A horizontal dashed line represents the floor of a train moving to the right at speed v. A stick figure labeled B is on the floor. Above the floor is a horizontal line labeled 'mirror'. Two light sources are on the floor, one on the left and one on the right. Light rays travel from the left source to the mirror and back to the right source. The speed of light is labeled c for both legs of the trip. Arrows indicate the train's motion to the right.](8a0c29fb729836799993d4b5ffac74a1_img.jpg)

Figure 11.9: A diagram showing the path of light in frame B. A horizontal dashed line represents the floor of a train moving to the right at speed v. A stick figure labeled B is on the floor. Above the floor is a horizontal line labeled 'mirror'. Two light sources are on the floor, one on the left and one on the right. Light rays travel from the left source to the mirror and back to the right source. The speed of light is labeled c for both legs of the trip. Arrows indicate the train's motion to the right.

Fig. 11.9

![Figure 11.10: A right triangle diagram illustrating the components of the light's velocity in frame B. The hypotenuse is labeled c. The horizontal base is labeled v. The vertical height is labeled sqrt(c^2 - v^2). A right angle symbol is at the bottom vertex.](d264c08aa65fc8a52f4561d1524bc084_img.jpg)

Figure 11.10: A right triangle diagram illustrating the components of the light's velocity in frame B. The hypotenuse is labeled c. The horizontal base is labeled v. The vertical height is labeled sqrt(c^2 - v^2). A right angle symbol is at the bottom vertex.

Fig. 11.10

<sup>19</sup> Yes, it's still  $v$ . The light is always located on the vertical line between the source and the mirror. Since both of these objects move horizontally at speed  $v$ , the light does also.

<sup>20</sup> The Pythagorean theorem is indeed valid here. It's valid for distances, and since speeds are just distances divided by time, it's valid also for speeds.

<sup>21</sup> We've assumed that the height of the train in  $B$ 's frame is still  $h$ . Although we'll see in Section 11.3.3 that there is length contraction along the direction of motion, there is none in the direction perpendicular to the motion (see Problem 11.1).

simultaneous, the rate at which clocks tick, and the length of things, as we'll see below), you might be wondering if there's *anything* they agree on. Yes, there are still frame-independent statements we can hang on to. If a bucket of paint flies past you and dumps paint on your head, then everyone agrees that you are covered in paint. Likewise, if  $A$  is standing next to the light clock and claps when the light reaches the floor, then everyone agrees on this. If the light is actually a strong laser pulse, and if  $A$ 's clapping motion happens to bring his hands right over the mirror when the pulse gets there, then everyone agrees that his hands get burned by the laser. ♣

What if we have a train that doesn't contain one of our special light clocks? It doesn't matter. We *could* have built one if we wanted to, so the same results concerning the claps must hold. Therefore, light clock or no light clock,  $B$  observes  $A$  moving strangely slowly. From  $B$ 's point of view,  $A$ 's heart beats slowly, his blinks are lethargic, and his sips of coffee are slow enough to suggest that he needs another cup.

The effects of dilation of time  
 Are magical, strange, and sublime.  
 In your frame, this verse,  
 Which you'll see is not terse,  
 Can be read in the same amount of time it takes someone  
 else in another frame to read a similar sort of rhyme.

Our assumption that  $A$  is at rest on the train was critical in the above derivation. If  $A$  is moving with respect to the train, then Eq. (11.9) doesn't hold, because we *cannot* say that both  $A$  and  $B$  must agree on the number of roundtrips the light beam takes between claps, because of the problem with simultaneity. More precisely, if  $A$  is at rest on the train right next to the light source, then there are no issues with simultaneity, because the distance  $L$  in Eq. (11.6) is zero. And if  $A$  is at rest at a fixed distance from the source, then consider a person  $A'$  at rest on the train right next to the source. The distance  $L$  between  $A$  and  $A'$  is nonzero, so from the loss of simultaneity,  $B$  sees their two clocks read different times. But this difference is constant, so  $B$  sees  $A$ 's clock tick at the same rate as  $A'$ 's clock. Equivalently, we can just build a second light clock in a little box and have  $A$  hold it, and it will have the same speed  $v$  (and thus yield the same  $\gamma$  factor) as the first clock.

However, if  $A$  is moving with respect to the train, then we have a problem. If  $A'$  is again at rest next to the source, then the distance  $L$  between  $A$  and  $A'$  is changing, so  $B$  can't use the reasoning in the previous paragraph to conclude that  $A$ 's and  $A'$ 's clocks tick at the same rate. And in fact they do not, because as above, we can build another light clock and have  $A$  hold it. In this case,  $A$ 's speed is what goes into the  $\gamma$  factor in Eq. (11.10), but this is different from  $A'$ 's speed (which is the speed of the train).

##### REMARKS:

1. The time dilation result derived in Eq. (11.9) is a bit strange, no doubt, but there doesn't seem to be anything downright incorrect about it until we look at the situation from  $A$ 's

point of view.  $A$  sees  $B$  flying by at a speed  $v$  in the other direction. The ground is no more fundamental than a train, so the same reasoning applies. The time dilation factor,  $\gamma$ , doesn't depend on the sign of  $v$ , so  $A$  sees the same time dilation factor that  $B$  sees. That is,  $A$  sees  $B$ 's clock running slow. But how can this be? Are we claiming that  $A$ 's clock is slower than  $B$ 's, and also that  $B$ 's clock is slower than  $A$ 's? Well . . . yes and no.

Remember that the above time-dilation reasoning applies only to a situation where something is motionless in the appropriate frame. In the second situation (where  $A$  sees  $B$  flying by), the statement  $t_A = \gamma t_B$  holds only when the two events (say, two ticks on  $B$ 's clock) happen at the same place in  $B$ 's frame. But for two such events, they are certainly not in the same place in  $A$ 's frame, so the  $t_B = \gamma t_A$  result in Eq. (11.9) does *not* hold. The conditions of being motionless in each frame never both hold for a given setup (unless  $v = 0$ , in which case  $\gamma = 1$  and  $t_A = t_B$ ). So, the answer to the question at the end of the previous paragraph is “yes” if you ask the questions in the appropriate frames, and “no” if you think the answer should be frame independent.

2. Concerning the fact that  $A$  sees  $B$ 's clock run slow, and  $B$  sees  $A$ 's clock run slow, consider the following statement. “This is a contradiction. It is essentially the same as saying, ‘I have two apples on a table. The left one is bigger than the right one, and the right one is bigger than the left one.’” How would you respond to this? Well, it is not a contradiction. Observers  $A$  and  $B$  are using *different coordinates* to measure time. The times measured in each of their frames are quite different things. The seemingly contradictory time-dilation result is really no stranger than having two people run away from each other into the distance, and having them both say that the other person looks smaller. In short, we are not comparing apples and apples. We are comparing apples and oranges. A more correct analogy would be the following. An apple and an orange sit on a table. The apple says to the orange, “You are a much uglier apple than I am,” and the orange says to the apple, “You are a much uglier orange than I am.”
3. One might view the statement, “ $A$  sees  $B$ 's clock running slow, and also  $B$  sees  $A$ 's clock running slow,” as somewhat unsettling. But in fact it would be a complete disaster for the theory if  $A$  and  $B$  viewed each other in different ways. A critical fact in the theory of relativity is that  $A$  sees  $B$  in exactly the same way as  $B$  sees  $A$ .
4. In everything we've done so far, we've assumed that  $A$  and  $B$  are in inertial frames, because these are the frames that the postulates of Special Relativity deal with. However, it turns out that the time dilation result in Eq. (11.9) holds even if  $A$  is accelerating, as long as  $B$  isn't. In other words, if you're looking at a clock that is undergoing a complicated accelerating motion, then to figure out how fast it's ticking in your frame, all you need to know is its speed at any instant; its acceleration is irrelevant (this has plenty of experimental verification). If, however, *you* are accelerating, then all bets are off, and it's not valid for you to use the time dilation result when looking at a clock. It's still possible to get a handle on such situations, but we'll wait until Chapter 14 to do so. ♣

**Example (Twin paradox):** Twin  $A$  stays on the earth, while twin  $B$  flies quickly to a distant star and back (see Fig. 11.11). Show that  $B$  is younger than  $A$  when they meet up again.

**Solution:** From  $A$ 's point of view,  $B$ 's clock is running slow by a factor  $\gamma$ , on both the outward and return parts of the trip. Therefore,  $B$  is younger than  $A$  when they meet up again. This is the answer, and that's that. So if getting the right answer is all we care about, then we can pack up and go home. But our reasoning leaves one large point unaddressed. The “paradox” part of this example's title comes from the following alternate reasoning. Someone might say that in  $B$ 's frame,  $A$ 's clock is running slow by a factor  $\gamma$ , and so  $A$  is younger than  $B$  when they meet up again.

![Diagram of the Twin Paradox. A circle labeled 'A' and 'earth' is on the left. A star is on the right. A horizontal line with arrows at both ends connects them. Above the line, 'A' is positioned over the circle and 'B' is positioned over the star. The line represents the path of twin B from Earth to the star and back.](94760bb9a17146875afaf9d1cf6a8631_img.jpg)

Diagram of the Twin Paradox. A circle labeled 'A' and 'earth' is on the left. A star is on the right. A horizontal line with arrows at both ends connects them. Above the line, 'A' is positioned over the circle and 'B' is positioned over the star. The line represents the path of twin B from Earth to the star and back.

Fig. 11.11

It's definitely true that when the two twins are standing next to each other (that is, when they are in the same frame), we can't have both  $B$  younger than  $A$ , and  $A$  younger than  $B$ . So what is wrong with the reasoning at the end of the previous paragraph? The error lies in the fact that there is no "one frame" that  $B$  is in. The inertial frame for the outward trip is different from the inertial frame for the return trip. The derivation of our time-dilation result applies only to one inertial frame.

Said in a different way,  $B$  accelerates when she turns around, and our time-dilation result holds only from the point of view of an *inertial* observer.<sup>22</sup> The symmetry in the problem is broken by the acceleration. If both  $A$  and  $B$  are blindfolded, they can still tell who is doing the traveling, because  $B$  will feel the acceleration at the turnaround. Constant velocity cannot be felt, but acceleration can be. (However, see Chapter 14 on General Relativity. Gravity complicates things.)

The above paragraphs show what is wrong with the " $A$  is younger" reasoning, but they don't show how to modify it quantitatively to obtain the correct answer. There are many different ways of doing this, and you can tackle some of them in the problems (Exercise 11.67, Problems 11.2, 11.19, 11.24, and various problems in Chapter 14). Also, Appendix H gives a list of all the possible resolutions to the twin paradox that I can think of.

---

**Example (Muon decay):** Elementary particles called *muons* (which are identical to electrons, except that they are about 200 times as massive) are created in the upper atmosphere when cosmic rays collide with air molecules. The muons have an average lifetime of about  $2 \cdot 10^{-6}$  seconds<sup>23</sup> (then they decay into electrons and neutrinos), and move at nearly the speed of light. Assume for simplicity that a certain muon is created at a height of 50 km, moves straight downward, has a speed  $v = 0.99998c$ , decays in exactly  $T = 2 \cdot 10^{-6}$  seconds, and doesn't collide with anything on the way down.<sup>24</sup> Will the muon reach the earth before it (the muon!) decays?

**Solution:** The naive thing to say is that the distance traveled by the muon is  $d = vT \approx (3 \cdot 10^8 \text{ m/s})(2 \cdot 10^{-6} \text{ s}) = 600 \text{ m}$ , and that this is less than 50 km, so the muon doesn't reach the earth. This reasoning is incorrect, because of the time-dilation effect. The muon lives longer in the earth frame, by a factor of  $\gamma$ , which is  $\gamma = 1/\sqrt{1 - v^2/c^2} \approx 160$  here. The correct distance traveled in the earth frame is therefore  $v(\gamma T) \approx 100 \text{ km}$ . Hence, the muon travels the 50 km, with room to spare. The real-life fact that we actually do detect muons reaching the surface of the earth in the predicted abundances (while the naive  $d = vT$  reasoning would predict that

<sup>22</sup> For the entire outward and return parts of the trip,  $B$  *does* observe  $A$ 's clock running slow, but enough strangeness occurs during the turning-around period to make  $A$  end up older. Note, however, that a discussion of acceleration is not required to quantitatively understand the paradox, as Problem 11.2 shows.

<sup>23</sup> This is the "proper" lifetime, that is, the lifetime as measured in the frame of the muon.

<sup>24</sup> In the real world, the muons are created at various heights, move in different directions, have different speeds, decay in lifetimes that vary according to a standard half-life formula, and may very well bump into air molecules. So technically we've got everything wrong here. But that's no matter. This example will work just fine for the present purpose.

we shouldn't see any) is one of the many experimental tests that support the relativity theory.

#### 11.3.3 Length contraction

Consider the following setup. Person  $A$  stands on a train which he measures to have length  $\ell'$ , and person  $B$  stands on the ground. The train moves at speed  $v$  with respect to the ground. A light source is located at the back of the train, and a mirror is located at the front. The source emits a flash of light that heads to the mirror, bounces off, then heads back to the source. By looking at how long this process takes in the two reference frames, we can determine the length of the train as measured by  $B$ .<sup>25</sup> In  $A$ 's frame (see Fig. 11.12), the roundtrip time for the light is simply

$$t_A = \frac{2\ell'}{c}. \quad (11.11)$$

Things are a little more complicated in  $B$ 's frame (see Fig. 11.13). Let the length of the train, as measured by  $B$ , be  $\ell$ . For all we know at this point,  $\ell$  may equal  $\ell'$ , but we'll soon find that it does not. The relative speed (as measured by  $B$ ) of the light and the mirror during the first part of the trip is  $c - v$ . The relative speed during the second part is  $c + v$ . During each part, the light must close a gap with initial length  $\ell$ . Therefore, the total roundtrip time is

$$t_B = \frac{\ell}{c-v} + \frac{\ell}{c+v} = \frac{2\ell c}{c^2-v^2} \equiv \frac{2\ell}{c} \gamma^2. \quad (11.12)$$

But we know from Eq. (11.9) that

$$t_B = \gamma t_A. \quad (11.13)$$

This is a valid statement, because the two events we are concerned with (light leaving back, and light returning to back) happen at the same place in the train frame, so it's legal to use the time-dilation result in Eq. (11.9). Substituting the results for  $t_A$  and  $t_B$  from Eqs. (11.11) and (11.12) into Eq. (11.13), we find

$$\ell = \frac{\ell'}{\gamma}. \quad (11.14)$$

Note that we could not have used this setup to find the length contraction if we had not already found the time dilation in Eq. (11.9).

<sup>25</sup> The third remark below gives another (quicker) derivation of length contraction. But we'll go through the present derivation because the calculation is instructive.

![Diagram of Fig. 11.12: A's frame. A rectangular box represents a train of length l'. A person A is standing inside. A light source (sun icon) is at the back, and a mirror is at the front. An arrow shows light traveling from the source to the mirror, and another arrow shows it returning to the source.](7afe9d4fafea456a6ce6d6d078b521e2_img.jpg)

Diagram of Fig. 11.12: A's frame. A rectangular box represents a train of length l'. A person A is standing inside. A light source (sun icon) is at the back, and a mirror is at the front. An arrow shows light traveling from the source to the mirror, and another arrow shows it returning to the source.

Fig. 11.12

![Diagram of Fig. 11.13: B's frame. A rectangular box represents a train of length l moving to the right at speed v. The diagram is divided into three stages: (start) shows the light source at the back; (later) shows the light wave (wavy line) moving right at speed c towards the front mirror; (finish) shows the light wave after reflecting off the mirror and moving left at speed c back towards the source.](d933ef52e1fdcf7635a7750c152191df_img.jpg)

Diagram of Fig. 11.13: B's frame. A rectangular box represents a train of length l moving to the right at speed v. The diagram is divided into three stages: (start) shows the light source at the back; (later) shows the light wave (wavy line) moving right at speed c towards the front mirror; (finish) shows the light wave after reflecting off the mirror and moving left at speed c back towards the source.

Fig. 11.13

Since  $\gamma \geq 1$ , we see that  $B$  measures the train to be shorter than  $A$  measures. The term *proper length* is used to describe the length of an object in its rest frame. So  $\ell'$  is the proper length of the above train, and the length in any other frame is less than or equal to  $\ell'$ . This length contraction is often called the *Lorentz–FitzGerald contraction*, for the reason given in Footnote 10.

Relativistic limericks have the attraction  
Of being shrunk by a Lorentz contraction.  
But for readers, unwary,  
The results may be scary,  
When a fraction ...

##### REMARKS:

1. The length-contraction result in Eq. (11.14) is for lengths along the direction of the relative velocity. There is no length contraction in the perpendicular direction, as shown in Problem 11.1.
2. As with time dilation, this length contraction is a bit strange, but there doesn't seem to be anything actually paradoxical about it, until we look at things from  $A$ 's point of view. To make a nice symmetrical situation, let's say  $B$  is standing on an identical train, which is motionless with respect to the ground.  $A$  sees  $B$  flying by at speed  $v$  in the other direction. Neither train is any more fundamental than the other, so the same reasoning applies, and  $A$  sees the same length contraction factor that  $B$  sees. That is,  $A$  measures  $B$ 's train to be short. But how can this be? Are we claiming that  $A$ 's train is shorter than  $B$ 's, and also that  $B$ 's train is shorter than  $A$ 's? Is the actual setup the one shown in Fig. 11.14, or is it the one shown in Fig. 11.15? Which does it really look like? Well ... it depends.

![Diagram Fig. 11.14: Two horizontal rectangles representing trains. The top rectangle is labeled 'A' and has a velocity vector 'v' pointing to the right above it. The bottom rectangle is labeled 'B' and is longer than rectangle A.](e57b1e5bb1481370156ea4c0b8c01260_img.jpg)

Diagram Fig. 11.14: Two horizontal rectangles representing trains. The top rectangle is labeled 'A' and has a velocity vector 'v' pointing to the right above it. The bottom rectangle is labeled 'B' and is longer than rectangle A.

Fig. 11.14

![Diagram Fig. 11.15: Two horizontal rectangles representing trains. The top rectangle is labeled 'A' and is longer than rectangle B. The bottom rectangle is labeled 'B' and has a velocity vector 'v' pointing to the left below it.](8c413f5dbcb2f83c9b1576dd1c2349dc_img.jpg)

Diagram Fig. 11.15: Two horizontal rectangles representing trains. The top rectangle is labeled 'A' and is longer than rectangle B. The bottom rectangle is labeled 'B' and has a velocity vector 'v' pointing to the left below it.

Fig. 11.15

The word “is” in the above paragraph is a very bad word to use and is generally the cause of all the confusion (but it is ok in this paragraph, thankfully). There is no such thing as “is-ness” when it comes to lengths. It makes no sense to say what the length of the train really *is*. It makes sense only to say what the length is in a given frame. The situation doesn't really *look like* one thing in particular. The look depends on the frame in which the looking is being done.

Let's be a little more specific. How do you measure a length? You write down the coordinates of the ends of something *measured simultaneously*, and then you take the difference. But the word “simultaneous” here should send up all sorts of red flags. Simultaneous events in one frame are not simultaneous events in another. Stated more precisely, here is what we are claiming: Let  $B$  write down simultaneous coordinates of the ends of  $A$ 's train, and also simultaneous coordinates of the ends of her own train. Then the difference between the former is smaller than the difference between the latter. Likewise, let  $A$  write down simultaneous coordinates of the ends of  $B$ 's train, and also simultaneous coordinates of the ends of his own train. Then the difference between the former is smaller than the difference between the latter. There is no contradiction here, because the times at which  $A$  and  $B$  are writing down the coordinates don't have much to do with each other, due to the loss of simultaneity. You can be quantitative about this in Problem 11.3. As with time dilation, we are comparing apples and oranges.

3. There is an easy argument to show that time dilation implies length contraction, and vice versa. Let  $B$  stand on the ground, next to a stick of length  $\ell$ . Let  $A$  fly past the stick at speed  $v$ . In  $B$ 's frame, it takes  $A$  a time of  $\ell/v$  to traverse the length of the stick. Therefore (assuming that we have demonstrated the time-dilation result), a watch on  $A$ 's wrist will advance by a time of only  $\ell/\gamma v$  while he traverses the length of the stick.

How does  $A$  view the situation? He sees the ground and the stick fly by at speed  $v$ . The time between the two ends passing him is  $\ell/\gamma v$  (because that is the time elapsed on his watch). To get the length of the stick in his frame, he simply multiplies the speed by the time. That is, he measures the length to be  $(\ell/\gamma v)v = \ell/\gamma$ , which is the desired contraction. The same argument also shows that length contraction implies time dilation.

4. As mentioned earlier, the length contraction factor  $\gamma$  is independent of position on the object. That is, all parts of the train are contracted by the same amount. This follows from the fact that all points in space are equivalent. Equivalently, we could put a large number of small replicas of the above source–mirror system along the length of the train. They would all produce the same value for  $\gamma$ , independent of the position on the train.
5. If you still want to ask, “Is the contraction really *real*?” then consider the following hypothetical undertaking. Imagine a sheet of paper moving sideways past the Mona Lisa, skimming the surface. A standard sheet of paper is plenty large enough to cover her face, so if the paper is moving slowly, and if you take a photograph at the appropriate time, then in the photo you’ll see her entire face covered by the paper. However, if the sheet is flying by sufficiently fast, and if you take a photograph at the appropriate time, then in the photo you’ll see a thin vertical strip of paper covering only a small fraction of her face. So you’ll still see her smiling at you. ♣

**Example (Passing trains):** Two trains,  $A$  and  $B$ , each have proper length  $L$  and move in the same direction.  $A$ ’s speed is  $4c/5$ , and  $B$ ’s speed is  $3c/5$ .  $A$  starts behind  $B$  (see Fig. 11.16). How long, as viewed by person  $C$  on the ground, does it take for  $A$  to overtake  $B$ ? By this we mean the time between the front of  $A$  passing the back of  $B$ , and the back of  $A$  passing the front of  $B$ .

**Solution:** Relative to  $C$  on the ground, the  $\gamma$  factors associated with  $A$  and  $B$  are  $5/3$  and  $5/4$ , respectively. Therefore, their lengths in the ground frame are  $3L/5$  and  $4L/5$ . While overtaking  $B$ ,  $A$  must travel farther than  $B$ , by an excess distance equal to the sum of the lengths of the trains, which is  $7L/5$ . The relative speed of the two trains (as viewed by  $C$  on the ground) is the difference of the speeds, which is  $c/5$ . The total time is therefore

$$t_C = \frac{7L/5}{c/5} = \frac{7L}{c}. \quad (11.15)$$

![Diagram showing two trains, A and B, moving to the right. Train A is behind train B. The speed of train A is 4c/5 and the speed of train B is 3c/5. An observer C is on the ground below the trains.](3a49168594fe4d0440820476ca61e931_img.jpg)

The diagram illustrates the 'Passing trains' example. It shows two rectangular blocks representing trains, labeled 'A' and 'B'. Train A is positioned behind train B. Both trains have arrows pointing to the right, indicating their direction of motion. Above train A, the speed is labeled as  $4c/5$ . Above train B, the speed is labeled as  $3c/5$ . Below the trains, there is a stick figure representing an observer labeled 'C'.

Diagram showing two trains, A and B, moving to the right. Train A is behind train B. The speed of train A is 4c/5 and the speed of train B is 3c/5. An observer C is on the ground below the trains.

Fig. 11.16

**Example (Muon decay, again):** Consider the “Muon decay” example from Section 11.3.2. From the muon’s point of view, it lives for a time of  $T = 2 \cdot 10^{-6}$  seconds, and the earth is speeding toward it at  $v = 0.99998c$ . How, then, does the earth (which travels only  $d = vT \approx 600$  m before the muon decays) reach the muon?

**Solution:** The important point here is that in the muon’s frame, the distance to the earth is contracted by a factor  $\gamma \approx 160$ . Therefore, the earth starts only  $50 \text{ km}/160 \approx 300$  m away. Since the earth can travel a distance of 600 m during the muon’s lifetime, the earth collides with the muon, with time to spare.

As stated in the third remark above, time dilation and length contraction are intimately related. We can’t have one without the other. In the earth’s frame, the muon’s

arrival on the earth is explained by time dilation. In the muon's frame, it is explained by length contraction.

Observe that for muons created,  
 The dilation of time is related  
 To Einstein's insistence  
 Of shrunken-down distance  
 In the frame where decays aren't belated.

---

An extremely important strategy in solving relativity problems is to plant yourself in a frame and *stay there*. The only thoughts running through your head should be what *you* observe. That is, don't try to use reasoning along the lines of, "Well, the person I'm looking at in this other frame sees such-and-such." This will almost certainly cause an error somewhere along the way, because you will inevitably end up writing down an equation that combines quantities that are measured in different frames, which is a no-no. Of course, you might want to solve another part of the problem by working in another frame, or you might want to redo the whole problem in another frame. That's fine, but once you decide which frame you're going to use, make sure you put yourself there and stay there.

Another very important strategy is to draw a picture of the setup (in whatever frame you've chosen) at every moment when something significant happens, as we did in Fig. 11.13. Once we drew the pictures there, it was clear what we needed to do. But without the pictures, we almost certainly would have gotten confused.

At this point you might want to look at the "Qualitative relativity questions" in Appendix F, just to make sure we're all on the same page. Some of the questions deal with material we haven't covered yet, but most are relevant to what we've done so far.

This concludes our treatment of the three fundamental effects. In the next section, we'll combine all the information we've gained and use it to derive the Lorentz transformations. But one last comment before we get to those:

##### *Lattice of clocks and meter sticks*

In everything we've done so far, we've taken the route of having observers sitting in various frames, making various measurements. But as mentioned earlier, this can cause some ambiguity, because you might think that the time when light reaches the observer is important, whereas what we are generally concerned with is the time when something actually happens.

A way to avoid this ambiguity is to remove the observers and then imagine filling up space with a large rigid lattice of meter sticks and synchronized

clocks. Different frames are defined by different lattices; assume that the lattices of different frames can somehow pass freely through each other. All the meter sticks in a given frame are at rest with respect to all the others, so we don't have to worry about issues of length contraction within each frame. But the lattice of a frame moving past you is squashed in the direction of motion, because all the meter sticks in that direction are contracted.

To measure the length of an object in a given frame, we just need to determine where the ends are (at simultaneous times, as measured in that frame) with respect to the lattice. As far as the synchronization of the clocks within each frame goes, this can be accomplished by putting a light source midway between any two clocks and sending out signals, and then setting the clocks to a certain value when the signals hit them. Alternatively, a more straightforward method of synchronization is to start with all the clocks synchronized right next to each other, and then move them very slowly to their final positions. Any time-dilation effects can be made arbitrarily small by moving the clocks sufficiently slowly. This is true because the time-dilation  $\gamma$  factor is second order in  $v$ , but the time it takes a clock to reach its final position is only first order in  $1/v$ .

This lattice way of looking at things emphasizes that observers are not important, and that a frame is defined simply as a lattice of space and time coordinates. Anything that happens (an “event”) is automatically assigned a space and time coordinate in every frame, independent of any observer. The concept of an “event” will be very important in the next section.

### 11.4 The Lorentz transformations

#### 11.4.1 The derivation

Consider a coordinate system,  $S'$ , moving relative to another system,  $S$  (see Fig. 11.17). Let the constant relative speed of the frames be  $v$ . Let the corresponding axes of  $S$  and  $S'$  point in the same direction, and let the origin of  $S'$  move along the  $x$  axis of  $S$ , in the positive direction. Nothing exciting happens in the  $y$  and  $z$  directions (see Problem 11.1), so we'll ignore them.

Our goal in this section is to look at two events (an event is anything that has space and time coordinates) in spacetime and relate the  $\Delta x$  and  $\Delta t$  of the coordinates in one frame to the  $\Delta x'$  and  $\Delta t'$  of the coordinates in another. We therefore want to find the constants  $A$ ,  $B$ ,  $C$ , and  $D$  in the relations,

$$\begin{aligned}\Delta x &= A \Delta x' + B \Delta t', \\ \Delta t &= C \Delta t' + D \Delta x'.\end{aligned}\tag{11.16}$$

The four constants here will end up depending on  $v$  (which is constant, given the two inertial frames). But we won't explicitly write this dependence, for ease of notation.

![Diagram showing two coordinate systems, S and S', in a 3D perspective. System S has axes x, y, and z. System S' has axes x', y', and z'. The origin of S' is shown moving along the positive x-axis of S with a velocity vector v pointing to the right. The y and z axes are shown as lines receding into the background.](9487733fdfcb6a8708483f1f40a7e1bd_img.jpg)

Diagram showing two coordinate systems, S and S', in a 3D perspective. System S has axes x, y, and z. System S' has axes x', y', and z'. The origin of S' is shown moving along the positive x-axis of S with a velocity vector v pointing to the right. The y and z axes are shown as lines receding into the background.

Fig. 11.17

##### REMARKS:

1. We have assumed in Eq. (11.16) that  $\Delta x$  and  $\Delta t$  are linear functions of  $\Delta x'$  and  $\Delta t'$ . And we have also assumed that  $A$ ,  $B$ ,  $C$ , and  $D$  are constants, that is, they depend at most on  $v$ , and not on  $x$ ,  $t$ ,  $x'$ ,  $t'$ .

The first of these assumptions is justified by the fact that any finite interval can be built up from a series of many infinitesimal ones. But for an infinitesimal interval, any terms such as  $(\Delta t')^2$ , for example, are negligible compared with the linear terms. Therefore, if we add up all the infinitesimal intervals to obtain a finite one, we will be left with only the linear terms. Equivalently, it shouldn't matter whether we make a measurement with, say, meter sticks or half-meter sticks.

The second assumption can be justified in various ways. One is that all inertial frames should agree on what “nonaccelerating” motion is. That is, if  $\Delta x' = u' \Delta t'$ , then we should also have  $\Delta x = u \Delta t$ , for some constant  $u$ . This is true only if the above coefficients are constants, as you can check. Another justification comes from the second of our two relativity postulates, which says that all points in (empty) space are indistinguishable. With this in mind, let's assume that we have a transformation of the form, say,  $\Delta x = A \Delta x' + B \Delta t' + Ex' \Delta x'$ . The  $x'$  in the last term implies that the absolute location in spacetime (and not just the relative position) is important. Therefore, this last term cannot exist.

2. If the relations in Eq. (11.16) turned out to be the usual Galilean transformations (which are the ones that hold for everyday relative speeds  $v$ ) then we would have  $\Delta x = \Delta x' + v \Delta t$ , and  $\Delta t = \Delta t'$  (that is,  $A = C = 1$ ,  $B = v$ , and  $D = 0$ ). We will find, however, that under the assumptions of Special Relativity, this is *not* the case. The Galilean transformations are not the correct transformations. But we will show below that the correct transformations do indeed reduce to the Galilean transformations in the limit of slow speeds, as they must. ♣

The constants  $A$ ,  $B$ ,  $C$ , and  $D$  in Eq. (11.16) are four unknowns, and we can solve for them by using four facts we found above in Section 11.3. The four facts we will use are:

|   | Effect                 | Condition | Result          | Eq. in text |
|---|------------------------|-----------|-----------------|-------------|
| 1 | Time dilation          | $x' = 0$  | $t = \gamma t'$ | (11.9)      |
| 2 | Length contraction     | $t' = 0$  | $x' = x/\gamma$ | (11.14)     |
| 3 | Relative $v$ of frames | $x = 0$   | $x' = -vt'$     |             |
| 4 | Rear clock ahead       | $t = 0$   | $t' = -vx'/c^2$ | (11.6)      |

We have taken the liberty of dropping the  $\Delta$ 's in front of the coordinates, lest things get too messy. We will often omit the  $\Delta$ 's, but it should be understood that  $x$  really means  $\Delta x$ , etc. We are always concerned with the *difference* between coordinates of two events in spacetime. The actual value of any coordinate is irrelevant, because there is no preferred origin in any frame.

You should pause for a moment and verify that the four “results” in the above table are in fact the proper mathematical expressions for the four effects, given the stated “conditions.”<sup>26</sup> My advice is to keep pausing until you're comfortable

<sup>26</sup> We can state the effects in other ways too, by switching the primes and unprimes. For example, time dilation can be written as “ $t' = \gamma t$  when  $x = 0$ .” But we've chosen the above ways of writing things because they will allow us to solve for the four unknowns in the most efficient way.

with all the entries in the table. Note that the sign in the “rear clock ahead” effect is indeed correct, because the front clock shows less time than the rear clock. So the clock with the higher  $x'$  value is the one with the lower  $t'$  value.

We can now use our four facts in the above table to quickly solve for the unknowns  $A$ ,  $B$ ,  $C$ , and  $D$  in Eq. (11.16).

Fact (1) gives  $C = \gamma$ .

Fact (2) gives  $A = \gamma$ .

Fact (3) gives  $B/A = v \implies B = \gamma v$ .

Fact (4) gives  $D/C = v/c^2 \implies D = \gamma v/c^2$ .

Equations (11.16), which are known as the *Lorentz transformations*, are therefore given by

$$\begin{aligned}\Delta x &= \gamma(\Delta x' + v \Delta t'), \\ \Delta t &= \gamma(\Delta t' + v \Delta x'/c^2), \\ \Delta y &= \Delta y', \\ \Delta z &= \Delta z',\end{aligned}\tag{11.17}$$

where

$$\gamma \equiv \frac{1}{\sqrt{1 - v^2/c^2}}.\tag{11.18}$$

We have tacked on the trivial transformations for  $y$  and  $z$ , but we won't bother writing these in the future. Also, we'll drop the  $\Delta$ 's from now on, but remember that they're always really there.

If we solve for  $x'$  and  $t'$  in terms of  $x$  and  $t$  in Eq. (11.17), then we see that the inverse Lorentz transformations are given by

$$\begin{aligned}x' &= \gamma(x - vt), \\ t' &= \gamma(t - vx/c^2).\end{aligned}\tag{11.19}$$

Of course, which ones you label as the “inverse” transformations depends on your point of view. But it's intuitively clear that the only difference between the two sets of equations is the sign of  $v$ , because  $S$  is simply moving backward with respect to  $S'$ .

The reason why the derivation of Eqs. (11.17) was so quick is that we already did most of the work in Section 11.3 when we derived the fundamental effects. If we wanted to derive the Lorentz transformations from scratch, that is, by starting with the two postulates in Section 11.2, then the derivation would be longer. In Appendix I we give such a derivation, where it is clear what information comes from each of the postulates. The procedure there is somewhat cumbersome, but it's worth taking a look at, because we will invoke the result in a very cool way in Section 11.10.

##### REMARKS:

1. In the limit  $v \ll c$  (or more precisely, in the limit  $vx'/c^2 \ll t'$ , which means that even if  $v$  is small, we have to be careful that  $x'$  isn't too large), Eqs. (11.17) reduce to  $x = x' + vt$  and  $t = t'$ , which are the good old Galilean transformations. This must be the case, because we know from everyday experience (where  $v \ll c$ ) that the Galilean transformations work just fine.
2. Equations (11.17) exhibit a nice symmetry between  $x$  and  $ct$ . With  $\beta \equiv v/c$ , we have

$$\begin{aligned} x &= \gamma(x' + \beta ct'), \\ ct &= \gamma(ct' + \beta x'). \end{aligned} \quad (11.20)$$

Equivalently, in units where  $c = 1$  (for example, where one unit of distance equals  $3 \cdot 10^8$  meters, or where one unit of time equals  $1/(3 \cdot 10^8)$  seconds), Eqs. (11.17) take the symmetric form,

$$\begin{aligned} x &= \gamma(x' + vt'), \\ t &= \gamma(t' + vx'). \end{aligned} \quad (11.21)$$

3. In matrix form, Eq. (11.20) can be written as

$$\begin{pmatrix} x \\ ct \end{pmatrix} = \begin{pmatrix} \gamma & \gamma\beta \\ \gamma\beta & \gamma \end{pmatrix} \begin{pmatrix} x' \\ ct' \end{pmatrix}. \quad (11.22)$$

This looks similar to a rotation matrix. More about this in Section 11.9, and in Problem 11.27.

4. We did the above derivation in terms of a primed and an unprimed system. But when you're doing problems, it's usually best to label your coordinates with subscripts such as A for Alice, or T for train. In addition to being more informative, this notation is less likely to make you think that one frame is more fundamental than the other.
5. It's easy to get confused about the sign on the right-hand side of the Lorentz transformations. To figure out if it should be a plus or a minus, write down  $x_A = \gamma(x_B \pm vt_B)$ , and then imagine sitting in system A and looking at a fixed point in B. This fixed point satisfies (putting the  $\Delta$ 's back in to avoid any mixup)  $\Delta x_B = 0$ , which gives  $\Delta x_A = \pm \gamma v \Delta t_B$ . So if the point moves to the right (that is, if it increases as time increases), then pick the "+." And if it moves to the left, then pick the "-." In other words, the sign is determined by which way A (the person associated with the coordinates on the left-hand side of the equation) sees B (ditto for the right-hand side) moving.
6. One very important thing we must check is that two successive Lorentz transformations (from  $S_1$  to  $S_2$  and then from  $S_2$  to  $S_3$ ) again yield a Lorentz transformation (from  $S_1$  to  $S_3$ ). This must be true because we showed that any two frames must be related by Eqs. (11.17). If we composed two L.T.'s (along the same direction) and found that the transformation from  $S_1$  to  $S_3$  was not of the form of Eqs. (11.17), for some new  $v$ , then the whole theory would be inconsistent, and we would have to drop one of our postulates.<sup>27</sup> You can show that the combination of an L.T. (with speed  $v_1$ ) and an L.T. (with speed  $v_2$ ) does indeed yield an L.T., and it has speed  $(v_1 + v_2)/(1 + v_1 v_2/c^2)$ . This is the task of Exercise 11.47, and also Problem 11.27 (which is stated in terms of *rapidity*, introduced

<sup>27</sup> This statement is true only for the composition of two L.T.'s in the *same* direction. If we composed an L.T. in the  $x$  direction with one in the  $y$  direction, the result would interestingly *not* be an L.T. along some new direction, but rather the composition of an L.T. along some direction and a rotation through some angle. This rotation results in what is known as the *Thomas precession*. See the appendix of Muller (1992) for a quick derivation of the Thomas precession. For further discussion, see Costella *et al.* (2001) and Rebilas (2002).

in Section 11.9). This resulting speed is one that we'll see again when we get to the velocity-addition formula in Section 11.5.1. ♣

**Example:** A train with proper length  $L$  moves at speed  $5c/13$  with respect to the ground. A ball is thrown from the back of the train to the front. The speed of the ball with respect to the train is  $c/3$ . As viewed by someone on the ground, how much time does the ball spend in the air, and how far does it travel?

**Solution:** The  $\gamma$  factor associated with the speed  $5c/13$  is  $\gamma = 13/12$ . The two events we are concerned with are “ball leaving back of train” and “ball arriving at front of train.” The spacetime separation between these events is easy to calculate on the train. We have  $\Delta x_T = L$ , and  $\Delta t_T = L/(c/3) = 3L/c$ . The Lorentz transformations giving the coordinates on the ground are therefore

$$\begin{aligned} x_G &= \gamma(x_T + vt_T) = \frac{13}{12} \left( L + \left( \frac{5c}{13} \right) \left( \frac{3L}{c} \right) \right) = \frac{7L}{3}, \\ t_G &= \gamma(t_T + vx_T/c^2) = \frac{13}{12} \left( \frac{3L}{c} + \frac{(5c/13)L}{c^2} \right) = \frac{11L}{3c}. \end{aligned} \quad (11.23)$$

In a given problem, such as the above example, one of the frames usually allows for a quick calculation of  $\Delta x$  and  $\Delta t$ , so you simply have to mechanically plug these quantities into the L.T.'s to obtain  $\Delta x'$  and  $\Delta t'$  in the other frame, where they may not be as obvious.

Relativity is a subject in which there are usually many ways to do a problem. If you're trying to find some  $\Delta x$ 's and  $\Delta t$ 's, then you can use the L.T.'s, or perhaps the invariant interval (introduced in Section 11.6), or maybe a velocity-addition approach (introduced in Section 11.5.1), or even the sending-of-light-signals strategy used in Section 11.3. Depending on the specific problem and what your personal preferences are, certain approaches will be more enjoyable than others. But no matter which method you choose, you should take advantage of the plethora of possibilities by picking a second method to double-check your answer. Personally, I find the L.T.'s to be the perfect option for this, because the other methods are generally more fun when solving a problem for the first time, while the L.T.'s are usually quick and easy to apply (perfect for a double-check).<sup>28</sup>

The excitement will build in your voice,  
As you rise from your seat and rejoice,  
“A Lorentz transformation  
Provides information,  
As an alternate method of choice!”

<sup>28</sup> I would, however, be very wary of solving a problem using only the L.T.'s, with no other check, because it's very easy to mess up a sign in the transformations. And since there's nothing to do except mechanically plug in numbers, there's not much opportunity for an intuitive check, either.

#### 11.4.2 The fundamental effects

Let's now see how the Lorentz transformations imply the three fundamental effects (namely, loss of simultaneity, time dilation, and length contraction) discussed in Section 11.3. Of course, we just used these effects to *derive* the L.T.'s, so we know everything will work out. We'll just be going in circles. But since these fundamental effects are, well, fundamental, let's belabor the point and discuss them one more time, with the starting point being the L.T.'s.

##### *Loss of simultaneity*

Let two events occur simultaneously in frame  $S'$ . Then the separation between them, as measured by  $S'$ , is  $(x', t') = (x', 0)$ . As usual, we are not bothering to write the  $\Delta$ 's in front of the coordinates. Using the second of Eqs. (11.17), we see that the time between the events, as measured by  $S$ , is  $t = \gamma vx'/c^2$ . This is not equal to zero (unless  $x' = 0$ ). Therefore, the events do not occur simultaneously in frame  $S$ .

##### *Time dilation*

Consider two events that occur in the same place in  $S'$ . Then the separation between them is  $(x', t') = (0, t')$ . Using the second of Eqs. (11.17), we see that the time between the events, as measured by  $S$ , is

$$t = \gamma t' \quad (\text{if } x' = 0). \quad (11.24)$$

The factor  $\gamma$  is greater than or equal to 1, so  $t \geq t'$ . The passing of one second on  $S'$ 's clock takes more than one second on  $S$ 's clock.  $S$  sees  $S'$  drinking his coffee very slowly.

The same strategy works if we interchange  $S$  and  $S'$ . Consider two events that occur in the same place in  $S$ . The separation between them is  $(x, t) = (0, t)$ . Using the second of Eqs. (11.19), we see that the time between the events, as measured by  $S'$ , is

$$t' = \gamma t \quad (\text{if } x = 0). \quad (11.25)$$

Therefore,  $t' \geq t$ . Another way to derive this is to use the first of Eqs. (11.17) to write  $x' = -vt'$ , and then substitute this into the second equation.

**REMARK:** If we write down the two above equations by themselves,  $t = \gamma t'$  and  $t' = \gamma t$ , they appear to contradict each other. This apparent contradiction arises from the omission of the conditions they are based on. The former equation is based on the assumption that  $x' = 0$ . The latter equation is based on the assumption that  $x = 0$ . They have nothing to do with each other. It would perhaps be better to write the equations as

$$(t = \gamma t')_{x'=0}, \quad \text{and} \quad (t' = \gamma t)_{x=0}, \quad (11.26)$$

but this is somewhat cumbersome. ♣

##### Length contraction

This proceeds just like the time dilation above, except that now we want to set certain time intervals equal to zero, instead of certain space intervals. We want to do this because to measure a length, we calculate the distance between two points whose positions are measured *simultaneously*. That's what a length is.

Consider a stick at rest in  $S'$ , where it has length  $\ell'$ . We want to find the length  $\ell$  in  $S$ . Simultaneous measurements of the coordinates of the ends of the stick in  $S$  yield a separation of  $(x, t) = (x, 0)$ . Using the first of Eqs. (11.19), we have

$$x' = \gamma x \quad (\text{if } t = 0). \quad (11.27)$$

But  $x$  is by definition the length in  $S$ . And  $x'$  is the length in  $S'$ , because the stick isn't moving in  $S'$ .<sup>29</sup> Therefore,  $\ell = \ell'/\gamma$ . And since  $\gamma \geq 1$ , we have  $\ell \leq \ell'$ , so  $S$  sees the stick shorter than  $S'$  sees it.

Now interchange  $S$  and  $S'$ . Consider a stick at rest in  $S$ , where it has length  $\ell$ . We want to find the length in  $S'$ . Measurements of the coordinates of the ends of the stick in  $S'$  yield a separation of  $(x', t') = (x', 0)$ . Using the first of Eqs. (11.17), we have

$$x = \gamma x' \quad (\text{if } t' = 0). \quad (11.28)$$

But  $x'$  is by definition the length in  $S'$ . And  $x$  is the length in  $S$ , because the stick is not moving in  $S$ . Therefore,  $\ell' = \ell/\gamma$ , so  $\ell' \leq \ell$ .

**REMARK:** As with time dilation, if we write down the two equations by themselves,  $\ell = \ell'/\gamma$  and  $\ell' = \ell/\gamma$ , they appear to contradict each other. But as before, this apparent contradiction arises from the omission of the conditions they are based on. The former equation is based on the assumptions that  $t = 0$  and that the stick is at rest in  $S'$ . The latter equation is based on the assumptions that  $t' = 0$  and that the stick is at rest in  $S$ . They have nothing to do with each other. We should really write,

$$(x = x'/\gamma)_{t=0}, \quad \text{and} \quad (x' = x/\gamma)_{t'=0}, \quad (11.29)$$

and then identify  $x'$  in the first equation with  $\ell'$  only after invoking the further assumption that the stick is at rest in  $S'$ . Likewise for the second equation. But this is a pain. ♣

### 11.5 Velocity addition

#### 11.5.1 Longitudinal velocity addition

Consider the following setup. An object moves at speed  $v_1$  with respect to frame  $S'$ . And frame  $S'$  moves at speed  $v_2$  with respect to frame  $S$ , in the same direction as the motion of the object (see Fig. 11.18). What is the speed,  $u$ , of the object with respect to frame  $S$ ?

![Diagram illustrating velocity addition. A rectangular box represents frame S'. Inside the box, a dot represents an object moving to the right with velocity v1. The box itself is moving to the right relative to frame S with velocity v2. The label S is positioned below the box, and the label S' is inside the box on the right side.](e4fd94e4257186c2521ef22a3523c1f1_img.jpg)

Diagram illustrating velocity addition. A rectangular box represents frame S'. Inside the box, a dot represents an object moving to the right with velocity v1. The box itself is moving to the right relative to frame S with velocity v2. The label S is positioned below the box, and the label S' is inside the box on the right side.

Fig. 11.18

<sup>29</sup> The measurements of the ends made by  $S$  are *not* simultaneous in the  $S'$  frame. In the  $S'$  frame, the separation between the events is  $(x', t')$ , where both  $x'$  and  $t'$  are nonzero. This doesn't satisfy our definition of a length measurement in  $S'$  (because  $t' \neq 0$ ), but the stick isn't moving in  $S'$ , so  $S'$  can measure the ends whenever he feels like it, and he will always get the same difference. So  $x'$  is indeed the length in the  $S'$  frame.

The Lorentz transformations can be used to easily answer this question. The relative speed of the frames is  $v_2$ . Consider two events along the object's path (for example, say it makes two beeps). We are given that  $\Delta x'/\Delta t' = v_1$ . Our goal is to find  $u \equiv \Delta x/\Delta t$ . The Lorentz transformations from  $S'$  to  $S$ , Eqs. (11.17), are

$$\Delta x = \gamma_2(\Delta x' + v_2 \Delta t'), \quad \text{and} \quad \Delta t = \gamma_2(\Delta t' + v_2 \Delta x'/c^2), \quad (11.30)$$

where  $\gamma_2 \equiv 1/\sqrt{1 - v_2^2/c^2}$ . Therefore,

$$\begin{aligned} u \equiv \frac{\Delta x}{\Delta t} &= \frac{\Delta x' + v_2 \Delta t'}{\Delta t' + v_2 \Delta x'/c^2} \\ &= \frac{\Delta x'/\Delta t' + v_2}{1 + v_2(\Delta x'/\Delta t')/c^2} \\ &= \frac{v_1 + v_2}{1 + v_1 v_2/c^2}. \end{aligned} \quad (11.31)$$

This is the *velocity-addition formula*, for adding velocities along the same line. Let's look at some of its properties.

- It is symmetric with respect to  $v_1$  and  $v_2$ , as it should be, because we could switch the roles of the object and frame  $S$ .
- For  $v_1 v_2 \ll c^2$ , it reduces to  $u \approx v_1 + v_2$ , which we know holds perfectly well for everyday speeds.
- If  $v_1 = c$  or  $v_2 = c$ , then we find  $u = c$ , as should be the case, because anything that moves with speed  $c$  in one frame moves with speed  $c$  in another.
- The maximum (or minimum) of  $u$  in the region  $-c \leq v_1, v_2 \leq c$  equals  $c$  (or  $-c$ ), which can be seen by noting that  $\partial u/\partial v_1$  and  $\partial u/\partial v_2$  are never zero in the interior of the region.

If you take any two velocities that are less than  $c$  and add them according to Eq. (11.31), then you will obtain a velocity that is again less than  $c$ . This shows that no matter how much you keep accelerating an object (that is, no matter how many times you give the object a speed  $v_1$  with respect to the frame moving at speed  $v_2$  that it was just in), you can't bring the speed up to the speed of light. We'll give another argument for this result in Chapter 12 when we discuss energy.

![Diagram showing a box representing frame B moving with velocity v2 relative to frame C. Inside the box, an object A is moving with velocity v1 relative to B.](91f6469662e7371724ca5a457f829e9e_img.jpg)

The diagram shows a rectangular box labeled 'B' at its right end. To the right of the box is an arrow pointing right, labeled 'v2'. Inside the box, on the left, is a dot labeled 'A' with an arrow pointing right, labeled 'v1'. Below the box is the letter 'C'.

Diagram showing a box representing frame B moving with velocity v2 relative to frame C. Inside the box, an object A is moving with velocity v1 relative to B.

For a bullet, a train, and a gun,  
 Adding the speeds can be fun.  
 Take a trip down the path  
 Paved with Einstein's new math,  
 Where a half plus a half isn't one.

![Diagram showing two separate frames. Frame B is moving with velocity v1 relative to frame A. Frame C is moving with velocity v2 relative to frame B.](59dd95c694658fd41ad4b3889541167c_img.jpg)

The diagram shows three labels: 'A', 'B', and 'C'. Below 'A' is an arrow pointing right, labeled 'v1'. Below 'B' is an arrow pointing left, labeled 'v2'. Below 'C' is nothing. This represents frame B moving at v1 relative to A, and frame C moving at v2 relative to B.

Diagram showing two separate frames. Frame B is moving with velocity v1 relative to frame A. Frame C is moving with velocity v2 relative to frame B.

**Fig. 11.19**

**REMARK:** Consider the two scenarios shown in Fig. 11.19. If the goal is to find the velocity of  $A$  with respect to  $C$ , then the velocity-addition formula applies to both scenarios, because the second scenario is the same as the first one, as observed in  $B$ 's frame.

The velocity-addition formula applies when we ask, “If  $A$  moves at  $v_1$  with respect to  $B$ , and  $B$  moves at  $v_2$  with respect to  $C$  (which means, of course, that  $C$  moves at speed  $v_2$  with respect to  $B$ ), then how fast does  $A$  move with respect to  $C$ ?” The formula does *not* apply if we ask the more mundane question, “What is the relative speed of  $A$  and  $C$ , as viewed by  $B$ ?” The answer to this is just  $v_1 + v_2$ .

In short, if the two velocities are given with respect to the *same* observer, say  $B$ , and if you are asking for the relative velocity as measured by  $B$ , then you simply have to add the velocities.<sup>30</sup> But if you are asking for the relative velocity as measured by  $A$  or  $C$ , then you have to use the velocity-addition formula. It makes no sense to add velocities that are measured with respect to different observers. Doing so would involve adding things that are measured in different coordinate systems, which is meaningless. In other words, taking the velocity of  $A$  with respect to  $B$  and adding it to the velocity of  $B$  with respect to  $C$ , hoping to obtain the velocity of  $A$  with respect to  $C$ , is invalid. ♣

**Example (Passing trains, again):** Consider again the scenario in the “Passing trains” example in Section 11.3.3.

- How long, as viewed by  $A$  and as viewed by  $B$ , does it take for  $A$  to overtake  $B$ ?
- Let event  $E_1$  be “the front of  $A$  passing the back of  $B$ ”, and let event  $E_2$  be “the back of  $A$  passing the front of  $B$ .” Person  $D$  walks at constant speed from the back of  $B$  to the front (see Fig. 11.20), such that he coincides with both events  $E_1$  and  $E_2$ . How long does the “overtaking” process take, as viewed by  $D$ ?

![Diagram for Fig. 11.20 showing two trains, A and B, moving to the right. Train A is above train B. An arrow above A indicates its velocity is 4c/5. An arrow above B indicates its velocity is 3c/5. A person D is shown walking from the back of B to the front. A person C is shown below the trains.](9c2e607018469e98bf1744336556798d_img.jpg)

Diagram for Fig. 11.20 showing two trains, A and B, moving to the right. Train A is above train B. An arrow above A indicates its velocity is 4c/5. An arrow above B indicates its velocity is 3c/5. A person D is shown walking from the back of B to the front. A person C is shown below the trains.

Fig. 11.20

**Solution:**

- First consider  $B$ ’s point of view. From the velocity-addition formula,  $B$  sees  $A$  move with speed

$$u = \frac{\frac{4c}{5} - \frac{3c}{5}}{1 - \frac{4}{5} \cdot \frac{3}{5}} = \frac{5c}{13}. \quad (11.32)$$

The  $\gamma$  factor associated with this speed is  $\gamma = 13/12$ . Therefore,  $B$  sees  $A$ ’s train contracted to a length  $12L/13$ . During the overtaking,  $A$  must travel a distance equal to the sum of the lengths of the trains in  $B$ ’s frame (see Fig. 11.21), which is  $L + 12L/13 = 25L/13$ . Since  $A$  moves at speed  $5c/13$ , the total time in  $B$ ’s frame is

$$t_B = \frac{25L/13}{5c/13} = \frac{5L}{c}. \quad (11.33)$$

The exact same reasoning holds from  $A$ ’s point of view, so we have  $t_A = t_B = 5L/c$ .

![Diagram for Fig. 11.21 showing the overtaking process in B's frame. Train A is shown at a 'start' position (solid rectangle) and an 'end' position (dashed rectangle). Train B is shown in between. Arrows above A indicate its velocity is 5c/13 at both start and end. The label 'B's frame' is below the diagram.](abface5a471f22cf8f95f2054d8ddb79_img.jpg)

Diagram for Fig. 11.21 showing the overtaking process in B's frame. Train A is shown at a 'start' position (solid rectangle) and an 'end' position (dashed rectangle). Train B is shown in between. Arrows above A indicate its velocity is 5c/13 at both start and end. The label 'B's frame' is below the diagram.

Fig. 11.21

<sup>30</sup> Note that the resulting speed can certainly be greater than  $c$ . If I see a ball heading toward me at  $0.9c$  from the right, and another one heading toward me at  $0.9c$  from the left, then the relative speed of the balls in my frame is  $1.8c$ . In the frame of one of the balls, however, the relative speed is  $(1.8/1.81)c \approx (0.9945)c$ , from Eq. (11.31).

![Figure 11.22: A diagram showing two trains, A and B, moving towards each other. Train A is on the left, moving right with velocity v. Train B is on the right, moving left with velocity v. A point D is marked on train B. The diagram shows the 'start' and 'end' positions of the trains relative to point D. At the start, the front of train A is at D. At the end, the back of train B is at D. The length of train A is L, and the length of train B is L. The total distance traveled by each train relative to D is 2L.](9e2f2a21f31783771df5cca9eb7f2c7f_img.jpg)

Figure 11.22: A diagram showing two trains, A and B, moving towards each other. Train A is on the left, moving right with velocity v. Train B is on the right, moving left with velocity v. A point D is marked on train B. The diagram shows the 'start' and 'end' positions of the trains relative to point D. At the start, the front of train A is at D. At the end, the back of train B is at D. The length of train A is L, and the length of train B is L. The total distance traveled by each train relative to D is 2L.

Fig. 11.22

- (b) Look at things from  $D$ 's point of view.  $D$  is at rest, and the two trains move with equal and opposite speeds  $v$  (see Fig. 11.22), because otherwise the second event  $E_2$  wouldn't be located at  $D$ . The relativistic addition of  $v$  with itself is the speed of  $A$  as viewed by  $B$ . But from part (a), we know that this relative speed equals  $5c/13$ . Therefore,

$$\frac{2v}{1 + v^2/c^2} = \frac{5c}{13} \implies v = \frac{c}{5}, \quad (11.34)$$

where we have ignored the unphysical solution,  $v = 5c$ . The  $\gamma$  factor associated with  $v = c/5$  is  $\gamma = 5/(2\sqrt{6})$ . So  $D$  sees both trains contracted to a length  $2\sqrt{6}L/5$ . During the overtaking, each train must travel a distance equal to its length, because both events,  $E_1$  and  $E_2$ , take place right at  $D$ . The total time in  $D$ 's frame is therefore

$$t_D = \frac{2\sqrt{6}L/5}{c/5} = \frac{2\sqrt{6}L}{c}. \quad (11.35)$$

**REMARKS:** There are a few double-checks we can perform. The speed of  $D$  with respect to the ground can be obtained either via  $B$ 's frame by relativistically adding  $3c/5$  and  $c/5$ , or via  $A$ 's frame by subtracting  $c/5$  from  $4c/5$ . These both give the same answer, namely  $5c/7$ , as they must. (The  $c/5$  speed can in fact be determined by this reasoning, instead of using Eq. (11.34).) The  $\gamma$  factor between the ground and  $D$  is therefore  $7/2\sqrt{6}$ . We can then use time dilation to say that someone on the ground sees the overtaking take a time of  $(7/2\sqrt{6})t_D$  (we can say this because both events happen right at  $D$ ). Using Eq. (11.35), this gives a ground-frame time of  $7L/c$ , in agreement with Eq. (11.15). Likewise, the  $\gamma$  factor between  $D$  and either train is  $5/2\sqrt{6}$ . So the time of the overtaking as viewed by either  $A$  or  $B$  is  $(5/2\sqrt{6})t_D = 5L/c$ , in agreement with Eq. (11.33).

Note that we *cannot* use simple time dilation to relate the ground to  $A$  or  $B$ , because the two events don't happen at the same place in the train frames. But since both events happen at the same place in  $D$ 's frame, namely right at  $D$ , it's legal to use time dilation to go from  $D$ 's frame to any other frame. ♣

![Figure 11.23: A diagram showing a velocity vector u' in frame S'. The vector u' has components u'_x and u'_y. Frame S' is moving with velocity v relative to frame S in the x direction. The diagram shows a right triangle with horizontal side u'_x and vertical side u'_y, and hypotenuse u'.](e9e07a3cc8c83714933ac39c3a326908_img.jpg)

Figure 11.23: A diagram showing a velocity vector u' in frame S'. The vector u' has components u'\_x and u'\_y. Frame S' is moving with velocity v relative to frame S in the x direction. The diagram shows a right triangle with horizontal side u'\_x and vertical side u'\_y, and hypotenuse u'.

Fig. 11.23

#### 11.5.2 Transverse velocity addition

Consider the following general two-dimensional situation. An object moves with velocity  $(u'_x, u'_y)$  with respect to frame  $S'$ . And frame  $S'$  moves with speed  $v$  with respect to frame  $S$ , in the  $x$  direction (see Fig. 11.23). What is the velocity,  $(u_x, u_y)$ , of the object with respect to frame  $S$ ?

The existence of motion in the  $y$  direction doesn't affect the preceding derivation of the speed in the  $x$  direction, so Eq. (11.31) is still valid. In the present notation, it becomes

$$u_x = \frac{u'_x + v}{1 + u'_x v/c^2}. \quad (11.36)$$

To find  $u_y$ , we can again make easy use of the Lorentz transformations. Consider two events along the object's path. We are given that  $\Delta x'/\Delta t' = u'_x$ , and  $\Delta y'/\Delta t' = u'_y$ . Our goal is to find  $u_y \equiv \Delta y/\Delta t$ . The relevant Lorentz transformations from  $S'$  to  $S$  in Eq. (11.17) are

$$\Delta y = \Delta y', \quad \text{and} \quad \Delta t = \gamma(\Delta t' + v\Delta x'/c^2). \quad (11.37)$$

Therefore,

$$\begin{aligned} u_y &\equiv \frac{\Delta y}{\Delta t} = \frac{\Delta y'}{\gamma(\Delta t' + v\Delta x'/c^2)} \\ &= \frac{\Delta y'/\Delta t'}{\gamma(1 + v(\Delta x'/\Delta t')/c^2)} \\ &= \frac{u'_y}{\gamma(1 + u'_x v/c^2)}. \end{aligned} \quad (11.38)$$

REMARK: In the special case where  $u'_x = 0$ , we have  $u_y = u'_y/\gamma$ . When  $u'_y$  is small and  $v$  is large, this result can be seen to be a special case of time dilation, in the following way. Consider a series of equally spaced lines parallel to the  $x$  axis (see Fig. 11.24). Imagine that the object's clock ticks once every time it crosses a line. Since  $u'_y$  is small, the object's frame is essentially frame  $S'$ . So if  $S$  flies by to the left, then the object is essentially moving at speed  $v$  with respect to  $S$ . Therefore,  $S$  sees the clock run slow by a factor  $\gamma$ . This means that  $S$  sees the object cross the lines at a slower rate, by a factor  $\gamma$  (because the clock still ticks once every time it crosses a line; this is a frame-independent statement). Since distances in the  $y$  direction are the same in the two frames, we conclude that  $u_y = u'_y/\gamma$ . This  $\gamma$  factor will be very important when we deal with momentum in Chapter 12.

To sum up: if you run in the  $x$  direction past an object, then its  $y$  speed is slower in your frame (or faster, depending on the relative sign of  $u'_x$  and  $v$ ). Strange indeed, but no stranger than other effects we've seen. Problem 11.16 deals with the special case where  $u'_x = 0$ , but where  $u'_y$  is not necessarily small. ♣

![Diagram illustrating the Lorentz transformation of time dilation. It shows two frames, S and S', with a series of horizontal dashed lines representing equally spaced lines parallel to the x-axis. Frame S' is moving to the right with velocity v relative to frame S. An object is shown moving vertically in S' (at rest in S'), and its path is shown crossing the dashed lines. The diagram illustrates how the object's clock ticks once every time it crosses a line, and how the relative motion of the frames affects the perceived rate of these ticks.](5eac53f55064a7b7f5fa47ea5e6c1ed9_img.jpg)

Diagram illustrating the Lorentz transformation of time dilation. It shows two frames, S and S', with a series of horizontal dashed lines representing equally spaced lines parallel to the x-axis. Frame S' is moving to the right with velocity v relative to frame S. An object is shown moving vertically in S' (at rest in S'), and its path is shown crossing the dashed lines. The diagram illustrates how the object's clock ticks once every time it crosses a line, and how the relative motion of the frames affects the perceived rate of these ticks.

Fig. 11.24

### 11.6 The invariant interval

Consider the quantity,

$$(\Delta s)^2 \equiv c^2(\Delta t)^2 - (\Delta x)^2. \quad (11.39)$$

Technically, we should also subtract off  $(\Delta y)^2$  and  $(\Delta z)^2$ , but nothing exciting happens in the transverse directions, so we'll ignore them. Using Eq. (11.17), we can write  $(\Delta s)^2$  in terms of the  $S'$  coordinates,  $\Delta x'$  and  $\Delta t'$ . The result is (dropping the  $\Delta$ 's)

$$\begin{aligned} c^2t^2 - x^2 &= \frac{c^2(t' + vx'/c^2)^2}{1 - v^2/c^2} - \frac{(x' + vt')^2}{1 - v^2/c^2} \\ &= \frac{t'^2(c^2 - v^2) - x'^2(1 - v^2/c^2)}{1 - v^2/c^2} \\ &= c^2t'^2 - x'^2. \end{aligned} \quad (11.40)$$

We see that the Lorentz transformations imply that the quantity  $c^2t^2 - x^2$  doesn't depend on the frame. This result is more than we bargained for, for the following reason. The speed-of-light postulate says that if  $c^2t'^2 - x'^2 = 0$ , then  $c^2t^2 - x^2 = 0$ . But Eq. (11.40) says that if  $c^2t'^2 - x'^2 = b$ , then  $c^2t^2 - x^2 = b$ , for *any* value of  $b$ , not just zero. This is, as you might guess, very useful. There are enough things that change when we go from one frame to another, so it's nice to have a frame-independent quantity that we can hang on to. The fact that  $s^2$  is invariant under Lorentz transformations of  $x$  and  $t$  is exactly analogous to the fact that  $r^2$  is invariant under rotations in the  $x$ - $y$  plane. The coordinates themselves change under the transformation, but the special combination of  $c^2t^2 - x^2$  for Lorentz transformations, or  $x^2 + y^2$  for rotations, remains the same. All inertial observers agree on the value of  $s^2$ , independent of what they measure for the actual coordinates.

“Potato?! Potahto!” said she,  
 “And of *course* it's tomahto, you see.  
 But the square of  $ct$   
 Minus  $x^2$  will be  
 Always something on which we agree.”

A note on terminology: The separation in the coordinates,  $(c\Delta t, \Delta x)$ , is usually referred to as the *spacetime interval*, while the quantity  $(\Delta s)^2 \equiv c^2(\Delta t)^2 - (\Delta x)^2$  is referred to as the *invariant interval* (or technically the square of the invariant interval). At any rate, just call it  $s^2$ , and people will know what you mean. The invariance of  $s^2$  is actually just a special case of more general results involving inner products and 4-vectors, which we'll discuss in Chapter 13. Let's now look at the physical significance of  $s^2 \equiv c^2t^2 - x^2$ ; there are three cases to consider.

#### Case 1: $s^2 > 0$ (timelike separation)

In this case, we say that the two events are *timelike* separated. We have  $c^2t^2 > x^2$ , and so  $|x/t| < c$ . Consider a frame  $S'$  moving at speed  $v$  with respect to  $S$ . The Lorentz transformation for  $x$  is

$$x' = \gamma(x - vt). \quad (11.41)$$

Since  $|x/t| < c$ , there exists a  $v$  that is less than  $c$  (namely  $v = x/t$ ) that makes  $x' = 0$ . In other words, if two events are timelike separated, it is possible to find a frame  $S'$  in which the two events happen at the same place. (In short, the condition  $|x/t| < c$  means that it is possible for a particle to travel from one event to the other.) The invariance of  $s^2$  then gives  $s^2 = c^2t^2 - x^2 = c^2t'^2$ . So we see that  $s/c$  is the time between the events in the frame in which the events occur at the same place. This time is called the *proper time*.

#### **Case 2: $s^2 < 0$ (spacelike separation)**

In this case, we say that the two events are *spacelike* separated.<sup>31</sup> We have  $c^2t^2 < x^2$ , and so  $|t/x| < 1/c$ . Consider a frame  $S'$  moving at speed  $v$  with respect to  $S$ . The Lorentz transformation for  $t'$  is

$$t' = \gamma(t - vx/c^2). \quad (11.42)$$

Since  $|t/x| < 1/c$ , there exists a  $v$  that is less than  $c$  (namely  $v = c^2t/x$ ) that makes  $t' = 0$ . In other words, if two events are spacelike separated, it is possible to find a frame  $S'$  in which the two events happen at the same time. (This statement is not as easy to see as the corresponding one in the timelike case above. But if you draw a Minkowski diagram, described in the next section, it becomes clear.) The invariance of  $s^2$  then gives  $s^2 = c^2t'^2 - x'^2 = -x'^2$ . So we see that  $|s|$  is the distance between the events in the frame in which the events occur at the same time. This distance is called the *proper distance*, or *proper length*.

#### **Case 3: $s^2 = 0$ (lightlike separation)**

In this case, we say that the two events are *lightlike* separated. We have  $c^2t^2 = x^2$ , and so  $|x/t| = c$ . This holds in every frame, so in every frame a photon emitted at one of the events will arrive at the other. It is not possible to find a frame  $S'$  in which the two events happen at the same place or the same time, because the frame would have to travel at the speed of light.

---

**Example (Time dilation):** An illustration of the usefulness of the invariance of  $s^2$  is a derivation of time dilation. Let frame  $S'$  move at speed  $v$  with respect to frame  $S$ . Consider two events at the origin of  $S'$ , separated by time  $t'$ . The separation between the events is

$$\begin{aligned} \text{in } S': (x', t') &= (0, t'), \\ \text{in } S: (x, t) &= (vt, t). \end{aligned} \quad (11.43)$$

The invariance of  $s^2$  implies  $c^2t'^2 - 0 = c^2t^2 - v^2t^2$ . Therefore,

$$t = \frac{t'}{\sqrt{1 - v^2/c^2}}. \quad (11.44)$$

This method makes it clear that the time-dilation result rests on the assumption that  $x' = 0$ .

---

**Example (Passing trains, yet again):** Consider again the scenario in the “Passing trains” examples in Sections 11.3.3 and 11.5.1. Verify that the  $s^2$  between the events  $E_1$  and  $E_2$  is the same in all of the frames,  $A$ ,  $B$ ,  $C$ , and  $D$  (see Fig. 11.25).

![Diagram showing four frames of reference: A, B, C, and D. Frame A is a rectangle with a right-pointing arrow above it labeled 4c/5. Frame B is a rectangle with a right-pointing arrow above it labeled 3c/5. Frame C is represented by a stick figure with a right-pointing arrow above it. Frame D is a rectangle with a right-pointing arrow inside it.](2ff2f966dff0fc590875b0e9500fa9c2_img.jpg)

Diagram showing four frames of reference: A, B, C, and D. Frame A is a rectangle with a right-pointing arrow above it labeled 4c/5. Frame B is a rectangle with a right-pointing arrow above it labeled 3c/5. Frame C is represented by a stick figure with a right-pointing arrow above it. Frame D is a rectangle with a right-pointing arrow inside it.

**Fig. 11.25**

<sup>31</sup> It's fine that  $s^2$  is negative in this case, which means that  $s$  is imaginary. We can take the absolute value of  $s$  if we want to obtain a real number.

**Solution:** The only quantity that we'll need that we haven't already found in the two examples above is the distance between  $E_1$  and  $E_2$  in  $C$ 's frame (the ground frame). In this frame, train  $A$  travels at a rate  $4c/5$  for a time  $t_C = 7L/c$ , covering a distance of  $28L/5$ . But event  $E_2$  occurs at the back of the train, which is a distance  $3L/5$  behind the front end (this is the contracted length in the ground frame). Therefore, the distance between events  $E_1$  and  $E_2$  in the ground frame is  $28L/5 - 3L/5 = 5L$ . You can also apply the same line of reasoning using train  $B$ , in which the  $5L$  result takes the form,  $(3c/5)(7L/c) + 4L/5$ .

Putting the previous results together, we have the following separations between the events in the various frames:

|            | $A$    | $B$    | $C$    | $D$            |
|------------|--------|--------|--------|----------------|
| $\Delta t$ | $5L/c$ | $5L/c$ | $7L/c$ | $2\sqrt{6}L/c$ |
| $\Delta x$ | $-L$   | $L$    | $5L$   | $0$            |

From the table, we see that  $\Delta s^2 \equiv c^2 \Delta t^2 - \Delta x^2 = 24L^2$  for all four frames, as desired. We could have worked backwards, of course, and used the  $s^2 = 24L^2$  result from frames  $A$ ,  $B$ , or  $D$ , to deduce that  $\Delta x = 5L$  in frame  $C$ . In Problem 11.10, you are asked to perform the tedious task of checking that the values in the above table satisfy the Lorentz transformations between the six different pairs of frames.

### 11.7 Minkowski diagrams

Minkowski diagrams (sometimes called “spacetime” diagrams) are extremely useful in seeing how coordinates transform between different reference frames. If you want to produce exact numbers in a problem, you'll probably have to use one of the strategies we've encountered so far. But as far as getting an overall intuitive picture of a setup goes (if there is in fact any such thing as intuition in relativity), there is no better tool than a Minkowski diagram. Here's how you make one.

Let frame  $S'$  move at speed  $v$  with respect to frame  $S$  (along the  $x$  axis, as usual, and ignore the  $y$  and  $z$  components). Draw the  $x$  and  $ct$  axes of frame  $S$ .<sup>32</sup> What do the  $x'$  and  $ct'$  axes of  $S'$  look like, superimposed on this diagram? That is, at what angles are the axes inclined, and what is the size of one unit on these axes? (There is no reason why one unit on the  $x'$  and  $ct'$  axes should have the same length on the paper as one unit on the  $x$  and  $ct$  axes.) We can answer these questions by using the Lorentz transformations, Eqs. (11.17). We'll first look at the  $ct'$  axis, and then the  $x'$  axis.

<sup>32</sup> We choose to plot  $ct$  instead of  $t$  on the vertical axis, so that the trajectory of a light beam lies at a nice  $45^\circ$  angle. Alternatively, we could choose units where  $c = 1$ .

#### ***ct'*-axis angle and unit size**

Look at the point  $(x', ct') = (0, 1)$ , which lies on the  $ct'$  axis, one  $ct'$  unit from the origin (see Fig. 11.26). Equations (11.17) tell us that this point is the point  $(x, ct) = (\gamma v/c, \gamma)$ . The angle between the  $ct'$  and  $ct$  axes is therefore given by  $\tan \theta_1 = x/ct = v/c$ . With  $\beta \equiv v/c$ , we have

$$\tan \theta_1 = \beta. \quad (11.45)$$

Alternatively, the  $ct'$  axis is simply the “worldline” of the origin of  $S'$ . (A worldline is the path an object takes as it travels through spacetime.) The origin moves at speed  $v$  with respect to  $S$ . Therefore, points on the  $ct'$  axis satisfy  $x/t = v$ , or  $x/ct = v/c$ .

On the paper, the point  $(x', ct') = (0, 1)$ , which we just found to be the point  $(x, ct) = (\gamma v/c, \gamma)$ , is a distance  $\gamma \sqrt{1 + v^2/c^2}$  from the origin. Therefore, using the definitions of  $\beta$  and  $\gamma$ , we see that

$$\frac{\text{one } ct' \text{ unit}}{\text{one } ct \text{ unit}} = \sqrt{\frac{1 + \beta^2}{1 - \beta^2}}, \quad (11.46)$$

as measured on a grid where the  $x$  and  $ct$  axes are orthogonal. This ratio approaches infinity as  $\beta \rightarrow 1$ . And it of course equals 1 if  $\beta = 0$ .

#### ***x'*-axis angle and unit size**

The same basic argument holds here. Look at the point  $(x', ct') = (1, 0)$ , which lies on the  $x'$  axis, one  $x'$  unit from the origin (see Fig. 11.26). Equations (11.17) tell us that this point is the point  $(x, ct) = (\gamma, \gamma v/c)$ . The angle between the  $x'$  and  $x$  axes is therefore given by  $\tan \theta_2 = ct/x = v/c$ . So, as in the  $ct'$ -axis case,

$$\tan \theta_2 = \beta. \quad (11.47)$$

On the paper, the point  $(x', ct') = (1, 0)$ , which we just found to be the point  $(x, ct) = (\gamma, \gamma v/c)$ , is a distance  $\gamma \sqrt{1 + v^2/c^2}$  from the origin. So, as in the  $ct'$ -axis case,

$$\frac{\text{one } x' \text{ unit}}{\text{one } x \text{ unit}} = \sqrt{\frac{1 + \beta^2}{1 - \beta^2}}, \quad (11.48)$$

as measured on a grid where the  $x$  and  $ct$  axes are orthogonal. Both the  $x'$  and  $ct'$  axes are therefore stretched by the same factor, and tilted in by the same angle, relative to the  $x$  and  $ct$  axes. This “squeezing in” of the axes in a Lorentz transformation is different from what happens in a rotation, where both axes rotate in the same direction.

**REMARKS:** If  $v/c \equiv \beta = 0$ , then  $\theta_1 = \theta_2 = 0$ , so the  $ct'$  and  $x'$  axes coincide with the  $ct$  and  $x$  axes, as they should. If  $\beta$  is very close to 1, then the  $x'$  and  $ct'$  axes are both very close to

![Figure 11.26: A Minkowski diagram showing the transformation of axes from (x, ct) to (x', ct'). The ct' axis is tilted from the ct axis by an angle theta_1, and the x' axis is tilted from the x axis by an angle theta_2. The point (x', ct') = (0, 1) is marked on the ct' axis, and its coordinates in the (x, ct) system are (x, ct) = (beta*gamma, gamma). The point (x', ct') = (1, 0) is marked on the x' axis, and its coordinates in the (x, ct) system are (x, ct) = (gamma, beta*gamma).](8ab81bd2eb0c658886d9ca0f036c985b_img.jpg)

Figure 11.26: A Minkowski diagram showing the transformation of axes from (x, ct) to (x', ct'). The ct' axis is tilted from the ct axis by an angle theta\_1, and the x' axis is tilted from the x axis by an angle theta\_2. The point (x', ct') = (0, 1) is marked on the ct' axis, and its coordinates in the (x, ct) system are (x, ct) = (beta\*gamma, gamma). The point (x', ct') = (1, 0) is marked on the x' axis, and its coordinates in the (x, ct) system are (x, ct) = (gamma, beta\*gamma).

**Fig. 11.26**

the  $45^\circ$  light-ray line. Note that since  $\theta_1 = \theta_2$ , the light-ray line bisects the  $x'$  and  $ct'$  axes. Therefore (as we verified above), the scales on these axes must be the same, because a light ray must satisfy  $x' = ct'$ . ♣

We now know what the  $x'$  and  $ct'$  axes look like. Given any two points in a Minkowski diagram (that is, given any two events in spacetime), we can just read off the  $\Delta x$ ,  $\Delta ct$ ,  $\Delta x'$ , and  $\Delta ct'$  quantities that our two observers measure, assuming that our graph is accurate enough. Although these quantities must of course be related by the Lorentz transformations, the advantage of a Minkowski diagram is that you can actually see geometrically what's going on.

There are very useful physical interpretations of the  $ct'$  and  $x'$  axes. If you stand at the origin of  $S'$ , then the  $ct'$  axis is the “here” axis, and the  $x'$  axis is the “now” axis (the line of simultaneity). That is, all events on the  $ct'$  axis take place at your position (the  $ct'$  axis is your worldline, after all), and all events on the  $x'$  axis take place simultaneously (they all have  $t' = 0$ ).

**Example (Length contraction):** For both parts of this problem, use a Minkowski diagram where the axes in frame  $S$  are orthogonal.

- The relative speed of  $S'$  and  $S$  is  $v$  (along the  $x$  direction). A meter stick lies along the  $x'$  axis and is at rest in  $S'$ . If  $S$  measures its length, what is the result?
- Now let the meter stick lie along the  $x$  axis and be at rest in  $S$ . If  $S'$  measures its length, what is the result?

![Minkowski diagram for length contraction. The vertical axis is ct and the horizontal axis is x. Two primed axes, ct' and x', originate from the origin A. The ct' axis is tilted to the right of the ct axis, and the x' axis is tilted to the right of the x axis. The angle between ct and ct' is theta, and the angle between x and x' is also theta. A dashed line represents the worldline of the right end of a meter stick at rest in S'. The left end of the stick is at the origin A. Point C is on the x' axis, representing the simultaneous position of the right end in the S' frame. A vertical dashed line from C meets the x axis at point D. A horizontal dashed line from C meets the ct axis at point B. The segment AC is labeled as 1 meter. The segment AB is the length measured in frame S. The segment CD is the vertical distance from the x axis to point C.](3170ea7bfb7557a879af7ea044d9d29f_img.jpg)

Minkowski diagram for length contraction. The vertical axis is ct and the horizontal axis is x. Two primed axes, ct' and x', originate from the origin A. The ct' axis is tilted to the right of the ct axis, and the x' axis is tilted to the right of the x axis. The angle between ct and ct' is theta, and the angle between x and x' is also theta. A dashed line represents the worldline of the right end of a meter stick at rest in S'. The left end of the stick is at the origin A. Point C is on the x' axis, representing the simultaneous position of the right end in the S' frame. A vertical dashed line from C meets the x axis at point D. A horizontal dashed line from C meets the ct axis at point B. The segment AC is labeled as 1 meter. The segment AB is the length measured in frame S. The segment CD is the vertical distance from the x axis to point C.

Fig. 11.27

#### **Solution:**

- Without loss of generality, pick the left end of the stick to be at the origin in  $S'$ . Then the worldlines of the two ends are shown in Fig. 11.27. The distance  $AC$  is 1 meter in the  $S'$  frame, because  $A$  and  $C$  are the endpoints of the stick at simultaneous times in the  $S'$  frame; this is how a length is measured. And since one unit on the  $x'$  axis has length  $\sqrt{1 + \beta^2}/\sqrt{1 - \beta^2}$ , this is the length on the paper of the segment  $AC$ .

How does  $S$  measure the length of the stick? He writes down the  $x$  coordinates of the ends at simultaneous times (as measured by him, of course), and takes the difference. Let the time he makes the measurements be  $t = 0$ . Then he measures the ends to be at the points  $A$  and  $B$ .<sup>33</sup> Now it's time to do some geometry. We have to find the length of segment  $AB$  in Fig. 11.27, given that segment  $AC$  has length  $\sqrt{1 + \beta^2}/\sqrt{1 - \beta^2}$ . We know that the primed axes are tilted at an angle  $\theta$ , where  $\tan \theta = \beta$ . Therefore,  $CD = (AC) \sin \theta$ . And since

<sup>33</sup> If  $S$  measures the ends in a dramatic fashion by, say, blowing them up, then  $S'$  will see the right end blow up first (the event at  $B$  has a negative  $t'$  coordinate, because it lies below the  $x'$  axis), and then a little while later  $S'$  will see the left end blow up (the event at  $A$  has  $t' = 0$ ). So  $S$  measures the ends at different times in the  $S'$  frame. This is part of the reason why  $S'$  should not be at all surprised that  $S$ 's measurement is smaller than one meter.

$\angle BCD = \theta$ , we have  $BD = (CD) \tan \theta = (AC) \sin \theta \tan \theta$ . Therefore (using  $\tan \theta = \beta$ ),

$$\begin{aligned}
 AB &= AD - BD = (AC) \cos \theta - (AC) \sin \theta \tan \theta \\
 &= (AC) \cos \theta (1 - \tan^2 \theta) \\
 &= \sqrt{\frac{1 + \beta^2}{1 - \beta^2}} \frac{1}{\sqrt{1 + \beta^2}} (1 - \beta^2) \\
 &= \sqrt{1 - \beta^2}.
 \end{aligned}
 \tag{11.49}$$

Therefore,  $S$  measures the meter stick to have length  $\sqrt{1 - \beta^2}$ , which is the standard length-contraction result.

- (b) The stick is now at rest in  $S$ , and we want to find the length that  $S'$  measures. Pick the left end of the stick to be at the origin in  $S$ . Then the worldlines of the two ends are shown in Fig. 11.28. The distance  $AB$  is 1 meter in the  $S$  frame.

In measuring the length of the stick,  $S'$  writes down the  $x'$  coordinates of the ends at simultaneous times (as measured by him), and takes the difference. Let the time he makes the measurements be  $t' = 0$ . Then he measures the ends to be at the points  $A$  and  $E$ . Now we do the geometry, which is easy in this case. The length of  $AE$  is simply  $1 / \cos \theta = \sqrt{1 + \beta^2}$ . But since one unit along the  $x'$  axis has length  $\sqrt{1 + \beta^2} / \sqrt{1 - \beta^2}$  on the paper, we see that  $AE$  is  $\sqrt{1 - \beta^2}$  of one unit in the  $S'$  frame. Therefore,  $S'$  measures the meter stick to have length  $\sqrt{1 - \beta^2}$ , which again is the standard length-contraction result.

![Figure 11.28: A Minkowski diagram showing the worldlines of the two ends of a meter stick. The vertical axis is ct and the horizontal axis is x. The left end is at the origin A. The right end is at B. The worldline of the right end is a vertical line at x=1. A dashed line represents the x' axis, making an angle theta with the x-axis. A point E is on the worldline of the right end, such that AE is a line segment making an angle theta with the ct axis. The distance AB is 1 meter in the S frame.](ebe11179cf8065e6716a43ed187d1609_img.jpg)

Figure 11.28: A Minkowski diagram showing the worldlines of the two ends of a meter stick. The vertical axis is ct and the horizontal axis is x. The left end is at the origin A. The right end is at B. The worldline of the right end is a vertical line at x=1. A dashed line represents the x' axis, making an angle theta with the x-axis. A point E is on the worldline of the right end, such that AE is a line segment making an angle theta with the ct axis. The distance AB is 1 meter in the S frame.

Fig. 11.28

The analysis used in the above example also works for time intervals. The derivation of time dilation, using a Minkowski diagram, is the task of Exercise 11.62. And the derivation of the  $Lv/c^2$  rear-clock-ahead result is the task of Exercise 11.63.

### 11.8 The Doppler effect

#### 11.8.1 Longitudinal Doppler effect

Consider a source that emits flashes at frequency  $f'$  (in its own frame) while moving directly toward you at speed  $v$ , as shown in Fig. 11.29. With what frequency do the flashes hit your eye? In these Doppler-effect problems, you must be careful to distinguish between the time at which an event *occurs* in your frame, and the time at which you *see* the event occur. This is one of the few situations where we are concerned with the latter.

There are two effects contributing to the longitudinal Doppler effect. The first is relativistic time dilation. There is more time between the flashes in your frame, which means that they occur at a smaller frequency. The second is the everyday

![Figure 11.29: A diagram showing a light source (a sun-like symbol) moving directly toward an observer (a stick figure) at speed v. A wavy arrow labeled c points from the source to the observer, representing the light signal.](956835821cfa96b447681dedf9dc79de_img.jpg)

Figure 11.29: A diagram showing a light source (a sun-like symbol) moving directly toward an observer (a stick figure) at speed v. A wavy arrow labeled c points from the source to the observer, representing the light signal.

Fig. 11.29

Doppler effect (as with sound), arising from the motion of the source. Successive flashes have a smaller (or larger, if  $v$  is negative) distance to travel to reach your eye. This effect increases (or decreases, if  $v$  is negative) the frequency at which the flashes hit your eye.

Let's now be quantitative and find the observed frequency. The time between emissions in the source's frame is  $\Delta t' = 1/f'$ . The time between emissions in your frame is then  $\Delta t = \gamma \Delta t'$ , by the usual time dilation. So the photons of one flash have traveled a distance (in your frame) of  $c\Delta t = c\gamma \Delta t'$  by the time the next flash occurs. During this time between emissions, the source has traveled a distance  $v\Delta t = v\gamma \Delta t'$  toward you in your frame. Therefore, at the instant the next flash occurs, the photons of this next flash are a distance (in your frame) of  $c\Delta t - v\Delta t = (c - v)\gamma \Delta t'$  behind the photons of the previous flash. This result holds for all adjacent flashes. The time,  $\Delta T$ , between the arrivals of the flashes at your eye is  $1/c$  times this distance, so we have

$$\Delta T = \frac{1}{c}(c - v)\gamma \Delta t' = \frac{1 - \beta}{\sqrt{1 - \beta^2}} \Delta t' = \sqrt{\frac{1 - \beta}{1 + \beta}} \left( \frac{1}{f'} \right), \quad (11.50)$$

where  $\beta = v/c$ . Therefore, the frequency you see is

$$f = \frac{1}{\Delta T} = \sqrt{\frac{1 + \beta}{1 - \beta}} f'. \quad (11.51)$$

If  $\beta > 0$  (that is, the source is moving toward you), then  $f > f'$ . The everyday Doppler effect wins out over the time-dilation effect. In this case we say that the light is “blueshifted,” because blue light is at the high-frequency end of the visible spectrum. The light need not have anything to do with the color blue, of course; by “blue” we just mean that the frequency is increased. If  $\beta < 0$  (that is, the source is moving away from you), then  $f < f'$ . Both effects serve to decrease the frequency. In this case we say that the light is “redshifted,” because red light is at the low-frequency end of the visible spectrum.

**REMARK:** We can also derive Eq. (11.51) by working in the frame of the source. In this frame, the distance between successive flashes is  $c\Delta t'$ . And since you are moving toward the source at speed  $v$ , the relative speed of you and a given flash is  $c + v$ . So the time between your running into successive flashes is  $c\Delta t'/(c + v) = \Delta t'/(1 + \beta)$ , as measured in the frame of the source. But your clock runs slow in this frame, so a time of only  $\Delta T = (1/\gamma)\Delta t'/(1 + \beta)$  elapses on your watch, which you can show agrees with the time in Eq. (11.50).

We certainly needed to obtain the same result by working in the frame of the source, because the principle of relativity states that the result can't depend on which object we consider to be the one at rest; there is no preferred frame. This is different from the situation with the standard nonrelativistic Doppler effect (relevant to a siren moving toward you), because the frequency there *does* depend on whether you or the source is the one that is moving. The reason for this is that when we say “moving” here, we mean moving with respect to the rest frame of the air, which is the medium that sound travels in. We therefore do in fact have a preferred frame of reference, unlike in relativity (where there is no “ether”). Using the arguments given above for the two different frames, but without the  $\gamma$  factors, you can show that the two nonrelativistic Doppler

results are  $f = f'/(1 - \beta)$  if the source is moving toward a stationary you, and  $f = (1 + \beta)f'$  if you are moving toward the stationary source. Here  $\beta$  is the ratio of the speed of the moving object to the speed of sound. In view of these two different results, the relativistic Doppler effect can be considered to be a simpler effect, in the sense that there is only one frequency to remember. ♣

#### 11.8.2 Transverse Doppler effect

Let's now consider a two-dimensional situation. Consider a source that emits flashes at frequency  $f'$  (in its own frame), while moving across your field of vision at speed  $v$ . There are two reasonable questions we can ask about the frequency you observe:

- **Case 1:** At the instant the source is at its closest approach to you, with what frequency do the flashes hit your eye?
- **Case 2:** When you *see* the source at its closest approach to you, with what frequency do the flashes hit your eye?

The difference between these two scenarios is shown in Fig. 11.30 and Fig. 11.31, where the source's motion is taken to be parallel to the  $x$  axis. In the first case, the photons you see must have been emitted at an earlier time, because the source moves during the nonzero time it takes the light to reach you. In this scenario, we are dealing with photons that hit your eye *when* (as measured in your frame) the source crosses the  $y$  axis. You therefore see the photons come in at an angle with respect to the  $y$  axis.

In the second case, you see the photons come in along the  $y$  axis (by the definition of this scenario). At the instant you observe one of these photons, the source is at a position past the  $y$  axis. Let's find the observed frequencies in these two cases.

**Case 1:** Let your frame be  $S$ , and let the source's frame be  $S'$ . Consider the situation from  $S'$ 's point of view.  $S'$  sees you moving across his field of vision at speed  $v$ . The relevant photons hit your eye when you cross the  $y'$  axis (defined to be the axis that passes through the source) of the  $S'$  frame.  $S'$  sees you get hit by a flash every  $\Delta t' = 1/f'$  seconds in his frame. (This is true because when you are very close to the  $y'$  axis, all points on your path are essentially equidistant from the source. So we don't have to worry about any longitudinal effects, in the  $S'$  frame.) This means that you get hit by a flash every  $\Delta T = \Delta t'/\gamma = 1/(f'\gamma)$  seconds in your frame, because  $S'$  sees your clock running slow. Therefore, the frequency in your frame is

$$f = \frac{1}{\Delta T} = \gamma f' = \frac{f'}{\sqrt{1 - \beta^2}}. \quad (11.52)$$

Hence,  $f$  is greater than  $f'$ . You see the flashes at a higher frequency than  $S'$  emits them.

![Diagram of Case 1: A source moving parallel to the x-axis, emitting a flash at the moment it crosses the y-axis. The observer is at the origin. The light ray is shown at an angle to the y-axis.](d29cd17b3b56c7d90a66be2b6b0f7634_img.jpg)

The diagram shows a 2D coordinate system with a vertical y-axis and a horizontal x-axis. A stick figure representing an observer is at the origin (0,0). A source, represented by a sun-like icon, is moving to the right (positive x-direction) with velocity v. At the exact moment the source crosses the y-axis, it emits a flash of light. A wavy line representing the light ray is shown traveling from the source's position at that moment towards the observer at an angle to the y-axis.

Diagram of Case 1: A source moving parallel to the x-axis, emitting a flash at the moment it crosses the y-axis. The observer is at the origin. The light ray is shown at an angle to the y-axis.

Fig. 11.30

![Diagram of Case 2: A source moving parallel to the x-axis, emitting a flash at a point past the y-axis. The light ray is shown traveling along the y-axis towards the observer.](156af2e6fd3a98721452246971d4ea8f_img.jpg)

The diagram shows a 2D coordinate system with a vertical y-axis and a horizontal x-axis. A stick figure representing an observer is at the origin (0,0). A source, represented by a sun-like icon, is moving to the right (positive x-direction) with velocity v. The source is at a position to the right of the y-axis. A wavy line representing a light ray is shown traveling vertically along the y-axis from the source's current position towards the observer. This represents the light that the observer sees at the moment the source is at its closest approach.

Diagram of Case 2: A source moving parallel to the x-axis, emitting a flash at a point past the y-axis. The light ray is shown traveling along the y-axis towards the observer.

Fig. 11.31

**Case 2:** Again, let your frame be  $S$ , and let the source’s frame be  $S'$ . Consider the situation from your point of view. Because of time dilation, a clock on the source runs slow (in your frame) by a factor of  $\gamma$ . So you get hit by a flash every  $\Delta T = \gamma \Delta t' = \gamma/f'$  seconds in your frame. (We have used the fact that the relevant photons are emitted from points that are essentially equidistant from you. So they all travel the same distance, and we don’t have to worry about any longitudinal effects, in your frame.) When you see the source cross the  $y$  axis, you therefore observe a frequency of

$$f = \frac{1}{\Delta T} = \frac{1}{\gamma \Delta t'} = \frac{f'}{\gamma} = f' \sqrt{1 - \beta^2}. \quad (11.53)$$

Hence,  $f$  is smaller than  $f'$ . You see the flashes at a lower frequency than  $S'$  emits them.

When people talk about the “transverse Doppler effect,” they sometimes mean Case 1, and they sometimes mean Case 2. The title “transverse Doppler” is therefore ambiguous, so you should remember to state exactly which scenario you are talking about. Other cases that are “in between” these two can also be considered. But they get a bit messy.

![Diagram showing two circular motion scenarios. Case 1: A source (star icon) is at the center of a circle, and a receiver (R in a box) is on the circumference. Case 2: A receiver (R in a box) is at the center of a circle, and a source (star icon) is on the circumference. Arrows on the circles indicate counter-clockwise motion.](ed508e94b96ef451db3c7609e006eb69_img.jpg)

Diagram showing two circular motion scenarios. Case 1: A source (star icon) is at the center of a circle, and a receiver (R in a box) is on the circumference. Case 2: A receiver (R in a box) is at the center of a circle, and a source (star icon) is on the circumference. Arrows on the circles indicate counter-clockwise motion.

**Fig. 11.32**

##### **REMARKS:**

1. The two scenarios may alternatively be described, respectively (as you can convince yourself), in the following ways (see Fig. 11.32).

- **Case 1:** A receiver moves with speed  $v$  in a circle around a source. What frequency does the receiver register?
- **Case 2:** A source moves with speed  $v$  in a circle around a receiver. What frequency does the receiver register?

These two setups make it clear that the results in Eqs. (11.52) and (11.53) arise from a simple time-dilation argument used by the inertial object at the center of each circle. These setups involve accelerating objects. We must therefore invoke the fact (which has plenty of experimental verification) that if an inertial observer looks at a moving clock, then only the instantaneous speed of the clock is important in computing the time-dilation factor. The acceleration is irrelevant.<sup>34</sup>

2. Beware of the following incorrect reasoning for Case 1, leading to an incorrect version of Eq. (11.52). “ $S$  sees things in  $S'$  slowed down by a factor  $\gamma$  (that is,  $\Delta t = \gamma \Delta t'$ ), by the usual time-dilation effect. Hence,  $S$  sees the light flashing at a slower pace. Therefore,  $f = f'/\gamma$ .” This reasoning puts the  $\gamma$  in the wrong place. Where is the error? The error lies in confusing the time at which an event *occurs* in  $S'$ ’s frame, with the time at which  $S$  *sees* (with his eyes) the event occur. The flashes certainly *occur* at a lower frequency in  $S$ , but due to the motion of  $S'$  relative to  $S$ , it turns out that the flashes meet  $S$ ’s eye at a faster rate, because the source is moving slightly toward  $S$  while it is emitting the relevant photons. You can work out the details from  $S$ ’s point of view.<sup>35</sup>

<sup>34</sup> The acceleration is, however, very important if things are considered from an accelerating object’s point of view. But we’ll wait until Chapter 14 on General Relativity to talk about this.

<sup>35</sup> This is a fun exercise (Exercise 11.66), but it should convince you that it’s much easier to look at things in the frame in which there are no longitudinal effects, as we did in our solutions above.

Alternatively, the error can be stated as follows. The time dilation result,  $\Delta t = \gamma \Delta t'$ , rests on the assumption that the  $\Delta x'$  between the two events is zero. This applies fine to two emissions of light from the source. However, the two events in question are the absorption of two light flashes by your eye (which is moving in  $S'$ ), so  $\Delta t = \gamma \Delta t'$  is not applicable. Instead,  $\Delta t' = \gamma \Delta t$  is the relevant result, valid when  $\Delta x = 0$ . (But we still need to invoke the fact that all the relevant photons travel the same distance, which means that we don't have to worry about any longitudinal effects.) ♣

### 11.9 Rapidity

#### 11.9.1 Definition

Let us define the *rapidity*,  $\phi$ , by

$$\tanh \phi \equiv \beta \equiv \frac{v}{c}. \quad (11.54)$$

A few properties of the hyperbolic trig functions are given in Appendix A. In particular,  $\tanh \phi \equiv (e^\phi - e^{-\phi})/(e^\phi + e^{-\phi})$ . The rapidity defined in Eq. (11.54) is very useful in relativity because many of our expressions take on a particularly nice form when written in terms of it. Consider, for example, the velocity-addition formula. Let  $\beta_1 = \tanh \phi_1$  and  $\beta_2 = \tanh \phi_2$ . Then if we add  $\beta_1$  and  $\beta_2$  using the velocity-addition formula, Eq. (11.31), we obtain

$$\frac{\beta_1 + \beta_2}{1 + \beta_1 \beta_2} = \frac{\tanh \phi_1 + \tanh \phi_2}{1 + \tanh \phi_1 \tanh \phi_2} = \tanh(\phi_1 + \phi_2), \quad (11.55)$$

where we have used the addition formula for  $\tanh \phi$ , which you can prove by writing things in terms of the exponentials,  $e^{\pm\phi}$ . Therefore, while the velocities add in the strange manner of Eq. (11.31), the rapidities add by standard addition.

The Lorentz transformations also take a nice form when written in terms of the rapidity. Our friendly  $\gamma$  factor can be written as

$$\gamma \equiv \frac{1}{\sqrt{1 - \beta^2}} = \frac{1}{\sqrt{1 - \tanh^2 \phi}} = \cosh \phi. \quad (11.56)$$

Also,

$$\gamma \beta \equiv \frac{\beta}{\sqrt{1 - \beta^2}} = \frac{\tanh \phi}{\sqrt{1 - \tanh^2 \phi}} = \sinh \phi. \quad (11.57)$$

Therefore, the Lorentz transformations in matrix form, Eqs. (11.22), become

$$\begin{pmatrix} x \\ ct \end{pmatrix} = \begin{pmatrix} \cosh \phi & \sinh \phi \\ \sinh \phi & \cosh \phi \end{pmatrix} \begin{pmatrix} x' \\ ct' \end{pmatrix}. \quad (11.58)$$

This transformation looks similar to a rotation in a plane, which is given by

$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x' \\ y' \end{pmatrix}, \quad (11.59)$$

except that we now have hyperbolic trig functions instead of trig functions. The fact that the interval  $s^2 \equiv c^2 t^2 - x^2$  does not depend on the frame is clear from Eq. (11.58), because the cross terms in the squares cancel, and  $\cosh^2 \phi - \sinh^2 \phi = 1$ . (Compare with the invariance of  $r^2 \equiv x^2 + y^2$  for rotations in a plane, where the cross terms from Eq. (11.59) likewise cancel, and  $\cos^2 \theta + \sin^2 \theta = 1$ .)

The quantities associated with a Minkowski diagram also take a nice form when written in terms of the rapidity. The angle between the  $S$  and  $S'$  axes satisfies

$$\tan \theta = \beta = \tanh \phi. \quad (11.60)$$

And the size of one unit on the  $x'$  or  $ct'$  axes is, from Eq. (11.46),

$$\sqrt{\frac{1 + \beta^2}{1 - \beta^2}} = \sqrt{\frac{1 + \tanh^2 \phi}{1 - \tanh^2 \phi}} = \sqrt{\cosh^2 \phi + \sinh^2 \phi} = \sqrt{\cosh 2\phi}. \quad (11.61)$$

For large  $\phi$ , this is approximately equal to  $e^\phi / \sqrt{2}$ .

#### 11.9.2 Physical meaning

The fact that the rapidity makes many of our formulas look nice and pretty is reason enough to consider it. But in addition, it turns out to have a very meaningful physical interpretation. Consider the following setup. A spaceship is initially at rest in the lab frame. At a given instant, it starts to accelerate. Let  $a$  be the *proper acceleration*, which is defined as follows. Let  $t$  be the time coordinate in the spaceship's frame.<sup>36</sup> If the proper acceleration is  $a$ , then at time  $t + dt$ , the spaceship is moving at speed  $a dt$  relative to the frame it was in at time  $t$ . An equivalent definition is that the astronaut feels a force of  $ma$  applied to his body by the spaceship. If he is standing on a scale, then the scale shows a reading of  $F = ma$ .

What is the relative speed of the spaceship and the lab frame at (the spaceship's) time  $t$ ? We can answer this question by considering two nearby times and using the velocity-addition formula, Eq. (11.31). From the definition of  $a$ , Eq. (11.31) gives, with  $v_1 \equiv a dt$  and  $v_2 \equiv v(t)$ ,

$$v(t + dt) = \frac{v(t) + a dt}{1 + v(t)a dt/c^2}. \quad (11.62)$$

<sup>36</sup> This frame is of course changing as time goes by, because the spaceship is accelerating. The time  $t$  is simply the spaceship's proper time. Normally, we would denote this by  $t'$ , but we don't want to have to keep writing the primes over and over in the following calculation.

Expanding this to first order in  $dt$  yields<sup>37</sup>

$$\frac{dv}{dt} = a \left( 1 - \frac{v^2}{c^2} \right) \implies \int_0^v \frac{dv}{1 - v^2/c^2} = \int_0^t a \, dt. \quad (11.63)$$

Separating variables and integrating gives, using  $\int dz/(1-z^2) = \tanh^{-1}z$ ,<sup>38</sup> and assuming that  $a$  is constant,

$$v(t) = c \tanh(at/c). \quad (11.64)$$

For small  $a$  or small  $t$  (more precisely, for  $at/c \ll 1$ ), we obtain  $v(t) \approx at$ , as we should (because  $\tanh z \approx z$  for small  $z$ , which follows from the exponential form of  $\tanh$ ). And for  $at/c \gg 1$ , we obtain  $v(t) \approx c$ , as we should. If  $a$  happens to be a function of time,  $a(t)$ , then we can't take the  $a$  outside the integral in Eq. (11.63), so we instead end up with the general formula,

$$v(t) = c \tanh \left( \frac{1}{c} \int_0^t a(t) \, dt \right). \quad (11.65)$$

The rapidity  $\phi$ , as defined in Eq. (11.54), is therefore given by

$$\phi(t) \equiv \frac{1}{c} \int_0^t a(t) \, dt. \quad (11.66)$$

Note that whereas  $v$  has  $c$  as a limiting value,  $\phi$  can become arbitrarily large. Looking at Eq. (11.65) we see that the  $\phi$  associated with a given  $v$  is  $1/mc$  times the time integral of the force (felt by the astronaut) that is needed to bring the astronaut up to speed  $v$ . By applying a force for an arbitrarily long time, we can make  $\phi$  arbitrarily large.

The integral  $\int a(t) \, dt$  may be described as the naive, incorrect speed. That is, it is the speed that the astronaut might think he has, if he has his eyes closed and knows nothing about the theory of relativity. And indeed, his thinking would be essentially correct for small speeds. This quantity  $\int a(t) \, dt = \int F(t) \, dt/m$  looks like a reasonably physical thing, so it seems like it should have *some* meaning. And indeed, although it doesn't equal  $v$ , all you have to do to get  $v$  is take a  $\tanh$  and throw in some factors of  $c$ .

The fact that rapidities add via simple addition when using the velocity-addition formula, as we saw in Eq. (11.55), is evident from Eq. (11.65). There is really nothing more going on here than the fact that

$$\int_{t_0}^{t_2} a(t) \, dt = \int_{t_0}^{t_1} a(t) \, dt + \int_{t_1}^{t_2} a(t) \, dt. \quad (11.67)$$

<sup>37</sup> Equivalently, just take the derivative of  $(v+w)/(1+vw/c^2)$  with respect to  $w$ , and then set  $w=0$ .

<sup>38</sup> Alternatively, you can use  $1/(1-z^2) = 1/(2(1-z)) + 1/(2(1+z))$ , and then integrate to obtain some logs, which then yield the  $\tanh$ . You can also use the result of Problem 11.17 to find  $v(t)$ . See the remark in the solution to that problem (after trying to solve it, of course!).

To be explicit, let a force be applied from  $t_0$  to  $t_1$  that brings a mass up to a speed of (dropping the  $c$ 's)  $\beta_1 = \tanh \phi_1 = \tanh \left( \int_{t_0}^{t_1} a \, dt \right)$ , and then let an additional force be applied from  $t_1$  to  $t_2$  that adds on an additional speed of  $\beta_2 = \tanh \phi_2 = \tanh \left( \int_{t_1}^{t_2} a \, dt \right)$ , relative to the frame at  $t_1$ . Then the resulting speed may be looked at in two ways: (1) it is the result of relativistically adding the speeds  $\beta_1 = \tanh \phi_1$  and  $\beta_2 = \tanh \phi_2$ , and (2) it is the result of applying the force from  $t_0$  to  $t_2$  (you get the same final speed, of course, whether or not you bother to record the speed along the way at  $t_1$ ), which is  $\beta = \tanh \left( \int_{t_0}^{t_2} a \, dt \right) = \tanh(\phi_1 + \phi_2)$ , where the second equality comes from the statement, Eq. (11.67), that integrals simply add. Therefore, the relativistic addition of  $\tanh \phi_1$  and  $\tanh \phi_2$  gives  $\tanh(\phi_1 + \phi_2)$ , as we wanted to show. Note that this reasoning doesn't rely on the fact that the function here is a  $\tanh$ . It could be anything. If we lived in a world where the speed were given by, for example,  $\beta = \tan \left( \int a \, dt \right)$ , then the rapidities would still add via simple addition. It's just that in our world we have a  $\tanh$ . (We'll see in the next section that a "tan" world would have issues, anyway.)

### 11.10 Relativity without $c$

In Section 11.2, we introduced the two postulates of Special Relativity, namely the speed-of-light postulate and the relativity postulate. Appendix I gives a derivation of the Lorentz transformations that works directly from these two postulates and doesn't use the three fundamental effects, which were the basis of the derivation in Section 11.4.1. It's interesting to see what happens if we relax these postulates. It's hard to imagine a reasonable (empty) universe where the relativity postulate doesn't hold, but it's easy to imagine a universe where the speed of light depends on the reference frame. Light could behave like a baseball, for example. So let's drop the speed-of-light postulate now and see what we can say about the coordinate transformations between frames, using only the relativity postulate. For further discussion of this topic, see Lee and Kalotas (1975) and references therein.

In Appendix I, the form of the transformations, just prior to invoking the speed-of-light postulate, is given in Eq. (I.8) as

$$\begin{aligned} x &= A_v(x' + vt'), \\ t &= A_v \left( t' + \frac{1}{v} \left( 1 - \frac{1}{A_v^2} \right) x' \right). \end{aligned} \quad (11.68)$$

We'll put a subscript on  $A$  in this section, to remind us of the  $v$  dependence. Can we say anything about  $A_v$  without invoking the speed-of-light postulate? Indeed we can. Define  $V_v$  by

$$\frac{1}{V_v^2} \equiv \frac{1}{v^2} \left( 1 - \frac{1}{A_v^2} \right) \implies A_v = \frac{1}{\sqrt{1 - v^2/V_v^2}}. \quad (11.69)$$

We have picked the positive square root because when  $v = 0$  we should have  $x = x'$  and  $t = t'$ . Equations (11.68) now become

$$\begin{aligned} x &= \frac{1}{\sqrt{1 - v^2/V_v^2}}(x' + vt'), \\ t &= \frac{1}{\sqrt{1 - v^2/V_v^2}}\left(\frac{v}{V_v^2}x' + t'\right). \end{aligned} \quad (11.70)$$

All we've done so far is make a change of variables. But we now make the following claim.

**Claim 11.1**  $V_v^2$  is independent of  $v$ .

**Proof:** As stated in the last remark in Section 11.4.1, we know that two successive applications of the transformations in Eqs. (11.70) must again yield a transformation of the same form. Consider a transformation characterized by velocity  $v_1$ , and another one characterized by velocity  $v_2$ . For simplicity, define

$$\begin{aligned} V_1 &\equiv V_{v_1}, \quad V_2 \equiv V_{v_2}, \\ \gamma_1 &\equiv \frac{1}{\sqrt{1 - v_1^2/V_1^2}}, \quad \gamma_2 \equiv \frac{1}{\sqrt{1 - v_2^2/V_2^2}}. \end{aligned} \quad (11.71)$$

To calculate the composite transformation, it is easiest to use matrix notation. Looking at Eqs. (11.70), we see that the composite transformation is given by the matrix

$$\begin{pmatrix} \gamma_2 & \gamma_2 v_2 \\ \gamma_2 \frac{v_2}{V_2^2} & \gamma_2 \end{pmatrix} \begin{pmatrix} \gamma_1 & \gamma_1 v_1 \\ \gamma_1 \frac{v_1}{V_1^2} & \gamma_1 \end{pmatrix} = \gamma_1 \gamma_2 \begin{pmatrix} 1 + \frac{v_1 v_2}{V_1^2} & v_2 + v_1 \\ \frac{v_1}{V_1^2} + \frac{v_2}{V_2^2} & 1 + \frac{v_1 v_2}{V_2^2} \end{pmatrix}. \quad (11.72)$$

The composite transformation must still be of the form of Eqs. (11.70). But this implies that the upper-left and lower-right entries of the composite matrix must be equal. Therefore,  $V_1^2 = V_2^2$ . Since this holds for arbitrary  $v_1$  and  $v_2$ , we see that  $V_v^2$  must be a constant. So it is independent of  $v$ . ■

Denote the constant value of  $V_v^2$  by  $V^2$ . Then the coordinate transformations in Eq. (11.70) become

$$\begin{aligned} x &= \frac{1}{\sqrt{1 - v^2/V^2}}(x' + vt'), \\ t &= \frac{1}{\sqrt{1 - v^2/V^2}}\left(t' + \frac{v}{V^2}x'\right). \end{aligned} \quad (11.73)$$

We have obtained this result using only the relativity postulate. These transformations have the same form as the Lorentz transformations in Eqs. (11.17).

The only extra information in Eqs. (11.17) is that  $V$  equals the speed of light,  $c$ . It is remarkable that we were able to prove so much by using only the relativity postulate.

We can say a few more things. There are four basic possibilities for the value of  $V^2$ . However, two of these are not physical.

- $V^2 = \infty$ : This gives the Galilean transformations,  $x = x' + vt'$  and  $t = t'$ .
- $0 < V^2 < \infty$ : This gives transformations of the Lorentz type.  $V$  is the limiting speed of an object. Experiments show that this case is the one that corresponds to the world we live in.
- $V^2 = 0$ : This case isn't physical, because any nonzero value of  $v$  makes the  $\gamma$  factor imaginary (and infinite). Nothing could ever move.
- $V^2 < 0$ : It turns out that this case is also not physical. You might be concerned that the square of  $V$  is less than zero, but this is fine because  $V$  appears in the transformations (11.73) only through its square. There is no need for  $V$  to actually be the speed of anything. The trouble is that the nature of Eqs. (11.73) implies the possibility of time reversal. This opens the door for causality violation and all the other problems associated with time reversal. We therefore reject this case. To be more explicit, define  $b^2 \equiv -V^2$ , where  $b$  is a positive number. Then Eqs. (11.73) may be written in the form,

$$\begin{aligned} x &= x' \cos \theta + (bt') \sin \theta, \\ bt &= -x' \sin \theta + (bt') \cos \theta, \end{aligned} \quad (11.74)$$

where  $\tan \theta \equiv v/b$ . Also,  $-\pi/2 \leq \theta \leq \pi/2$ , because the positive sign of the  $x'$  and  $t'$  coefficients in Eqs. (11.73) implies that the  $\cos \theta$  in Eqs. (11.74) satisfies  $\cos \theta \geq 0$ . We have the normal trig functions in Eqs. (11.74) instead of the hyperbolic trig functions in the Lorentz transformation in Eqs. (11.58). This present transformation is simply a rotation of the axes through an angle  $\theta$  in the plane. The  $S$  axes are rotated counter-clockwise (as you can check) by an angle  $\theta$  relative to the  $S'$  axes. Equivalently, the  $S'$  axes are rotated clockwise by an angle  $\theta$  relative to the  $S$  axes.

Equations (11.74) satisfy the requirement that the composition of two transformations is again a transformation of the same form. Rotation by  $\theta_1$ , and then by  $\theta_2$ , yields a rotation by  $\theta_1 + \theta_2$ . However, if  $\theta_1$  and  $\theta_2$  are positive, and if the resulting rotation is through an angle  $\theta$  that is greater than  $90^\circ$ , then we have a problem. The tangent of such an angle is negative. Therefore,  $\tan \theta = v/b$  implies that  $v$  is negative.

This situation is shown in Fig. 11.33. Frame  $S''$  moves at velocity  $v_2 > 0$  with respect to frame  $S'$ , which moves at velocity  $v_1 > 0$  with respect to frame  $S$ . From the figure, we see that someone standing at rest in frame  $S''$  (that is, someone whose worldline is the  $bt''$  axis) is going to have some serious issues in frame  $S$ . For one, the  $bt''$  axis has a negative slope in frame  $S$ , which means that as  $t$  increases,  $x$  decreases. The person is therefore moving at a *negative* velocity with respect to  $S$ . Adding two positive velocities and obtaining a negative one is clearly absurd. But even worse, someone standing at rest in  $S''$  is moving in the positive direction along the  $bt''$  axis, which means that he is traveling *backwards* in time in  $S$ . That is, he will die before he is born. This is not good.

![Figure 11.33: A diagram showing the rotation of coordinate axes. The original axes are x and bt. The first set of rotated axes, S', are x' and bt', rotated counter-clockwise by an angle theta_1. The second set of rotated axes, S'', are x'' and bt'', rotated counter-clockwise by an additional angle theta_2 from the S' axes. The bt'' axis has a negative slope in the original S frame, indicating a negative velocity.](1da636242b4bce3defade78e7e9334b7_img.jpg)

Figure 11.33: A diagram showing the rotation of coordinate axes. The original axes are x and bt. The first set of rotated axes, S', are x' and bt', rotated counter-clockwise by an angle theta\_1. The second set of rotated axes, S'', are x'' and bt'', rotated counter-clockwise by an additional angle theta\_2 from the S' axes. The bt'' axis has a negative slope in the original S frame, indicating a negative velocity.

Fig. 11.33

An equivalent method of dismissing this case, given in Lee and Kalotas (1977), but one that doesn't specifically refer to causality violation, is to note that the transformations in Eqs. (11.74) don't form a closed group. In other words, successive applications of the transformations can eventually yield a transformation that isn't of the form in Eqs. (11.74), due to the  $-\pi/2 \leq \theta \leq \pi/2$  restriction. (In contrast, the rotations in a plane form a closed group, because there are no restrictions on what  $\theta$  can be.) This argument is equivalent to the time-reversal argument above, because  $-\pi/2 \leq \theta \leq \pi/2$  is equivalent to  $\cos \theta \geq 0$ , which is equivalent to the statement that the coefficients of  $t$  and  $t'$  in Eqs. (11.74) have the same sign.

Note that all of the finite  $0 < V^2 < \infty$  possibilities are essentially the same. Any difference in the numerical value of  $V$  can be absorbed into the definitions of the unit sizes for  $x$  and  $t$ . Given that  $V$  is finite, it has to be *something*, so it doesn't make sense to put much importance on its numerical value. There is therefore only one decision to be made when constructing the spacetime structure of an (empty) universe. You just have to say whether  $V$  is finite or infinite, that is, whether the universe is Lorentzian or Galilean. Equivalently, all you have to say is whether or not there is an upper limit on the speed of any object. If there is, then you can simply postulate the existence of something that moves with this limiting speed. In other words, to create your universe, you simply have to say, "Let there be light."

### 11.11 Problems

### Section 11.3: The fundamental effects

#### 11.1. No transverse length contraction \*

Two meter sticks,  $A$  and  $B$ , move past each other as shown in Fig. 11.34. Stick  $A$  has paint brushes on its ends. Use this setup to show that in the frame of one stick, the other stick still has a length of one meter.

![Diagram showing two vertical meter sticks, A and B, moving towards each other. Stick A is on the left with an arrow pointing right, and stick B is on the right with an arrow pointing left. Both sticks have small squares at their top and bottom ends.](c3e9ccbcb986694724265631af4177ac_img.jpg)

Diagram showing two vertical meter sticks, A and B, moving towards each other. Stick A is on the left with an arrow pointing right, and stick B is on the right with an arrow pointing left. Both sticks have small squares at their top and bottom ends.

Fig. 11.34

#### 11.2. Explaining time dilation \*\*

Two planets,  $A$  and  $B$ , are at rest with respect to each other, a distance  $L$  apart, with synchronized clocks. A spaceship flies at speed  $v$  past planet  $A$  toward planet  $B$  and synchronizes its clock with  $A$ 's right when it passes  $A$  (they both set their clocks to zero). The spaceship eventually flies past planet  $B$  and compares its clock with  $B$ 's. We know, from working in the planets' frame, that when the spaceship reaches  $B$ ,  $B$ 's clock reads  $L/v$ . And the spaceship's clock reads  $L/\gamma v$ , because it runs slow by a factor of  $\gamma$  when viewed in the planets' frame.

How would someone on the spaceship quantitatively explain to you why  $B$ 's clock reads  $L/v$  (which is *more* than its own  $L/\gamma v$ ), considering that the spaceship sees  $B$ 's clock running *slow*?

#### **11.3. Explaining length contraction \*\***

Two bombs lie on a train platform, a distance  $L$  apart. As a train passes by at speed  $v$ , the bombs explode simultaneously (in the platform frame) and leave marks on the train. Due to the length contraction of the train, we know that the marks on the train are a distance  $\gamma L$  apart when viewed in the train's frame, because this distance is what is length-contracted down to the given distance  $L$  in the platform frame.

How would someone on the train quantitatively explain why the marks are a distance  $\gamma L$  apart, considering that the bombs are a distance of only  $L/\gamma$  apart in the train frame?

#### **11.4. A passing stick \*\***

A stick of length  $L$  moves past you at speed  $v$ . There is a time interval between the front end coinciding with you and the back end coinciding with you. What is this time interval in

- your frame? (Calculate this by working in your frame.)
- your frame? (Work in the stick's frame.)
- the stick's frame? (Work in your frame. This is the tricky one.)
- the stick's frame? (Work in the stick's frame.)

#### **11.5. Rotated square \*\***

A square with side  $L$  flies past you at speed  $v$ , in a direction parallel to two of its sides. You stand in the plane of the square. When you see the square at its nearest point to you, show that it *looks* to you like it is rotated, instead of contracted. (Assume that  $L$  is small compared with the distance between you and the square.)

#### **11.6. Train in a tunnel \*\***

A train and a tunnel both have proper lengths  $L$ . The train moves toward the tunnel at speed  $v$ . A bomb is located at the front of the train. The bomb is designed to explode when the front of the train passes the far end of the tunnel. A deactivation sensor is located at the back of the train. When the back of the train passes the near end of the tunnel, the sensor tells the bomb to disarm itself. Does the bomb explode?

![Diagram (lab frame) showing a ruler and a stick. The ruler is horizontal with tick marks. The stick is also horizontal, positioned to the right of the ruler. The stick's length is labeled L/γ. A person icon stands to the left of the ruler. A velocity vector v points to the right, indicating the stick is moving towards the ruler.](752829b3503eb2ac0898c3fdef18ec25_img.jpg)

Diagram (lab frame) showing a ruler and a stick. The ruler is horizontal with tick marks. The stick is also horizontal, positioned to the right of the ruler. The stick's length is labeled L/γ. A person icon stands to the left of the ruler. A velocity vector v points to the right, indicating the stick is moving towards the ruler.

![Diagram (stick frame) showing a ruler and a stick. The ruler is horizontal. The stick is horizontal and longer than the ruler, with its length labeled L. A person icon stands below the ruler. A velocity vector v points to the left, indicating the ruler is moving towards the stick. The stick's right end is at a wall.](cda009a93bba4009da6871b5a80add08_img.jpg)

Diagram (stick frame) showing a ruler and a stick. The ruler is horizontal. The stick is horizontal and longer than the ruler, with its length labeled L. A person icon stands below the ruler. A velocity vector v points to the left, indicating the ruler is moving towards the stick. The stick's right end is at a wall.

#### **11.7. Seeing behind the stick \*\***

A ruler is positioned perpendicular to a wall, and you stand at rest with respect to the ruler and the wall. A stick of length  $L$  flies by at speed  $v$ . It travels in front of the ruler, so that it obscures part of the ruler from your view. When the stick hits the wall it stops. Which of the following two reasonings is correct (and what is wrong with the incorrect one)?

In your reference frame, the stick is shorter than  $L$ . Therefore, right before it hits the wall, you are able to see a mark on the ruler that is closer than  $L$  units to the wall (see Fig. 11.35).

**Fig. 11.35**

But in the stick's frame, the marks on the ruler are closer together. Therefore, when the wall hits the stick, the closest mark to the wall that you can see on the ruler is greater than  $L$  units (see Fig. 11.35).

#### 11.8. Cookie cutter \*\*

Cookie dough (chocolate chip, of course) lies on a conveyor belt that moves at speed  $v$ . A circular stamp stamps out cookies as the dough rushes by beneath it. When you buy these cookies in a store, what shape are they? That is, are they squashed in the direction of the belt, stretched in that direction, or circular?

#### 11.9. Getting shorter \*\*

Two balls move with speed  $v$  along a line toward two people standing along the same line. The proper distance between the balls is  $\gamma L$ , and the proper distance between the people is  $L$ . Due to length contraction, the people measure the distance between the balls to be  $L$ , so the balls pass the people simultaneously (as measured by the people), as shown in Fig. 11.36. Assume that the people's clocks both read zero at this time. If the people catch the balls, then the resulting proper distance between the balls becomes  $L$ , which is shorter than the initial proper distance of  $\gamma L$ . Your task: By working in the frame in which the balls are initially at rest, explain how the proper distance between the balls decreases from  $\gamma L$  to  $L$ . Do this in the following way.

![Figure 11.36: A diagram showing two people (stick figures) and two balls (black dots) on a horizontal line. The balls are moving towards the people with speed v, as indicated by arrows above the balls. The people are standing still.](32bf1b07d772fec7350b787aa7894203_img.jpg)

Figure 11.36: A diagram showing two people (stick figures) and two balls (black dots) on a horizontal line. The balls are moving towards the people with speed v, as indicated by arrows above the balls. The people are standing still.

Fig. 11.36

- Draw the beginning and ending pictures for the process. Indicate the readings on both clocks in the two pictures, and label all relevant lengths.
- Using the distances labeled in your pictures, how far do the people travel? Using the times labeled in your pictures, how far do the people travel? Show that these two methods give the same result.
- Explain in words how the proper distance between the balls decreases from  $\gamma L$  to  $L$ .

### Section 11.4: The Lorentz transformations

#### 11.10. A bunch of L.T.'s \*

Verify that the values of  $\Delta x$  and  $\Delta t$  in the table in the "Passing trains" example in Section 11.6 satisfy the L.T.'s between the six pairs of frames, namely  $AB$ ,  $AC$ ,  $AD$ ,  $BC$ ,  $BD$ , and  $CD$  (see Fig. 11.37).

![Figure 11.37: A diagram showing three frames of reference. Frame A is a rectangle with a right-pointing arrow labeled 4c/5. Frame B is a rectangle with a right-pointing arrow labeled 3c/5. Frame D is a rectangle with a right-pointing arrow labeled 3c/5. Frame C is a stick figure with a right-pointing arrow labeled 3c/5.](0fff1f80274222a9d840198aadd9001a_img.jpg)

Figure 11.37: A diagram showing three frames of reference. Frame A is a rectangle with a right-pointing arrow labeled 4c/5. Frame B is a rectangle with a right-pointing arrow labeled 3c/5. Frame D is a rectangle with a right-pointing arrow labeled 3c/5. Frame C is a stick figure with a right-pointing arrow labeled 3c/5.

Fig. 11.37

### Section 11.5: Velocity addition

#### 11.11. Equal speeds \*

$A$  and  $B$  travel at  $4c/5$  and  $3c/5$  with respect to the ground, as shown in Fig. 11.38. How fast should  $C$  travel so that she sees  $A$  and  $B$  approaching her at the same speed? What is this speed?

![Figure 11.38: A diagram showing three points A, C, and B on a horizontal line. Point A has a right-pointing arrow labeled 4c/5. Point C has a right-pointing arrow labeled ? (unknown). Point B has a right-pointing arrow labeled 3c/5.](62d44e3683b3805967ced11aab4884d2_img.jpg)

Figure 11.38: A diagram showing three points A, C, and B on a horizontal line. Point A has a right-pointing arrow labeled 4c/5. Point C has a right-pointing arrow labeled ? (unknown). Point B has a right-pointing arrow labeled 3c/5.

Fig. 11.38

![Diagram for Fig. 11.39: Three points A, C, and B are shown on a horizontal line. Point A has a velocity vector v pointing right. Point C has a velocity vector with a question mark pointing right. Point B is stationary.](c3a742279c7e4d07c58268994a863c83_img.jpg)

Diagram for Fig. 11.39: Three points A, C, and B are shown on a horizontal line. Point A has a velocity vector v pointing right. Point C has a velocity vector with a question mark pointing right. Point B is stationary.

Fig. 11.39

![Diagram for Fig. 11.40: Two vectors originate from a common point. The upper vector has magnitude v and makes an angle theta with a horizontal dashed line. The lower vector also has magnitude v and makes an angle theta with the horizontal dashed line, so the total angle between them is 2*theta.](b2ff07fc77974cf968f0545a86062b1f_img.jpg)

Diagram for Fig. 11.40: Two vectors originate from a common point. The upper vector has magnitude v and makes an angle theta with a horizontal dashed line. The lower vector also has magnitude v and makes an angle theta with the horizontal dashed line, so the total angle between them is 2\*theta.

Fig. 11.40

![Diagram for Fig. 11.41: Two vectors originate from a common point. The lower vector has magnitude u and points horizontally to the right. The upper vector has magnitude v and makes an angle theta with the lower vector.](8200a5069e5b6b06d20352f3e0049793_img.jpg)

Diagram for Fig. 11.41: Two vectors originate from a common point. The lower vector has magnitude u and points horizontally to the right. The upper vector has magnitude v and makes an angle theta with the lower vector.

Fig. 11.41

![Diagram for Fig. 11.42: Two frames of reference, S and S', are shown. The top part shows frame S' with a particle moving vertically upwards with velocity u' between horizontal dotted lines. Frame S is moving to the left with velocity v relative to S'. The bottom part shows the same situation from frame S, where the particle moves along a diagonal path with a vertical component u and a horizontal component v to the right.](bf38af8963366a758c75bc94a67070f2_img.jpg)

Diagram for Fig. 11.42: Two frames of reference, S and S', are shown. The top part shows frame S' with a particle moving vertically upwards with velocity u' between horizontal dotted lines. Frame S is moving to the left with velocity v relative to S'. The bottom part shows the same situation from frame S, where the particle moves along a diagonal path with a vertical component u and a horizontal component v to the right.

Fig. 11.42

#### **11.12. More equal speeds \*\***

$A$  travels at speed  $v$  with respect to the ground, and  $B$  is at rest, as shown in Fig. 11.39. How fast should  $C$  travel so that she sees  $A$  and  $B$  approaching her at the same speed? In the ground frame ( $B$ 's frame), what is the ratio of the distances  $CB$  and  $AC$  (assume that  $A$  and  $C$  arrive at  $B$  at the same time)? The answer to this is very nice and clean. Can you think of a simple intuitive explanation for the result?

#### **11.13. Equal transverse speeds \***

In the lab frame, an object moves with velocity  $(u_x, u_y)$ , and you move with velocity  $v$  in the  $x$  direction. What should  $v$  be so that you also see the object move with velocity  $u_y$  in your  $y$  direction? One solution is of course  $v = 0$ . Find the other one.

#### **11.14. Relative speed \***

In the lab frame, two particles move with speed  $v$  along the paths shown in Fig. 11.40. The angle between the trajectories is  $2\theta$ . What is the speed of one particle, as viewed by the other? (Note: This problem is posed again in Chapter 13, where it can be solved in a much simpler way, using 4-vectors.)

#### **11.15. Another relative speed \*\***

In the lab frame, particles  $A$  and  $B$  move with speeds  $u$  and  $v$  along the paths shown in Fig. 11.41. The angle between the trajectories is  $\theta$ . What is the speed of one particle, as viewed by the other? (Note: This problem is posed again in Chapter 13, where it can be solved in a much simpler way, using 4-vectors.)

#### **11.16. Transverse velocity addition \*\***

For the special case of  $u'_x = 0$ , the transverse velocity-addition formula, Eq. (11.38), yields  $u_y = u'_y/\gamma$ . Derive this in the following way: In frame  $S'$ , a particle moves with velocity  $(0, u')$ , as shown in the first picture in Fig. 11.42. Frame  $S$  moves to the left with speed  $v$ , so the situation in  $S$  looks like what is shown in the second picture in Fig. 11.42, with the  $y$  speed now  $u$ . Consider a series of equally spaced dotted lines, as shown. The ratio of the times between passes of the dotted lines in frames  $S$  and  $S'$  is  $T_S/T_{S'} = u'/u$ . Derive another expression for this ratio by using time-dilation arguments, and then equate the two expressions to solve for  $u$  in terms of  $u'$  and  $v$ .

#### **11.17. Many velocity additions \*\***

An object moves at speed  $v_1/c \equiv \beta_1$  with respect to  $S_1$ , which moves at speed  $\beta_2$  with respect to  $S_2$ , which moves at speed  $\beta_3$  with respect to  $S_3$ , and so on, until finally  $S_{N-1}$  moves at speed  $\beta_N$  with respect to  $S_N$

(see Fig. 11.43). Show by induction that the speed, call it  $\beta_{(N)}$ , of the object with respect to  $S_N$  can be written as

$$\beta_{(N)} = \frac{P_N^+ - P_N^-}{P_N^+ + P_N^-}, \quad (11.75)$$

where  $P_N^+ \equiv \prod_{i=1}^N (1 + \beta_i)$ , and  $P_N^- \equiv \prod_{i=1}^N (1 - \beta_i)$ .

![Diagram for Fig. 11.43 showing a series of nested rectangular frames S1, S2, S3, S4, S5, ... Each frame contains a dot representing an object and a velocity vector v1, v2, v3, v4, v5, ... respectively, all pointing to the right. The frames are nested, with S1 inside S2, which is inside S3, and so on.](e1c1d70f0126389b0e473fbe544bff82_img.jpg)

Diagram for Fig. 11.43 showing a series of nested rectangular frames S1, S2, S3, S4, S5, ... Each frame contains a dot representing an object and a velocity vector v1, v2, v3, v4, v5, ... respectively, all pointing to the right. The frames are nested, with S1 inside S2, which is inside S3, and so on.

Fig. 11.43

#### 11.18. Velocity addition from scratch \*\*

A ball moves at speed  $v_1$  with respect to a train. The train moves at speed  $v_2$  with respect to the ground. What is the speed of the ball with respect to the ground? Solve this problem (that is, derive the velocity-addition formula, Eq. (11.31)) in the following way (don't use time dilation, length contraction, etc; use only the relativity postulate and the fact that the speed of light is the same in any inertial frame):

Let the ball be thrown from the back of the train. At the same instant, a photon is released next to it (see Fig. 11.44). The photon heads to the front of the train, bounces off a mirror, heads back, and eventually runs into the ball. In both the frame of the train and the frame of the ground, calculate the fraction of the way along the train where the meeting occurs, and then equate these fractions.

![Diagram for Fig. 11.44 showing a horizontal line representing a train. A photon (wavy arrow) is emitted from the back (left) towards the front (right). A ball (dot) is also moving to the right with velocity v1. The train itself is moving to the right with velocity v2. A mirror is at the front of the train.](bed1161c5452bbd9603340be5dfd3d07_img.jpg)

Diagram for Fig. 11.44 showing a horizontal line representing a train. A photon (wavy arrow) is emitted from the back (left) towards the front (right). A ball (dot) is also moving to the right with velocity v1. The train itself is moving to the right with velocity v2. A mirror is at the front of the train.

Fig. 11.44

#### 11.19. Modified twin paradox \*\*\*

Consider the following variation of the twin paradox.  $A$ ,  $B$ , and  $C$  each have a clock. In  $A$ 's reference frame,  $B$  flies past  $A$  with speed  $v$  to the right. When  $B$  passes  $A$ , they both set their clocks to zero. Also, in  $A$ 's reference frame,  $C$  starts far to the right and moves to the left with speed  $v$ . When  $B$  and  $C$  pass each other,  $C$  sets his clock to read the same as  $B$ 's. Finally, when  $C$  passes  $A$ , they compare the readings on their clocks. At this moment, let  $A$ 's clock read  $T_A$ , and let  $C$ 's clock read  $T_C$ .

- Working in  $A$ 's frame, show that  $T_C = T_A/\gamma$ , where  $\gamma = 1/\sqrt{1 - v^2/c^2}$ .
- Working in  $B$ 's frame, show again that  $T_C = T_A/\gamma$ .
- Working in  $C$ 's frame, show again that  $T_C = T_A/\gamma$ .

### Section 11.6: The invariant interval

#### 11.20. Throwing on a train \*\*

A train with proper length  $L$  moves at speed  $c/2$  with respect to the ground. A ball is thrown from the back to the front, at speed  $c/3$  with

respect to the train. How much time does this take, and what distance does the ball cover, in:

- (a) The train frame?
- (b) The ground frame? Solve this by
  - i. Using a velocity-addition argument.
  - ii. Using the Lorentz transformations to go from the train frame to the ground frame.
- (c) The ball frame?
- (d) Verify that the invariant interval is indeed the same in all three frames.
- (e) Show that the times in the ball frame and ground frame are related by the relevant  $\gamma$  factor.
- (f) Ditto for the ball frame and train frame.
- (g) Show that the times in the train frame and ground frame are *not* related by the relevant  $\gamma$  factor. Why not?

### Section 11.7: Minkowski diagrams

#### 11.21. A new frame \*

In a given reference frame, Event 1 happens at  $x = 0$ ,  $ct = 0$ , and Event 2 happens at  $x = 2$ ,  $ct = 1$  (in units of some specified length). Find a frame in which the two events are simultaneous.

![Minkowski diagram showing a hyperbola c^2t^2 - x^2 = 1 and axes for frames S and S'.](80c37ac73c80e2823448ac7c69568a5c_img.jpg)

The figure is a Minkowski diagram with a vertical axis labeled  $ct$  and a horizontal axis labeled  $x$ . A hyperbola labeled  $c^2t^2 - x^2 = 1$  is drawn in the first quadrant. Two solid lines originate from the origin: one is the  $ct'$  axis, which is steeper than the  $ct$  axis, and the other is the  $x'$  axis, which is less steep than the  $x$  axis. A dashed line is also shown, parallel to the  $x'$  axis, intersecting the hyperbola. An arrow points from the hyperbola label towards the  $ct'$  axis.

Minkowski diagram showing a hyperbola c^2t^2 - x^2 = 1 and axes for frames S and S'.

Fig. 11.45

#### 11.22. Minkowski diagram units \*

Consider the Minkowski diagram in Fig. 11.45. In frame  $S$ , the hyperbola  $c^2t^2 - x^2 = 1$  is drawn. Also drawn are the axes of frame  $S'$ , which moves past  $S$  with speed  $v$ . Use the invariance of the interval  $s^2 = c^2t^2 - x^2$  to derive the ratio of the unit sizes on the  $ct'$  and  $ct$  axes, and check your result with Eq. (11.46).

#### 11.23. Velocity addition via Minkowski \*\*

An object moves at speed  $v_1$  with respect to frame  $S'$ . Frame  $S'$  moves at speed  $v_2$  with respect to frame  $S$  (in the same direction as the motion of the object). What is the speed,  $u$ , of the object with respect to frame  $S$ ? Solve this problem (that is, derive the velocity-addition formula) by drawing a Minkowski diagram with frames  $S$  and  $S'$ , drawing the worldline of the object, and doing some geometry.

#### 11.24. Clapping both ways \*\*

Twin  $A$  stays on the earth, and twin  $B$  flies to a distant star and back. For both of the following setups, draw a Minkowski diagram that explains what is happening.

- (a) Throughout the trip,  $B$  claps in such a way that his claps occur at equal time intervals  $\Delta t$  in  $A$ 's frame. At what time intervals do the claps occur in  $B$ 's frame?
- (b) Now let  $A$  clap in such a way that his claps occur at equal time intervals  $\Delta t$  in  $B$ 's frame. At what time intervals do the claps occur in  $A$ 's frame? (Be careful on this one. The sum of all the time intervals must equal the increase in  $A$ 's age, which is greater than the increase in  $B$ 's age, as we know from the usual twin paradox.)

#### 11.25. Acceleration and redshift \*\*\*

Use a Minkowski diagram to solve the following problem: Two people stand a distance  $d$  apart. They simultaneously start accelerating in the same direction (along the line between them) with the same proper acceleration  $a$ . At the instant they start to move, how fast does each person's clock tick in the (changing) frame of the other person?

#### 11.26. Break or not break? \*\*\*

Two spaceships float in space and are at rest relative to each other. They are connected by a string (see Fig. 11.46). The string is strong, but it cannot withstand an arbitrary amount of stretching. At a given instant, the spaceships simultaneously (with respect to their initial inertial frame) start accelerating in the same direction (along the line between them) with the same constant proper acceleration. In other words, assume they bought identical engines from the same store, and they put them on the same setting. Will the string eventually break?

![Diagram showing two spaceships connected by a dashed line (string). Both spaceships have arrows pointing to the right, indicating they are accelerating in the same direction.](4d5f72ec2354633873d8c461feed6bd2_img.jpg)

Diagram showing two spaceships connected by a dashed line (string). Both spaceships have arrows pointing to the right, indicating they are accelerating in the same direction.

Fig. 11.46

### Section 11.9: Rapidity

#### 11.27. Successive Lorentz transformations

The Lorentz transformation in Eq. (11.58) may be written in matrix form as

$$\begin{pmatrix} x \\ ct \end{pmatrix} = \begin{pmatrix} \cosh \phi & \sinh \phi \\ \sinh \phi & \cosh \phi \end{pmatrix} \begin{pmatrix} x' \\ ct' \end{pmatrix}. \quad (11.76)$$

Show that if you apply an L.T. with  $v_1 = \tanh \phi_1$ , and then another one with  $v_2 = \tanh \phi_2$ , the result is an L.T. with  $v = \tanh(\phi_1 + \phi_2)$ .

#### 11.28. Accelerator's time \*\*

A spaceship is initially at rest in the lab frame. At a given instant, it starts to accelerate. Let this happen when the lab clock reads  $t = 0$  and the spaceship clock reads  $t' = 0$ . The proper acceleration is  $a$ . (That is, at time  $t' + dt'$ , the spaceship is moving at speed  $a dt'$  relative

to the frame it was in at time  $t'$ .) Later on, a person in the lab measures  $t$  and  $t'$ . What is the relation between them?

### 11.12 Exercises

### Section 11.3: The fundamental effects

#### 11.29. Effectively speed $c$ \*

A rocket flies between two planets that are one light-year apart. What should the rocket's speed be so that the time elapsed on the captain's watch is one year?

#### 11.30. A passing train \*

A train of length  $15\text{ cs}$  moves at speed  $3c/5$ .<sup>39</sup> How much time does it take to pass a person standing on the ground (as measured by that person)? Solve this by working in the frame of the person, and then again by working in the frame of the train.

#### 11.31. Overtaking a train \*

Train  $A$  has length  $L$ . Train  $B$  moves past  $A$  (on a parallel track, facing the same direction) with relative speed  $4c/5$ . The length of  $B$  is such that  $A$  says that the fronts of the trains coincide at exactly the same time as the backs coincide. What is the time difference between the fronts coinciding and the backs coinciding, as measured by  $B$ ?

#### 11.32. Walking on a train \*

A train of proper length  $L$  and speed  $3c/5$  approaches a tunnel of length  $L$ . At the moment the front of the train enters the tunnel, a person leaves the front of the train and walks (briskly) toward the back. She arrives at the back of the train right when it (the back) leaves the tunnel.

- How much time does this take in the ground frame?
- What is the person's speed with respect to the ground?
- How much time elapses on the person's watch?

#### 11.33. Simultaneous waves \*

Alice flies past Bob at speed  $v$ . Right when she passes, they both set their watches to zero. When Alice's watch shows a time  $T$ , she waves to Bob. Bob then waves to Alice simultaneously (as measured by him) with Alice's wave (so this is before he actually *sees* her wave). Alice then waves to Bob simultaneously (as measured by her) with Bob's wave. Bob then waves to Alice simultaneously (as measured by him)

<sup>39</sup>  $1\text{ cs}$  is one "light-second." It equals  $(1)(3 \cdot 10^8\text{ m/s})(1\text{ s}) = 3 \cdot 10^8\text{ m}$ .

with Alice's second wave. And so on. What are the readings on Alice's watch for all the times she waves? And likewise for Bob?

#### **11.34. Here and there \***

A train of proper length  $L$  travels past you at speed  $v$ . A person on the train stands at the front, next to a clock that reads zero. At this moment in time (as measured by you), a clock at the back of the train reads  $Lv/c^2$ . How would you respond to the following statement:

"The person at the front of the train can leave the front right after the clock there reads zero, and then run to the back and get there right before the clock there reads  $Lv/c^2$ . You (on the ground) will therefore see the person simultaneously at *both* the front and the back of the train when the clocks there read zero and  $Lv/c^2$ , respectively."

#### **11.35. Photon on a train \***

A train of proper length  $L$  has clocks at the front and back. A photon is fired from the back of the train to the front. Working in the train frame, we can easily say that if the photon leaves the back of the train when the clock there reads zero, then it arrives at the front when the clock there reads  $L/c$ .

Now consider this setup in the ground frame, where the train travels by at speed  $v$ . Rederive the above result (that the difference in the readings of the two clocks is  $L/c$ ) by working *only* in the ground frame.

#### **11.36. Triplets \***

Triplet  $A$  stays on the earth. Triplet  $B$  travels at speed  $4c/5$  to a planet (a distance  $L$  away) and back. Triplet  $C$  travels out to the planet at speed  $3c/4$ , and then returns at the necessary speed to arrive back exactly when  $B$  does. How much does each triplet age during this process? Who is youngest?

#### **11.37. Seeing the light \*\***

$A$  and  $B$  leave from a common point (with their clocks both reading zero) and travel in opposite directions with relative speed  $v$ . When  $B$ 's clock reads  $T$ , he ( $B$ ) sends out a light signal. When  $A$  receives the signal, what time does his ( $A$ 's) clock read? Answer this question by doing the calculation entirely in (a)  $A$ 's frame, and then (b)  $B$ 's frame. (This problem is basically a derivation of the longitudinal Doppler effect, discussed in Section 11.8.1.)

#### **11.38. Two trains and a tree \*\***

Two trains of proper length  $L$  move toward each other in opposite directions on parallel tracks. They both move at speed  $v$  with respect to the ground. Both trains have clocks at the front and back, and these

clocks are synchronized as usual in the frame of the train they are in. A tree is located on the ground at the place where the fronts of the trains pass each other. The clocks at the fronts of the trains both read zero when they pass. Find the reading on the clocks at the backs of the trains when they (the backs) pass each other at the tree. Do this in three different ways:

- (a) Imagine that you stand next to the tree on the ground, and you observe what one of the rear clocks is doing.
- (b) Imagine that you are on one of the trains, and you observe what your own rear clock is doing during the time the tree travels the relevant distance.
- (c) Imagine that you are on one of the trains, and you observe what the other train's rear clock is doing during the time the tree travels the relevant distance. (You'll need to use velocity addition.)

#### 11.39. **Twice simultaneous \*\***

A train of proper length  $L$  moves at speed  $v$  with respect to the ground. When the front of the train passes a tree on the ground, a ball is simultaneously (as measured in the *ground frame*) thrown from the back of the train toward the front, with speed  $u$  with respect to the train. What should  $u$  be so that the ball hits the front simultaneously (as measured in the *train frame*) with the tree passing the back of the train? Show that in order for a solution for  $u$  to exist, we must have  $v/c < (\sqrt{5} - 1)/2$ , which happens to be the inverse of the golden ratio.

#### 11.40. **People clapping \*\***

Two people stand a distance  $L$  apart along an east–west road. They both clap their hands at precisely noon in the ground frame. You are driving eastward down this road at speed  $4c/5$ . You notice that you are next to the western person at the same instant (as measured in your frame) that the eastern person claps. Later on, you notice that you are next to a tree at the same instant (as measured in your frame) that the western person claps. Where is the tree along the road? (Describe its location in the ground frame.)

#### 11.41. **Photon, tree, and house \*\***

- (a) A train of proper length  $L$  moves at speed  $v$  with respect to the ground. At the instant the back of the train passes a certain tree, someone at the back of the train shines a photon toward the front. The photon happens to hit the front of the train at the instant the front passes a certain house. As measured in the ground frame, how far apart are the tree and the house? Solve this by working in the ground frame.

- (b) Now look at the setup from the point of view of the train frame. Using your result for the tree–house distance from part (a), verify that the house meets the front of the train at the same instant the photon meets it.

#### **11.42. Tunnel fraction \*\***

A person runs with speed  $v$  toward a tunnel of length  $L$ . A light source is located at the far end of the tunnel. At the instant the person enters the tunnel, the light source simultaneously (as measured in the tunnel frame) emits a photon that travels down the tunnel toward the person. When the person and the photon eventually meet, the person’s location is a fraction  $f$  along the tunnel. What is  $f$ ? Solve this by working in the tunnel frame, and then again by working in the person’s frame.

#### **11.43. Overlapping trains \*\***

An observer on the ground sees two trains,  $A$  and  $B$ , both of proper length  $L$ , move in opposite directions at speed  $v$  with respect to the ground. She notices that when the trains “overlap,” clocks at the front of  $A$  and rear of  $B$  both read zero. From the “rear clock ahead” effect, she therefore also notices that clocks at the rear of  $A$  and front of  $B$  read  $Lv/c^2$  and  $-Lv/c^2$ , respectively (as shown in Fig. 11.47). Now imagine riding along on  $A$ . When the rear of  $B$  passes the front of your train ( $A$ ), clocks at both of these places read zero (as stated above). Explain, by working *only* in the frame of  $A$ , why clocks at the back of  $A$  and the front of  $B$  read  $Lv/c^2$  and  $-Lv/c^2$ , respectively, when these points coincide. (You’ll need to use velocity addition.)

![Diagram of two trains, A and B, in the ground frame. Train B is moving left with velocity v, and its rear clock reads -Lv/c^2 while its front clock reads 0. Train A is moving right with velocity v, and its rear clock reads Lv/c^2 while its front clock reads 0.](6e1a2b7c09eeeb3f39bb30ceca9054f1_img.jpg)

The diagram shows two horizontal rectangles representing trains A and B. Above train B, a left-pointing arrow is labeled  $v$ . Inside the left end of train B is a circle containing  $-Lv/c^2$ , and inside the right end is a circle containing 0. The label  $B$  is to the right of the train. Below train A, a right-pointing arrow is labeled  $v$ . Inside the left end of train A is a circle containing  $Lv/c^2$ , and inside the right end is a circle containing 0. The label  $A$  is to the right of the train. The text "(ground frame)" is at the top left of the diagram.

Diagram of two trains, A and B, in the ground frame. Train B is moving left with velocity v, and its rear clock reads -Lv/c^2 while its front clock reads 0. Train A is moving right with velocity v, and its rear clock reads Lv/c^2 while its front clock reads 0.

**Fig. 11.47**

#### **11.44. Bouncing stick \*\***

A stick, oriented horizontally, falls and bounces off the ground. Qualitatively, what does this look like in the frame of someone running by at speed  $v$ ?

#### **11.45. Through the hole? \*\***

A stick of proper length  $L$  moves at speed  $v$  in the direction of its length. It passes over an infinitesimally thin sheet that has a hole of diameter  $L$  cut in it. As the stick passes over the hole, the sheet is raised so that the stick passes through the hole and ends up underneath the sheet. Well, maybe . . .

In the lab frame, the stick’s length is contracted to  $L/\gamma$ , so it appears to easily make it through the hole. But in the stick frame, the hole is contracted to  $L/\gamma$ , so it appears that the stick does *not* make it through the hole (or rather, the hole doesn’t make it around the stick, since the hole is what is moving in the stick frame). So the question is: Does the stick end up on the other side of the sheet or not?

#### **11.46. Short train in a tunnel \*\***

Consider the scenario in Problem 11.6, with the only change being that the train now has length  $rL$ , where  $r$  is some numerical factor. What is the largest value of  $r$ , in terms of  $v$ , for which it is possible for the bomb not to explode? Verify that you obtain the same answer working in the train frame and working in the tunnel frame.

### *Section 11.4: The Lorentz transformations*

#### **11.47. Successive L.T.'s \*\***

Show that the combination of an L.T. (with speed  $v_1$ ) and an L.T. (with speed  $v_2$ ) yields an L.T. with speed  $u = (v_1 + v_2)/(1 + v_1 v_2/c^2)$ .

#### **11.48. Loss of simultaneity \*\***

A train moves at speed  $v$  with respect to the ground. Two events occur simultaneously, a distance  $L$  apart, in the train frame. What are the time and space separations in the ground frame? Solve this by:

- Using the Lorentz transformations.
- Using only the results in Section 11.3. Do this by working in the ground frame, and then again by working in the train frame.

### *Section 11.5: Velocity addition*

#### **11.49. Some $\gamma$ 's \***

Show that the relativistic addition (or subtraction) of the velocities  $u$  and  $v$  has a  $\gamma$  factor given by  $\gamma = \gamma_u \gamma_v (1 \pm uv)$ .

#### **11.50. Slanted time dilation \***

A clock moves vertically with speed  $u$  in a given frame, and you run horizontally with speed  $v$  with respect to this frame. Show that you see the clock run slow by the nice simple factor,  $\gamma_u \gamma_v$ .

#### **11.51. Pythagorean triples \***

Let  $(a, b, h)$  be a Pythagorean triple. (We'll use  $h$  to denote the hypotenuse, instead of  $c$ , for obvious reasons.) Consider the relativistic addition or subtraction of the two speeds,  $\beta_1 = a/h$  and  $\beta_2 = b/h$ . Show that the numerator and denominator of the result are the leg and hypotenuse of another Pythagorean triple, and find the other leg. What is the associated  $\gamma$  factor?

#### **11.52. Running away \***

$A$  and  $B$  both start at the origin and simultaneously head off in opposite directions at speed  $3c/5$  with respect to the ground.  $A$  moves to the right, and  $B$  moves to the left. Consider a mark on the ground at  $x = L$ .

As viewed in the ground frame,  $A$  and  $B$  are a distance  $2L$  apart when  $A$  passes this mark. As viewed by  $A$ , how far away is  $B$  when  $A$  coincides with the mark?

#### **11.53. Angled photon \***

A photon moves at an angle  $\theta$  with respect to the  $x'$  axis in frame  $S'$ . Frame  $S'$  moves at speed  $v$  with respect to frame  $S$  (along the  $x'$  axis). Calculate the components of the photon's velocity in  $S$ , and verify that the speed is  $c$ .

#### **11.54. Running on a train \*\***

A train of proper length  $L$  moves at speed  $v_1$  with respect to the ground. A passenger runs from the back of the train to the front at speed  $v_2$  with respect to the train. How much time does this take, as viewed by someone on the ground? Solve this in two different ways:

- (a) Find the relative speed of the passenger and the train (as viewed by someone on the ground), and then find the time it takes for the passenger to erase the initial “head start” that the front of the train had.
- (b) Find the time elapsed on the passenger's clock (by working in whatever frame you want), and then use time dilation to get the time elapsed on a ground clock.

#### **11.55. Velocity addition \*\***

The fact that the previous exercise can be solved in two different ways suggests a method of deriving the velocity-addition formula: A train of proper length  $L$  moves at speed  $v_1$  with respect to the ground. A ball is thrown from the back of the train to the front at speed  $v_2$  with respect to the train. Let the speed of the ball with respect to the ground be  $V$ . Calculate the time of the ball's journey, as measured by an observer on the ground, in the following two different ways, and then set them equal to solve for  $V$  in terms of  $v_1$  and  $v_2$ . (This gets a bit messy. And yes, you have to solve a quadratic.)

- (a) First way: Find the relative speed of the ball and the train (as viewed by someone on the ground), and then find the time it takes for the ball to erase the initial “head start” that the front of the train had.
- (b) Second way: Find the time elapsed on the ball's clock (by working in whatever frame you want), and then use time dilation to get the time elapsed on a ground clock.

#### **11.56. Velocity addition again \*\***

A train of proper length  $L$  moves at speed  $v$  with respect to the ground. A ball is thrown from the back of the train to the front at speed  $u$  with

respect to the train. When finding the time of this process in the ground frame, a common error is to use time dilation to go from the train frame to the ground frame, which gives an incorrect answer of  $\gamma_v(L/u)$ . This is incorrect because time dilation is valid only if the two relevant events occur at the same place in one of the frames; otherwise simultaneity becomes an issue.

- (a) Find the total time in the ground frame correctly by looking at how much a clock at rest in the train frame advances (for example, a clock at the front of the train), and by applying time dilation to this clock.
- (b) Find the total time in the ground frame by applying time dilation to the ball's clock. Your answer will contain the unknown speed  $V$  of the ball with respect to the ground.
- (c) Equate your results from parts (a) and (b) to show that  $\gamma_V = \gamma_u \gamma_v (1 + uv/c^2)$ . Then solve for  $V$  to produce the velocity-addition formula.

#### 11.57. Bullets on a train \*\*

A train moves at speed  $v$ . Bullets are successively fired at speed  $u$  (relative to the train) from the back of the train to the front. A new bullet is fired at the instant (as measured in the train frame) the previous bullet hits the front. In the frame of the ground, what fraction of the way along the train is a given bullet, at the instant (as measured in the ground frame) the next bullet is fired? What is the maximum number of bullets that are in flight at a given instant, in the ground frame?

#### 11.58. Time dilation and $Lv/c^2$ \*\*

A person walks very slowly at speed  $u$  from the back of a train of proper length  $L$  to the front. The time-dilation effect in the train frame can be made arbitrarily small by picking  $u$  to be sufficiently small (because the effect is second order in  $u$ ). Therefore, if the person's watch agrees with a clock at the back of the train when he starts, then it also (essentially) agrees with a clock at the front when he finishes.

Now consider this setup in the ground frame, where the train moves at speed  $v$ . The rear clock reads  $Lv/c^2$  more than the front, so in view of the preceding paragraph, the time gained by the person's watch during the process must be  $Lv/c^2$  less than the time gained by the front clock. By working in the ground frame, explain why this is the case. Assume  $u \ll v$ .<sup>40</sup>

<sup>40</sup> If you line up a collection of these train systems around the circumference of a rotating platform, then the above result implies the following fact. Let person  $A$  be at rest on the platform, and let person  $B$  walk arbitrarily slowly around the circumference. Then when  $B$  returns to  $A$ ,  $B$ 's clock will read less than  $A$ 's. This is true because the above reasoning shows (as you will figure out)

### *Section 11.6: The invariant interval*

#### **11.59. Passing a train \*\***

Person  $A$  stands on the ground, train  $B$  with proper length  $L$  moves to the right at speed  $3c/5$ , and person  $C$  runs to the right at speed  $4c/5$ .  $C$  starts behind the train and eventually passes it. Let event  $E_1$  be “ $C$  coincides with the back of the train,” and let event  $E_2$  be “ $C$  coincides with the front of the train.” Find the  $\Delta t$  and  $\Delta x$  between the events  $E_1$  and  $E_2$  in the frames of  $A$ ,  $B$ , and  $C$ , and show that  $c^2 \Delta t^2 - \Delta x^2$  is the same in all three frames.

#### **11.60. Passing trains \*\***

Train  $A$  with proper length  $L$  moves eastward at speed  $v$ , while train  $B$  with proper length  $2L$  moves westward also at speed  $v$ . How much time does it take for the trains to pass each other (defined as the time between the fronts coinciding and the backs coinciding):

- (a) In  $A$ 's frame?
- (b) In  $B$ 's frame?
- (c) In the ground frame?
- (d) Verify that the invariant interval is the same in all three frames.

#### **11.61. Throwing on a train \*\***

A train with proper length  $L$  moves at speed  $3c/5$  with respect to the ground. A ball is thrown from the back to the front, at speed  $c/2$  with respect to the train. How much time does this take, and what distance does the ball cover, in:

- (a) The train frame?
- (b) The ground frame? Solve this by
  - i. Using a velocity-addition argument.
  - ii. Using the Lorentz transformations to go from the train frame to the ground frame.
- (c) The ball frame?
- (d) Verify that the invariant interval is indeed the same in all three frames.
- (e) Show that the times in the ball frame and ground frame are related by the relevant  $\gamma$  factor.

that an inertial observer sees  $B$ 's clock running slower than  $A$ 's. This result, that you can walk arbitrarily slowly in a particular reference frame and have your clock lose synchronization with other clocks, is a consequence of the fact that in some accelerating reference frames it is impossible to produce a consistent method (that is, one without a discontinuity) of clock synchronization. See Cranor *et al.* (2000) for more details.

- (f) Ditto for the ball frame and train frame.
- (g) Show that the times in the train frame and ground frame are *not* related by the relevant  $\gamma$  factor. Why not?

### *Section 11.7: Minkowski diagrams*

#### **11.62. Time dilation via Minkowski \***

In the spirit of the example in Section 11.7, use a Minkowski diagram to derive the time-dilation result between frames  $S$  and  $S'$  (in both directions, as in the example).

#### **11.63. $Lv/c^2$ via Minkowski \***

In the spirit of the example in Section 11.7, use a Minkowski diagram to derive the  $Lv/c^2$  rear-clock-ahead result for frames  $S$  and  $S'$  (in both directions, as in the example).

#### **11.64. Simultaneous waves again \*\***

Solve Exercise 11.33 by using a Minkowski diagram from the point of view of someone who sees Alice and Bob moving with equal and opposite speeds.

#### **11.65. Short train in a tunnel again \*\*\***

Solve Exercise 11.46 by using a Minkowski diagram from the point of view of the train, and also of the tunnel.

### *Section 11.8: The Doppler effect*

#### **11.66. Transverse Doppler \*\***

As mentioned in Remark 2 of Section 11.8.2, it is possible to solve the transverse Doppler effect for Case 1 by working in the frame of the observer, provided that you account for the longitudinal component of the source's motion. Solve the problem this way and reproduce Eq. (11.52).

#### **11.67. Twin paradox via Doppler \*\***

Twin  $A$  stays on the earth, and twin  $B$  flies at speed  $v$  to a distant star and back. The star is a distance  $L$  from the earth in the earth-star frame. Use the Doppler effect to show that  $B$  is younger by a factor  $\gamma$  when she returns (don't use any time dilation or length contraction results). Do this in the following two ways; both are doable by working in either  $A$ 's frame or  $B$ 's frame(s), so take your pick.

- (a)  $A$  sends out flashes at intervals of  $t$  seconds (as measured in his frame). By considering the numbers of redshifted and blueshifted flashes that  $B$  receives, show that  $T_B = T_A/\gamma$ .

- (b)  $B$  sends out flashes at intervals of  $t$  seconds (as measured in her frame). By considering the numbers of redshifted and blueshifted flashes that  $A$  receives, show that  $T_B = T_A/\gamma$ .

### Section 11.9: Rapidity

#### 11.68. Time of travel \*\*

Consider the setup in Problem 11.28 (and feel free to use the results from that problem in this exercise). Let the spaceship travel to a planet a distance  $L$  from the earth.

- By working in the frame of the earth, find the time of the journey, as measured by the earth. Check the large and small  $L$  (compared with  $c^2/a$ ) limits.
- By working in the (changing) frame of the spaceship, find the time of the journey, as measured by the spaceship (an implicit equation is fine). Check the small  $L$  limit. How does the time behave for large  $L$ ?

### 11.13 Solutions

#### 11.1. No transverse length contraction

Assume that the paint brushes are capable of leaving marks on stick  $B$  if  $B$  is long enough, or if  $A$  is short enough. The key fact we need here is the second postulate of relativity, which says that the frames of the sticks are equivalent. That is, if  $A$  sees  $B$  shorter than (or longer than, or equal to) itself, then  $B$  also sees  $A$  shorter than (or longer than, or equal to) itself. The contraction factor must be the same when going each way between the frames.

Assume (in search of a contradiction) that  $A$  sees  $B$  shortened. Then  $B$  won't extend out to the ends of  $A$ , so there will be no marks on  $B$ . But in this case,  $B$  must also see  $A$  shortened, so there *will* be marks on  $B$  (see Fig. 11.48). This is a contradiction. Likewise, if we assume that  $A$  sees  $B$  lengthened, we also reach a contradiction. We are therefore left with only the third possibility, namely that each stick sees the other stick as one meter long.

#### 11.2. Explaining time dilation

The resolution to the apparent paradox is the “head start” that  $B$ 's clock has over  $A$ 's clock, as seen in the spaceship frame. From Eq. (11.6), we know that in the spaceship frame,  $B$ 's clock reads  $Lv/c^2$  more than  $A$ 's. (The two planets may be considered to be at the ends of the train in the example in Section 11.3.1.)

Therefore, what a person on the spaceship says is: “My clock advances by  $L/\gamma v$  during the whole trip. I see  $B$ 's clock running slow by a factor  $\gamma$ , so I see  $B$ 's clock advance by only  $(L/\gamma v)/\gamma = L/\gamma^2 v$ . However,  $B$ 's clock started not at zero but at  $Lv/c^2$ . Therefore, the final reading on  $B$ 's clock when I get there is

$$\frac{Lv}{c^2} + \frac{L}{\gamma^2 v} = \frac{L}{v} \left( \frac{v^2}{c^2} + \frac{1}{\gamma^2} \right) = \frac{L}{v} \left( \frac{v^2}{c^2} + \left( 1 - \frac{v^2}{c^2} \right) \right) = \frac{L}{v}, \quad (11.77)$$

as we wanted to show.”

![Figure 11.48: A diagram illustrating the paradox of transverse length contraction. It shows two views: (A's view) and (B's view). In (A's view), stick A is vertical and stick B is horizontal, with an arrow pointing left from B towards A. In (B's view), stick A is horizontal and stick B is vertical, with an arrow pointing right from A towards B. The diagram shows that if one stick is shorter than the other, the other must also be shorter, leading to a contradiction.](15517affbdf16108453e218d9b026b88_img.jpg)

Figure 11.48: A diagram illustrating the paradox of transverse length contraction. It shows two views: (A's view) and (B's view). In (A's view), stick A is vertical and stick B is horizontal, with an arrow pointing left from B towards A. In (B's view), stick A is horizontal and stick B is vertical, with an arrow pointing right from A towards B. The diagram shows that if one stick is shorter than the other, the other must also be shorter, leading to a contradiction.

Fig. 11.48

#### 11.3. Explaining length contraction

The resolution to the apparent paradox is that the explosions do not occur simultaneously in the train frame. As the platform rushes past the train, the “rear” bomb explodes before the “front” bomb explodes.<sup>41</sup> The front bomb then gets to travel farther by the time it explodes and leaves its mark. The distance between the marks is therefore larger than you might naively expect. Let’s be quantitative about this.

Let the two bombs contain clocks that read zero when they explode (they are synchronized in the platform frame). Then in the train frame, the front bomb’s clock reads only  $-Lv/c^2$  when the rear bomb explodes when showing a time of zero. (This is the “rear clock ahead” result from Eq. (11.6).) The front bomb’s clock must therefore advance by a time of  $Lv/c^2$  before it explodes. But the train sees the bombs’ clocks running slow by a factor  $\gamma$ , so in the train frame the front bomb explodes a time  $\gamma Lv/c^2$  after the rear bomb explodes. During this time of  $\gamma Lv/c^2$ , the platform moves a distance  $(\gamma Lv/c^2)v$  relative to the train.

Therefore, what a person on the train says is: “Due to length contraction, the distance between the bombs is  $L/\gamma$ . The front bomb is therefore a distance  $L/\gamma$  ahead of the rear bomb when the latter explodes. The front bomb then travels an additional distance of  $\gamma Lv^2/c^2$  by the time it explodes, at which point it is a distance of

$$\frac{L}{\gamma} + \frac{\gamma Lv^2}{c^2} = \gamma L \left( \frac{1}{\gamma^2} + \frac{v^2}{c^2} \right) = \gamma L \left( \left( 1 - \frac{v^2}{c^2} \right) + \frac{v^2}{c^2} \right) = \gamma L \quad (11.78)$$

ahead of the rear bomb’s mark, as we wanted to show.”

#### 11.4. A passing stick

- (a) The stick has length  $L/\gamma$  in your frame, and it moves with speed  $v$ . Therefore, the time taken in your frame to cover the distance  $L/\gamma$  is  $L/\gamma v$ .
- (b) The stick sees you fly by at speed  $v$ . The stick has length  $L$  in its own frame, so the time elapsed in the stick frame is  $L/v$ . During this time, the stick sees the watch on your wrist run slow by a factor  $\gamma$ . Therefore, a time of  $L/\gamma v$  elapses on your watch, in agreement with part (a).

Logically, the two solutions in (a) and (b) differ in that one uses length contraction and the other uses time dilation. Mathematically, they differ simply in the order in which the divisions by  $\gamma$  and  $v$  occur.

- (c) You see the rear clock on the stick showing a time of  $Lv/c^2$  more than the front clock. In addition to this head start, more time will of course elapse on the rear clock by the time it reaches you. The time in your frame is  $L/\gamma v$  (because the stick has length  $L/\gamma$  in your frame). But the stick’s clocks run slow, so a time of only  $L/\gamma^2 v$  will elapse on the rear clock by the time it reaches you. The total additional time (compared with the front clock’s reading when it passed you) that the rear clock shows is therefore

$$\frac{Lv}{c^2} + \frac{L}{\gamma^2 v} = \frac{L}{v} \left( \frac{v^2}{c^2} + \frac{1}{\gamma^2} \right) = \frac{L}{v} \left( \frac{v^2}{c^2} + \left( 1 - \frac{v^2}{c^2} \right) \right) = \frac{L}{v}, \quad (11.79)$$

in agreement with the quick calculation that follows in part (d).

- (d) The stick sees you fly by at speed  $v$ . The stick has length  $L$  in its own frame, so the time elapsed in the stick frame is  $L/v$ .

<sup>41</sup> Since we’ll be working in the train frame here, we’ll use the words “rear” and “front” in the way that someone on the train uses them as she watches the platform rush by. That is, if the train is heading east with respect to the platform, then from the point of view of the train, the platform is heading west, so the eastern bomb on the platform is the rear one, and the western bomb is the front one. So they have the opposite orientation compared with the way that someone on the platform labels the rear and front of the train. Using the same orientation would entail writing the phrase “front clock ahead” below, which would make me cringe.

#### 11.5. Rotated square

Figure 11.49 shows a top view of the square at the instant (in your frame) when it is closest to you. Its length is contracted along the direction of motion, so it takes the shape of a rectangle with sides  $L$  and  $L/\gamma$ . This is what the shape *is* in your frame (where *is*-ness is defined by where all the points of an object are at simultaneous times). But what does the square *look* like to you? That is, what is the nature of the photons hitting your eye at a given instant?<sup>42</sup>

Photons from the far side of the square have to travel an extra distance  $L$  to get to your eye, compared with photons from the near side. So they need an extra time  $L/c$  of flight. During this time  $L/c$ , the square moves a distance  $Lv/c \equiv L\beta$  sideways. Therefore, referring to Fig. 11.50, a photon emitted at point  $A$  reaches your eye at the same time as a photon emitted from point  $B$ . This means that the trailing side of the square spans a distance  $L\beta$  across your field of vision, while the near side spans a distance  $L/\gamma = L\sqrt{1-\beta^2}$  across your field of vision. But this is exactly what a rotated square of side  $L$  looks like, as shown in Fig. 11.51, where the angle of rotation satisfies  $\sin \theta = \beta$ . For the case of a circle instead of a square, see Hollenbach (1976).

#### 11.6. Train in a tunnel

Yes, the bomb explodes. This is clear in the frame of the train (see Fig. 11.52). In this frame, the train has length  $L$ , and the tunnel speeds past it. The tunnel is length-contracted down to  $L/\gamma$ . Therefore, the far end of the tunnel passes the front of the train before the near end passes the back, so the bomb explodes.

We can, however, also look at things in the frame of the tunnel (see Fig. 11.53). Here the tunnel has length  $L$ , and the train is length-contracted down to  $L/\gamma$ . Therefore, the deactivation device gets triggered *before* the front of the train passes the far end of the tunnel, so you might think that the bomb does *not* explode. We appear to have a paradox.

The resolution to this paradox is that the deactivation device cannot instantaneously tell the bomb to deactivate itself. It takes a finite time for the signal to travel the length of the train from the sensor to the bomb. And it turns out that this transmission time makes it impossible for the deactivation signal to get to the bomb before the bomb gets to the far end of the tunnel, no matter how fast the train is moving. Let's show this.

The signal has the best chance of winning this “race” if it has speed  $c$ , so let's assume this is the case. Now, the signal gets to the bomb before the bomb gets to the far end of the tunnel if and only if a light pulse emitted from the near end of the tunnel (at the instant the back of the train goes by) reaches the far end of the tunnel before the front of the train does. The former takes a time  $L/c$ . The latter takes a time  $L(1 - 1/\gamma)/v$ , because the front of the train is already a distance  $L/\gamma$  through the tunnel. So if the bomb is *not* to explode, we must have

$$\begin{aligned} L/c &< L(1 - 1/\gamma)/v \\ \iff \beta &< 1 - \sqrt{1 - \beta^2} \\ \iff \sqrt{1 - \beta^2} &< 1 - \beta \\ \iff \sqrt{1 + \beta} &< \sqrt{1 - \beta}. \end{aligned} \quad (11.80)$$

This is never true. Therefore, the signal always arrives too late, and the bomb always explodes.

<sup>42</sup> In relativity problems, we virtually always subtract off the time it takes light to travel from the object to your eye (that is, we find out what really *is*). But along with the Doppler effect discussed in Section 11.8, this problem is one of the few exceptions where we actually want to determine what your eye registers.

![Figure 11.49: A top view of a square in a frame where it is moving to the right with velocity v. The square is contracted along the direction of motion, appearing as a rectangle with vertical sides of length L and horizontal sides of length L/γ.](62034e6cdf062975afb95c709819c84f_img.jpg)

Figure 11.49: A top view of a square in a frame where it is moving to the right with velocity v. The square is contracted along the direction of motion, appearing as a rectangle with vertical sides of length L and horizontal sides of length L/γ.

Fig. 11.49

![Figure 11.50: A diagram showing two points A and B. A is at the top left, and B is at the bottom right. A dashed horizontal line connects the vertical projections of A and B. The horizontal distance between these projections is labeled Lβ. The horizontal distance from the projection of B to the vertical projection of A is labeled L√(1-β²). A solid line connects A and B.](66b63453a1c4d97fafcba55e5b160870_img.jpg)

Figure 11.50: A diagram showing two points A and B. A is at the top left, and B is at the bottom right. A dashed horizontal line connects the vertical projections of A and B. The horizontal distance between these projections is labeled Lβ. The horizontal distance from the projection of B to the vertical projection of A is labeled L√(1-β²). A solid line connects A and B.

Fig. 11.50

![Figure 11.51: A diagram showing a square of side L rotated by an angle θ. The square is inscribed within a dashed rectangle. The horizontal width of the dashed rectangle is Lβ, and the horizontal distance from the right side of the square to the right side of the dashed rectangle is L√(1-β²). The angle θ is shown at the bottom-left and bottom-right corners of the square.](c62fbd9203754ace1f582e4244342d76_img.jpg)

Figure 11.51: A diagram showing a square of side L rotated by an angle θ. The square is inscribed within a dashed rectangle. The horizontal width of the dashed rectangle is Lβ, and the horizontal distance from the right side of the square to the right side of the dashed rectangle is L√(1-β²). The angle θ is shown at the bottom-left and bottom-right corners of the square.

Fig. 11.51

(train frame)

![Figure 11.52: A diagram in the train frame. A train of length L is moving to the right with velocity v. A sensor is at the back (left) and a bomb is at the front (right). A tunnel of length L/γ is shown below the train. The sensor is at the back of the tunnel, and the bomb is at the front of the tunnel.](3de34615653dd0063ee33de3fe01aa8c_img.jpg)

Figure 11.52: A diagram in the train frame. A train of length L is moving to the right with velocity v. A sensor is at the back (left) and a bomb is at the front (right). A tunnel of length L/γ is shown below the train. The sensor is at the back of the tunnel, and the bomb is at the front of the tunnel.

Fig. 11.52

(tunnel frame)

![Figure 11.53: A diagram in the tunnel frame. A tunnel of length L is shown. A train of length L/γ is moving to the right with velocity v. The sensor is at the back of the train, and the bomb is at the front of the train.](8d9883ba355e8ba044f09fcb5b295036_img.jpg)

Figure 11.53: A diagram in the tunnel frame. A tunnel of length L is shown. A train of length L/γ is moving to the right with velocity v. The sensor is at the back of the train, and the bomb is at the front of the train.

Fig. 11.53

#### 11.7. Seeing behind the stick

The first reasoning is correct. You will be able to see a mark on the ruler that is less than  $L$  units from the wall. You will actually be able to see a mark even closer to the wall than  $L/\gamma$ , as we'll show below.

The error in the second reasoning (in the stick's frame) is that the second picture in Fig. 11.35 is *not* what you see. This second picture shows where things are at simultaneous times in the stick's frame, which are not simultaneous times in your frame. Alternatively, the error is the implicit assumption that signals travel instantaneously. But in fact the back of the stick cannot know that the front of the stick has been hit by the wall until a finite time has passed. During this time, the ruler (and the wall and you) travels farther to the left, allowing you to see more of the ruler. Let's be quantitative about this and calculate (in both frames) the closest mark to the wall that you can see.

Consider your reference frame. The stick has length  $L/\gamma$ . Therefore, when the stick hits the wall, you can see a mark a distance  $L/\gamma$  from the wall. You will, however, be able to see a mark even closer to the wall, because the back end of the stick will keep moving forward, since it doesn't know yet that the front end has hit the wall. The stopping signal (shock wave, etc.) takes time to travel.

Let's assume that the stopping signal travels along the stick at speed  $c$ . (We could instead work with a general speed  $u$ , but the speed  $c$  is simpler, and it yields an upper bound on the closest mark you can see.) Where will the signal reach the back end? Starting from the time the stick hits the wall, the signal travels backward from the wall at speed  $c$ , while the back end of the stick travels forward at speed  $v$  (from a point  $L/\gamma$  away from the wall). So the relative speed (as viewed by you) of the signal and the back end is  $c + v$ . Therefore, the signal hits the back end after a time  $(L/\gamma)/(c + v)$ . During this time, the signal has traveled a distance  $c(L/\gamma)/(c + v)$  from the wall. The closest point to the wall that you can see on the ruler is therefore the mark with the value

$$\frac{L}{\gamma(1 + \beta)} = L \sqrt{\frac{1 - \beta}{1 + \beta}}. \quad (11.81)$$

Now consider the stick's reference frame. The wall is moving to the left toward the stick at speed  $v$ . After the wall hits the right end of the stick, the signal moves to the left with speed  $c$ , while the wall keeps moving to the left with speed  $v$ . Where is the wall when the signal reaches the left end? The wall travels  $v/c$  as fast as the signal, so it travels a distance  $Lv/c$  in the time that the signal travels the distance  $L$ . This means that the wall is  $L(1 - v/c)$  away from the left end of the stick. In the stick's frame, this corresponds to a distance  $\gamma L(1 - v/c)$  on the ruler, because the ruler is length contracted. So the left end of the stick is at the mark with the value

$$L\gamma(1 - \beta) = L \sqrt{\frac{1 - \beta}{1 + \beta}}, \quad (11.82)$$

in agreement with Eq. (11.81).

#### 11.8. Cookie cutter

Let the diameter of the cookie cutter be  $L$ , and consider the two following reasonings.

- In the lab frame, the dough is length contracted, so the diameter  $L$  corresponds to a distance larger than  $L$  (namely  $\gamma L$ ) in the dough's frame. Therefore, when you buy a cookie, it is stretched out by a factor  $\gamma$  in the direction of the belt.<sup>43</sup>

<sup>43</sup> The shape is an ellipse, since that's what a stretched-out circle is. The eccentricity of an ellipse is the focal distance divided by the semi-major axis length. As an exercise, you can show that this equals  $\beta \equiv v/c$  here.

- In the frame of the dough, the cookie cutter is length contracted down to  $L/\gamma$  in the direction of motion. So in the frame of the dough, the cookies have a length of only  $L/\gamma$ . Therefore, when you buy a cookie, it is squashed by a factor  $\gamma$  in the direction of the belt.

Which reasoning is correct? The first one is. The cookies are stretched out. The fallacy in the second reasoning is that the various parts of the cookie cutter do *not* strike the dough simultaneously in the dough frame. What the dough sees is this: Assuming that the cutter moves to the left, the right side of the cutter stamps the dough, then nearby parts of the cutter stamp it, and so on, until finally the left side of the cutter stamps the dough. But by this time the front (that is, the left) of the cutter has moved farther to the left. So the cookie turns out to be longer than  $L$ . It takes a little work to demonstrate (by working in the dough frame) that the length is actually  $\gamma L$ , but let's do that now.

Consider the moment when the rightmost point of the cutter strikes the dough. In the dough frame, a clock at the rear (the right side) of the cutter reads  $Lv/c^2$  more than a clock at the front (the left side). The front clock must therefore advance by  $Lv/c^2$  by the time it strikes the dough. (This is true because all points on the cutter strike the dough simultaneously in the cutter frame. Hence, all cutter clocks read the same when they strike.) But due to time dilation, this takes a time  $\gamma(Lv/c^2)$  in the dough frame. During this time, the cutter travels a distance  $v(\gamma Lv/c^2)$ . Since the front of the cutter was initially a distance  $L/\gamma$  (due to length contraction) ahead of the back, the total length of the cookie in the dough frame is

$$\ell = \frac{L}{\gamma} + v \left( \frac{\gamma Lv}{c^2} \right) = \gamma L \left( \frac{1}{\gamma^2} + \frac{v^2}{c^2} \right) = \gamma L \left( \left( 1 - \frac{v^2}{c^2} \right) + \frac{v^2}{c^2} \right) = \gamma L,$$

as we wanted to show. If the dough is then slowly decelerated, the shape of the cookies won't change. So this is the shape you see in the store.

#### 11.9. Getting shorter

- (a) In the frame in which the balls are initially at rest, the beginning picture (when the left person catches the left ball when his clock reads zero) is shown in Fig. 11.54. The balls are a distance  $\gamma L$  apart, and the people's separation is length contracted down to  $L/\gamma$ . The front person's clock is  $Lv/c^2$  behind the back person's clock, so it reads  $-Lv/c^2$ .

The ending picture (when the right person catches the right ball when his clock reads zero) is shown in Fig. 11.55. By the time the right person catches the ball, the left person has moved to the right while holding the left ball. The left person's clock is ahead, so it reads  $Lv/c^2$ .

- (b) By looking at the distances in the figures, we see that the people travel a distance  $\gamma L - L/\gamma$ .

Let's now use the clock readings to get the distance. The total time for the process is  $\gamma(Lv/c^2)$  because each person's clock advances by  $Lv/c^2$ , but these clocks run slow in the frame we're working in. Since the speed of the people is  $v$ , the distance they travel is  $v(\gamma Lv/c^2)$ . This had better be equal to  $\gamma L - L/\gamma$ . And it is, because

$$\gamma L - \frac{L}{\gamma} = \gamma L \left( 1 - \frac{1}{\gamma^2} \right) = \gamma L \left( 1 - \left( 1 - \frac{v^2}{c^2} \right) \right) = \frac{\gamma Lv^2}{c^2}. \quad (11.83)$$

If we then shift to the frame in which everything is at rest, we see that the proper distance between the balls is  $L$ , as we wanted to show.

- (c) To sum up, the proper distance between the balls decreases because in the frame in which the balls are initially at rest, the left person catches the left ball first and then drags it closer to the right ball by the time the right person catches that one. So it all comes down to the loss of simultaneity.

![Diagram Fig. 11.54: Initial state in the ball rest frame. Two black dots representing balls are separated by a distance gamma L. Two stick figures representing people are moving to the right at speed v. The distance between the people is L/gamma. The left person's clock reads 0, and the right person's clock reads -Lv/c^2.](54443800bf1fde2ed701c319a9bdd64d_img.jpg)

Diagram Fig. 11.54: Initial state in the ball rest frame. Two black dots representing balls are separated by a distance gamma L. Two stick figures representing people are moving to the right at speed v. The distance between the people is L/gamma. The left person's clock reads 0, and the right person's clock reads -Lv/c^2.

Fig. 11.54

![Diagram Fig. 11.55: Final state in the ball rest frame. The left person has caught the left ball and the right person has caught the right ball. The distance between the balls is still gamma L. The left person's clock now reads Lv/c^2, and the right person's clock reads 0. The people are still moving to the right at speed v.](bf42aa5c35d3d07f38b45bed2e26ce5b_img.jpg)

Diagram Fig. 11.55: Final state in the ball rest frame. The left person has caught the left ball and the right person has caught the right ball. The distance between the balls is still gamma L. The left person's clock now reads Lv/c^2, and the right person's clock reads 0. The people are still moving to the right at speed v.

Fig. 11.55

#### 11.10. A bunch of L.T.'s

Using the results from the “Passing trains” examples in Sections 11.5.1 and 11.6, the relative speeds and the associated  $\gamma$  factors for the six pairs of frames are

|          | <i>AB</i> | <i>AC</i> | <i>AD</i>     | <i>BC</i> | <i>BD</i>     | <i>CD</i>     |
|----------|-----------|-----------|---------------|-----------|---------------|---------------|
| <i>v</i> | $5c/13$   | $4c/5$    | $c/5$         | $3c/5$    | $c/5$         | $5c/7$        |
| $\gamma$ | $13/12$   | $5/3$     | $5/2\sqrt{6}$ | $5/4$     | $5/2\sqrt{6}$ | $7/2\sqrt{6}$ |

From the example in Section 11.6, the separations between the two events in the four frames are

|            | <i>A</i> | <i>B</i> | <i>C</i> | <i>D</i>       |
|------------|----------|----------|----------|----------------|
| $\Delta x$ | $-L$     | $L$      | $5L$     | $0$            |
| $\Delta t$ | $5L/c$   | $5L/c$   | $7L/c$   | $2\sqrt{6}L/c$ |

The Lorentz transformations are

$$\begin{aligned}\Delta x &= \gamma(\Delta x' + v \Delta t'), \\ \Delta t &= \gamma(\Delta t' + v \Delta x'/c^2).\end{aligned}\tag{11.84}$$

For each of the six pairs, we'll transform from the faster frame to the slower frame. This means that the coordinates of the faster frame will be on the right-hand side of the L.T.'s. The sign on the right-hand side of the L.T.'s will therefore always be a “+.” In the *AB* case, for example, we'll write “Frames *B* and *A*,” in that order, to signify that the *B* coordinates are on the left-hand side and the *A* coordinates are on the right-hand side. We'll simply list the L.T.'s for the six cases, and you can check that they do indeed all work out.

$$\begin{aligned}\text{Frames } B \text{ and } A : \quad L &= \frac{13}{12}\left(-L + \left(\frac{5c}{13}\right)\left(\frac{5L}{c}\right)\right), \\ \frac{5L}{c} &= \frac{13}{12}\left(\frac{5L}{c} + \frac{\frac{5c}{13}(-L)}{c^2}\right).\end{aligned}$$

$$\begin{aligned}\text{Frames } C \text{ and } A : \quad 5L &= \frac{5}{3}\left(-L + \left(\frac{4c}{5}\right)\left(\frac{5L}{c}\right)\right), \\ \frac{7L}{c} &= \frac{5}{3}\left(\frac{5L}{c} + \frac{\frac{4c}{5}(-L)}{c^2}\right).\end{aligned}$$

$$\begin{aligned}\text{Frames } D \text{ and } A : \quad 0 &= \frac{5}{2\sqrt{6}}\left(-L + \left(\frac{c}{5}\right)\left(\frac{5L}{c}\right)\right), \\ \frac{2\sqrt{6}L}{c} &= \frac{5}{2\sqrt{6}}\left(\frac{5L}{c} + \frac{\frac{c}{5}(-L)}{c^2}\right).\end{aligned}$$

$$\begin{aligned}\text{Frames } C \text{ and } B : \quad 5L &= \frac{5}{4}\left(L + \left(\frac{3c}{5}\right)\left(\frac{5L}{c}\right)\right), \\ \frac{7L}{c} &= \frac{5}{4}\left(\frac{5L}{c} + \frac{\frac{3c}{5}L}{c^2}\right).\end{aligned}\tag{11.85}$$

$$\text{Frames } B \text{ and } D : \quad L = \frac{5}{2\sqrt{6}} \left( 0 + \left( \frac{c}{5} \right) \left( \frac{2\sqrt{6}L}{c} \right) \right),$$

$$\frac{5L}{c} = \frac{5}{2\sqrt{6}} \left( \frac{2\sqrt{6}L}{c} + \frac{\frac{c}{5}(0)}{c^2} \right).$$

$$\text{Frames } C \text{ and } D : \quad 5L = \frac{7}{2\sqrt{6}} \left( 0 + \left( \frac{5c}{7} \right) \left( \frac{2\sqrt{6}L}{c} \right) \right),$$

$$\frac{7L}{c} = \frac{7}{2\sqrt{6}} \left( \frac{2\sqrt{6}L}{c} + \frac{\frac{5c}{7}(0)}{c^2} \right).$$

#### 11.11. Equal speeds

FIRST SOLUTION: Let  $C$  move at speed  $v$  with respect to the ground, and let the relative speed of  $C$  and both  $A$  and  $B$  be  $u$  (as viewed by  $C$ ). Then two different expressions for  $u$  are the relativistic subtraction of  $v$  from  $4c/5$ , and the relativistic subtraction of  $3c/5$  from  $v$ . Therefore (dropping the  $c$ 's),

$$\frac{\frac{4}{5} - v}{1 - \frac{4}{5}v} = u = \frac{v - \frac{3}{5}}{1 - \frac{3}{5}v}. \quad (11.86)$$

This gives  $0 = 35v^2 - 74v + 35 = (5v - 7)(7v - 5)$ . Since the  $v = 7/5$  root represents a speed larger than  $c$ , we must have

$$v = \frac{5}{7}c. \quad (11.87)$$

Plugging this back into Eq. (11.86) gives  $u = c/5$ .

SECOND SOLUTION: With  $v$  and  $u$  defined as above, two different expressions for  $v$  are the relativistic subtraction of  $u$  from  $4c/5$ , and the relativistic addition of  $u$  to  $3c/5$ . Therefore,

$$\frac{\frac{4}{5} - u}{1 - \frac{4}{5}u} = v = \frac{\frac{3}{5} + u}{1 + \frac{3}{5}u}. \quad (11.88)$$

This gives  $0 = 5u^2 - 26u + 5 = (5u - 1)(u - 5)$ . Since the  $u = 5$  root represents a speed larger than  $c$ , we must have

$$u = \frac{c}{5}. \quad (11.89)$$

Plugging this back into Eq. (11.88) gives  $v = 5c/7$ .

THIRD SOLUTION: The relative speed of  $A$  and  $B$  is

$$\frac{\frac{4}{5} - \frac{3}{5}}{1 - \frac{4}{5} \cdot \frac{3}{5}} = \frac{5}{13}. \quad (11.90)$$

From  $C$ 's point of view, this  $5/13$  is the result of relativistically adding  $u$  with another  $u$ . Therefore,

$$\frac{5}{13} = \frac{2u}{1 + u^2} \implies 5u^2 - 26u + 5 = 0, \quad (11.91)$$

as in the second solution.

#### 11.12. More equal speeds

Let  $u$  be the speed at which  $C$  sees  $A$  and  $B$  approaching her. So  $u$  is the desired speed of  $C$  with respect to  $B$ , that is, the ground. From  $C$ 's point of view, the given speed  $v$  is the result of relativistically adding  $u$  with another  $u$ . Therefore (dropping the  $c$ 's),

$$v = \frac{2u}{1 + u^2} \implies u = \frac{1 - \sqrt{1 - v^2}}{v}. \quad (11.92)$$

The quadratic equation for  $u$  also has a solution with a plus sign in front of the square root, but this solution cannot be correct, because it is greater than 1 (and in fact goes to infinity as  $v$  goes to zero). The above solution for  $u$  has the proper limit as  $v$  goes to zero, namely  $u \rightarrow v/2$ , which can be obtained by using the Taylor expansion for the square root.

The ratio of the distances  $CB$  and  $AC$  in the lab frame is the same as the ratio of the differences in the velocities in the lab frame (because both  $A$  and  $C$  run into  $B$  at the same time, so you could imagine running the scenario backwards in time). Therefore,

$$\begin{aligned} \frac{CB}{AC} &= \frac{V_C - V_B}{V_A - V_C} = \frac{\frac{1-\sqrt{1-v^2}}{v} - 0}{v - \frac{1-\sqrt{1-v^2}}{v}} \\ &= \frac{1 - \sqrt{1-v^2}}{\sqrt{1-v^2} - (1-v^2)} \\ &= \frac{1}{\sqrt{1-v^2}} \equiv \gamma. \end{aligned} \quad (11.93)$$

We see that  $C$  is  $\gamma$  times as far from  $B$  as she is from  $A$ , as measured in the lab frame. Note that for nonrelativistic speeds, we have  $\gamma \approx 1$ , so  $C$  is midway between  $A$  and  $B$ , as expected. An intuitive reason for the simple factor of  $\gamma$  is the following. Imagine that  $A$  and  $B$  are carrying identical jousting sticks as they run toward  $C$ . Consider what the situation looks like when the tips of the sticks reach  $C$ . In the lab frame (in which  $B$  is at rest),  $B$ 's stick is uncontracted, but  $A$ 's stick is length contracted by a factor  $\gamma$ . Therefore, in the lab frame,  $A$  is closer to  $C$  than  $B$  is, by a factor  $\gamma$ .

#### 11.13. Equal transverse speeds

From your point of view, the lab frame is moving with speed  $v$  in the negative  $x$  direction. The transverse velocity-addition formula, Eq. (11.38), therefore gives the  $y$  speed in your frame as  $u_y/\gamma(1 - u_x v)$ . Demanding that this equals  $u_y$  gives

$$\gamma(1 - u_x v) = 1 \quad \Rightarrow \quad \sqrt{1-v^2} = (1 - u_x v) \quad \Rightarrow \quad v = \frac{2u_x}{1 + u_x^2}, \quad (11.94)$$

or  $v = 0$ , of course. This  $v$  is simply the relativistic addition of  $u_x$  with itself. This makes sense, because it means that both your frame and the original lab frame move with speed  $u_x$  (but in opposite directions) relative to the frame in which the object has no speed in the  $x$  direction. By symmetry, therefore, the  $y$  speed of the object must be the same in your frame and in the lab frame.

### 11.14. Relative speed

Consider the frame  $S'$  that travels along with the point  $P$  midway between the particles.  $S'$  moves at speed  $v \cos \theta$ , so the  $\gamma$  factor relating it to the lab frame is

$$\gamma = \frac{1}{\sqrt{1-v^2 \cos^2 \theta}}. \quad (11.95)$$

Let's find the vertical speeds of the particles in  $S'$ . Since the particles have  $u'_x = 0$ , the transverse velocity-addition formula, Eq. (11.38), gives  $v \sin \theta = u'_y/\gamma$ . Therefore, in  $S'$  each particle moves along the vertical axis away from  $P$  with speed

$$u'_y = \gamma v \sin \theta. \quad (11.96)$$

The speed of one particle as viewed by the other can now be found via the longitudinal velocity-addition formula,

$$V = \frac{2u'_y}{1 + u'^2_y} = \frac{\frac{2v \sin \theta}{\sqrt{1-v^2 \cos^2 \theta}}}{1 + \frac{v^2 \sin^2 \theta}{1-v^2 \cos^2 \theta}} = \frac{2v \sin \theta \sqrt{1-v^2 \cos^2 \theta}}{1-v^2 \cos 2\theta}. \quad (11.97)$$

If desired, this can be written as (for future reference in Chapter 13)

$$V = \sqrt{1 - \frac{(1 - v^2)^2}{(1 - v^2 \cos 2\theta)^2}}. \quad (11.98)$$

REMARK: If  $2\theta = 180^\circ$ , then  $V = 2v/(1 + v^2)$ , as it should. And if  $\theta = 0^\circ$ , then  $V = 0$ , as it should. If  $\theta$  is very small, then the result reduces to  $V \approx 2v \sin \theta / \sqrt{1 - v^2}$ , which is simply the nonrelativistic addition of (essentially) the speed in Eq. (11.96) with itself, as it should be. ♣

#### 11.15. Another relative speed

Let the velocity of  $A$  point in the  $x$  direction, as shown in Fig. 11.56. Let  $S'$  be the lab frame, and let  $S$  be  $A$ 's frame (so frame  $S'$  moves at velocity  $-u$  with respect to  $S$ ). The  $x$  and  $y$  speeds of  $B$  in frame  $S'$  are  $v \cos \theta$  and  $v \sin \theta$ . Therefore, the longitudinal and transverse velocity-addition formulas, Eqs. (11.31) and (11.38), give the components of  $B$ 's velocity in  $S$  as

$$\begin{aligned} V_x &= \frac{v \cos \theta - u}{1 - uv \cos \theta}, \\ V_y &= \frac{v \sin \theta}{\gamma_u(1 - uv \cos \theta)} = \frac{\sqrt{1 - u^2} v \sin \theta}{1 - uv \cos \theta}. \end{aligned} \quad (11.99)$$

The total speed of  $B$  in frame  $S$  (that is, from  $A$ 's point of view) is therefore

$$\begin{aligned} V &= \sqrt{V_x^2 + V_y^2} = \sqrt{\left(\frac{v \cos \theta - u}{1 - uv \cos \theta}\right)^2 + \left(\frac{\sqrt{1 - u^2} v \sin \theta}{1 - uv \cos \theta}\right)^2} \\ &= \frac{\sqrt{u^2 + v^2 - 2uv \cos \theta - u^2 v^2 \sin^2 \theta}}{1 - uv \cos \theta}. \end{aligned} \quad (11.100)$$

If desired, this can be written as

$$V = \sqrt{1 - \frac{(1 - u^2)(1 - v^2)}{(1 - uv \cos \theta)^2}}. \quad (11.101)$$

The reason why this can be written in such an organized form will become clear in Chapter 13.

REMARK: If  $u = v$ , this reduces to the result of the previous problem (if we replace  $\theta$  by  $2\theta$ ). If  $\theta = 180^\circ$ , then  $V = (u + v)/(1 + uv)$ , as it should. And if  $\theta = 0^\circ$ , then  $V = |v - u|/(1 - uv)$ , as it should. ♣

#### 11.16. Transverse velocity addition

Assume that a clock on the particle shows a time  $T$  between successive passes of the dotted lines. In frame  $S'$ , the speed of the particle is  $u'$ , so the time-dilation factor is  $\gamma' = 1/\sqrt{1 - u'^2}$ . The time between successive passes of the dotted lines is therefore  $T_{S'} = \gamma' T$ .

In frame  $S$ , the speed of the particle is  $\sqrt{v^2 + u^2}$ . (Yes, the Pythagorean theorem holds for these speeds, because both speeds are measured with respect to the same frame.) Hence, the time-dilation factor is  $\gamma = 1/\sqrt{1 - v^2 - u^2}$ . The time between successive passes of the dotted lines is therefore  $T_S = \gamma T$ . Equating our two expressions for  $T_S/T_{S'}$  gives

$$\frac{u'}{u} = \frac{T_S}{T_{S'}} = \frac{\sqrt{1 - u'^2}}{\sqrt{1 - v^2 - u^2}}. \quad (11.102)$$

![Diagram illustrating the velocity addition problem. Frame S' is the lab frame, and frame S is moving with velocity u relative to S'. Point A is at the origin of S. Point B is moving with velocity v at an angle theta to the x-axis in S'. The components of B's velocity in S' are v cos theta and v sin theta. The total velocity of B in S is V.](5e73c239dfba1ee723690328fe3b88f0_img.jpg)

The diagram shows two frames of reference, S and S'. Frame S' is the lab frame, and frame S is moving with velocity u relative to S'. Point A is at the origin of S. Point B is moving with velocity v at an angle theta to the x-axis in S'. The components of B's velocity in S' are v cos theta and v sin theta. The total velocity of B in S is V.

Diagram illustrating the velocity addition problem. Frame S' is the lab frame, and frame S is moving with velocity u relative to S'. Point A is at the origin of S. Point B is moving with velocity v at an angle theta to the x-axis in S'. The components of B's velocity in S' are v cos theta and v sin theta. The total velocity of B in S is V.

Fig. 11.56

Solving for  $u$  gives the desired result,

$$u = u' \sqrt{1 - v^2} \equiv \frac{u'}{\gamma_v}. \quad (11.103)$$

REMARK: A slightly quicker method is the following. Imagine a clock at rest in  $S'$ , with the same  $x'$  value as the particle. Let this clock tick simultaneously (as seen in  $S'$ ) with the particle's crossings of the dotted lines. Then the clock also ticks simultaneously with the particle's crossings of the dotted lines in  $S$ , because the clock and the particle have the same  $x'$  values. But the clock ticks slower in  $S$  by a factor  $\sqrt{1 - v^2}$ . Therefore, the  $y$  speed is smaller in  $S$  by this factor, as we wanted to show. ♣

#### 11.17. Many velocity additions

Let's first check the formula for  $N = 1$  and  $N = 2$ . When  $N = 1$ , the formula gives

$$\beta_{(1)} = \frac{P_1^+ - P_1^-}{P_1^+ + P_1^-} = \frac{(1 + \beta_1) - (1 - \beta_1)}{(1 + \beta_1) + (1 - \beta_1)} = \beta_1, \quad (11.104)$$

as it should. And when  $N = 2$ , the formula gives

$$\beta_{(2)} = \frac{P_2^+ - P_2^-}{P_2^+ + P_2^-} = \frac{(1 + \beta_1)(1 + \beta_2) - (1 - \beta_1)(1 - \beta_2)}{(1 + \beta_1)(1 + \beta_2) + (1 - \beta_1)(1 - \beta_2)} = \frac{\beta_1 + \beta_2}{1 + \beta_1 \beta_2}, \quad (11.105)$$

in agreement with the velocity-addition formula.

Let's now prove the formula for general  $N$ . We will use induction. That is, we will assume that the result holds for  $N$  and then show that it holds for  $N + 1$ . To find the speed,  $\beta_{(N+1)}$ , of the object with respect to  $S_{N+1}$ , we can relativistically add the speed of the object with respect to  $S_N$  (which is  $\beta_{(N)}$ ) with the speed of  $S_N$  with respect to  $S_{N+1}$  (which is  $\beta_{N+1}$ ). This gives

$$\beta_{(N+1)} = \frac{\beta_{N+1} + \beta_{(N)}}{1 + \beta_{N+1} \beta_{(N)}}. \quad (11.106)$$

Under the assumption that our formula holds for  $N$ , this becomes

$$\begin{aligned} \beta_{(N+1)} &= \frac{\beta_{N+1} + \frac{P_N^+ - P_N^-}{P_N^+ + P_N^-}}{1 + \beta_{N+1} \frac{P_N^+ - P_N^-}{P_N^+ + P_N^-}} = \frac{\beta_{N+1}(P_N^+ + P_N^-) + (P_N^+ - P_N^-)}{(P_N^+ + P_N^-) + \beta_{N+1}(P_N^+ - P_N^-)} \\ &= \frac{P_N^+(1 + \beta_{N+1}) - P_N^-(1 - \beta_{N+1})}{P_N^+(1 + \beta_{N+1}) + P_N^-(1 - \beta_{N+1})} \\ &\equiv \frac{P_{N+1}^+ - P_{N+1}^-}{P_{N+1}^+ + P_{N+1}^-}, \end{aligned} \quad (11.107)$$

as we wanted to show. We have therefore shown that if the result holds for  $N$ , then it also holds for  $N + 1$ . Since we know that the result does indeed hold for  $N = 1$ , it therefore holds for all  $N$ .

The expression for  $\beta_{(N)}$  has some expected properties. It is symmetric in the  $\beta_i$ . And if the given object is a photon with  $\beta_1 = 1$ , then  $P_N^- = 0$ , which gives  $\beta_{(N)} = 1$  as it should. And if the given object is a photon with  $\beta_1 = -1$ , then  $P_N^+ = 0$ , which gives  $\beta_{(N)} = -1$  as it should.

REMARK: We can use the result of this problem to derive the  $v(t)$  given in Eq. (11.64). First, note that if all the  $\beta_i$  here are equal, and if their common value is sufficiently

small, then

$$\beta_{(N)} = \frac{(1 + \beta)^N - (1 - \beta)^N}{(1 + \beta)^N + (1 - \beta)^N} \approx \frac{e^{\beta N} - e^{-\beta N}}{e^{\beta N} + e^{-\beta N}} = \tanh(\beta N). \quad (11.108)$$

Let  $\beta$  equal  $a dt/c$ , which is the relative speed of two frames at nearby times in the spaceship scenario leading up to Eq. (11.64). If we let  $N = t/dt$  be the number of frames (and if we take the limit  $dt \rightarrow 0$ ), then we have reproduced the spaceship scenario. Therefore, the  $\beta_{(N)}$  in Eq. (11.108) should equal the  $v(t)$  in Eq. (11.64). And indeed, with  $\beta = a dt/c$  and  $N = t/dt$ , Eq. (11.108) gives  $\beta_{(N)} = \tanh(at/c)$ , as desired. ♣

#### **11.18. Velocity addition from scratch**

As stated in the problem, we will use the fact that the meeting of the photon and the ball occurs at the same fraction of the way along the train, independent of the frame. This is true because although distances may change depending on the frame, fractions remain the same, because length contraction doesn't depend on position. We'll compute the desired fraction in the train frame  $S'$ , and then in the ground frame  $S$ .

**TRAIN FRAME:** Let the train have length  $L'$  in the train frame. Let's first find the time at which the photon meets the ball (see Fig. 11.57). From the figure, we see that the sum of the distances traveled by the ball and the photon, which is  $v_1 t' + ct'$ , must equal twice the length of the train, which is  $2L'$ . The time of the meeting is therefore

$$t' = \frac{2L'}{c + v_1}. \quad (11.109)$$

The distance the ball has traveled is then  $v_1 t' = 2v_1 L'/(c + v_1)$ , and the desired fraction  $F'$  is

$$F' = \frac{2v_1}{c + v_1}. \quad (11.110)$$

**GROUND FRAME:** Let the speed of the ball with respect to the ground be  $v$ , and let the train have length  $L$  in the ground frame ( $L$  equals  $L'/\gamma$ , but we're not going to use this). Again, let's first find the time at which the photon meets the ball (see Fig. 11.58). Light takes a time  $L/(c - v_2)$  to reach the mirror, because the mirror is receding at speed  $v_2$ . At this time, the light has traveled a distance  $cL/(c - v_2)$ . From the figure, we see that we can use the same reasoning as in the train-frame case, but now with the sum of the distances traveled by the ball and the photon, which is  $vt + ct$ , equaling  $2cL/(c - v_2)$ . The time of the meeting is therefore

$$t = \frac{2cL}{(c - v_2)(c + v)}. \quad (11.111)$$

The relative speed of the ball and the back of the train (as viewed in the ground frame) is  $v - v_2$ , so the distance between the ball and the back of the train at this time is  $2(v - v_2)cL/[(c - v_2)(c + v)]$ . The desired fraction  $F$  is therefore

$$F = \frac{2(v - v_2)c}{(c - v_2)(c + v)}. \quad (11.112)$$

We can now equate the above expressions for  $F'$  and  $F$ . For convenience, define  $\beta \equiv v/c$ ,  $\beta_1 \equiv v_1/c$ , and  $\beta_2 \equiv v_2/c$ . Then  $F' = F$  yields

$$\frac{\beta_1}{1 + \beta_1} = \frac{\beta - \beta_2}{(1 - \beta_2)(1 + \beta)}. \quad (11.113)$$

Solving for  $\beta$  in terms of  $\beta_1$  and  $\beta_2$  gives

$$\beta = \frac{\beta_1 + \beta_2}{1 + \beta_1 \beta_2}, \quad (11.114)$$

as desired. This problem is solved in Mermin (1983).

![Diagram of a train in frame S' with a photon and a ball.](fe5d233799fc7443edd7879ff39bef58_img.jpg)

A diagram of a train in frame  $S'$ . The train has length  $L'$ . A photon (represented by a wavy arrow) is emitted from the back of the train. A ball (represented by a dot) is moving towards the photon with velocity  $v_1$ . The photon is moving towards the front of the train.

Diagram of a train in frame S' with a photon and a ball.

(frame  $S'$ )

**Fig. 11.57**

![Diagram of a train in frame S showing the start, later, and finish positions of a photon and ball.](bdb49081a36f3aeb3b127b6960259c90_img.jpg)

A diagram of a train in frame  $S$  showing three stages: (start), (later), and (finish). In the (start) stage, the train has length  $L$  and is moving with velocity  $v_2$ . A photon is emitted from the back. In the (later) stage, the photon is at the front of the train. In the (finish) stage, the photon has reached the back of the train. The ball is moving with velocity  $v$  relative to the ground.

Diagram of a train in frame S showing the start, later, and finish positions of a photon and ball.

**Fig. 11.58**

![Figure 11.59: A spacetime diagram in A's reference frame. The vertical axis is ct and the horizontal axis is x. Worldline A is a vertical line on the left. Worldline B is a line with a positive slope starting from the origin. Worldline C is a line with a negative slope starting from the top of the ct axis. Worldline B intersects worldline C, and worldline B intersects worldline A at a point labeled t on the ct axis. A dashed line is also shown.](8520eb5255f7a2b234c75e56cbf642be_img.jpg)

Figure 11.59: A spacetime diagram in A's reference frame. The vertical axis is ct and the horizontal axis is x. Worldline A is a vertical line on the left. Worldline B is a line with a positive slope starting from the origin. Worldline C is a line with a negative slope starting from the top of the ct axis. Worldline B intersects worldline C, and worldline B intersects worldline A at a point labeled t on the ct axis. A dashed line is also shown.

Fig. 11.59

![Figure 11.60: A spacetime diagram in B's reference frame. The vertical axis is ct and the horizontal axis is x. Worldline B is a vertical line in the center. Worldline A is a line with a negative slope on the left. Worldline C is a line with a positive slope on the right. Worldline A and C intersect at a point on the x-axis. Worldline B intersects worldline A and worldline C at different points.](ae11c60feb544e83a0ef802bf234adc0_img.jpg)

Figure 11.60: A spacetime diagram in B's reference frame. The vertical axis is ct and the horizontal axis is x. Worldline B is a vertical line in the center. Worldline A is a line with a negative slope on the left. Worldline C is a line with a positive slope on the right. Worldline A and C intersect at a point on the x-axis. Worldline B intersects worldline A and worldline C at different points.

Fig. 11.60

![Figure 11.61: A spacetime diagram in C's reference frame. The vertical axis is ct and the horizontal axis is x. Worldline C is a vertical line on the right. Worldline A is a line with a positive slope on the left. Worldline B is a line with a steeper positive slope, starting from the same point on the x-axis as A but ending at a lower point on the ct axis than A. Worldline A and C intersect at a point on the ct axis.](75a90127105ca42b446a33f4a3f4f3d3_img.jpg)

Figure 11.61: A spacetime diagram in C's reference frame. The vertical axis is ct and the horizontal axis is x. Worldline C is a vertical line on the right. Worldline A is a line with a positive slope on the left. Worldline B is a line with a steeper positive slope, starting from the same point on the x-axis as A but ending at a lower point on the ct axis than A. Worldline A and C intersect at a point on the ct axis.

Fig. 11.61

#### 11.19. Modified twin paradox

- (a) In  $A$ 's reference frame, the worldlines of  $A$ ,  $B$ , and  $C$  are shown in Fig. 11.59.  $B$ 's clock runs slow by a factor  $1/\gamma$ . Therefore, if  $A$ 's clock reads  $t$  when  $B$  meets  $C$ , then  $B$ 's clock reads  $t/\gamma$  when he meets  $C$ . So the time he gives to  $C$  is  $t/\gamma$ .

In  $A$ 's reference frame, the time between this event and the event where  $C$  meets  $A$  is again  $t$ , because  $B$  and  $C$  travel at the same speed. But  $A$  sees  $C$ 's clock run slow by a factor  $1/\gamma$ , so  $A$  sees  $C$ 's clock increase by  $t/\gamma$ . Therefore, when  $A$  and  $C$  meet,  $A$ 's clock reads  $2t$ , and  $C$ 's clock reads  $2t/\gamma$ . In other words,  $T_C = T_A/\gamma$ .

- (b) Let's now look at things in  $B$ 's frame. The worldlines of  $A$ ,  $B$ , and  $C$  are shown in Fig. 11.60. From  $B$ 's point of view, there are two competing effects that lead to the relation  $T_C = T_A/\gamma$ . The first is that  $B$  sees  $A$ 's clock run slow, so the time he hands off to  $C$  is *larger* than the time  $A$ 's clock reads at this moment. The second effect is that from this point on,  $B$  sees  $C$ 's clock run *slower* than  $A$ 's (because the relative speed of  $C$  and  $B$  is greater than the relative speed of  $A$  and  $B$ ). It turns out that this slowness wins out over the head start that  $C$ 's clock had over  $A$ 's. So in the end,  $C$ 's clock reads a smaller time than  $A$ 's. Let's be quantitative about this.

Let  $B$ 's clock read  $t_B$  when he meets  $C$ . Then when  $B$  hands off this time to  $C$ ,  $A$ 's clock reads only  $t_B/\gamma$ . We'll find all relevant times below in terms of  $t_B$ . We must determine how much additional time elapses on  $A$ 's clock and  $C$ 's clock, by the time they meet. From the velocity-addition formula,  $B$  sees  $C$  move to the left at speed  $2v/(1+v^2)$ . He also sees  $A$  move to the left at speed  $v$ . But  $A$  had a head start of  $vt_B$  in front of  $C$ , so if  $t$  is the time (as viewed from  $B$ ) between the meeting of  $B$  and  $C$  and the meeting of  $A$  and  $C$ , then

$$\frac{2vt}{1+v^2} = vt + vt_B \implies t = t_B \left( \frac{1+v^2}{1-v^2} \right). \quad (11.115)$$

During this time,  $B$  sees  $A$ 's and  $C$ 's clocks increase by  $t$  divided by the relevant time-dilation factor. For  $A$ , this factor is  $\gamma = 1/\sqrt{1-v^2/c^2}$ . For  $C$ , it is

$$\frac{1}{\sqrt{1 - \left( \frac{2v}{1+v^2} \right)^2}} = \frac{1+v^2}{1-v^2}. \quad (11.116)$$

Therefore, the total time shown on  $A$ 's clock when  $A$  and  $C$  meet is

$$\begin{aligned} T_A &= \frac{t_B}{\gamma} + t\sqrt{1-v^2} = t_B\sqrt{1-v^2} + t_B \left( \frac{1+v^2}{1-v^2} \right) \sqrt{1-v^2} \\ &= \frac{2t_B}{\sqrt{1-v^2}}. \end{aligned} \quad (11.117)$$

And the total time shown on  $C$ 's clock when  $A$  and  $C$  meet is

$$T_C = t_B + t \left( \frac{1-v^2}{1+v^2} \right) = t_B + t_B \left( \frac{1+v^2}{1-v^2} \right) \left( \frac{1-v^2}{1+v^2} \right) = 2t_B. \quad (11.118)$$

Therefore,  $T_C = T_A\sqrt{1-v^2} \equiv T_A/\gamma$ .

- (c) Let's now work in  $C$ 's frame. The worldlines of  $A$ ,  $B$ , and  $C$  are shown in Fig. 11.61. As in part (b), the relative speed of  $B$  and  $C$  is  $2v/(1+v^2)$ , and the time-dilation factor between  $B$  and  $C$  is  $(1+v^2)/(1-v^2)$ . Also, as in part (b), let  $B$  and  $C$  meet when  $B$ 's clock reads  $t_B$ . So this is the time that  $B$  hands off to  $C$ . We'll find all relevant times below in terms of  $t_B$ .

$C$  sees  $B$ 's clock running slow, so from  $C$ 's point of view,  $B$  travels for a time  $t_B(1 + v^2)/(1 - v^2)$  after his meeting with  $A$ . In this time,  $B$  covers a distance in  $C$ 's frame equal to

$$d = t_B \left( \frac{1 + v^2}{1 - v^2} \right) \frac{2v}{1 + v^2} = \frac{2vt_B}{1 - v^2}. \quad (11.119)$$

$A$  must travel this same distance (from where he met  $B$ ) to meet up with  $C$ . We can now find  $T_A$ . The time (as viewed by  $C$ ) that it takes  $A$  to travel the distance  $d$  to reach  $C$  is  $d/v = 2t_B/(1 - v^2)$ . But since  $C$  sees  $A$ 's clock running slow by a factor  $\sqrt{1 - v^2}$ ,  $A$ 's clock will read only

$$T_A = \frac{2t_B}{\sqrt{1 - v^2}}. \quad (11.120)$$

Now let's find  $T_C$ . To find  $T_C$ , we must take  $t_B$  and add to it the extra time it takes  $A$  to reach  $C$ , compared with the time it takes  $B$  to reach  $C$ . From above, this extra time is  $2t_B/(1 - v^2) - t_B(1 + v^2)/(1 - v^2) = t_B$ . Therefore,  $C$ 's clock reads

$$T_C = 2t_B. \quad (11.121)$$

Hence,  $T_C = T_A \sqrt{1 - v^2} \equiv T_A/\gamma$ .

#### 11.20. Throwing on a train

- (a) In the train frame, the distance is simply  $d = L$ . And the time is  $t = L/(c/3) = 3L/c$ .  
 (b) i. The velocity of the ball with respect to the ground is (with  $u = c/3$  and  $v = c/2$ )

$$V_g = \frac{u + v}{1 + \frac{uv}{c^2}} = \frac{\frac{c}{3} + \frac{c}{2}}{1 + \frac{1}{3} \cdot \frac{1}{2}} = \frac{5c}{7}. \quad (11.122)$$

The length of the train in the ground frame is  $L/\gamma_{1/2} = \sqrt{3}L/2$ . Therefore, at time  $t$  the position of the front of the train is  $\sqrt{3}L/2 + vt$ . And the position of the ball is  $V_g t$ . These two positions are equal when

$$(V_g - v)t = \frac{\sqrt{3}L}{2} \implies t = \frac{\frac{\sqrt{3}L}{2}}{\frac{5c}{7} - \frac{c}{2}} = \frac{7L}{\sqrt{3}c}. \quad (11.123)$$

Equivalently, this time is obtained by noting that the ball closes the initial head start of  $\sqrt{3}L/2$  that the front of the train had, at a relative speed of  $V_g - v$ .

The distance the ball travels is  $d = V_g t = (5c/7)(7L/\sqrt{3}c) = 5L/\sqrt{3}$ .

- ii. In the train frame, the space and time intervals are  $x' = L$  and  $t' = 3L/c$ , from part (a). The  $\gamma$  factor between the frames is  $\gamma_{1/2} = 2/\sqrt{3}$ , so the Lorentz transformations give the coordinates in the ground frame as

$$\begin{aligned} x &= \gamma(x' + vt') = \frac{2}{\sqrt{3}} \left( L + \frac{c}{2} \left( \frac{3L}{c} \right) \right) = \frac{5L}{\sqrt{3}}, \\ t &= \gamma(t' + vx'/c^2) = \frac{2}{\sqrt{3}} \left( \frac{3L}{c} + \frac{c}{2} \frac{L}{c^2} \right) = \frac{7L}{\sqrt{3}c}, \end{aligned} \quad (11.124)$$

in agreement with the above results.

- (c) In the ball frame, the train has length,  $L/\gamma_{1/3} = \sqrt{8}L/3$ . Therefore, the time it takes the train to fly past the ball at speed  $c/3$  is  $t = (\sqrt{8}L/3)/(c/3) = 2\sqrt{2}L/c$ . And the distance is  $d = 0$ , of course, because the ball doesn't move in the ball frame.

(d) The values of  $c^2t^2 - x^2$  in the three frames are:

$$\text{Train frame: } c^2t^2 - x^2 = c^2(3L/c)^2 - L^2 = 8L^2.$$

$$\text{Ground frame: } c^2t^2 - x^2 = c^2(7L/\sqrt{3}c)^2 - (5L/\sqrt{3})^2 = 8L^2.$$

$$\text{Ball frame: } c^2t^2 - x^2 = c^2(2\sqrt{2}L/c)^2 - (0)^2 = 8L^2.$$

These are all equal, as they should be.

(e) The relative speed of the ball frame and the ground frame is  $5c/7$ . Therefore,  $\gamma_{5/7} = 7/2\sqrt{6}$ , and the times are indeed related by

$$t_g = \gamma t_b \iff \frac{7L}{\sqrt{3}c} = \frac{7}{2\sqrt{6}} \left( \frac{2\sqrt{2}L}{c} \right), \text{ which is true.} \quad (11.125)$$

(f) The relative speed of the ball frame and the train frame is  $c/3$ . Therefore,  $\gamma_{1/3} = 3/2\sqrt{2}$ , and the times are indeed related by

$$t_t = \gamma t_b \iff \frac{3L}{c} = \frac{3}{2\sqrt{2}} \left( \frac{2\sqrt{2}L}{c} \right), \text{ which is true.} \quad (11.126)$$

(g) The relative speed of the train frame and the ground frame is  $c/2$ . Therefore,  $\gamma_{1/2} = 2/\sqrt{3}$ , and the times are *not* related by a simple time-dilation factor, because

$$t_g \neq \gamma t_t \iff \frac{7L}{\sqrt{3}c} \neq \frac{2}{\sqrt{3}} \left( \frac{3L}{c} \right). \quad (11.127)$$

We don't obtain an equality because time dilation is legal to use only if the two events happen at the *same place* in one of the frames. Mathematically, the Lorentz transformation  $\Delta t = \gamma(\Delta t' + (v/c^2)\Delta x')$  leads to  $\Delta t = \gamma\Delta t'$  only if  $\Delta x' = 0$ . In this problem, the “ball leaving the back” and “ball hitting the front” events happen at the same place in the ball frame, but in neither the train frame nor the ground frame. Equivalently, neither the train frame nor the ground frame is any more special than the other, as far as these two events go. So if someone insisted on trying to use time dilation, he would have a hard time deciding which side of the equation the  $\gamma$  should go on.

![Minkowski diagram for Figure 11.62. The vertical axis is labeled ct and the horizontal axis is labeled x. A solid line labeled ct' is shown at a steeper angle than the x-axis. A dashed line labeled x' is shown at a shallower angle than the ct-axis. A point (2, 1) is marked on the x' axis.](9ddef731de49107cc92f81c5c9004248_img.jpg)

Minkowski diagram for Figure 11.62. The vertical axis is labeled ct and the horizontal axis is labeled x. A solid line labeled ct' is shown at a steeper angle than the x-axis. A dashed line labeled x' is shown at a shallower angle than the ct-axis. A point (2, 1) is marked on the x' axis.

Fig. 11.62

#### 11.21. A new frame

FIRST SOLUTION: Consider the Minkowski diagram in Fig. 11.62. In frame  $S$ , Event 1 is at the origin, and Event 2 is at the point  $(2, 1)$ . Consider now the frame  $S'$  whose  $x'$  axis passes through the point  $(2, 1)$ . Since all points on the  $x'$  axis are simultaneous in the frame  $S'$  (they all have  $t' = 0$ ), we see that  $S'$  is the desired frame. From Eq. (11.47), the slope of the  $x'$  axis equals  $\beta \equiv v/c$ . Since the slope is  $1/2$ , we have  $v = c/2$ . Note that by looking at our Minkowski diagram, it is clear that if the relative speed of  $S$  and  $S'$  is greater than  $c/2$ , then Event 2 occurs before Event 1 in  $S'$ . And if it is less than  $c/2$ , then Event 2 occurs after Event 1 in  $S'$ .

SECOND SOLUTION: Let the original frame be  $S$ , and let the desired frame be  $S'$ . Let  $S'$  move at speed  $v$  (in the positive direction) with respect to  $S$ . Our goal is to find  $v$ . The Lorentz transformations from  $S$  to  $S'$  are

$$\Delta x' = \gamma(\Delta x - v\Delta t), \quad \Delta t' = \gamma(\Delta t - v\Delta x/c^2). \quad (11.128)$$

We want to make  $\Delta t'$  equal to zero, so the second of these equations yields  $\Delta t - v\Delta x/c^2 = 0$ , or  $v = c^2\Delta t/\Delta x$ . We are given  $\Delta x = 2$  and  $\Delta t = 1/c$ , so the desired  $v$  is  $c/2$ .

THIRD SOLUTION: Consider the setup in Fig. 11.63, which explicitly constructs the two given events. Receivers are located at  $x = 0$  and  $x = 2$ , and a light source is

![Diagram for Figure 11.63 showing a horizontal line with two vertical bars at x=0 and x=2. A light source is located at x=0, emitting a wavy line representing a light pulse towards the right.](8b4ea502497d296f00d13c0c501093c2_img.jpg)

Diagram for Figure 11.63 showing a horizontal line with two vertical bars at x=0 and x=2. A light source is located at x=0, emitting a wavy line representing a light pulse towards the right.

Fig. 11.63

located at  $x = 1/2$ . The source emits a flash, and when the light hits a receiver we will say an event has occurred. So the left event happens at  $x = 0, ct = 1/2$ . And the right event happens at  $x = 2, ct = 3/2$ . If we want, we can shift our clocks by  $-1/(2c)$  in order to make the events happen at  $ct = 0$  and  $ct = 1$ , but this shift is irrelevant because all we are concerned with is differences in time.

Now consider an observer moving to the right at speed  $v$ . She sees the apparatus moving to the left at speed  $v$  (see Fig. 11.64). Our goal is to find the  $v$  for which the photons hit the receivers at the same time in her frame. Consider the photons moving to the left. She sees them moving at speed  $c$ , but the left-hand receiver is receding at speed  $v$ . So the relative speed (as measured by her) of the photons and the left-hand receiver is  $c - v$ . By similar reasoning, the relative speed of the photons and the right-hand receiver is  $c + v$ . The light source is three times as far from the right-hand receiver as it is from the left-hand receiver. Therefore, if the light is to reach the two receivers at the same time, we must have  $c + v = 3(c - v)$ . This gives  $v = c/2$ .

![Diagram of a light source between two receivers moving at speed v.](c5b73d753106364907c8a6aaa77bbcf5_img.jpg)

A horizontal line represents the apparatus. In the center is a light source emitting waves to the left and right. Arrows above the line indicate the light moving at speed  $c$  in both directions. Arrows below the line indicate the entire apparatus moving to the left at speed  $v$ . There are receivers at both ends of the apparatus.

Diagram of a light source between two receivers moving at speed v.

Fig. 11.64

#### **11.22. Minkowski diagram units**

All points on the  $ct'$  axis have the property that  $x' = 0$ . All points on the hyperbola have the property that  $c^2t'^2 - x'^2 = 1$ , due to the invariance of  $s^2$ . So the  $ct'$  value at the intersection point  $A$  equals 1. Therefore, we simply have to determine the distance on the paper from  $A$  to the origin (see Fig. 11.65). We'll do this by finding the  $(x, ct)$  coordinates of  $A$ . We know that  $\tan \theta = \beta$ . But  $\tan \theta = x/ct$ . Therefore,  $x = \beta(ct)$  (which is just the statement that  $x = vt$ ). Plugging this into the given information,  $c^2t'^2 - x^2 = 1$ , we find  $ct = 1/\sqrt{1 - \beta^2}$ . The distance from  $A$  to the origin is then

![Minkowski diagram showing axes ct, ct', x, x' and a hyperbola with point A.](873460b1ce58ee8e5a5dc87b76209621_img.jpg)

A Minkowski diagram with a vertical  $ct$  axis and a horizontal  $x$  axis. A rotated vertical axis  $ct'$  and a rotated horizontal axis  $x'$  are also shown, both originating from the same point. A hyperbola  $c^2t'^2 - x'^2 = 1$  is drawn in the first quadrant. Point  $A$  is the intersection of the  $ct'$  axis and the hyperbola. An angle  $\theta$  is marked between the  $ct$  axis and the  $ct'$  axis.

Minkowski diagram showing axes ct, ct', x, x' and a hyperbola with point A.

Fig. 11.65

$$\sqrt{c^2t'^2 - x^2} = ct\sqrt{1 - \beta^2} = \sqrt{\frac{1 + \beta^2}{1 - \beta^2}}. \quad (11.129)$$

This quantity is therefore the ratio of the unit sizes on the  $ct'$  and  $ct$  axes, in agreement with Eq. (11.46). Exactly the same analysis holds for the  $x$ -axis unit size ratio.

#### **11.23. Velocity addition via Minkowski**

Pick a point  $P$  on the object's worldline. Let the coordinates of  $P$  in frame  $S$  be  $(x, ct)$ . Our goal is to find the speed  $u = x/t$ . Throughout this problem, it will be easier to work with the quantities  $\beta \equiv v/c$ , so our goal is then to find  $\beta_u \equiv x/(ct)$ .

The coordinates of  $P$  in  $S'$ , namely  $(x', ct')$ , are indicated by the parallelogram in Fig. 11.66. For convenience, let  $ct'$  have length  $a$  on the paper. Then from the given information, we have  $x' = v_1t' \equiv \beta_1(ct') = \beta_1a$ . This is the distance from  $A$  to  $P$  on the paper. In terms of  $a$ , we can now determine the coordinates  $(x, ct)$  of  $P$ . The coordinates of point  $A$  are

![Minkowski diagram showing velocity addition with a parallelogram for point P.](e9f80c0701634b5cc118115dee34342d_img.jpg)

A Minkowski diagram similar to Fig. 11.65, but with a point  $P$  on a worldline. A parallelogram is constructed to find the coordinates of  $P$  in frame  $S$ . One side of the parallelogram is along the  $ct'$  axis from the origin to point  $A$ , with length  $a$ . The other side is parallel to the  $x'$  axis, from  $A$  to  $P$ , with length  $\beta_1 a$ . The angle between the  $ct$  axis and  $ct'$  axis is  $\theta$ . The angle between the  $x$  axis and  $x'$  axis is also  $\theta$ . The angle between the  $ct'$  axis and the line  $AP$  is  $\theta$ . The angle between the  $x$  axis and the line  $AP$  is  $\theta$ .

Minkowski diagram showing velocity addition with a parallelogram for point P.

Fig. 11.66

$$(x, ct)_A = (a \sin \theta, a \cos \theta). \quad (11.130)$$

The coordinates of  $P$ , relative to  $A$ , are

$$(x, ct)_{P-A} = (\beta_1 a \cos \theta, \beta_1 a \sin \theta). \quad (11.131)$$

Adding these two sets of coordinates gives the coordinates of point  $P$  as

$$(x, ct)_P = (a \sin \theta + \beta_1 a \cos \theta, a \cos \theta + \beta_1 a \sin \theta). \quad (11.132)$$

The ratio of  $x$  to  $ct$  at the point  $P$  is therefore

$$\beta_u \equiv \frac{x}{ct} = \frac{\sin \theta + \beta_1 \cos \theta}{\cos \theta + \beta_1 \sin \theta} = \frac{\tan \theta + \beta_1}{1 + \beta_1 \tan \theta} = \frac{\beta_2 + \beta_1}{1 + \beta_1 \beta_2}, \quad (11.133)$$

where we have used  $\tan \theta = v_2/c \equiv \beta_2$ , because  $S'$  moves at speed  $v_2$  with respect to  $S$ . If we change from the  $\beta$ 's back to the  $v$ 's, the result is  $u = (v_2 + v_1)/(1 + v_1 v_2/c^2)$ , as expected.

![Minkowski diagram for Fig. 11.67 showing worldlines A and B. Worldline A is vertical, and worldline B is tilted to the right. Horizontal lines represent simultaneity in A's frame, intersecting B's worldline. The vertical spacing between these lines is labeled cΔt. The worldline B is labeled with a circled B, and worldline A with a circled A.](58a075e97c11ca0d1fa659e80d6926b8_img.jpg)

Minkowski diagram for Fig. 11.67 showing worldlines A and B. Worldline A is vertical, and worldline B is tilted to the right. Horizontal lines represent simultaneity in A's frame, intersecting B's worldline. The vertical spacing between these lines is labeled cΔt. The worldline B is labeled with a circled B, and worldline A with a circled A.

Fig. 11.67

![Minkowski diagram for Fig. 11.68 showing worldlines A and B. Worldline A is vertical, and worldline B is tilted to the right. Tilted lines represent simultaneity in B's frame, intersecting A's worldline. The vertical spacing between these lines is labeled βL. The worldline B is labeled with a circled B, and worldline A with a circled A. The angle θ is shown between the x-axis and the worldline B.](b22f392916d6d0c551f927319616f27e_img.jpg)

Minkowski diagram for Fig. 11.68 showing worldlines A and B. Worldline A is vertical, and worldline B is tilted to the right. Tilted lines represent simultaneity in B's frame, intersecting A's worldline. The vertical spacing between these lines is labeled βL. The worldline B is labeled with a circled B, and worldline A with a circled A. The angle θ is shown between the x-axis and the worldline B.

Fig. 11.68

![Minkowski diagram for Fig. 11.69 showing worldlines A and B. Worldline A is vertical, and worldline B is tilted to the right. The worldline B is labeled with a circled B, and worldline A with a circled A. The distance d is marked on the x-axis.](61667071ce831f80745ed40f96ba9e0e_img.jpg)

Minkowski diagram for Fig. 11.69 showing worldlines A and B. Worldline A is vertical, and worldline B is tilted to the right. The worldline B is labeled with a circled B, and worldline A with a circled A. The distance d is marked on the x-axis.

Fig. 11.69

#### 11.24. Clapping both ways

- (a) From the usual time-dilation result,  $A$  sees  $B$ 's clock run slow, so  $B$  must clap his hands at time intervals of  $\Delta t/\gamma$  in order for the intervals to be  $\Delta t$  in  $A$ 's frame. The relevant Minkowski diagram is shown in Fig. 11.67. Let  $B$  clap at the spacetime locations where the horizontal lines (lines of simultaneity in  $A$ 's frame) intersect  $B$ 's worldline. From the given information, the vertical spacing between the lines is  $c \Delta t$ . Therefore, the spacing along  $B$ 's tilted worldline (which has a slope of  $\pm 1/\beta$ ) is  $\sqrt{1 + \beta^2} c \Delta t$ . But we know from Eq. (11.46) that the unit size of  $B$ 's  $ct$  axis on the paper is  $\sqrt{(1 + \beta^2)/(1 - \beta^2)}$  times the unit size of  $A$ 's  $ct$  axis. Therefore, the time interval between claps in  $B$ 's frame is

$$\frac{\sqrt{1 + \beta^2} c \Delta t}{\sqrt{(1 + \beta^2)/(1 - \beta^2)}} = \sqrt{1 - \beta^2} \Delta t \equiv \frac{\Delta t}{\gamma}, \quad (11.134)$$

as above.

- (b) From the usual time-dilation result,  $B$  sees  $A$ 's clock run slow, so  $A$  must clap his hands at time intervals of  $\Delta t/\gamma$  in order for the intervals to be  $\Delta t$  in  $B$ 's frame. However,  $B$  can invoke this standard time-dilation reasoning only during the parts of the trip where he is in an inertial frame. That is, he cannot invoke it during the turnaround period. We therefore have the situation shown in Fig. 11.68. Let  $A$  clap at the spacetime locations where the tilted lines (lines of simultaneity in  $B$ 's frame) intersect  $A$ 's worldline. From the given information, the tilted spacing between the lines along  $B$ 's worldline is  $c \Delta t$  time units, which has a length  $\sqrt{(1 + \beta^2)/(1 - \beta^2)} c \Delta t$  on the paper. But then by the same type of geometry reasoning that led to Eq. (11.49), the vertical spacing between the lines along  $A$ 's worldline is (as you should verify)  $\sqrt{1 - \beta^2} c \Delta t$ , which gives a time interval of  $\Delta t/\gamma$ , as above.

But the critical point here is that since the slope of the tilted lines abruptly changes when  $B$  turns around, there is a large interval of time in the middle of  $A$ 's worldline where the tilted lines don't hit it. The result is that  $A$  claps frequently for a while, then doesn't clap at all for a while, then claps frequently again. The overall result, as we will now show, is that more time elapses in  $A$ 's frame (it will turn out to be  $2L/v$ , of course, where  $L$  is the distance in  $A$ 's frame to the star) than in  $B$ 's frame ( $2L/\gamma v$ , from the usual time-dilation result).

Since the time between claps is shorter in  $A$ 's frame than in  $B$ 's frame (except in the middle region), the time elapsed on  $A$ 's clock while he is clapping is  $1/\gamma$  times the total time elapsed on  $B$ 's clock, which gives  $(2L/\gamma v)/\gamma = 2L/\gamma^2 v$ . But as shown in Fig. 11.68, the length of the region on  $A$ 's  $ct$  axis where there is no clapping is  $2\beta L$ , which corresponds to a time of  $2vL/c^2$ . The total time elapsed on  $A$ 's clock during the entire process is therefore

$$\frac{2L}{\gamma^2 v} + \frac{2vL}{c^2} = \frac{2L}{v} \left( \frac{1}{\gamma^2} + \frac{v^2}{c^2} \right) = \frac{2L}{v} \left( \left( 1 - \frac{v^2}{c^2} \right) + \frac{v^2}{c^2} \right) = \frac{2L}{v}, \quad (11.135)$$

as expected.

### 11.25. Acceleration and redshift

There are various ways to solve this problem, for example, by sending photons between the people, or by invoking the Equivalence Principle in General Relativity. We'll do it here by using a Minkowski diagram, to demonstrate that this redshift result can be derived perfectly fine using only basic Special Relativity.

Draw the world lines of the two people,  $A$  and  $B$ , as seen by an observer,  $C$ , in the frame where they were both initially at rest. We have the situation shown in Fig. 11.69. Consider an infinitesimal time  $\Delta t$ , as measured by  $C$ . At this time (in  $C$ 's frame),

$A$  and  $B$  are both moving at speed  $a\Delta t$ . The axes of the  $A$  frame are shown in Fig. 11.70. Both  $A$  and  $B$  have moved a distance  $a(\Delta t)^2/2$ , which can be neglected because  $\Delta t$  is small (it will turn out that the leading-order terms in the result are of order  $\Delta t$ , so any  $(\Delta t)^2$  terms can be ignored.) Also, the special-relativistic time-dilation factor between any of the  $A$ ,  $B$ ,  $C$  frames can be neglected, because the relative speeds are at most  $v = a\Delta t$ , so the time-dilation factors differ from 1 by order  $(\Delta t)^2$ . Let  $A$  make a little explosion (call this event  $E_1$ ) at time  $\Delta t$  in  $C$ 's frame. Then  $\Delta t$  is also the time of the explosion as measured by  $A$ , up to an error of order  $(\Delta t)^2$ .

Let's figure out where  $A$ 's  $x$  axis (that is, the "now" axis in  $A$ 's frame) meets  $B$ 's worldline. The slope of  $A$ 's  $x$  axis in the figure is  $v/c = a\Delta t/c$ . So the axis starts at a height  $c\Delta t$ , and then climbs up by the amount  $ad\Delta t/c$ , over the distance  $d$  (the distance is indeed  $d$ , up to corrections of order  $(\Delta t)^2$ ). Therefore, the axis meets  $B$ 's worldline at a height  $c\Delta t + ad\Delta t/c$  as viewed by  $C$ , that is, at a time  $\Delta t + ad\Delta t/c^2$ , as viewed by  $C$ . But  $C$ 's time is the same as  $B$ 's time (up to order  $(\Delta t)^2$ ), so  $B$ 's clock reads  $\Delta t(1 + ad/c^2)$ . Let's say that  $B$  makes a little explosion (event  $E_2$ ) at this time.

Events  $E_1$  and  $E_2$  both occur at the same time in  $A$ 's frame, because they both lie along a line of constant time in  $A$ 's frame. This means that in  $A$ 's frame,  $B$ 's clock reads  $\Delta t(1 + ad/c^2)$  when  $A$ 's clock reads  $\Delta t$ . Therefore, in  $A$ 's (changing) frame,  $B$ 's clock is sped up by a factor,

$$\frac{\Delta t_B}{\Delta t_A} = 1 + \frac{ad}{c^2}. \quad (11.136)$$

We can perform the same procedure to see how  $A$ 's clock behaves in  $B$ 's frame. Drawing  $B$ 's  $x$  axis at time  $\Delta t$ , we quickly find that in  $B$ 's (changing) frame,  $A$ 's clock is slowed down by a factor,

$$\frac{\Delta t_A}{\Delta t_B} = 1 - \frac{ad}{c^2}. \quad (11.137)$$

We'll see much more of these results in Chapter 14.

##### REMARKS:

1. In the usual Special Relativity situation where two observers fly past each other with relative speed  $v$ , they *both* see the other person's time slowed down by the same factor. This had better be the case, because the situation is symmetric between the observers. But in this problem,  $A$  sees  $B$ 's clock sped up, and  $B$  sees  $A$ 's clock slowed down. This difference is possible because the situation is *not* symmetric between  $A$  and  $B$ . The acceleration vector determines a direction in space, and one person (namely  $B$ ) is farther along this direction than the other person.
2. Another derivation of this  $ad/c^2$  result is the following. Consider the setup a short time after the start. An outside observer sees  $A$ 's and  $B$ 's clocks showing the same time. Therefore, by the usual  $vd/c^2$  rear-clock-ahead result in Special Relativity,  $B$ 's clock must read  $vd/c^2$  more than  $A$ 's, in the moving frame. The increase per unit time, as viewed by  $A$ , is therefore  $(vd/c^2)/t = ad/c^2$ . Note that any special-relativistic time-dilation or length-contraction effects are of second order in  $v/c$ , and hence negligible since  $v$  is small here. At any later time, we can repeat (roughly) this derivation in the instantaneous rest frame of  $A$ . ♣

### 11.26. Break or not break?

There are two possible reasonings, so we seem to have a paradox:

- To an observer in the original rest frame, the spaceships stay the same distance  $d$  apart. Therefore, in the frame of the spaceships, the distance between them,  $d'$ , must equal  $\gamma d$ . This is true because  $d'$  is the distance that gets length-contracted down to  $d$ . After a long enough time,  $\gamma$  will differ appreciably from 1, so the string will be stretched by a large factor. Therefore, it will break.

![Figure 11.70: A spacetime diagram showing the worldlines of two objects, A and B, in a frame C. The vertical axis is ct and the horizontal axis is x_C. Worldline A is a straight line starting from the origin with a slope of 1. Worldline B is a curve starting from the origin and curving upwards. A dashed line represents the x-axis of frame A, starting at height cΔt on the ct axis and having a slope of v/c = aΔt/c. This dashed line intersects worldline B at a point labeled with the expression (adΔt/c) / c. The horizontal distance from the origin to this intersection point is labeled d. The vertical distance from the origin to the intersection point is labeled ct_A. The vertical distance from the origin to the point on worldline B directly below the intersection point is labeled ct_B. The vertical distance from the origin to the point on worldline A directly below the intersection point is labeled cΔt.](46f7b618f90dfaf39b985bd6054c2410_img.jpg)

Figure 11.70: A spacetime diagram showing the worldlines of two objects, A and B, in a frame C. The vertical axis is ct and the horizontal axis is x\_C. Worldline A is a straight line starting from the origin with a slope of 1. Worldline B is a curve starting from the origin and curving upwards. A dashed line represents the x-axis of frame A, starting at height cΔt on the ct axis and having a slope of v/c = aΔt/c. This dashed line intersects worldline B at a point labeled with the expression (adΔt/c) / c. The horizontal distance from the origin to this intersection point is labeled d. The vertical distance from the origin to the intersection point is labeled ct\_A. The vertical distance from the origin to the point on worldline B directly below the intersection point is labeled ct\_B. The vertical distance from the origin to the point on worldline A directly below the intersection point is labeled cΔt.

Fig. 11.70

![Figure 11.71: A Minkowski diagram showing the worldlines of two spaceships, A and B, in a frame where A is at rest. The vertical axis is ct and the horizontal axis is x. Worldline A is a vertical curve starting from the origin. Worldline B is a curve to the right of A. A dashed horizontal line segment PQ connects worldline A at point P to worldline B at point Q, with length d. A tilted axis x' is shown, and a dashed line segment PQ' is drawn along this axis from P to Q'. The length of PQ' is labeled as gamma*d.](4f4a6c5fa45611cb9ee8b5d71f716c53_img.jpg)

Figure 11.71: A Minkowski diagram showing the worldlines of two spaceships, A and B, in a frame where A is at rest. The vertical axis is ct and the horizontal axis is x. Worldline A is a vertical curve starting from the origin. Worldline B is a curve to the right of A. A dashed horizontal line segment PQ connects worldline A at point P to worldline B at point Q, with length d. A tilted axis x' is shown, and a dashed line segment PQ' is drawn along this axis from P to Q'. The length of PQ' is labeled as gamma\*d.

Fig. 11.71

- Let  $A$  be the rear spaceship, and let  $B$  be the front spaceship. From  $A$ 's point of view, it looks like  $B$  is doing exactly what he is doing (and vice versa).  $A$  says that  $B$  has the same acceleration that he has. So  $B$  should stay the same distance ahead of him. Therefore, the string shouldn't break.

The first reasoning is correct (or mostly correct; see the first remark below). The string *will* break. So that's the answer to our problem. But as with any good relativity paradox, we shouldn't feel at ease until we've explained what's wrong with the incorrect reasoning.

The problem with the second reasoning is that  $A$  does *not* see  $B$  doing exactly what he is doing. Rather, we know from Problem 11.25 that  $A$  sees  $B$ 's clock running fast (and  $B$  sees  $A$ 's clock running slow).  $A$  therefore sees  $B$ 's engine running faster, and so  $B$  pulls away from  $A$ . Therefore, the string eventually breaks.<sup>44</sup>

Things become more clear if we draw a Minkowski diagram. Figure 11.71 shows the  $x'$  and  $ct'$  axes of  $A$ 's frame. The  $x'$  axis is tilted up, so it meets  $B$ 's worldline farther to the right than you might think. The distance  $PQ$  along the  $x'$  axis is the distance that  $A$  measures the string to be. Although it isn't obvious that this distance in  $A$ 's frame is larger than  $d$  (because the unit size on the  $x'$  axis is larger than that in the original frame), we can demonstrate this as follows. In  $A$ 's frame, the distance  $PQ$  is greater than the distance  $PQ'$ . But  $PQ'$  is simply the length of something in  $A$ 's frame that has length  $d$  in the original frame. So  $PQ'$  is  $\gamma d$  in  $A$ 's frame. And since  $PQ > \gamma d > d$  in  $A$ 's frame, the string breaks.

#### REMARKS:

- There is one slight (inconsequential) flaw in the first reasoning above. There isn't one "frame of the spaceships." Their frames differ, because they measure a relative speed between themselves. Therefore, it isn't clear exactly what is meant by the "length" of the string, because it isn't clear what frame the measurement should take place in. This ambiguity, however, does not change the fact that  $A$  and  $B$  observe their separation to be (roughly)  $\gamma d$ .

If we want there to eventually be a well-defined "frame of the spaceships," we can modify the problem by stating that after a while the spaceships stop accelerating simultaneously, as measured by someone in the original inertial frame. Equivalently,  $A$  and  $B$  turn off their engines after equal proper times. What  $A$  sees is the following.  $B$  pulls away from  $A$ .  $B$  then turns off his engine. The gap continues to widen. But  $A$  continues to fire his engine until he reaches  $B$ 's speed. They then sail onward, in a common frame, keeping a constant separation (which is greater than the original separation, by a factor  $\gamma$ ).

- The main issue in this problem is that it depends on exactly how we choose to accelerate an extended object. If we accelerate a stick by pushing on the back end (or by pulling on the front end), its length will remain essentially the same in its own frame, and it will become shorter in the original frame. But if we arrange for each end (or perhaps a number of points on the stick) to speed up in such a way that they always move at the same speed with respect to the original frame, then the stick will be torn apart.
- This problem gives the key to the classic problem of the relativistic wagon wheel, which can be stated as follows (you may want to cover up the following paragraph, so you can solve the problem on your own). A wheel is spun faster

<sup>44</sup> This also follows from the Equivalence Principle and the general-relativistic time-dilation effect which we'll discuss in Chapter 14. Since  $A$  and  $B$  are accelerating, they may be considered (by the Equivalence Principle) to be in a gravitational field, with  $B$  "higher" in the field. But high clocks run fast in a gravitational field. Therefore,  $A$  sees  $B$ 's clock running fast (and  $B$  sees  $A$ 's clock running slow).

and faster, until the points on the rim move at a relativistic speed. In the lab frame, the circumference is length contracted, but the spokes aren't (because they always lie perpendicular to the direction of motion). So if the rim has length  $2\pi r$  in the lab frame, then it has length  $2\pi\gamma r$  in the wheel frame. Therefore, in the wheel frame, the ratio of the circumference to the diameter is larger than  $\pi$ . So the question is: Is this really true? And if so, how does the circumference become longer in the wheel frame?

I'm putting this sentence here just in case you happened to see the first sentence of this paragraph as you were trying to cover it up and solve the problem on your own; it should probably even be a little longer, maybe like ... this. The answer is that it is indeed true. If we imagine little rocket engines placed around the rim, and if we have them all accelerate with the same proper acceleration, then from the above results, the separation between the engines will gradually increase, thereby increasing the length of the circumference. Assuming that the material in the rim can't stretch indefinitely, the rim will eventually break between each engine. In the rotating (and hence accelerating) wheel frame, the ratio of the circumference to the diameter is indeed larger than  $\pi$ . In other words, space is curved in the wheel frame. This is consistent with the facts that (1) the Equivalence Principle (discussed in Chapter 14) states that acceleration is equivalent to gravity, and (2) gravitational fields in General Relativity are associated with curved space. ♣

#### 11.27. Successive Lorentz transformations

It isn't necessary, of course, to use matrices in this problem, but things look nicer if we do. The desired composite L.T. is obtained by multiplying the matrices for the individual L.T.'s. So we have

$$\begin{aligned} L &= \begin{pmatrix} \cosh \phi_2 & \sinh \phi_2 \\ \sinh \phi_2 & \cosh \phi_2 \end{pmatrix} \begin{pmatrix} \cosh \phi_1 & \sinh \phi_1 \\ \sinh \phi_1 & \cosh \phi_1 \end{pmatrix} \\ &= \begin{pmatrix} \cosh \phi_1 \cosh \phi_2 + \sinh \phi_1 \sinh \phi_2 & \sinh \phi_1 \cosh \phi_2 + \cosh \phi_1 \sinh \phi_2 \\ \cosh \phi_1 \sinh \phi_2 + \sinh \phi_1 \cosh \phi_2 & \sinh \phi_1 \sinh \phi_2 + \cosh \phi_1 \cosh \phi_2 \end{pmatrix} \\ &= \begin{pmatrix} \cosh(\phi_1 + \phi_2) & \sinh(\phi_1 + \phi_2) \\ \sinh(\phi_1 + \phi_2) & \cosh(\phi_1 + \phi_2) \end{pmatrix}. \end{aligned} \quad (11.138)$$

This is an L.T. with  $v = \tanh(\phi_1 + \phi_2)$ , as desired. Except for a few minus signs, this proof is just like the one for successive rotations in a plane.

#### 11.28. Accelerator's time

Equation (11.64) gives the speed as a function of the spaceship's time (which we are denoting by  $t'$  here) as

$$\beta(t') \equiv \frac{v(t')}{c} = \tanh(at'/c). \quad (11.139)$$

The person in the lab frame sees the spaceship's clock slowed down by a factor  $1/\gamma = \sqrt{1 - \beta^2}$ , which means that  $dt = dt'/\sqrt{1 - \beta^2}$ . So we have

$$t = \int_0^t dt = \int_0^{t'} \frac{dt'}{\sqrt{1 - \beta(t')^2}} = \int_0^{t'} \cosh(at'/c) dt' = \frac{c}{a} \sinh(at'/c). \quad (11.140)$$

For small  $a$  or  $t'$  (more precisely, for  $at'/c \ll 1$ ), we obtain  $t \approx t'$ , as we should. For very large times, we essentially have

$$t \approx \frac{c}{2a} e^{at'/c}, \quad \text{or} \quad t' = \frac{c}{a} \ln(2at/c). \quad (11.141)$$

The lab frame will see the astronaut read all of *Moby Dick*, but it will take an exponentially long time (not that it doesn't already).