# Chapter 14 General Relativity

This will be somewhat of a strange chapter, because we won't have enough time to get to the heart of General Relativity (GR).<sup>1</sup> But we'll still be able to get a flavor of the subject and derive a few interesting GR results. One crucial idea in GR is the Equivalence Principle. This says that gravity is equivalent to acceleration. Or in more practical terms, it says that you can't tell the difference. We'll have much to say about this in the sections below. Another crucial concept in GR is that of coordinate independence: the laws of physics can't depend on what coordinate system you choose. This seemingly innocuous statement has surprisingly far-reaching consequences. However, a discussion of this topic is one of the many things we won't have time for. We would need a whole book on GR to do it justice. But fortunately it's possible to get a sense of the nature of GR without having to master such things. This is the route we'll take in this chapter.

### 14.1 The Equivalence Principle

Einstein's Equivalence Principle says that it is impossible to locally distinguish between gravity and acceleration. This may be stated more precisely in (at least) three ways.

- Let person  $A$  be enclosed in a small box, far from any massive objects, that undergoes uniform acceleration (say,  $g$ ). Let person  $B$  stand at rest on the earth (see Fig. 14.1). The Equivalence Principle says that there are no local experiments these two people can perform that will tell them which of the two settings they are in. The physics of each setting is the same.
- Let person  $A$  be enclosed in a small box that is in free-fall near a planet. Let person  $B$  float freely in space, far away from any massive objects (see Fig. 14.2). The Equivalence Principle says that there are no local experiments these two people can perform that will tell them which of the two settings they are in. The physics of each setting is the same.

<sup>1</sup> Ten years after his 1905 paper on the Special Theory of Relativity, Einstein completed his General Theory of Relativity in 1915, collaborating with Marcel Grossmann during the latter part of this period. David Hilbert also developed many of the final pieces of the theory in parallel with Einstein; see Medicus (1984). For a wonderful account of other historical developments of the theory, see Chandrasekhar (1979).

![Diagram illustrating the Equivalence Principle. On the left, a person labeled A is inside a box that is accelerating upwards with acceleration g. On the right, a person labeled B is standing on the surface of the Earth. A vertical dashed line separates the two scenarios.](e428142cc5fb20f8abec4e641e2cd0fd_img.jpg)

The diagram shows two equivalent physical situations. On the left, a person labeled  $A$  is inside a rectangular box. An upward-pointing arrow labeled  $g$  indicates the box is accelerating upwards. On the right, a person labeled  $B$  is standing on a circle labeled 'earth'. A vertical dashed line separates the two scenarios, indicating they are locally equivalent.

Diagram illustrating the Equivalence Principle. On the left, a person labeled A is inside a box that is accelerating upwards with acceleration g. On the right, a person labeled B is standing on the surface of the Earth. A vertical dashed line separates the two scenarios.

Fig. 14.1

![Diagram illustrating the Equivalence Principle. On the left, a person labeled A is inside a box that is in free-fall, indicated by a downward-pointing arrow labeled g. On the right, a person labeled B is floating freely in space. A vertical dashed line separates the two scenarios.](c28d9161f9592bce7567791d732ac466_img.jpg)

The diagram shows two equivalent physical situations. On the left, a person labeled  $A$  is inside a rectangular box. A downward-pointing arrow labeled  $g$  indicates the box is in free-fall. On the right, a person labeled  $B$  is floating freely in space. A vertical dashed line separates the two scenarios, indicating they are locally equivalent.

Diagram illustrating the Equivalence Principle. On the left, a person labeled A is inside a box that is in free-fall, indicated by a downward-pointing arrow labeled g. On the right, a person labeled B is floating freely in space. A vertical dashed line separates the two scenarios.

Fig. 14.2

- “Gravitational” mass is equal to (or proportional to) “inertial” mass. Gravitational mass is the  $m_g$  that appears in the formula,  $F = GMm_g/r^2 \equiv m_g g$ . Inertial mass is the  $m_i$  that appears in the formula,  $F = m_i a$ . There is no a-priori reason why these two  $m$ ’s should be the same (or proportional). An object that is dropped on the earth has acceleration  $a = (m_g/m_i)g$ . For all we know, the ratio  $m_g/m_i$  for plutonium might be different from that for copper. But experiments with various materials have detected no difference in the ratios. The Equivalence Principle states that the ratios are equal for any type of mass.

This definition of the Equivalence Principle is equivalent to, say, the second one above for the following reason. Two different masses that start at rest near  $B$  will stay right where they are as they float freely in space. But two different masses that start at rest near  $A$  will stay next to each other if and only if their accelerations are equal, that is, if and only if the ratio  $m_g/m_i$  is the same for both. If this ratio is different for the two masses, then they will diverge from each other, which means that it is possible to distinguish between the two settings.

These statements are all quite believable. Consider the first one, for example. When standing on the earth, you have to keep your legs firm to avoid falling down. When standing in the accelerating box, you have to keep your legs firm to maintain the same position relative to the floor (that is, to avoid “falling down”). You certainly can’t naively tell the difference between the two scenarios. The Equivalence Principle says that it’s not just that you’re too inept to figure out a way to differentiate between them, but instead that there is no possible local experiment you can perform to tell the difference, no matter how clever you are.

REMARK: Note the inclusion of the words “small box” and “local” above. On the surface of the earth, the lines of the gravitational force are not parallel; they converge to the center. The gravitational force also varies with height. Therefore, an experiment performed over a non-negligible distance (for example, dropping two balls next to each other, and watching them converge; or dropping two balls on top of each other and watching them diverge) will have different results from the same experiment in the accelerating box. The Equivalence Principle says that if your laboratory is small enough, or if the gravitational field is sufficiently uniform, then the two scenarios look essentially the same. ♣

### 14.2 Time dilation

The Equivalence Principle has a striking consequence concerning the behavior of clocks in a gravitational field. It implies that higher clocks run faster than lower clocks. If someone puts a watch on top of a tower, and if you stand on the ground, then you will see the watch on the tower tick faster than an identical watch on your wrist. If the watch on the tower is taken down and you compare it with the one on your wrist, it will show more time elapsed.<sup>2</sup> Likewise, someone standing

<sup>2</sup> This is true only if the watch on the tower is kept there for a long enough time (assuming that the watches show the same time when you start observing), because the movement of the watch when

on top of the tower will see a clock on the ground run slow. To be quantitative about this, let's consider the following two scenarios.

- A light source on top of a tower of height  $h$  emits flashes at time intervals  $t_s$ . A receiver on the ground receives the flashes at time intervals  $t_r$  (see Fig. 14.3). What is  $t_r$  in terms of  $t_s$ ?
- A rocket of length  $h$  accelerates with acceleration  $g$ . A light source at the front end emits flashes at time intervals  $t_s$ . A receiver at the back end receives the flashes at time intervals  $t_r$  (see Fig. 14.4). What is  $t_r$  in terms of  $t_s$ ?

![Diagram of a tower of height h with a light source at the top and a receiver at the bottom.](41739c466750d499c2986a2f0e6301ba_img.jpg)

A diagram showing a tall, thin tower with a lattice structure. At the very top, there is a light source symbol (a circle with radiating lines). At the base of the tower, there is a small black rectangle representing a receiver. To the left of the tower, a vertical double-headed arrow is labeled with the letter  $h$ , indicating the height of the tower.

Diagram of a tower of height h with a light source at the top and a receiver at the bottom.

Fig. 14.3

The Equivalence Principle tells us that these two scenarios are exactly the same, as far as the sources and receivers are concerned. Hence, the relation between  $t_r$  and  $t_s$  must be the same in each. Therefore, to find out what is going on in the first scenario, we will study the second scenario (because we can figure out how this one behaves).

Consider an instantaneous inertial frame,  $S$ , of the rocket. In this frame, the rocket is momentarily at rest (at, say,  $t = 0$ ), and then it accelerates out of the frame with acceleration  $g$ . The following discussion will be made with respect to the frame  $S$ . Consider a series of quick light pulses emitted from the source, starting at  $t = 0$ . The distance the rocket has traveled out of  $S$  at time  $t$  is  $gt^2/2$ , so if we assume that  $t_s$  is very small, then we may say that many light pulses are emitted before the rocket moves appreciably. Likewise, the speed of the source, namely  $gt$ , is also very small. We may therefore ignore the motion of the rocket, as far as the light source is concerned.

![Diagram of a rocket of length h accelerating with acceleration g, with a light source at the front and a receiver at the back.](3dc9c44456eb97a629bd72073370d479_img.jpg)

A diagram showing a rocket in profile, pointing upwards. It has a rectangular body and a triangular nose cone. Inside the body, near the top (front), there is a light source symbol. Near the bottom (back), there is a small black rectangle representing a receiver. To the left of the rocket, a vertical double-headed arrow is labeled with the letter  $h$ , indicating the length of the rocket. To the right of the rocket, an upward-pointing arrow is labeled with the letter  $g$ , indicating the direction of acceleration.

Diagram of a rocket of length h accelerating with acceleration g, with a light source at the front and a receiver at the back.

Fig. 14.4

However, the light takes a finite time to reach the receiver, and by then the receiver will be moving. We therefore *cannot* ignore the motion of the rocket when dealing with the receiver. The time it takes the light to reach the receiver is  $h/c$ , at which point the receiver has a speed of  $v = g(h/c)$ .<sup>3</sup> Therefore, by the usual classical Doppler effect, the time between the received pulses is<sup>4</sup>

$$t_r = \frac{t_s}{1 + (v/c)}. \quad (14.1)$$

it is taken down causes it to run slow, due to the usual special-relativistic time dilation. But the speeding-up effect due to the height can be made arbitrarily large compared with the slowing-down effect due to the motion, by simply keeping the watch on the tower for an arbitrarily long time.

<sup>3</sup> The receiver moves a tiny bit during this time, so the “ $h$ ” here should really be replaced by a slightly smaller distance. But this yields a negligible second-order effect in the small quantity  $gh/c^2$ , as you can show. To sum up, the displacement of the source, the speed of the source, and the displacement of the receiver are all negligible. But the speed of the receiver is quite relevant.

<sup>4</sup> Quick proof of the classical Doppler effect (for a moving receiver): As seen in frame  $S$ , when the receiver and a particular pulse meet, the next pulse is a distance  $ct_s$  behind. The receiver and this next pulse then travel toward each other at relative speed  $c + v$  (as measured by someone in  $S$ ). The time difference between receptions is therefore  $t_r = ct_s/(c + v)$ .

So the frequencies,  $f_r = 1/t_r$  and  $f_s = 1/t_s$ , are related by

$$f_r = \left(1 + \frac{v}{c}\right) f_s = \left(1 + \frac{gh}{c^2}\right) f_s. \quad (14.2)$$

Returning to the clock-on-tower scenario, the Equivalence Principle tells us that an observer on the ground must see the clock on the tower running fast, by a factor  $1 + gh/c^2$ . This means that the upper clock really *is* running fast, compared with the lower clock.<sup>5</sup> That is,

$$\Delta t_h = \left(1 + \frac{gh}{c^2}\right) \Delta t_0. \quad (14.3)$$

A twin from Denver will be older than his twin from Boston when they meet up at a family reunion (all other things being equal).

Greetings! Dear brother from Boulder,  
 I hear that you've gotten much older.  
 And please tell me why  
 My lower left thigh  
 Hasn't aged quite as much as my shoulder!

Note that the  $gh$  in Eq. (14.3) is the gravitational potential energy divided by  $m$ .

REMARK: You might object to the above derivation, because  $t_r$  is the time measured by someone in the inertial frame  $S$ . And since the receiver is eventually moving with respect to  $S$ , we should multiply the  $f_r$  in Eq. (14.2) by the usual special-relativistic time-dilation factor,  $1/\sqrt{1 - (v/c)^2}$  (because the receiver's clocks are running slow relative to  $S$ , so the frequency measured by the receiver is greater than that measured in  $S$ ). However, this is a second-order effect in the small quantity  $v/c = gh/c^2$ . We already dropped other effects of the same order, so we have no right to keep this one. Of course, if the leading effect in our final answer turned out to be second order in  $v/c$ , then we would know that our answer was garbage. But the leading effect happens to be first order, so we can afford to be careless with the second-order effects. ♣

After a finite time has passed, the frame  $S$  will no longer be of any use to us. But we can always pick a new instantaneous rest frame of the rocket, so we can repeat the above analysis at any later time. Therefore, the result in Eq. (14.2) holds at all times.

This gravitational time-dilation effect was first measured by R. Pound and G. Rebka in 1960. By sending gamma rays both up and down a 22 m tower, they were able to measure the redshift (that is, the decrease in frequency) at the top. This was a notable feat indeed, considering that they were able to measure a frequency shift of  $gh/c^2$  (which is only a few parts in  $10^{15}$ ) to within 10% accuracy. In 1964, R. Pound and J. Snider improved the accuracy to 1%.

<sup>5</sup> Unlike the situation where two people fly past each other (as with the usual twin paradox), we can say here that what an observer *sees* is also what actually *is*. We can say this because everyone here is in the same frame. The “turnaround” effect that was present in the twin paradox isn't present now. The two clocks can be slowly moved together without anything exciting or drastic happening to their readings.

### 14.3 Uniformly accelerating frame

Before reading this section, you should think carefully about the “Break or not break” problem in Chapter 11 (Problem 11.26). Don’t look at the solution too soon, because chances are you will change your answer after a few more minutes of thought. This is a classic problem, so don’t waste it by peeking!

Technically, the uniformly accelerating frame we’ll construct here has nothing to do with GR. We won’t need to leave the realm of Special Relativity for the analysis in this section. But the reason we choose to study this special-relativistic setup in detail is that it shows many similarities to genuine GR situations, such as black holes.

#### 14.3.1 Uniformly accelerating point particle

In order to understand a uniformly accelerating frame, we first need to understand a uniformly accelerating point particle. In Section 11.9, we briefly discussed the motion of a uniformly accelerating particle, that is, one that feels a constant force in its instantaneous rest frame. We’ll now take a closer look at such a particle. Let the particle’s instantaneous rest frame be  $S'$ , and let it start at rest in the inertial frame  $S$ . Let its mass be  $m$ . We know from Section 12.5.3 that the longitudinal force is the same in the two frames. Therefore, since it is constant in  $S'$ , it is also constant in  $S$ . Call it  $f$ . If we let  $g \equiv f/m$  (so  $g$  is the proper acceleration felt by the particle), then in  $S$  we have, using the fact that  $f$  is constant,

$$f = \frac{dp}{dt} = \frac{d(m\gamma v)}{dt} \implies gt = \gamma v \implies v = \frac{gt}{\sqrt{1 + (gt)^2}}, \quad (14.4)$$

where we have set  $c = 1$ . As a double-check, this has the correct behavior for  $t \rightarrow 0$  and  $t \rightarrow \infty$ . If you want to keep the  $c$ ’s in, then  $(gt)^2$  becomes  $(gt/c)^2$  to make the units right. Having found the speed in  $S$  at time  $t$ , the position in  $S$  at time  $t$  is given by

$$x = \int_0^t v dt = \int_0^t \frac{gt dt}{\sqrt{1 + (gt)^2}} = \frac{1}{g} \left( \sqrt{1 + (gt)^2} - 1 \right). \quad (14.5)$$

For convenience, let  $P$  be the point (see Fig. 14.5)

$$(x_P, t_P) = (-1/g, 0). \quad (14.6)$$

Then Eq. (14.5) yields

$$(x - x_P)^2 - t^2 = \frac{1}{g^2}. \quad (14.7)$$

This is the equation for a hyperbola with its center (defined as the intersection of the asymptotes) at point  $P$ . For a large acceleration  $g$ , the point  $P$  is very close to the particle’s starting point. For a small acceleration, it is far away.

![Figure 14.5: A spacetime diagram showing the worldline of a uniformly accelerating point particle. The vertical axis is time t and the horizontal axis is position x. A hyperbola represents the particle's worldline, starting from point A on the t-axis. The hyperbola has asymptotes that intersect at point P on the x-axis. The distance from the origin to P is labeled 1/g. A dashed line represents the worldline of the particle's instantaneous rest frame S'.](d1245223c828f06fb94a0cf664f9dcdb_img.jpg)

The figure is a spacetime diagram with a vertical axis labeled  $t$  and a horizontal axis labeled  $x$ . A solid curve, labeled 'hyperbola', represents the worldline of a uniformly accelerating particle. This curve starts at a point  $A$  on the  $t$ -axis and curves upwards and to the right. Two dashed lines, labeled 'asymptote', represent the asymptotes of the hyperbola; they intersect at a point  $P$  on the  $x$ -axis. The distance from the origin to point  $P$  is marked as  $1/g$ . A solid line labeled  $x'$  represents the worldline of the particle's instantaneous rest frame  $S'$ , which is a straight line passing through point  $A$  and parallel to the  $x'$ -axis of the  $S'$  frame.

Figure 14.5: A spacetime diagram showing the worldline of a uniformly accelerating point particle. The vertical axis is time t and the horizontal axis is position x. A hyperbola represents the particle's worldline, starting from point A on the t-axis. The hyperbola has asymptotes that intersect at point P on the x-axis. The distance from the origin to P is labeled 1/g. A dashed line represents the worldline of the particle's instantaneous rest frame S'.

Fig. 14.5

Everything has been fairly normal up to this point, but now the fun begins. Consider a point  $A$  on the particle's hyperbolic worldline at time  $t$ . From Eq. (14.5),  $A$  has coordinates

$$(x_A, t_A) = \left( \frac{1}{g} \left( \sqrt{1 + (gt)^2} - 1 \right), t \right). \quad (14.8)$$

The slope of the line  $PA$  is therefore

$$\frac{t_A - t_P}{x_A - x_P} = \frac{gt}{\sqrt{1 + (gt)^2}}. \quad (14.9)$$

Looking at Eq. (14.4), we see that this slope equals the speed  $v$  of the particle at point  $A$ . But we know very well that the speed  $v$  is the slope of the particle's instantaneous  $x'$  axis; see Eq. (11.47). Therefore, the line  $PA$  and the particle's  $x'$  axis are the same line. This holds for any arbitrary time  $t$ . So we may say that at any point along the particle's worldline, the line  $PA$  is the instantaneous  $x'$  axis of the particle. Or, said another way, no matter where the particle is, the event at  $P$  is simultaneous with an event located at the particle, as measured in the instantaneous frame of the particle. In other words, the particle always says that  $P$  happens “now.”<sup>6</sup>

Here is another strange fact. What is the distance from  $P$  to  $A$ , as measured in an instantaneous rest frame,  $S'$ , of the particle? The  $\gamma$  factor between frames  $S$  and  $S'$  is, using Eq. (14.4),  $\gamma = \sqrt{1 + (gt)^2}$ . The distance between  $P$  and  $A$  in frame  $S$  is  $x_A - x_P = \sqrt{1 + (gt)^2} / g$ . So the distance between  $P$  and  $A$  in frame  $S'$  is (using the Lorentz transformation  $\Delta x = \gamma(\Delta x' + v\Delta t')$ , with  $\Delta t' = 0$ )

$$x'_A - x'_P = \frac{1}{\gamma}(x_A - x_P) = \frac{1}{g}. \quad (14.10)$$

This has the unexpected property of being independent of  $t$ . Therefore, not only do we find that  $P$  is always simultaneous with the particle, as measured in the particle's instantaneous rest frame; we also find that  $P$  is always the same distance (namely  $1/g$ ) away from the particle, in the particle's frame. This is rather strange. The particle accelerates away from point  $P$ , but it doesn't get farther away from it, as measured in its own frame.

**REMARK:** We can give a continuity argument that shows that such a point  $P$  must exist. If a point is close to you, and if you accelerate away from it, then of course you get farther away from it. Everyday experience is quite valid here. But if a point is sufficiently far away from you, and if you accelerate away from it, then the  $at^2/2$  distance you travel away from it can easily be compensated by the decrease in distance due to length contraction (brought about by your newly acquired velocity). This effect grows with distance, so we simply need to pick the

<sup>6</sup> The point  $P$  is very much like the event horizon of a black hole. Time seems to stand still at  $P$  in this treatment. And if we went more deeply into GR, we would find that time seems to stand still at the edge of a black hole, too (as viewed by someone far away).

point to be sufficiently far away. What this means is that every time you get out of your chair and walk to the door, there are stars very far away behind you that get closer to you as you walk away from them (as measured in your instantaneous rest frame). By continuity, then, there must exist a point  $P$  that remains the same distance from you (in your frame) as you accelerate away from it. ♣

#### 14.3.2 Uniformly accelerating frame

Let's now put a collection of uniformly accelerating particles together to make a uniformly accelerating frame. Our goal will be to create a frame in which the distances between particles (as measured in any particle's instantaneous rest frame) remain constant. Why is this our goal? We know from the "Break or not break" problem in Chapter 11 that if all the particles accelerate with the same proper acceleration,  $g$ , then the distances (as measured in a particle's instantaneous rest frame) grow larger. While this is a perfectly possible frame to construct, it is not desirable, for the following reason. Einstein's Equivalence Principle states that an accelerating frame is equivalent to a frame sitting on, say, the earth. We can therefore study the effects of gravity by studying an accelerating frame. But if we want this frame to look anything like the surface of the earth, we certainly can't have distances that change over time. We therefore want to construct a *static* frame, that is, one in which distances do not change (as measured in the frame). This will allow us to say that if we enclose the frame in a windowless box, then for all a person inside knows, he is standing motionless in a static gravitational field (which has a certain definite form, as we shall see).

Let's figure out how to construct the frame. We'll discuss the acceleration of just two particles here. Others can be added in a similar manner. In the end, the desired frame as a whole is constructed by accelerating each atom in the floor of the frame with a specific proper acceleration. From Section 14.3.1, we already have a particle  $A$  that is "centered" around the point  $P$ . (This will be our shorthand notation for "traveling along a branch of a hyperbola whose center is the point  $P$ .") We claim, for reasons that will become clear, that every other particle in the frame should also be "centered" around the same point  $P$ .

Consider another particle,  $B$ . Let  $a$  and  $b$  be the initial distances from  $P$  to  $A$  and  $B$ . If both particles are to be centered around  $P$ , then their proper accelerations must be, from Eq. (14.6),

$$g_A = \frac{1}{a}, \quad \text{and} \quad g_B = \frac{1}{b}. \quad (14.11)$$

Therefore, in order to have all points in the frame be centered around  $P$ , we simply have to make their proper accelerations inversely proportional to their initial distances from  $P$ .

Why do we want every particle to be centered around  $P$ ? Consider two events,  $E_A$  and  $E_B$ , such that  $P$ ,  $E_A$ , and  $E_B$  are collinear in Fig. 14.6. From Section 14.3.1, we know that the line  $PE_AE_B$  is the  $x'$  axis for both particle

![Figure 14.6: A spacetime diagram showing the worldlines of two particles, A and B, in a uniformly accelerating frame. The vertical axis is time (t) and the horizontal axis is position (x). A dashed line represents the worldline of particle A, and a solid line represents the worldline of particle B. Both worldlines are hyperbolas centered at point P on the x-axis. The initial distance from P to A is labeled 'a', and the initial distance from P to B is labeled 'b'. A solid line labeled x' passes through P, E_A, and E_B, representing the x' axis for both particles. The events E_A and E_B are marked on the worldlines of A and B respectively, and they lie on the x' axis.](60387fd27e4f258c4d4bac592e3db1af_img.jpg)

Figure 14.6: A spacetime diagram showing the worldlines of two particles, A and B, in a uniformly accelerating frame. The vertical axis is time (t) and the horizontal axis is position (x). A dashed line represents the worldline of particle A, and a solid line represents the worldline of particle B. Both worldlines are hyperbolas centered at point P on the x-axis. The initial distance from P to A is labeled 'a', and the initial distance from P to B is labeled 'b'. A solid line labeled x' passes through P, E\_A, and E\_B, representing the x' axis for both particles. The events E\_A and E\_B are marked on the worldlines of A and B respectively, and they lie on the x' axis.

Fig. 14.6

$A$  and particle  $B$ , at the positions shown. We also know that  $A$  is always a distance  $a$  from  $P$ , and  $B$  is always a distance  $b$  from  $P$  (in their frame). Combining these facts with the fact that  $A$  and  $B$  measure their distances along the  $x'$  axis of the same frame (at the events shown in the figure), we see that both  $A$  and  $B$  measure the distance between them to be  $b - a$ . This is independent of  $t$ , so  $A$  and  $B$  measure a constant distance between them. We have therefore constructed our desired static frame. This frame is often called a “Rindler space.” If a person walks around in the frame, he will think that he lives in a static world where the acceleration due to gravity takes the form  $g(z) \propto 1/z$ , where  $z$  is the distance to a certain magical point which is located at the end of the known “universe.”

What if a person releases himself from the accelerating frame, so that he forever sails through space at constant speed? His view is that he is falling. He falls past the “magical point”  $P$  in a finite proper time, because the hyperbolic worldline of a point infinitesimally close to  $P$  is essentially the asymptote of all the hyperbolas, and the person’s straight-line worldline intersects this line. But his friends who are still in the frame will see him take an infinitely long time to get to  $P$ , because the  $x'$  axes of points in the frame never quite swing up to the asymptote, even after an infinite amount of time. So the “now” line of any point in the frame never quite passes through the event where the person crosses the asymptote. This is similar to the situation with a black hole. An outside observer will see it take an infinitely long time for a falling person to reach the “boundary” of a black hole, even though it takes a finite proper time for the person.

Our analysis shows that  $A$  and  $B$  feel different proper accelerations, because  $a \neq b$ . There is no way to construct a static frame where all points feel the same proper acceleration, so it is impossible to mimic a constant gravitational field (over a finite distance) by using an accelerating frame. The problems and exercises for this chapter offer plenty of opportunity for you to play around with the properties of our uniformly accelerating frame.

### 14.4 Maximal-proper-time principle

The maximal-proper-time principle in General Relativity says: Given two events in spacetime, a particle under the influence of only gravity takes the path in spacetime that maximizes the proper time. For example, if you throw a ball from given coordinates  $(\mathbf{r}_1, t_1)$ , and it lands at given coordinates  $(\mathbf{r}_2, t_2)$ , then the claim is that the ball takes the path that maximizes its proper time.<sup>7</sup>

This is clear for a freely moving ball in outer space, far from any massive objects. The ball travels at constant speed from one point to another, and we

<sup>7</sup> The principle is actually the “stationary-proper-time principle,” because as with the Lagrangian formalism in Chapter 6, any type of stationary point (a maximum, minimum, or saddle point) is allowed. But although we were very careful about stating things properly in Chapter 6, we’ll be a little sloppy here and just use the word “maximum,” because that’s what it will generally turn out to be in the situations we’ll look at. However, see Problem 14.8.

know that this constant-speed motion is the motion with the maximal proper time. This is true because a ball,  $A$ , moving at constant speed sees the clock on any other ball,  $B$ , running slow due to the special-relativistic time dilation, if there is a relative speed between them. (We're assuming that  $B$ 's nonuniform velocity is caused by a nongravitational force acting on it.)  $B$  therefore shows a shorter elapsed time. This argument doesn't work the other way around, because  $B$  isn't in an inertial frame and therefore can't use the special-relativistic time-dilation result.

### *Consistency with Newtonian physics*

The maximal-proper-time principle sounds like a plausible idea, but we already know from Chapter 6 that the path an object takes is the one that yields a stationary value of the classical action,  $\int (T - V)$ . We must therefore demonstrate that the maximal-proper-time principle reduces to the stationary-action principle, in the limit of small velocities. If this weren't the case, then we'd have to throw out the maximal-proper-time principle.

Consider a ball thrown vertically on the earth. Assume that the initial and final coordinates are fixed to be  $(y_1, t_1)$  and  $(y_2, t_2)$ . Our plan will be to assume that the maximal-proper-time principle holds, and to then show that this leads to the stationary-action principle. Before being quantitative, let's get a qualitative idea about what's going on with the ball. There are two competing effects, as far as maximizing the proper time goes. On one hand, the ball wants to climb very high, because its clock will run faster there, due to the GR time dilation. But on the other hand, if it climbs very high, then it must move very fast to get there (because the total time,  $t_2 - t_1$ , is fixed), and this will make its clock run slow, due to the SR time dilation. So there's a tradeoff. Let's now look quantitatively at the implications of this tradeoff. The goal is to maximize

$$\tau = \int_{t_1}^{t_2} d\tau. \quad (14.12)$$

Due to the motion of the ball, we have the usual time dilation,  $d\tau = \sqrt{1 - v^2/c^2} dt$ . But due to the height of the ball, we also have the gravitational time dilation,  $d\tau = (1 + gy/c^2) dt$ . Combining these effects gives<sup>8</sup>

$$d\tau = \sqrt{1 - \frac{v^2}{c^2}} \left(1 + \frac{gy}{c^2}\right) dt. \quad (14.13)$$

<sup>8</sup> This result is technically incorrect, because the two effects are intertwined in a somewhat more complicated manner (see Exercise 14.20). But it's valid up to first order in  $v^2/c^2$  and  $gy/c^2$ , which is all we're concerned with here.

Using the Taylor expansion for  $\sqrt{1 - \epsilon}$ , and dropping terms of order  $1/c^4$  and smaller, we see that we want to maximize

$$\int_{t_1}^{t_2} d\tau \approx \int_{t_1}^{t_2} \left(1 - \frac{v^2}{2c^2}\right) \left(1 + \frac{gy}{c^2}\right) dt \approx \int_{t_1}^{t_2} \left(1 - \frac{v^2}{2c^2} + \frac{gy}{c^2}\right) dt. \quad (14.14)$$

The “1” term gives a constant, so maximizing this integral is equivalent to minimizing

$$mc^2 \int_{t_1}^{t_2} \left(\frac{v^2}{2c^2} - \frac{gy}{c^2}\right) dt = \int_{t_1}^{t_2} \left(\frac{mv^2}{2} - mgy\right) dt, \quad (14.15)$$

which is the classical action, as desired. For a one-dimensional gravitational problem such as this one, the action is always a (global) minimum, and the proper time is always a (global) maximum, as you can show by considering the second-order change in the action (see Exercise 14.23, which is the same as Exercise 6.32).

In retrospect, it isn’t surprising that the kinetic energy here works out. The factor of  $1/2$  comes about in exactly the same way as in the derivation in Eq. (12.9), where we showed that the relativistic form of energy reduces to the familiar Newtonian expression. As far as the potential energy goes, the  $gy$  here can be traced to the acceleration times a certain time, where this time is proportional to the distance; see the paragraph before Eq. (14.1). This yields (when multiplied by  $mc^2$ ) the usual force times distance expression for the potential.

The maximal-proper-time principle here is equivalent to the statement that the action for the Lagrangian we introduced near the end of Section 12.1 is  $S = -mc \int d\tau$ . In both cases we want to extremize the integral of the proper time. In Section 12.1 we dealt only with a free particle, so the treatment here is a little more general because it includes the effect of gravity. But note that although Eq. (14.15) has the obvious interpretation of including the gravitational potential, the starting point in Eq. (14.12) makes no mention of a gravitational force. In the present treatment, gravity shouldn’t be thought of as a force, but instead as something that affects the proper time.<sup>9</sup>

### 14.5 Twin paradox revisited

Let’s take another look at the standard twin paradox, this time from the perspective of General Relativity. We should emphasize that GR is by no means necessary for an understanding of the original formulation of the paradox (the first scenario below). We were able to solve it in Section 11.3.2, after all. The present discussion is given simply to show that the answer to an alternative formulation (the second

<sup>9</sup> For an interesting article on how the classical action, along with a few ingredients from differential geometry, can lead to General Relativity, see Rindler (1994).

scenario below) is consistent with what we've learned about GR. Consider the two following twin-paradox setups.

- Twin  $A$  floats freely in outer space. Twin  $B$  flies past  $A$  in a spaceship, with speed  $v_0$  (see Fig. 14.7). At the instant they are next to each other, they both set their clocks to zero. At this same instant,  $B$  turns on the reverse thrusters of his spaceship and decelerates with proper deceleration  $g$ .  $B$  eventually reaches a farthest point from  $A$  and then accelerates back toward  $A$ , finally passing him with speed  $v_0$  again. When they are next to each other, they compare the readings on their clocks. Which twin is younger?
- Twin  $B$  stands on the earth. Twin  $A$  is thrown upward with speed  $v_0$  (let's say he is fired from a cannon in a hole in the ground; see Fig. 14.8). At the instant they are next to each other, they both set their clocks to zero.  $A$  rises up and then falls back down, finally passing  $B$  with speed  $v_0$  again. When they are next to each other, they compare the readings on their clocks. Which twin is younger?

The first scenario is easily solved using Special Relativity. Since  $A$  is in an inertial frame, he can apply the results of Special Relativity. In particular, he sees  $B$ 's clock run slow, due to the usual special-relativistic time dilation. Therefore,  $B$  ends up younger at the end.  $B$  cannot use the reverse reasoning, because she is not in an inertial frame.

What about the second scenario? The key point to realize is that the Equivalence Principle says that these two scenarios are exactly the same (ignoring the nonuniformity of the earth's gravitational force), as far as the twins are concerned. Twin  $B$  has no way of knowing whether she is in a spaceship accelerating at  $g$  or on the surface of the earth. And  $A$  has no way of knowing whether he is floating freely in outer space or in free-fall in a gravitational field.<sup>10</sup> We therefore conclude that  $B$  must be younger in the second scenario, too.

At first glance, this seems incorrect, because in the second scenario,  $B$  is sitting motionless while  $A$  is the one who is moving. It seems that  $B$  should see  $A$ 's clock running slow, due to the usual special-relativistic time dilation, and hence  $A$  should be younger. This reasoning is incorrect because it fails to take into account the gravitational time dilation. The fact of the matter is that  $A$  is higher in the gravitational field, and therefore his clock runs faster. This effect does indeed win out over the special-relativistic time dilation, and  $A$  ends up older. You can explicitly show this in Problem 14.11.

The reasoning in this section yields another way to conclude that the Equivalence Principle implies that higher clocks must run faster (in one way or another). The Equivalence Principle implies that  $A$  must be older in the second scenario, which means that there must be some height effect that makes  $A$ 's clock run

![Diagram for Fig. 14.7: Twin A is represented by a dot. Twin B is in a spaceship, represented by a rectangle with a right-pointing arrow, moving with velocity v_0. Dashed lines show B's path moving away from A and then returning towards A.](c5d3b3125df3c03bdb4e779886b07c04_img.jpg)

Diagram for Fig. 14.7: Twin A is represented by a dot. Twin B is in a spaceship, represented by a rectangle with a right-pointing arrow, moving with velocity v\_0. Dashed lines show B's path moving away from A and then returning towards A.

Fig. 14.7

![Diagram for Fig. 14.8: Twin B is on the surface of the earth, represented by a curved line. Twin A is thrown upward from a point on the earth's surface with an initial velocity v_0. A dashed vertical line with arrows indicates A's path going up and then falling back down to the earth.](2b09278c843346ca5c8114081071ea34_img.jpg)

Diagram for Fig. 14.8: Twin B is on the surface of the earth, represented by a curved line. Twin A is thrown upward from a point on the earth's surface with an initial velocity v\_0. A dashed vertical line with arrows indicates A's path going up and then falling back down to the earth.

Fig. 14.8

<sup>10</sup> As mentioned in Section 14.1, this fact is made possible by the equivalence of inertial and gravitational mass. Were it not for this, different parts of  $A$ 's body would want to accelerate at different rates in the gravitational field in the second scenario. This would certainly clue him in to the fact that he wasn't floating freely in space.

fast (fast enough to win out over the special-relativistic time dilation). But it takes some more work to show that the factor is actually  $1 + gh/c^2$ . Note that the fact that  $A$  is older is consistent with the maximal-proper-time principle. In both scenarios,  $A$  is under the influence of only gravity (zero gravity in the first scenario), whereas  $B$  feels a normal force from either the spaceship's floor or the ground.

### 14.6 Problems

### Section 14.2: Time dilation

### 14.1. Airplane's speed \*

A plane flies at constant height  $h$ . What should its speed be so that an observer on the ground sees the plane's clock tick at the same rate as a ground clock? (Assume  $v \ll c$ .)

### 14.2. Clock on a tower \*\*

A clock starts on the ground and then moves up a tower at constant speed  $v$ . It sits on top of the tower for a time  $T$  and then descends at constant speed  $v$ . If the tower has height  $h$ , how long should the clock sit at the top so that it comes back showing the same time as a clock that remained on the ground? (Assume  $v \ll c$ .)

### 14.3. Circular motion \*\*

$B$  moves at speed  $v$  (with  $v \ll c$ ) in a circle of radius  $r$  around  $A$ , far from any masses. By what fraction does  $B$ 's clock run slower than  $A$ 's? Calculate this in three ways. Work in:

- $A$ 's frame.
- The frame whose origin is  $B$  and whose axes remain parallel to an inertial set of axes.
- The rotating frame that is centered at  $A$  and rotates with the same frequency as  $B$ .

### 14.4. More circular motion \*\*

$A$  and  $B$  move at speed  $v$  ( $v \ll c$ ) in a circle of radius  $r$ , at diametrically opposite points, far from any masses. They both see their clocks ticking at the same rate. Show this in three ways. Work in:

- The lab frame (the inertial frame whose origin is the center of the circle).
- The frame whose origin is  $B$  and whose axes remain parallel to an inertial set of axes.
- The rotating frame that is centered at the origin and rotates with the same frequency as  $A$  and  $B$ .

### *Section 14.3: Uniformly accelerating frame*

### **14.5. Accelerator's point of view \*\*\***

A rocket starts at rest relative to a planet, a distance  $\ell$  away. It accelerates toward the planet with proper acceleration  $g$ . Let  $\tau$  and  $t$  be the readings on the rocket's and planet's clocks, respectively.

- (a) Show that when the astronaut's clock reads  $\tau$ , he observes the rocket–planet distance  $x$  (as measured in his instantaneous inertial frame) to be given by

$$1 + gx = \frac{1 + g\ell}{\cosh(g\tau)}. \quad (14.16)$$

- (b) Show that when the astronaut's clock reads  $\tau$ , he observes the time  $t$  on the planet's clock to be given by

$$gt = (1 + g\ell) \tanh(g\tau). \quad (14.17)$$

The results from Exercises 14.16 and 14.20 will be useful here.

### **14.6. Getting way ahead \*\*\*\***

A rocket with proper length  $L$  accelerates from rest, with proper acceleration  $g$  (where  $gL \ll c^2$ ). Clocks are located at the front and back of the rocket. If we look at this setup in the rocket frame, then the GR time-dilation effect tells us that the times on the two clocks are related by  $t_f = (1 + gL/c^2)t_b$ . Therefore, if we look at things in the ground frame, then the times on the two clocks are related by

$$t_f = t_b \left( 1 + \frac{gL}{c^2} \right) - \frac{Lv}{c^2}, \quad (14.18)$$

where the last term comes from the SR “rear clock ahead” result. Derive the above relation by working entirely in the ground frame.<sup>11</sup>

### **14.7. $Lv/c^2$ revisited \*\***

You stand at rest relative to a rocket that has synchronized clocks at its ends. It is then arranged for you and the rocket to move with relative speed  $v$ . A reasonable question to ask is: As viewed by you, what is the difference in readings on the clocks located at the ends of the rocket?

<sup>11</sup> You might find this relation surprising, because it implies that the front clock will eventually be an arbitrarily large time ahead of the back clock, in the ground frame. (The subtractive  $Lv/c^2$  term is bounded by  $L/c$  and will therefore eventually become negligible compared with the additive, and unbounded,  $(gL/c^2)t_b$  term.) But both clocks seem to be doing basically the same thing relative to the ground frame, so how can they end up differing by so much? Your job is to find out.

It turns out that this question cannot be answered without further information on how you and the rocket got to be moving with relative speed  $v$ . There are two basic ways this relative speed can come about. The rocket can accelerate while you sit there, or you can accelerate while the rocket sits there. Using the results from Problems 14.5 and 14.6, explain what the answers to the above question are in these two cases.

### *Section 14.4: Maximal-proper-time principle*

### 14.8. **Circling the earth** \*\*

Clock  $A$  sits at rest on the earth, and clock  $B$  circles the earth in an orbit that skims along the ground. Both  $A$  and  $B$  are essentially at the same radius, so the GR time-dilation effect yields no difference in their times. But  $B$  is moving relative to  $A$ , so  $A$  sees  $B$  running slow, due to the usual SR time-dilation effect. The orbiting clock,  $B$ , therefore shows a *smaller* elapsed proper time each time it passes  $A$ . In other words, the clock under the influence of only gravity ( $B$ ) does *not* show the maximal proper time, in conflict with what we have been calling the maximal-proper-time principle. Explain.

### *Section 14.5: Twin paradox revisited*

### 14.9. **Twin paradox** \*

A spaceship travels at speed  $v$  ( $v \ll c$ ) to a distant star. Upon reaching the star, it decelerates and then accelerates back up to speed  $v$  in the opposite direction (uniformly, and in a short time compared with the total journey time). By what fraction does the traveler age less than her twin on the earth? (Ignore the gravity from the earth.) Work in:

- (a) The earth frame.
- (b) The spaceship frame.

### 14.10. **Twin paradox again** \*\*

- (a) Answer part (b) of the previous problem, except now let the spaceship turn around by moving in a small semicircle while maintaining speed  $v$ .
- (b) Answer part (b) of the previous problem, except now let the spaceship turn around by moving in an arbitrary manner. The only constraints are that the turnaround is done quickly (compared with the total journey time) and that it is contained in a small region of space (compared with the earth–star distance).

### **14.11. Twin paradox times \*\*\***

- (a) In the first scenario in Section 14.5, calculate the ratio of  $B$ 's elapsed time to  $A$ 's, in terms of  $v_0$  and  $g$ . Work in  $A$ 's frame. Assume  $v_0 \ll c$ , and drop high-order terms.
- (b) Do the same for the second scenario in Section 14.5. Do this from scratch using the time dilations, and then check that your answer agrees (within the accuracy of the calculations) with part (a), as the Equivalence Principle demands. Work in  $B$ 's frame.

### **14.7 Exercises**

### *Section 14.2: Time dilation*

#### **14.12. Driving on a hill \***

You drive up and down a hill of height  $h$  at constant speed. The hill is in the shape of an isosceles triangle with altitude  $h$ . What should your speed be so that you age the same amount as someone standing at the base of the hill? (Assume  $v \ll c$ .)

### **14.13. $Lv/c^2$ and $gh/c^2$ \***

The familiar special-relativistic “rear clock ahead” result,  $Lv/c^2$ , looks rather similar to the  $gh/c^2$  term in the GR time-dilation result, Eq. (14.3). Imagine standing on the ground near the front of a train of length  $L$ . For small  $v$ , devise a thought experiment that explains how the  $Lv/c^2$  result follows from the  $gh/c^2$  result.

### **14.14. Both points of view \*\***

$A$  and  $B$  are initially a distance  $L$  apart, at rest with respect to each other. At a given time,  $B$  accelerates toward  $A$  with constant proper acceleration  $a$ . Assume  $aL \ll c^2$ .

- (a) Working in  $A$ 's frame, calculate the difference in readings on  $A$ 's and  $B$ 's clocks when  $B$  reaches  $A$ .
- (b) Do the same by working in  $B$ 's frame, and show that the result agrees (neglecting higher-order effects) with the result from part (a).

### **14.15. Opposite circular motion \*\*\*\***

$A$  and  $B$  move at speed  $v$  ( $v \ll c$ ) in opposite directions around a circle of radius  $r$  (so they pass each other after each half-revolution), far from any masses. They both see their two clocks ticking, on average, at the same rate. That is, if they compare their clocks each time they pass

each other, both clocks show the same time elapsed. Demonstrate this in three ways. Work in:

- (a) The lab frame (the inertial frame whose origin is the center of the circle).
- (b) The frame whose origin is  $B$  and whose axes remain parallel to an inertial set of axes.
- (c) The rotating frame that is centered at the origin and rotates along with  $B$ . This part is very tricky; the solution is given in Cranor *et al.* (2000), but don't peek too soon.

### Section 14.3: Uniformly accelerating frame

### 14.16. Various quantities \*

A particle starts at rest and accelerates with proper acceleration  $g$ . Let  $\tau$  be the time on the particle's clock. Starting with the  $v$  from Eq. (14.4), use time dilation to show that the time  $t$  in the original inertial frame, the speed of the particle, and the associated  $\gamma$  factor are given by (with  $c = 1$ )

$$gt = \sinh(g\tau), \quad v = \tanh(g\tau), \quad \gamma = \cosh(g\tau). \quad (14.19)$$

### 14.17. Using rapidity \*

Another way to derive the  $v$  in Eq. (14.4) is to use the  $v = \tanh(g\tau)$  rapidity result (where  $\tau$  is the particle's proper time) from Section 11.9. Use time dilation to show that this implies  $gt = \sinh(g\tau)$ , which then implies Eq. (14.4).

### 14.18. Speed in an accelerating frame \*

In the setup in Problem 14.5, use Eq. (14.16) to find the speed of the planet in the rocket's accelerating frame,  $|dx/d\tau|$ , as a function of  $\tau$ . What is the maximum value of this speed, in terms of  $g$  and the initial distance  $\ell$ ?

### 14.19. Redshift, blueshift \*\*

We found in Section 14.2 that a clock at the rear of a rocket sees a clock at the front run fast by a factor  $1 + gh/c^2$ . However, we ignored higher-order effects in  $1/c^2$ , so for all we know, we found only the first term in the Taylor series, and the factor is actually something like  $e^{gh/c^2}$  or perhaps  $1 + \ln(1 + gh/c^2)$ .

- (a) For the uniformly accelerating frame in Section 14.3.2, show that the factor is in fact exactly  $1 + g_r h/c^2$ , where  $g_r$  is the acceleration of the rear of the rocket. Show this by lining up a series of clocks and looking at the successive factors between them. (*Hint: Take the log of the product of the factors.*) The

overall factor takes a very nice form when written in terms of the  $a$  and  $b$  in Fig. 14.6; what is it?

- (b) By the same reasoning as in part (a), it follows that the front clock sees the rear clock run slow by a factor  $1 - g_f h/c^2$ , where  $g_f$  is the acceleration of the front. Show explicitly that  $(1 + g_r h/c^2)(1 - g_f h/c^2) = 1$ , as must be the case, because a clock can't gain time with respect to itself (and because the two clocks are at rest in the frame of the rocket; this reasoning wouldn't apply to two clocks flying past each other).

### 14.20. Gravity and speed combined \*\*

In the spirit of Problem 11.25 (“Acceleration and redshift”), use a Minkowski diagram to solve this problem. A rocket accelerates with proper acceleration  $g$  toward a planet. As measured in the instantaneous inertial frame of the rocket, the planet is a distance  $x$  away and moves at speed  $v$ . Everything is in one dimension here. As measured in the *accelerating* frame of the rocket, show that the planet's clock runs at a rate (with  $c = 1$ ),

$$dt_p = dt_r (1 + gx) \sqrt{1 - v^2}, \quad (14.20)$$

and show that the planet's speed is

$$V = (1 + gx)v. \quad (14.21)$$

Note that if we combine these two results and eliminate  $v$ , and if we then invoke the Equivalence Principle, we arrive at the result that a clock moving at speed  $V$  at height  $h$  in a gravitational field is seen by someone on the ground to run at a rate (putting the  $c$ 's back in),

$$\sqrt{\left(1 + \frac{gh}{c^2}\right)^2 - \frac{V^2}{c^2}}. \quad (14.22)$$

### 14.21. Length contraction \*\*

A pencil points directly at you. From some distance away from it, you start at rest and accelerate toward it with acceleration  $a$ . After a time  $t$ , the pencil is length contracted in your frame by a factor  $\sqrt{1 - v^2/c^2} \approx 1 - (at)^2/2c^2$ , for small  $t$  (more precisely, for  $at \ll c$ ). But the only way the pencil can shrink is for the back to move faster than the front, as measured by you in your accelerating frame. Using Eq. (14.21), show that the contraction factor works out as it should, for small  $t$ .

#### 14.22. Accelerating stick's length \*\*

Consider a uniformly accelerating frame consisting of a stick, the ends of which have worldlines given by the curves in Fig. 14.6 (so the stick

has proper length  $b - a$ ). At time  $t$  in the lab frame, we know from Eqs. (14.5) and (14.6) that a point that undergoes acceleration  $g$  has position  $\sqrt{1 + (gt)^2}/g$  relative to the point  $P$  in Fig. 14.6. An observer in the original inertial frame sees the stick being length contracted by different factors along its length, because different points move with different speeds (at a given time in the original frame). Show, by doing the appropriate integral, that the inertial observer concludes that the stick always has proper length  $b - a$ .

### Section 14.4: Maximal-proper-time principle

#### 14.23. Maximum proper time \*

Show that the stationary value of the gravitational action in Eq. (14.15) is always a minimum (which means that the proper time is always a maximum). Do this by considering a function,  $y(t) = y_0(t) + \xi(t)$ , where  $y_0$  is the path that yields the stationary value, and  $\xi$  is a small variation.

### Section 14.5: Twin paradox revisited

#### 14.24. Symmetric twin nonparadox \*\*

Two twins travel toward each other, both at speed  $v$  ( $v \ll c$ ) with respect to an inertial observer. They synchronize their clocks when they pass each other. They travel to stars located at positions  $\pm \ell$ , and then decelerate and accelerate back up to speed  $v$  in the opposite direction (uniformly, and in a short time compared with the total journey time). In the frame of the inertial observer, it is clear (by symmetry) that both twins age the same amount by the time they pass each other again. Reproduce this result by working in the frame of one of the twins.

### 14.8 Solutions

#### 14.1. Airplane's speed

An observer on the ground sees the plane's clock run slow by a factor  $\sqrt{1 - v^2/c^2}$  due to SR time dilation. But he also sees it run fast by a factor  $(1 + gh/c^2)$  due to GR time dilation. We therefore want the product of these two factors to equal 1. Using the standard Taylor-series approximation for slow speeds in the first factor, we find

$$\left(1 - \frac{v^2}{2c^2}\right) \left(1 + \frac{gh}{c^2}\right) = 1 \implies 1 - \frac{v^2}{2c^2} + \frac{gh}{c^2} - \mathcal{O}\left(\frac{1}{c^4}\right) = 1. \quad (14.23)$$

Neglecting the small  $1/c^4$  term, and canceling the 1's, we obtain  $v = \sqrt{2gh}$ . Interestingly,  $\sqrt{2gh}$  is also the answer to a standard question from Newtonian physics, namely, how fast do you need to throw a ball straight up so that it reaches a height  $h$ ?

#### 14.2. Clock on a tower

The SR time-dilation factor is  $\sqrt{1 - v^2/c^2} \approx 1 - v^2/2c^2$ . The clock therefore loses a fraction  $v^2/2c^2$  of the time elapsed during its motion up and down the tower. The

upward journey takes a time  $h/v$ , and likewise for the downward trip, so the time loss due to the SR effect is

$$\left(\frac{v^2}{2c^2}\right) \left(\frac{2h}{v}\right) = \frac{vh}{c^2}. \quad (14.24)$$

Our goal is to balance this time loss with the time gain due to the GR time-dilation effect. If the clock sits on top of the tower for a time  $T$ , then the time gain is  $(gh/c^2)T$ .

But we must not forget the increase in time due to the height gained while the clock is in motion. During its motion, the clock's average height is  $h/2$ . The total time in motion is  $2h/v$ , so the GR time gain while the clock is moving is (we can use the average height here, because the GR effect is linear in  $h$ )

$$\left(\frac{g(h/2)}{c^2}\right) \left(\frac{2h}{v}\right) = \frac{gh^2}{c^2v}. \quad (14.25)$$

Setting the total change in the clock's time equal to zero gives

$$-\frac{vh}{c^2} + \frac{gh}{c^2}T + \frac{gh^2}{c^2v} = 0 \implies -v + gT + \frac{gh}{v} = 0 \implies T = \frac{v}{g} - \frac{h}{v}. \quad (14.26)$$

REMARKS: Note that we must have  $v > \sqrt{gh}$  in order for a positive solution for  $T$  to exist. If  $v < \sqrt{gh}$ , then the SR effect is too small to cancel out the GR effect, even if the clock spends no time sitting at the top. If  $v = \sqrt{gh}$ , then  $T = 0$ , and we essentially have the same situation as in Exercise 14.12. Note also that if  $v$  is very large compared with  $\sqrt{gh}$  (but still small compared with  $c$ , so that our  $\sqrt{1 - v^2/c^2} \approx 1 - v^2/2c^2$  approximation is valid), then  $T \approx v/g$ , which is independent of  $h$ . ♣

### 14.3. Circular motion

- In  $A$ 's frame, there is only the SR time-dilation effect.  $A$  sees  $B$  move at speed  $v$ , so  $B$ 's clock runs slow by a factor of  $\sqrt{1 - v^2/c^2}$ . And since  $v \ll c$ , we may use the Taylor series to approximate this as  $1 - v^2/2c^2$ .
- In this frame, there are both SR and GR time-dilation effects.  $A$  moves at speed  $v$  with respect to  $B$  in this frame, so the SR effect is that  $A$ 's clock runs slow by a factor  $\sqrt{1 - v^2/c^2} \approx 1 - v^2/2c^2$ . But  $B$  undergoes an acceleration of  $a = v^2/r$  toward  $A$ , so for all  $B$  knows, he lives in a world where the acceleration due to gravity is  $v^2/r$ .  $A$  is "higher" in the gravitational field, so the GR effect is that  $A$ 's clock runs fast by a factor  $1 + ar/c^2 = 1 + v^2/c^2$ . Multiplying the SR and GR effects together, we find (to lowest order) that  $A$ 's clock runs fast by a factor  $1 + v^2/2c^2$ . This means (to lowest order) that  $B$ 's clock runs slow by a factor  $1 - v^2/2c^2$ , in agreement with the answer to part (a).
- In this frame, there is no relative motion between  $A$  and  $B$ , so there is only the GR time-dilation effect. The gravitational field (that is, the centripetal acceleration) at a distance  $x$  from the center is  $g_x = x\omega^2$ . Imagine lining up a series of clocks along a radius, with separation  $dx$ . Then the GR time-dilation result tells us that each clock loses a fraction  $g_x dx/c^2 = x\omega^2 dx/c^2$  of time relative to the next clock inward. Integrating these fractions from  $x = 0$  to  $x = r$  shows that  $B$ 's clock loses a fraction  $r^2\omega^2/2c^2 = v^2/2c^2$ , compared with  $A$ 's clock. This agrees with the results in parts (a) and (b).

REMARK: If you want to imagine an analogous line of clocks in part (b), you can imagine lining a stick with them, with  $B$  at one end of the stick. The sensible thing to do with the stick is to have it be motionless with respect to  $B$ 's frame (as the line of clocks was in part (c)). But this means that the stick doesn't rotate with respect to the inertial axes, because  $B$ 's axes don't rotate. So all of the

clocks feel the same acceleration  $r\omega^2 = v^2/r$ , in contrast with the decreasing accelerations in part (c). The integral of all the fractions therefore doesn't pick up the factor of 2 as it did in part (c), and so we simply end up with  $v^2/c^2$ . The SR effect then arises in part (b) because  $A$  is flying past the clock on the other end of the stick, whereas in part (c)  $A$  was at rest. ♣

### 14.4. More circular motion

- (a) In the lab frame, the situation is symmetric with respect to  $A$  and  $B$ . Therefore, if  $A$  and  $B$  are decelerated in a symmetric manner and brought together, their clocks must read the same time.

Assume (in the interest of obtaining a contradiction) that  $A$  sees  $B$ 's clock run slow. Then after an arbitrarily long time,  $A$  will see  $B$ 's clock an arbitrarily large time behind his. Now bring  $A$  and  $B$  to a stop. There is no possible way that the stopping motion can make  $B$ 's clock gain an arbitrarily large amount of time, as seen by  $A$ . This is true because everything takes place in a finite region of space, so there is an upper bound on the GR time-dilation effect (because it behaves like  $gh/c^2$ , and  $h$  is bounded). Therefore,  $A$  will end up seeing  $B$ 's clock reading less. This contradicts the result of the previous paragraph. Likewise for the case where  $A$  sees  $B$ 's clock run fast.

**REMARK:** Note how this problem differs from the problem where  $A$  and  $B$  move with equal speeds directly away from each other, and then reverse directions and head back to meet up again. For this new “linear” problem, the symmetry reasoning in the first paragraph above still holds, so  $A$  and  $B$  will indeed have the same clock readings when they meet up again. But the reasoning in the second paragraph does not hold (it had better not, because each person does *not* see the other person's clock running at the same rate). The error is that in this linear scenario, the experiment is not contained in a small region of space, so the turning-around effects of order  $gh/c^2$  become arbitrarily large as the time of travel becomes arbitrarily large, because  $h$  grows with time (see Problem 14.9). ♣

- (b) In this frame, there are both SR and GR time-dilation effects.  $A$  moves at speed  $2v$  with respect to  $B$  in this frame (we don't need to use the relativistic velocity-addition formula, because  $v \ll c$ ), so the SR effect is that  $A$ 's clock runs slow by a factor  $\sqrt{1 - (2v)^2/c^2} \approx 1 - 2v^2/c^2$ . But  $B$  undergoes an acceleration of  $a = v^2/r$  toward  $A$ , so the GR effect is that  $A$ 's clock runs fast by a factor  $1 + a(2r)/c^2 = 1 + 2v^2/c^2$  (because they are separated by a distance  $2r$ ). Multiplying the SR and GR effects together, we find (to lowest order) that the two clocks run at the same rate.
- (c) In this frame, there is no relative motion between  $A$  and  $B$ , so there is only (at most) the GR effect. But  $A$  and  $B$  are both at the same gravitational potential, because they are at the same radius. Therefore, they both see the clocks running at the same rate. If you want, you can line up a series of clocks along the diameter between  $A$  and  $B$ , as we did along a radius in part (c) of Problem 14.3. The clocks will gain time as you march in toward the center, and then lose the same amount of time as you march back out to the diametrically opposite point.

### 14.5. Accelerator's point of view

- (a) **FIRST SOLUTION:** Equation (14.5) says that the distance traveled by the rocket (as measured in the original inertial frame), as a function of the time in the inertial frame, is

$$d = \frac{1}{g} \left( \sqrt{1 + (gt)^2} - 1 \right). \quad (14.27)$$

An inertial observer on the planet therefore measures the rocket–planet distance to be

$$x = \ell - \frac{1}{g} \left( \sqrt{1 + (gt)^2} - 1 \right). \quad (14.28)$$

The rocket observer sees this length contracted by a factor  $\gamma$ . Using the result of Exercise 14.16, we have  $\gamma = \sqrt{1 + (gt)^2} = \cosh(g\tau)$ . So the rocket–planet distance, as measured in the instantaneous inertial frame of the rocket, is

$$x = \frac{\ell - \frac{1}{g}(\cosh(g\tau) - 1)}{\cosh(g\tau)} \implies 1 + gx = \frac{1 + g\ell}{\cosh(g\tau)}. \quad (14.29)$$

SECOND SOLUTION: Equation (14.21) gives the speed of the planet in the accelerating frame of the rocket. Using the results of Exercise 14.16 to write  $v$  in terms of  $\tau$ , we have (with  $c = 1$ )

$$\frac{dx}{d\tau} = -(1 + gx) \tanh(g\tau). \quad (14.30)$$

Separating variables and integrating gives

$$\begin{aligned} \int \frac{dx}{1 + gx} &= - \int \tanh(g\tau) d\tau \implies \ln(1 + gx) = -\ln(\cosh(g\tau)) + C \\ &\implies 1 + gx = \frac{A}{\cosh(g\tau)}. \end{aligned} \quad (14.31)$$

Since the initial condition is  $x = \ell$  when  $\tau = 0$ , we must have  $A = 1 + g\ell$ , which gives Eq. (14.16), as desired.

(b) Equation (14.20) says that the planet’s clock runs fast (or slow) according to

$$dt = d\tau (1 + gx) \sqrt{1 - v^2}. \quad (14.32)$$

The results of Exercise 14.16 yield  $\sqrt{1 - v^2} = 1/\cosh(g\tau)$ . Combining this with the result for  $1 + gx$  above, and integrating, gives

$$\int dt = \int \frac{(1 + g\ell) d\tau}{\cosh^2(g\tau)} \implies gt = (1 + g\ell) \tanh(g\tau). \quad (14.33)$$

### 14.6. Getting way ahead

The explanation of why the two clocks show different times in the ground frame is the following. The rocket becomes increasingly length contracted in the ground frame, which means that the front end isn’t traveling quite as fast as the back end. Therefore, the time-dilation factor for the front clock isn’t as large as that for the back clock. So the front clock loses less time relative to the ground, and hence ends up ahead of the back clock. Of course, it’s not at all obvious that everything works out quantitatively and that the front clock eventually ends up an arbitrarily large time ahead of the back clock. In fact, it’s quite surprising that this is the case, because the above difference in speeds is very small. But let’s now show that the above explanation does indeed account for the difference in the clock readings.

Let the back of the rocket be located at position  $x$ . Then the front is located at position  $x + L\sqrt{1 - v^2}$ , due to the length contraction. Taking the time derivatives of

the two positions, we see that the speeds of the back and front are (with  $v \equiv dx/dt$ )<sup>12</sup>

$$v_b = v, \quad \text{and} \quad v_f = v(1 - L\gamma\dot{v}). \quad (14.34)$$

If we assume that the back is the part that accelerates at  $g$  (it doesn't matter which point we pick, to leading order), then we can just invoke the result in Eq. (14.4),

$$v_b = v = \frac{gt}{\sqrt{1 + (gt)^2}}, \quad (14.35)$$

where  $t$  is the time in the ground frame. Having written down  $v$ , we must now find the  $\gamma$  factors associated with the speeds of the front and back. The  $\gamma$  factor associated with the speed of the back, namely  $v$ , is

$$\gamma_b = \frac{1}{\sqrt{1 - v^2}} = \sqrt{1 + (gt)^2}. \quad (14.36)$$

The  $\gamma$  factor associated with the speed of the front,  $v_f = v(1 - L\gamma\dot{v})$ , is a bit more complicated. We must first calculate  $\dot{v}$ . From Eq. (14.35), we obtain  $\dot{v} = g/(1 + g^2t^2)^{3/2}$ , which gives

$$v_f = v(1 - L\gamma\dot{v}) = \frac{gt}{\sqrt{1 + (gt)^2}} \left( 1 - \frac{gL}{1 + g^2t^2} \right). \quad (14.37)$$

The  $\gamma$  factor (or rather  $1/\gamma$ , which is what we'll be concerned with) associated with this speed is given as follows. In the first line below, we ignore the higher-order  $(gL)^2$  term, because it is really  $(gL/c^2)^2$ , and we are assuming that  $gL/c^2$  is small. And in obtaining the third line, we use the Taylor-series approximation,  $\sqrt{1 - \epsilon} \approx 1 - \epsilon/2$ .

$$\begin{aligned} \frac{1}{\gamma_f} &= \sqrt{1 - v_f^2} \approx \sqrt{1 - \frac{g^2t^2}{1 + g^2t^2} \left( 1 - \frac{2gL}{1 + g^2t^2} \right)} \\ &= \frac{1}{\sqrt{1 + g^2t^2}} \sqrt{1 + \frac{2g^3t^2L}{1 + g^2t^2}} \\ &\approx \frac{1}{\sqrt{1 + g^2t^2}} \left( 1 + \frac{g^3t^2L}{1 + g^2t^2} \right). \end{aligned} \quad (14.38)$$

We can now calculate the time that each clock shows, at time  $t$  in the ground frame. The time on the back clock changes according to  $dt_b = dt/\gamma_b$ , so Eq. (14.36) gives

$$t_b = \int_0^t \frac{dt}{\sqrt{1 + g^2t^2}}. \quad (14.39)$$

The integral of  $dx/\sqrt{1 + x^2}$  is  $\sinh^{-1} x$  (to derive this, make the substitution  $x \equiv \sinh \theta$ ). Letting  $x \equiv gt$ , this gives

$$gt_b = \sinh^{-1}(gt). \quad (14.40)$$

The time on the front clock changes according to  $dt_f = dt/\gamma_f$ , so Eq. (14.38) gives

$$t_f = \int_0^t \frac{dt}{\sqrt{1 + g^2t^2}} + \int_0^t \frac{g^3t^2L dt}{(1 + g^2t^2)^{3/2}}. \quad (14.41)$$

<sup>12</sup> Since these two speeds aren't equal, there is an ambiguity concerning which speed we should use in the length-contraction factor,  $\sqrt{1 - v^2}$ . Equivalently, the rocket doesn't have a single inertial frame that describes all of it. But you can show that any differences arising from this ambiguity are of higher order in  $gL/c^2$  than we need to be concerned with.

The integral of  $x^2 dx / (1 + x^2)^{3/2}$  is  $\sinh^{-1} x - x / \sqrt{1 + x^2}$  (to derive this, make the substitution  $x \equiv \sinh \theta$ , and use  $\int d\theta / \cosh^2 \theta = \tanh \theta$ ). Letting  $x \equiv gt$ , this gives

$$gt_f = \sinh^{-1}(gt) + (gL) \left( \sinh^{-1}(gt) - \frac{gt}{\sqrt{1 + g^2 t^2}} \right). \quad (14.42)$$

Using Eqs. (14.35) and (14.40), we may rewrite this as

$$gt_f = gt_b(1 + gL) - gLv. \quad (14.43)$$

Dividing by  $g$ , and putting the  $c$ 's back in to make the units correct, we finally have

$$t_f = t_b \left( 1 + \frac{gL}{c^2} \right) - \frac{Lv}{c^2}, \quad (14.44)$$

as we wanted to show. If we look at this calculation from the reverse point of view, we see that by using only Special Relativity concepts, we have demonstrated that someone at the back of a rocket sees a clock at the front running fast by a factor  $(1 + gL/c^2)$ . There are, however, much easier ways of deriving this, as we saw in Section 14.2 and in Problem 11.25 (“Acceleration and redshift”).

### 14.7. $Lv/c^2$ revisited

Consider first the case where the rocket accelerates while you sit there. Problem 14.6 is exactly relevant here, and it tells us that in your frame the clock readings are related by

$$t_f = t_b \left( 1 + \frac{gL}{c^2} \right) - \frac{Lv}{c^2}. \quad (14.45)$$

You will eventually see the front clock an arbitrarily large time ahead of the back clock. But note that for small times (before things become relativistic), the standard Newtonian result,  $v \approx gt_b$ , is valid, so we have

$$t_f \approx \left( t_b + \frac{Lv}{c^2} \right) - \frac{Lv}{c^2} = t_b. \quad (14.46)$$

So in this setup where the rocket is the one that accelerates, both clocks show essentially the same time near the start. This makes sense; both clocks have essentially the same speed at the beginning, so to lowest order their  $\gamma$  factors are the same, so the clocks run at the same rate. But eventually the front clock will get ahead of the back clock.

Now consider the case where you accelerate while the rocket sits there. Problem 14.5 is relevant here, if we let the rocket in that problem now become you, and if we let two planets a distance  $L$  apart become the two ends of the rocket. The times you observe on the front and back clocks on the rocket are then, using Eq. (14.33) and assuming that you are accelerating toward the rocket,

$$gt_f = (1 + g\ell) \tanh(g\tau), \quad \text{and} \quad gt_b = (1 + g(\ell + L)) \tanh(g\tau). \quad (14.47)$$

But from Exercise 14.16, we know that your speed relative to the rocket is  $v = \tanh(g\tau)$ . Equation (14.47) therefore gives  $t_b = t_f + Lv$ , or  $t_b = t_f + Lv/c^2$  with the  $c^2$ . So in this case we arrive at the standard  $Lv/c^2$  “rear clock ahead” result.

The point here is that in this second case, the clocks are synchronized in the rocket frame, and this is the assumption that went into our derivation of the  $Lv/c^2$  result in Chapter 11. In the first case above where the rocket accelerates, the clocks are *not* synchronized in the rocket frame (except right at the start), so it isn't surprising that we don't obtain the  $Lv/c^2$  result.

### 14.8. Circling the earth

This is one setup where we really need to use the correct term, *stationary*-proper-time principle. It turns out that  $B$ 's path yields a saddle point for the proper time. The value at this saddle point is less than  $A$ 's proper time, but this is irrelevant, because we care only about local stationary points, not about global extrema.

To show that we have a saddle point, we must show that (1) the differences in the proper time are second order, and (2) there exist nearby paths that give both a larger and a smaller proper time. The first of these is true because the first-order differences vanish due to the fact that the path satisfies the Euler–Lagrange equations for the Lagrangian in Eq. (14.15), because the path is indeed a physical one.

The second is true because the proper time can be made smaller by having  $B$  speed up and slow down. This will cause a net increase in the time-dilation effect as viewed by  $A$ , thereby yielding a smaller proper time.<sup>13</sup> And the proper time can be made larger by having  $B$  take a nearby path that doesn't quite form a great circle on the earth. (Imagine the curve traced out by a rubber band that has just begun to slip away from a great-circle position.) This path is shorter, so  $B$  won't have to travel as fast to get back in a given time, so the time-dilation effect will be smaller as viewed by  $A$ , thereby yielding a larger proper time.

### 14.9. Twin paradox

- (a) In the earth frame, the spaceship travels at speed  $v$  for essentially the whole time. Therefore, the traveler ages less by a fraction  $\sqrt{1 - v^2/c^2} \approx 1 - v^2/2c^2$ . The fractional loss of time is thus  $v^2/2c^2$ . The time-dilation effect is different during the short turning-around period, but this is negligible.

- (b) Let the distance to the star be  $\ell$ , as measured in the frame of the earth (but the difference in lengths in the two frames is negligible in this problem), and let the turnaround take a time  $T$ . Then the given information says that  $T \ll (2\ell)/v$ .

During the constant-speed part of the trip, the traveler sees the earth clock running slow by a fraction  $\sqrt{1 - v^2/c^2} \approx 1 - v^2/2c^2$ . The time for this constant-speed part is (essentially)  $2\ell/v$ , so the earth clock loses a time of  $(v^2/2c^2)(2\ell/v) = v\ell/c^2$ .

However, during the turnaround time, the spaceship is accelerating toward the earth, so the traveler sees the earth clock running fast, due to the GR time dilation. The magnitude of the acceleration is  $a = 2v/T$ , because the spaceship goes from velocity  $v$  to  $-v$  in time  $T$ . The earth clock therefore runs fast by a factor  $1 + a\ell/c^2 = 1 + 2v\ell/Tc^2$ . This happens for a time  $T$ , so the earth clock gains a time of  $(2v\ell/Tc^2)T = 2v\ell/c^2$ .

Combining the results of the previous two paragraphs, we see that the earth clock gains a time of  $2v\ell/c^2 - v\ell/c^2 = v\ell/c^2$ . This is a fraction  $(v\ell/c^2)/(2\ell/v) = v^2/2c^2$  of the total time, in agreement with part (a).

![Diagram of a circular path with a semicircular turnaround. A dashed line represents a straight path, and a solid line represents a curved path. The angle theta is shown between the dashed line and the radius r of the semicircle. The velocity vector v is shown at the end of the path.](c56f04a44dbbd36574253eefdbc5187e_img.jpg)

The diagram shows a path consisting of two straight segments connected by a semicircular arc. The straight segments are represented by dashed lines with arrows pointing towards the arc. The semicircular arc is a solid line with an arrow indicating the direction of travel. A radius  $r$  is drawn from the center of the semicircle to a point on the arc. An angle  $\theta$  is shown between this radius and a dashed line that is collinear with the incoming straight path. A velocity vector  $v$  is shown at the end of the arc, tangent to it.

Diagram of a circular path with a semicircular turnaround. A dashed line represents a straight path, and a solid line represents a curved path. The angle theta is shown between the dashed line and the radius r of the semicircle. The velocity vector v is shown at the end of the path.

### 14.10. Twin paradox again

- (a) The only difference between this problem and the previous one is the nature of the turnaround, so all we need to show here is that the traveler still sees the earth clock gain a time of  $2v\ell/c^2$  during the turnaround.

Let the radius of the semicircle be  $r$ . Then the magnitude of the acceleration is  $a = v^2/r$ . Let  $\theta$  be the angle shown in Fig. 14.9. For a given  $\theta$ , the earth is at

Fig. 14.9

<sup>13</sup> This is true for the same reason that a person who travels at constant speed in a straight line between two points shows a larger proper time than a second person who speeds up and slows down. This follows directly from SR time dilation, as viewed by the first person. If you want, you can imagine unrolling  $B$ 's circular orbit into a straight line, and then invoke the result just mentioned. As far as SR time-dilation effects from clock  $A$ 's point of view go, it doesn't matter if the circle is unrolled into a straight line.

a height of essentially  $\ell \cos \theta$  in the gravitational field felt by the spaceship. The fractional time that the earth gains while the traveler is at an angle  $\theta$  is therefore  $ah/c^2 = (v^2/r)(\ell \cos \theta)/c^2$ . Integrating this over the time of the turnaround, and using  $dt = r d\theta/v$ , we see that the earth gains the desired time of

$$\Delta t = \int_{-\pi/2}^{\pi/2} \left( \frac{v^2 \ell \cos \theta}{rc^2} \right) \left( \frac{r d\theta}{v} \right) = \frac{2v\ell}{c^2}. \quad (14.48)$$

- (b) Let the acceleration vector at a given instant be  $\mathbf{a}$ , and let  $\boldsymbol{\ell}$  be the vector from the spaceship to the earth. Note that since the turnaround is done in a small region of space,  $\boldsymbol{\ell}$  is essentially constant here. The earth is at a height of  $\hat{\mathbf{a}} \cdot \boldsymbol{\ell}$  in the gravitational field felt by the spaceship; the dot product just gives the cosine term in the above solution in part (a). The fractional time gain,  $ah/c^2$ , is therefore equal to  $|\mathbf{a}|(\hat{\mathbf{a}} \cdot \boldsymbol{\ell})/c^2 = \mathbf{a} \cdot \boldsymbol{\ell}/c^2$ . Integrating this over the time of the turnaround, we see that the earth gains a time of

$$\begin{aligned} \Delta t &= \int_{t_i}^{t_f} \frac{\mathbf{a} \cdot \boldsymbol{\ell}}{c^2} dt = \frac{\boldsymbol{\ell}}{c^2} \cdot \int_{t_i}^{t_f} \mathbf{a} dt \\ &= \frac{\boldsymbol{\ell}}{c^2} \cdot (\mathbf{v}_f - \mathbf{v}_i) \\ &= \frac{\boldsymbol{\ell} \cdot (2\mathbf{v}_f)}{c^2} \\ &= \frac{2v\ell}{c^2}, \end{aligned} \quad (14.49)$$

as we wanted to show. The point here is that no matter how complicated the motion is during the turnaround, the total effect is simply to change the velocity from  $\mathbf{v}$  outward to  $\mathbf{v}$  inward.

### 14.11. Twin paradox times

- (a) As viewed by  $A$ , the relation between the twins' times is

$$dt_B = \sqrt{1 - v^2} dt_A. \quad (14.50)$$

Assuming  $v_0 \ll c$ , we may say that  $v(t_A)$  is essentially equal to  $v_0 - gt_A$ , so the out and back parts of the trip each take a time of essentially  $v_0/g$  in  $A$ 's frame. The total elapsed time on  $B$ 's clock is therefore

$$\begin{aligned} T_B &= \int dt_B \approx 2 \int_0^{v_0/g} \sqrt{1 - v^2} dt_A \\ &\approx 2 \int_0^{v_0/g} \left( 1 - \frac{v^2}{2} \right) dt_A \\ &\approx 2 \int_0^{v_0/g} \left( 1 - \frac{1}{2}(v_0 - gt)^2 \right) dt \\ &= 2 \left( t + \frac{1}{6g}(v_0 - gt)^3 \right) \Big|_0^{v_0/g} \\ &= \frac{2v_0}{g} - \frac{v_0^3}{3gc^2}, \end{aligned} \quad (14.51)$$

where we have put the  $c$ 's back in to make the units right. The ratio of  $B$ 's elapsed time to  $A$ 's is therefore

$$\frac{T_B}{T_A} \approx \frac{T_B}{2v_0/g} \approx 1 - \frac{v_0^2}{6c^2}. \quad (14.52)$$

(b) As viewed by  $B$ , the relation between the twins' times is given by Eq. (14.13),

$$dt_A = \sqrt{1 - \frac{v^2}{c^2}} \left(1 + \frac{gy}{c^2}\right) dt_B. \quad (14.53)$$

Assuming  $v_0 \ll c$ , we may say that  $v(t_B)$  is essentially equal to  $v_0 - gt_B$ , and  $A$ 's height is essentially equal to  $v_0 t_B - gt_B^2/2$ . The up and down parts of the trip each take a time of essentially  $v_0/g$  in  $B$ 's frame. Therefore, the total elapsed time on  $A$ 's clock is (using the approximation in Eq. (14.14), and dropping the  $c$ 's)

$$\begin{aligned} T_A &= \int dt_A \approx 2 \int_0^{v_0/g} \left(1 - \frac{v^2}{2} + gy\right) dt_B. \\ &\approx 2 \int_0^{v_0/g} \left(1 - \frac{1}{2}(v_0 - gt)^2 + g(v_0 t - gt^2/2)\right) dt. \\ &= 2 \left( t + \frac{1}{6g}(v_0 - gt)^3 + g\left(\frac{v_0 t^2}{2} - \frac{gt^3}{6}\right) \right) \Big|_0^{v_0/g} \\ &= \frac{2v_0}{g} - \frac{v_0^3}{3g} + g \left( \frac{v_0^3}{g^2} - \frac{v_0^3}{3g^2} \right) \\ &= \frac{2v_0}{g} + \frac{v_0^3}{3gc^2}, \end{aligned} \quad (14.54)$$

where we have put the  $c$ 's back in to make the units right. We therefore have

$$\frac{T_A}{T_B} \approx \frac{T_A}{2v_0/g} \approx 1 + \frac{v_0^2}{6c^2} \implies \frac{T_B}{T_A} \approx 1 - \frac{v_0^2}{6c^2}, \quad (14.55)$$

up to higher-order corrections. This agrees with the result found in part (a), as the Equivalence Principle requires.