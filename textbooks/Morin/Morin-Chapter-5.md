# Chapter 5 Conservation of energy and momentum

Conservation laws are extremely important in physics. They are enormously helpful, both quantitatively and qualitatively, in figuring out what is going on in a physical system. When we say that something is “conserved,” we mean that it is constant over time. If a certain quantity is conserved, for example, while a ball rolls around in a valley, or while a group of particles interact, then the possible final motions are greatly restricted. If we can write down enough conserved quantities (which we are generally able to do, at least for the systems we’ll be concerned with), then we can restrict the final motions down to just one possibility, and so we have solved our problem. Conservation of energy and momentum are two of the main conservation laws in physics. A third, conservation of angular momentum, is discussed in Chapters 7–9.

It should be noted that it isn’t *necessary* (in principle) to use conservation of energy and momentum when solving a problem. We’ll derive these conservation laws from Newton’s laws. Therefore, if you felt like it, you could always (in theory) simply start with first principles and use  $F = ma$ , etc. However, at best, you would soon grow weary of this approach. And at worst, you would throw in the towel after finding the problem completely intractable. For example, you would get nowhere trying to analyze the collision between two shopping carts (whose contents are free to shift around) by looking at the forces on all the various objects. But conservation of momentum can quickly give you a great deal of information. The point of conservation laws is that they make your calculations much easier, and they also provide a means for getting a good idea of the overall qualitative behavior of a system.

## 5.1 Conservation of energy in one dimension

Consider a force, in just one dimension for now, that depends only on position. That is,  $F = F(x)$ . If the force acts on a particle of mass  $m$ , and if we write  $a$  as  $v dv/dx$ , then  $F = ma$  becomes

$$F(x) = mv \frac{dv}{dx}. \quad (5.1)$$

We can separate variables here and integrate from a given point  $x_0$  where the velocity is  $v_0$  to an arbitrary point  $x$  where the velocity is  $v$ . The result is

$$\begin{aligned} \int_{x_0}^x F(x') dx' &= \int_{v_0}^v mv' dv' \implies \int_{x_0}^x F(x') dx' = \frac{1}{2}mv^2 - \frac{1}{2}mv_0^2 \\ &\implies E = \frac{1}{2}mv^2 - \int_{x_0}^x F(x') dx', \end{aligned} \quad (5.2)$$

where  $E \equiv mv_0^2/2$ .  $E$  depends on  $v_0$ , so it therefore also depends on the choice of  $x_0$ , because a different  $x_0$  would yield (in general) a different  $v_0$ . What we've done here is simply follow the procedure in Section 3.3, for a function that depends only on  $x$ . If we now define the *potential energy*,  $V(x)$ , as

$$V(x) \equiv - \int_{x_0}^x F(x') dx', \quad (5.3)$$

then Eq. (5.2) becomes

$$\frac{1}{2}mv^2 + V(x) = E. \quad (5.4)$$

We define the first term here to be the *kinetic energy*. Since this equation is true at all points in the particle's motion, the sum of the kinetic energy and potential energy is constant. In other words, the total energy is conserved. If a particle loses (or gains) potential energy, then its speed increases (or decreases). Common examples of potential energy are  $kx^2/2$  for a Hooke's-law spring force ( $-kx$ ), with  $x_0$  chosen to be zero; and  $mgy$  for the gravitational force ( $-mg$ ), with  $y_0$  chosen to be zero.

In Boston, lived Jack as did Jill,  
 Who gained  $mgh$  on a hill.  
 In their liquid pursuit,  
 Jill exclaimed with a hoot,  
 "I think we've just climbed a landfill!"

While noting, "Oh, this is just grand,"  
 Jack tripped on some trash in the sand.  
 He changed his potential  
 To kinetic, torrential,  
 But not before grabbing Jill's hand.

So that's what really happened on that hill. People don't just magically come "tumbling after" for no reason, of course.

For a particle undergoing a given motion, both  $E$  and  $V(x)$  depend on the arbitrary choice of  $x_0$  in Eq. (5.3). This implies that  $E$  and  $V(x)$  have no real meaning by themselves. Only the *difference* between  $E$  and  $V(x)$  is relevant (and

it equals the kinetic energy); this difference is independent of the choice of  $x_0$ . But in order to be concrete in a given setup, we need to pick an arbitrary  $x_0$ , so we must remember to state which  $x_0$  we've chosen. For example, it makes no sense to simply say that the gravitational potential energy of an object at height  $y$  above the ground is  $-\int F dy = -\int (-mg) dy = mgy$ . We have to say that the potential energy is  $mgy$  with respect to the ground (assuming that our  $y_0$  is at ground level). If we wanted to, we could say that the potential energy is  $mgy + mg(7 \text{ m})$  with respect to a point 7 meters below the ground. This is perfectly legitimate, although a bit unconventional.<sup>1</sup> But no matter what reference point we pick, the difference in the potential energies at the points, say,  $y = 3 \text{ m}$  and  $y = 5 \text{ m}$  equals  $mg(2 \text{ m})$ .

Note that although we introduced the  $x_0$  in Eq. (5.2) as a point where the particle was at some time, the particle in fact need not ever be at the point  $x_0$ . For example, we can throw a ball up at 8 m/s from a height of 5 m while measuring the gravitational potential energy with respect to a point a kilometer high. The ball is certainly not going to reach a height of a kilometer, but that's fine. All that matters is the difference between  $E$  and  $V(x)$  (both of which are very much negative here) throughout the motion, so a constant shift is irrelevant. We've simply added on the same negative quantity to both  $E$  and  $V(x)$  in Eq. (5.4), compared with the values someone would measure if the ground were the reference point.

If we take the difference between Eq. (5.4) evaluated at two points,  $x_1$  and  $x_2$  (or if we just integrate Eq. (5.1) from  $x_1$  to  $x_2$ ), then we obtain

$$\begin{aligned} \frac{1}{2}mv^2(x_2) - \frac{1}{2}mv^2(x_1) &= V(x_1) - V(x_2) \\ &= \int_{x_1}^{x_2} F(x') dx' \equiv (\text{Work})_{x_1 \rightarrow x_2}. \end{aligned} \quad (5.5)$$

Here it is clear that only differences in potential energies matter. If we define the integral in this equation to be the *work* done on the particle as it moves from  $x_1$  to  $x_2$ , then we have produced the *work–energy theorem*:<sup>2</sup>

**Theorem 5.1** *The change in a particle's kinetic energy between points  $x_1$  and  $x_2$  equals the work done on the particle between  $x_1$  and  $x_2$ .*

If the force points in the same direction as the motion (that is, if the  $F(x)$  and the  $dx$  in Eq. (5.5) have the same sign), then the work is positive and the speed increases. If the force points in the direction opposite to the motion, then the work is negative and the speed decreases.

<sup>1</sup> It gets to be a pain to keep repeating “with respect to the ground.” Therefore, whenever anyone talks about gravitational potential energy in a setup on the surface of the earth, it's generally understood that the ground is the reference point. If, on the other hand, the experiment reaches out to distances far from the earth, then  $r = \infty$  is understood to be the reference point, for reasons of convenience we will see in the first example below.

<sup>2</sup> In the form stated here, this theorem holds only for a point particle with no internal structure. See the “Work vs. potential energy” subsection below for the general theorem.

Referring back to Eq. (5.4), and assuming we've chosen a reference point  $x_0$  for the potential energy (and perhaps we've added on a constant to  $V(x)$ , just because we felt like it), let's draw in Fig. 5.1 the  $V(x)$  curve and also the constant  $E$  line (which we can determine if we're given, say, the initial position and speed). Then the difference between  $E$  and  $V(x)$  gives the kinetic energy. The places where  $V(x) > E$  are the regions where the particle cannot go. The places where  $V(x) = E$  are the "turning points" where the particle stops and changes direction. In the figure, the particle is trapped between  $x_1$  and  $x_2$ , and oscillates back and forth. The potential  $V(x)$  is extremely useful this way because it makes clear the general properties of the motion.

![Figure 5.1: A graph of potential energy V(x) versus position x. The V(x) curve is a continuous, wavy line. A horizontal dashed line represents the total energy E. The curve V(x) intersects the E line at two points, x1 and x2. Between x1 and x2, the curve V(x) is below the E line, indicating regions where the particle can move. Outside this interval, V(x) is above E, indicating forbidden regions.](1e095c02ade34d65a1d4aadd2575d2c9_img.jpg)

Figure 5.1: A graph of potential energy V(x) versus position x. The V(x) curve is a continuous, wavy line. A horizontal dashed line represents the total energy E. The curve V(x) intersects the E line at two points, x1 and x2. Between x1 and x2, the curve V(x) is below the E line, indicating regions where the particle can move. Outside this interval, V(x) is above E, indicating forbidden regions.

Fig. 5.1

REMARK: It may seem silly to introduce a specific  $x_0$  as a reference point, considering that it's only the differences in the potential (which are independent of  $x_0$ ) that have any meaning. It's sort of like taking the difference between 17 and 8 by first finding their sizes relative to 5, namely 12 and 3, and then subtracting 3 from 12 to obtain 9. However, since integrals are harder to do than simple subtractions, it's advantageous to do the integral once and for all and thereby label all positions with a definite number  $V(x)$ , and to then take differences between the  $V$ 's when needed. ♣

The differential form of Eq. (5.3) is

$$F(x) = -\frac{dV(x)}{dx}. \quad (5.6)$$

Given  $V(x)$ , it is easy to take its derivative to obtain  $F(x)$ . But given  $F(x)$ , it may be difficult (or impossible) to perform the integration in Eq. (5.3) and write  $V(x)$  in closed form. But this is not of much concern. The function  $V(x)$  is well defined (assuming that the force is a function of  $x$  only), and if needed it can be computed numerically to any desired accuracy.

**Example (Gravitational potential energy):** Consider two point masses,  $M$  and  $m$ , separated by a distance  $r$ . Newton's law of gravitation says that the force between them is attractive and has magnitude  $GMm/r^2$  (we'll talk more about gravity in Section 5.4.1). The potential energy of the system at separation  $r$ , measured relative to separation  $r_0$ , is therefore

$$V(r) - V(r_0) = -\int_{r_0}^r \frac{-GMm}{r'^2} dr' = \frac{-GMm}{r} + \frac{GMm}{r_0}, \quad (5.7)$$

where the minus sign in the integrand comes from the attractive nature of the force. A convenient choice for  $r_0$  is  $\infty$ , because this makes the second term vanish. It will be understood from now on that this  $r_0 = \infty$  reference point has been chosen. Therefore (see Fig. 5.2),

$$V(r) = \frac{-GMm}{r}. \quad (5.8)$$

![Figure 5.2: A graph of gravitational potential energy V(r) versus separation r. The V(r) curve is a hyperbola in the fourth quadrant, starting from negative infinity at r=0 and asymptotically approaching the r-axis (V=0) as r increases. The equation V(r) = -GMm/r is written next to the curve.](85721f3c7cf0210cd55e0d4dc8028a5e_img.jpg)

Figure 5.2: A graph of gravitational potential energy V(r) versus separation r. The V(r) curve is a hyperbola in the fourth quadrant, starting from negative infinity at r=0 and asymptotically approaching the r-axis (V=0) as r increases. The equation V(r) = -GMm/r is written next to the curve.

Fig. 5.2

**Example (Gravity near the earth):** What is the gravitational potential energy of a mass  $m$  at height  $y$ , relative to the ground? We know, of course, that it is  $mgy$ , but let's do it the hard way. If  $M$  is the mass of the earth and  $R$  is its radius, then Eq. (5.8) gives (assuming  $y \ll R$ )

$$\begin{aligned} V(R+y) - V(R) &= \frac{-GMm}{R+y} - \frac{-GMm}{R} = \frac{-GMm}{R} \left( \frac{1}{1+y/R} - 1 \right) \\ &\approx \frac{-GMm}{R} \left( (1 - y/R) - 1 \right) \\ &= \frac{GMmy}{R^2}, \end{aligned} \quad (5.9)$$

where we have used the Taylor series approximation for  $1/(1 + \epsilon)$  to obtain the second line. We have also used the fact that a sphere can be treated like a point mass, as far as gravity is concerned. We'll prove this in Section 5.4.1.

Using  $g \equiv GM/R^2$ , we see that the potential energy difference in Eq. (5.9) equals  $mgy$ . We have, of course, simply gone around in circles here. We integrated in Eq. (5.7), and then we basically differentiated in Eq. (5.9) by taking the difference between the forces at nearby points. But it's good to check that everything works out.

---

A good way to visualize a potential  $V(x)$  is to imagine a ball sliding around in a valley or on a hill. For example, the potential of a typical spring is  $V(x) = kx^2/2$  (this produces the Hooke's-law force,  $F(x) = -dV/dx = -kx$ ), and we can get a decent idea of what is going on if we imagine a valley with height given by  $y = x^2/2$ . The gravitational potential of the ball is then  $mgy = mgx^2/2$ . Choosing  $mg = k$  gives the desired potential. If we then look at the projection of the ball's motion on the  $x$  axis, it seems like we have constructed a setup identical to the original spring.

However, although this analogy helps in visualizing the basic properties of the motion, the two setups are *not* the same. The details of this fact are left for Problem 5.7, but the following observation should convince you that they are indeed different. Let the ball be released from rest in both setups at a large value of  $x$ . Then the force  $kx$  due to the spring is very large. But the force in the  $x$  direction on the particle in the valley is only a fraction of  $mg$ , namely  $(mg \sin \theta) \cos \theta$ , where  $\theta$  is the angle of the valley at that point. The setups are approximately the same, however, for small oscillations near the bottom of the valley. See Problem 5.7 for more details.

#### Conservative forces

Given any force (it can depend on  $x$ ,  $v$ ,  $t$ , and/or whatever), the work it does on a particle is defined by  $W \equiv \int F dx$ . If the particle starts at  $x_1$  and ends up at  $x_2$ , then no matter how it gets there (it might speed up or slow down, or reverse direction a few times), we can calculate the total work done on it by all the forces

in the setup, and then equate the result with the change in kinetic energy, via

$$W_{\text{total}} \equiv \int_{x_1}^{x_2} F_{\text{total}} dx = \int_{x_1}^{x_2} m \left( \frac{v dv}{dx} \right) dx = \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2. \quad (5.10)$$

For some forces, the work done is independent of how the particle moves. A force that depends only on position (in one dimension) has this property, because the integral in Eq. (5.10) depends only on the endpoints. The  $W = \int F dx$  integral is the (signed) area under the  $F$  vs.  $x$  graph, and this area is independent of how the particle goes from  $x_1$  to  $x_2$ .

For other forces, the work done depends on how the particle moves. Such is the case for forces that depend on  $t$  or  $v$ , because it then matters *when* or *how quickly* the particle goes from  $x_1$  to  $x_2$ . A common example of such a force is friction. If you slide a brick across a table from  $x_1$  to  $x_2$ , then the work done by friction equals  $-\mu mg|\Delta x|$ . But if you slide the brick by wiggling it back and forth for an hour before you finally reach  $x_2$ , then the amount of negative work done by friction is very large. Since friction always opposes the motion, the contributions to the  $W = \int F dx$  integral are always negative, so there is never any cancellation. The result is therefore a large negative number.

The issue with friction is that although the  $\mu mg$  force looks like a constant force (which is a subset of position-only dependent forces), it actually isn't. At a given location, the friction can point to the right or to the left, depending on which way the particle is moving. Friction is therefore a function of velocity. True, it's a function only of the *direction* of the velocity, but that's enough to ruin the position-only dependence.

We now define a *conservative force* as one for which the work done on a particle between two given points is independent of how the particle makes the journey. From the preceding discussion, we know that a one-dimensional force is conservative if and only if it depends only on  $x$  (or is constant).<sup>3</sup> The point we're leading up to here is that although we can calculate the work done by any force, it makes sense to talk about the potential energy associated with a force only if the force is conservative. This is true because we want to be able to label each value of  $x$  with a unique number,  $V(x)$ , given by  $V(x) = -\int_{x_0}^x F dx$ . If this integral were dependent on how the particle goes from  $x_0$  to  $x$ , then it wouldn't be well defined, so we wouldn't know what number to assign to  $V(x)$ . We therefore talk about potential energies only if they are associated with conservative forces. In particular, it makes no sense to talk about the potential energy associated with a friction force.

A useful fact about the gravitational potential energy,  $mgz$ , is that it doesn't depend on the path the particle takes, even in two or three dimensions. This is true because even if the particle moves in a complicated direction, only the

<sup>3</sup> In two or three dimensions, however, we will see in Section 5.3 that a conservative force must satisfy another requirement, in addition to being dependent only on position.

vertical  $z$  component of the displacement is relevant in calculating the work done by gravity. If we break the path up into many little pieces, the total work done by gravity is obtained by adding up the many little  $-mg(dz)$  terms. But the sum of all the  $dz$ 's is always equal to the total  $z$ , independent of the path. Therefore, no matter what the particle is doing in the two horizontal directions, the change in gravitational potential energy is always just  $mgz$ . So the gravitational force is a conservative force in three dimensions. We'll see in Section 5.3 that this is a special case of a more general result.

---

**Example (Unwinding string):** A mass is connected to one end of a massless string, the other end of which is connected to a very thin frictionless vertical pole. The string is initially wound completely around the pole, in a very large number of tiny horizontal circles, so that the mass touches the pole. The mass is released, and the string gradually unwinds. What angle does the string make with the pole at the moment it becomes completely unwound?

**Solution:** Let  $\ell$  be the length of the string, and let  $\theta$  be the final angle it makes with the pole. Then the final height of the mass is  $\ell \cos \theta$  below the starting point. So the mass loses a potential energy of  $mg(\ell \cos \theta)$ . Conservation of energy therefore gives (picking the initial height as  $y = 0$ , although this doesn't matter)

$$K_i + V_i = K_f + V_f \implies 0 + 0 = \frac{1}{2}mv^2 - mg\ell \cos \theta \implies v^2 = 2g\ell \cos \theta. \quad (5.11)$$

There are two unknowns here,  $v$  and  $\theta$ , so we need one more equation. This will be the radial  $F = ma$  equation for the (essentially) final circular motion. Because the pole is very thin, the motion can always be approximated by a horizontal circle, which very slowly lowers as time goes by. Because there is essentially no motion in the vertical direction, the total force in this direction is zero. Therefore, the vertical component of the tension is essentially  $mg$ . The horizontal component is then  $mg \tan \theta$ , so the  $F = ma$  equation for the final circular motion (which has a radius of  $\ell \sin \theta$ ) is

$$mg \tan \theta = \frac{mv^2}{\ell \sin \theta} \implies v^2 = g\ell \sin \theta \tan \theta. \quad (5.12)$$

Equating our two expressions for  $v^2$  gives  $\tan \theta = \sqrt{2} \implies \theta \approx 54.7^\circ$ . Interestingly, this angle is independent of  $\ell$  and  $g$ .

---

#### *Work vs. potential energy*

When you drop a ball, does its speed increase because the gravitational force is doing work on it, or because its gravitational potential energy is decreasing? Well, both (or more precisely, either). Work and potential energy are two different ways of talking about the same thing (at least for conservative forces). Either method of

reasoning gives the correct result. However, be careful not to use *both* reasonings and “double count” the effect of gravity on the ball. Which choice of terminology you use depends on what you call your “system.” Just as with  $F = ma$  and free-body diagrams, it is important to label your system when dealing with work and energy, as we’ll see in the example below.

The work–energy theorem stated in Theorem 5.1 is relevant to one particle. What if we are dealing with the work done on a system that is composed of various parts? The general work–energy theorem states that the work done on a system by *external* forces equals the change in energy of the system. This energy may come in the form of (1) overall kinetic energy, (2) internal potential energy, or (3) internal kinetic energy (heat falls into this category, because it’s simply the random motion of molecules). So we can write the general work–energy theorem as

$$W_{\text{external}} = \Delta K + \Delta V + \Delta K_{\text{internal}} \quad (5.13)$$

For a point particle, there is no internal structure, so we have only the first of the three terms on the right-hand side, in agreement with Theorem 5.1. But to see what happens when a system has internal structure, consider the following example.

---

**Example (Raising a book):** Assume that you lift a book up at constant speed, so there is no change in kinetic energy. Let’s see what the general work–energy theorem says for various choices of the system.

- System = (book): Both you and gravity are external forces, and there is no change in the energy of the book as a system in itself. So the W–E theorem says

$$W_{\text{you}} + W_{\text{grav}} = 0 \quad \Longleftrightarrow \quad mgh + (-mgh) = 0. \quad (5.14)$$

- System = (book + earth): Now you are the only external force. The gravitational force between the earth and the book is an internal force which produces an internal potential energy. So the W–E theorem says

$$W_{\text{you}} = \Delta V_{\text{earth–book}} \quad \Longleftrightarrow \quad mgh = mgh. \quad (5.15)$$

- System = (book + earth + you): There is now no external force. The internal energy of the system changes because the earth–book gravitational potential energy increases, and also because *your* potential energy decreases. In order to lift the book, you have to burn some calories from the dinner you ate. So the W–E theorem says

$$0 = \Delta V_{\text{earth–book}} + \Delta V_{\text{you}} \quad \Longleftrightarrow \quad 0 = mgh + (-mgh). \quad (5.16)$$

Actually, a human body isn't 100% efficient, so what really happens here is that your potential energy decreases by more than  $mgh$ , but heat is produced. The sum of these two changes in energy equals  $-mgh$ . So, including an amount  $\eta$  of energy in the form of heat, we have

$$\begin{aligned} 0 &= \Delta V_{\text{earth-book}} + \Delta V_{\text{you}} + \Delta K_{\text{internal}} \\ \iff 0 &= mgh + (-mgh - \eta) + \eta. \end{aligned} \quad (5.17)$$

Another contribution to this  $\eta$  heat term can come from, for example, the heat from friction if you slide the book up a rough wall as you lift it.<sup>4</sup>

---

The moral of all this is that you can look at a setup in various ways, depending on what you pick as your system. Potential energy in one way might show up as work in another. In practice, it is usually more convenient to work in terms of potential energy. So for a dropped ball, people usually consider (consciously or not) gravity to be an internal force in the earth-ball system, as opposed to an external force on the ball system. In general, “conservation of energy,” commonly used in setups involving gravity and/or springs, is a straightforward principle to apply (and you'll get plenty of practice with it in the problems and exercises for this chapter). So it turns out that you can usually ignore all these issues about work and about picking your system.

But let's look at one more example, just to make sure we're on the same page. Consider a car that is braking (but not skidding). The friction force from the ground on the tires is what causes the car to slow down. But this force does no work on the car, because the ground isn't moving; the force acts over zero distance. So the external work on the left side of Eq. (5.13) is zero. The right side is therefore also zero. That is, the total energy of the car doesn't change. This is indeed true, because although the overall kinetic energy of the car decreases, there is an equal increase in internal kinetic energy in the form of heat in the brake pads and discs. In other words,  $\Delta K = -\Delta K_{\text{internal}}$ , and the total energy remains constant. The unfortunate fact about this process is that the energy that goes into heat is lost and can't be converted back into overall kinetic energy of the car. It makes much more sense to convert the overall kinetic energy into some form of internal potential energy (that is,  $\Delta K = -\Delta U$ ), which can then be converted back into overall kinetic energy. Such is the case with hybrid cars which convert overall kinetic energy into chemical potential energy in a battery.

Conversely, when a car accelerates, the friction force from the ground does no work (because the ground isn't moving), so the total energy of the car remains

<sup>4</sup> In this case we have included the wall as a fourth object in our system, because it might contain some of the heat. If you want to instead consider the wall as an external object providing a force, then things get tricky; see Problem 5.6.

the same. The internal potential energy of the gasoline (or battery) is converted into overall kinetic energy (along with some heat and sound). A similar thing happens when you stand at rest and then start walking. The friction force from the ground does no work on you, so your total energy remains the same. You're simply trading your breakfast for overall kinetic energy (plus some heat). For further discussion of work, see Mallinckrodt and Leff (1992).

### 5.2 Small oscillations

Consider an object in one dimension, subject to the potential  $V(x)$ . Let the object initially be at rest at a local minimum of  $V(x)$ , and then let it be given a small kick so that it moves back and forth around the equilibrium point. What can we say about this motion? Is it simple harmonic? Does the frequency depend on the amplitude?

It turns out that for small amplitudes, the motion is indeed simple harmonic, and the frequency can easily be found, given  $V(x)$ . To see this, expand  $V(x)$  in a Taylor series around the equilibrium point,  $x_0$ ,

$$\begin{aligned} V(x) = & V(x_0) + V'(x_0)(x - x_0) + \frac{1}{2!}V''(x_0)(x - x_0)^2 \\ & + \frac{1}{3!}V'''(x_0)(x - x_0)^3 + \cdots. \end{aligned} \quad (5.18)$$

This looks like a bit of a mess, but we can simplify it greatly.  $V(x_0)$  is an irrelevant additive constant. We can ignore it because only differences in energy matter (or equivalently, because  $F = -dV/dx$ ). And  $V'(x_0) = 0$ , by definition of the equilibrium point. So that leaves us with the  $V''(x_0)$  and higher-order terms. But for sufficiently small displacements, these higher-order terms are negligible compared with the  $V''(x_0)$  term, because they are suppressed by additional powers of  $(x - x_0)$ . So we are left with<sup>5</sup>

$$V(x) \approx \frac{1}{2}V''(x_0)(x - x_0)^2. \quad (5.19)$$

But this has exactly the same form as the Hooke's-law potential,  $V(x) = (1/2)k(x - x_0)^2$ , provided that we let  $V''(x_0)$  be our “spring constant”  $k$ . Equivalently, the force is  $F = -dV/dx = -V''(x_0)(x - x_0) \equiv -k(x - x_0)$ . The frequency of small oscillations,  $\omega = \sqrt{k/m}$ , is therefore

$$\omega = \sqrt{\frac{V''(x_0)}{m}}. \quad (5.20)$$

<sup>5</sup> Even if  $V'''(x_0)$  is much larger than  $V''(x_0)$ , we can always pick  $(x - x_0)$  small enough so that the third-order term is negligible. The one case where this is not true is when  $V''(x_0) = 0$ . But the result in Eq. (5.20) is still valid in this case. The frequency  $\omega$  just happens to be zero, in the limit of infinitesimal oscillations.

![Figure 5.3: A graph of potential energy V(x) versus position x. The curve starts at a high value for small positive x, crosses the x-axis, reaches a minimum, and then asymptotically approaches the x-axis from above as x increases.](41c354be5fdbdb4f0fc864d4ea9d3363_img.jpg)

Figure 5.3: A graph of potential energy V(x) versus position x. The curve starts at a high value for small positive x, crosses the x-axis, reaches a minimum, and then asymptotically approaches the x-axis from above as x increases.

Fig. 5.3

**Example:** A particle moves under the influence of the potential  $V(x) = A/x^2 - B/x$ , where  $A, B > 0$ . Find the frequency of small oscillations around the equilibrium point. This potential is relevant to planetary motion, as we'll see in Chapter 7. The rough shape is shown in Fig. 5.3.

**Solution:** The first thing we need to do is calculate the equilibrium point  $x_0$ . The minimum occurs where

$$0 = V'(x) = -\frac{2A}{x^3} + \frac{B}{x^2} \implies x = \frac{2A}{B} \equiv x_0. \quad (5.21)$$

The second derivative of  $V(x)$  is

$$V''(x) = \frac{6A}{x^4} - \frac{2B}{x^3}. \quad (5.22)$$

Plugging in  $x_0 = 2A/B$ , we find

$$\omega = \sqrt{\frac{V''(x_0)}{m}} = \sqrt{\frac{B^4}{8mA^3}}. \quad (5.23)$$

![Figure 5.4: A graph showing a solid curve V(x) and a dashed parabola. The parabola is tangent to the solid curve at its minimum point, illustrating that the potential looks like a parabola near its minimum.](dafe1e070adde01b4d127609636af4e9_img.jpg)

Figure 5.4: A graph showing a solid curve V(x) and a dashed parabola. The parabola is tangent to the solid curve at its minimum point, illustrating that the potential looks like a parabola near its minimum.

Fig. 5.4

Equation (5.20) is an important result, because *any* function  $V(x)$  looks basically like a parabola (see Fig. 5.4) in a small enough region around a minimum (except in the special case where  $V''(x_0) = 0$ ).

A potential may look quite erratic,  
 And its study may seem problematic.  
 But down near a min,  
 You can say with a grin,  
 “It behaves like a simple quadratic!”

### 5.3 Conservation of energy in three dimensions

The concepts of work and potential energy in three dimensions are somewhat more complicated than in one dimension, but the general ideas are the same.<sup>6</sup> As in the 1-D case, we'll start with Newton's second law, which now takes the vector form,  $\mathbf{F} = m\mathbf{a}$ . And as in the 1-D case, we'll deal only with forces that depend only on position, that is,  $\mathbf{F} = \mathbf{F}(\mathbf{r})$ , because these are the only ones that have any chance of being conservative. The  $\mathbf{F} = m\mathbf{a}$  vector equation is shorthand for three equations analogous to Eq. (5.1), namely  $mv_x(dv_x/dx) = F_x$ , and likewise for  $y$  and  $z$ . The  $F_x$  here is a function of position, so we should really be writing

<sup>6</sup> We'll invoke a few results from vector calculus here. If you haven't seen such material before, a brief review is given in Appendix B.

$F_x(x, y, z)$ , but we'll drop the arguments, lest our expressions get too cluttered. Multiplying through by  $dx$ , etc., in these three equations, and then adding them together gives

$$F_x dx + F_y dy + F_z dz = m(v_x dv_x + v_y dv_y + v_z dv_z). \quad (5.24)$$

The left-hand side is the work done on the particle. With  $d\mathbf{r} \equiv (dx, dy, dz)$ , this work can be written as  $\mathbf{F} \cdot d\mathbf{r}$  (see Appendix B for the definition of the “dot product”). Using Eq. (B.2), we see that the work can also be written as  $F|d\mathbf{r}| \cos \theta$ , where  $\theta$  is the angle between  $\mathbf{F}$  and  $d\mathbf{r}$ . Grouping this as  $(F \cos \theta)|d\mathbf{r}|$  shows that the work equals the distance moved times the component of the force along the displacement. Alternatively, grouping it as  $F(|d\mathbf{r}| \cos \theta)$  shows that the work also equals the magnitude of the force times the component of the displacement in the direction of the force.

Integrating Eq. (5.24) from the point  $(x_0, y_0, z_0)$  to the point  $(x, y, z)$  yields<sup>7</sup>

$$E + \int_{x_0}^x F_x dx' + \int_{y_0}^y F_y dy' + \int_{z_0}^z F_z dz' = \frac{1}{2}m(v_x^2 + v_y^2 + v_z^2) = \frac{1}{2}mv^2, \quad (5.25)$$

where  $E$  is a constant of integration; it equals  $mv_0^2/2$ , where  $v_0$  is the speed at  $(x_0, y_0, z_0)$ . Note that the integrations on the left-hand side depend on the path in 3-D space that the particle takes in going from  $(x_0, y_0, z_0)$  to  $(x, y, z)$ , because the components of  $\mathbf{F}$  are functions of position. We'll address this issue below. In terms of the dot product, Eq. (5.25) can be written in the more compact form,

$$\frac{1}{2}mv^2 - \int_{\mathbf{r}_0}^{\mathbf{r}} \mathbf{F}(\mathbf{r}') \cdot d\mathbf{r}' = E. \quad (5.26)$$

Therefore, if we define the potential energy  $V(\mathbf{r})$  as

$$V(\mathbf{r}) \equiv - \int_{\mathbf{r}_0}^{\mathbf{r}} \mathbf{F}(\mathbf{r}') \cdot d\mathbf{r}', \quad (5.27)$$

then we can write

$$\frac{1}{2}mv^2 + V(\mathbf{r}) = E. \quad (5.28)$$

In other words, the sum of the kinetic energy and potential energy is constant.

<sup>7</sup> We've put primes on the integration variables so that we don't confuse them with the limits of integration. And as mentioned above,  $F_x$  is really  $F_x(x', y', z')$ , etc.

#### ***Conservative forces in three dimensions***

For a force that depends only on position (as we have been assuming), there is one complication that arises in 3-D that we didn't have to worry about in 1-D. In 1-D, there is only one route that goes from  $x_0$  to  $x$ . The motion itself may involve speeding up or slowing down, or backtracking, but the path is always restricted to be along the line containing  $x_0$  and  $x$ . But in 3-D, there is an infinite number of routes that go from  $\mathbf{r}_0$  to  $\mathbf{r}$ . In order for the potential  $V(\mathbf{r})$  to have any meaning and to be of any use, it must be well defined. That is, it must be path-independent. As in the 1-D case, we call the force associated with such a potential a *conservative force*. Let's now see what types of 3-D forces are conservative.

**Theorem 5.2** *Given a force  $\mathbf{F}(\mathbf{r})$ , a necessary and sufficient condition for the potential,*

$$V(\mathbf{r}) \equiv - \int_{\mathbf{r}_0}^{\mathbf{r}} \mathbf{F}(\mathbf{r}') \cdot d\mathbf{r}', \tag{5.29}$$

*to be well defined (that is, to be path-independent) is that the curl of  $\mathbf{F}$  is zero everywhere (that is,  $\nabla \times \mathbf{F} = \mathbf{0}$ ; see Appendix B for the definition of the curl).*<sup>8</sup>

**Proof:** First, let us show that  $\nabla \times \mathbf{F} = \mathbf{0}$  is a necessary condition for path-independence. In other words, "If  $V(\mathbf{r})$  is path-independent, then  $\nabla \times \mathbf{F} = \mathbf{0}$ ." This follows quickly from the discussion of the curl in Appendix B. We show in Eq. (B.24) that the integral  $\int \mathbf{F} \cdot d\mathbf{r}$  (that is, the work done) around a little rectangle in the  $x$ - $y$  plane equals the  $z$  component of the curl times the area. If the work done in going from corner  $A$  to corner  $B$  in Fig. 5.5 is the same for paths "1" and "2" (as we are assuming), then the round-trip integral around the rectangle is zero, because one of the paths is being traced out backwards, so it cancels the contribution from the other path. So path-independence implies that the round-trip integral  $\int \mathbf{F} \cdot d\mathbf{r}$  is zero for any arbitrary rectangle in the  $x$ - $y$  plane. Equation (B.24) therefore says that the  $z$  component of the curl must be zero everywhere. Likewise for the  $y$  and  $x$  components. We have therefore shown that  $\nabla \times \mathbf{F} = \mathbf{0}$  is a necessary condition for path independence.

Now let us show that it is sufficient. In other words, "If  $\nabla \times \mathbf{F} = \mathbf{0}$ , then  $V(\mathbf{r})$  is path-independent." The proof of sufficiency follows immediately from Stokes' theorem, which is stated in Eq. (B.25). This theorem implies that if  $\nabla \times \mathbf{F} = \mathbf{0}$  everywhere, then  $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$  for any closed curve. But Fig. 5.6 shows that traversing the loop  $C$  counterclockwise entails traversing path "1" in the "forward" direction, and then traversing path "2" in the "backward" direction. Therefore, from the same reasoning as in the previous paragraph, the integrals

![Diagram for Fig. 5.5 showing a rectangle in the x-y coordinate plane with bottom-left corner A and top-right corner B. Path 1 goes along the bottom and right edges from A to B with an arrow, and Path 2 goes along the left and top edges from A to B with an arrow.](0cb0bad3471991281dab94abf60ff91f_img.jpg)

Diagram for Fig. 5.5 showing a rectangle in the x-y coordinate plane with bottom-left corner A and top-right corner B. Path 1 goes along the bottom and right edges from A to B with an arrow, and Path 2 goes along the left and top edges from A to B with an arrow.

**Fig. 5.5**

![Diagram for Fig. 5.6 showing an arbitrary closed surface S bounded by a loop C with counterclockwise orientation arrows. Points r_0 and r are shown on the boundary, with path 1 traversing the bottom part and path 2 traversing the top part.](e40699ae16db097a5e8d3cb8ab70b071_img.jpg)

Diagram for Fig. 5.6 showing an arbitrary closed surface S bounded by a loop C with counterclockwise orientation arrows. Points r\_0 and r are shown on the boundary, with path 1 traversing the bottom part and path 2 traversing the top part.

**Fig. 5.6**

<sup>8</sup> If the force is infinite at any point, then the proof of sufficiency below (which is based on Stokes' theorem) isn't valid, and it turns out that a second condition is required; see Feng (1969). But we won't worry about that here.

from  $\mathbf{r}_0$  to  $\mathbf{r}$  along paths “1” and “2” are equal. This holds for arbitrary points  $\mathbf{r}_0$  and  $\mathbf{r}$ , and arbitrary curves  $C$ , so  $V(\mathbf{r})$  is path-independent. ■

REMARK: Another way to show that  $\nabla \times \mathbf{F} = 0$  is a necessary condition for path-independence (that is, “If  $V(\mathbf{r})$  is path-independent, then  $\nabla \times \mathbf{F} = 0$ ”) is the following. If  $V(\mathbf{r})$  is path-independent (and therefore well defined), then it is legal to write down the differential form of Eq. (5.27), namely

$$dV(\mathbf{r}) = -\mathbf{F}(\mathbf{r}) \cdot d\mathbf{r} \equiv -(F_x dx + F_y dy + F_z dz). \quad (5.30)$$

But another expression for  $dV$  is

$$dV(\mathbf{r}) = \frac{\partial V}{\partial x} dx + \frac{\partial V}{\partial y} dy + \frac{\partial V}{\partial z} dz. \quad (5.31)$$

These two expressions must be equivalent for arbitrary  $dx$ ,  $dy$ , and  $dz$ . So we have

$$(F_x, F_y, F_z) = -\left(\frac{\partial V}{\partial x}, \frac{\partial V}{\partial y}, \frac{\partial V}{\partial z}\right) \implies \mathbf{F}(\mathbf{r}) = -\nabla V(\mathbf{r}). \quad (5.32)$$

In other words, the force is the gradient of the potential. Therefore,

$$\nabla \times \mathbf{F} = -\nabla \times \nabla V(\mathbf{r}) = 0, \quad (5.33)$$

because the curl of a gradient is identically zero, as you can verify by using the definition of the curl in Eq. (B.20) and the fact that partial differentiation is commutative (that is,  $\partial^2 V / \partial x \partial y = \partial^2 V / \partial y \partial x$ ). ♣

**Example (Central force):** A *central force* is defined to be a force that points radially and whose magnitude depends only on  $r$ . That is,  $\mathbf{F}(\mathbf{r}) = F(r)\hat{\mathbf{r}}$ . Show that a central force is conservative by explicitly showing that  $\nabla \times \mathbf{F} = \mathbf{0}$ .

**Solution:** The force  $\mathbf{F}$  may be written as

$$\mathbf{F}(x, y, z) = F(r)\hat{\mathbf{r}} = F(r)\left(\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right). \quad (5.34)$$

Now, as you can verify,

$$\frac{\partial r}{\partial x} = \frac{\partial \sqrt{x^2 + y^2 + z^2}}{\partial x} = \frac{x}{r}, \quad (5.35)$$

and similarly for  $y$  and  $z$ . Therefore, the  $z$  component of  $\nabla \times \mathbf{F}$  equals (writing  $F$  for  $F(r)$ , and  $F'$  for  $dF(r)/dr$ , and making use of the chain rule)

$$\begin{aligned} \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} &= \frac{\partial(yF/r)}{\partial x} - \frac{\partial(xF/r)}{\partial y} \\ &= \left(\frac{y}{r}F' \frac{\partial r}{\partial x} - yF \frac{1}{r^2} \frac{\partial r}{\partial x}\right) - \left(\frac{x}{r}F' \frac{\partial r}{\partial y} - xF \frac{1}{r^2} \frac{\partial r}{\partial y}\right) \\ &= \left(\frac{yxF'}{r^2} - \frac{yxF}{r^3}\right) - \left(\frac{xyF'}{r^2} - \frac{xyF}{r^3}\right) = 0. \end{aligned} \quad (5.36)$$

Likewise for the  $x$  and  $y$  components.

## 5.4 Gravity

#### 5.4.1 Newton's universal law of gravitation

The gravitational force on a point mass  $m$ , located a distance  $r$  from a point mass  $M$ , is given by Newton's law of gravitation,

$$F(r) = \frac{-GMm}{r^2}, \quad (5.37)$$

where the minus sign indicates an attractive force. The numerical value of  $G$  is  $6.67 \cdot 10^{-11} \text{ m}^3/(\text{kg s}^2)$ . We'll show how this value is obtained in Section 5.4.2 below.

What is the force if we replace the point mass  $M$  by a sphere of radius  $R$  and mass  $M$ ? The answer (assuming that the sphere is spherically symmetric, that is, the density is a function only of  $r$ ) is that it is still  $-GMm/r^2$ . A sphere acts just like a point mass at its center, for the purposes of gravity (as long as we're considering a mass  $m$  outside the sphere). This is an extremely pleasing result, to say the least. If it were not the case, then the universe would be a far more complicated place than it is. In particular, the motion of planets and such things would be much harder to describe.

To demonstrate that spheres behave like points, as far as gravity is concerned, it turns out to be much easier to calculate the potential energy due to a sphere, and to then take the derivative to obtain the force, rather than to calculate the force explicitly.<sup>9</sup> So this is the route we will take. It will suffice to demonstrate the result for a thin spherical shell, because a sphere is the sum of many such shells. Our strategy for calculating the potential energy at a point  $P$ , due to a spherical shell, will be to slice the shell into rings as shown in Fig. 5.7. Let the radius of the shell be  $R$ , let  $P$  be a distance  $r$  from the center of the shell, and let the ring make the angle  $\theta$  shown. The distance,  $\ell$ , from  $P$  to the ring is a function of  $R$ ,  $r$ , and  $\theta$ . It may be found as follows. In Fig. 5.8, segment  $AB$  has length  $R \sin \theta$ , and segment  $BP$  has length  $r - R \cos \theta$ . So the length  $\ell$  in triangle  $ABP$  is

$$\ell = \sqrt{(R \sin \theta)^2 + (r - R \cos \theta)^2} = \sqrt{R^2 + r^2 - 2rR \cos \theta}. \quad (5.38)$$

What we've done here is just prove the law of cosines.

The area of a ring between  $\theta$  and  $\theta + d\theta$  is its width (which is  $R d\theta$ ) times its circumference (which is  $2\pi R \sin \theta$ ). Letting  $\sigma = M/(4\pi R^2)$  be the mass density per unit area of the shell, we see that the potential energy of a mass  $m$  at  $P$  due to a thin ring is  $-Gm\sigma(R d\theta)(2\pi R \sin \theta)/\ell$ . This is true because the gravitational potential energy,

$$V(\ell) = \frac{-Gm_1 m_2}{\ell}, \quad (5.39)$$

<sup>9</sup> The reason for this is that the potential energy is a scalar quantity (just a number), whereas the force is a vector. If we tried to calculate the force, we would have to worry about forces pointing in all sorts of directions. With the potential energy, we simply have to add up a bunch of numbers.

![Figure 5.7: A diagram showing a spherical shell of radius R and a point P at a distance r from the center. A ring on the shell is defined by an angle theta from the horizontal axis. The distance from P to the ring is labeled l. The horizontal distance from the center to the ring is R cos theta.](644048a5a07ca66e606893efefb22679_img.jpg)

Figure 5.7: A diagram showing a spherical shell of radius R and a point P at a distance r from the center. A ring on the shell is defined by an angle theta from the horizontal axis. The distance from P to the ring is labeled l. The horizontal distance from the center to the ring is R cos theta.

Fig. 5.7

![Figure 5.8: A right-angled triangle ABP. Vertex A is on the spherical shell, B is on the horizontal axis, and P is the external point. AB is the radius R, BP is the distance r - R cos theta, and AP is the distance l. The angle at A is theta, and the angle at B is 90 degrees. The length of AB is R sin theta.](df79f4ee9493c64912adc07c2be43969_img.jpg)

Figure 5.8: A right-angled triangle ABP. Vertex A is on the spherical shell, B is on the horizontal axis, and P is the external point. AB is the radius R, BP is the distance r - R cos theta, and AP is the distance l. The angle at A is theta, and the angle at B is 90 degrees. The length of AB is R sin theta.

Fig. 5.8

is a scalar quantity, so the contributions from the little mass pieces simply add. Every piece of the ring is the same distance from  $P$ , and this distance is all that matters; the direction from  $P$  is irrelevant (unlike it would be with the force). The total potential energy at  $P$  is therefore

$$\begin{aligned} V(r) &= - \int_0^\pi \frac{2\pi\sigma GR^2 m \sin\theta \, d\theta}{\sqrt{R^2 + r^2 - 2rR \cos\theta}} \\ &= - \frac{2\pi\sigma GRm}{r} \sqrt{R^2 + r^2 - 2rR \cos\theta} \Big|_0^\pi. \end{aligned} \quad (5.40)$$

The  $\sin\theta$  in the numerator is what makes this integral nice and doable. We must now consider two cases. If  $r > R$ , then we have

$$V(r) = - \frac{2\pi\sigma GRm}{r} \left( (r+R) - (r-R) \right) = - \frac{G(4\pi R^2\sigma)m}{r} = - \frac{GMm}{r}, \quad (5.41)$$

which is the potential due to a point mass  $M$  located at the center of the shell, as desired. If  $r < R$ , then we have

$$V(r) = - \frac{2\pi\sigma GRm}{r} \left( (r+R) - (R-r) \right) = - \frac{G(4\pi R^2\sigma)m}{R} = - \frac{GMm}{R}, \quad (5.42)$$

which is independent of  $r$ . Having found  $V(r)$ , we can now find  $F(r)$  by taking the negative of the gradient of  $V$ . The gradient is just  $\hat{\mathbf{r}}(d/dr)$  here, because  $V$  is a function only of  $r$ . Therefore,

$$\begin{aligned} F(r) &= - \frac{GMm}{r^2}, \quad \text{if } r > R, \\ F(r) &= 0, \quad \text{if } r < R. \end{aligned} \quad (5.43)$$

These forces are directed radially, of course. A solid sphere is the sum of many spherical shells, so if  $P$  is outside a given sphere, then the force at  $P$  is  $-GMm/r^2$ , where  $M$  is the total mass of the sphere. This result holds even if the shells have different mass densities (but each one must have uniform density). Note that the gravitational force between two spheres is the same as if they were both replaced by point masses. This follows from two applications of our “point mass” result.

Newton looked at the data, numerical,  
And then observations, empirical.  
He said, “But, of course,  
We get the same force  
From a point mass and something that’s spherical!”

If  $P$  is inside a given sphere, then the only relevant material is the mass inside a concentric sphere through  $P$ , because all the shells outside this region give zero

![Figure 5.9: A diagram of a sphere with a point P on its surface. Two lines are drawn from P to the sphere's boundary, illustrating the geometry of a spherical shell. The lines represent the paths of light or force from P to the edges of a small segment of the shell.](4d0e0cdbf7e38f7f86380dfbaf3e1f43_img.jpg)

Figure 5.9: A diagram of a sphere with a point P on its surface. Two lines are drawn from P to the sphere's boundary, illustrating the geometry of a spherical shell. The lines represent the paths of light or force from P to the edges of a small segment of the shell.

Fig. 5.9

force, from the second equation in Eq. (5.43). The material “outside” of  $P$  is, for the purposes of gravity, not there.

It isn’t obvious that the force inside a spherical shell is zero. Consider the point  $P$  in Fig. 5.9. A piece of mass  $dm$  on the right side of the shell gives a larger force on  $P$  than a piece of mass  $dm$  on the left side, due to the  $1/r^2$  dependence. But from the figure, there is more mass on the left side than the right side. These two effects happen to exactly cancel, as you can show in Problem 5.10.

**Example (Supporting a tube):** Imagine the following unrealistic undertaking. Drill a narrow tube, with cross-sectional area  $A$ , from the surface of the earth down to the center. Then line the cylindrical wall of the tube with a frictionless coating. Then fill the tube back up with the dirt (and magma, etc.) that you originally removed. What force is necessary at the bottom of the tube of dirt (that is, at the center of the earth) to hold it up? Let the earth’s radius be  $R$ , and assume (incorrectly) a uniform mass density  $\rho$ .

**Solution:** The gravitational force on a mass  $dm$  at radius  $r$  is effectively due to the mass inside the radius  $r$  (call this  $M_r$ ). The mass outside  $r$  is effectively not there. The gravitational force is therefore

$$F_{dm} = \frac{GM_r dm}{r^2} = \frac{G((4/3)\pi r^3 \rho) dm}{r^2} = \frac{4}{3}\pi G \rho r dm, \quad (5.44)$$

which we see increases linearly with  $r$ . The dirt in the tube between  $r$  and  $r + dr$  has volume  $A dr$ , so its mass is  $dm = \rho A dr$ . The total gravitational force on the entire tube is therefore

$$\begin{aligned} F &= \int F_{dm} = \int_0^R \frac{4}{3}\pi G \rho r (\rho A dr) = \frac{4}{3}\pi G \rho^2 A \int_0^R r dr \\ &= \frac{4}{3}\pi G \rho^2 A \cdot \frac{R^2}{2} = \frac{2}{3}\pi G \rho^2 A R^2. \end{aligned} \quad (5.45)$$

The force at the bottom of the tube must be equal and opposite to this force. In terms of the mass of the earth,  $M_E = (4/3)\pi R^3 \rho$ , and the total mass of the tube,  $M_t = \rho A R$ , this result can be written as  $F = GM_E M_t / 2R^2$ . So the required force is half of what a scale on the surface of the earth would read if all of the tube’s dirt sat in a lump on top of it. The reason for this is basically that the force in Eq. (5.44) is linear in  $r$ .

An important subtopic of gravity is the *tidal force*, but because this is most easily discussed in the context of accelerating frames of reference and fictitious forces, we’ll postpone it until Chapter 10.

#### 5.4.2 The Cavendish experiment

How do we determine the numerical value of  $G$  in Eq. (5.37)? If we can produce a setup in which we know the values  $F$ ,  $M$ ,  $m$ , and  $r$ , then we can determine  $G$ .

The first strategy that comes to mind is to take advantage of the fact that the gravitational force on an object on the earth's surface is known to be  $F = mg$ . Combining this with Eq. (5.37) gives  $g = GM_E/R^2$ . We know the values of  $g$  and  $R$ ,<sup>10</sup> so this tells us what the product  $GM_E$  is. However, this information unfortunately doesn't help us, because we don't know what the mass of the earth is (without knowing  $G$  first, which we're assuming we don't know yet; see the last paragraph in this section). For all we know, the mass of the earth might be 10 times larger than what we think it is, with  $G$  being 10 times smaller. The only way to find  $G$  is to use a setup with two known masses. But this then presents the problem that the resulting force is extremely small. So the task boils down to figuring out a way to measure the tiny force between two known masses. Henry Cavendish solved this problem in 1798 by performing an extremely delicate experiment (which was devised a few years earlier by John Michell, but he died before being able to perform it).<sup>11</sup> The basic idea behind the experiment is the following.

Consider the setup in Fig. 5.10, which shows the top view. A dumbbell with two masses  $m$  on its ends hangs from a very thin wire. The dumbbell is free to twist, although if it twists, the wire will provide a tiny restoring torque.<sup>12</sup> The dumbbell starts with no twist in the wire, and then two other masses  $M$  are placed (fixed) at the positions shown. These masses produce attractive forces on the dumbbell masses and cause the dumbbell to twist counterclockwise. The dumbbell will oscillate back and forth before finally settling down at some tiny angle  $\theta$  away from the initial position.

The torque on the dumbbell that arises from the twist in the wire takes the form of  $\tau = -b\theta$  (with counterclockwise torque taken to be positive), where  $b$  is a constant that depends on the thickness and makeup of the wire. This linear relation between  $\tau$  and  $\theta$  holds for small  $\theta$  for all the same reasons that the  $F = -kx$  Hooke's-law result in Section 5.2 holds.

The gravitational force between each pair of masses is  $GMm/d^2$ , where  $d$  is the separation between the centers of the masses in each pair. So the torque on the dumbbell due to the two gravitational forces is  $2(GMm/d^2)\ell$ , where  $\ell$  is half the length of the dumbbell. Demanding that the total torque on the dumbbell be zero gives

$$\frac{2GMm\ell}{d^2} - b\theta = 0 \quad \Rightarrow \quad G = \frac{b\theta d^2}{2Mm\ell}. \quad (5.46)$$

<sup>10</sup> The radius of the earth has been known (at least roughly) since the time of Eratosthenes, about 250 BC. For an interesting way to measure it yourself, see Rawlins (1979).

<sup>11</sup> The purpose of the experiment, as intended by Michell and Cavendish, was actually to measure the density of the earth, and not  $G$ ; see Clotfelter (1987). But as we'll see below, this is equivalent to measuring  $G$ .

<sup>12</sup> We won't talk about torque until Chapter 8, so you may want to come back and read this section after that. We'll invoke some results about rotational dynamics here, but the general setup should be clear even if you're not familiar with rotations.

![Diagram of the Cavendish experiment setup (top view). A dumbbell with masses m is suspended by a wire. Two fixed masses M are placed near the dumbbell, causing it to twist by an angle theta from its initial position. The wire is shown as a dashed line, and the dumbbell is shown as a solid line. The angle theta is indicated between the initial position and the current position of the dumbbell.](cf95964c5a82c2e90211071488c44d06_img.jpg)

The diagram shows a top-down view of the Cavendish torsion balance. A central horizontal line represents the 'initial position' of the dumbbell. A solid line, labeled 'dumbbell', is rotated counter-clockwise from this initial position by an angle  $\theta$ . The dumbbell has two masses,  $m$ , at its ends. Two larger, fixed masses,  $M$ , are positioned near the dumbbell's masses. One  $M$  is above and to the right of the right-hand  $m$ , and another  $M$  is below and to the left of the left-hand  $m$ . A vertical line labeled 'wire' passes through the center of the dumbbell. The text '(out of page)' is written below the wire label. The entire diagram is labeled '(top view)' at the top.

Diagram of the Cavendish experiment setup (top view). A dumbbell with masses m is suspended by a wire. Two fixed masses M are placed near the dumbbell, causing it to twist by an angle theta from its initial position. The wire is shown as a dashed line, and the dumbbell is shown as a solid line. The angle theta is indicated between the initial position and the current position of the dumbbell.

Fig. 5.10

We know all the parameters on the right-hand side except  $b$ , so if we can determine that, then we're done. It's very difficult to measure  $b$  directly with any reasonable accuracy, because the torque in the wire is so tiny. But fortunately there's a sneaky way to determine  $b$  that involves taking a page from our playbook on oscillations. The bread-and-butter equation for rotations is  $\tau = I\ddot{\theta}$ , where  $I$  is the moment of inertia (which we can calculate for the dumbbell); this is the rotational analog of Newton's second law,  $F = m\ddot{x}$ . Now, if the torque takes the form of  $\tau = -b\theta$  for small  $\theta$ , then  $\tau = I\ddot{\theta}$  becomes  $-b\theta = I\ddot{\theta}$ . This is a good old simple-harmonic-oscillator equation, so we know that the frequency of the oscillations is  $\omega = \sqrt{b/I}$ . Therefore, all we need to do is measure the period,  $T = 2\pi/\omega$ , of the oscillations while the dumbbell is settling down, and we can determine  $b$  from  $b = I\omega^2 = I(2\pi/T)^2$ . (The time  $T$  is large, because  $b$  is small on the scale of things, because otherwise there wouldn't be any noticeable twist in the wire.) Plugging this value of  $b$  into Eq. (5.46) finally gives

$$G = \frac{4\pi^2 I \theta d^2}{2Mm\ell T^2}. \quad (5.47)$$

The Cavendish experiment is also known as the “weighing the earth” (or perhaps the “massing the earth”) experiment, because now that we know  $G$  (and also  $g$  and  $R$ ), we can use  $g = GM_E/R^2$  to calculate the mass of the earth,  $M_E$ . The only possible way to determine  $M_E$  (without examining every cubic meter of the inside of the earth, which is obviously impossible) is to determine  $G$  first, as we have done.<sup>13</sup> Interestingly, the resulting value of  $M_E$ , which is roughly  $6 \cdot 10^{24}$  kg, leads to an average density of the earth of about  $5.5 \text{ g/cm}^3$ . This is larger than the density of the earth's crust and mantle, so we conclude that there must be something very dense deep down inside the earth. So the Cavendish experiment, which involves masses hanging from a wire, amazingly tells us something about the earth's core!<sup>14</sup>

## 5.5 Momentum

#### 5.5.1 Conservation of momentum

Newton's third law says that for every force there is an equal and opposite force. In other words, if  $\mathbf{F}_{ab}$  is the force that particle  $a$  feels due to particle  $b$ , and if  $\mathbf{F}_{ba}$  is the force that particle  $b$  feels due to particle  $a$ , then  $\mathbf{F}_{ba} = -\mathbf{F}_{ab}$  at all times. This law has important implications concerning momentum,  $\mathbf{p} \equiv m\mathbf{v}$ . Consider two particles that interact over a period of time. Assume that they are isolated from outside forces. From Newton's second law,  $\mathbf{F} = d\mathbf{p}/dt$ , we see by integrating this that the total change in a particle's momentum equals the time

<sup>13</sup> If you want to determine  $M_E$  without using  $g$  or  $R$  (but still using  $G$ , of course, because  $M_E$  appears only through the combination  $GM_E$ ), see Celnikier (1983).

<sup>14</sup> For a comprehensive discussion of the earth's core, see Brush (1980).

integral of the force acting on it. That is,

$$\mathbf{p}(t_2) - \mathbf{p}(t_1) = \int_{t_1}^{t_2} \mathbf{F} dt. \quad (5.48)$$

This integral is called the *impulse*. If we now invoke the third law,  $\mathbf{F}_{ba} = -\mathbf{F}_{ab}$ , we find

$$\mathbf{p}_a(t_2) - \mathbf{p}_a(t_1) = \int_{t_1}^{t_2} \mathbf{F}_{ab} dt = - \int_{t_1}^{t_2} \mathbf{F}_{ba} dt = -(\mathbf{p}_b(t_2) - \mathbf{p}_b(t_1)). \quad (5.49)$$

Therefore,

$$\mathbf{p}_a(t_2) + \mathbf{p}_b(t_2) = \mathbf{p}_a(t_1) + \mathbf{p}_b(t_1). \quad (5.50)$$

This is the statement that the total momentum of this isolated system of two particles is *conserved*; it does not depend on time. Note that Eq. (5.50) is a vector equation, so it is really three equations, namely conservation of  $p_x$ ,  $p_y$ , and  $p_z$ .

REMARK: Newton's third law makes a statement about forces. But force is related to momentum via  $F = dp/dt$ . So the third law essentially *postulates* conservation of momentum. (The “proof” above in Eq. (5.49) is hardly a proof. It involves one simple integration.) So you might wonder if momentum conservation is something you can *prove*, or if it's something you have to *assume*, as we have basically done because we have simply accepted the third law.

The difference between a postulate and a theorem is rather nebulous. One person's postulate might be another person's theorem, and vice versa. You have to start *somewhere* in your assumptions. We chose to start with the third law. In the Lagrangian formalism in Chapter 6, the starting point is different, and momentum conservation is deduced as a consequence of translational invariance (as we will see). So it looks more like a theorem in that formalism.

But one thing is certain. Momentum conservation for two particles *cannot* be proved from scratch for arbitrary forces, because it is not necessarily true. For example, if two charged particles interact in a certain way through the magnetic fields they produce, then the total momentum of the two particles might *not* be conserved. Where is the missing momentum? It is carried off in the electromagnetic field. The total momentum of the system is indeed conserved, but the crucial point is that the system consists of the two particles *plus* the electromagnetic field. Said in another way, each particle actually interacts with the electromagnetic field, and not the other particle. Newton's third law does not necessarily hold for particles subject to such a force. ♣

Let's now look at momentum conservation for a system of many particles. As above, let  $\mathbf{F}_{ij}$  be the force that particle  $i$  feels due to particle  $j$ . Then  $\mathbf{F}_{ij} = -\mathbf{F}_{ji}$  at all times. Assume that the particles are isolated from outside forces. The change in momentum of the  $i$ th particle from  $t_1$  to  $t_2$  is (we won't bother writing all the  $t$ 's in the expressions below)

$$\Delta \mathbf{p}_i = \int \left( \sum_j \mathbf{F}_{ij} \right) dt. \quad (5.51)$$

Therefore, the change in the total momentum of all the particles is (switching the order of the integration and the sum over  $i$  on the right-hand side here)

$$\Delta \mathbf{P} \equiv \sum_i \Delta \mathbf{p}_i = \int \left( \sum_i \sum_j \mathbf{F}_{ij} \right) dt. \quad (5.52)$$

But  $\sum_i \sum_j \mathbf{F}_{ij} = 0$  at all times, because for every term  $\mathbf{F}_{ab}$  there is a term  $\mathbf{F}_{ba}$ , and  $\mathbf{F}_{ab} + \mathbf{F}_{ba} = 0$  (and also,  $\mathbf{F}_{aa} = 0$ ). The forces all cancel in pairs. Therefore, the total momentum of an isolated system of particles is conserved.

---

**Example (Snow on a sled):** You are riding on a sled that is given an initial push and slides across frictionless ice. Snow is falling vertically (in the frame of the ice) on the sled. Assume that the sled travels in tracks that constrain it to move in a straight line. Which of the following three strategies causes the sled to move the fastest? The slowest?

- A: You sweep the snow off the sled so that it leaves the sled in the direction perpendicular to the sled's tracks, as seen by you in the frame of the sled.
- B: You sweep the snow off the sled so that it leaves the sled in the direction perpendicular to the sled's tracks, as seen by someone in the frame of the ice.
- C: You do nothing.

**First solution:** The sideways motion of the snow after you sweep it off is irrelevant, because although Newton's third law says that the swept snow applies a sideways force on the sled, the normal force from the tracks keeps the sled from sliding off the tracks. Also, the vertical motion of the snow when it hits the sled is irrelevant, because the vertical normal force from the tracks keeps the sled from falling through the ground. We are therefore concerned only with the motion in the direction of the tracks. And since there are no external forces in this direction on the you/sled/snow system, the momentum in this direction is conserved.

In general, the speed of the sled can (possibly) change due to two kinds of events: (1) new snow hitting the sled (and eventually coming to rest with respect to the sled), and (2) snow being swept off the sled.

Let's first compare *A* with *C*. In strategy *A*, your sweeping action doesn't change the speed of the sled, because you are sweeping the snow directly sideways in your frame. Since the sideways motion of the snow is irrelevant as far as the forward momentum goes, you are essentially just reaching out and plopping a ball of snow on the ice. This snow then simply travels along next to the sled at the same speed; it might as well be connected to the sled (at least for a moment, until new snow hits the sled). In strategy *C*, your (non) action obviously don't change the speed of the sled. So in comparing *A* with *C*, the departure of snow doesn't differentiate them. We therefore need only consider what happens to the sled when new snow hits it. But this is easy to do: Since the sled is heavier in *C* than in *A*, a new snowflake slows it down less in *C* than in *A*. Therefore, *C* is faster than *A*.

Now let's compare *B* with *C*. *B* is faster than *C* because in *B* the snowflakes have zero forward momentum in the end, whereas in *C* they have nonzero forward momentum (because they are sitting on the moving sled). The momenta of the two systems must be the same (equal to the initial momentum of the sled plus you), so the sled must be moving faster in *B*.

Therefore, *B* is faster than *C*, which is faster than *A*. As a consistency check, it's easy to see that *B* is faster than *A*, because in *B* you must push the snow backward with

respect to the sled. So by Newton's third law, the swept snow in  $B$  exerts a forward force on the sled.

**Second solution:** In the end, this solution is basically the same as the first one, but it's a slightly more systematic way of looking at things: In  $B$ , all the snow is moving *slower* than the sled; in fact, it is all at rest (at least in the forward direction) with respect to the ice. In  $C$ , all the snow is *on* the sled. And in  $A$ , all the snow is moving *faster* than the sled; it is moving along with various forward speeds, ranging from the initial speed of the sled down to the present speed, depending on when it was swept off.

By conservation of momentum, the total momentum of the sled (including you) plus the snow at any given time is the same in all three cases. The only consistent way to combine the facts in the previous paragraph with conservation of momentum is for the speed of the sled to satisfy  $B > C > A$ . This is true because if someone claimed that  $C > B$ , then the slowest object (namely everything, since all the snow is on the sled) in  $C$  would be going faster than the fastest object (the sled) in  $B$ ; this would contradict the fact that the momenta of the two systems are equal. Therefore, we must have  $B > C$ . Likewise, if someone claimed that  $A > C$ , then the slowest object (the sled) in  $A$  would be going faster than the fastest object (everything) in  $C$ ; this would again be a contradiction. Therefore, we must have  $C > A$ . Putting these together gives  $B > C > A$ . See Exercise 5.70 for a quantitative treatment of this setup.

#### 5.5.2 Rocket motion

The quantitative application of momentum conservation can get a little tricky when the mass  $m$  is allowed to vary. Such is the case with rockets, because most of their mass consists of fuel which is eventually ejected.

Let mass be ejected backward with (constant) speed  $u$  relative to the rocket.<sup>15</sup> Since  $u$  is a speed here, it is defined to be positive. This means that the velocity of the ejected particles is obtained by subtracting  $u$  from the velocity of the rocket. Let the rocket have initial mass  $M$ , and let  $m$  be the (changing) mass at a later time. Then the rate of change of the rocket's mass is  $dm/dt$ , which is negative. So mass is ejected at a rate  $|dm/dt| = -dm/dt$ , which is positive. In other words, during a small time  $dt$ , a negative mass  $dm$  gets added to the rocket, and a positive mass  $(-dm)$  gets shot out the back. (If you wanted, you could define  $dm$  to be positive, and then *subtract* it from the rocket's mass, and have  $dm$  get shot out the back. Either way is fine.) It may sound silly, but the hardest thing about rocket motion is picking a sign for these quantities and sticking with it.

Consider a moment when the rocket has mass  $m$  and speed  $v$ . Then at a time  $dt$  later (see Fig. 5.11), the rocket has mass  $m + dm$  and speed  $v + dv$ , while the

![Diagram illustrating rocket motion. A rocket of mass m moves with velocity v. After a small time dt, a mass -dm is ejected backward with velocity v - u, and the rocket's mass becomes m + dm and its velocity becomes v + dv.](b76c25955ec22d26cc7d540f4eea936e_img.jpg)

The diagram shows two states of a rocket. In the top state, a rocket with mass  $m$  is moving to the right with velocity  $v$ . A downward arrow indicates the passage of time. In the bottom state, the rocket has a new mass  $m + dm$  and a new velocity  $v + dv$ . To the left of the rocket, a small rectangular block represents the ejected mass, labeled  $-dm$ . This ejected mass is moving to the right with a velocity  $v - u$ , where  $u$  is the exhaust speed relative to the rocket.

Diagram illustrating rocket motion. A rocket of mass m moves with velocity v. After a small time dt, a mass -dm is ejected backward with velocity v - u, and the rocket's mass becomes m + dm and its velocity becomes v + dv.

Fig. 5.11

<sup>15</sup> Just to emphasize,  $u$  is the speed with respect to the rocket. It wouldn't make sense to say "relative to the ground," because the rocket's engine shoots out the matter relative to itself, and the engine has no way of knowing how fast the rocket is moving with respect to the ground.

exhaust has mass  $(-dm)$  and speed  $v - u$  (which may be positive or negative, depending on the relative sizes of  $v$  and  $u$ ). There are no external forces, so the total momentum at each of these times must be equal. Therefore,

$$mv = (m + dm)(v + dv) + (-dm)(v - u). \quad (5.53)$$

Ignoring the second-order term  $dm\,dv$ , this simplifies to  $m\,dv = -u\,dm$ . Dividing by  $m$  and integrating from  $t_1$  to  $t_2$  gives

$$\int_{v_1}^{v_2} dv = - \int_{m_1}^{m_2} u \frac{dm}{m} \implies v_2 - v_1 = u \ln \frac{m_1}{m_2}. \quad (5.54)$$

For the case where the initial mass is  $M$  and the initial speed is 0, we have  $v = u \ln(M/m)$ . Note that we haven't assumed anything about  $dm/dt$  in this derivation. There is no need for it to be constant; it can change in any way it wants. The only thing that matters (assuming that  $M$  and  $u$  are given) is the final mass  $m$ . In the special case where  $dm/dt$  happens to be constant (call it  $-\eta$ , where  $\eta$  is positive), we have  $v(t) = u \ln[M/(M - \eta t)]$ .

The log in the result in Eq. (5.54) is not very encouraging. If the mass of the metal in the rocket is  $m$ , and if the mass of the fuel is  $9m$ , then the final speed is only  $u \ln 10 \approx (2.3)u$ . If the mass of the fuel is increased by a factor of 11 up to  $99m$  (which is probably not even structurally possible, given the amount of metal required to hold it),<sup>16</sup> then the final speed only doubles to  $u \ln 100 = 2(u \ln 10) \approx (4.6)u$ . How do you make a rocket go significantly faster? Exercise 5.69 deals with this question.

**REMARK:** If you want, you can solve this rocket problem by using force instead of conservation of momentum. If a chunk of mass  $(-dm)$  is ejected out the back, then its momentum changes by  $u\,dm$  (which is negative). Therefore, because force equals the rate of change in momentum, the force on this chunk is  $u\,dm/dt$ . By Newton's third law, the remaining part of the rocket then feels a force of  $-u\,dm/dt$  (which is positive). This force accelerates the remaining part of the rocket, so  $F = ma$  gives  $-u\,dm/dt = m\,dv/dt$ ,<sup>17</sup> which is equivalent to the  $m\,dv = -u\,dm$  result above.

We see that this rocket problem can be solved by using either force or conservation of momentum. In the end, these two strategies are really the same, because the latter was derived from  $F = dp/dt$ . But the philosophies behind the approaches are somewhat different. The choice of strategy depends on personal preference. In an isolated system such as a rocket, conservation of momentum is usually simpler. But in a problem involving an external force, you have to use  $F = dp/dt$ . You'll get lots of practice with  $F = dp/dt$  in the problems for this section and also in Section 5.8. Note that we used both  $F = dp/dt$  and  $F = ma$  in this second solution to the rocket problem. For further discussion of which expression to use in a given situation, see Appendix C. ♣

<sup>16</sup> The space shuttle's external fuel tank, just by itself, has a fuel-to-container mass ratio of only about 20.

<sup>17</sup> Whether we use  $m$  or  $m + dm$  here for the mass of the rocket doesn't matter. Any differences are of second order.

## 5.6 The center of mass frame

#### 5.6.1 Definition

When talking about momentum, it is understood that a certain frame of reference has been chosen. After all, the velocities of the particles have to be measured with respect to some coordinate system. Any inertial (that is, nonaccelerating) frame is legal to pick, but we will see that there is one particular reference frame that is often advantageous to use.

Consider a frame  $S$  and another frame  $S'$  that moves at constant velocity  $\mathbf{u}$  with respect to  $S$  (see Fig. 5.12). Given a system of particles, the velocity of the  $i$ th particle in  $S$  is related to its velocity in  $S'$  by

$$\mathbf{v}_i = \mathbf{v}'_i + \mathbf{u}. \quad (5.55)$$

This relation implies that if momentum is conserved during a collision in frame  $S'$ , then it is also conserved in frame  $S$ . This is true because both the initial and final momenta of the system in  $S$  are increased by the same amount,  $(\sum m_i)\mathbf{u}$ , compared with what they are in  $S'$ .<sup>18</sup>

Let us therefore consider the unique frame in which the total momentum of a system of particles is zero. This is called the *center of mass frame*, or CM frame. If the total momentum is  $\mathbf{P} \equiv \sum m_i \mathbf{v}_i$  in frame  $S$ , then the CM frame is the frame  $S'$  that moves with velocity

$$\mathbf{u} = \frac{\mathbf{P}}{M} \equiv \frac{\sum m_i \mathbf{v}_i}{M} \quad (5.56)$$

with respect to  $S$ , where  $M \equiv \sum m_i$  is the total mass. This follows from using Eq. (5.55) to write

$$\mathbf{P}' = \sum m_i \mathbf{v}'_i = \sum m_i \left( \mathbf{v}_i - \frac{\mathbf{P}}{M} \right) = \mathbf{P} - \mathbf{P} = \mathbf{0}. \quad (5.57)$$

The CM frame is extremely useful. Physical processes are generally much more symmetrical in this frame, and this makes the results more transparent. The CM frame is sometimes called the “zero momentum” frame. But the “center of mass” name is commonly used because the center of mass of the particles doesn’t move in the CM frame, for the following reason. The position of the center of mass is defined by

$$\mathbf{R}_{\text{CM}} \equiv \frac{\sum m_i \mathbf{r}_i}{M}. \quad (5.58)$$

<sup>18</sup> Alternatively, nowhere in our earlier derivation of momentum conservation did we say what frame we were using. We assumed only that the frame wasn’t accelerating. If it were accelerating, then  $\mathbf{F}$  would *not* equal  $m\mathbf{a}$ . We will see in Chapter 10 how  $\mathbf{F} = m\mathbf{a}$  is modified in a noninertial frame. But there’s no need to worry about that here.

![Diagram showing two coordinate systems, S and S', with S' moving at velocity u relative to S.](0722a6baa573ab41ec5e32c0ad847bcf_img.jpg)

The diagram illustrates two Cartesian coordinate systems,  $S$  and  $S'$ . System  $S$  has horizontal and vertical axes labeled  $x$  and  $y$ . System  $S'$  has horizontal and vertical axes labeled  $x'$  and  $y'$ . The origin of  $S'$  is located at a point in the first quadrant of  $S$ . A vector  $\mathbf{u}$  is shown originating from the origin of  $S$  and pointing towards the origin of  $S'$ , representing the constant velocity of  $S'$  relative to  $S$ .

Diagram showing two coordinate systems, S and S', with S' moving at velocity u relative to S.

Fig. 5.12

This is the location of the pivot upon which a rigid system would balance, as we'll see in Chapter 8. The fact that the CM doesn't move with respect to the CM frame follows from the fact that the derivative of  $\mathbf{R}_{\text{CM}}$  is the velocity of the CM frame in Eq. (5.56). The center of mass may therefore be chosen as the origin of the CM frame.

If we take two derivatives of Eq. (5.58), we obtain

$$M\mathbf{a}_{\text{CM}} \equiv \sum m_i \mathbf{a}_i = \sum \mathbf{F}_i = \mathbf{F}_{\text{total}}. \quad (5.59)$$

So as far as the acceleration of the CM goes, we can treat the system of particles like a point mass at the CM, and then just apply  $F = ma$  to this point mass. Since the internal forces cancel in pairs, we need only consider the external forces when calculating  $F_{\text{total}}$ .

Along with the CM frame, the other frame that people generally work with is the *lab frame*. There is nothing at all special about this frame. It is simply the frame (assumed to be inertial) in which the conditions of the problem are given. Any inertial frame can be called the “lab frame.” Solving problems often involves switching back and forth between the lab and CM frames. For example, if the final answer is requested in the lab frame, then you may want to transform the given information from the lab frame to the CM frame where things are more obvious, and then transform back to the lab frame to give the answer.

![Diagram of a 1D collision between two masses. A small mass m is moving to the right with velocity v, indicated by an arrow. A larger mass M is stationary to the right of m.](aa3aecec45db3606066bee2365b340fc_img.jpg)

Diagram of a 1D collision between two masses. A small mass m is moving to the right with velocity v, indicated by an arrow. A larger mass M is stationary to the right of m.

Fig. 5.13

**Example (Two masses in 1-D):** A mass  $m$  with speed  $v$  approaches a stationary mass  $M$  (see Fig. 5.13). The masses bounce off each other without any loss in total energy. What are the final velocities of the particles? Assume that the motion takes place in 1-D.

**Solution:** Doing this problem in the lab frame would require a potentially messy use of conservation of energy (see the example in Section 5.7.1). But if we work in the CM frame, things are much easier. The total momentum in the lab frame is  $mv$ , so the CM frame moves to the right with speed  $mv/(m + M) \equiv u$  with respect to the lab frame. Therefore, in the CM frame, the velocities of the two masses are

$$v_m = v - u = \frac{Mv}{m + M}, \quad \text{and} \quad v_M = 0 - u = -\frac{mv}{m + M}. \quad (5.60)$$

As a double-check, the difference in the velocities is  $v$ , and the ratio of the speeds is  $M/m$ , which makes the total momentum zero.

The important point to realize now is that in the CM frame, the two particles must simply reverse their velocities after the collision (assuming that they do indeed hit each other). This is true because the speeds must still be in the ratio  $M/m$  after the collision, in order for the total momentum to remain zero. Therefore, the speeds must either both increase or both decrease. But if they do either of these, then energy is not conserved.<sup>19</sup>

<sup>19</sup> So we *did* have to use conservation of energy in this CM-frame solution. But it was far less messy than it would have been in the lab frame.

If we now go back to the lab frame by adding the CM velocity of  $mv/(m + M)$  to the two new velocities of  $-Mv/(m + M)$  and  $mv/(m + M)$ , we obtain final lab velocities of

$$v_m = \frac{(m - M)v}{m + M}, \quad \text{and} \quad v_M = \frac{2mv}{m + M}. \quad (5.61)$$

REMARK: If  $m = M$ , then the left mass stops, and the right mass picks up a velocity of  $v$  (this should be familiar to pool players). If  $M \gg m$ , then the left mass bounces back with velocity  $\approx -v$ , and the right mass hardly moves (it's essentially a brick wall). If  $m \gg M$ , then the left mass keeps plowing along with velocity  $\approx v$ , and the right mass picks up a velocity of  $\approx 2v$ . This  $2v$  is an interesting result (it is clearer if you consider things in the frame of the heavy mass  $m$ , which is essentially the CM frame), and it leads to some neat effects, such as in Problem 5.23. ♣

#### 5.6.2 Kinetic energy

Given a system of particles, the relation between the total kinetic energy in two different frames is not very enlightening in general. But if one of the frames is the CM frame, then the relation turns out to be quite nice. Let  $S'$  be the CM frame, which moves at constant velocity  $\mathbf{u}$  with respect to another frame  $S$ . Then the velocities of the particles in the two frames are related by  $\mathbf{v}_i = \mathbf{v}'_i + \mathbf{u}$ . The kinetic energy in the CM frame is

$$K_{\text{CM}} = \frac{1}{2} \sum m_i |\mathbf{v}'_i|^2. \quad (5.62)$$

And the kinetic energy in frame  $S$  is

$$\begin{aligned} K_S &= \frac{1}{2} \sum m_i |\mathbf{v}'_i + \mathbf{u}|^2 \\ &= \frac{1}{2} \sum m_i (\mathbf{v}'_i \cdot \mathbf{v}'_i + 2\mathbf{v}'_i \cdot \mathbf{u} + \mathbf{u} \cdot \mathbf{u}) \\ &= \frac{1}{2} \sum m_i |\mathbf{v}'_i|^2 + \mathbf{u} \cdot \left( \sum m_i \mathbf{v}'_i \right) + \frac{1}{2} |\mathbf{u}|^2 \sum m_i \\ &= K_{\text{CM}} + \frac{1}{2} M u^2, \end{aligned} \quad (5.63)$$

where  $M$  is the total mass of the system, and where we have used  $\sum_i m_i \mathbf{v}'_i = 0$ , by definition of the CM frame. Therefore, the  $K$  in any frame equals the  $K$  in the CM frame, plus the  $K$  of the whole system treated like a point mass  $M$  located at the CM, which moves with velocity  $\mathbf{u}$ . An immediate corollary of this fact is that if the  $K$  is conserved in a collision in one frame (which implies that  $K_{\text{CM}}$  is conserved, because conservation of momentum says that the CM speed  $u$  is the same before and after the collision), then it is conserved in any other frame (because again, the  $u$  relevant to that frame is the same before and after the collision).

### 5.7 Collisions

There are two basic types of collisions among particles, namely *elastic* ones (in which kinetic energy is conserved), and *inelastic* ones (in which kinetic energy is lost). In any collision, the *total* energy is conserved, but in inelastic collisions some of this energy goes into the form of heat (that is, relative motion of the molecules inside the particles) instead of showing up in the net translational motion of the particles.<sup>20</sup>

We'll deal mainly with elastic collisions here, although some situations are inherently inelastic, as we'll see in Section 5.8. For inelastic collisions where it is stated that a certain fraction, say 20%, of the kinetic energy is lost, only a trivial modification to the procedure is required. To solve any elastic collision problem, we just have to write down the conservation of energy and momentum equations, and then solve for whatever variables we want to find.

#### 5.7.1 One-dimensional motion

Let's first look at one-dimensional motion. To see the general procedure, we'll solve the example from Section 5.6.1 again.

![Diagram showing a mass m moving with velocity v towards a stationary mass M.](ab9daa86203d0b410e0a01f588a2f9ca_img.jpg)

The diagram shows a small black dot representing mass  $m$  with a horizontal arrow pointing to the right, labeled with velocity  $v$ . To its right is a larger black dot representing mass  $M$ , which is stationary.

Diagram showing a mass m moving with velocity v towards a stationary mass M.

Fig. 5.14

**Example (Two masses in 1-D, again):** A mass  $m$  with speed  $v$  approaches a stationary mass  $M$  (see Fig. 5.14). The masses bounce off each other elastically. What are the final velocities of the particles? Assume that the motion takes place in 1-D.

**Solution:** Let  $v_f$  and  $V_f$  be the final velocities of the masses. Then conservation of momentum and energy give, respectively,

$$\begin{aligned} mv + 0 &= mv_f + MV_f, \\ \frac{1}{2}mv^2 + 0 &= \frac{1}{2}mv_f^2 + \frac{1}{2}MV_f^2. \end{aligned} \quad (5.64)$$

We must solve these two equations for the two unknowns  $v_f$  and  $V_f$ . Solving for  $V_f$  in the first equation and substituting into the second gives

$$\begin{aligned} mv^2 &= mv_f^2 + M \frac{m^2(v - v_f)^2}{M^2}, \\ \implies 0 &= (m + M)v_f^2 - 2mvv_f + (m - M)v^2, \\ \implies 0 &= \left( (m + M)v_f - (m - M)v \right) (v_f - v). \end{aligned} \quad (5.65)$$

One solution is  $v_f = v$ , but this isn't the one we're concerned with. It is of course a solution, because the initial conditions certainly satisfy conservation of energy and

<sup>20</sup> We'll use the terminology where "kinetic energy" refers to the overall translational energy of a particle. That is, we'll exclude heat from this definition, even though heat is just the relative kinetic energy of molecules inside a particle.

momentum with the initial conditions (a fine tautology indeed). If you want, you can view  $v_f = v$  as the solution where the particles miss each other. The fact that  $v_f = v$  is always a root can often save you a lot of quadratic-formula trouble.

The  $v_f = v(m - M)/(m + M)$  root is the one we want. Plugging this  $v_f$  back into the first of Eqs. (5.64) to obtain  $V_f$  gives

$$v_f = \frac{(m - M)v}{m + M}, \quad \text{and} \quad V_f = \frac{2mv}{m + M}, \quad (5.66)$$

in agreement with Eq. (5.61).

---

This solution was somewhat of a pain, because it involved a quadratic equation. The following theorem is extremely useful because it offers a way to avoid the hassle of quadratic equations when dealing with 1-D elastic collisions.

**Theorem 5.3** *In a 1-D elastic collision, the relative velocity of the two particles after the collision is the negative of the relative velocity before the collision.*

**Proof:** Let the masses be  $m$  and  $M$ . Let  $v_i$  and  $V_i$  be the initial velocities, and let  $v_f$  and  $V_f$  be the final velocities. Conservation of momentum and energy give

$$\begin{aligned} mv_i + MV_i &= mv_f + MV_f, \\ \frac{1}{2}mv_i^2 + \frac{1}{2}MV_i^2 &= \frac{1}{2}mv_f^2 + \frac{1}{2}MV_f^2. \end{aligned} \quad (5.67)$$

Rearranging these yields

$$\begin{aligned} m(v_i - v_f) &= M(V_f - V_i), \\ m(v_i^2 - v_f^2) &= M(V_f^2 - V_i^2). \end{aligned} \quad (5.68)$$

Dividing the second equation by the first gives  $v_i + v_f = V_i + V_f$ . Therefore,

$$v_i - V_i = -(v_f - V_f), \quad (5.69)$$

as we wanted to show. In taking the quotient of these two equations, we have lost the  $v_f = v_i$  and  $V_f = V_i$  solution. But as stated in the above example, this is the trivial solution. ■

This is a splendid theorem. It has the quadratic energy-conservation statement built into it. Hence, using this theorem along with momentum conservation (both of which are linear equations and thus easy to deal with) gives the same information as the standard combination of Eqs. (5.67). Another quick proof is the following. It is fairly easy to see that the theorem is true in the CM frame (as we argued in the example in Section 5.6.1), so it is therefore true in any frame, because it involves only differences in velocities.

#### 5.7.2 Two-dimensional motion

Let's now look at the more general case of two-dimensional motion. Three-dimensional motion is just more of the same, so we'll confine ourselves to 2-D. Everything is basically the same as in 1-D, except that there is one more momentum equation, and one more variable to solve for. This is best seen through an example.

![Diagram of an elastic collision between two identical balls of mass m. The top part shows the initial state: a ball on the left moving right with velocity v, and a stationary ball on the right. The bottom part shows the final state: the first ball is deflected at an angle theta above the horizontal dashed line with velocity v_f, and the second ball is deflected at an angle phi below the horizontal dashed line with velocity V_f.](e6f4d6cf616642378701b77ec430c917_img.jpg)

Diagram of an elastic collision between two identical balls of mass m. The top part shows the initial state: a ball on the left moving right with velocity v, and a stationary ball on the right. The bottom part shows the final state: the first ball is deflected at an angle theta above the horizontal dashed line with velocity v\_f, and the second ball is deflected at an angle phi below the horizontal dashed line with velocity V\_f.

**Fig. 5.15**

**Example (Billiards):** A billiard ball with speed  $v$  approaches an identical stationary one. The balls bounce off each other elastically, in such a way that the incoming one gets deflected by an angle  $\theta$  (see Fig. 5.15). What are the final speeds of the balls? What is the angle  $\phi$  at which the stationary ball is deflected?

**Solution:** Let  $v_f$  and  $V_f$  be the final speeds of the balls. Then conservation of  $p_x$ ,  $p_y$ , and  $E$  give, respectively,

$$\begin{aligned} mv &= mv_f \cos \theta + mV_f \cos \phi, \\ 0 &= mv_f \sin \theta - mV_f \sin \phi, \\ \frac{1}{2}mv^2 &= \frac{1}{2}mv_f^2 + \frac{1}{2}mV_f^2. \end{aligned} \quad (5.70)$$

We must solve these three equations for the three unknowns  $v_f$ ,  $V_f$ , and  $\phi$ . There are various ways to do this. Here's one. Eliminate  $\phi$  by adding the squares of the first two equations (after putting the  $v_f$  terms on the left-hand side) to obtain

$$v^2 - 2vv_f \cos \theta + v_f^2 = V_f^2. \quad (5.71)$$

Now eliminate  $V_f$  by combining this with the third equation to obtain<sup>21</sup>

$$v_f = v \cos \theta. \quad (5.72)$$

The third equation then yields

$$V_f = v \sin \theta. \quad (5.73)$$

The second equation then gives  $m(v \cos \theta) \sin \theta = m(v \sin \theta) \sin \phi$ , which implies  $\cos \theta = \sin \phi$  (or  $\theta = 0$ , which corresponds to no collision). Therefore,

$$\phi = 90^\circ - \theta. \quad (5.74)$$

In other words, the balls bounce off at right angles with respect to each other. This fact is well known to pool players. Problem 5.19 gives another (cleaner) way to demonstrate this result. Note that we needed to specify one of the four quantities,  $v_f$ ,  $V_f$ ,  $\theta$ ,  $\phi$  (we chose  $\theta$ ), because we have only three equations. Intuitively, we can't expect to solve for all four of these quantities, because we can imagine one ball hitting

<sup>21</sup> Another solution is  $v_f = 0$ . In this case,  $\phi$  must equal zero, and  $\theta$  is not well defined. This is simply the 1-D motion in the example in Section 5.6.1.

the other at various distances away from directly head-on, which will cause the balls to be deflected at various angles.

As we saw in the 1-D example in Section 5.6.1, collisions are often much easier to deal with in the CM frame. Using the same reasoning (conservation of  $p$  and  $E$ ) that we used in that example, we conclude that in 2-D (or 3-D) the final speeds of two elastically colliding particles must be the same as the initial speeds. The only degree of freedom in the CM frame is the angle of the line containing the final (oppositely directed) velocities. This simplicity in the CM frame invariably provides for a cleaner solution than the lab frame yields. A good example of this is Exercise 5.81, which gives yet another way to derive the above right-angle billiard result.

### 5.8 Inherently inelastic processes

There is a nice class of problems where the system has inherently inelastic properties, even if it doesn't appear so at first glance. In such a problem, no matter how you try to set it up, there will be inevitable kinetic energy loss that shows up in the form of heat. Total energy is conserved, of course, since heat is simply another form of energy. But the point is that if you try to write down a bunch of  $(1/2)mv^2$ 's and conserve their sum, then you're going to get the wrong answer. The following example is the classic illustration of this type of problem.

**Example (Sand on conveyor belt):** Sand drops vertically (from a negligible height) at a rate  $\sigma$  kg/s onto a moving conveyor belt.

- What force must you apply to the belt in order to keep it moving at a constant speed  $v$ ?
- How much kinetic energy does the sand gain per unit time?
- How much work do you do per unit time?
- How much energy is lost to heat per unit time?

#### Solution:

- Your force equals the rate of change in momentum. If we let  $m$  be the combined mass of the conveyor belt plus the sand on the belt, then

$$F = \frac{dp}{dt} = \frac{d(mv)}{dt} = m \frac{dv}{dt} + \frac{dm}{dt} v = 0 + \sigma v, \quad (5.75)$$

where we have used the fact that  $v$  is constant.

- The kinetic energy gained per unit time is

$$\frac{d}{dt} \left( \frac{mv^2}{2} \right) = \frac{dm}{dt} \left( \frac{v^2}{2} \right) = \frac{\sigma v^2}{2}. \quad (5.76)$$

(c) The work done by your force per unit time is

$$\frac{d(\text{Work})}{dt} = \frac{F dx}{dt} = Fv = \sigma v^2, \quad (5.77)$$

where we have used Eq. (5.75).

(d) If work is done at a rate  $\sigma v^2$ , and kinetic energy is gained at a rate  $\sigma v^2/2$ , then the “missing” energy must be lost to heat at a rate  $\sigma v^2 - \sigma v^2/2 = \sigma v^2/2$ .

---

In this example, it turned out that exactly the same amount of energy was lost to heat as was converted into kinetic energy of the sand. There is an interesting and simple way to see why this is true. In the following explanation, we’ll just deal with one particle of mass  $M$  that falls onto the conveyor belt, for simplicity.

In the lab frame, the mass gains a kinetic energy of  $Mv^2/2$  by the time it finally comes to rest with respect to the belt, because the belt moves at speed  $v$ . Now look at things in the conveyor belt’s reference frame. In this frame, the mass comes flying in with an initial kinetic energy of  $Mv^2/2$ , and then it eventually slows down and comes to rest on the belt. Therefore, all of the  $Mv^2/2$  energy is converted to heat. And since the heat is the same in both frames, this is the amount of heat in the lab frame, too.

We therefore see that in the lab frame, the equality of the heat loss and the gain in kinetic energy is a consequence of the obvious fact that the belt moves at the same rate with respect to the lab (namely  $v$ ) as the lab moves with respect to the belt (also  $v$ ).

In the solution to the above example, we did not assume anything about the nature of the friction force between the belt and the sand. The loss of energy to heat is an unavoidable result. You might think that if the sand comes to rest on the belt very “gently” (over a long period of time), then you can avoid the heat loss. This is not the case. In that scenario, the smallness of the friction force is compensated by the fact that the force must act over a very large distance. Likewise, if the sand comes to rest on the belt very abruptly, then the largeness of the friction force is compensated by the smallness of the distance over which it acts. No matter how you set things up, the work done by the friction force is the same nonzero quantity.

In other problems such as the following one, it is fairly clear that the process is inelastic. But the challenge is to correctly use  $F = dp/dt$  instead of  $F = ma$ , because  $F = ma$  will get you into trouble due to the changing mass.

---

**Example (Chain on a scale):** An “idealized” (see the comments following this example) chain with length  $L$  and mass density  $\sigma$  kg/m is held such that it hangs vertically just above a scale. It is then released. What is the reading on the scale, as a function of the height of the top of the chain?

**First solution:** Let  $y$  be the height of the top of the chain, and let  $F$  be the desired force applied by the scale. The net force on the entire chain is  $F - (\sigma L)g$ , with upward taken to be positive. The momentum of the entire chain (which just comes from the moving part) is  $(\sigma y)\dot{y}$ . Note that this is negative, because  $\dot{y}$  is negative. Equating the net force on the entire chain with the rate of change in its momentum gives

$$\begin{aligned} F - \sigma Lg &= \frac{d(\sigma y\dot{y})}{dt} \\ &= \sigma y\ddot{y} + \sigma\dot{y}^2. \end{aligned} \quad (5.78)$$

The part of the chain that is still above the scale is in free fall. Therefore,  $\ddot{y} = -g$ . And conservation of energy gives  $\dot{y} = \sqrt{2g(L-y)}$ , because the chain has fallen a distance  $L-y$ . Plugging these into Eq. (5.78) gives

$$\begin{aligned} F &= \sigma Lg - \sigma yg + 2\sigma(L-y)g \\ &= 3\sigma(L-y)g, \end{aligned} \quad (5.79)$$

which happens to be three times the weight of the chain already on the scale. This answer for  $F$  has the expected property of equaling zero when  $y = L$ , and also the interesting property of equaling  $3(\sigma L)g$  right before the last bit touches the scale. Once the chain is completely on the scale, the reading suddenly drops down to the weight of the chain, namely  $(\sigma L)g$ .

If you used conservation of energy to do this problem and assumed that all of the lost potential energy goes into the kinetic energy of the moving part of the chain, then you would obtain a speed of infinity for the last infinitesimal part of the chain to hit the scale. This is certainly incorrect, and the reason is that there is inevitable heat loss that arises when the pieces of the chain inelastically smash into the scale.

**Second solution:** The normal force from the scale is responsible for doing two things. It holds up the part of the chain that already lies on the scale, and it also changes the momentum of the atoms that are suddenly brought to rest when they hit the scale. The first of these two parts of the force is simply the weight of the chain already on the scale, which is  $F_{\text{weight}} = \sigma(L-y)g$ .

To find the second part of the force, we need to find the change in momentum,  $dp$ , of the part of the chain that hits the scale during a given time  $dt$ . The amount of mass that hits the scale in a time  $dt$  is  $dm = \sigma|dy| = \sigma|\dot{y}|dt = -\sigma\dot{y}dt$ , since  $\dot{y}$  is negative. This mass initially has velocity  $\dot{y}$ , and then it is abruptly brought to rest. Therefore, the change in its momentum is  $dp = 0 - (dm)\dot{y} = \sigma\dot{y}^2 dt$ , which is positive. The force required to cause this change in momentum is

$$F_{dp/dt} = \frac{dp}{dt} = \sigma\dot{y}^2. \quad (5.80)$$

But as in the first solution, we have  $\dot{y} = \sqrt{2g(L-y)}$ . Therefore, the total force from the scale is

$$\begin{aligned} F &= F_{\text{weight}} + F_{dp/dt} = \sigma(L-y)g + 2\sigma(L-y)g \\ &= 3\sigma(L-y)g. \end{aligned} \quad (5.81)$$

Note that  $F_{dp/dt} = 2F_{\text{weight}}$  (until the chain is completely on the scale), independent of  $y$ .

![Diagram of a vertical chain of length L being held by a hand at the top, with its bottom end resting on a scale.](49db8f927099283cf66c9e1254b8c29f_img.jpg)

A diagram showing a vertical chain of length

 $L$ 

. At the top, a hand is shown holding the chain. The chain hangs straight down. At the bottom, the chain is draped over the edge of a rectangular scale. The label 'hand' is at the top, and 'L' is next to the vertical part of the chain.

Diagram of a vertical chain of length L being held by a hand at the top, with its bottom end resting on a scale.

Fig. 5.16

![Diagram of a vertical chain with point masses, showing a bend at the bottom where it rests on a scale.](7adece84bcb18fcd9f28c138beb9d4d9_img.jpg)

A diagram showing a vertical chain with several point masses (dots) attached at intervals. The chain is held at the top. At the bottom, the chain forms a U-shaped bend as it rests on a rectangular scale. The bend is wide, indicating that the spacing between masses is large compared to the scale's width.

Diagram of a vertical chain with point masses, showing a bend at the bottom where it rests on a scale.

Fig. 5.17

![Diagram of a vertical chain with point masses, showing a tight bend at the bottom where it rests on a scale.](fd5b985ab71868eb1f6d0ac040bc29ce_img.jpg)

A diagram showing a vertical chain with several point masses (dots) attached at intervals. The chain is held at the top. At the bottom, the chain forms a very tight, narrow U-shaped bend as it rests on a rectangular scale. The bend is much narrower than in Fig. 5.17, indicating that the spacing between masses is small compared to the scale's width.

Diagram of a vertical chain with point masses, showing a tight bend at the bottom where it rests on a scale.

Fig. 5.18

In this example, we assumed that the chain was “ideal,” in the sense that it was completely flexible, infinitesimally thin, and unstretchable. The simplest model that satisfies these criteria is a series of point masses connected by short massless strings. But in the above example, the strings actually don’t even matter. You could instead start with many little unconnected point masses held in a vertical line, with the bottom one just above the scale. If you then dropped all of them simultaneously, they would successively smash into the scale in the same manner as if they were attached by little strings; the tension in the strings would all be zero. However, even though the strings aren’t necessary in this chain and scale example, there are many setups involving idealized chains where they are in fact necessary, because a tension is required in them. This is evident in many of the problems and exercises for this chapter, as you will see.

An interesting fact is that even with the above definition of an ideal chain, there are some setups (in contrast with the one above) for which it is impossible to specify how the system behaves, without being given more information. This information involves the relative size of two specific length scales, as we’ll see below. To illustrate this, consider the two following scenarios for the setup in Problem 5.28 (see Fig. 5.16), where a vertical ideal chain is dropped with its bottom end attached to the underneath of a support.

- **FIRST SCENARIO (ENERGY NONCONSERVING):** Let the spacing between the point masses in our ideal chain be large compared with the horizontal span of the bend in the chain at its bottom; see Fig. 5.17. Then the system is for all practical purposes one dimensional. Each of the masses stops abruptly when it reaches the bend. This stoppage is a completely inelastic collision in the same way it was in the above example with the chain falling on the scale. Note that at any point in time, the bend consists of a massless piece of string folded back along itself (or perhaps it consists of one of the masses, if we happen to be looking at it right when a mass stops). There is no tension in this bottom piece of string (if there were, then the massless bend would have an infinite acceleration upward), so there is no tension pulling down the part of the chain on the left side of the bend. The left part of the chain is therefore in freefall.
- **SECOND SCENARIO (ENERGY CONSERVING):** Let the spacing between the point masses in our ideal chain be small compared with the horizontal span of the bend in the chain at its bottom; see Fig. 5.18. The system is now inherently two dimensional, and the masses are essentially continuously distributed along the chain, as far as the bend is concerned. This has the effect of allowing each mass to gradually come to rest, so there is no abrupt inelastic stopping like there was in the first scenario. Each mass

in the bend keeps the same distance from its two neighbors, whereas in the first scenario the mass that has just stopped soon sees the next mass fly directly past it before abruptly coming to rest. The process in this second scenario is elastic; no energy is lost to heat.

The basic difference between the two scenarios is whether or not there is slack in any of the strings in the bend. If there is, then the relative speed between a pair of masses changes abruptly at some point, which means that the relative kinetic energy of the masses goes into damped (perhaps very overdamped) vibrational motion in the connecting string, which then decays into the random motion of heat.<sup>22</sup>

If no energy is lost to heat in the second scenario, then you might think that the last infinitesimal piece of the chain will have an infinite speed. However, there isn't one *last* piece of the chain. When the left part of the chain has disappeared and we are left with only the bend and the right part, the small (but nonzero) bend is the last "piece," and it ends up swinging horizontally with a large speed. This then drags the whole chain to the side in a very visible motion (which can be traced to the horizontal force from the support), at which point we have a very noticeably two-dimensional system. The initial potential energy of the chain ends up as kinetic energy of the final wavy side-to-side motion.

A consequence of energy conservation in the second scenario is that for a given height fallen, the left part of the chain will be moving faster than the left part in the first scenario. In other words, the left part in the second scenario accelerates downward faster than the freefall  $g$ . But although this result follows quickly from energy considerations, it isn't so obvious in terms of a force argument. Apparently there exists a tension at the left end of the bend in the second scenario that drags down the left part of the chain to give it an acceleration greater than  $g$ . A qualitative way of seeing why a tension exists there is the following. A tiny piece of the chain that enters the bend from the left part slows down as it gradually joins the fixed right part of the chain. There must therefore be an upward force on this tiny piece. This upward force can't occur at the bottom of the piece, because any tension there pulls *down* on it. The force must therefore occur at the top of the piece. In other words, there is a tension at this point, and so by Newton's third law this tension pulls down on the left part of the chain, thereby causing it to accelerate faster than  $g$ . One of the tasks of Problem 5.29 is to find the tensions at the two ends of the bend.

There is a simple way to demonstrate the existence of a tension that pulls on the free part of the chain. The following setup is basically the falling-chain setup without gravity, but it still has all the essential parts. Place a rope on a

<sup>22</sup> If the strings were ideal springs with weak spring constants, then the energy would keep changing back and forth between potential energy of the springs and kinetic energy of the masses, causing the masses to bounce around and possibly run into each other. But we're assuming that the strings in our ideal chain are essentially very rigid overdamped springs.

(fairly smooth) table, in the shape of a very thin “U” so that it doubles back along itself. Then quickly yank on one of the ends, in the direction away from the bend. You will find that the other end moves backwards, in the direction *opposite* to the motion of your hand, toward the bend (at least until the bend reaches it and drags it forward). There must therefore exist a tension in the rope to drag the other end backwards. But there’s no need to take my word for it – all you need is a piece of rope. This effect is essentially the same as the one (in a simplified version, since the rope here has constant density) that leads to the crack of a whip.

Note that a perfectly flexible thin *rope*, with its continuous mass distribution, does indeed behave elastically like the second scenario above. The continuous rope may be thought of as a series of point masses with infinitesimal separation, and so this separation is much smaller than the small (but finite) length of the bend. As long as the thickness of the rope is much smaller than the length of the bend, every piece of the rope slows to a stop gradually in the original falling-chain setup, or starts up from rest gradually in the preceding “U” setup. So there is no heat loss in either setup from abrupt changes in motion.

Returning to the falling-chain system with one of our ideal chains, you might think that if the bend is made *really* small, so that the system looks one-dimensional, then it should behave inelastically like the first scenario above. However, the only relevant fact is whether the bend is smaller than the spacing between the point masses in our ideal chain. The word “small” is meaningless, of course, because we are talking about the length of the bend, which is a dimensionful quantity. It makes sense only to use the word “smaller,” that is, to compare one length with another. The other length here is the spacing between the masses. If the length of the bend is large compared with this spacing, then no matter what the actual length of the bend is, the system behaves elastically like the second scenario above.

So which of the two scenarios better describes a real chain? Details of an actual experiment involving a falling chain are given in Calkin and March (1989). The results show that a real chain behaves basically like the chain in the second scenario above, at least until the final part of the motion. In other words, it is energy conserving, and the left part accelerates faster than  $g$ .<sup>23</sup>

Having said all this, it turns out that the energy-conserving second scenario leads to complicated issues in problems (such as the numerical integration in Problem 5.29), so for all the problems and exercises in this chapter (with the exception of Problem 5.29), we’ll assume that we’re dealing with the inelastic first scenario.

<sup>23</sup> Spur-of-the-moment (but still plenty convincing) experiments were also performed by Wes Campbell in the physics laboratory of John Doyle at Harvard.

### 5.9 Problems

### Section 5.1: Conservation of energy in one dimension

#### 5.1. Minimum length \*

The shortest configuration of string joining three given points is the one shown in the first setup in Fig. 5.19, where all three angles are  $120^\circ$ .<sup>24</sup> Explain how you could experimentally prove this fact by cutting three holes in a table and making use of three equal masses attached to the ends of strings, the other ends of which are connected as shown in the second setup in Fig. 5.19.

#### 5.2. Heading to zero \*

A particle moves toward  $x = 0$  under the influence of a potential  $V(x) = -A|x|^n$ , where  $A > 0$  and  $n > 0$ . The particle has barely enough energy to reach  $x = 0$ . For what values of  $n$  will it reach  $x = 0$  in a finite time?

#### 5.3. Leaving the sphere \*

A small mass rests on top of a fixed frictionless sphere. The mass is given a tiny kick and slides downward. At what point does it lose contact with the sphere?

#### 5.4. Pulling the pucks \*\*

- A massless string of length  $2\ell$  connects two hockey pucks that lie on frictionless ice. A constant horizontal force  $F$  is applied to the midpoint of the string, perpendicular to it (see Fig. 5.20). By calculating the work done in the transverse direction, find how much kinetic energy is lost when the pucks collide, assuming they stick together.
- The answer you obtained above should be very clean and nice. Find the slick solution that makes it transparent why the answer is so nice.

#### 5.5. Constant $\dot{y}$ \*\*

A bead, under the influence of gravity, slides down a frictionless wire whose height is given by the function  $y(x)$ . Assume that at position  $(x, y) = (0, 0)$ , the wire is vertical and the bead passes this point with a given speed  $v_0$  downward. What should the shape of the wire be (that is, what is  $y$  as a function of  $x$ ) so that the vertical speed remains  $v_0$  at all times? Assume that the curve heads toward positive  $x$ .

![Figure 5.19: Two diagrams illustrating the shortest configuration of a string joining three points. The top diagram shows three points connected by a string forming a Y-shape with 120-degree angles at the junction. The bottom diagram shows three masses labeled 'm' connected by strings to a central point, illustrating an experimental setup to find the shortest path.](93acc44e927f47bcd8d983692e036565_img.jpg)

Figure 5.19: Two diagrams illustrating the shortest configuration of a string joining three points. The top diagram shows three points connected by a string forming a Y-shape with 120-degree angles at the junction. The bottom diagram shows three masses labeled 'm' connected by strings to a central point, illustrating an experimental setup to find the shortest path.

Fig. 5.19

![Figure 5.20: A diagram showing a vertical string of length 2l with two pucks at the ends. A horizontal force F is applied to the midpoint of the string, pulling it to the right. The string segments are labeled 'l'.](e907a872929128b23f5b65ea1718da4e_img.jpg)

Figure 5.20: A diagram showing a vertical string of length 2l with two pucks at the ends. A horizontal force F is applied to the midpoint of the string, pulling it to the right. The string segments are labeled 'l'.

Fig. 5.20

<sup>24</sup> If the three points form a triangle that has an angle greater than  $120^\circ$ , then the string simply passes through the point where that angle is. We won't worry about this case.

#### **5.6. Dividing the heat \*\*\***

A block rests on a table where the coefficient of kinetic friction is  $\mu_k$ . You pull the block at a constant speed across the table by applying a force  $\mu_k N$ . Consider a period of time during which the block moves a distance  $d$ . How much work is done on the block? On the table? How much does each object heat up? Is it possible to answer these questions? *Hint:* You'll have to make some sort of model, however crude, for the way that friction works.

![Figure 5.21: A graph showing height = V(x) as a function of position x. The curve starts at a high point, descends to a local minimum, then rises to a local maximum, and finally descends again. The vertical axis is labeled y and the horizontal axis is labeled x.](273af3b421f433375f037ff1eb9d381e_img.jpg)

Figure 5.21: A graph showing height = V(x) as a function of position x. The curve starts at a high point, descends to a local minimum, then rises to a local maximum, and finally descends again. The vertical axis is labeled y and the horizontal axis is labeled x.

**Fig. 5.21**

#### **5.7. $V(x)$ vs. a hill \*\*\***

A bead, under the influence of gravity, slides along a frictionless wire whose height is given by the function  $V(x)$ , as shown in Fig. 5.21. Find an expression for the bead's horizontal acceleration,  $\ddot{x}$ . (It can depend on whatever quantities you need it to depend on.) You should find that the result is *not* the same as the  $\ddot{x}$  for a particle moving in one dimension in the potential  $mgV(x)$ , in which case  $\ddot{x} = -gV'$ . But if you grab hold of the wire, is there any way you can move it so that the bead's  $\ddot{x}$  is equal to the  $\ddot{x} = -gV'$  result for the one-dimensional potential  $mgV(x)$ ?

### *Section 5.2: Small oscillations*

#### **5.8. Hanging mass**

The potential for a mass hanging from a spring is  $V(y) = ky^2/2 + mgy$ , where  $y = 0$  corresponds to the position of the spring when nothing is hanging from it. Find the frequency of small oscillations around the equilibrium point.

#### **5.9. Small oscillations \***

A particle moves under the influence of the potential  $V(x) = -Cx^n e^{-ax}$ . Find the frequency of small oscillations around the equilibrium point.

### *Section 5.4: Gravity*

![Figure 5.22: A diagram of a spherical shell. A point P is located inside the shell. Two thin cones are drawn with their vertices at P, extending to the surface of the shell. The cones are symmetric about the line passing through P and the center of the shell.](67599b3744478fdbdea6c00d0d4a8c29_img.jpg)

Figure 5.22: A diagram of a spherical shell. A point P is located inside the shell. Two thin cones are drawn with their vertices at P, extending to the surface of the shell. The cones are symmetric about the line passing through P and the center of the shell.

**Fig. 5.22**

#### **5.10. Zero force inside a sphere \***

Show that the gravitational force inside a spherical shell is zero by showing that the pieces of mass at the ends of the thin cones in Fig. 5.22 give canceling forces at point  $P$ .

#### **5.11. Escape velocity \***

- (a) Find the escape velocity (that is, the velocity above which a particle escapes to  $r = \infty$ ) for a particle on a spherical planet of radius  $R$  and mass  $M$ . What is the numerical value for the earth? The moon? The sun?

- (b) Approximately how small must a spherical planet be in order for a human to be able to jump off? Assume a density roughly equal to the earth's.

#### **5.12. Ratio of potentials \*\***

Consider a cube of uniform mass density. Find the ratio of the gravitational potential energy of a mass at a corner to that of the same mass at the center. *Hint:* There's a slick way that doesn't involve any messy integrals.

#### **5.13. Through the hole \*\***

- (a) A hole of radius  $R$  is cut out from an infinite flat sheet with mass density  $\sigma$  per unit area. Let  $L$  be the line that is perpendicular to the sheet and that passes through the center of the hole. What is the force on a mass  $m$  that is located on  $L$ , at a distance  $x$  from the center of the hole? *Hint:* Consider the plane to consist of many concentric rings.
- (b) If a particle is released from rest on  $L$ , very close to the center of the hole, show that it undergoes oscillatory motion, and find the frequency of these oscillations.
- (c) If a particle is released from rest on  $L$ , at a distance  $x$  from the sheet, what is its speed when it passes through the center of the hole? What is your answer in the limit  $x \gg R$ ?

### *Section 5.5: Momentum*

#### **5.14. Snowball \***

A snowball is thrown against a wall. Where does its momentum go? Where does its energy go?

#### **5.15. Propelling a car \*\***

For some odd reason, you decide to throw baseballs at a car of mass  $M$  that is free to move frictionlessly on the ground. You throw the balls at the back of the car at speed  $u$ , and they leave your hand at a mass rate of  $\sigma$  kg/s (assume the rate is continuous, for simplicity). If the car starts at rest, find its speed and position as a function of time, assuming that the balls bounce elastically directly backward off the back window.

#### **5.16. Propelling a car again \*\***

Do the previous problem, except now assume that the back window is open, so that the balls collect inside the car.

![Diagram of a leaky bucket connected to a wall by a spring.](9a1b724bda44c790b84a04a6019c3814_img.jpg)

A diagram showing a vertical wall on the left and a horizontal ground. A bucket is placed on the ground to the right of the wall. A horizontal line representing a spring connects the wall to the bucket. The spring is labeled with the letter 'T' above it, indicating constant tension. The bucket is shown as a cylinder with a dashed line at its base.

Diagram of a leaky bucket connected to a wall by a spring.

Fig. 5.23

#### 5.17. Leaky bucket \*\*

At  $t = 0$ , a massless bucket contains a mass  $M$  of sand. It is connected to a wall by a massless spring with constant tension  $T$  (that is, independent of length).<sup>25</sup> See Fig. 5.23. The ground is frictionless, and the initial distance to the wall is  $L$ . At later times, let  $x$  be the distance from the wall, and let  $m$  be the mass of sand in the bucket. The bucket is released, and on its way to the wall, it leaks sand at a rate  $dm/dx = M/L$ . In other words, the rate is constant with respect to distance, not time; and it ends up empty right when it reaches the wall. Note that  $dx$  is negative, so  $dm$  is also.

- What is the kinetic energy of the (sand in the) bucket, as a function of  $x$ ? What is its maximum value?
- What is the magnitude of the momentum of the bucket, as a function of  $x$ ? What is its maximum value?

#### 5.18. Another leaky bucket \*\*\*

Consider the setup in Problem 5.17, but now let the sand leak at a rate proportional to the bucket's acceleration. That is,  $dm/dt = b\ddot{x}$ . Note that  $\ddot{x}$  is negative, so  $dm$  is also.

- Find the mass as a function of time,  $m(t)$ .
- Find  $v(t)$  and  $x(t)$  during the time when the bucket contains a nonzero amount of sand. Also find  $v(m)$  and  $x(m)$ . What is the speed right before all the sand leaves the bucket (assuming it hasn't hit the wall yet)?
- What is the maximum value of the bucket's kinetic energy, assuming it is achieved before it hits the wall?
- What is the maximum value of the magnitude of the bucket's momentum, assuming it is achieved before it hits the wall?
- For what value of  $b$  does the bucket become empty right when it hits the wall?

### Section 5.7: Collisions

#### 5.19. Right angle in billiards \*

A billiard ball collides elastically with an identical stationary one. Use the fact that  $mv^2/2$  may be written as  $m(\mathbf{v} \cdot \mathbf{v})/2$  to show that the angle

<sup>25</sup> You can construct a constant-tension spring with a regular Hooke's-law spring in the following way. Pick the spring constant to be very small, and stretch the spring a very large distance. Have it pass through a hole in the wall, with its other end bolted down a large distance to the left of the wall. Any changes in the bucket's position will yield a negligible change in the spring force.

between the resulting trajectories is  $90^\circ$ . *Hint:* Take the dot product of the conservation of momentum equation with itself.

#### 5.20. Bouncing and recoiling \*\*

A ball of mass  $m$  and initial speed  $v_0$  bounces back and forth between a fixed wall and a block of mass  $M$ , with  $M \gg m$ ; see Fig. 5.24. The block is initially at rest. Assume that the ball bounces elastically and instantaneously. The coefficient of kinetic friction between the block and the ground is  $\mu$ . There is no friction between the ball and the ground. What is the speed of the ball after the  $n$ th bounce off the block? How far does the block eventually move? How much total time does the block actually spend in motion? Work in the approximation where  $M \gg m$ , and assume that the distance to the wall is large enough so that the block comes to rest by the time the next bounce occurs.

![Diagram for problem 5.20 showing a ball of mass m moving with velocity v_0 towards a block of mass M on a horizontal surface with friction coefficient mu. A vertical wall is on the left.](b0fe994c1cb447fa7ba46b06674073cc_img.jpg)

Diagram for problem 5.20 showing a ball of mass m moving with velocity v\_0 towards a block of mass M on a horizontal surface with friction coefficient mu. A vertical wall is on the left.

Fig. 5.24

#### 5.21. Drag force on a sheet \*\*

A sheet of mass  $M$  moves with speed  $V$  through a region of space that contains particles of mass  $m$  and speed  $v$ . There are  $n$  of these particles per unit volume. The sheet moves in the direction of its normal. Assume  $m \ll M$ , and assume that the particles do not interact with each other.

- If  $v \ll V$ , what is the drag force per unit area on the sheet?
- If  $v \gg V$ , what is the drag force per unit area on the sheet? Assume, for simplicity, that the component of every particle's velocity in the direction of the sheet's motion is exactly  $\pm v/2$ .<sup>26</sup>

#### 5.22. Drag force on a cylinder \*\*

A cylinder of mass  $M$  and radius  $R$  moves with speed  $V$  through a region of space that contains particles of mass  $m$  that are at rest. There are  $n$  of these particles per unit volume. The cylinder moves in a direction perpendicular to its axis. Assume  $m \ll M$ , and assume that the particles do not interact with each other. What is the drag force per unit length on the cylinder?

#### 5.23. Basketball and tennis ball \*\*

- A tennis ball with a small mass  $m_2$  sits on top of a basketball with a large mass  $m_1$  (see Fig. 5.25). The bottom of the basketball is a height  $h$  above the ground, and the bottom of the tennis ball is a height  $h + d$  above the ground. The balls are dropped. To what height does the tennis ball bounce? *Note:* Work in the

![Diagram for problem 5.23 showing a basketball (B1) of radius R and a tennis ball (B2) of radius r sitting on top of it. The bottom of the basketball is at height h above the ground, and the bottom of the tennis ball is at height h + d above the ground.](5b449030ea055d1b78008909e0972c65_img.jpg)

Diagram for problem 5.23 showing a basketball (B1) of radius R and a tennis ball (B2) of radius r sitting on top of it. The bottom of the basketball is at height h above the ground, and the bottom of the tennis ball is at height h + d above the ground.

Fig. 5.25

<sup>26</sup> In reality, the velocities are randomly distributed, but this idealization actually gives the correct answer because the average speed in any direction is  $\overline{|v_x|} = v/2$ , as you can show.

![Diagram of four balls stacked vertically on a horizontal surface. The balls are labeled B1, B2, B3, and B4 from bottom to top. B1 is the largest, and B4 is the smallest. A vertical arrow labeled 'h' indicates the height from the ground to the bottom of B1. The text 'n = 4' is to the left of the stack.](dfd6b90809eb7392bc1466f1f1cbfee7_img.jpg)

Diagram of four balls stacked vertically on a horizontal surface. The balls are labeled B1, B2, B3, and B4 from bottom to top. B1 is the largest, and B4 is the smallest. A vertical arrow labeled 'h' indicates the height from the ground to the bottom of B1. The text 'n = 4' is to the left of the stack.

Fig. 5.26

approximation where  $m_1$  is much larger than  $m_2$ , and assume that the balls bounce elastically. Also assume, for the sake of having a nice clean problem, that the balls are initially separated by a small distance, and that the balls bounce instantaneously.

- (b) Now consider  $n$  balls,  $B_1, \dots, B_n$ , having masses  $m_1, m_2, \dots, m_n$  (with  $m_1 \gg m_2 \gg \dots \gg m_n$ ), standing in a vertical stack (see Fig. 5.26). The bottom of  $B_1$  is a height  $h$  above the ground, and the bottom of  $B_n$  is a height  $h + \ell$  above the ground. The balls are dropped. In terms of  $n$ , to what height does the top ball bounce? *Note:* Make assumptions and approximations similar to the ones in part (a).

If  $h = 1$  meter, what is the minimum number of balls needed for the top one to bounce to a height of at least 1 kilometer? To reach escape velocity? Assume that the balls still bounce elastically (which is a bit absurd here), and ignore wind resistance, etc., and assume that  $\ell$  is negligible.

#### 5.24. Maximal deflection \*\*\*

A mass  $M$  collides with a stationary mass  $m$ . If  $M < m$ , then it is possible for  $M$  to bounce directly backward. However, if  $M > m$ , then there is a maximal angle of deflection of  $M$ . Show that this maximal angle equals  $\sin^{-1}(m/M)$ . *Hint:* It is possible to do this problem by working in the lab frame, but you can save yourself a lot of time by considering what happens in the CM frame, and then shifting back to the lab frame.

### Section 5.8: Inherently inelastic processes

*Note: In the problems involving chains in this section (with the exception of Problem 5.29), we'll assume that the chains are of the type described in the first scenario near the end of Section 5.8.*

#### 5.25. Colliding masses \*

A mass  $M$ , initially moving at speed  $V$ , collides and sticks to a mass  $m$ , initially at rest. Assume  $M \gg m$ , and work in this approximation. What are the final energies of the two masses, and how much energy is lost to heat, in:

- The lab frame?
- The frame in which  $M$  is initially at rest?

![Diagram showing a hand pulling a chain of length L on a horizontal surface. The hand is on the left, and the chain is being pulled to the right with a velocity v. The text '(top view)' is above the diagram.](1431dff095a4dce48ea1111a893cb77b_img.jpg)

Diagram showing a hand pulling a chain of length L on a horizontal surface. The hand is on the left, and the chain is being pulled to the right with a velocity v. The text '(top view)' is above the diagram.

Fig. 5.27

#### 5.26. Pulling a chain \*\*

A chain with length  $L$  and mass density  $\sigma$  kg/m lies straight on a frictionless horizontal surface. You grab one end and pull it back along itself, in a parallel manner (see Fig. 5.27). Assume that you pull it at constant

speed  $v$ . What force must you apply? What is the total work that you do, by the time the chain is straightened out? How much energy is lost to heat, if any?

#### **5.27. Pulling a chain again \*\***

A chain with mass density  $\sigma$  kg/m lies in a heap on the floor. You grab an end and pull horizontally with constant force  $F$ . What is the position of the end of the chain, as a function of time, while it is unravelling? Assume that the chain is greased, so that it has no friction with itself.

#### **5.28. Falling chain \*\***

A chain with length  $L$  and mass density  $\sigma$  kg/m is held in the position shown in Fig. 5.28, with one end attached to a support. Assume that only a negligible length of the chain starts out below the support. The chain is released. Find the force that the support applies to the chain, as a function of time.

![Diagram of a chain hanging from a hand. The hand is at the top, holding the chain. The chain is vertical and has a length L. The bottom end of the chain is attached to a support, which is represented by a horizontal line with a small vertical segment at the end.](9c2b9256d944dbdc5f8dee35395a5e21_img.jpg)

Diagram of a chain hanging from a hand. The hand is at the top, holding the chain. The chain is vertical and has a length L. The bottom end of the chain is attached to a support, which is represented by a horizontal line with a small vertical segment at the end.

**Fig. 5.28**

#### **5.29. Falling chain (energy conserving) \*\*\***

Consider the setup in the previous problem, but now let the chain be of the type in the second scenario described in Section 5.8. Show that the total time it takes the chain to straighten out is approximately 85% of the time it would take if the left part were in freefall (as it was in the previous problem); you will need to solve something numerically. Also, show that the tension at the left end of the infinitesimal bend equals the tension at the right end at all times.<sup>27</sup>

#### **5.30. Falling from a table \*\*\***

- A chain with length  $L$  lies in a straight line on a frictionless table, except for a very small piece at one end which hangs down through a hole in the table. This piece is released, and the chain slides down through the hole. What is the speed of the chain at the instant it loses contact with the table? (see Footnote 3.19.)
- Answer the same question, but now let the chain lie in a heap on a table, except for a very small piece at one end which hangs down through the hole. Assume that the chain is greased, so that it has no friction with itself. Which of these two scenarios has the larger final speed?

<sup>27</sup> The “ends” of the bend actually aren’t well defined, because the chain is at least a little bit curved everywhere. But since we’re assuming that the horizontal span of the chain is very small, we can define the height of the bend to be, say, 100 times this horizontal span, and this height is still negligible compared with the total height of the chain.

#### **5.31. The raindrop \*\*\*\***

Assume that a cloud consists of tiny water droplets suspended (uniformly distributed, and at rest) in air, and consider a raindrop falling through them. What is the acceleration of the raindrop? Assume that the raindrop is initially of negligible size and that when it hits a water droplet, the droplet's water gets added to it. Also, assume that the raindrop is spherical at all times.

### **5.10 Exercises**

### *Section 5.1: Conservation of energy in one dimension*

#### **5.32. Cart in a valley**

A cart containing sand starts at rest and then rolls, without any energy loss to friction, down into a valley and then up a hill on the other side. Let the initial height be  $h_1$ , and let the final height attained on the other side be  $h_2$ . If the cart leaks sand along the way, how does  $h_2$  compare with  $h_1$ ?

#### **5.33. Walking on an escalator**

An escalator moves downward at constant speed. You walk up the escalator at this same speed, so that you remain at rest with respect to the ground. In the ground frame, are you doing any work?

#### **5.34. Lots of work**

If you push on a wall with your hand, you don't do any work, because your hand doesn't move. But in the reference frame of a person moving past you (from front to back), you do in fact do work, because your hand moves. And since the person's speed can be made arbitrarily large, you can do an arbitrarily large amount of work in the person's frame. It therefore seems like you should quickly use up your dinner from the night before and become very hungry. But you don't. Why not?

#### **5.35. Spring energy**

Using the explicit form of the position of a mass on the end of a spring,  $x(t) = A \cos(\omega t + \phi)$ , verify that the total energy is conserved.

#### **5.36. Damping work \***

A damped oscillator (with  $m\ddot{x} = -kx - b\dot{x}$ ) has initial position  $x_0$  and speed  $v_0$ . After a long time, it will essentially be at rest at the origin. Therefore, by the work-energy theorem, the work done by the damping force must equal  $-kx_0^2/2 - mv_0^2/2$ . Verify that this is true. *Hint:* It's rather messy to explicitly find  $\dot{x}$  in terms of the initial conditions and

then calculate the desired integral. An easier way is to use the  $F = ma$  equation to rewrite the  $\dot{x}$  in your integral.

#### **5.37. Heading to infinity \***

A particle moves under the influence of a potential  $V(x) = -A|x|^n$ , where  $A > 0$  and  $n > 0$ . It starts at a positive value of  $x$  with a velocity that points in the positive  $x$  direction. For what values of  $n$  will the particle reach infinity in a finite time? You may assume that  $E > 0$ , although this isn't necessary. (You can compare this exercise with Problem 5.2.)

#### **5.38. Work in different frames \***

An object, initially at rest, is subject to a force that gives it constant acceleration  $a$  for time  $t$ . Verify explicitly that  $W = \Delta K$  in (a) the lab frame, and (b) a frame moving to the left at speed  $V$ .

#### **5.39. Roller coaster \***

A roller coaster car starts at rest and coasts down a frictionless track. It encounters a vertical loop of radius  $R$ . How much higher than the top of the loop must the car start if it is to remain in contact with the track at all times?

#### **5.40. Pendulum and peg \***

A pendulum of length  $L$  is held with its string horizontal, and then released. The string runs into a peg a distance  $d$  below the pivot, as shown in Fig. 5.29. What is the smallest value of  $d$  for which the string remains taut at all times?

![Diagram of a pendulum of length L pivoted at a point. A peg is located a distance d below the pivot. The pendulum is shown in its initial horizontal position and at the bottom of its swing, where the string is caught by the peg. A dashed arc indicates the path of the bob.](27beac0e28bb9c069cf16b7f014d1499_img.jpg)

Diagram of a pendulum of length L pivoted at a point. A peg is located a distance d below the pivot. The pendulum is shown in its initial horizontal position and at the bottom of its swing, where the string is caught by the peg. A dashed arc indicates the path of the bob.

Fig. 5.29

#### **5.41. Circling around a cone \***

A fixed hollow frictionless cone is positioned with its tip pointing down. A particle is released from rest on the inside surface. After it has slid part way down to the tip, it bounces elastically off a platform. The platform is positioned at a  $45^\circ$  angle along the surface of the cone, so the particle ends up being deflected horizontally along the surface (in other words, into the page in Fig. 5.30). If the resulting motion of the particle is a horizontal circle around the cone, what is the ratio of the initial height of the particle to the height of the platform?

![Diagram of a cone with its tip pointing down. A platform is placed on the inside surface at a 45-degree angle. A particle is shown at a higher point on the cone's surface, and an arrow indicates its path sliding down towards the platform.](52a72f2e88ce868cbf75eb239f4fcd89_img.jpg)

Diagram of a cone with its tip pointing down. A platform is placed on the inside surface at a 45-degree angle. A particle is shown at a higher point on the cone's surface, and an arrow indicates its path sliding down towards the platform.

Fig. 5.30

#### **5.42. Hanging spring \***

A massless spring with spring constant  $k$  hangs vertically from a ceiling, initially at its relaxed length. A mass  $m$  is then attached to the bottom and is released.

- (a) Calculate the potential energy  $V$  of the system, as a function of the height  $y$  (which is negative), relative to the initial position.

![Diagram for Fig. 5.31: A block of mass m is on an inclined plane at an angle theta. A spring with constant k is attached to the block and the incline. The coefficient of static friction is mu.](3ab048dc30f66895c2eb9310c0bc173c_img.jpg)

Diagram for Fig. 5.31: A block of mass m is on an inclined plane at an angle theta. A spring with constant k is attached to the block and the incline. The coefficient of static friction is mu.

Fig. 5.31

- (b) Find  $y_0$ , the point at which the potential energy is minimum. Make a rough plot of  $V(y)$ .
- (c) Rewrite the potential energy as a function of  $z \equiv y - y_0$ . Explain why your result shows that a hanging spring can be considered to be a spring in a world without gravity, provided that the new equilibrium point,  $y_0$ , is now called the “relaxed” length of the spring.

#### 5.43. Removing the friction \*

A block of mass  $m$  is supported by a spring on an inclined plane, as shown in Fig. 5.31. The spring constant is  $k$ , the plane’s angle of inclination is  $\theta$ , and the coefficient of static friction between the block and the plane is  $\mu$ .

- (a) You move the block down the plane, compressing the spring. What is the maximum compression distance of the spring (relative to the relaxed length it has when nothing is attached to it) that allows the block to remain at rest when you let go of it?
- (b) Assume that the block is at the maximum compression you found in part (a). At a given instant, you somehow cause the plane to become frictionless, and the block gets pushed up along the plane. What must the relation between  $\theta$  and the original  $\mu$  be, so that the block reaches its maximum height when the spring is at its relaxed length?

#### 5.44. Spring and friction \*\*

A spring with spring constant  $k$  stands vertically, and a mass  $m$  is placed on top of it. The mass is slowly lowered to its equilibrium position. With the spring held at this compression length, the system is rotated to a horizontal position. The left end of the spring is attached to a wall, and the mass is placed on a table with a coefficient of friction (both kinetic and static) of  $\mu = 1/8$ ; see Fig. 5.32. The mass is released.

![Diagram for Fig. 5.32: The top part shows a mass m on a vertical spring with constant k. An arrow points down to the bottom part, which shows the mass m on a horizontal surface with friction mu=1/8, attached to a horizontal spring with constant k.](a7035d6c735b8c3bf2288eabfd9cadfe_img.jpg)

Diagram for Fig. 5.32: The top part shows a mass m on a vertical spring with constant k. An arrow points down to the bottom part, which shows the mass m on a horizontal surface with friction mu=1/8, attached to a horizontal spring with constant k.

Fig. 5.32

- (a) What is the initial compression of the spring?
- (b) How much does the maximal stretch (or compression) of the spring decrease after each half-oscillation?
- (c) How many times does the mass oscillate back and forth before coming to rest?

#### 5.45. Keeping contact \*\*

A frictionless circle of radius  $R$  is made out of a strip of metal and held fixed in a vertical plane. A massless spring with spring constant  $k$  has one end attached to the bottom point on the inside surface of the circle, and the other end attached to a mass  $m$ . The spring is compressed to zero length,

with the mass touching the inside surface of the circle at the bottom. (Whatever negligible length of spring remains is essentially horizontal.) The spring is then released, and the mass gets pushed initially to the right and then up along the circle; the setup at a random later time is shown in Fig. 5.33. Let  $\ell$  be the equilibrium length of the spring. What is the minimum value of  $\ell$  for which the mass remains in contact with the circle at all times?

![Figure 5.33: A diagram showing a mass m attached to a spring with spring constant k. The mass is inside a circular hoop of radius R. The spring is attached to the bottom of the hoop and the mass is at an angle from the vertical. An arrow indicates the mass is moving upwards along the inner surface of the hoop.](9bcbf3a961add6b34ece21ca0a45cc5a_img.jpg)

Figure 5.33: A diagram showing a mass m attached to a spring with spring constant k. The mass is inside a circular hoop of radius R. The spring is attached to the bottom of the hoop and the mass is at an angle from the vertical. An arrow indicates the mass is moving upwards along the inner surface of the hoop.

Fig. 5.33

#### **5.46. Spring and hoop \*\***

A fixed hoop of radius  $R$  stands vertically. A spring with spring constant  $k$  and relaxed length of zero is attached to the top of the hoop.

- A block of mass  $m$  is attached to the unstretched spring and dropped from the top of the hoop. If the resulting motion of the mass is a linear vertical oscillation between the top and bottom points on the hoop, what is  $k$ ?
- The block is now removed from the spring, and the spring is stretched and connected to a bead, also of mass  $m$ , at the bottom of the hoop, as shown in Fig. 5.34. The bead is constrained to move along the hoop. It is given a rightward kick and acquires an initial speed  $v_0$ . Assuming that it moves frictionlessly, how does its speed depend on its position along the hoop?

![Figure 5.34: A diagram showing a bead of mass m at the bottom of a vertical hoop of radius R. A spring with spring constant k is attached to the top of the hoop and the bead. An arrow indicates the bead has an initial rightward velocity v_0.](0eb27eadaf69b57162dba6eb811b33be_img.jpg)

Figure 5.34: A diagram showing a bead of mass m at the bottom of a vertical hoop of radius R. A spring with spring constant k is attached to the top of the hoop and the bead. An arrow indicates the bead has an initial rightward velocity v\_0.

Fig. 5.34

#### **5.47. Constant $\dot{x}$ \*\***

A bead, under the influence of gravity, slides along a frictionless wire whose height is given by the function  $y(x)$ . Assume that at position  $(x, y) = (0, 0)$ , the wire is horizontal and the bead passes this point with a given speed  $v_0$  to the right. What should the shape of the wire be (that is, what is  $y$  as a function of  $x$ ) so that the horizontal speed remains  $v_0$  at all times? One solution is simply  $y = 0$ . Find the other.<sup>28</sup>

#### **5.48. Over the pipe \*\***

A frictionless cylindrical pipe with radius  $r$  is positioned with its axis parallel to the ground, at height  $h$ . What is the minimum speed at which a ball must be thrown (from ground level) in order to make it over the pipe? Consider two cases: (a) the ball is allowed to touch the pipe, and (b) the ball is not allowed to touch the pipe.

#### **5.49. Pendulum projectile \*\***

A pendulum is held with its string horizontal and is then released. The mass swings down, and then on its way back up, the string is cut when

<sup>28</sup> Solve this exercise in the spirit of Problem 5.5, that is, by solving a differential equation. Once you get the answer, you'll see that you could have just written it down without any calculations, based on your knowledge of a certain kind of physical motion.

![Diagram for Fig. 5.35: A mass on a string of length L is at an angle theta from the vertical. The string is cut at this position, and a dashed arc shows the subsequent parabolic trajectory of the mass.](8695438a52e9fef6c9622fa9eceb3544_img.jpg)

Diagram for Fig. 5.35: A mass on a string of length L is at an angle theta from the vertical. The string is cut at this position, and a dashed arc shows the subsequent parabolic trajectory of the mass.

Fig. 5.35

![Diagram for Fig. 5.36: A mass swings in a vertical circle. At an angle theta from the vertical, the string is cut. A dashed arc shows the projectile path of the mass after the cut.](558150ca52920cc46dedb5e5ad1b24f8_img.jpg)

Diagram for Fig. 5.36: A mass swings in a vertical circle. At an angle theta from the vertical, the string is cut. A dashed arc shows the projectile path of the mass after the cut.

Fig. 5.36

![Diagram for Fig. 5.37: Two beads of mass m are at the top of a vertical hoop of mass M and radius R. Arrows indicate they slide down in opposite directions.](33faf19cc8c99d623b389ebf4da2a138_img.jpg)

Diagram for Fig. 5.37: Two beads of mass m are at the top of a vertical hoop of mass M and radius R. Arrows indicate they slide down in opposite directions.

Fig. 5.37

![Diagram for Fig. 5.38: A particle of mass m is at the top of a hemispherical bowl of mass M. The bowl sits on a horizontal surface with a coefficient of friction mu = 1. An arrow shows the particle sliding down the frictionless inner surface.](c38d7197afa26ccd821f2b91e67c4251_img.jpg)

Diagram for Fig. 5.38: A particle of mass m is at the top of a hemispherical bowl of mass M. The bowl sits on a horizontal surface with a coefficient of friction mu = 1. An arrow shows the particle sliding down the frictionless inner surface.

Fig. 5.38

it makes an angle  $\theta$  with the vertical; see Fig. 5.35. What should  $\theta$  be so that the mass travels the largest horizontal distance by the time it returns to the height it had when the string was cut?

#### 5.50. Centered projectile motion \*\*

A mass is attached to one end of a massless string, the other end of which is attached to a fixed support. The mass swings around in a vertical circle as shown in Fig. 5.36. Assuming that the mass has the minimum speed necessary at the top of the circle to keep the string from going slack, at what location should you cut the string so that the resulting projectile motion of the mass has its maximum height located directly above the center of the circle?

#### 5.51. Beads on a hoop \*\*

Two beads of mass  $m$  are initially at rest at the top of a frictionless hoop of mass  $M$  and radius  $R$ , which stands vertically on the ground. The beads are given tiny kicks, and they slide down the hoop, one to the right and one to the left, as shown in Fig. 5.37. What is the largest value of  $m/M$  for which the hoop never rises up off the ground?

#### 5.52. Stationary bowl \*\*\*

A hemispherical bowl of mass  $M$  rests on a table. The inside surface of the bowl is frictionless, while the coefficient of friction between the bottom of the bowl and the table is  $\mu = 1$ . A particle of mass  $m$  is released from rest at the top of the bowl and slides down into it, as shown in Fig. 5.38. What is the largest value of  $m/M$  for which the bowl never slides on the table? *Hint:* The angle you're concerned with is *not*  $45^\circ$ .

#### 5.53. Leaving the hemisphere \*\*\*\*

A point particle of mass  $m$  sits at rest on top of a frictionless hemisphere of mass  $M$ , which rests on a frictionless table. The particle is given a tiny kick and slides down the (recoiling) hemisphere. At what angle  $\theta$  (measured from the top of the hemisphere) does the particle lose contact with the hemisphere? In answering this question for  $m \neq M$ , it is sufficient for you to produce an equation that  $\theta$  must satisfy (it's a cubic). However, for the special case of  $m = M$ , the equation can be solved without too much difficulty; find the angle in this case.

#### 5.54. Tetherball \*\*\*\*

A small ball is attached to a massless string of length  $L$ , the other end of which is attached to a very thin pole. The ball is thrown so that it initially travels in a horizontal circle, with the string making an angle  $\theta_0$  with the vertical. As time goes on, the string wraps itself around the

pole. Assume that (1) the pole is thin enough so that the length of string in the air decreases very slowly, so that the ball's motion may always be approximated as a circle, and (2) the pole has enough friction so that the string does not slide on the pole, once it touches it. Show that the ratio of the ball's final speed (right before it hits the pole) to initial speed is  $v_f/v_i = \sin \theta_0$ .

### Section 5.4: Gravity

#### 5.55. Projectile between planets \*

Two planets of mass  $M$  and radius  $R$  are at rest (somehow) with respect to each other, with their centers a distance  $4R$  apart. You wish to fire a projectile from the surface of one planet to the other. What is the minimum firing speed for which this is possible?

#### 5.56. Spinning quickly \*

Consider a planet with uniform mass density  $\rho$ . If the planet rotates too fast, it will fly apart. Show that the minimum period of rotation is given by

$$T = \sqrt{\frac{3\pi}{G\rho}}.$$

What is the minimum  $T$  if  $\rho = 5.5 \text{ g/cm}^3$  (the average density of the earth)?

#### 5.57. A cone \*\*

- A particle of mass  $m$  is located at the tip of a hollow cone (such as an ice cream cone without the ice cream) with surface mass density  $\sigma$ . The slant height of the cone is  $L$ , and the half-angle at the vertex is  $\theta$ . What can you say about the gravitational force on the mass  $m$  due to the cone?
- If the top half of the cone is removed and thrown away (see Fig. 5.39), what is the gravitational force on the mass  $m$  due to the remaining part of the cone? For what angle  $\theta$  is this force maximum?

#### 5.58. Sphere and cones \*\*

- Consider a thin hollow fixed spherical shell of radius  $R$  and surface mass density  $\sigma$ . A particle initially at rest falls in from infinity. What is its speed when it reaches the center of the shell? Assume that a tiny hole has been cut in the shell to let the particle through; see Fig. 5.40(a).

![Diagram of a hollow cone with a mass m at its tip. The cone has a slant height L/2 for each half. The half-angle at the vertex is theta. The top half is dashed, and the bottom half is solid.](2f54f6f0b8f8d0c973411f8f645bd3f4_img.jpg)

Diagram of a hollow cone with a mass m at its tip. The cone has a slant height L/2 for each half. The half-angle at the vertex is theta. The top half is dashed, and the bottom half is solid.

Fig. 5.39

![Two diagrams labeled (a) and (b). Diagram (a) shows a cross-section of a sphere of radius R with a particle at its center. Diagram (b) shows a double-cone structure with a particle at the central vertex. The top cone has a dashed base of radius R and slant height L. The bottom cone is solid with slant height L.](b15ba0212629f50eb5bed84e1ab98425_img.jpg)

Two diagrams labeled (a) and (b). Diagram (a) shows a cross-section of a sphere of radius R with a particle at its center. Diagram (b) shows a double-cone structure with a particle at the central vertex. The top cone has a dashed base of radius R and slant height L. The bottom cone is solid with slant height L.

Fig. 5.40

- (b) Consider two hollow fixed cones (such as ice cream cones without the ice cream), arranged as shown in Fig. 5.40(b). They have base radius  $R$ , slant height  $L$ , and surface mass density  $\sigma$ . A particle initially at rest falls in from infinity, along the perpendicular bisector line shown. What is its speed when it reaches the tip of the cones?

![Figure 5.41: Two diagrams illustrating scaling arguments for potential energy. The top diagram shows a square with a central dot and dashed lines, equated to a smaller square with a dot at its corner, labeled A. The bottom diagram shows the same square with a central dot, equated to a smaller square with a dot at its center, labeled B.](82cfb05b63e324939961c97d7994cf2e_img.jpg)

Figure 5.41: Two diagrams illustrating scaling arguments for potential energy. The top diagram shows a square with a central dot and dashed lines, equated to a smaller square with a dot at its corner, labeled A. The bottom diagram shows the same square with a central dot, equated to a smaller square with a dot at its center, labeled B.

Fig. 5.41

#### 5.59. Ratio of potentials \*\*

Consider the following two systems: (1) a mass  $m$  is placed at a corner of a flat square sheet of mass  $M$ , and (2) a mass  $m$  is placed at the center of a flat square sheet of mass  $M$ . What is the ratio of the potential energies of  $m$  in the two systems? *Hint:* Find  $A$  and  $B$  in the suggestive relations in Fig. 5.41. You'll need to use a scaling argument to find  $B$ .

#### 5.60. Solar escape velocity \*\*

What is the minimum initial velocity (with respect to the earth) required for an object to escape from the solar system?<sup>29</sup> Take the orbital motion of the earth into account (but ignore the rotation of the earth, and ignore the other planets). You are free to choose (wisely) the firing direction. Make the (good) approximation that the process occurs in two separate steps: first the object escapes from the earth, and then it escapes from the sun (starting at the radius of the earth's orbit). Some useful quantities are given in the solution to Problem 5.11; also, the orbital speed of the earth is about 30 km/s. *Hint:* a common incorrect answer is 13.5 km/s.

#### 5.61. Spherical shell \*\*

- (a) A spherical shell of mass  $M$  has inner radius  $R_1$  and outer radius  $R_2$ . A particle of mass  $m$  is located a distance  $r$  from the center of the shell. Calculate (and make a rough plot of) the force on  $m$ , as a function of  $r$ , for  $0 \leq r \leq \infty$ .
- (b) If the mass  $m$  is dropped from  $r = \infty$  and falls down through the shell (assume that a tiny hole has been drilled in it), what will its speed be at the center of the shell? You can let  $R_2 = 2R_1$  in this part of the problem, to keep things from getting too messy. Give your answer in terms of  $R \equiv R_1$ .

![Figure 5.42: A diagram of a planet of radius R. A stick of length 2R is attached to the planet's surface, extending radially outwards to a distance of 3R from the center. A dashed line labeled 'later' shows the stick's position after a small rotation, still pointing radially from the center.](d8e9ea6900860138f0adb306805886d6_img.jpg)

Figure 5.42: A diagram of a planet of radius R. A stick of length 2R is attached to the planet's surface, extending radially outwards to a distance of 3R from the center. A dashed line labeled 'later' shows the stick's position after a small rotation, still pointing radially from the center.

Fig. 5.42

#### 5.62. Orbiting stick \*\*

Consider a planet of mass  $M$  and radius  $R$ . A very long stick of length  $2R$  extends from just above the surface of the planet out to a radius  $3R$ . If initial conditions have been set up so that the stick moves in a circular orbit while always pointing radially (see Fig. 5.42), what is the period

<sup>29</sup> This problem is discussed in Hendel and Longo (1988).

of this orbit? How does this period compare with the period of a satellite in a circular orbit of radius  $2R$ ?

#### **5.63. Speedy travel \*\***

A straight tube is drilled between two points on the earth, as shown in Fig. 5.43. An object is dropped into the tube. What is the resulting motion? How long does it take to reach the other end? Ignore friction, and assume (incorrectly) that the density of the earth is constant ( $\rho = 5.5 \text{ g/cm}^3$ ).

![Diagram of a sphere representing the Earth. A horizontal line segment passes through the center, representing a straight tube. A small black dot is placed on the right side of the tube, and a double-headed arrow indicates motion back and forth along the tube.](e742464c8cced5296729a712074142dd_img.jpg)

Diagram of a sphere representing the Earth. A horizontal line segment passes through the center, representing a straight tube. A small black dot is placed on the right side of the tube, and a double-headed arrow indicates motion back and forth along the tube.

**Fig. 5.43**

#### **5.64. Mine shaft \*\***

- If the earth had constant density, the gravitational force would decrease linearly with radius as you descend in a mine shaft; see Eq. (5.44). However, the density of the earth is not constant, and in fact the gravitational force *increases* as you descend. Show that the general condition under which this is true is  $\rho_c < (2/3)\rho_{\text{avg}}$ , where  $\rho_{\text{avg}}$  is the average density of the earth, and  $\rho_c$  is the density of the crust at the surface. (The values for the earth are  $\rho_c \approx 3 \text{ g/cm}^3$  and  $\rho_{\text{avg}} \approx 5.5 \text{ g/cm}^3$ .) See Zaidins (1972).
- A similar problem to the one in part (a), which actually turns out to be exactly the same, is the following. Consider a large flat horizontal sheet of material with density  $\rho$  and thickness  $x$ . Show that the gravitational force (from the earth plus the sheet) just below the sheet is larger than the force just above it if  $\rho < (2/3)\rho_{\text{avg}}$ , where  $\rho_{\text{avg}}$  is the average density of the earth. A sheet of wood (with a density roughly equal to that of water) satisfies this inequality, but a sheet of gold doesn't. A result from Problem 5.13 will be useful here.
- Assuming that the density of a planet is a function of radius only, what should  $\rho(r)$  look like if you want the gravitational force to be independent of the depth in a mine shaft, all the way down to the center of the planet?

#### **5.65. Space elevator \*\***

- Let the earth's radius be  $R$ , its average density be  $\rho$ , and its angular frequency of rotation be  $\omega$ . Show that if a satellite is to remain above the same point on the equator at all times, then it must travel in a circle of radius  $\eta R$ , where

$$\eta^3 = \frac{4\pi G\rho}{3\omega^2}. \quad (5.82)$$

What is the numerical value of  $\eta$ ?

- (b) Instead of a satellite, consider a long rope with uniform mass density extending radially from just above the surface of the earth out to a radius  $\eta'R$ .<sup>30</sup> Show that if the rope is to remain above the same point on the equator at all times, then  $\eta'$  must be given by

$$\eta'^2 + \eta' = \frac{8\pi G\rho}{3\omega^2}. \quad (5.83)$$

What is the numerical value of  $\eta'$ ? Where does the tension in the rope achieve its maximum value? *Hint:* no messy calculations required.

#### 5.66. Force from a straight wire \*\*\*

A particle of mass  $m$  is placed a distance  $\ell$  away from an infinitely long straight wire with mass density  $\sigma$  kg/m. Show that the force on the particle is  $F = 2G\sigma m/\ell$ . Do this in two ways:

- Integrate along the wire the contributions to the force.
- Integrate along the wire the contributions to the potential, and then differentiate to obtain the force. You will find that the potential due to the infinite wire is infinite,<sup>31</sup> but you can escape this difficulty by letting the wire have a large but finite length, then finding the potential and force, and then letting the length go to infinity.

#### 5.67. Maximal gravity \*\*\*

Given a point  $P$  in space, and given a piece of malleable material of constant density, how should you shape and place the material in order to create the largest possible gravitational field at  $P$ ?

### Section 5.5: Momentum

#### 5.68. Maximum $P$ and $E$ of a rocket \*

A rocket that starts at rest with mass  $M$  ejects exhaust at a given speed  $u$ . What is the mass of the rocket (including unused fuel) when its momentum is maximum? What is the mass when its energy is maximum?

#### 5.69. Speedy rockets \*

Assume that it is impossible to build a structurally sound container that can hold fuel of more than, say, nine times its mass (the actual limit is higher than this, but let's use this number just to be concrete). It would then seem like the limit for the speed of a rocket is  $u \ln 10$ , from Eq. (5.54). How can you build a rocket that goes faster than this?

<sup>30</sup> Any proposed space elevator wouldn't have uniform mass density. But this simplified problem still gives a good idea of the general features. For more on the space elevator, see Aravind (2007).

<sup>31</sup> There's nothing bad about this. All that matters as far as the force is concerned is differences in the potential, and these differences are finite.

#### **5.70. Snow on a sled, quantitative \*\***

Consider the setup in the example in Section 5.5.1. At  $t = 0$ , let the mass of the sled (including you) be  $M$ , and let its speed be  $V_0$ . If the snow hits the sled at a rate of  $\sigma$  kg/s, find the speed as a function of time for the three cases.

#### **5.71. Leaky bucket \*\*\***

Consider the setup in Problem 5.17, but now let the sand leak at a rate  $dm/dt = -bM$ . In other words, the rate is constant with respect to time, not distance. We've factored out an  $M$  here, just to make the calculations a little nicer.

- Find  $v(t)$  and  $x(t)$  during the time when the bucket contains a nonzero amount of sand.
- What is the maximum value of the bucket's kinetic energy, assuming it is achieved before it hits the wall?
- What is the maximum value of the magnitude of the bucket's momentum, assuming it is achieved before it hits the wall?
- For what value of  $b$  does the bucket become empty right when it hits the wall?

#### **5.72. Throwing a brick \*\*\***

A brick is thrown from ground level, at an angle  $\theta$  with respect to the (horizontal) ground. Assume that the long face of the brick remains parallel to the ground at all times, and that there is no deformation in the ground or the brick when the brick hits the ground. If the coefficient of friction between the brick and the ground is  $\mu$ , what should  $\theta$  be so that the brick travels the maximum total horizontal distance before finally coming to rest? Assume that the brick doesn't bounce. *Hint:* The brick slows down when it hits the ground. Think in terms of impulse.

### *Section 5.7: Collisions*

#### **5.73. A one-dimensional collision \***

Consider the following one-dimensional collision. A mass  $2m$  moves to the right, and a mass  $m$  moves to the left, both with speed  $v$ . They collide elastically. Find their final lab-frame velocities. Solve this by:

- Working in the lab frame.
- Working in the CM frame.

#### **5.74. Perpendicular vectors \***

A moving mass  $m$  collides elastically with a stationary mass  $2m$ . Let their resulting velocities be  $\mathbf{v}_1$  and  $\mathbf{v}_2$ , respectively. Show that  $\mathbf{v}_2$  must be perpendicular to  $2\mathbf{v}_1 + \mathbf{v}_2$ . *Hint:* See Problem 5.19.

![Diagram for problem 5.75: A single pool ball on the left moves with velocity v towards two stationary pool balls stacked vertically on the right.](44851cf2a7ba64610196c82530aae10b_img.jpg)

Diagram for problem 5.75: A single pool ball on the left moves with velocity v towards two stationary pool balls stacked vertically on the right.

Fig. 5.44

#### **5.75. Three pool balls \***

A pool ball with initial speed  $v$  is aimed right between two other pool balls, as shown in Fig. 5.44. If the two right balls leave the (elastic) collision with equal speeds, find the final velocities of all three balls.

![Diagram for problem 5.76: Seven pool balls are arranged in a hexagonal pattern. The center ball is labeled with velocity v to the right. The six surrounding balls are labeled A (top-right), B (bottom-right), C (bottom), D (bottom-left), E (top-left), and F (top).](4302428cd77cf5d8ab4ca5eb6c168282_img.jpg)

Diagram for problem 5.76: Seven pool balls are arranged in a hexagonal pattern. The center ball is labeled with velocity v to the right. The six surrounding balls are labeled A (top-right), B (bottom-right), C (bottom), D (bottom-left), E (top-left), and F (top).

Fig. 5.45

#### **5.76. Seven pool balls \*\***

Seven pool balls are situated at rest as shown in Fig. 5.45. The middle ball suddenly somehow acquires a speed  $v$  to the right. Assume that starting with ball  $A$ , the balls spiral out an infinitesimal amount. So  $A$  is closer to the center ball than  $B$  is, and  $B$  is closer than  $C$  is, etc. This means that the center ball collides with  $A$  first, then it gets deflected into  $B$ , and then it gets deflected into  $C$ , and so on. But all the collisions happen in the blink of an eye. What will the center ball's velocity be after it collides (elastically) with all six balls? (You can use the results from the example in Section 5.7.2.)

#### **5.77. Midair collision \*\***

A ball is held and then released. At the instant it is released, an identical ball, moving horizontally with speed  $v$ , collides elastically with it and is deflected at an upward angle. What is the maximum horizontal distance the latter ball can travel by the time it returns to the height of the collision? (You can use the results from the example in Section 5.7.2.)

#### **5.78. Maximum number of collisions \*\***

$N$  identical balls are constrained to move in one dimension. If you are allowed to pick their initial velocities, what is the maximum number of collisions you can arrange for the balls to have among themselves? Assume that the collisions are elastic.

![Diagram for problem 5.79: A ball is shown moving towards a wall of a triangular room. The wall is a solid line, and the other wall is a dashed line. The angle between the walls is theta. A dashed line represents the angle bisector, and the ball's initial velocity is parallel to it.](50cff0f82f4a4f9197753c66230e573e_img.jpg)

Diagram for problem 5.79: A ball is shown moving towards a wall of a triangular room. The wall is a solid line, and the other wall is a dashed line. The angle between the walls is theta. A dashed line represents the angle bisector, and the ball's initial velocity is parallel to it.

Fig. 5.46

#### **5.79. Triangular room \*\***

A ball is thrown against a wall of a very long triangular room which has vertex angle  $\theta$ . The initial direction of the ball is parallel to the angle bisector (see Fig. 5.46). How many (elastic) bounces does the ball make? Assume that the walls are frictionless.

#### **5.80. Equal angles \*\***

- A mass  $2m$  moving at speed  $v_0$  collides elastically with a stationary mass  $m$ . If the two masses scatter at equal (nonzero) angles with respect to the incident direction, what is this angle?
- What is the largest number that the above “2” can be replaced with, if you want it to be possible for the masses to scatter at equal angles?

#### **5.81. Right angle in billiards \*\***

A billiard ball collides elastically with an identical stationary one. By looking at the collision in the CM frame, show that the angle between the resulting trajectories in the lab frame is  $90^\circ$ . (We proved this result by working in the lab frame in the example in Section 5.7.2.)

#### **5.82. Equal $v_x$ 's \*\***

A mass  $m$  moving with speed  $v$  in the  $x$  direction collides elastically with a stationary mass  $nm$ , where  $n$  is some number. After the collision, it is observed that both masses have equal  $x$  components of their velocities. What angle does the velocity of mass  $nm$  make with the  $x$  axis? (This can be solved by working in the lab frame or the CM frame, but the CM solution is slick.)

#### **5.83. Maximum $v_y$ \*\***

A mass  $M$  moving in the positive  $x$  direction collides elastically with a stationary mass  $m$ . The collision is not necessarily head-on, so the masses may come off at angles, as shown in Fig. 5.47. Let  $\theta$  be the angle of  $m$ 's resulting motion. What should  $\theta$  be so that  $m$  has the largest possible speed in the  $y$  direction? *Hint:* Think about what the collision should look like in the CM frame.

![Diagram of an elastic collision between two masses M and m. Mass M is initially moving to the right with velocity v. After the collision, mass M moves at an angle theta above the horizontal, and mass m moves at an angle theta below the horizontal. The angle theta is measured from the horizontal dashed line.](8efbe26b3ceced80316c76cbceb2bcea_img.jpg)

Diagram of an elastic collision between two masses M and m. Mass M is initially moving to the right with velocity v. After the collision, mass M moves at an angle theta above the horizontal, and mass m moves at an angle theta below the horizontal. The angle theta is measured from the horizontal dashed line.

**Fig. 5.47**

#### **5.84. Bouncing between rings \*\***

Two fixed circular rings, in contact with each other, stand in a vertical plane. A ball bounces elastically back and forth between the rings (see Fig. 5.48). Assume that initial conditions have been set up so that the ball's motion forever lies in one parabola. Let this parabola hit the rings at an angle  $\theta$  from the horizontal. Show that if you want the magnitude of the change in the horizontal component of the ball's momentum at each bounce to be maximum, then you should pick  $\cos \theta = (\sqrt{5} - 1)/2$ , which just happens to be the inverse of the golden ratio.

![Diagram of a ball bouncing between two fixed circular rings. The ball follows a parabolic path (dashed line) between the rings. The angle theta is shown between the horizontal and the path of the ball at the point of contact with one of the rings.](6197a69f6f94513d922787343c666f52_img.jpg)

Diagram of a ball bouncing between two fixed circular rings. The ball follows a parabolic path (dashed line) between the rings. The angle theta is shown between the horizontal and the path of the ball at the point of contact with one of the rings.

**Fig. 5.48**

#### **5.85. Bouncing between surfaces \*\***

Consider the following generalization of the previous exercise. A ball bounces back and forth between a surface defined by  $f(x)$  and its reflection across the  $y$  axis (see Fig. 5.49). Assume that initial conditions have been set up so that the ball's motion forever lies in one parabola, with the contact points located at  $\pm x_0$ . For what function  $f(x)$  is the magnitude of the change in the horizontal component of the ball's momentum at each bounce independent of  $x_0$ ?

![Diagram of a ball bouncing between two surfaces. The surfaces are defined by the function f(x) and its reflection across the y-axis, f(-x). The ball follows a parabolic path (dashed line) between the surfaces. The contact points are at x = -x_0 and x = x_0 on the x-axis.](ff6dc7ee0730f05434751167609d60f3_img.jpg)

Diagram of a ball bouncing between two surfaces. The surfaces are defined by the function f(x) and its reflection across the y-axis, f(-x). The ball follows a parabolic path (dashed line) between the surfaces. The contact points are at x = -x\_0 and x = x\_0 on the x-axis.

**Fig. 5.49**

#### **5.86. Drag force on a sphere \*\***

A sphere of mass  $M$  and radius  $R$  moves with speed  $V$  through a region of space that contains particles of mass  $m$  that are at rest. There are  $n$  of

these particles per unit volume. Assume  $m \ll M$ , and assume that the particles do not interact with each other. What is the drag force on the sphere?

![Diagram for Fig. 5.50 showing a semicircle of N identical balls with total mass M. An incoming ball of mass m is moving towards the semicircle from the left. A dashed arrow points to the left, indicating the final direction of the incoming ball after it has bounced off all N balls.](cd6b945f80140dcb39c162958d040819_img.jpg)

Diagram for Fig. 5.50 showing a semicircle of N identical balls with total mass M. An incoming ball of mass m is moving towards the semicircle from the left. A dashed arrow points to the left, indicating the final direction of the incoming ball after it has bounced off all N balls.

Fig. 5.50

#### 5.87. Balls in a semicircle \*\*\*

$N$  identical balls lie equally spaced in a semicircle on a frictionless horizontal table, as shown. The total mass of these balls is  $M$ . Another ball of mass  $m$  approaches the semicircle from the left, with the proper initial conditions so that it bounces (elastically) off all  $N$  balls and finally leaves the semicircle, heading directly to the left (see Fig. 5.50).

- In the limit  $N \rightarrow \infty$  (so the mass of each ball in the semicircle,  $M/N$ , goes to zero), find the minimum value of  $M/m$  that allows the incoming ball to come out heading directly to the left. *Hint:* You'll need to do Problem 5.24 first.
- In the minimum  $M/m$  case found in part (a), show that the ratio of  $m$ 's final speed to initial speed equals  $e^{-\pi}$ .

#### 5.88. Block and bouncing ball \*\*\*\*

A block with large mass  $M$  slides with speed  $V_0$  on a frictionless table toward a wall. It collides elastically with a ball with small mass  $m$ , which is initially at rest at a distance  $L$  from the wall. The ball slides toward the wall, bounces elastically, and then proceeds to bounce back and forth between the block and the wall.

- How close does the block come to the wall?
- How many times does the ball bounce off the block, by the time the block makes its closest approach to the wall?

Assume  $M \gg m$ , and give your answers to leading order in  $m/M$ .

### Section 5.8: Inherently inelastic processes

*Note: In the exercises involving chains in this section, we'll assume that the chains are of the type described in the first scenario near the end of Section 5.8.*

#### 5.89. Slowing down, speeding up \*

A plate of mass  $M$  moves horizontally with initial speed  $v$  on a frictionless table. A mass  $m$  is dropped vertically onto it and soon comes to rest with respect to it. How much energy is required to bring the system back up to speed  $v$ ? Explain intuitively your answer in the  $M \gg m$  limit.

#### 5.90. Pulling a chain back \*\*

A chain with length  $L$  and mass density  $\sigma$  kg/m lies outstretched on a frictionless horizontal table. You grab one end and pull it back along

itself, in a parallel manner, as shown in Fig. 5.51. If your hand starts from rest and has constant acceleration  $a$ , what is your force at the moment right before the chain is straightened out?

#### **5.91. Falling chain \*\***

A chain with length  $L$  and mass density  $\sigma$  kg/m is held in a heap, and you grab an end that protrudes a tiny bit out of the top. The chain is then released. As a function of time, what is the force that your hand must apply to keep the top end of the chain motionless? Assume that the chain has no friction with itself, so that the remaining part of the heap is always in freefall. The setup at a random later time is shown in Fig. 5.52.

#### **5.92. Pulling a chain down \*\***

A chain with mass density  $\sigma$  kg/m lies in a heap at the edge of a table. One end of the chain initially sticks out an infinitesimal distance from the heap. You grab this end and accelerate it downward with acceleration  $a$ . Assume that there is no friction of the chain with itself as it unravels. As a function of time, what force does your hand apply to the chain? Find the value of  $a$  that makes your force always equal to zero. (In other words, find the  $a$  with which the chain naturally falls.)

#### **5.93. Raising a chain \*\***

A chain with length  $L$  and mass density  $\sigma$  kg/m lies in a heap on the floor. You grab one end of the chain and pull upward with a force such that the chain moves at constant speed  $v$ . What is the total work you do, by the time the chain is completely off the floor? How much energy is lost to heat, if any? Assume that the chain is greased, so that it has no friction with itself.

#### **5.94. Downhill dustpan \*\***

A plane inclined at an angle  $\theta$  is covered with dust. An essentially massless dustpan on wheels is released from rest and rolls down the plane, gathering up dust. The density of dust in the path of the dustpan is  $\sigma$  kg/m. What is the acceleration of the dustpan?

#### **5.95. Heap and block \*\***

A chain with mass density  $\sigma$  kg/m lies in a heap on the floor, with one end attached to a block of mass  $M$ . The block is given a sudden kick and instantly acquires a speed  $V_0$ . Let  $x$  be the distance traveled by the block. In terms of  $x$ , what is the tension in the chain, just to the right of the heap; that is, at the point  $P$  shown in Fig. 5.53? There is no friction in this problem; none with the floor, and none in the chain with itself.

![Diagram for Fig. 5.51: A top view of a hand pulling a chain. The hand is at the left end of a horizontal line representing the chain. An arrow labeled 'a' points to the right from the hand. The total length of the chain is labeled 'L'.](4e08052e5ade976df8313494418ca5a9_img.jpg)

(top view)

Diagram for Fig. 5.51: A top view of a hand pulling a chain. The hand is at the left end of a horizontal line representing the chain. An arrow labeled 'a' points to the right from the hand. The total length of the chain is labeled 'L'.

**Fig. 5.51**

![Diagram for Fig. 5.52: A side view of a hand pulling a chain down. The hand is at the top, holding a vertical chain. The bottom of the chain is in a dark, irregular shape labeled 'heap'. A downward arrow is next to the heap.](bd27737285c2ebfbc333f562018b2c6e_img.jpg)

Diagram for Fig. 5.52: A side view of a hand pulling a chain down. The hand is at the top, holding a vertical chain. The bottom of the chain is in a dark, irregular shape labeled 'heap'. A downward arrow is next to the heap.

**Fig. 5.52**

![Diagram for Fig. 5.53: Two diagrams showing a block of mass M on a horizontal surface. The top diagram, labeled '(start)', shows a block M with a small heap of mass m to its left. An arrow above the block is labeled V_0. The bottom diagram, labeled '(later)', shows the block M has moved to the right by a distance x. The heap is now at point P. An arrow above the block indicates it is still moving to the right.](ffb3921a6f833113c7d9e204d1eded5f_img.jpg)

Diagram for Fig. 5.53: Two diagrams showing a block of mass M on a horizontal surface. The top diagram, labeled '(start)', shows a block M with a small heap of mass m to its left. An arrow above the block is labeled V\_0. The bottom diagram, labeled '(later)', shows the block M has moved to the right by a distance x. The heap is now at point P. An arrow above the block indicates it is still moving to the right.

**Fig. 5.53**

![Diagram of a chain hanging from a spring. A horizontal ceiling is at the top. A spring with spring constant k is attached to the ceiling. A chain of length L and mass density sigma hangs vertically from the spring. The bottom of the chain is labeled 'heap' and is resting on a horizontal floor.](7998f3854052b6c62ad17672f52bb6ea_img.jpg)

Diagram of a chain hanging from a spring. A horizontal ceiling is at the top. A spring with spring constant k is attached to the ceiling. A chain of length L and mass density sigma hangs vertically from the spring. The bottom of the chain is labeled 'heap' and is resting on a horizontal floor.

Fig. 5.54

#### 5.96. Touching the floor \*\*\*\*

A chain with mass density  $\sigma$  kg/m hangs from a spring with spring constant  $k$ . In the equilibrium position, a length  $L$  is in the air, and the bottom part of the chain lies in a heap on the floor; see Fig. 5.54. The chain is raised by a very small distance,  $b$ , and then released. What is the amplitude of the oscillations, as a function of time?

Assume that (1)  $L \gg b$ , (2) the chain is very thin, so that the size of the heap on the floor is very small compared with  $b$ , (3) the length of the chain in the initial heap is larger than  $b$ , so that some of the chain always remains in contact with the floor, and (4) there is no friction of the chain with itself inside the heap.

## 5.11 Solutions

#### 5.1. Minimum length

Drop the masses through the three holes, and let the system reach its equilibrium position. The equilibrium position is the one with the lowest potential energy of the masses, that is, the one with the most string hanging below the table. In other words, it is the one with the least string lying on the table. This is the desired minimum-length configuration.

What are the angles at the vertex of the string? The tensions in all three strings are equal to  $mg$ , because they are holding up the masses. The vertex of the string is in equilibrium, so the net force on it must be zero. This implies that each string must bisect the angle formed by the other two. Therefore, the angles between the strings must all be  $120^\circ$ .

#### 5.2. Heading to zero

The energy of the particle is  $E = mv^2/2 - A|x|^n$ . The given information tells us that  $v = 0$  when  $x = 0$ . Therefore,  $E = 0$ , which then implies that  $v = -\sqrt{2Ax^n/m}$  (we'll assume  $x > 0$ ; the  $x < 0$  case works the same). We have chosen the minus sign because the particle is heading toward the origin. Writing  $v$  as  $dx/dt$  and separating variables gives

$$\int_{x_0}^0 \frac{dx}{x^{n/2}} = -\sqrt{\frac{2A}{m}} \int_0^T dt = -T\sqrt{\frac{2A}{m}}, \quad (5.84)$$

where  $x_0$  is the initial position and  $T$  is the time to reach the origin. The integral on the left is finite if and only if  $n/2 < 1$ . Therefore, the condition that  $T$  is finite is  $n < 2$ .

**REMARK:** If  $0 < n < 1$ , then  $V(x)$  has a cusp at  $x = 0$  (infinite slope on either side), so it's clear that  $T$  is finite. If  $n = 1$ , then the slope is a finite constant, so it's also clear that  $T$  is finite. If  $n > 1$ , then the slope of  $V(x)$  is zero at  $x = 0$ , so it's not obvious what happens with  $T$ . But the above calculation shows that  $n = 2$  is the value where  $T$  becomes infinite.

The particle therefore takes a finite time to reach the top of a triangle or the curve  $-Ax^{3/2}$ . But it takes an infinite time to reach the top of a parabola, cubic, etc. A circle looks like a parabola at the top, so  $T$  is infinite in that case also. In fact, any nice polynomial function  $V(x)$  requires an infinite  $T$  to reach a local maximum, because the Taylor series starts at order two (at least) around an extremum. ♣

#### 5.3. Leaving the sphere

FIRST SOLUTION: Let  $R$  be the radius of the sphere, and let  $\theta$  be the angle of the mass, measured from the top of the sphere. The radial  $F = ma$  equation is

$$mg \cos \theta - N = \frac{mv^2}{R}, \quad (5.85)$$

where  $N$  is the normal force. The mass loses contact with the sphere when the normal force becomes zero (that is, when the normal component of gravity is barely large enough to account for the centripetal acceleration of the mass). Therefore, the mass loses contact when

$$\frac{mv^2}{R} = mg \cos \theta. \quad (5.86)$$

But conservation of energy gives  $mv^2/2 = mgR(1 - \cos \theta)$ . Hence,  $v = \sqrt{2gR(1 - \cos \theta)}$ . Plugging this into Eq. (5.86) gives

$$\cos \theta = \frac{2}{3} \implies \theta \approx 48.2^\circ. \quad (5.87)$$

SECOND SOLUTION: Let's assume (incorrectly) that the mass always stays in contact with the sphere, and then find the point where the horizontal component of  $v$  starts to decrease, which it of course can't do, because the normal force doesn't have a "backward" component. From above, the horizontal component of  $v$  is

$$v_x = v \cos \theta = \sqrt{2gR(1 - \cos \theta)} \cos \theta. \quad (5.88)$$

Taking the derivative of this, we find that the maximum occurs when  $\cos \theta = 2/3$ . So this is where  $v_x$  would start to decrease if the mass were constrained to remain on the sphere. But there is no such constraining force available, so the mass loses contact when  $\cos \theta = 2/3$ .

#### 5.4. Pulling the pucks

- (a) Let  $\theta$  be defined as in Fig. 5.55. Then the tension in the string is  $T = F/(2 \cos \theta)$ , because the force on the massless kink in the string must be zero. Consider the "top" puck. The component of the tension in the  $y$  direction is  $-T \sin \theta = -(F/2) \tan \theta$ . The work done on the puck by this component is therefore

$$\begin{aligned} W_y &= \int_{\ell}^0 \frac{-F \tan \theta}{2} dy = \int_{\pi/2}^0 \frac{-F \tan \theta}{2} d(\ell \sin \theta) \\ &= \int_{\pi/2}^0 \frac{-F \ell \sin \theta}{2} d\theta \\ &= \frac{F \ell \cos \theta}{2} \Big|_{\pi/2}^0 = \frac{F \ell}{2}. \end{aligned} \quad (5.89)$$

By the work-energy theorem (or equivalently, by separating variables and integrating  $F_y = mv_y dv_y/dy$ ), this work equals the value of  $mv_y^2/2$  right before the collision. There are two pucks, so the total kinetic energy lost when they stick together is twice this quantity ( $v_x$  doesn't change during the collision), which is  $F\ell$ .

- (b) Consider two systems,  $A$  and  $B$  (see Fig. 5.56).  $A$  is the original setup, while  $B$  starts with  $\theta$  already at zero. Let the pucks in both systems start simultaneously at  $x = 0$ . As the force  $F$  is applied, all four pucks will have the same  $x(t)$ , because the same force in the  $x$  direction, namely  $F/2$ , is applied to every puck at all times. After the collision, both systems will therefore look exactly the same.

Let the collision of the pucks occur at  $x = d$ . At this point,  $F(d + \ell)$  work has been done on system  $A$ , because the center of the string (where the force

![Figure 5.55: A diagram showing a string with a kink being pulled by a force F. The string makes an angle theta with the horizontal dashed line. The tension T is shown in the two segments of the string. A coordinate system with x and y axes is shown to the right.](1f9fc61a1c5468ca8f88476acb978ed8_img.jpg)

Figure 5.55: A diagram showing a string with a kink being pulled by a force F. The string makes an angle theta with the horizontal dashed line. The tension T is shown in the two segments of the string. A coordinate system with x and y axes is shown to the right.

Fig. 5.55

![Figure 5.56: A diagram showing two systems, A and B. System A shows a string with a kink being pulled by a force F. System B shows two pucks being pulled by a force F. Both systems are shown with a horizontal dashed line indicating the direction of the force.](f85b347348cfdfbda4307d90a185b84a_img.jpg)

Figure 5.56: A diagram showing two systems, A and B. System A shows a string with a kink being pulled by a force F. System B shows two pucks being pulled by a force F. Both systems are shown with a horizontal dashed line indicating the direction of the force.

Fig. 5.56

![Diagram showing a force F applied to a system, represented by a dashed arrow pointing right from a curved line.](a0c84ac28b8247bc75800a063509d396_img.jpg)

Diagram showing a force F applied to a system, represented by a dashed arrow pointing right from a curved line.

Fig. 5.57

is applied) ends up moving a distance  $\ell$  more than the masses. However, only  $Fd$  work has been done on system  $B$ . Since both systems have the same kinetic energy after the collision, the extra  $F\ell$  work done on system  $A$  must be what is lost in the collision.

REMARK: The reasoning in this second solution can be used to solve the problem in the case where we have a uniform massive rope (so the rope flops down, as in Fig. 5.57). The center of mass of the rope moves in exactly the same manner as the position of the two pucks in system  $B$  (assuming that the mass of each puck is chosen to be half the mass of the rope), because the same force  $F$  acts on both systems. You can show that this implies that the force acts over an extra distance of  $\ell/2$  on the rope, compared with system  $B$ , by the time the rope has flopped into a straight line. From the reasoning above,  $F\ell/2$  of work must therefore be lost to heat in the rope. ♣

#### 5.5. Constant $\dot{y}$

By conservation of energy, the bead's speed at any time is given by (note that  $y$  is negative here)

$$\frac{1}{2}mv^2 + mgy = \frac{1}{2}mv_0^2 \implies v = \sqrt{v_0^2 - 2gy}. \quad (5.90)$$

The vertical component of the velocity is  $\dot{y} = v \sin \theta$ , where  $\theta$  is the (negative) angle the wire makes with the horizontal. The slope of the wire is  $\tan \theta = dy/dx \equiv y'$ , which yields  $\sin \theta = y'/\sqrt{1+y'^2}$ . The requirement  $\dot{y} = -v_0$ , which is equivalent to  $v \sin \theta = -v_0$ , may therefore be written as

$$\sqrt{v_0^2 - 2gy} \cdot \frac{y'}{\sqrt{1+y'^2}} = -v_0. \quad (5.91)$$

Squaring both sides and solving for  $y' \equiv dy/dx$  yields  $dy/dx = -v_0/\sqrt{-2gy}$ . Separating variables and integrating gives

$$\int \sqrt{-2gy} dy = -v_0 \int dx \implies \frac{(-2gy)^{3/2}}{3g} = v_0x, \quad (5.92)$$

where the constant of integration has been set to zero, because  $(x,y) = (0,0)$  is a point on the curve. Therefore,

$$y = -\frac{(3gv_0x)^{2/3}}{2g}. \quad (5.93)$$

#### 5.6. Dividing the heat

It turns out that it isn't possible to answer these questions without being given more information. The way that the work is divided up between the objects depends on what their surfaces look like. It's theoretically possible for one of the objects to gain all the heat, while the other doesn't heat up at all.

To understand this, we'll need to make a model of how friction works. The general way that friction works is that molecules from one surface rub against molecules from the other surface. The molecules stretch to the side and then bounce back and vibrate. This vibrational motion is the kinetic energy associated with heat. The model we'll use here will have a bunch of springs with masses on the ends, on both surfaces at the interface. When the surfaces rub against each other, the masses catch on each other for a short time (as shown in Fig. 5.58), and then they release, whereupon they vibrate back and forth on the springs. This is the kinetic energy of the heat we see. Though an oversimplification, this is basically the way friction works.

Now, if everything is symmetrical between the two objects (that is, if the springs and masses on one object look like those on the other), then both objects will heat up by

![Diagram showing a block on a table with a spring-like interface between them, representing friction. A force F is applied to the block.](1985c43eab491bdc8421092a0d50093d_img.jpg)

Diagram showing a block on a table with a spring-like interface between them, representing friction. A force F is applied to the block.

Fig. 5.58

the same amount. But things need not be symmetrical. You can imagine the springs on one surface being much stiffer (that is, having a much larger  $k$  value) than the springs on the other surface. Or, you can even take the limit where one surface (say, the block) is made of completely rigid teeth, as shown (for one tooth) in Fig. 5.59. In this case, only the bottom surface (the table) will end up with heat from vibrational motion.

Is this asymmetrical result consistent with what we obtain from the work–energy theorem? Well, the net work done on the block is zero, because your pulling force does  $Fd$  positive work (where  $F = \mu_k N$ ), while the friction force (the sum of all the forces from the masses on the little teeth) does  $Fd$  negative work. Therefore, since zero net work is done on the block, its total energy is constant. And since the kinetic energy due to its motion as a whole is constant, its internal thermal energy must also be constant. In other words, it doesn’t heat up.

The net work done on the table in this scenario comes from the force from the teeth on the little masses on the springs. These teeth do  $Fd$  positive work on all the little spring–mass systems, so  $Fd$  is the work done on the table. Therefore, its total energy increases by  $Fd$ . And since the kinetic energy due to its motion as a whole is constant (and zero, since the table is just sitting there), its internal thermal energy must increase by  $Fd$ . In other words, it heats up.

Now consider the reverse situation, where the table has the rigid teeth and the block has the springs and masses, as shown in Fig. 5.60. The block is now the object that heats up, because it has the vibrational motion of the masses. And as above, we can show that this is consistent with the work–energy theorem, as follows. In the present case, the force from the table’s teeth does no work on the block (because the teeth aren’t moving), so the net work done on the block is simply the  $Fd$  from your pulling, so it heats up. Likewise, the little masses do no work on the teeth (because the teeth aren’t moving), so the work done on the table is zero, so it doesn’t heat up.

For the in between case where the spring constants on the two objects are equal, the net work done on each object is  $Fd/2$ , where  $d$  is the distance the block moves. This is true because the two masses in Fig. 5.58 each move half as far as the block moves. So the work done on the block is  $Fd - Fd/2 = Fd/2$  (this is the positive work done by you, plus the negative work done by the table’s little masses). And the work done on the table is  $Fd/2$  (this is the positive work done by the block’s little masses). So the objects heat up the same amount. For more discussion of the issues in this problem, see Sherwood (1984).

#### 5.7. $V(x)$ vs. a hill

FIRST SOLUTION: Consider the normal force  $N$  acting on the bead at a given point. Let  $\theta$  be the angle that the tangent to  $V(x)$  makes with the horizontal, as shown in Fig. 5.61. The horizontal  $F = ma$  equation is

$$-N \sin \theta = m\ddot{x}. \tag{5.94}$$

The vertical  $F = ma$  equation is

$$N \cos \theta - mg = m\ddot{y} \implies N \cos \theta = mg + m\ddot{y}. \tag{5.95}$$

Dividing Eq. (5.94) by Eq. (5.95) gives

$$-\tan \theta = \frac{\ddot{x}}{g + \ddot{y}}. \tag{5.96}$$

But  $\tan \theta = V'(x)$ . Therefore,

$$\ddot{x} = -(g + \ddot{y})V'. \tag{5.97}$$

We see that this is not equal to  $-gV'$ . In fact, there is in general no way to construct a curve with height  $z(x)$  that gives the same horizontal motion that a 1-D potential  $mgV(x)$  gives, for all initial conditions. We would need  $-(g + \ddot{z})z' = -gV'$ , for all  $x$ . But at a given  $x$ , the quantities  $V'$  and  $z'$  are fixed, whereas  $\ddot{z}$  depends on the initial

![Diagram Fig. 5.59: A block is on a table. The bottom surface of the block has a series of small teeth pointing downwards. A spring is attached to one of these teeth and a small mass. A force F is applied to the right on the block.](12798d734beb1e72231b42507f502e7e_img.jpg)

Diagram Fig. 5.59: A block is on a table. The bottom surface of the block has a series of small teeth pointing downwards. A spring is attached to one of these teeth and a small mass. A force F is applied to the right on the block.

Fig. 5.59

![Diagram Fig. 5.60: A block is on a table. The top surface of the table has a series of small teeth pointing upwards. A spring is attached to one of these teeth and a small mass on the block. A force F is applied to the right on the block.](5f18cfdd98c3e349032c61a75791fdcc_img.jpg)

Diagram Fig. 5.60: A block is on a table. The top surface of the table has a series of small teeth pointing upwards. A spring is attached to one of these teeth and a small mass on the block. A force F is applied to the right on the block.

Fig. 5.60

![Diagram Fig. 5.61: A bead is on a curve V(x). A force N acts perpendicular to the tangent of the curve at the bead's position. A force mg acts vertically downwards. The angle theta is shown between the normal force N and the vertical dashed line, and also between the tangent line and the horizontal dashed line.](bab4ada8ffecbdfbc2dc40e0bd98d075_img.jpg)

Diagram Fig. 5.61: A bead is on a curve V(x). A force N acts perpendicular to the tangent of the curve at the bead's position. A force mg acts vertically downwards. The angle theta is shown between the normal force N and the vertical dashed line, and also between the tangent line and the horizontal dashed line.

Fig. 5.61

conditions. For example, if there is a bend in the wire, then  $\ddot{z}$  will be large if  $\dot{z}$  is large. And  $\dot{z}$  depends (in general) on how far the bead has fallen.

Equation (5.97) holds the key to constructing a situation that does give the  $\ddot{x} = -gV'$  result. All we have to do is get rid of the  $\ddot{y}$  term. So here's what we do. We grab our  $y = V(x)$  wire and move it up and/or down in precisely the manner that makes the bead stay at the same height with respect to the ground. (Actually, constant vertical speed would be good enough.) This will make the  $\ddot{y}$  term vanish, as desired. The vertical movement of the curve doesn't change the slope  $V'$  at a given value of  $x$ , so the  $\theta$  in the above derivation is still the same  $\theta$ .

Note that the quantity  $y$  here is the vertical position of the bead. It equals  $V(x)$  if the curve is stationary, but not if the curve is being moved up and down.

**REMARK:** There is one case where  $\ddot{x}$  is (approximately) equal to  $-gV'$ , even when the wire remains stationary. In the case of small oscillations of the bead near a minimum of  $V(x)$ ,  $\ddot{y}$  is small compared with  $g$ . Hence, Eq. (5.97) shows that  $\ddot{x}$  is approximately equal to  $-gV'$ . Therefore, for small oscillations, it is reasonable to model a particle in a 1-D potential  $mgV(x)$  as a particle sliding in a valley whose height is given by  $y = V(x)$ . ♣

**SECOND SOLUTION:** The component of gravity along the wire is what causes the change in velocity of the bead. That is,

$$-g \sin \theta = \frac{dv}{dt}, \quad (5.98)$$

where  $\theta$  is given by

$$\tan \theta = V'(x) \implies \sin \theta = \frac{V'}{\sqrt{1+V'^2}}, \quad \cos \theta = \frac{1}{\sqrt{1+V'^2}}. \quad (5.99)$$

We are, however, not concerned with the rate of change of  $v$ , but rather with the rate of change of  $\dot{x}$ . In view of this, let us write  $v$  in terms of  $\dot{x}$ . Since  $\dot{x} = v \cos \theta$ , we have  $v = \dot{x} / \cos \theta = \dot{x} \sqrt{1+V'^2}$  (dots denote  $d/dt$ , primes denote  $d/dx$ ). Therefore, Eq. (5.98) becomes

$$\begin{aligned} \frac{-gV'}{\sqrt{1+V'^2}} &= \frac{d}{dt} \left( \dot{x} \sqrt{1+V'^2} \right) \\ &= \ddot{x} \sqrt{1+V'^2} + \frac{\dot{x}V'(dV'/dt)}{\sqrt{1+V'^2}}. \end{aligned} \quad (5.100)$$

Hence,  $\ddot{x}$  is given by

$$\ddot{x} = \frac{-gV'}{1+V'^2} - \frac{\dot{x}V'(dV'/dt)}{1+V'^2}. \quad (5.101)$$

We'll simplify this in a moment, but first a remark.

**REMARK:** A common incorrect solution to this problem is the following. The acceleration along the curve is  $g \sin \theta = -g(V'/\sqrt{1+V'^2})$ . Calculating the horizontal component of this acceleration brings in a factor of  $\cos \theta = 1/\sqrt{1+V'^2}$ . Therefore, we might think that

$$\ddot{x} = \frac{-gV'}{1+V'^2} \quad (\text{incorrect}). \quad (5.102)$$

We have missed the second term in Eq. (5.101). Where is the mistake? The error is that we forgot to take into account the possible change in the curve's slope (Eq. (5.102) is true for straight lines). We addressed only the acceleration due to a change in *speed*. We forgot to consider the acceleration due to a change in the *direction* of motion (the term we missed is the one with  $dV'/dt$ ). Intuitively, if we have a sharp enough bend in

the wire, then  $\dot{x}$  can change at an arbitrarily large rate, even if  $v$  is roughly constant. In view of this fact, Eq. (5.102) is definitely incorrect, because it is bounded (by  $g/2$ , in fact). ♣

To simplify Eq. (5.101), note that  $V' \equiv dV/dx = (dV/dt)/(dx/dt) \equiv \dot{V}/\dot{x}$  ( $\dot{V}$  is just the rate of change in the bead's height). Therefore, the numerator in the second term on the right-hand side of Eq. (5.101) is

$$\begin{aligned}\dot{x}V' \frac{dV'}{dt} &= \dot{x}V' \frac{d}{dt} \left( \frac{\dot{V}}{\dot{x}} \right) = \dot{x}V' \left( \frac{\dot{x}\ddot{V} - \dot{V}\ddot{x}}{\dot{x}^2} \right) \\ &= V'\ddot{V} - V'\ddot{x} \left( \frac{\dot{V}}{\dot{x}} \right) = V'\ddot{V} - V'^2\ddot{x}.\end{aligned}\quad (5.103)$$

Substituting this into Eq. (5.101) yields

$$\ddot{x} = -(g + \ddot{V})V', \quad (5.104)$$

in agreement with Eq. (5.97), because  $y = V(x)$  if the wire is stationary. Equation (5.104) is valid only for a curve  $V(x)$  that remains fixed. If we grab the wire and start moving it up and down, then the above solution is invalid, because the starting point, Eq. (5.98), rests on the assumption that gravity is the only force that does work on the bead. But if we move the wire, then the normal force also does work.

It turns out that for a moving wire, we simply need to replace the  $\ddot{V}$  in Eq. (5.104) by  $\ddot{y}$ , which then gives Eq. (5.97). This can be seen by looking at things in the vertically accelerating frame in which the wire is at rest. We won't cover accelerating frames until Chapter 10, so we'll just invoke here the result that there is an extra fictitious "translational" force in this accelerating frame, and the consequence of this is that the bead thinks that it lives in a world where the acceleration from gravity is  $g + \ddot{h}$  (if  $\ddot{h}$  is positive, then the bead thinks gravity is larger), where  $h$  is the position of your hand that is accelerating the wire. In this new frame, the wire is at rest, so the above solution is valid. So with the  $g$  in Eq. (5.104) replaced by  $g + \ddot{h}$ , we have  $\ddot{x} = -(g + \ddot{h} + \ddot{V})V'$ . But  $\ddot{V}$  (which is the vertical acceleration of the bead with respect to the new frame) plus  $\ddot{h}$  (which is the vertical acceleration of the new frame with respect to the ground) equals  $\ddot{y}$  (which, by our definition in the first solution, is the vertical acceleration of the bead with respect to the ground). We have therefore reproduced Eq. (5.97).

#### 5.8. Hanging mass

We will calculate the equilibrium point  $y_0$ , and then use  $\omega = \sqrt{V''(y_0)/m}$ . The derivative of  $V$  is

$$V'(y) = ky + mg. \quad (5.105)$$

Therefore,  $V'(y) = 0$  when  $y = -mg/k \equiv y_0$ . The second derivative of  $V$  is

$$V''(y) = k. \quad (5.106)$$

We therefore have

$$\omega = \sqrt{\frac{V''(y_0)}{m}} = \sqrt{\frac{k}{m}}. \quad (5.107)$$

REMARK: This is independent of  $y_0$ , which makes sense because the only effect of gravity is to change the equilibrium position. More precisely, if  $y_r$  is the position relative to  $y_0$  (so that  $y \equiv y_0 + y_r$ ), then the total force as a function of  $y_r$  is

$$F(y_r) = -k(y_0 + y_r) - mg = -k \left( -\frac{mg}{k} + y_r \right) - mg = -ky_r, \quad (5.108)$$

so it still looks like a regular spring. (This works only because the spring force is linear.) Alternatively, you can think in terms of the potential energy; this is the task of Exercise 5.42. ♣

#### 5.9. Small oscillations

We will calculate the equilibrium point  $x_0$ , and then use  $\omega = \sqrt{V''(x_0)/m}$ . The derivative of  $V$  is

$$V'(x) = -Ce^{-ax}x^{n-1}(n - ax). \quad (5.109)$$

Therefore,  $V'(x) = 0$  when  $x = n/a \equiv x_0$ . The second derivative of  $V$  is

$$V''(x) = -Ce^{-ax}x^{n-2}((n - 1 - ax)(n - ax) - ax). \quad (5.110)$$

Plugging in  $x_0 = n/a$  simplifies this a bit, and we find

$$\omega = \sqrt{\frac{V''(x_0)}{m}} = \sqrt{\frac{Ce^{-n}n^{n-1}}{ma^{n-2}}}. \quad (5.111)$$

![Diagram of a sphere with a point P inside. A chord AB passes through P. Two small triangles, A'P and B'P, are shown with their bases on the sphere's surface. The angles at P for these triangles are equal, illustrating the geometric relationship used in the proof of the zero force inside a spherical shell.](beea498838882be6c29e8393232da81d_img.jpg)

Diagram of a sphere with a point P inside. A chord AB passes through P. Two small triangles, A'P and B'P, are shown with their bases on the sphere's surface. The angles at P for these triangles are equal, illustrating the geometric relationship used in the proof of the zero force inside a spherical shell.

Fig. 5.62

#### 5.10. Zero force inside a sphere

Let  $a$  be the distance from  $P$  to piece  $A$ , and let  $b$  be the distance from  $P$  to piece  $B$  (see Fig. 5.62). Draw the “perpendicular” bases of the cones, and call them  $A'$  and  $B'$ . The ratio of the areas of  $A'$  and  $B'$  is  $a^2/b^2$ . The key point here is that the angle between the planes of  $A$  and  $A'$  is the same as the angle between  $B$  and  $B'$ . This is true because the chord between  $A$  and  $B$  meets the circle at equal angles at its ends. So the ratio of the areas of  $A$  and  $B$  is also  $a^2/b^2$ . But the gravitational force decreases like  $1/r^2$ , and this effect exactly cancels the  $a^2/b^2$  ratio of the areas. Therefore, the forces at  $P$  due to  $A$  and  $B$  (which can be treated like point masses, because the cones are assumed to be thin) are equal in magnitude; and opposite in direction, of course. If we draw enough cones to cover the whole shell, then the contributions to the force from little pieces over the whole shell cancel in pairs, so we are left with zero force at  $P$ . This holds for any point  $P$  inside the shell.

**REMARK:** Interestingly, the force inside an ellipsoidal shell of constant density (per volume) is also zero, assuming that the shell is defined to be the region between the surfaces described by  $ax^2 + by^2 + cz^2 = k$ , for two different values of  $k$ . In short, this is true because an ellipsoid is simply a stretched sphere. In detail: Let the above spherical shell have some thickness  $dr$  (which was irrelevant for the sphere, but it will be important in the ellipsoid case). From above, we know that the masses at the ends of the thin cones in the sphere have canceling forces. If we now stretch the sphere into an ellipsoid (uniformly in each direction, but the factors in the three directions can be different), then the distances from the end masses to  $P$  will still be in the ratio of  $a$  to  $b$  (as you can verify). And the end masses will still be in the ratio of  $a^2$  to  $b^2$ , because both masses change by the same factor. This is true because every infinitesimal cube in the end masses has its volume changed by the same factor (namely  $f_x f_y f_z$ , where these  $f$ 's are the stretching factors in each direction). So the masses are still in the ratio of  $a^2$  to  $b^2$ , and the same argument about canceling forces holds as in the spherical case. Note that this zero-force result is *not* true for an ellipsoid with constant thickness, because such an object isn't the result of stretching a spherical shell (because a stretching results in the ellipsoidal shell being thicker near the ends where it is more “pointy”). ♣

#### 5.11. Escape velocity

- (a) The cutoff case is where the particle barely makes it to infinity, that is, where its speed is zero at infinity. Conservation of energy for this situation gives

$$\frac{1}{2}mv_{\text{esc}}^2 - \frac{GMm}{R} = 0 + 0. \quad (5.112)$$

In other words, the initial kinetic energy,  $mv_{\text{esc}}^2/2$ , must account for the gain in potential energy,  $GMm/R$ . Therefore,

$$v_{\text{esc}} = \sqrt{\frac{2GM}{R}}. \quad (5.113)$$

In terms of the acceleration,  $g = GM/R^2$ , at the surface of a planet, we can write this as  $v_{\text{esc}} = \sqrt{2gR}$ . Using  $M = 4\pi\rho R^3/3$ , we can also write it as  $v_{\text{esc}} = \sqrt{8\pi GR^2\rho/3}$ . So for a given density  $\rho$ ,  $v_{\text{esc}}$  grows like  $R$ . Using the values of  $g$  and  $R$  given in Appendix J, we have:

$$\text{For the earth, } v_{\text{esc}} = \sqrt{2gR} \approx \sqrt{2(9.8 \text{ m/s}^2)(6.4 \cdot 10^6 \text{ m})} \approx 11.2 \text{ km/s.}$$

$$\text{For the moon, } v_{\text{esc}} = \sqrt{2gR} \approx \sqrt{2(1.6 \text{ m/s}^2)(1.7 \cdot 10^6 \text{ m})} \approx 2.3 \text{ km/s.}$$

$$\text{For the sun, } v_{\text{esc}} = \sqrt{2gR} \approx \sqrt{2(270 \text{ m/s}^2)(7.0 \cdot 10^8 \text{ m})} \approx 620 \text{ km/s.}$$

REMARK: Another reasonable question to ask is: what is the escape velocity from the sun for an object located where the earth is (but imagine that the earth isn't there)? The answer is  $\sqrt{2GM_S/R_{\text{ES}}}$ , where  $R_{\text{ES}}$  is the earth–sun distance. Numerically, this is

$$\sqrt{2(6.67 \cdot 10^{-11} \text{ m}^3/\text{kg s}^2)(2 \cdot 10^{30} \text{ kg})/(1.5 \cdot 10^{11} \text{ m})} \approx 42 \text{ km/s.} \quad (5.114)$$

If you want to bring the earth back in (but let's assume it's at rest and not orbiting) and find the escape velocity (from both the sun and the earth) from a point on the earth's surface, you can't just add the 42 km/s and 11.2 km/s results. Instead, you have to take the square root of the sum of the squares. This follows from Eq. (5.112) and from the fact that potentials simply add. The result is about 43.5 km/s. The task of Exercise 5.60 is to find the escape velocity if the orbital motion of the earth is included. ♣

- (b) To get a rough answer, we'll assume that the initial speed of a person's jump on the small planet is the same as it is on the earth. This probably isn't quite true, but it's close enough for the purposes here. A good jump on the earth is about a meter. For this jump, conservation of energy gives  $mv^2/2 = mg(1 \text{ m})$ . Therefore,  $v = \sqrt{2g(1 \text{ m})} \approx \sqrt{20} \text{ m/s}$ . So we want  $\sqrt{20} \text{ m/s} = \sqrt{8\pi GR^2\rho/3}$ . Using  $\rho \approx 5500 \text{ kg/m}^3$ , we find  $R \approx 2.5 \text{ km}$ . On such a planet, you should tread lightly.

#### 5.12. Ratio of potentials

Let  $\rho$  be the mass density of the cube. Let  $V_{\ell}^{\text{cor}}$  be the potential energy of a mass  $m$  at the corner of a cube of side  $\ell$ , and let  $V_{\ell}^{\text{cen}}$  be the potential energy of a mass  $m$  at the center of a cube of side  $\ell$ . By dimensional analysis,

$$V_{\ell}^{\text{cor}} \propto \frac{G(\rho\ell^3)m}{\ell} \propto \ell^2. \quad (5.115)$$

Therefore,<sup>32</sup>

$$V_{\ell}^{\text{cor}} = 4V_{\ell/2}^{\text{cor}}. \quad (5.116)$$

But a cube of side  $\ell$  can be built from eight cubes of side  $\ell/2$ . So by superposition, we have

$$V_{\ell}^{\text{cen}} = 8V_{\ell/2}^{\text{cor}}, \quad (5.117)$$

because the center of the larger cube lies at a corner of the eight smaller cubes (and because potentials just add). Therefore,

$$\frac{V_{\ell}^{\text{cor}}}{V_{\ell}^{\text{cen}}} = \frac{4V_{\ell/2}^{\text{cor}}}{8V_{\ell/2}^{\text{cor}}} = \frac{1}{2}. \quad (5.118)$$

<sup>32</sup> In other words, imagine expanding a cube of side  $\ell/2$  to one of side  $\ell$ . If we consider corresponding pieces of the two cubes, then the larger piece has  $2^3 = 8$  times the mass of the smaller. But corresponding distances are twice as big in the large cube as in the small cube. Therefore, the larger piece contributes  $8/2 = 4$  times as much to  $V_{\ell}^{\text{cor}}$  as the smaller piece contributes to  $V_{\ell/2}^{\text{cor}}$ .

#### 5.13. Through the hole

- (a) By symmetry, only the component of the gravitational force perpendicular to the plane survives. A piece of mass  $dm$  at radius  $r$  on the plane provides a force equal to  $Gm(dm)/(r^2+x^2)$ . To obtain the component perpendicular to the plane, we must multiply this by  $x/\sqrt{r^2+x^2}$ . Slicing the plane up into rings with mass  $dm = (2\pi r dr)\sigma$ , we find that the total force is

$$\begin{aligned} F(x) &= -\int_R^\infty \frac{Gm(2\pi r \sigma dr)x}{(r^2+x^2)^{3/2}} = 2\pi\sigma Gmx(r^2+x^2)^{-1/2} \Big|_{r=R}^{r=\infty} \\ &= -\frac{2\pi\sigma Gmx}{\sqrt{R^2+x^2}}. \end{aligned} \quad (5.119)$$

Note that if  $R = 0$  (so that we have a uniform plane without a hole), then  $F = -2\pi\sigma Gm$ , which is independent of the distance from the plane.

- (b) If  $x \ll R$ , then Eq. (5.119) gives  $F(x) \approx -2\pi\sigma Gmx/R$ , so  $F = ma$  yields

$$\ddot{x} + \left(\frac{2\pi\sigma G}{R}\right)x = 0. \quad (5.120)$$

The frequency of small oscillations is therefore

$$\omega = \sqrt{\frac{2\pi\sigma G}{R}}, \quad (5.121)$$

which is independent of  $m$ .

REMARK: For everyday values of  $R$ , this is a very small number because  $G$  is so small. Let's determine the rough size. If the sheet has thickness  $d$ , and if it is made of a material with density  $\rho$  (per unit volume), then  $\sigma = \rho d$ . So  $\omega = \sqrt{2\pi\rho dG/R}$ . In the above analysis, we assumed that the sheet was infinitely thin. In practice, we need  $d$  to be much smaller than the amplitude of the motion. But this amplitude must be much smaller than  $R$  in order for our approximation to hold. So we conclude that  $d \ll R$ . To get a rough upper bound on  $\omega$ , let's pick  $d/R = 1/10$ . And let's make our sheet out of gold (with  $\rho \approx 2 \cdot 10^4 \text{ kg/m}^3$ ). We then find  $\omega \approx 1 \cdot 10^{-3} \text{ s}^{-1}$ , which corresponds to an oscillation about every 100 minutes. For the analogous system consisting of electrical charges, the frequency is much larger, because the electrical force is so much stronger than the gravitational force. ♣

- (c) Integrating the force in Eq. (5.119) to obtain the potential energy (relative to the center of the hole) gives

$$\begin{aligned} V(x) &= -\int_0^x F(x) dx = \int_0^x \frac{2\pi\sigma Gmx dx}{\sqrt{R^2+x^2}} \\ &= 2\pi\sigma Gm\sqrt{R^2+x^2} \Big|_0^x = 2\pi\sigma Gm(\sqrt{R^2+x^2} - R). \end{aligned} \quad (5.122)$$

By conservation of energy, the speed at the center of the hole is given by  $mv^2/2 = V(x)$ . Therefore,

$$v = 2\sqrt{\pi\sigma G(\sqrt{R^2+x^2} - R)}. \quad (5.123)$$

For  $x \gg R$  this reduces to  $v \approx 2\sqrt{\pi\sigma Gx}$ .

REMARK: You can also obtain this last result by noting that for large  $x$ , the force in Eq. (5.119) reduces to  $F = -2\pi\sigma Gm$ . This is constant, so it's basically just like a gravitational force  $F = mg'$ , where  $g' \equiv 2\pi\sigma G$ . But we know that in this familiar case,  $v = \sqrt{2g'h} \rightarrow \sqrt{2(2\pi\sigma G)x}$ , as above. ♣

#### **5.14. Snowball**

All of the snowball's momentum goes into the earth, which then translates (and rotates) a tiny bit faster (or slower, depending on which way the snowball was thrown).

What about the energy? Let  $m$  and  $v$  be the mass and initial speed of the snowball. Let  $M$  and  $V$  be the mass and final speed of the earth (with respect to the original rest frame of the earth). Since  $m \ll M$ , conservation of momentum gives  $V \approx mv/M$ . The kinetic energy of the earth is therefore

$$\frac{1}{2}M\left(\frac{mv}{M}\right)^2 = \frac{1}{2}mv^2\left(\frac{m}{M}\right) \ll \frac{1}{2}mv^2. \quad (5.124)$$

There is also a rotational kinetic-energy term of the same order of magnitude, but that doesn't matter. We see that essentially none of the snowball's energy goes into the earth. It therefore must all go into the form of heat, which melts some of the snow (and/or heats up the wall). This is a general result for a small object hitting a large object: The large object picks up essentially all of the momentum but essentially none of the energy (except possibly in the form of heat).

#### **5.15. Propelling a car**

Let the speed of the car be  $v(t)$ . Consider the collision of a ball of mass  $dm$  with the car. In the instantaneous rest frame of the car, the speed of the ball is  $u - v$ . In this frame, the ball reverses velocity when it bounces (because the car is so much more massive), so its change in momentum is  $-2(u - v) dm$ . This is also the change in momentum in the lab frame, because the two frames are related by a given speed at any instant. Therefore, in the lab frame the car gains a momentum of  $2(u - v) dm$  from each ball that hits it. The rate of change in momentum of the car (that is, the force) is thus

$$\frac{dp}{dt} = 2\sigma'(u - v), \quad (5.125)$$

where  $\sigma' \equiv dm/dt$  is the rate at which mass hits the car.  $\sigma'$  is related to the given  $\sigma$  by  $\sigma' = \sigma(u - v)/u$ , because although you throw the balls at speed  $u$ , the relative speed of the balls and the car is only  $(u - v)$ . We therefore have

$$\begin{aligned} M\frac{dv}{dt} &= \frac{2(u - v)^2\sigma}{u} \Rightarrow \int_0^v \frac{dv}{(u - v)^2} = \frac{2\sigma}{Mu} \int_0^t dt \\ &\Rightarrow \frac{1}{u - v} - \frac{1}{u} = \frac{2\sigma t}{Mu} \\ &\Rightarrow v(t) = \frac{\left(\frac{2\sigma t}{M}\right)u}{1 + \frac{2\sigma t}{M}}. \end{aligned} \quad (5.126)$$

Note that  $v \rightarrow u$  as  $t \rightarrow \infty$ , as it should. Writing this speed as  $u(1 - 1/(1 + 2\sigma t/M))$ , we can integrate it to obtain the position,

$$x(t) = ut - \frac{Mu}{2\sigma} \ln\left(1 + \frac{2\sigma t}{M}\right), \quad (5.127)$$

where the constant of integration is zero because  $x = 0$  at  $t = 0$ . We see that even though the speed approaches  $u$ , the car will eventually be an arbitrarily large distance behind an object that moves with constant speed  $u$  (for example, pretend that your first ball misses the car and continues forward at speed  $u$ ).

#### **5.16. Propelling a car again**

We can carry over some of the results from the previous problem. The only change in the calculation of the force on the car is that since the balls don't bounce backward, we don't pick up the factor of 2 in Eq. (5.125). The force on the car is therefore

$$m\frac{dv}{dt} = \frac{(u - v)^2\sigma}{u}, \quad (5.128)$$

where  $m(t)$  is the mass of the car-plus-contents, as a function of time. The main difference between this problem and the previous one is that this mass  $m$  changes because the balls are collecting inside the car. From the previous problem, the rate at which mass enters the car is  $\sigma' = \sigma(u - v)/u$ . Therefore,

$$\frac{dm}{dt} = \frac{(u - v)\sigma}{u}. \quad (5.129)$$

We must now solve the two preceding differential equations. Dividing Eq. (5.128) by Eq. (5.129), and separating variables, gives<sup>33</sup>

$$\int_0^v \frac{dv}{u - v} = \int_M^m \frac{dm}{m} \implies -\ln\left(\frac{u - v}{u}\right) = \ln\left(\frac{m}{M}\right) \implies m = \frac{Mu}{u - v}. \quad (5.130)$$

Note that  $m \rightarrow \infty$  as  $v \rightarrow u$ , as it should. Substituting this value of  $m$  into either Eq. (5.128) or Eq. (5.129) gives

$$\begin{aligned} \int_0^v \frac{dv}{(u - v)^3} &= \int_0^t \frac{\sigma dt}{Mu^2} \implies \frac{1}{2(u - v)^2} - \frac{1}{2u^2} = \frac{\sigma t}{Mu^2} \\ \implies v(t) &= u - \frac{u}{\sqrt{1 + \frac{2\sigma t}{M}}}. \end{aligned} \quad (5.131)$$

Note that  $v \rightarrow u$  as  $t \rightarrow \infty$ , as it should. Integrating this speed to obtain the position gives

$$x(t) = ut - \frac{Mu}{\sigma} \sqrt{1 + \frac{2\sigma t}{M}} + \frac{Mu}{\sigma}, \quad (5.132)$$

where the constant of integration has been chosen so that  $x = 0$  at  $t = 0$ . For a given  $t$ , the  $v(t)$  in Eq. (5.131) is smaller than the  $v(t)$  for the previous problem in Eq. (5.126), which is easy to see if the latter is written as  $u(1 - 1/(1 + 2\sigma t/M))$ . This makes sense, because in the present problem the balls have less of an effect on  $v(t)$ , because (1) they don't bounce back, and (2) the mass of the car-plus-contents is larger.

#### 5.17. Leaky bucket

- (a) FIRST SOLUTION: The initial position is  $x = L$ . The given rate of leaking implies that the mass of the bucket at position  $x$  is  $m = M(x/L)$ . Therefore,  $F = ma$  gives  $-T = (Mx/L)\ddot{x}$ . Writing the acceleration as  $v dv/dx$ , and separating variables and integrating, gives

$$-\frac{TL}{M} \int_L^x \frac{dx}{x} = \int_0^v v dv \implies -\frac{TL}{M} \ln\left(\frac{x}{L}\right) = \frac{v^2}{2}. \quad (5.133)$$

The kinetic energy at position  $x$  is therefore

$$E = \frac{mv^2}{2} = \left(\frac{Mx}{L}\right) \frac{v^2}{2} = -Tx \ln\left(\frac{x}{L}\right). \quad (5.134)$$

In terms of the fraction  $z \equiv x/L$ , we have  $E = -TLz \ln z$ . Setting  $dE/dz = 0$  to find the maximum gives

$$z = \frac{1}{e} \implies E_{\max} = \frac{TL}{e}. \quad (5.135)$$

<sup>33</sup> We can also quickly derive this equation by writing down conservation of momentum for the time interval when a mass  $dm$  enters the car:  $dm u + mv = (m + dm)(v + dv)$ . This yields the first equality in Eq. (5.130). But we will still need to use one of Eqs. (5.128) and (5.129) in what follows.

Note that the (fractional) location of  $E_{\max}$  is independent of  $M$ ,  $T$ , and  $L$ , but its value depends on  $T$  and  $L$ . These facts follow from dimensional analysis.

REMARK: We began this solution by writing down  $F = ma$ , where  $m$  is the mass of the bucket. You may be wondering why we didn't use  $F = dp/dt$ , where  $p$  is the momentum of the bucket. This would certainly give a different result, because  $dp/dt = d(mv)/dt = ma + (dm/dt)v$ . We used  $F = ma$  because at any instant the mass  $m$  is what is being accelerated by the force  $F$ .

If you want, you can imagine the process occurring in discrete steps: The force pulls on the mass for a short period of time, then a little piece falls off. Then the force pulls again on the new mass, then another little piece falls off. And so on. In this scenario, it is clear that  $F = ma$  is the appropriate formula, because it holds for each step in the process.

It is indeed true that  $F = dp/dt$ , if you let  $F$  be *total* force in the problem, and let  $p$  be the *total* momentum. The tension  $T$  is the only horizontal force in the problem, because we've assumed the ground to be frictionless. However, the total momentum consists of both the sand in the bucket *and* the sand that has leaked out and is sliding along on the ground. If we use  $F = dp/dt$ , where  $p$  is the total momentum, we obtain (remember that  $dm/dt$  is a negative quantity)

$$-T = \frac{dp_{\text{bucket}}}{dt} + \frac{dp_{\text{leaked}}}{dt} = \left(ma + \frac{dm}{dt}v\right) + \left(-\frac{dm}{dt}\right)v = ma, \quad (5.136)$$

as expected. See Appendix C for further discussion of the uses of  $F = ma$  and  $F = dp/dt$ . ♣

SECOND SOLUTION: Consider a small time interval during which the bucket moves from  $x$  to  $x + dx$  (where  $dx$  is negative). The bucket's kinetic energy changes by  $(-T) dx$  (this is positive) due to the work done by the spring, and also changes by a fraction  $dx/x$  (this is negative) due to the leaking. Therefore,  $dE = -T dx + E dx/x$ , or

$$\frac{dE}{dx} = -T + \frac{E}{x}. \quad (5.137)$$

In solving this differential equation, it is convenient to introduce the variable  $y \equiv E/x$ . Then  $E' = xy' + y$ , where a prime denotes differentiation with respect to  $x$ . Equation (5.137) then becomes  $xy' = -T$ , which gives

$$\int_0^{E/x} dy = -T \int_L^x \frac{dx}{x} \implies E = -Tx \ln\left(\frac{x}{L}\right), \quad (5.138)$$

as in the first solution.

- (b) From Eq. (5.133), the speed is  $v = \sqrt{2TL/M} \sqrt{-\ln z}$ , where  $z \equiv x/L$ . Therefore, the magnitude of the momentum is

$$p = mv = (Mz)v = \sqrt{2TLM} \sqrt{-z^2 \ln z}. \quad (5.139)$$

Setting  $dp/dz = 0$  to find the maximum gives

$$z = \frac{1}{\sqrt{e}} \implies p_{\max} = \sqrt{\frac{TLM}{e}}. \quad (5.140)$$

Note that the (fractional) location of  $p_{\max}$  is independent of  $M$ ,  $T$ , and  $L$ , but its value depends on all three. These facts follow from dimensional analysis.

REMARK:  $E_{\max}$  occurs closer to the wall (that is, at a later time) than  $p_{\max}$ . The reason for this is that  $v$  matters more in  $E = mv^2/2$  than it does in  $p = mv$ . As far as  $E$  is concerned, it is beneficial for the bucket to lose a little more mass if it means being able to pick up a little more speed (up to a certain point). ♣

#### 5.18. Another leaky bucket

- (a)  $F = ma$  gives  $-T = m\ddot{x}$ . Combining this with the given  $dm/dt = b\ddot{x}$  equation yields  $m dm = -bT dt$ . Integration then gives  $m^2/2 = C - bTt$ . But  $m = M$  when  $t = 0$ , so we have  $C = M^2/2$ . Therefore,

$$m(t) = \sqrt{M^2 - 2bTt}. \quad (5.141)$$

This holds for  $t < M^2/2bT$ , provided that the bucket hasn't hit the wall yet.

- (b) The given equation  $dm/dt = b\ddot{x} = b dv/dt$  integrates to  $v = m/b + D$ . But  $v = 0$  when  $m = M$ , so we have  $D = -M/b$ . Therefore,

$$v(m) = \frac{m - M}{b} \implies v(t) = \frac{\sqrt{M^2 - 2bTt}}{b} - \frac{M}{b}. \quad (5.142)$$

At the instant right before all the sand leaves the bucket, we have  $m = 0$ . Therefore,  $v = -M/b$  at this point. Integrating  $v(t)$  to obtain  $x(t)$ , we find

$$x(t) = \frac{-(M^2 - 2bTt)^{3/2}}{3b^2T} - \frac{M}{b}t + L + \frac{M^3}{3b^2T}, \quad (5.143)$$

where the constant of integration has been chosen so that  $x = L$  when  $t = 0$ . Solving for  $t$  in terms of  $m$  from Eq. (5.141), substituting the result into Eq. (5.143), and simplifying, gives

$$x(m) = L - \frac{(M - m)^2(M + 2m)}{6b^2T}. \quad (5.144)$$

- (c) Using Eq. (5.142), the kinetic energy is (it's easier to work in terms of  $m$  here)

$$E = \frac{1}{2}mv^2 = \frac{1}{2b^2}m(m - M)^2. \quad (5.145)$$

Taking the derivative  $dE/dm$  to find the maximum, we obtain

$$m = \frac{M}{3} \implies E_{\max} = \frac{2M^3}{27b^2}. \quad (5.146)$$

- (d) Using Eq. (5.142), the momentum is

$$p = mv = \frac{1}{b}m(m - M). \quad (5.147)$$

Taking the derivative to find the maximum magnitude, we obtain

$$m = \frac{M}{2} \implies |p|_{\max} = \frac{M^2}{4b}. \quad (5.148)$$

- (d) We want  $x = 0$  when  $m = 0$ , so Eq. (5.144) gives

$$0 = L - \frac{M^3}{6b^2T} \implies b = \sqrt{\frac{M^3}{6TL}}. \quad (5.149)$$

This is the only combination of  $M$ ,  $T$ , and  $L$  that has the units of  $b$ , namely kg s/m. But we needed to do the calculation to find the numerical factor of  $1/\sqrt{6}$ .

#### 5.19. Right angle in billiards

Let  $\mathbf{v}$  be the initial velocity, and let  $\mathbf{v}_1$  and  $\mathbf{v}_2$  be the final velocities. Since the masses are equal, conservation of momentum gives  $\mathbf{v} = \mathbf{v}_1 + \mathbf{v}_2$ . Taking the dot product of this equation with itself gives

$$\mathbf{v} \cdot \mathbf{v} = \mathbf{v}_1 \cdot \mathbf{v}_1 + 2\mathbf{v}_1 \cdot \mathbf{v}_2 + \mathbf{v}_2 \cdot \mathbf{v}_2. \quad (5.150)$$

And conservation of energy gives (dropping the factors of  $m/2$ )

$$\mathbf{v} \cdot \mathbf{v} = \mathbf{v}_1 \cdot \mathbf{v}_1 + \mathbf{v}_2 \cdot \mathbf{v}_2. \quad (5.151)$$

Taking the difference of these two equations yields

$$\mathbf{v}_1 \cdot \mathbf{v}_2 = 0. \quad (5.152)$$

So  $v_1 v_2 \cos \theta = 0$ , which means that  $\theta = 90^\circ$ . (Or  $v_1 = 0$ , which means the incoming mass stops because the collision is head-on. Or  $v_2 = 0$ , which means the masses miss each other.)

#### 5.20. Bouncing and recoiling

Let  $v_i$  be the speed of the ball after the  $i$ th bounce, and let  $V_i$  be the speed of the block right after the  $i$ th bounce. Then conservation of momentum gives

$$mv_i = MV_{i+1} - mv_{i+1}. \quad (5.153)$$

But Theorem 5.3 says that  $v_i = V_{i+1} + v_{i+1}$ . Solving this system of two linear equations gives

$$v_{i+1} = \frac{(M - m)v_i}{M + m} \equiv \frac{(1 - \epsilon)v_i}{1 + \epsilon} \approx (1 - 2\epsilon)v_i, \quad \text{and} \quad V_{i+1} \approx 2\epsilon v_i, \quad (5.154)$$

where  $\epsilon \equiv m/M \ll 1$ . This expression for  $v_{i+1}$  implies that the speed of the ball after the  $n$ th bounce is

$$v_n = (1 - 2\epsilon)^n v_0, \quad \text{where} \quad \epsilon \equiv m/M. \quad (5.155)$$

The total distance traveled by the block can be obtained by looking at the work done by friction. Eventually, the ball has negligible energy, so all of its initial kinetic energy goes into heat from friction. Therefore,  $mv_0^2/2 = F_f d = (\mu Mg)d$ , which gives

$$d = \frac{mv_0^2}{2\mu Mg}. \quad (5.156)$$

To find the total time, we can add up the times,  $t_n$ , the block moves after each bounce. Since the product of force and time equals the change in momentum, we have  $F_f t_n = MV_n$ , and so  $(\mu Mg)t_n = M(2\epsilon v_{n-1}) = 2M\epsilon(1 - 2\epsilon)^{n-1}v_0$ . Therefore,

$$t = \sum_{n=1}^{\infty} t_n = \frac{2\epsilon v_0}{\mu g} \sum_{n=0}^{\infty} (1 - 2\epsilon)^n = \frac{2\epsilon v_0}{\mu g} \cdot \frac{1}{1 - (1 - 2\epsilon)} = \frac{v_0}{\mu g}. \quad (5.157)$$

We've let the sum go to  $n = \infty$  even though our  $v_n = (1 - 2\epsilon)^n v_0$  approximation eventually breaks down for very large  $n$  (because we dropped terms of order  $\epsilon^2$  in deriving it). But by the time it breaks down, the terms are negligibly small anyway. The calculation of  $d$  above can also be done by adding up the geometric series of the distances moved after each bounce.

**REMARKS:** This  $t = v_0/\mu g$  result is much larger than the result obtained in the case where the ball sticks to the block on the first hit, in which case the answer is  $t = mv_0/(\mu Mg)$ . The total time is proportional to the total momentum that the block picks up, and the  $t = v_0/\mu g$  answer is larger because the wall keeps transferring positive momentum to the ball, which then gets transferred to the block.

In contrast,  $d$  is the same as it would be in the case where the ball sticks to the block on the first hit. The total distance is proportional to the total energy that the block picks up, and in both cases the total energy given to the block is  $mv_0^2/2$ . The wall (which is attached to the very massive earth) transfers essentially no energy to the ball.

The  $t = v_0/\mu g$  result is independent of the masses (as long as  $M \gg m$ ), although it's not at all intuitively obvious that if we keep the same  $v_0$ , but decrease  $m$  by a factor

of 100, that we'll end up with the same  $t$ . The distance  $d$ , on the other hand, would decrease by 100. ♣

#### 5.21. Drag force on a sheet

- (a) We will set  $v = 0$  here. When the sheet hits a particle, the particle acquires a speed of essentially  $2V$ . This follows from Theorem 5.3, or by working in the frame of the heavy sheet. The momentum of the particle is then  $2mV$ . In time  $t$ , the sheet sweeps through a volume  $AVt$ , where  $A$  is the area of the sheet. Therefore, in time  $t$ , the sheet hits  $AVn$  particles. The sheet therefore loses momentum at a rate of  $dP/dt = -(AVn)(2mV)$ . But  $F = dP/dt$ , so the magnitude of the drag force per unit area is

$$\frac{F}{A} = 2nmV^2 \equiv 2\rho V^2, \quad (5.158)$$

where  $\rho$  is the mass density of the particles. We see that the force depends quadratically on  $V$ .

- (b) If  $v \gg V$ , the particles now hit the sheet from various directions on both sides, but we need only consider the particles' motions along the line of the sheet's motion. As stated in the problem, we will assume that all velocities in this direction are equal to  $\pm v/2$ . Note that we won't be able to set  $V$  exactly equal to zero here, because we would obtain a force of zero and miss the lowest-order effect.

Consider a particle in front of the sheet, moving backward toward the sheet. The relative speed between the particle and the sheet is  $v/2 + V$ . This relative speed reverses direction during the collision, so the change in momentum of the particle is  $2m(v/2 + V)$ . We have used the fact that the speed of the heavy sheet is essentially unaffected by the collision. The rate at which particles collide with the sheet is  $A(v/2 + V)(n/2)$ , from the reasoning in part (a). The  $n/2$  factor comes from the fact that half of the particles move toward the sheet, and half move away from it.

Now consider a particle behind the sheet, moving forward toward the sheet. The relative speed between the particle and the sheet is  $v/2 - V$ . This relative speed reverses direction during the collision, so the change in momentum of this particle is  $-2m(v/2 - V)$ . And the rate at which particles collide with the sheet is  $A(v/2 - V)(n/2)$ . Therefore, the magnitude of the drag force per unit area is

$$\begin{aligned} \frac{F}{A} &= \frac{1}{A} \cdot \left| \frac{dP}{dt} \right| \\ &= \left( \frac{n}{2}(v/2 + V) \right) (2m(v/2 + V)) + \left( \frac{n}{2}(v/2 - V) \right) (-2m(v/2 - V)) \\ &= 2nmvV \equiv 2\rho vV, \end{aligned} \quad (5.159)$$

where  $\rho$  is the mass density of the particles. We see that the force depends linearly on  $V$ . The fact that it agrees with the result in part (a) in the case of  $v = V$  is coincidence. Neither result is valid when  $v = V$ .

#### 5.22. Drag force on a cylinder

Consider a particle that makes contact with the cylinder at an angle  $\theta$  with respect to the line of motion. In the frame of the heavy cylinder (see Fig. 5.63), the particle comes in with velocity  $-V$  and then bounces off with a horizontal velocity component of  $V \cos 2\theta$ . So in this frame (and hence also in the lab frame), the particle increases its horizontal momentum by  $mV(1 + \cos 2\theta)$ . The cylinder must therefore lose this momentum.

The area on the cylinder that lies between  $\theta$  and  $\theta + d\theta$  sweeps out volume at a rate  $(R d\theta \cos \theta)V \ell$ , where  $\ell$  is the length of the cylinder. The  $\cos \theta$  factor here gives

![Diagram of a cylinder in the cylinder frame. A circle represents the cylinder. A horizontal dashed line passes through the center. A solid line from the center to the top-right edge makes an angle theta with the horizontal dashed line. A horizontal arrow labeled V points to the right, representing the cylinder's velocity. A dashed arrow labeled V points to the left, representing the incoming particle's velocity. A solid arrow labeled V points away from the cylinder at an angle 2*theta above the horizontal, representing the outgoing particle's velocity. The angle between the incoming and outgoing velocity vectors is 2*theta.](1784053a3c11681377be382085c4557f_img.jpg)

Diagram of a cylinder in the cylinder frame. A circle represents the cylinder. A horizontal dashed line passes through the center. A solid line from the center to the top-right edge makes an angle theta with the horizontal dashed line. A horizontal arrow labeled V points to the right, representing the cylinder's velocity. A dashed arrow labeled V points to the left, representing the incoming particle's velocity. A solid arrow labeled V points away from the cylinder at an angle 2\*theta above the horizontal, representing the outgoing particle's velocity. The angle between the incoming and outgoing velocity vectors is 2\*theta.

Fig. 5.63

the projection orthogonal to the direction of motion. The force per unit length on the cylinder (that is, the rate of change in momentum per unit length) is therefore

$$\begin{aligned}
 \frac{F}{\ell} &= \int_{-\pi/2}^{\pi/2} (n(R d\theta \cos \theta) V) (mV(1 + \cos 2\theta)) \\
 &= 2nmRV^2 \int_{-\pi/2}^{\pi/2} \cos \theta (1 - \sin^2 \theta) d\theta \\
 &= 2nmRV^2 \left( \sin \theta - \frac{1}{3} \sin^3 \theta \right) \Big|_{-\pi/2}^{\pi/2} \\
 &= \frac{8}{3} nmRV^2 \equiv \frac{8}{3} \rho RV^2,
 \end{aligned} \tag{5.160}$$

where  $\rho$  is the mass density of the particles. Note that the average force per cross-sectional area,  $F/(2R\ell)$ , equals  $(4/3)\rho V^2$ . This is smaller than the result for the sheet in the previous problem, as it should be, because the particles bounce off somewhat sideways in the cylinder case.

#### 5.23. Basketball and tennis ball

- (a) Right before the basketball hits the ground, both balls move downward with speed (using  $mv^2/2 = mgh$ )

$$v = \sqrt{2gh}. \tag{5.161}$$

Right after the basketball bounces off the ground, it moves upward with speed  $v$ , while the tennis ball still moves downward with speed  $v$ . The relative speed is therefore  $2v$ . After the balls bounce off each other, the relative speed is still  $2v$  (this follows from Theorem 5.3, or by working in the frame of the heavy basketball). Since the upward speed of the basketball essentially stays equal to  $v$ , the upward speed of the tennis ball is  $2v + v = 3v$ . By conservation of energy, it therefore rises to a height of  $H = d + (3v)^2/(2g)$ . But  $v^2 = 2gh$ , so we have

$$H = d + 9h. \tag{5.162}$$

- (b) Right before  $B_1$  hits the ground, all of the balls move downward with speed  $v = \sqrt{2gh}$ . We will inductively determine the speed of each ball after it bounces off the one below it. If  $B_i$  achieves a speed of  $v_i$  after bouncing off  $B_{i-1}$ , then what is the speed of  $B_{i+1}$  after it bounces off  $B_i$ ? The relative speed of  $B_{i+1}$  and  $B_i$  (right before they bounce) is  $v + v_i$ . This is also the relative speed after they bounce. Therefore, since  $B_i$  is still moving upward at essentially speed  $v_i$ , we see that the final upward speed of  $B_{i+1}$  equals  $(v + v_i) + v_i$ . Thus,

$$v_{i+1} = 2v_i + v. \tag{5.163}$$

Since  $v_1 = v$ , we obtain  $v_2 = 3v$  (in agreement with part (a)), and then  $v_3 = 7v$ , and then  $v_4 = 15v$ , etc. In general,

$$v_n = (2^n - 1)v, \tag{5.164}$$

which is easily seen to satisfy Eq. (5.163), with the initial value  $v_1 = v$ . From conservation of energy,  $B_n$  therefore rises to a height of

$$H = \ell + \frac{((2^n - 1)v)^2}{2g} = \ell + (2^n - 1)^2 h. \tag{5.165}$$

If  $h$  is 1 meter, and if we want this height to be 1000 meters, then (assuming  $\ell$  is not very large) we need  $2^n - 1 > \sqrt{1000}$ . Five balls won't quite do the trick,

but six will, in which case the height is almost 4 kilometers. Escape velocity from the earth (which is  $v_{\text{esc}} = \sqrt{2gR} \approx 11\,200\text{ m/s}$ ) is reached when

$$v_n \geq v_{\text{esc}} \implies (2^n - 1)\sqrt{2gh} \geq \sqrt{2gR} \implies n \geq \ln_2 \left( \sqrt{\frac{R}{h}} + 1 \right). \quad (5.166)$$

With  $R = 6.4 \cdot 10^6\text{ m}$  and  $h = 1\text{ m}$ , we find  $n \geq 12$ . Of course, the elasticity assumption is absurd in this case, as is the notion that you can find 12 balls with the property that  $m_1 \gg m_2 \gg \dots \gg m_{12}$ .

#### 5.24. Maximal deflection

FIRST SOLUTION: Let's figure out what the collision looks like in the CM frame. If  $M$  has initial speed  $V$  in the lab frame, then the CM moves with speed  $V_{\text{CM}} = MV/(M+m)$ . The speeds of  $M$  and  $m$  in the CM frame therefore equal, respectively,

$$U = V - V_{\text{CM}} = \frac{mV}{M+m}, \quad \text{and} \quad u = |-V_{\text{CM}}| = \frac{MV}{M+m}. \quad (5.167)$$

In the CM frame, the collision is simple. The particles keep the same speeds, but simply change their directions (while still moving in opposite directions), as shown in Fig. 5.64. The angle  $\theta$  is free to have any value. This scenario clearly satisfies conservation of energy and momentum, so it must be what happens.

The important point to note is that since  $\theta$  can have any value, the tip of the  $\mathbf{U}$  velocity vector can be located anywhere on a circle of radius  $U$ . If we then shift back to the lab frame, we see that the final velocity of  $M$  with respect to the lab frame,  $\mathbf{V}_{\text{lab}}$ , is obtained by adding  $\mathbf{V}_{\text{CM}}$  to the vector  $\mathbf{U}$ , which can point anywhere on the dotted circle in Fig. 5.65. A few possibilities for  $\mathbf{V}_{\text{lab}}$  are shown. The largest angle of deflection is obtained when  $\mathbf{V}_{\text{lab}}$  is tangent to the dotted circle, in which case we have the situation shown in Fig. 5.66. The maximum angle of deflection,  $\phi_{\text{max}}$ , is therefore given by

$$\sin \phi_{\text{max}} = \frac{U}{V_{\text{CM}}} = \frac{mV/(M+m)}{MV/(M+m)} = \frac{m}{M}. \quad (5.168)$$

If  $M < m$ , then the dotted circle passes to the left of the left vertex of the triangle. This means that  $\phi$  can take on any value. In particular, it is possible for  $M$  to bounce directly backward.

SECOND SOLUTION: We'll work in the lab frame in this solution. Let  $V'$  and  $v'$  be the final speeds, and let  $\phi$  and  $\gamma$  be the scattering angles of  $M$  and  $m$ , respectively, in the lab frame. Then conservation of  $p_x$ ,  $p_y$ , and  $E$  give

$$MV = MV' \cos \phi + mv' \cos \gamma, \quad (5.169)$$

$$0 = MV' \sin \phi - mv' \sin \gamma, \quad (5.170)$$

$$\frac{1}{2}MV^2 = \frac{1}{2}MV'^2 + \frac{1}{2}mv'^2. \quad (5.171)$$

Putting the  $\phi$  terms on the left-hand sides of Eqs. (5.169) and (5.170), and then squaring and adding these equations, gives

$$M^2(V^2 + V'^2 - 2VV' \cos \phi) = m^2v'^2. \quad (5.172)$$

Equating this expression for  $m^2v'^2$  with the one obtained by multiplying Eq. (5.171) through by  $m$  gives

$$\begin{aligned} M(V^2 + V'^2 - 2VV' \cos \phi) &= m(V^2 - V'^2) \\ \implies (M+m)V'^2 - (2MV \cos \phi)V' + (M-m)V^2 &= 0. \end{aligned} \quad (5.173)$$

![Figure 5.64: A vector diagram in the center-of-mass (CM) frame. A horizontal line represents the initial velocity U of mass M. After the collision, the velocity vectors are U and u, both at an angle theta from the horizontal line.](e98f2054f2fc4c0fdbfd91cd7d73800f_img.jpg)

Figure 5.64: A vector diagram in the center-of-mass (CM) frame. A horizontal line represents the initial velocity U of mass M. After the collision, the velocity vectors are U and u, both at an angle theta from the horizontal line.

Fig. 5.64

![Figure 5.65: A vector diagram in the lab frame. A horizontal vector U represents the initial velocity of mass M. A vector V_CM represents the velocity of the center of mass. A dotted circle of radius U is centered at the tip of V_CM. Several vectors V_lab are shown originating from the tail of V_CM and ending on the dotted circle, representing possible final velocities of mass M in the lab frame.](023cfbb0ffd75096cdbe0f5b6abe4d37_img.jpg)

Figure 5.65: A vector diagram in the lab frame. A horizontal vector U represents the initial velocity of mass M. A vector V\_CM represents the velocity of the center of mass. A dotted circle of radius U is centered at the tip of V\_CM. Several vectors V\_lab are shown originating from the tail of V\_CM and ending on the dotted circle, representing possible final velocities of mass M in the lab frame.

Fig. 5.65

![Figure 5.66: A vector diagram showing the maximum deflection angle phi_max. A horizontal vector MV/(M+m) is shown. A dotted circle of radius mV/(M+m) is tangent to the horizontal line at the tip of the vector. A right triangle is formed with the horizontal vector as the base, the radius of the dotted circle as the height, and the hypotenuse as the vector V_lab. The angle phi_max is indicated between the horizontal vector and V_lab.](16b48f1dea7410e57921dd82f493c313_img.jpg)

Figure 5.66: A vector diagram showing the maximum deflection angle phi\_max. A horizontal vector MV/(M+m) is shown. A dotted circle of radius mV/(M+m) is tangent to the horizontal line at the tip of the vector. A right triangle is formed with the horizontal vector as the base, the radius of the dotted circle as the height, and the hypotenuse as the vector V\_lab. The angle phi\_max is indicated between the horizontal vector and V\_lab.

Fig. 5.66

A solution to this quadratic equation in  $V'$  exists if and only if the discriminant is non-negative. Therefore, we must have

$$\begin{aligned} (2MV \cos \phi)^2 - 4(M+m)(M-m)V^2 &\geq 0 \\ \implies m^2 &\geq M^2(1 - \cos^2 \phi) \\ \implies m^2 &\geq M^2 \sin^2 \phi \\ \implies \frac{m}{M} &\geq \sin \phi. \end{aligned} \quad (5.174)$$

#### 5.25. Colliding masses

- (a) By conservation of momentum, the final speed of the combined masses is  $MV/(M+m) \approx (1 - m/M)V$ , plus higher-order corrections. The final energies are therefore

$$\begin{aligned} E_m &= \frac{1}{2}m \left(1 - \frac{m}{M}\right)^2 V^2 \approx \frac{1}{2}mV^2, \\ E_M &= \frac{1}{2}M \left(1 - \frac{m}{M}\right)^2 V^2 \approx \frac{1}{2}MV^2 - mV^2. \end{aligned} \quad (5.175)$$

These energies add up to  $MV^2/2 - mV^2/2$ , which is  $mV^2/2$  less than the initial energy of mass  $M$ , namely  $MV^2/2$ . Therefore,  $mV^2/2$  is lost to heat.

- (b) In this frame, mass  $m$  has initial speed  $V$ , so its initial energy is  $E_i = mV^2/2$ . By conservation of momentum, the final speed of the combined masses is  $mV/(M+m) \approx (m/M)V$ , plus higher-order corrections. The final energies are therefore

$$\begin{aligned} E_m &= \frac{1}{2}m \left(\frac{m}{M}\right)^2 V^2 = \left(\frac{m}{M}\right)^2 E_i \approx 0, \\ E_M &= \frac{1}{2}M \left(\frac{m}{M}\right)^2 V^2 = \left(\frac{m}{M}\right) E_i \approx 0. \end{aligned} \quad (5.176)$$

This negligible final energy of zero is  $mV^2/2$  less than  $E_i$ . Therefore,  $mV^2/2$  is lost to heat, in agreement with part (a).

#### 5.26. Pulling a chain

Let  $x$  be the distance your hand has moved. Then  $x/2$  is the length of the moving part of the chain, because the chain gets “doubled up.” The momentum of this moving part is therefore  $p = (\sigma x/2)\dot{x}$ . The force that your hand applies is found from  $F = dp/dt$ , which gives  $F = (\sigma/2)(\dot{x}^2 + x\ddot{x})$ . But since  $v$  is constant, the  $\ddot{x}$  term vanishes. The change in momentum here is due simply to additional mass acquiring speed  $v$ , and not due to any increase in speed of the part already moving. Hence,

$$F = \frac{\sigma v^2}{2}, \quad (5.177)$$

which is constant. Your hand applies this force over a total distance  $2L$ , so the total work you do is

$$F(2L) = \sigma L v^2. \quad (5.178)$$

The mass of the chain is  $\sigma L$ , so its final kinetic energy is  $(\sigma L)v^2/2$ . This is only half of the work you do. Therefore, an energy of  $\sigma L v^2/2$  is lost to heat. Each atom in the chain goes abruptly from rest to speed  $v$ , and there is no way to avoid heat loss in such a process. This is clear when viewed in the reference frame of your hand. In this frame, the chain initially moves at speed  $v$  and then eventually comes to rest, piece by piece. So all of its initial kinetic energy,  $(\sigma L)v^2/2$ , goes into heat.

#### **5.27. Pulling a chain again**

Let  $x$  be the position of the end of the chain. The momentum of the chain is then  $p = (\sigma x)\dot{x}$ .  $F = dp/dt$  gives (using the fact that  $F$  is constant)  $Ft = p$ , so we have  $Ft = (\sigma x)\dot{x}$ . Separating variables and integrating yields

$$\int_0^x \sigma x \, dx = \int_0^t Ft \, dt \implies \frac{\sigma x^2}{2} = \frac{Ft^2}{2} \implies x = t\sqrt{F/\sigma}. \quad (5.179)$$

The position therefore grows linearly with time. In other words, the speed is constant, and it equals  $\sqrt{F/\sigma}$ .

**REMARK:** Realistically, when you grab the chain, there is some small initial value of  $x$  (call it  $\epsilon$ ). The  $dx$  integral above now starts at  $\epsilon$  instead of 0, so  $x$  takes the form,  $x = \sqrt{Ft^2/\sigma + \epsilon^2}$ . If  $\epsilon$  is very small, the speed very quickly approaches  $\sqrt{F/\sigma}$ . Even if  $\epsilon$  is not small, the position becomes arbitrarily close to  $t\sqrt{F/\sigma}$  as  $t$  becomes large. The “head start” of  $\epsilon$  therefore doesn’t help you in the long run. ♣

#### **5.28. Falling chain**

**FIRST SOLUTION:** The left part of the chain is in freefall (because we’re dealing with a chain described by our first scenario), so at time  $t$  it is moving at speed  $gt$  and has fallen a distance  $gt^2/2$ . The chain gets doubled up below the support, so a length of only  $gt^2/4$  hangs at rest. Hence, a length of  $L - gt^2/4$  is falling at speed  $gt$ . With upward taken to be positive, the momentum of the entire chain (which just comes from the moving part, of course) is therefore

$$p = \sigma(L - gt^2/4)(-gt) = -\sigma Lgt + \sigma g^2 t^3/4. \quad (5.180)$$

If  $F_s$  is the force from the support, then the net force on the entire chain is  $F_s - \sigma Lg$ . So  $F = dp/dt$  for the entire chain gives

$$F_s - \sigma Lg = \frac{d}{dt} \left( -\sigma Lgt + \frac{\sigma g^2 t^3}{4} \right) \implies F_s = \frac{3\sigma g^2 t^2}{4}. \quad (5.181)$$

This result holds until the top of the chain has fallen a distance  $2L$  (at  $T = \sqrt{4L/g}$ ). Prior to time  $T$ ,  $F_s$  equals three times the weight,  $\sigma(gt^2/4)g$ , of the part of the chain that hangs at rest. After time  $T$ ,  $F_s$  simply equals the total weight of the chain,  $\sigma Lg$ . So at time  $T$ ,  $F_s$  abruptly drops from  $3\sigma Lg$  to  $\sigma Lg$ .

**SECOND SOLUTION:**  $F_s$  is responsible for two things: (1) It holds up the part of the chain that hangs at rest below the support, and (2) it changes the momentum of the atoms in the chain that are suddenly brought to rest at the kink in the chain. In other words,  $F_s = F_{\text{weight}} + F_{dp/dt}$ . From the first solution above, we have  $F_{\text{weight}} = \sigma(gt^2/4)g$ .

Now let’s find  $F_{dp/dt}$ . At time  $t$ , the speed of the chain is  $gt$ , so in a small time interval  $dt$ , the top of the chain falls a distance  $(gt)dt$ . But due to the “doubling up” effect, only half of this length is brought to rest in the time  $dt$ . Therefore, a small piece of mass  $\sigma(1/2)(gt)dt$  that was moving at speed  $gt$  is suddenly brought to rest. The momentum was  $(\sigma/2)(gt)^2 dt$  downward, and then it becomes zero. Hence,  $dp = +(\sigma/2)g^2 t^2 dt$ , and so  $F_{dp/dt} = dp/dt = (\sigma/2)g^2 t^2$ . Therefore,

$$F_s = F_{\text{weight}} + F_{dp/dt} = \frac{\sigma g^2 t^2}{4} + \frac{\sigma g^2 t^2}{2} = \frac{3\sigma g^2 t^2}{4}. \quad (5.182)$$

#### **5.29. Falling chain (energy conserving)**

Let  $\sigma$  be the mass density of the chain, let  $L$  be its total length, and let  $x$  be the distance (defined to be positive) that the top of the chain has fallen. For a given  $x$ , a piece of chain with mass  $\sigma x$  and CM position  $L - x/2$  has effectively been replaced by a thin “U” below the support, with height  $x/2$ ; so its CM position is  $-x/4$ . The loss in potential energy is therefore  $(\sigma x)g(L - x/2) - (\sigma x)g(-x/4) = \sigma xg(L - x/4)$ . Since

we are assuming that energy is conserved in this setup, this loss in potential energy shows up as the gain in kinetic energy of the moving part of the chain. This part has length  $L - x/2$  (because  $x/2$  is the length hanging below the support), so conservation of energy gives

$$\frac{1}{2}\sigma(L - x/2)v^2 = \sigma xg(L - x/4) \implies v = \sqrt{\frac{2gx(L - x/4)}{L - x/2}}. \quad (5.183)$$

This has the expected property of going to infinity for  $x \rightarrow 2L$ . However, the finite size of the bend becomes relevant when  $x$  approaches  $2L$ , so all of the energy never ends up being concentrated in an infinitely small piece. All speeds therefore remain finite, as they must.

Writing  $v$  as  $dx/dt$  in Eq. (5.183), and separating variables and integrating, gives

$$t = \frac{1}{\sqrt{g}} \int_0^{2L} \sqrt{\frac{L - x/2}{2x(L - x/4)}} dx \implies t = \sqrt{\frac{L}{g}} \int_0^2 \sqrt{\frac{1 - z/2}{2z(1 - z/4)}} dz, \quad (5.184)$$

where we have changed variables to  $z \equiv x/L$ . Numerically integrating this gives a total time of  $t \approx (1.694)\sqrt{L/g}$ . Since the freefall time in the previous problem is given by  $gt^2/2 = 2L \implies t = 2\sqrt{L/g}$ , we see that the time in the present energy-conserving case is about 0.847 times the time in the freefall case.

To find the tension  $T$  at the left end of the bend, let's paint a little dot on the chain there. We'll find the acceleration of the falling part above the dot and then use  $F = ma$ . The acceleration of the falling part is  $a = dv/dt$ , where  $v$  is given in Eq. (5.183). Taking the derivative, you can show (don't forget the  $dx/dt$  from the chain rule) that  $a$  can be written in the form,

$$a = g \left( 1 + \frac{(x/2)(L - x/4)}{(L - x/2)^2} \right). \quad (5.185)$$

The  $F = ma$  equation for the part of the chain above the dot, with downward taken to be positive, gives  $T + mg = ma \implies T = m(a - g)$ . Therefore, with  $m = \sigma(L - x/2)$ , we have

$$T = \sigma(L - x/2)g \left( \frac{(x/2)(L - x/4)}{(L - x/2)^2} \right) = \frac{\sigma gx(L - x/4)}{2(L - x/2)} = \frac{\sigma v^2}{4}, \quad (5.186)$$

where we have used Eq. (5.183). This has the expected properties of equaling zero when  $x = 0$  and diverging when  $x \rightarrow 2L$ .

To find the tension at the right end of the bend, note that the total upward tension on the tiny bend equals the rate of change in momentum of the bend (the gravitational force is negligible). In a small time  $dt$ , a length  $v dt/2$  of chain is brought to rest (the factor of 2 comes from the doubling-up effect). This length goes from moving downward at speed  $v$  to being at rest, so the change in momentum is  $\sigma(v dt/2)v$  upward. Therefore,  $dp/dt = \sigma v^2/2$ . This must be the total upward force on the bend, and since we found above that the upward force at the left end is  $\sigma v^2/4$ , there must also be an upward force at the right end of  $\sigma v^2/4$ . The tensions at the two ends are therefore equal.

#### 5.30. Falling from a table

- (a) FIRST SOLUTION: Let  $\sigma$  be the mass density of the chain. From conservation of energy, we know that the chain's final kinetic energy, which is  $(\sigma L)v^2/2$ , equals the loss in potential energy. This loss equals  $(\sigma L)(L/2)g$ , because the center of mass falls a distance  $L/2$ . Therefore,

$$v = \sqrt{gL}. \quad (5.187)$$

This equals the speed obtained by an object that falls a distance  $L/2$ . Note that if the initial piece hanging down through the hole is arbitrarily short, then the

chain will take an arbitrarily long time to fall down. But the final speed will still be (arbitrarily close to)  $\sqrt{gL}$ .

SECOND SOLUTION: Let  $x$  be the length that hangs down through the hole. The gravitational force on this length, which is  $(\sigma x)g$ , is responsible for changing the momentum of the entire chain, which is  $(\sigma L)\dot{x}$ . Therefore,  $F = dp/dt$  gives  $(\sigma x)g = (\sigma L)\ddot{x}$ , which is simply the  $F = ma$  equation. Hence,  $\ddot{x} = (g/L)x$ , and the general solution to this equation is<sup>34</sup>

$$x(t) = Ae^{t\sqrt{g/L}} + Be^{-t\sqrt{g/L}}. \quad (5.188)$$

Let  $T$  be the time for which  $x(T) = L$ . If  $\epsilon$  is very small, then  $T$  will be very large. But for large  $t$  (more precisely, for  $t \gg \sqrt{L/g}$ ), we may neglect the negative-exponent term in Eq. (5.188). We then have

$$x \approx Ae^{t\sqrt{g/L}} \implies \dot{x} \approx \left(Ae^{t\sqrt{g/L}}\right)\sqrt{g/L} \approx x\sqrt{g/L} \quad (\text{for large } t). \quad (5.189)$$

When  $x = L$ , we obtain

$$\dot{x}(T) = L\sqrt{g/L} = \sqrt{gL}, \quad (5.190)$$

in agreement with the first solution.

- (b) Let  $\sigma$  be the mass density of the chain, and let  $x$  be the length that hangs down through the hole. The gravitational force on this length, which is  $(\sigma x)g$ , is responsible for changing the momentum of the chain. This momentum is  $(\sigma x)\dot{x}$ , because only the hanging part is moving. Therefore,  $F = dp/dt$  gives

$$xg = x\ddot{x} + \dot{x}^2. \quad (5.191)$$

Note that  $F = ma$  gives the wrong equation, because it neglects the fact that the amount of moving mass,  $\sigma x$ , is changing. It therefore misses the second term on the right-hand side of Eq. (5.191). In short, the momentum of the chain increases because it is speeding up (which gives the  $x\ddot{x}$  term) and because additional mass is continually being added to the moving part (which gives the  $\dot{x}^2$  term, as you can show).

Let's now solve Eq. (5.191) for  $x(t)$ . Since  $g$  is the only parameter in the equation, the solution for  $x(t)$  can involve only  $g$ 's and  $t$ 's.<sup>35</sup> By dimensional analysis,  $x(t)$  must then be of the form  $x(t) = bgt^2$ , where  $b$  is a numerical constant to be determined. Plugging this expression for  $x(t)$  into Eq. (5.191) and dividing by  $g^2t^2$  gives  $b = 2b^2 + 4b^2$ . Therefore,  $b = 1/6$ , and our solution may be written as

$$x(t) = \frac{1}{2} \left(\frac{g}{3}\right) t^2. \quad (5.192)$$

This is the equation for something that accelerates downward with acceleration  $g' = g/3$ . The time the chain takes to fall a distance  $L$  is then given by  $L = g't^2/2$ , which yields  $t = \sqrt{2L/g'}$ . The final speed is thus

$$v = g't = \sqrt{2Lg'} = \sqrt{\frac{2gL}{3}}. \quad (5.193)$$

<sup>34</sup> If  $\epsilon$  is the initial value of  $x$ , then  $A = B = \epsilon/2$  satisfies the initial conditions  $x(0) = \epsilon$  and  $\dot{x}(0) = 0$ , in which case we can write  $x(t) = \epsilon \cosh(t\sqrt{g/L})$ . But we won't need this information in what follows.

<sup>35</sup> The other dimensionful quantities in the problem,  $L$  and  $\sigma$ , do not appear in Eq. (5.191), so they cannot appear in the solution. Also, the initial position and speed (which in general appear in the solution for  $x(t)$ , because Eq. (5.191) is a second-order differential equation) do not appear in this case, because they are equal to zero.

This is smaller than the  $\sqrt{gL}$  result in part (a). We therefore see that although the total time for the scenario in part (a) is very large, the final speed in that case is in fact larger than that in the present scenario. You can show that the speed in part (a)'s scenario is smaller than the speed in part (b)'s scenario for  $x$  less than  $2L/3$ , but larger for  $x$  greater than  $2L/3$ .

**REMARKS:** Using Eq. (5.193), you can show that  $1/3$  of the available potential energy is lost to heat. This inevitable loss occurs during the abrupt motions that suddenly bring the atoms from zero to nonzero speed when they join the moving part of the chain. The use of conservation of energy is therefore *not* a valid way to solve part (b). If you used conservation of energy, you would (as you can verify) obtain an incorrect acceleration of  $g/2$ . In view of the above solution based on  $F = dp/dt$ , this  $g/2$  result cannot be correct, because there is simply not enough downward force in the setup to yield this acceleration. The only downward force comes from gravity, and we showed above that this leads to an acceleration of  $g/3$ .

If we want to try to get rid of the energy loss and somehow produce an acceleration of  $g/2$ , a plausible idea is to use a continuous piece of rope instead of the ideal kind of chain we've been using. As mentioned near the end of Section 5.8, a rope yields an energy-conserving system. However, from the reasoning on page 171, there is now a nonzero tension *everywhere* throughout the rope, even in the part inside the heap; this is the price we pay for having none of the points in the rope abruptly go from zero to nonzero speed. This tension then causes the rope (all of it) in the heap to move. The system is therefore completely different from the original one with our ideal chain, where it was understood that all the little strings connecting the ideal point masses in the heap are initially limp with zero tension; the tension in a given little string becomes nonzero only when it joins the moving part of the chain. The solution to this new energy-conserving setup therefore depends on exactly how the rope in the heap is initially situated; more information is therefore needed to solve the problem. But one thing is certain: this new setup is definitely not going to yield an acceleration of  $g/2$ , because the conservation-of-energy solution that leads to  $g/2$  is based on the assumption that the entire loss in potential energy goes exclusively into the gain in kinetic energy of the part of the rope that has fallen below the table. The fact that the rope inside the heap is now also moving ruins this assumption. ♣

#### 5.31. The raindrop

Let  $\rho$  be the mass density of the raindrop, and let  $\lambda$  be the average mass density in space of the water droplets. Let  $r(t)$ ,  $M(t)$ , and  $v(t)$  be the radius, mass, and velocity of the raindrop, respectively. We need three equations to solve for these three unknowns. The equations we will use are two different expressions for  $dM/dt$ , and the  $F = dp/dt$  expression for the raindrop. The first expression for  $\dot{M}$  is obtained by taking the derivative of  $M = (4/3)\pi r^3 \rho$ , which gives

$$\dot{M} = 4\pi r^2 \dot{r} \rho \quad (5.194)$$

$$= 3M \frac{\dot{r}}{r}. \quad (5.195)$$

The second expression for  $\dot{M}$  is obtained by noting that the change in  $M$  is due to the acquisition of water droplets. The raindrop sweeps out volume at a rate given by its cross-sectional area times its velocity. Therefore,

$$\dot{M} = \pi r^2 v \lambda. \quad (5.196)$$

The  $F = dp/dt$  equation is found as follows. The gravitational force is  $Mg$ , and the momentum is  $Mv$ . Therefore,  $F = dp/dt$  gives

$$Mg = \dot{M}v + M\dot{v}. \quad (5.197)$$

We now have three equations involving the three unknowns,  $r$ ,  $M$ , and  $v$ .<sup>36</sup> Our goal is to find  $\dot{v}$ . We will do this by first finding  $\ddot{r}$ . Equating the expressions for  $\dot{M}$  in Eqs. (5.194) and (5.196) gives

$$v = \frac{4\rho}{\lambda} \dot{r} \quad (5.198)$$

$$\implies \dot{v} = \frac{4\rho}{\lambda} \ddot{r}. \quad (5.199)$$

Plugging Eqs. (5.195), (5.198), and (5.199) into Eq. (5.197) gives

$$Mg = \left(3M \frac{\dot{r}}{r}\right) \left(\frac{4\rho}{\lambda} \dot{r}\right) + M \left(\frac{4\rho}{\lambda} \ddot{r}\right). \quad (5.200)$$

Therefore,

$$\tilde{g}r = 12\dot{r}^2 + 4r\ddot{r}, \quad (5.201)$$

where we have defined  $\tilde{g} \equiv g\lambda/\rho$ , for convenience. The only parameter in Eq. (5.201) is  $\tilde{g}$ . Therefore,  $r(t)$  can depend only on  $\tilde{g}$  and  $t$ .<sup>37</sup> Hence, by dimensional analysis,  $r$  must take the form

$$r(t) = A\tilde{g}t^2, \quad (5.202)$$

where  $A$  is a numerical constant, to be determined. Plugging this expression for  $r$  into Eq. (5.201) gives

$$\begin{aligned} \tilde{g}(A\tilde{g}t^2) &= 12(2A\tilde{g}t)^2 + 4(A\tilde{g}t^2)(2A\tilde{g}) \\ \implies A &= 48A^2 + 8A^2. \end{aligned} \quad (5.203)$$

Therefore,  $A = 1/56$ , and so  $\ddot{r} = 2A\tilde{g} = \tilde{g}/28 = g\lambda/28\rho$ . Eq. (5.199) then gives the acceleration of the raindrop as

$$\dot{v} = \frac{g}{7}, \quad (5.204)$$

independent of  $\rho$  and  $\lambda$ . For further discussion of the raindrop problem, see Krane (1981).

**REMARK:** A common invalid solution to this problem is the following, which (incorrectly) uses conservation of energy: The fact that  $v$  is proportional to  $\dot{r}$  (shown in Eq. (5.198)) means that the volume swept out by the raindrop is a cone. The center of mass of a cone is  $1/4$  of the way from the base to the apex (as you can show by integrating over horizontal circular slices). Therefore, if  $M$  is the mass of the raindrop after it has fallen a height  $h$ , then an (incorrect) application of conservation of energy gives

$$\frac{1}{2}Mv^2 = Mg \frac{h}{4} \implies v^2 = \frac{gh}{2}. \quad (5.205)$$

Taking the derivative of this (or just using the general result,  $v^2 = 2ah$ ) gives

$$\dot{v} = \frac{g}{4} \quad (\text{incorrect}). \quad (5.206)$$

<sup>36</sup> Note that we *cannot* write down the naive conservation-of-energy equation (which would say that the decrease in the water's potential energy equals the increase in its kinetic energy), because mechanical energy is *not* conserved. The collisions between the raindrop and the droplets are completely inelastic. The raindrop will, in fact, heat up. See the remark at the end of the solution.

<sup>37</sup> The other dimensionful quantities in the problem,  $\rho$  and  $\lambda$ , do not appear in Eq. (5.201), except through  $\tilde{g}$ , so they cannot appear in the solution. Also, the initial values of  $r$  and  $\dot{r}$  (which in general appear in the solution for  $r(t)$ , because Eq. (5.201) is a second-order differential equation) do not appear in this case, because they are equal to zero.

The reason why this solution is invalid is that the collisions between the raindrop and the droplets are completely inelastic. Heat is generated, and the overall kinetic energy of the raindrop is smaller than you would otherwise expect.

Let's calculate how much mechanical energy is lost (and therefore how much the raindrop heats up) as a function of the height fallen. The loss in mechanical energy is

$$E_{\text{lost}} = Mg \frac{h}{4} - \frac{1}{2} M v^2. \quad (5.207)$$

Using  $v^2 = 2(g/7)h$ , this becomes

$$\Delta E_{\text{int}} = E_{\text{lost}} = \frac{3}{28} Mgh, \quad (5.208)$$

where  $\Delta E_{\text{int}}$  is the gain in internal thermal energy. The energy required to heat 1 g of water by  $1^\circ\text{C}$  is 1 calorie ( $= 4.18$  joules). Therefore, the energy required to heat 1 kg of water by  $1^\circ\text{C}$  is  $\approx 4200$  J. In other words,

$$\Delta E_{\text{int}} = 4200 M \Delta T, \quad (5.209)$$

where  $M$  is measured in kilograms, and  $T$  is measured in degrees Celsius. Equations (5.208) and (5.209) give the increase in temperature as a function of  $h$ ,

$$4200 \Delta T = \frac{3}{28} gh. \quad (5.210)$$

How far must the raindrop fall before it starts to boil? If we assume that the water droplets' temperature is near freezing, then the height through which the raindrop must fall to have  $\Delta T = 100^\circ\text{C}$  is found from Eq. (5.210) to be

$$h \approx 400\,000 \text{ m} = 400 \text{ km}, \quad (5.211)$$

which is much larger than the height of the atmosphere. We have, of course, idealized the problem in a drastic manner. But needless to say, there is no need to worry about getting burned by the rain. A typical value for  $h$  is a few kilometers, which would raise the temperature by only about one degree. This effect is completely washed out by many other factors. ♣