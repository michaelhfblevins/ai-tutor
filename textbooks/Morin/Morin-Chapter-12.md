# Chapter 12 Relativity (Dynamics)

In the previous chapter, we dealt only with abstract particles flying through space and time. We didn't concern ourselves with the nature of the particles, how they got to be moving, or what would happen if various particles interacted. In this chapter we will deal with these issues. That is, we will discuss masses, forces, energy, momentum, etc. The two main results of this chapter are that the momentum and energy of a particle are given by

$$\mathbf{p} = \gamma m \mathbf{v}, \quad \text{and} \quad E = \gamma m c^2, \quad (12.1)$$

where  $\gamma \equiv 1/\sqrt{1 - v^2/c^2}$ , and  $m$  is the mass of the particle.<sup>1</sup> When  $v \ll c$ , the expression for  $\mathbf{p}$  reduces to  $\mathbf{p} = m\mathbf{v}$ , as it should for a nonrelativistic particle. When  $v = 0$ , the expression for  $E$  reduces to the well-known  $E = mc^2$ .

## 12.1 Energy and momentum

In this section, we'll give some justification for Eqs. (12.1). The reasoning here should convince you of their truth. An alternative, and perhaps more convincing, motivation comes from the 4-vector formalism in Chapter 13. In the end, however, the justification for Eqs. (12.1) is obtained through experiments. And indeed, experiments in high-energy accelerators are continually verifying the truth of these expressions. (More precisely, they are verifying that these energy and momenta are *conserved* in any type of collision.) We therefore conclude, with reasonable certainty, that Eqs. (12.1) give the correct expressions for energy and momentum. But actual experiments aside, let's consider a few thought-experiments that motivate the above expressions.

![Diagram showing two particles, A and B, moving in opposite directions in a coordinate system with x and y axes. Particle A moves from the top left towards the center, and particle B moves from the bottom right towards the center. Vertical dashed lines represent worldlines, and solid lines with arrows represent the trajectories of the particles.](e3818712aec88af26eaee21e72b1c21c_img.jpg)

Diagram showing two particles, A and B, moving in opposite directions in a coordinate system with x and y axes. Particle A moves from the top left towards the center, and particle B moves from the bottom right towards the center. Vertical dashed lines represent worldlines, and solid lines with arrows represent the trajectories of the particles.

Fig. 12.1

### 12.1.1 Momentum

Consider the following system. In the lab frame, identical particles  $A$  and  $B$  move as shown in Fig. 12.1. They move with equal and opposite small speeds in the

<sup>1</sup> There are various ways that people use the word “mass” in relativity. In particular, some people talk about “rest mass” and “relativistic mass.” But we won't use these terms. We'll use “mass” to refer only to what other people would call “rest mass.” See the discussion on page 590 for more on this.

$x$  direction, and with equal and opposite large speeds in the  $y$  direction. Their paths are arranged so that they glance off each other and reverse their motion in the  $x$  direction. Imagine a series of equally spaced vertical lines for reference. Assume that  $A$  and  $B$  have identical clocks that tick every time they cross one of these lines.

Consider now the reference frame that moves in the  $y$  direction with the same  $v_y$  as  $A$ . In this frame, the situation is shown in Fig. 12.2. The collision simply changes the sign of the  $x$  velocities of the particles. Therefore, the  $x$  momenta of the two particles must be the same. This is true because if, say,  $A$ 's  $p_x$  were larger than  $B$ 's  $p_x$ , then the total  $p_x$  would point to the right before the collision, and to the left after the collision. Since momentum is something we want to be conserved, this cannot be the case.

However, the  $x$  speeds of the two particles are *not* the same in this frame.  $A$  is essentially at rest in this frame, and  $B$  is moving with a very large speed,  $v$ . Therefore,  $B$ 's clock is running slower than  $A$ 's, by a factor essentially equal to  $1/\gamma \equiv \sqrt{1 - v^2/c^2}$ . And since  $B$ 's clock ticks once for every vertical line it crosses (this fact is independent of the frame),  $B$  must therefore be moving slower in the  $x$  direction, by a factor of  $1/\gamma$ . Therefore, the Newtonian expression,  $p_x = mv_x$ , cannot be the correct one for momentum, because  $B$ 's momentum would be smaller than  $A$ 's (by a factor of  $1/\gamma$ ), due to their different  $v_x$ 's. But the  $\gamma$  factor in

$$p_x = \gamma mv_x \equiv \frac{mv_x}{\sqrt{1 - v^2/c^2}} \quad (12.2)$$

precisely takes care of this problem, because  $\gamma \approx 1$  for  $A$ , and  $\gamma = 1/\sqrt{1 - v^2/c^2}$  for  $B$ , which cancels the effect of  $B$ 's smaller  $v_x$ .

To obtain the three-dimensional form of  $\mathbf{p}$ , we can use the fact that the vector  $\mathbf{p}$  must point in the same direction as the vector  $\mathbf{v}$ , because any other direction for  $\mathbf{p}$  would violate rotation invariance. If someone claims that  $\mathbf{p}$  points in the direction shown in Fig. 12.3, then he would be hard-pressed to explain why it doesn't instead point along the direction  $\mathbf{p}'$  shown. In short, the direction of  $\mathbf{v}$  is the only preferred direction in space. Therefore, Eq. (12.2) implies that the momentum vector must be

$$\mathbf{p} = \gamma m\mathbf{v} \equiv \frac{m\mathbf{v}}{\sqrt{1 - v^2/c^2}}, \quad (12.3)$$

in agreement with Eqs. (12.1). Note that all the components of  $\mathbf{p}$  have the same denominator, which involves the whole speed,  $v^2 = v_x^2 + v_y^2 + v_z^2$ . The denominator of, say,  $p_x$  is *not*  $\sqrt{1 - v_x^2/c^2}$ . This would yield a  $\mathbf{p}$  that doesn't point along  $\mathbf{v}$ .

The above setup is only one specific type of collision among an infinite number of possible types of collisions. What we've shown with this setup is that the only possible vector of the form  $f(v)m\mathbf{v}$  (where  $f$  is some function) that has

![Figure 12.2: A diagram showing two particles, A and B, in a reference frame moving with velocity v_y relative to the original frame. Particle A is at rest (indicated by a dot), and particle B is moving with a large speed v. Vertical dashed lines represent reference lines. Arrows indicate the paths of the particles before and after a collision, showing they reverse their x-direction motion.](d1e569b8d2bed49c0db701ce96eea791_img.jpg)

Figure 12.2: A diagram showing two particles, A and B, in a reference frame moving with velocity v\_y relative to the original frame. Particle A is at rest (indicated by a dot), and particle B is moving with a large speed v. Vertical dashed lines represent reference lines. Arrows indicate the paths of the particles before and after a collision, showing they reverse their x-direction motion.

Fig. 12.2

![Figure 12.3: A vector diagram illustrating rotation invariance. A horizontal vector v points to the right. Two other vectors, p and p', originate from the same point as v. Vector p is at an angle theta above v, and vector p' is at an angle theta below v. This shows that if p were the momentum vector, p' would be an equally valid choice, violating the uniqueness of the direction of v.](ca4a4f994fa5d7133ebe62b2c64a6edf_img.jpg)

Figure 12.3: A vector diagram illustrating rotation invariance. A horizontal vector v points to the right. Two other vectors, p and p', originate from the same point as v. Vector p is at an angle theta above v, and vector p' is at an angle theta below v. This shows that if p were the momentum vector, p' would be an equally valid choice, violating the uniqueness of the direction of v.

Fig. 12.3

any chance at being conserved in all collisions is  $\gamma m\mathbf{v}$  (or some constant multiple of this). We haven't proved that it actually *is* conserved in all collisions. This is where the gathering of data from experiments comes in. But we've shown above that it would be a waste of time to consider, for example, the vector  $\gamma^5 m\mathbf{v}$ .

### 12.1.2 Energy

Having given some justification for the momentum expression,  $\mathbf{p} = \gamma m\mathbf{v}$ , let's now try to justify the energy expression,

$$E = \gamma mc^2. \quad (12.4)$$

![Diagram Fig. 12.4: Two identical particles of mass m moving towards each other with speed u. They collide and stick together to form a single particle of mass M at rest.](e263d662265441272ff56a34f65582f8_img.jpg)

Diagram Fig. 12.4 shows two particles, each with mass  $m$ , moving towards each other with speed  $u$ . The left particle has a velocity vector  $u$  pointing right, and the right particle has a velocity vector  $u$  pointing left. A downward arrow indicates the collision, resulting in a single particle of mass  $M$  at rest.

Diagram Fig. 12.4: Two identical particles of mass m moving towards each other with speed u. They collide and stick together to form a single particle of mass M at rest.

Fig. 12.4

![Diagram Fig. 12.5: Two identical particles of mass m. The left particle moves right with speed v = 2u/(1+u^2). The right particle is at rest. They collide and stick together to form a single particle of mass M moving right with speed u.](0878681ed9aa907129d8c789ae60b277_img.jpg)

Diagram Fig. 12.5 shows two particles, each with mass  $m$ . The left particle moves to the right with speed  $v = \frac{2u}{1+u^2}$ . The right particle is at rest. A downward arrow indicates the collision, resulting in a single particle of mass  $M$  moving to the right with speed  $u$ .

Diagram Fig. 12.5: Two identical particles of mass m. The left particle moves right with speed v = 2u/(1+u^2). The right particle is at rest. They collide and stick together to form a single particle of mass M moving right with speed u.

Fig. 12.5

More precisely, we'll show that the above form of the momentum implies that  $\gamma mc^2$  is conserved in interactions (or at least in the specific interaction below). There are various ways to do this. The best way, perhaps, is to use the 4-vector formalism in Chapter 13. But we'll study one simple setup here that should do the job.

Consider the following system. Two identical particles of mass  $m$  head toward each other, both with speed  $u$ , as shown in Fig. 12.4. They stick together and form a particle of mass  $M$ .  $M$  is at rest, due to the symmetry of the situation. At the moment we can't assume anything about the size of  $M$ , but we'll find below that it does *not* equal the naive value of  $2m$ . This setup is a fairly uninteresting one (conservation of momentum gives  $0=0$ ), so let's instead consider the less trivial view of it in the frame moving to the left at speed  $u$ . This situation is shown in Fig. 12.5. The right mass is at rest, the left mass moves to the right at speed  $v = 2u/(1+u^2)$  from the velocity-addition formula,<sup>2</sup> and the final mass  $M$  moves to the right at speed  $u$ . Note that the  $\gamma$  factor associated with the speed  $v$  is

$$\gamma_v \equiv \frac{1}{\sqrt{1-v^2}} = \frac{1}{\sqrt{1-\left(\frac{2u}{1+u^2}\right)^2}} = \frac{1+u^2}{1-u^2}. \quad (12.5)$$

Conservation of momentum in this collision then gives

$$\begin{aligned} \gamma_v m v + 0 &= \gamma_u M u \quad \Rightarrow \quad m \left( \frac{1+u^2}{1-u^2} \right) \left( \frac{2u}{1+u^2} \right) = \frac{Mu}{\sqrt{1-u^2}} \\ &\Rightarrow \quad M = \frac{2m}{\sqrt{1-u^2}}. \end{aligned} \quad (12.6)$$

Conservation of momentum therefore tells us that  $M$  does *not* equal  $2m$ . But if  $u$  is very small, then  $M$  is approximately equal to  $2m$ , as we know from everyday experience.

<sup>2</sup> We're going to set  $c = 1$  for a little while here, because this calculation would get a bit messy if we kept in the  $c$ 's. We'll discuss the issue of setting  $c = 1$  in more detail at the end of this section.

Using the value of  $M$  from Eq. (12.6), let's now check that our candidate for energy,  $E = \gamma mc^2$ , is conserved in this collision. There is no freedom left in any of the parameters, so  $\gamma mc^2$  is either conserved or it isn't. In the original frame where  $M$  is at rest,  $E$  is conserved if

$$\gamma_0 Mc^2 = 2(\gamma_u mc^2) \iff \frac{2m}{\sqrt{1-u^2}} = 2\left(\frac{1}{\sqrt{1-u^2}}\right)m, \quad (12.7)$$

which is indeed true. Let's also check that  $E$  is conserved in the frame where the right mass is at rest.  $E$  is conserved if

$$\begin{aligned} \gamma_v mc^2 + \gamma_0 mc^2 &= \gamma_u Mc^2 \\ \iff \left(\frac{1+u^2}{1-u^2}\right)m + m &= \frac{M}{\sqrt{1-u^2}} \\ \iff \frac{2m}{1-u^2} &= \left(\frac{2m}{\sqrt{1-u^2}}\right) \frac{1}{\sqrt{1-u^2}}, \end{aligned} \quad (12.8)$$

which is indeed true. So  $E$  is also conserved in this frame. This example should convince you that  $\gamma mc^2$  is at least a believable expression for the energy of a particle. But just as in the case of momentum, we haven't proved that  $\gamma mc^2$  actually *is* conserved in all collisions. This is the duty of experiments. But we've shown that it would be a waste of time to consider, for example, the quantity  $\gamma^4 mc^2$ .

One thing that we certainly need to check is that if  $E$  and  $p$  are conserved in one reference frame, then they are conserved in any other. We'll demonstrate this in Section 12.2. A conservation law shouldn't depend on what frame you're in, after all.

#### REMARKS:

1. As mentioned above, we're technically not trying to justify Eqs. (12.1) here. These two equations by themselves are devoid of any meaning. All they do is define the letters  $\mathbf{p}$  and  $E$ . Our goal is to make a meaningful physical statement, not just a definition.

The meaningful physical statement that we want to make is that the quantities  $\gamma m\mathbf{v}$  and  $\gamma mc^2$  are *conserved* in an interaction among particles (and this is what we tried to justify above). This fact then makes these quantities worthy of special attention, because conserved quantities are very helpful in understanding what is happening in a given physical situation. And anything worthy of special attention certainly deserves a label, so we may then attach the names "momentum" and "energy" to  $\gamma m\mathbf{v}$  and  $\gamma mc^2$ . Any other names would work just as well, of course, but we choose these because in the limit of small speeds,  $\gamma m\mathbf{v}$  and  $\gamma mc^2$  reduce (as we will soon show) to some other nicely conserved quantities, which someone already tagged with the labels "momentum" and "energy" long ago.

2. As we've noted, the fact of the matter is that we can't *prove* that  $\gamma m\mathbf{v}$  and  $\gamma mc^2$  are conserved. In Newtonian physics, conservation of  $\mathbf{p} \equiv m\mathbf{v}$  is basically postulated by Newton's third law, and we're not going to be able to do any better than that here. All we can hope to do as physicists is provide some motivation for considering  $\gamma m\mathbf{v}$  and  $\gamma mc^2$ , then show that it is consistent for  $\gamma m\mathbf{v}$  and  $\gamma mc^2$  to be conserved during an interaction, and then gather a large amount of experimental evidence, all of which is consistent with

$\gamma m \mathbf{v}$  and  $\gamma m c^2$  being conserved. As far as the experimental evidence goes, suffice it to say that high-energy accelerators, cosmological observations, and many other forums are continually verifying everything that we think is true about relativistic dynamics. If the theory isn't correct, then we know that it must be the limiting case of a more correct theory.<sup>3</sup> But all this experimental induction has to count for something ...

“To three, five, and seven, assign  
A name,” the prof said, “We’ll define.”  
But he botched the instruction  
With woeful induction  
And told us the next prime was nine.

3. Conservation of energy in relativistic mechanics is actually a much simpler concept than in nonrelativistic mechanics, because  $E = \gamma m c^2$  is conserved, period. We don't have to worry about the generation of internal energy (heat or internal potential energy), which ruins conservation of the nonrelativistic  $E = mv^2/2$ . The internal energy is simply built into the total energy. In the above example, the two  $m$ 's collide and generate internal energy (heat) in the resulting mass  $M$ . This internal energy shows up as an increase in mass, which makes  $M$  larger than  $2m$ . The energy that corresponds to the increase in mass comes from the initial kinetic energy of the two  $m$ 's.
4. Problem 12.1 gives an alternate derivation of the energy and momentum expressions in Eq. (12.1). This derivation uses additional facts, namely that the energy and momentum of a photon are given by  $E = h\nu$  and  $p = h\nu/c$ , where  $\nu$  is the frequency of the light, and  $h$  is Planck's constant. ♣

Any multiple of  $\gamma m c^2$  is also conserved, of course. Why did we pick  $\gamma m c^2$  to label as “ $E$ ” instead of, say,  $5\gamma m c^2$ ? Consider the approximate form that  $\gamma m c^2$  takes in the Newtonian limit, that is, in the limit  $v \ll c$ . We have, using the Taylor series expansion for  $(1 - x)^{-1/2}$ ,

$$\begin{aligned} E \equiv \gamma m c^2 &= \frac{m c^2}{\sqrt{1 - v^2/c^2}} \\ &= m c^2 \left( 1 + \frac{v^2}{2c^2} + \frac{3v^4}{8c^4} + \cdots \right) \\ &= m c^2 + \frac{1}{2} m v^2 + \cdots . \end{aligned} \quad (12.9)$$

The dots represent higher-order terms in  $v^2/c^2$ , which may be neglected if  $v \ll c$ . In an elastic collision in Newtonian physics, no heat is generated, so mass is conserved. That is, the quantity  $m c^2$  has a fixed value. We therefore see that conservation of  $E \equiv \gamma m c^2$  reduces to the familiar conservation of Newtonian kinetic energy,  $mv^2/2$ , for elastic collisions in the limit of slow speeds. This is an example of the *correspondence principle*, which says that relativistic formulas must reduce to the familiar nonrelativistic ones in the nonrelativistic limit. Likewise, for the momentum we picked  $\mathbf{p} \equiv \gamma m \mathbf{v}$  instead of, say,  $6\gamma m c^4 \mathbf{v}$ , because

<sup>3</sup> And in fact it isn't correct, because it doesn't incorporate quantum mechanics. The more complete theory that includes both relativity and quantum mechanics is quantum field theory.

the former reduces to the familiar Newtonian momentum,  $m\mathbf{v}$ , in the limit of slow speeds.

Whether abstract, profound, or just mystic,  
 Or boring, or somewhat simplistic,  
 A theory must lead  
 To results that we need  
 In limits, nonrelativistic.

Whenever we use the term “energy,” we will mean the total energy,  $\gamma mc^2$ . If we use the term “kinetic energy,” we will mean a particle’s excess energy over the energy it has when it is motionless. In other words, the kinetic energy is  $\gamma mc^2 - mc^2$ . Kinetic energy is *not* necessarily conserved in a collision, because mass is not necessarily conserved, as we saw in Eq. (12.6) in the above example. In the CM frame, there was kinetic energy before the collision, but none after. Kinetic energy is a rather artificial concept in relativity. You virtually always want to use the total energy,  $\gamma mc^2$ , when solving a problem.

Note the following important relation,

$$\begin{aligned} E^2 - |\mathbf{p}|^2 c^2 &= \gamma^2 m^2 c^4 - \gamma^2 m^2 |\mathbf{v}|^2 c^2 \\ &= \gamma^2 m^2 c^4 \left( 1 - \frac{v^2}{c^2} \right) \\ &= m^2 c^4. \end{aligned} \quad (12.10)$$

This is a primary ingredient in solving relativistic collision problems, as we’ll soon see. It replaces the  $K = p^2/2m$  relation between kinetic energy and momentum in Newtonian physics. It can be derived in more profound ways, as we’ll see in Chapter 13. It’s so important that I like to call it the Very Important Relation. Let’s put it in a box:

$$\boxed{E^2 = p^2 c^2 + m^2 c^4} \quad (12.11)$$

Whenever you know two of the three quantities  $E$ ,  $p$ , and  $m$ , this equation gives you the third. In the case where  $m = 0$  (as with photons), Eq. (12.11) says that

$$E = pc \quad (\text{for photons}). \quad (12.12)$$

This is the key equation for massless objects. For photons, the two equations,  $\mathbf{p} = \gamma m \mathbf{v}$  and  $E = \gamma mc^2$ , don’t tell us much, because  $m = 0$  and  $\gamma = \infty$ , so their product is undetermined. But  $E^2 - |\mathbf{p}|^2 c^2 = m^2 c^4$  still holds, and we conclude that  $E = pc$ . Note that any massless particle must have  $\gamma = \infty$ . That is, it must travel at speed  $c$ . If this weren’t the case, then  $E = \gamma mc^2$  would equal zero, in which case the particle wouldn’t be much of a particle. We’d have a hard time observing something with no energy.

Another nice relation, which follows from Eqs. (12.1) and holds for particles of any mass, is

$$\frac{\mathbf{p}}{E} = \frac{\mathbf{v}}{c^2}. \quad (12.13)$$

Given  $p$  and  $E$ , this is definitely the quickest way to get  $v$ .

#### *The general size of $mc^2$*

What is the general size of  $mc^2$ ?<sup>4</sup> If we let  $m = 1$  kg, then we have  $mc^2 = (1 \text{ kg})(3 \cdot 10^8 \text{ m/s})^2 \approx 10^{17} \text{ J}$ . How big is this? A typical household electric bill might be around \$50 per month, or \$600 per year. At about 10 cents per kilowatt-hour, this translates to 6000 kilowatt-hours per year. Since there are 3600 seconds in an hour, this converts to  $(6000)(10^3)(3600) \approx 2 \cdot 10^{10}$  watt-seconds. That is,  $2 \cdot 10^{10}$  joules per year. We therefore see that if one kilogram were converted completely into usable energy (that is, kinetic energy, which can then be used to drive a turbine), it would be enough to provide electricity to about  $10^{17}/(2 \cdot 10^{10})$ , or 5 million, homes for a year. That's a lot.

In a nuclear reactor, only a small fraction of the mass is converted into usable energy (heat). Most of the mass remains in the final products, which doesn't help in lighting your home. If a particle were to combine with its antiparticle, then it would be possible for all of the mass energy to be converted into usable energy. But we're a while away from being able to do this productively. However, even a small fraction of the very large quantity,  $E = mc^2$ , can be large, as evidenced by the use of nuclear power and nuclear weapons. Any quantity with a few factors of  $c$  is bound to change the face of the world.

#### *Mass*

Some treatments of relativity use the term “rest mass,”  $m_0$ , to refer to the mass of a motionless particle, and “relativistic mass,”  $m_{\text{rel}}$ , to refer to the quantity  $\gamma m_0$  of a moving particle. We won't use this terminology here. The only thing we'll call “mass” is what the above treatments call “rest mass.” (For example, the mass of an electron is  $9.11 \cdot 10^{-31}$  kg, and the mass of a liter of water is 1 kg, independent of their speed.) And since we'll refer to only one type of mass, there is no need to use the qualifier “rest” or the subscript “0.” We'll therefore simply use the notation “ $m$ .”

Of course, you can *define* the quantity  $\gamma m$  to be anything you want. There's nothing wrong with calling it “relativistic mass.” But the point is that  $\gamma m$  already goes by another name. It's just the energy, up to factors of  $c$ . The use of the word “mass” for this quantity, although quite permissible, is certainly not needed.

Furthermore, the word “mass” is used to describe what is on the right-hand side of the equation,  $E^2 - |\mathbf{p}|^2 c^2 = m^2$ . The  $m^2$  here is an *invariant*, that is,

<sup>4</sup> See Fadner (1988) for a history of the mass–energy relation.

it is something that is independent of the frame of reference. Although  $E$  and  $p$  depend on the frame because they involve  $v$ , this  $v$  dependence cancels out when taking the difference of their squares, yielding a frame-independent  $m^2$ . If “mass” is to be used in this definite way to describe an invariant, then it doesn’t make sense to also use it to describe the quantity  $\gamma m$ , which is frame-dependent. The prefixes “rest” and “relativistic” are introduced to avoid this problem, but the result of this is just a watering down of the very important invariance quality of “mass.”

However, since there is in fact nothing actually wrong with using “relativistic mass,” it mainly comes down to personal preference whether or not you like the term. Certainly one motivation for labeling  $\gamma m$  as some kind of mass is that the expression for momentum looks like  $p = \gamma m_0 v \equiv m_{\text{rel}} v$ , which mimics the Newtonian expression. And the expression for energy takes the nice form,  $E = \gamma m_0 c^2 \equiv m_{\text{rel}} c^2$ . But considering that Newtonian physics is only a limiting case of relativistic physics, it is questionable what is gained by molding a theory that is more correct into one that is less correct. At any rate, my view is that these nice formulas don’t outweigh the usefulness of having the word “mass” mean a very specific invariant quantity, with the word “energy” referring to the frame-dependent quantity  $\gamma m$ . Invariant quantities have a certain sacred place in physics, so they should be given a name that doesn’t have any noninvariant connotations.

#### *Lagrangian method*

Another way to motivate the above expressions for  $E$  and  $p$  is to use the Lagrangian method. To take this route, we must of course figure out what the relativistic Lagrangian is. This might seem like a daunting task, considering that the Lagrangians we dealt with in Chapter 6 involved the kinetic energy, and we have no idea yet what the energy is here (that’s one of our goals, after all).

It turns out, however, that it’s fairly easy to write down the relativistic Lagrangian, provided that we think outside the “ $T - V$ ” box and concentrate instead on the all-important fact that the action is something that is stationary for the classical path. Combining this fact with the relativity postulate, which states that there is no preferred reference frame, we see that the action must be stationary in all frames. A sensible property to require of the action is therefore that it be *independent* of the frame. This way, if it is stationary in one frame, then it is stationary in any other.<sup>5</sup>

What invariant quantities do we know of? Well, there are certainly  $m$  and  $c$ . But the more interesting one that we’re familiar with is the invariant interval (the proper time),  $c \, d\tau \equiv \sqrt{c^2 dt^2 - dx^2}$ . This is pretty much all we have to work

<sup>5</sup> I suppose you could imagine a quantity that depends on the frame, but that is still stationary in any frame. But clearly the simplest thing to try (which will in fact work) is something that is independent of the frame.

with, so let's try an action of the form (we'll just deal with a free particle),

$$S = -mc \int c \, d\tau = -mc \int \sqrt{c^2 dt^2 - dx^2} = -mc \int \sqrt{c^2 - \dot{x}^2} \, dt. \quad (12.14)$$

We have put the  $mc$  out front to give  $S$  the usual units of energy times time. And the minus sign (which doesn't affect the stationary property) is included so that we will obtain the correct signs for the energy and momentum. Our Lagrangian is therefore

$$L = -mc\sqrt{c^2 - \dot{x}^2}. \quad (12.15)$$

The Euler–Lagrange equation is thus

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}} \right) = \frac{\partial L}{\partial x} \implies \frac{d}{dt} \left( \frac{mc\dot{x}}{\sqrt{c^2 - \dot{x}^2}} \right) = 0. \quad (12.16)$$

The quantity in the parentheses can be written as

$$p \equiv \frac{mv}{\sqrt{1 - v^2/c^2}} \equiv \gamma mv. \quad (12.17)$$

This is simply the momentum we defined earlier, which, in view of Eq. (12.16), is conserved, as it should be. What about the energy? The energy associated with our Lagrangian is given by (using Eq. (6.52))

$$\begin{aligned} E &= \dot{x} \frac{\partial L}{\partial \dot{x}} - L = \dot{x} \left( \frac{mc\dot{x}}{\sqrt{c^2 - \dot{x}^2}} \right) - \left( -mc\sqrt{c^2 - \dot{x}^2} \right) \\ &= \frac{mc^3}{\sqrt{c^2 - \dot{x}^2}} = \frac{mc^2}{\sqrt{1 - v^2/c^2}} \equiv \gamma mc^2, \end{aligned} \quad (12.18)$$

which agrees with our earlier expression for  $E$ . We can also calculate the angular momentum. In polar coordinates, the Lagrangian can be written as

$$L = -mc\sqrt{c^2 - (\dot{r}^2 + r^2\dot{\theta}^2)}. \quad (12.19)$$

The Euler–Lagrange equation obtained from varying  $\theta$  is therefore

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\theta}} \right) = \frac{\partial L}{\partial \theta} \implies \frac{d}{dt} \left( \frac{mcr^2\dot{\theta}}{\sqrt{c^2 - (\dot{r}^2 + r^2\dot{\theta}^2)}} \right) = 0. \quad (12.20)$$

The quantity in the parentheses, which we see is conserved, can be written as  $\gamma mr^2\dot{\theta}$ . Because it is associated with the angle  $\theta$ , we call it the angular momentum. And as expected, it reduces properly to the nonrelativistic result when  $\gamma = 1$ .

Of course, this Lagrangian justification for  $E$  and  $p$  might seem a little silly, because we're just dealing with a free particle, and *any* quantity involving  $v$  is conserved for a free particle. But the fact that the above  $E$  and  $p$  can be derived from a Lagrangian involving an invariant quantity (which is the only nontrivial invariant quantity we know of) gives them a reasonable amount of credence.

If we want to go beyond a free particle and incorporate a potential energy into the system, things get more complicated; see Brehme (1971). The first thought that comes to mind is to simply subtract off a potential  $V(x)$  in the Lagrangian, as we did in the nonrelativistic case. We then have  $L = -mc\sqrt{c^2 - \dot{x}^2} - V(x)$ , and the Euler–Lagrange equation becomes

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}} \right) = \frac{\partial L}{\partial x} \implies \frac{d}{dt} \left( \frac{mc\dot{x}}{\sqrt{c^2 - \dot{x}^2}} \right) = -\frac{\partial V}{\partial x} \implies \frac{dp}{dt} = F(x). \quad (12.21)$$

This is the correct  $F = dp/dt$  statement, so it seems that we picked the right Lagrangian. However, there is something amiss here; the action now involves the quantity  $\int V(x) dt$  which isn't invariant, because the time in one frame doesn't equal the time in another. Although the above Lagrangian does indeed yield the correct equation of motion in the particular reference frame in which the function  $V(x)$  is defined, if we switch to another frame there is no guarantee that it will do so again. In order to maintain an invariant action, we must construct it from 4-vectors (discussed in Chapter 13), or other tensors, multiplied in an appropriate way. The classic system involving 4-vectors is a charged particle in an electromagnetic field. Other systems involving more complicated tensors occur in General Relativity. But we're not going to get into any of that here, because our goal was only to motivate the expressions for  $E$  and  $p$ .<sup>6</sup>

##### Setting $c = 1$

For the remainder of our treatment of relativity, we will invariably work in units where  $c = 1$ . For example, instead of one meter being the unit of distance, we can make  $3 \cdot 10^8$  meters equal to one unit. Or, we can keep the meter as is, and make  $1/(3 \cdot 10^8)$  seconds the unit of time. In such units, our various expressions become

$$\mathbf{p} = \gamma m \mathbf{v}, \quad E = \gamma m, \quad E^2 = p^2 + m^2, \quad \frac{\mathbf{p}}{E} = \mathbf{v}. \quad (12.22)$$

Said in another way, you can simply ignore all the  $c$ 's in your calculations (which will generally save you a lot of strife), and then put them back into your final answer to make the units correct. For example, let's say the goal of a certain

<sup>6</sup> In multiparticle systems, it turns out that in general it is impossible to create a consistent relativistic Lagrangian formalism. The only way to proceed is to work in terms of fields instead of particles. But this is well beyond the scope of what we're doing here. See Goldstein *et al.* (2002).

problem is to find the time of some event. If your answer comes out to be  $\ell$ , where  $\ell$  is a given length, then you know that the correct answer (in terms of the usual mks units) has to be  $\ell/c$ , because this has units of time. In order for this procedure to work, there must be only one way to put the  $c$ 's back in at the end. This is always the case, because if there were two ways, then we would have  $c^a = c^b$ , for some numbers  $a \neq b$ . But this is impossible, because  $c$  has units.

![Diagram showing two coordinate systems, S and S', with their x and x' axes. Frame S' is moving to the right relative to frame S with velocity v. A particle is shown in frame S' with velocity u'.](bc389df671a6baa49bb8a5a5f0b84f18_img.jpg)

The diagram illustrates two inertial frames of reference, S and S'. Frame S has a horizontal x-axis. Frame S' is shown to the right of S, with its x'-axis parallel to the x-axis. An arrow labeled 'v' points from the origin of S towards the origin of S', indicating that S' is moving with velocity v relative to S in the positive x direction. A particle is depicted as a black dot within the S' frame, with an arrow labeled 'u'' pointing to the right, representing the particle's velocity in the S' frame.

Diagram showing two coordinate systems, S and S', with their x and x' axes. Frame S' is moving to the right relative to frame S with velocity v. A particle is shown in frame S' with velocity u'.

Fig. 12.6

## 12.2 Transformations of $E$ and $p$

Consider the following one-dimensional situation, where all the motion is along the  $x$  axis. A particle has energy  $E'$  and momentum  $p'$  in frame  $S'$ . Frame  $S'$  moves at speed  $v$  with respect to frame  $S$ , in the positive  $x$  direction (see Fig. 12.6). What are  $E$  and  $p$  in  $S$ ?

Let  $u'$  be the particle's speed in  $S'$ . From the velocity-addition formula, the particle's speed in  $S$  is (dropping the factors of  $c$ )

$$u = \frac{u' + v}{1 + u'v}. \quad (12.23)$$

This is all we need to know, because a particle's velocity determines its energy and momentum. But we'll need to go through a little algebra to make things look nice and pretty. The  $\gamma$  factor associated with the speed  $u$  is

$$\gamma_u = \frac{1}{\sqrt{1 - \left(\frac{u'+v}{1+u'v}\right)^2}} = \frac{1 + u'v}{\sqrt{(1 - u'^2)(1 - v^2)}} \equiv \gamma_{u'}\gamma_v(1 + u'v). \quad (12.24)$$

The energy and momentum in  $S'$  are

$$E' = \gamma_{u'}m, \quad \text{and} \quad p' = \gamma_{u'}mu', \quad (12.25)$$

while the energy and momentum in  $S$  are, using Eq. (12.24),

$$\begin{aligned} E &= \gamma_u m = \gamma_{u'}\gamma_v(1 + u'v)m, \\ p &= \gamma_u mu = \gamma_{u'}\gamma_v(1 + u'v)m \left( \frac{u' + v}{1 + u'v} \right) = \gamma_{u'}\gamma_v(u' + v)m. \end{aligned} \quad (12.26)$$

Using the  $E'$  and  $p'$  from Eqs. (12.25), we can rewrite  $E$  and  $p$  as (with  $\gamma \equiv \gamma_v$ )

$$\begin{aligned} E &= \gamma(E' + vp'), \\ p &= \gamma(p' + vE'). \end{aligned} \quad (12.27)$$

These are transformations for  $E$  and  $p$  between frames. If you want to put the factors of  $c$  back in, then the  $vE'$  term becomes  $vE'/c^2$ , to make the units correct. These transformations are easy to remember, because they look *exactly* like the

Lorentz transformations for the coordinates  $t$  and  $x$  in Eq. (11.21). More precisely with the  $c$ 's included,  $E$  and  $pc$  transform like  $ct$  and  $x$ , respectively.<sup>7</sup> This is no coincidence, as we will see in Chapter 13. As a check on Eqs. (12.27), if  $u' = 0$  (so that  $p' = 0$  and  $E' = m$ ), then  $E = \gamma m$  and  $p = \gamma mv$ , as expected. Also, if  $u' = -v$  (so that  $p' = -\gamma mv$  and  $E' = \gamma m$ ), then  $E = m$  and  $p = 0$ , as expected.

Because the transformations in Eqs. (12.27) are linear, they also hold if  $E$  and  $p$  represent the total energy and momentum of a collection of particles. That is,

$$\begin{aligned}\sum E &= \gamma \left( \sum E' + v \sum p' \right), \\ \sum p &= \gamma \left( \sum p' + v \sum E' \right).\end{aligned}\tag{12.28}$$

In fact, any (corresponding) linear combinations of the energies and momenta are valid here, in place of the sums. For example, we can use the combinations  $(E_1^b + 3E_2^a - 7E_3^b)$  and  $(p_1^b + 3p_2^a - 7p_3^b)$  in Eqs. (12.27), where the subscripts indicate which particle, and the superscripts indicate before or after a collision. You can verify this by simply taking the appropriate linear combination of Eqs. (12.27) for the various particles. This consequence of linearity is a very important and useful result, as will become clear in the remarks below.

You can use Eqs. (12.27) to show that

$$E^2 - p^2 = E'^2 - p'^2,\tag{12.29}$$

just as we showed that  $t^2 - x^2 = t'^2 - x'^2$  in Eq. (11.40). The proof there was based on the fact that  $t$  and  $x$  transform under the Lorentz transformations, so exactly the same proof works here with  $E$  and  $p$ , in view of the Lorentz transformations in Eqs. (12.27). The  $E$ 's and  $p$ 's in Eq. (12.29) can represent any (corresponding) linear combinations of the  $E$ 's and  $p$ 's of the various particles (for example, the total  $E$  and  $p$  of the particles), due to the linearity of Eqs. (12.27). For one particle, we already know that Eq. (12.29) is true, because both sides are equal to  $m^2$ , from Eq. (12.10). For many particles, the invariant quantity  $E_{\text{total}}^2 - p_{\text{total}}^2$  equals the square of the total energy in the CM frame (which reduces to  $m^2$  for one particle), because  $p_{\text{total}} = 0$  in the CM frame, by definition.

#### REMARKS:

1. In the previous section, we said that we needed to show that if  $E$  and  $p$  are conserved in one reference frame during a collision, then they are conserved in any other frame (because a conservation law shouldn't depend on what frame you're in). This can be shown as follows. The total  $\Delta E$  is a linear combination of the initial and final  $E$ 's, and likewise for

<sup>7</sup> Since the Lorentz transformations are symmetric in  $ct$  and  $x$ , and likewise in  $E$  and  $pc$ , it isn't clear which coordinate in one transformation corresponds to which coordinate in the other. But since  $x$  and  $p$  are the components of vectors, while  $t$  and  $E$  aren't, the correct correspondence must be  $ct \longleftrightarrow E$  and  $x \longleftrightarrow pc$ .

$\Delta p$ . Therefore, since Eq. (12.27) is a linear equation in the  $E$ 's and  $p$ 's, it also holds for the  $\Delta E$ 's and  $\Delta p$ 's. That is,

$$\Delta E = \gamma(\Delta E' + v\Delta p'), \quad \text{and} \quad \Delta p = \gamma(\Delta p' + v\Delta E'). \quad (12.30)$$

So if the total  $\Delta E'$  and  $\Delta p'$  in  $S'$  are zero, then the total  $\Delta E$  and  $\Delta p$  in  $S$  must also be zero.

2. Equation (12.30) makes it clear that if you accept the fact that  $p = \gamma mv$  is conserved in all frames, then you must also accept the fact that  $E = \gamma m$  is conserved in all frames (and vice versa). This is true because the second of Eqs. (12.30) says that if  $\Delta p$  and  $\Delta p'$  are both zero, then  $\Delta E'$  must also be zero.  $E$  and  $p$  have no choice but to go hand in hand. ♣

Equation (12.27) applies to the  $x$  component of the momentum. How do the transverse components,  $p_y$  and  $p_z$ , transform? Just as with the  $y$  and  $z$  coordinates in the Lorentz transformations,  $p_y$  and  $p_z$  don't change between frames. The analysis in Chapter 13 makes this obvious, so for now we'll simply state that if the relative velocity between the frames is in the  $x$  direction, then

$$p_y = p'_y, \quad \text{and} \quad p_z = p'_z. \quad (12.31)$$

If you really want to show explicitly that the transverse components don't change between frames, or if you're worried that a nonzero speed in the  $y$  direction will mess up the relationship between  $p_x$  and  $E$  that we calculated in Eq. (12.27), then Exercise 12.23 is for you. But it's a bit tedious, so feel free to settle for the much cleaner reasoning in Chapter 13.

## 12.3 Collisions and decays

The strategy for studying relativistic collisions is the same as that for studying nonrelativistic ones. You just have to write down all the conservation of energy and momentum equations, and then solve for whatever variables you want to solve for. The conservation principles are the same as they've always been. The only difference is that now the energy and momentum take the new forms in Eqs. (12.1). In writing down the conservation of energy and momentum equations, it proves extremely useful to put  $E$  and  $\mathbf{p}$  together into one four-component vector,

$$P \equiv (E, \mathbf{p}) \equiv (E, p_x, p_y, p_z). \quad (12.32)$$

This is called the *energy–momentum 4-vector*, or the *4-momentum*, for short. If we were keeping in the factors of  $c$ , then the first term would be  $E/c$ , although some people instead multiply the  $\mathbf{p}$  by  $c$ ; either convention is fine. Our notation in this chapter will be to use an uppercase  $P$  to denote a 4-momentum and a lowercase  $\mathbf{p}$  or  $p$  to denote a spatial momentum. The components of a 4-momentum are usually indexed from 0 to 3, so that  $P_0 \equiv E$ , and  $(P_1, P_2, P_3) \equiv \mathbf{p}$ . For one particle, we have

$$P = (\gamma m, \gamma m v_x, \gamma m v_y, \gamma m v_z). \quad (12.33)$$

The 4-momentum for a collection of particles consists of the total  $E$  and total  $\mathbf{p}$  of all the particles. There are deep reasons for considering the 4-momentum, as we'll see in Chapter 13, but for now we'll just view it as a matter of convenience. If nothing else, it helps with the bookkeeping. Conservation of energy and momentum in a collision reduce to the concise statement,

$$P_{\text{before}} = P_{\text{after}}, \quad (12.34)$$

where these are the total 4-momenta of all the particles.

If we define the *inner product* between two 4-momenta,  $A \equiv (A_0, A_1, A_2, A_3)$  and  $B \equiv (B_0, B_1, B_2, B_3)$ , to be

$$A \cdot B \equiv A_0 B_0 - A_1 B_1 - A_2 B_2 - A_3 B_3, \quad (12.35)$$

then the Very Important Relation in Eq. (12.11),  $E^2 - p^2 = m^2$ , which is true for one particle, may be concisely written as

$$P \cdot P = m^2, \quad \text{or} \quad P^2 = m^2, \quad (12.36)$$

where  $P^2 \equiv P \cdot P$ . In other words, the square of a particle's 4-momentum equals the square of its mass. This relation will prove to be very useful in collision problems. Note that it is frame-independent, as we saw in Eq. (12.29).

This inner product is different from the one we're used to in three-dimensional space. It has one positive sign and three negative signs, in contrast with the usual three positive signs. But we are free to define it however we wish, and we did indeed pick a good definition, because our inner product is invariant under Lorentz transformations, just as the usual 3-D inner product is invariant under rotations. For the inner product of a 4-momentum with itself (which could be any linear combination of 4-momenta of various particles), this invariance is the statement in Eq. (12.29). For the inner product of two different 4-momenta, we'll prove the invariance in Section 13.3.

---

**Example (Relativistic billiards):** A particle with mass  $m$  and energy  $E$  approaches an identical particle at rest. They collide elastically<sup>8</sup> in such a way that they both scatter at an angle  $\theta$  relative to the incident direction (see Fig. 12.7). What is  $\theta$  in terms of  $E$  and  $m$ ? What is  $\theta$  in the relativistic and nonrelativistic limits?

**Solution:** The first thing we should do is write down the 4-momenta. The 4-momenta before the collision are

$$P_1 = (E, p, 0, 0), \quad P_2 = (m, 0, 0, 0), \quad (12.37)$$

<sup>8</sup> An elastic collision in nonrelativistic physics is defined as one in which no heat is generated. In relativity, heat shows up as mass. So an elastic collision in relativistic physics is defined as one in which none of the masses change.

![Diagram of a relativistic elastic collision. A particle with mass m and energy E moves horizontally to the right, indicated by a dot and an arrow. It approaches a stationary particle of the same mass m, represented by a dot. After the collision, both particles move away from the point of impact. Their paths are shown as arrows originating from a common point. A horizontal dashed line represents the original direction of the incident particle. Both scattered particles make an angle theta with this dashed line, one above and one below. A curved arrow indicates the deflection of the particles.](e278c4c3f892963e2fea5a56a90e7199_img.jpg)

Diagram of a relativistic elastic collision. A particle with mass m and energy E moves horizontally to the right, indicated by a dot and an arrow. It approaches a stationary particle of the same mass m, represented by a dot. After the collision, both particles move away from the point of impact. Their paths are shown as arrows originating from a common point. A horizontal dashed line represents the original direction of the incident particle. Both scattered particles make an angle theta with this dashed line, one above and one below. A curved arrow indicates the deflection of the particles.

Fig. 12.7

where  $p = \sqrt{E^2 - m^2}$ . The 4-momenta after the collision are (primes now denote “after”)

$$P'_1 = (E', p' \cos \theta, p' \sin \theta, 0), \quad P'_2 = (E', p' \cos \theta, -p' \sin \theta, 0), \quad (12.38)$$

where  $p' = \sqrt{E'^2 - m^2}$ . Conservation of energy gives  $E' = (E + m)/2$ , and conservation of  $p_x$  gives  $p' \cos \theta = p/2$ . Therefore, the 4-momenta after the collision are

$$P'_{1,2} = \left( \frac{E+m}{2}, \frac{p}{2}, \pm \frac{p}{2} \tan \theta, 0 \right). \quad (12.39)$$

From Eq. (12.36), the squares of these 4-momenta must be  $m^2$ . Therefore,

$$\begin{aligned} m^2 &= \left( \frac{E+m}{2} \right)^2 - \left( \frac{p}{2} \right)^2 (1 + \tan^2 \theta) \\ \implies 4m^2 &= (E+m)^2 - \frac{(E^2 - m^2)}{\cos^2 \theta} \\ \implies \cos^2 \theta &= \frac{E^2 - m^2}{E^2 + 2Em - 3m^2} = \frac{E+m}{E+3m}. \end{aligned} \quad (12.40)$$

The relativistic limit is  $E \gg m$ , which yields  $\cos \theta \approx 1$ . This means that both particles scatter almost directly forward. You can convince yourself that  $\theta$  should be small by looking at the collision in the CM frame and then shifting back to the lab frame. The transverse speeds decrease during this shift of frames.

The nonrelativistic limit is  $E \approx m$  (it's *not*  $E \approx 0$ ), which yields  $\cos \theta \approx 1/\sqrt{2}$ . So  $\theta \approx 45^\circ$ , and the particles scatter with a  $90^\circ$  angle between them. This agrees with the result from the “Billiards” example in Section 5.7.2, a result which pool players are very familiar with.

---

Note that we never wrote down any  $v$ 's in the above solution. That is, we never used the relations  $E = \gamma mc^2$  and  $p = \gamma mv$ . There was no need to find the velocities; doing so would have essentially involved going in circles. Using  $E = \gamma mc^2$  and  $p = \gamma mv$  certainly provides a valid way of solving the problem, but in many situations like this one, where velocities aren't given or explicitly asked for, it leads to a very messy solution. A far cleaner method is to use the  $E^2 - p^2 = m^2$  relation.

If  $\gamma mv$  yields frustration,  
 And the similar  $E$ , irritation,  
 Just ditch all the  $v$ 's,  
 And use (won't you please)  
 The Very Important Relation!

Let's now look at a decay. Decays are basically the same as collisions. All you have to do is conserve energy and momentum, as the following example shows.

**Example (Decay at an angle):** A particle with mass  $M$  and energy  $E$  decays into two identical particles. In the lab frame, one of them is emitted at a  $90^\circ$  angle, as shown in Fig. 12.8. What are the energies of the created particles? We'll give two solutions. The second one shows how 4-momenta can be used in a very clever and time-saving way.

![Diagram of a particle decay. A particle with mass M and energy E moves horizontally to the right. It decays into two identical particles. One of the decay products is emitted vertically upwards, perpendicular to the initial direction of motion. The other decay product is emitted at an angle below the horizontal. A dashed line indicates the horizontal direction, and a right-angle symbol indicates the 90-degree angle between the initial direction and the vertically emitted particle.](7d059f4ead193721b79717a3c9117d90_img.jpg)

Diagram of a particle decay. A particle with mass M and energy E moves horizontally to the right. It decays into two identical particles. One of the decay products is emitted vertically upwards, perpendicular to the initial direction of motion. The other decay product is emitted at an angle below the horizontal. A dashed line indicates the horizontal direction, and a right-angle symbol indicates the 90-degree angle between the initial direction and the vertically emitted particle.

Fig. 12.8

**First solution:** The 4-momentum before the decay is

$$P = (E, p, 0, 0), \quad (12.41)$$

where  $p = \sqrt{E^2 - M^2}$ . Let the created particles have mass  $m$ , and let the second particle make an angle  $\theta$  with the  $x$  axis. The 4-momenta after the decay are

$$P_1 = (E_1, 0, p_1, 0), \quad P_2 = (E_2, p_2 \cos \theta, -p_2 \sin \theta, 0). \quad (12.42)$$

Conservation of  $p_x$  immediately gives  $p_2 \cos \theta = p$ , which then implies that  $p_2 \sin \theta = p \tan \theta$ . Conservation of  $p_y$  says that the final  $p_y$ 's are opposites. Therefore, the 4-momenta after the decay are

$$P_1 = (E_1, 0, p \tan \theta, 0), \quad P_2 = (E_2, p, -p \tan \theta, 0). \quad (12.43)$$

Conservation of energy gives  $E = E_1 + E_2$ . Writing  $E_1$  and  $E_2$  in terms of the momenta and masses, this becomes

$$E = \sqrt{p^2 \tan^2 \theta + m^2} + \sqrt{p^2(1 + \tan^2 \theta) + m^2}. \quad (12.44)$$

Putting the first radical on the left side, squaring, and solving for that radical (which is  $E_1$ ) gives

$$E_1 = \frac{E^2 - p^2}{2E} = \frac{M^2}{2E}. \quad (12.45)$$

In a similar manner, we find that  $E_2$  equals

$$E_2 = \frac{E^2 + p^2}{2E} = \frac{2E^2 - M^2}{2E}. \quad (12.46)$$

These add up to  $E$ , as they should.

**Second solution:** With the 4-momenta defined as in Eqs. (12.41) and (12.42), conservation of energy and momentum can be combined into the statement,  $P = P_1 + P_2$ . Therefore,

$$\begin{aligned} P - P_1 &= P_2, \\ \Rightarrow (P - P_1) \cdot (P - P_1) &= P_2 \cdot P_2, \\ \Rightarrow P^2 - 2P \cdot P_1 + P_1^2 &= P_2^2, \\ \Rightarrow M^2 - 2EE_1 + m^2 &= m^2, \\ \Rightarrow E_1 &= \frac{M^2}{2E}. \end{aligned} \quad (12.47)$$

And then  $E_2 = E - E_1 = (2E^2 - M^2)/2E$ . This solution should convince you that 4-momenta can save you a lot of work. What happened here was that the expression for  $P_2$  was fairly messy, but we arranged things so that it appeared only in the form of  $P_2^2$ , which is simply  $m^2$ . 4-momenta provide a remarkably organized method for sweeping unwanted garbage under the rug.

## 12.4 Particle-physics units

A branch of physics that uses relativity as one of its main ingredients is elementary-particle physics, which is the study of the building blocks of matter (electrons, quarks, neutrinos, etc.). It's unfortunately the case that most of the elementary particles we want to study don't exist naturally in the world. We therefore have to create them in particle accelerators by colliding other particles together at very high energies. The high speeds involved require the use of relativistic dynamics. Newtonian physics is essentially useless.

What is a typical size of a rest energy,  $mc^2$ , of an elementary particle? The rest energy of a proton (which isn't really elementary; it's made up of quarks, but never mind) is

$$E_p = m_p c^2 = (1.67 \cdot 10^{-27} \text{ kg})(3 \cdot 10^8 \text{ m/s})^2 = 1.5 \cdot 10^{-10} \text{ joules.} \quad (12.48)$$

This is very small, of course. So a joule is probably not the best unit to work with. We would get very tired of writing the negative exponents over and over. We could perhaps work with “nanojoules,” but particle physicists like to work instead with the “eV,” the *electron-volt*. This is the change in energy of an electron when it passes through a potential of one volt. The electron charge is (negative)  $e = 1.602 \cdot 10^{-19} \text{ C}$ , and a volt is defined as  $1 \text{ V} = 1 \text{ J/C}$ . So the conversion from eV to joules is<sup>9</sup>

$$1 \text{ eV} = (1.602 \cdot 10^{-19} \text{ C})(1 \text{ J/C}) = 1.602 \cdot 10^{-19} \text{ J.} \quad (12.49)$$

Therefore, in terms of eV, the rest energy of a proton is  $938 \cdot 10^6 \text{ eV}$ . We now have the opposite problem of having a large exponent hanging around. But this is easily remedied by the prefix “M,” which stands for “mega” or “million.” So we finally have a proton rest energy of

$$E_p = 938 \text{ MeV.} \quad (12.50)$$

<sup>9</sup> This is getting a little picky, but “eV” should technically be written as “eV,” because when people write “eV,” they actually mean that two things are being multiplied together (in contrast with, for example, the “kg” symbol for “kilogram”). One of these things is the electron charge, which is usually denoted by  $e$ .

You can work out for yourself that an electron has a rest energy of  $E_e = 0.511$  MeV. The rest energies of various particles are listed in the table below. The ones preceded by a “ $\approx$ ” are the averages of differently charged particles, whose energies differ by a few MeV. These (and the many other) elementary particles have specific properties (spin, charge, etc.), but for the present purposes they need only be thought of as point objects having a definite mass.

| Particle           | Rest energy (MeV) |
|--------------------|-------------------|
| electron (e)       | 0.511             |
| muon ($\mu$)       | 105.7             |
| tau ($\tau$)       | 1784              |
| proton (p)         | 938.3             |
| neutron (n)        | 939.6             |
| lambda ($\Lambda$) | 1115.6            |
| sigma ($\Sigma$)   | $\approx 1193$    |
| delta ($\Delta$)   | $\approx 1232$    |
| pion ($\pi$)       | $\approx 137$     |
| kaon (K)           | $\approx 496$     |

For higher energies, the prefixes “G” (for “giga,” meaning  $10^9$ ) and “T” (for “tera,” meaning  $10^{12}$ ) are used.

We now come to a slight abuse of language. When particle physicists talk about masses, they say things like, “The mass of a proton is 938 MeV.” This, of course, makes no sense, because the units are wrong; a mass can’t equal an energy. But what they mean is that if you take this energy and divide it by  $c^2$ , then you get the mass. It would truly be a pain to keep saying, “The mass is such-and-such an energy, divided by  $c^2$ .” For a quick conversion back to kilograms, you can show that

$$1 \text{ MeV}/c^2 = 1.783 \cdot 10^{-30} \text{ kg}. \quad (12.51)$$

## 12.5 Force

### 12.5.1 Force in one dimension

In nonrelativistic physics, Newton’s second law is  $F = dp/dt$ , which reduces to  $F = ma$  if the mass is constant. We’ll carry this law over to relativity and continue to write (we’ll just deal with one-dimensional motion for now)

$$F = \frac{dp}{dt}. \quad (12.52)$$

However, in relativity we have  $p = \gamma mv$ , and  $\gamma$  can change with time. This complicates things, and it turns out that  $F$  does *not* equal  $ma$ . But if  $dp/dt$  and  $ma$  are different, why does  $F$  equal  $dp/dt$  instead of  $ma$ ? Perhaps the best reason arises from the 4-vector formalism in Chapter 13. But another reason is that the  $F$  in Eq. (12.52) leads to a familiar work–energy theorem, as we’ll see in Eq. (12.57).

To see what form the  $F$  in Eq. (12.52) takes in terms of the acceleration  $a \equiv \dot{v}$ , let’s first calculate  $d\gamma/dt$ :

$$\frac{d\gamma}{dt} \equiv \frac{d}{dt} \left( \frac{1}{\sqrt{1-v^2}} \right) = \frac{v\dot{v}}{(1-v^2)^{3/2}} \equiv \gamma^3 va. \quad (12.53)$$

Assuming that  $m$  is constant, we therefore have

$$F = \frac{d(\gamma mv)}{dt} = m(\dot{\gamma}v + \gamma\dot{v}) = ma\gamma(\gamma^2 v^2 + 1) = \gamma^3 ma. \quad (12.54)$$

This doesn’t look as nice as  $F = ma$ , but that’s the way it goes. However,  $F$  correctly reduces to  $ma$  in the limit of small speeds (where  $\gamma \approx 1$ ), as it must.

They said, “ $F$  is  $ma$ , bar none.”

What they *meant* wasn’t quite as much fun.

It’s  $dp$  by  $dt$ ,

Which just happens to be

Good ol’ “ $ma$ ” when  $\gamma$  is 1.

Consider now the quantity  $dE/dx$ , where  $E$  is the energy,  $E = \gamma m$ . We have

$$\frac{dE}{dx} = \frac{d(\gamma m)}{dx} = m \frac{d(1/\sqrt{1-v^2})}{dx} = \gamma^3 mv \frac{dv}{dx}. \quad (12.55)$$

But  $v(dv/dx) = (dx/dt)(dv/dx) = dv/dt = a$ . Therefore,  $dE/dx = \gamma^3 ma$ . Combining this with Eq. (12.54) gives

$$F = \frac{dE}{dx}. \quad (12.56)$$

Note that Eqs. (12.52) and (12.56) take exactly the same form as in nonrelativistic physics. The only new thing in relativity is that the expressions for  $p$  and  $E$  are modified.

**REMARK:** The result in Eq. (12.56) suggests another way to motivate the  $E = \gamma m$  expression. The reasoning is exactly the same as in the derivation of nonrelativistic energy conservation in Section 5.1. Define  $F$ , as we have done, through Eq. (12.52). Then integrate Eq. (12.54) from  $x_1$  to  $x_2$  to obtain

$$\int_{x_1}^{x_2} F dx = \int_{x_1}^{x_2} (\gamma^3 ma) dx = \int_{x_1}^{x_2} \left( \gamma^3 mv \frac{dv}{dx} \right) dx = \int_{v_1}^{v_2} \gamma^3 mv dv = \gamma m \Big|_{v_1}^{v_2}, \quad (12.57)$$

where we have used the  $d\gamma = \gamma^3 v dv$  relation from Eq. (12.55). We see that if we define the energy as  $E = \gamma m$ , then the work–energy theorem,  $\int F dx = \Delta E$ , holds in relativity just as it does in Newtonian physics. The only difference is that  $E$  is  $\gamma m$  instead of  $mv^2/2$ .<sup>10</sup> ♣

### 12.5.2 Force in two dimensions

In two dimensions, the concept of force becomes a little strange. In particular, as we’ll see, the acceleration of an object need not point in the same direction as the force. We start with

$$\mathbf{F} = \frac{d\mathbf{p}}{dt}. \quad (12.58)$$

This is a vector equation. Without loss of generality, we’ll deal with only two spatial dimensions. Consider a particle moving in the  $x$  direction, and let us apply a force,  $\mathbf{F} = (F_x, F_y)$ . The particle’s momentum is

$$\mathbf{p} = \frac{m(v_x, v_y)}{\sqrt{1 - v_x^2 - v_y^2}}. \quad (12.59)$$

Taking the derivative of this, and using the fact that  $v_y$  is initially zero, we obtain

$$\begin{aligned} \mathbf{F} &= \frac{d\mathbf{p}}{dt} \bigg|_{v_y=0} \\ &= m \left( \frac{\dot{v}_x}{\sqrt{1 - v^2}} + \frac{v_x(v_x \dot{v}_x + v_y \dot{v}_y)}{(\sqrt{1 - v^2})^3}, \frac{\dot{v}_y}{\sqrt{1 - v^2}} + \frac{v_y(v_x \dot{v}_x + v_y \dot{v}_y)}{(\sqrt{1 - v^2})^3} \right) \bigg|_{v_y=0} \\ &= m \left( \frac{\dot{v}_x}{\sqrt{1 - v^2}} \left( 1 + \frac{v^2}{1 - v^2} \right), \frac{\dot{v}_y}{\sqrt{1 - v^2}} \right) \\ &= m \left( \frac{\dot{v}_x}{(\sqrt{1 - v^2})^3}, \frac{\dot{v}_y}{\sqrt{1 - v^2}} \right) \\ &\equiv m(\gamma^3 a_x, \gamma a_y). \end{aligned} \quad (12.60)$$

This is *not* proportional to  $(a_x, a_y)$ . The first component agrees with Eq. (12.54), but the second component has only one factor of  $\gamma$ . The difference comes from the fact that  $\gamma$  has a first-order change if  $v_x$  changes, but not if  $v_y$  changes, assuming that  $v_y$  is initially zero. The particle therefore responds differently to forces in the  $x$  and  $y$  directions. It is easier to accelerate something in the transverse direction.

<sup>10</sup> Actually, this reasoning suggests only that  $E$  is given by  $\gamma m$  up to an additive constant. For all we know,  $E$  might take the form,  $E = \gamma m - m$ , which would make the energy of a motionless particle equal to zero. An argument along the lines of Section 12.1.2 is required to show that the additive constant is zero.

![Diagram showing two coordinate frames, S and S', with their respective x and x' axes. Frame S' is moving with velocity v relative to frame S along the x-axis.](52170c121daaf9af0f70110eeaebb698_img.jpg)

The diagram illustrates two inertial frames of reference, S and S'. Frame S has a horizontal x-axis and a vertical y-axis. Frame S' is shown to the right of S, with its x'-axis parallel to the x-axis and its y'-axis parallel to the y-axis. An arrow labeled 'v' points from the origin of S towards the origin of S', indicating that S' is moving with a constant velocity v relative to S along the positive x-direction.

Diagram showing two coordinate frames, S and S', with their respective x and x' axes. Frame S' is moving with velocity v relative to frame S along the x-axis.

Fig. 12.9

### 12.5.3 Transformation of forces

Let a force act on a particle. How are the components of the force in the particle's frame,  $S'$ , related to the components of the force in another frame,  $S$ ?<sup>11</sup> Let the relative motion be along the  $x$  and  $x'$  axes, as shown in Fig. 12.9. In frame  $S$ , Eq. (12.60) says

$$(F_x, F_y) = m(\gamma^3 a_x, \gamma a_y). \quad (12.61)$$

And in frame  $S'$ , the  $\gamma$  factor for the particle equals 1, so Eq. (12.60) reduces to the usual expression,

$$(F'_x, F'_y) = m(a'_x, a'_y). \quad (12.62)$$

Let's now relate these two forces, by writing the primed accelerations on the right-hand side of Eq. (12.62) in terms of the unprimed accelerations.

First, we have  $a'_y = \gamma^2 a_y$ . This is true because transverse distances are the same in the two frames, but times are shorter in  $S'$  by a factor  $\gamma$ . That is,  $dt' = dt/\gamma$ . We have indeed put the  $\gamma$  in the right place here, because the particle is essentially at rest in  $S'$ , so the usual time dilation holds. Therefore,  $a'_y \equiv d^2y'/dt'^2 = d^2y/(dt/\gamma)^2 \equiv \gamma^2 a_y$ .

Second, we have  $a'_x = \gamma^3 a_x$ . In short, this is true because time dilation brings in two factors of  $\gamma$  (as in the  $a_y$  case), and length contraction brings in one. In more detail: Let the particle move from one point to another in frame  $S'$ , as it accelerates from rest in  $S'$ . Mark these two points, which are essentially a distance  $a'_x(dt')^2/2$  apart, in  $S'$ . As  $S'$  flies past  $S$ , the distance between the two marks is length contracted by a factor  $\gamma$ , as viewed by  $S$ . This distance (which is the excess distance the particle travels over what it would have traveled if there were no acceleration) is what  $S$  calls  $a_x(dt)^2/2$ . Therefore,

$$\frac{1}{2} a_x dt^2 = \frac{1}{\gamma} \left( \frac{1}{2} a'_x dt'^2 \right) \implies a'_x = \gamma a_x \left( \frac{dt}{dt'} \right)^2 = \gamma^3 a_x. \quad (12.63)$$

Equation (12.62) may now be written as

$$(F'_x, F'_y) = m(\gamma^3 a_x, \gamma^2 a_y). \quad (12.64)$$

Comparing Eqs. (12.61) and (12.64) then gives

$$F_x = F'_x, \quad \text{and} \quad F_y = \frac{F'_y}{\gamma}. \quad (12.65)$$

We see that the longitudinal force is the same in the two frames, but the transverse force is larger by a factor of  $\gamma$  in the particle's frame.

<sup>11</sup> To be more precise,  $S'$  is the instantaneous inertial frame of the particle. Once the force is applied, the particle will accelerate and will therefore no longer be at rest in  $S'$ . But for a very small elapsed time, the particle will still essentially be in  $S'$ .

#### REMARKS:

1. What if someone comes along and switches the labels of the primed and unprimed frames in Eq. (12.65), and concludes that the transverse force is *smaller* in the particle's frame? He certainly can't be correct, given that Eq. (12.65) is true, but where is the error? The error lies in the fact that we (correctly) used  $dt' = dt/\gamma$  above, because this is the relevant expression concerning two events along the particle's worldline. We are interested in two such events, because we want to see how the particle moves. The inverted expression,  $dt = dt'/\gamma$ , deals with two events located at the same position in  $S$ , and therefore has nothing to do with the situation at hand. Similar reasoning holds for the relation between  $dx$  and  $dx'$ . Because we are dealing with a given particle, there is indeed one frame that is special among all possible frames, namely the particle's instantaneous inertial frame.
2. If you want to compare forces in two frames, neither of which is the particle's rest frame, then just use Eq. (12.65) twice and relate each of the forces to the rest-frame forces. It quickly follows that for another frame  $S''$ , we have  $F''_x = F_x$ , and  $F''_y = \gamma F_y$ , where the  $\gamma$ 's are measured relative to the rest frame  $S'$ . ♣

**Example (Bead on a rod):** A spring with a tension has one end attached to the end of a rod, and the other end attached to a bead that is constrained to move along the rod. The rod makes an angle  $\theta'$  with respect to the  $x'$  axis, and is fixed at rest in the  $S'$  frame (see Fig. 12.10). The bead is released and is pulled along the rod by the spring. Right after the bead is released, what does the situation look like in the frame,  $S$ , of someone moving to the left at speed  $v$ ? In answering this, draw the directions of

- (a) the rod,
- (b) the acceleration of the bead,
- (c) the force on the bead.

In frame  $S$ , does the wire exert a force of constraint?

**Solution:** In frame  $S$ :

- (a) The horizontal span of the rod is decreased by a factor  $\gamma$ , due to length contraction, and the vertical span is unchanged, so we have  $\tan \theta = \gamma \tan \theta'$ , as shown in Fig. 12.11.
- (b) The acceleration must point along the rod, because the bead always lies on the rod, and because the rod moves at constant speed in  $S$ . Quantitatively, the position of the bead in  $S$  takes the form of  $(x, y) = (vt - a_x t^2/2, -a_y t^2/2)$ , by the definition of acceleration. The position relative to the starting point on the rod, which has coordinates  $(vt, 0)$ , is then  $(\Delta x, \Delta y) = (-a_x t^2/2, -a_y t^2/2)$ . The condition for the bead to stay on the rod is that the ratio of these coordinates equals the slope of the rod in  $S$ . Therefore,  $a_y/a_x = \tan \theta$ , and the acceleration points along the rod.
- (c) The  $y$  component of the force on the bead is decreased by a factor  $\gamma$ , by Eq. (12.65). Therefore, since the force points at an angle  $\theta'$  in  $S'$  (because it points along the rod in  $S'$ ), the angle in  $S$  is given by  $\tan \phi = (1/\gamma) \tan \theta'$ , as shown in the figure.

![Figure 12.10: A diagram showing a rod in frame S' at an angle theta' to the x' axis. A bead is on the rod, and a force F' and acceleration a' are shown pointing along the rod. Frame S is moving to the left with velocity v relative to S'.](ebef17416f7b072d10a1692987ad66a4_img.jpg)

Figure 12.10: A diagram showing a rod in frame S' at an angle theta' to the x' axis. A bead is on the rod, and a force F' and acceleration a' are shown pointing along the rod. Frame S is moving to the left with velocity v relative to S'.

Fig. 12.10

![Figure 12.11: A diagram showing the rod in frame S. The rod is at an angle theta to the x axis. The force F and acceleration a are shown. The angle phi is between the force F and the vertical. The equation tan phi = (1/gamma) tan theta' is shown. The equation tan theta = gamma tan theta' is also shown.](daffb4875715900e02223fbc6b612213_img.jpg)

Figure 12.11: A diagram showing the rod in frame S. The rod is at an angle theta to the x axis. The force F and acceleration a are shown. The angle phi is between the force F and the vertical. The equation tan phi = (1/gamma) tan theta' is shown. The equation tan theta = gamma tan theta' is also shown.

Fig. 12.11

As a double-check that  $\mathbf{a}$  does indeed point along the rod, we can use Eq. (12.60) to write  $a_y/a_x = \gamma^2 F_y/F_x$ . Then Eq. (12.65) gives  $a_y/a_x = \gamma F'_y/F'_x = \gamma \tan \theta' = \tan \theta$ , which is the direction of the wire.

The wire does *not* exert a force of constraint. The bead doesn't need to touch the wire in  $S'$ , so it doesn't need to touch it in  $S$ . There is no need to have an extra force to combine with  $\mathbf{F}$  to make the result point along  $\mathbf{a}$ , because  $\mathbf{F}$  simply doesn't have to be collinear with  $\mathbf{a}$ .

## 12.6 Rocket motion

Up to this point, we have dealt with situations where the masses of our particles are constant, or where they change abruptly (as in a decay, where the sum of the masses of the products is less than the mass of the initial particle). But in many setups, the mass of an object changes continuously. A rocket is the classic example of this, so we'll use the term “rocket motion” to describe the general class of problems where the mass changes continuously.

The relativistic rocket itself encompasses all of the important ideas, so we'll study that example here. Many more examples are left for the problems. We'll present three solutions to the rocket problem, the last of which is rather slick. In the end, the solutions are all basically the same, but it should be helpful to see the various ways of looking at things.

**Example (Relativistic rocket):** Assume that a rocket propels itself by continually converting mass into photons and firing them out the back. Let  $m$  be the instantaneous mass of the rocket, and let  $v$  be the instantaneous speed with respect to the ground. Show that

$$\frac{dm}{m} + \frac{dv}{1-v^2} = 0. \quad (12.66)$$

If the initial mass is  $M$ , and the initial  $v$  is zero, integrate Eq. (12.66) to obtain

$$m = M \sqrt{\frac{1-v}{1+v}}. \quad (12.67)$$

**First solution:** The strategy of this solution will be to use conservation of momentum in the ground frame. Consider the effect of a small mass being converted into photons. The mass of the rocket goes from  $m$  to  $m + dm$  (where  $dm$  is negative). So in the frame of the rocket, photons with total energy  $E_r = -dm$  (which is positive) are fired out the back. In the frame of the rocket, these photons have momentum  $p_r = dm$  (which is negative). We'll drop the  $c$ 's here.

Let the rocket move at speed  $v$  with respect to the ground. Then the momentum of the photons in the ground frame,  $p_g$ , can be found via the Lorentz transformation,

$$p_g = \gamma(p_r + vE_r) = \gamma(dm + v(-dm)) = \gamma(1-v) dm. \quad (12.68)$$

This is still negative, of course.

REMARK: A common error is to say that the converted mass ( $-dm$ ) takes the form of photons of energy ( $-dm$ ) in the ground frame. This is incorrect, because although the photons have energy ( $-dm$ ) in the rocket frame, they are redshifted (due to the Doppler effect) in the ground frame. From Eq. (11.51), we see that the frequency (and hence the energy) of the photons decreases by a factor of  $\sqrt{(1-v)/(1+v)}$  when going from the rocket frame to the ground frame. This factor equals the  $\gamma(1-v)$  factor in Eq. (12.68). ♣

We can now use conservation of momentum in the ground frame to say that

$$(m\gamma v)_{\text{old}} = \gamma(1-v) dm + (m\gamma v)_{\text{new}} \implies \gamma(1-v) dm + d(m\gamma v) = 0. \quad (12.69)$$

The  $d(m\gamma v)$  term may be expanded to give

$$\begin{aligned} d(m\gamma v) &= (dm)\gamma v + m(d\gamma)v + m\gamma(dv) \\ &= \gamma v dm + m(\gamma^3 v dv)v + m\gamma dv \\ &= \gamma v dm + m\gamma(\gamma^2 v^2 + 1) dv \\ &= \gamma v dm + m\gamma^3 dv. \end{aligned} \quad (12.70)$$

Therefore, Eq. (12.69) gives

$$\begin{aligned} 0 &= \gamma(1-v) dm + \gamma v dm + m\gamma^3 dv \\ &= \gamma dm + m\gamma^3 dv. \end{aligned} \quad (12.71)$$

Hence,

$$\frac{dm}{m} + \frac{dv}{1-v^2} = 0, \quad (12.72)$$

in agreement with Eq. (12.66). We must now integrate this. With the given initial values, we have

$$\int_M^m \frac{dm}{m} + \int_0^v \frac{dv}{1-v^2} = 0. \quad (12.73)$$

We can look up the  $dv$  integral in a table, but let's instead do it from scratch.<sup>12</sup> Writing  $1/(1-v^2)$  as the sum of two fractions gives

$$\begin{aligned} \int_0^v \frac{dv}{1-v^2} &= \frac{1}{2} \int_0^v \left( \frac{1}{1+v} + \frac{1}{1-v} \right) dv \\ &= \frac{1}{2} \left( \ln(1+v) - \ln(1-v) \right) \Big|_0^v \\ &= \frac{1}{2} \ln \left( \frac{1+v}{1-v} \right). \end{aligned} \quad (12.74)$$

<sup>12</sup> Tables often list the integral of  $1/(1-v^2)$  as  $\tanh^{-1}(v)$ . You can show that this is equivalent to the result in Eq. (12.74).

Equation (12.73) therefore gives

$$\ln\left(\frac{m}{M}\right) = -\frac{1}{2} \ln\left(\frac{1+v}{1-v}\right) \implies m = M\sqrt{\frac{1-v}{1+v}}, \quad (12.75)$$

in agreement with Eq. (12.67). This result is independent of the rate at which the mass is converted into photons. It is also independent of the frequency of the emitted photons. Only the total mass expelled matters. Note that Eq. (12.75) quickly tells us that the energy of the rocket, as a function of velocity, is

$$E = \gamma m = \gamma M\sqrt{\frac{1-v}{1+v}} = \frac{M}{1+v}. \quad (12.76)$$

This has the interesting property of approaching  $M/2$  as  $v \rightarrow c$ . In other words, half of the initial energy remains with the rocket, and half ends up as photons (see Exercise 12.38).

**REMARK:** From Eq. (12.68), or from the previous remark, we see that the ratio of the energy of the photons in the ground frame to that in the rocket frame is  $\sqrt{(1-v)/(1+v)}$ . This factor is the same as the factor in Eq. (12.75). In other words, the photons' energy in the ground frame decreases in exactly the same manner as the mass of the rocket (assuming that the photons are ejected with the same frequency in the rocket frame throughout the process). Therefore, in the ground frame, the ratio of the photons' energy to the mass of the rocket doesn't change with time. There must be a nice intuitive explanation for this, but it eludes me. ♣

**Second solution:** The strategy of this solution will be to use  $F = dp/dt$  in the ground frame. Let  $\tau$  denote the time in the rocket frame. Then in the rocket frame,  $dm/d\tau$  is the rate at which the mass of the rocket decreases and is converted into photons ( $dm$  is negative). The photons therefore acquire momentum at the rate  $dp/d\tau = dm/d\tau$  in the rocket frame. Since force is the rate of change in momentum, we see that a force of  $dm/d\tau$  pushes the photons backward, and so an equal and opposite force of  $F = -dm/d\tau$  pushes the rocket forward in the rocket frame.

Now go to the ground frame. We know from Eq. (12.65) that the longitudinal force is the same in both frames, so  $F = -dm/d\tau$  is also the force on the rocket in the ground frame. And since  $dt = \gamma d\tau$ , where  $t$  is the time on the ground (the photon emissions occur at the same place in the rocket frame, so we have indeed put the time-dilation factor of  $\gamma$  in the right place), we have

$$F = -\gamma \frac{dm}{dt}. \quad (12.77)$$

**REMARK:** We can also calculate the force on the rocket by working entirely in the ground frame. Consider a mass ( $-dm$ ) that is converted into photons. Initially, this mass is traveling along with the rocket, so it has momentum  $(-dm)\gamma v$ . After it is converted into photons, it has momentum  $\gamma(1-v)dm$  (from the first solution above). The change in momentum is therefore  $\gamma(1-v)dm - (-dm)\gamma v = \gamma dm$ . Since force is the rate of change in momentum, a force of  $\gamma dm/dt$  pushes the photons backward, and so an equal and opposite force of  $F = -\gamma dm/dt$  pushes the rocket forward. ♣

Now things get a little tricky. It is tempting to write down  $F = dp/dt = d(m\gamma v)/dt$ , which gives  $F = (dm/dt)\gamma v + m d(\gamma v)/dt$ . This, however, is incorrect, because the

$dm/dt$  term isn't relevant here. When the force is applied to the rocket at an instant when the rocket has mass  $m$ , the only thing the force cares about is that the mass of the rocket at the given instant is  $m$ . It doesn't care that  $m$  is changing.<sup>13</sup> Therefore, the correct expression we want is

$$F = m \frac{d(\gamma v)}{dt}. \quad (12.78)$$

As in the first solution above, or in Eq. (12.54), we have  $d(\gamma v)/dt = \gamma^3 dv/dt$ . Using the  $F$  from Eq. (12.77), we arrive at

$$-\gamma \frac{dm}{dt} = m\gamma^3 \frac{dv}{dt}, \quad (12.79)$$

which is equivalent to Eq. (12.71). The solution proceeds as above.

**Third solution:** The strategy of this solution will be to use conservation of energy and momentum in the ground frame, in a slick way. Consider a clump of photons fired out the back. The energy and momentum of these photons are equal in magnitude and opposite in sign (with the convention that the photons are fired in the negative direction). By conservation of energy and momentum, the same statement must be true about the changes in energy and momentum of the rocket. That is,

$$d(\gamma m) = -d(\gamma m v) \implies d(\gamma m + \gamma m v) = 0. \quad (12.80)$$

Therefore,  $\gamma m(1 + v)$  is a constant. We are given that  $m = M$  when  $v = 0$ . Hence, the constant equals  $M$ . Therefore,

$$\gamma m(1 + v) = M \implies m = M \sqrt{\frac{1 - v}{1 + v}}. \quad (12.81)$$

Now, *that's* a quick solution, if there ever was one!

## 12.7 Relativistic strings

Consider a “massless” string with a tension that is constant, that is, independent of length.<sup>14</sup> We call such objects *relativistic strings*, and we will study them for two reasons. First, these strings, or reasonable approximations thereof, actually do occur in nature. For example, the gluon force which holds quarks together is approximately constant over distance. And second, they open the door to a whole new class of setups we can study, such as the two below. Relativistic strings might

<sup>13</sup> Said in a different way, the momentum associated with the ejected mass still exists. It's just that it's not part of the rocket anymore; it's in the photons. This issue is expanded on in Appendix C.

<sup>14</sup> By “massless,” we mean that the string has no mass in its unstretched (that is, zero-length) state. Once it is stretched, it will have energy in its rest frame, and hence mass.

seem a bit strange, but any one-dimensional problem involving them basically comes down to the two equations,

$$F = \frac{dp}{dt}, \quad \text{and} \quad F = \frac{dE}{dx}. \quad (12.82)$$

![Diagram for Fig. 12.12: A mass m is shown as a black dot moving with velocity v to the right, away from a vertical wall represented by a thick grey line.](237212d35a0761d060b613b3438e0048_img.jpg)

Diagram for Fig. 12.12: A mass m is shown as a black dot moving with velocity v to the right, away from a vertical wall represented by a thick grey line.

Fig. 12.12

**Example (Mass connected to a wall):** A mass  $m$  is connected to a wall by a relativistic string with tension  $T$ . The mass starts next to the wall and has an initial speed  $v$  away from it (see Fig. 12.12). How far from the wall does the mass get? How much time does it take to reach this point?

**Solution:** Let  $\ell$  be the maximum distance from the wall. The initial energy of the mass is  $E = \gamma m$ . The final energy at  $x = \ell$  is simply  $m$ , because the mass is instantaneously at rest there. Integrating  $F = dE/dx$ , and using the fact that the force always equals  $-T$ , gives

$$F\Delta x = \Delta E \implies (-T)\ell = m - \gamma m \implies \ell = \frac{m(\gamma - 1)}{T}. \quad (12.83)$$

Let  $t$  be the time it takes to reach this point. The initial momentum of the mass is  $p = \gamma mv$ . Integrating  $F = dp/dt$ , and using the fact that the force always equals  $-T$ , gives

$$F\Delta t = \Delta p \implies (-T)t = 0 - \gamma mv \implies t = \frac{\gamma mv}{T}. \quad (12.84)$$

Note that we *cannot* use  $F = ma$  to do this problem.  $F$  does not equal  $ma$ . It equals  $dp/dt$  (and also  $dE/dx$ ).

![Diagram for Fig. 12.13: Two masses, m and M, are connected by a dashed line representing a string of length l and tension T. The masses are shown as black dots.](cf1b69520c30078fb13c36227936d9f2_img.jpg)

Diagram for Fig. 12.13: Two masses, m and M, are connected by a dashed line representing a string of length l and tension T. The masses are shown as black dots.

Fig. 12.13

**Example (Where the masses meet):** A relativistic string of length  $\ell$  and tension  $T$  connects a mass  $m$  and a mass  $M$  (see Fig. 12.13). The masses are released from rest. Where do they meet?

**Solution:** Let the masses meet at a distance  $x$  from the initial position of  $m$ . At this meeting point,  $F = dE/dx$  tells us that the energy of  $m$  is  $m + Tx$ , and the energy of  $M$  is  $M + T(\ell - x)$ . Using  $p = \sqrt{E^2 - m^2}$  we see that the magnitudes of the momenta at the meeting point are

$$p_m = \sqrt{(m + Tx)^2 - m^2} \quad \text{and} \quad p_M = \sqrt{(M + T(\ell - x))^2 - M^2}. \quad (12.85)$$

But  $F = dp/dt$  tells us that these must be equal, because the same force (in magnitude, but opposite in direction) acts on the two masses for the same time. Equating the above  $p$ 's yields

$$x = \frac{\ell(M + T(\ell/2))}{M + m + T\ell}. \quad (12.86)$$

This result is reassuring, because it is the location of the initial center of mass, with the string being treated (quite correctly) like a stick of length  $\ell$  and mass  $T\ell$  (divided by  $c^2$ ).

REMARK: Let's check a few limits. In the limit of large  $T$  or  $\ell$  (more precisely, in the limit  $T\ell \gg Mc^2$  and  $T\ell \gg mc^2$ ), we have  $x = \ell/2$ . This makes sense, because in this case the masses are negligible and therefore both move at essentially speed  $c$ , and hence meet in the middle. In the limit of small  $T$  or  $\ell$  (more precisely, in the limit  $T\ell \ll Mc^2$  and  $T\ell \ll mc^2$ ), we have  $x = M\ell/(M + m)$ , which is simply the Newtonian result for an everyday-strength massless spring. ♣

## 12.8 Problems

## Section 12.1: Energy and momentum

### 12.1. Deriving $E$ and $p$ \*\*

Accepting the facts that the energy and momentum of a photon are  $E = h\nu$  and  $p = h\nu/c$  (where  $\nu$  is the frequency of the light wave, and  $h$  is Planck's constant), derive the relativistic formulas for the energy and momentum of a massive particle,  $E = \gamma mc^2$  and  $p = \gamma mv$ . *Hint:* Consider a mass  $m$  that decays into two photons. Look at this decay in the rest frame of the mass, and then in a frame where the mass has speed  $v$ . You'll need to use the Doppler effect.

### Section 12.3: Collisions and decays

### 12.2. Colliding photons \*

Two photons each have energy  $E$ . They collide at an angle  $\theta$  and create a particle of mass  $M$ . What is  $M$ ?

### 12.3. Increase in mass \*

A large mass  $M$ , moving at speed  $V$ , collides and sticks to a small mass  $m$ , initially at rest. What is the mass of the resulting object? Work in the approximation where  $M \gg m$ .

### 12.4. Two-body decay \*

A stationary mass  $M_A$  decays into masses  $M_B$  and  $M_C$ . What are the energies of  $M_B$  and  $M_C$ ? What are their momenta?

### 12.5. Threshold energy \*\*

A particle of mass  $m$  and energy  $E$  collides with an identical stationary particle. What is the threshold energy for a final state containing  $N$  particles of mass  $m$ ? ("Threshold energy" is the minimum energy for which the process can occur.)

### **12.6. Head-on collision \*\***

A ball of mass  $M$  and energy  $E$  collides head-on elastically with a stationary ball of mass  $m$ . Show that the final energy of mass  $M$  is

$$E' = \frac{2mM^2 + E(m^2 + M^2)}{2Em + m^2 + M^2}. \quad (12.87)$$

*Hint:* This problem is a little messy, but you can save yourself a lot of trouble by noting that  $E' = E$  must be a root of the equation you get for  $E'$ . (Why?) As a reward for trudging through the mess, there are lots of interesting limits you can take.

![Diagram of Compton scattering. An incident photon with wavelength λ moves horizontally to the right. An electron with mass m is initially at rest, indicated by a downward arrow. After the collision, the photon is scattered at an angle θ with wavelength λ', and the electron recoils with mass m at an angle below the horizontal.](aecebcea7146898323f025f3a014bd67_img.jpg)

Diagram of Compton scattering. An incident photon with wavelength λ moves horizontally to the right. An electron with mass m is initially at rest, indicated by a downward arrow. After the collision, the photon is scattered at an angle θ with wavelength λ', and the electron recoils with mass m at an angle below the horizontal.

### **12.7. Compton scattering \*\***

A photon collides with a stationary electron. If the photon scatters at an angle  $\theta$  (see Fig. 12.14), show that the resulting wavelength,  $\lambda'$ , is given in terms of the original wavelength,  $\lambda$ , by

$$\lambda' = \lambda + \frac{h}{mc}(1 - \cos \theta), \quad (12.88)$$

where  $m$  is the mass of the electron. *Note:* The energy of a photon is  $E = h\nu = hc/\lambda$ .

Fig. 12.14

### *Section 12.5: Force*

### **12.8. System of masses \*\***

Consider a dumbbell made of two equal masses,  $m$ . The dumbbell spins around, with its center pivoted at the end of a stick (see Fig. 12.15). If the speed of the masses is  $v$ , then the energy of the system is  $2\gamma m$ . Treated as a whole, the system is at rest. Therefore, the mass of the system must be  $2\gamma m$ . (Imagine enclosing it in a box, so that you can't see what's going on inside.) Convince yourself that the system does indeed behave like a mass of  $M = 2\gamma m$ , by pushing on the stick (when the dumbbell is in the “transverse” position shown in the figure) and showing that  $F \equiv dp/dt = Ma$ .

![Diagram of a dumbbell system. Two masses m are connected by a vertical rod. The center of the rod is pivoted to a horizontal stick. The masses are moving with velocity v in opposite directions, perpendicular to the rod. The entire system is enclosed in a dashed rectangular box.](a527c41266d40cf7f3df7996bf1581db_img.jpg)

Diagram of a dumbbell system. Two masses m are connected by a vertical rod. The center of the rod is pivoted to a horizontal stick. The masses are moving with velocity v in opposite directions, perpendicular to the rod. The entire system is enclosed in a dashed rectangular box.

Fig. 12.15

### **12.9. Relativistic harmonic oscillator \*\***

A particle of mass  $m$  moves along the  $x$  axis under a force  $F = -m\omega^2 x$ . The amplitude is  $b$ . Show that the period is given by

$$T = \frac{4}{c} \int_0^b \frac{\gamma}{\sqrt{\gamma^2 - 1}} dx, \quad \text{where} \quad \gamma = 1 + \frac{\omega^2}{2c^2}(b^2 - x^2). \quad (12.89)$$

### *Section 12.6: Rocket motion*

### **12.10. Relativistic rocket \*\***

Consider the relativistic rocket in Section 12.6. Let mass be converted into photons at a rate  $\sigma$  in the rest frame of the rocket. Find the time  $t$  in the ground frame as a function of  $v$ . (Alas, it isn't possible to invert this, to obtain  $v$  as a function of  $t$ .) You'll need to evaluate a slightly tricky integral. Pick your favorite method – pencil, book, or computer.

### **12.11. Relativistic dustpan I \***

A dustpan of mass  $M$  is given an initial relativistic speed. It gathers up dust with mass density  $\lambda$  per unit length on the floor (as measured in the lab frame). At the instant the speed is  $v$ , find the rate (as measured in the lab frame) at which the mass of the dustpan-plus-dust-inside system is increasing.

### **12.12. Relativistic dustpan II \*\***

Consider the setup in Problem 12.11. If the initial speed of the dustpan is  $V$ , find  $v(x)$ ,  $v(t)$ , and  $x(t)$ . All quantities here are measured with respect to the lab frame.

### **12.13. Relativistic dustpan III \*\***

Consider the setup in Problem 12.11. Calculate, in both the dustpan frame and the lab frame, the force on the dustpan-plus-dust-inside system (due to the newly acquired dust particles smashing into it) as a function of  $v$ , and show that the results are equal.

### **12.14. Relativistic cart I \*\*\*\***

A long cart moves at relativistic speed  $v$ . Sand is dropped into the cart at a rate  $dm/dt = \sigma$  in the ground frame. Assume that you stand on the ground next to where the sand falls in, and you push on the cart to keep it moving at constant speed  $v$ . What is the force between your feet and the ground? Calculate this force in both the ground frame (your frame) and the cart frame, and show that the results are equal.

### **12.15. Relativistic cart II \*\*\*\***

A long cart moves at relativistic speed  $v$ . Sand is dropped into the cart at a rate  $dm/dt = \sigma$  in the ground frame. Assume that you grab the front of the cart and pull on it to keep it moving at constant speed  $v$  (while running with it). What force does your hand apply to the cart? (Assume that the cart is made of the most rigid material possible.) Calculate this force in both the ground frame and the cart frame (your frame), and show that the results are equal.

### Section 12.7: Relativistic strings

### 12.16. Different frames \*\*

![Diagram for problem 12.16: Two masses m are connected by a string of length l and constant tension T. A frame moving to the left at speed v is shown below the string.](d4237b9982d93a94385df7c55211c70f_img.jpg)

The diagram shows two black dots representing masses  $m$  connected by a horizontal line representing a string of length  $l$ . The tension  $T$  is indicated below the string. Below the string, a stick figure is shown moving to the left with velocity  $v$ .

Diagram for problem 12.16: Two masses m are connected by a string of length l and constant tension T. A frame moving to the left at speed v is shown below the string.

Fig. 12.16

- (a) Two masses  $m$  are connected by a string of length  $\ell$  and constant tension  $T$ . The masses are released simultaneously, and they collide and stick together. What is the mass,  $M$ , of the resulting blob?
- (b) Consider this scenario from the point of view of a frame moving to the left at speed  $v$  (see Fig. 12.16). The energy of the resulting blob must be  $\gamma Mc^2$ , from part (a). Show that you obtain this same result by computing the work done on the two masses.

### 12.17. Splitting mass \*\*

![Diagram for problem 12.17: A massless string with constant tension T has one end attached to a wall and the other end attached to a mass M. The initial length of the string is l.](08eefe27b1ae5e803c6072290f7076ba_img.jpg)

The diagram shows a vertical wall on the left connected to a horizontal string of length  $l$  with tension  $T$ . The string is attached to a mass  $M$  on the right.

Diagram for problem 12.17: A massless string with constant tension T has one end attached to a wall and the other end attached to a mass M. The initial length of the string is l.

Fig. 12.17

A massless string with constant tension  $T$  has one end attached to a wall and the other end attached to a mass  $M$ . The initial length of the string is  $\ell$  (see Fig. 12.17). The mass is released. Halfway to the wall, the back half of the mass breaks away from the front half (with zero initial relative speed). What is the total time it takes the front half to reach the wall?

### 12.18. Relativistic leaky bucket \*\*\*

![Diagram for problem 12.18: A massless bucket containing an initial mass M of sand is attached to a wall by a string of length l and tension T.](559863f057d83527dc022f42d1d987fe_img.jpg)

The diagram shows a vertical wall on the left connected to a horizontal string of length  $l$  with tension  $T$ . The string is attached to a bucket containing mass  $M$  on the right.

Diagram for problem 12.18: A massless bucket containing an initial mass M of sand is attached to a wall by a string of length l and tension T.

Fig. 12.18

Let the mass  $M$  in Problem 12.17 be replaced by a massless bucket containing an initial mass  $M$  of sand (see Fig. 12.18). On the way to the wall, the bucket leaks sand at a rate  $dm/dx = M/\ell$ , where  $m$  denotes the mass at later positions. Note that  $dm$  and  $dx$  are both negative here.

- (a) What is the energy of the bucket, as a function of distance from the wall? What is its maximum value? What is the maximum value of the kinetic energy?
- (b) What is the momentum of the bucket, as a function of distance from the wall? Where is it maximum?

![Diagram for problem 12.19: A massless string with constant tension T has one end attached to a wall and the other end attached to a mass m. The initial length of the string is l.](c8eb0f2a55516ad5a8f89902aa193e5a_img.jpg)

The diagram shows a vertical wall on the left connected to a horizontal string of length  $l$  with tension  $T$ . The string is attached to a mass  $m$  on the right.

Diagram for problem 12.19: A massless string with constant tension T has one end attached to a wall and the other end attached to a mass m. The initial length of the string is l.

Fig. 12.19

### 12.19. Relativistic bucket \*\*\*

- (a) A massless string with constant tension  $T$  has one end attached to a wall and the other end attached to a mass  $m$ . The initial length of the string is  $\ell$  (see Fig. 12.19). The mass is released. How long does it take to reach the wall?
- (b) Let the string now have length  $2\ell$ , with a mass  $m$  on the end. Let another mass  $m$  be positioned next to the  $\ell$  mark on the string, but not touching it (see Fig. 12.20). The right mass is released. It heads toward the wall (while the left mass remains motionless) and then sticks to the left mass to make one large

![Diagram for problem 12.20: A massless string of length 2l is attached to a wall. A mass m is at the l mark, and another mass m is at the 2l mark.](1e66225021f23f1ae009f9f743c3f683_img.jpg)

The diagram shows a vertical wall on the left connected to a horizontal string of total length  $2l$  with tension  $T$ . A mass  $m$  is positioned at the  $l$  mark, and another mass  $m$  is at the end of the string ( $2l$  mark).

Diagram for problem 12.20: A massless string of length 2l is attached to a wall. A mass m is at the l mark, and another mass m is at the 2l mark.

Fig. 12.20

blob, which then heads toward the wall.<sup>15</sup> How much time does this whole process take? *Hint:* You can solve this in various ways, but one method that generalizes nicely for part (c) is to show that the change in  $p^2$  from the start to a point right before the wall is  $\Delta(p^2) = (E_2^2 - E_1^2) + (E_4^2 - E_3^2)$ , where the energies of the moving object (that is, the initial  $m$  or the resulting blob) are:  $E_1$  right at the start,  $E_2$  just before the collision,  $E_3$  just after the collision, and  $E_4$  right before the wall. Note that this method doesn't require knowledge of the mass of the blob (which is *not*  $2m$ ).

- (c) Let there now be  $N$  masses and a string of length  $N\ell$  (see Fig. 12.21). How much time does this whole process take?
- (d) Consider now a massless bucket at the end of the string (of length  $L$ ) that gathers up a continuous stream of sand (of total mass  $M$ ) as it gets pulled to the wall (see Fig. 12.22). How much time does this whole process take? What are the mass and speed of the bucket right before it hits the wall?

![Diagram for Fig. 12.21: A vertical wall on the left is connected to a horizontal string. Along the string are five dots representing masses. The distance between the first two dots is labeled 'l'. The tension in the string is labeled 'T'. The rightmost mass is labeled 'm'. Above the string, it says '(N=5)'.](a791c9daf45325f902465707e0121a9a_img.jpg)

Diagram for Fig. 12.21: A vertical wall on the left is connected to a horizontal string. Along the string are five dots representing masses. The distance between the first two dots is labeled 'l'. The tension in the string is labeled 'T'. The rightmost mass is labeled 'm'. Above the string, it says '(N=5)'.

Fig. 12.21

![Diagram for Fig. 12.22: A vertical wall on the left is connected to a horizontal string. The string has a length 'L' and a tension 'T'. At the right end of the string is a bucket, represented by a semi-circle. Above the string, the total mass of the sand in the bucket is labeled 'M'.](5ed9095afbc9aef73d90b33dc5334949_img.jpg)

Diagram for Fig. 12.22: A vertical wall on the left is connected to a horizontal string. The string has a length 'L' and a tension 'T'. At the right end of the string is a bucket, represented by a semi-circle. Above the string, the total mass of the sand in the bucket is labeled 'M'.

Fig. 12.22

### 12.9 Exercises

### Section 12.2: Transformations of $E$ and $p$

### 12.20. Energy of two masses \*

Two masses  $M$  move at speed  $V$ , one to the east and one to the west. What is the total energy of the system? Now consider the setup as viewed in a frame moving to the west at speed  $u$ . Find the energy of each mass in this frame. Is the total energy larger or smaller than the total energy in the lab frame?

### 12.21. System of particles \*

Given  $p_{\text{total}}$  and  $E_{\text{total}}$  for a system of particles, use a Lorentz transformation to find the velocity of the CM. More precisely, find the speed of the frame in which the total momentum is zero.

### 12.22. CM frame \*\*

A mass  $m$  travels at speed  $3c/5$ , and another mass  $m$  sits at rest.

- (a) Find the energy and momentum of the two particles in the lab frame.
- (b) Find the speed of the CM of the system, by using a velocity-addition argument.

<sup>15</sup> The left mass could actually be attached to the string, and we would still have the same situation. The mass wouldn't move during the first part of the process, because there would be equal tensions  $T$  on both sides of it.

- (c) Find the energy and momentum of the two particles in the CM frame, without using the Lorentz transformations.
- (d) Verify that the  $E$ 's and  $p$ 's are related by the relevant Lorentz transformations.
- (e) Verify that  $E^2 - p^2c^2$  for each mass is the same in both frames. Likewise for  $E_{\text{total}}^2 - p_{\text{total}}^2c^2$ .

### 12.23. Transformations for 2-D motion \*\*

A particle has velocity  $(u'_x, u'_y)$  in frame  $S'$ , which travels at speed  $v$  in the  $x$  direction relative to frame  $S$ . Use the velocity-addition formulas in Section 11.5.2 (Eqs. (11.36) and (11.38)) to show that

$$\gamma_u = \gamma_{u'}\gamma_v(1 + u'_x v), \quad \text{where } u = \sqrt{u_x^2 + u_y^2} \text{ and } u' = \sqrt{u'^2_x + u'^2_y} \quad (12.90)$$

are the speeds in the two frames. Then verify that  $E$  and  $p_x$  transform according to Eqs. (12.27), and also that  $p_y = p'_y$ .

## Section 12.3: Collisions and decays

### 12.24. Photon and mass collision \*

A photon with energy  $E$  collides with a stationary mass  $m$ . They combine to form one particle. What is the mass of this particle? What is its speed?

![Diagram for problem 12.23: A particle of mass m moves with velocity v to the right. It collides with a stationary particle. The resulting single particle moves at an angle of 120 degrees above the horizontal. Two other dashed lines are shown at 120 degrees below the horizontal, indicating a symmetric decay or collision geometry.](f75a7b9723041b70bd48192191b184c8_img.jpg)

Diagram for problem 12.23: A particle of mass m moves with velocity v to the right. It collides with a stationary particle. The resulting single particle moves at an angle of 120 degrees above the horizontal. Two other dashed lines are shown at 120 degrees below the horizontal, indicating a symmetric decay or collision geometry.

Fig. 12.23

### 12.25. A decay \*

A stationary mass  $M$  decays into a particle and a photon. If the speed of the particle is  $v$ , what is its mass? What is the energy of the photon?

### 12.26. Three photons \*

A mass  $m$  moves at speed  $v$ . It decays into three photons, one of which travels in the forward direction, and the other two of which move at angles of  $120^\circ$  (in the lab frame) as shown in Fig. 12.23. What are the energies of these three photons?

![Diagram for problem 12.24: A photon with energy E moves to the right towards a stationary mass M. Below this, a second diagram shows the mass M after the collision, moving at an angle below the horizontal. A dashed line indicates the original direction of the photon. A wavy arrow points vertically upwards from the collision point, representing the scattered photon.](26987f309b3fed9971b6b661cbc35625_img.jpg)

Diagram for problem 12.24: A photon with energy E moves to the right towards a stationary mass M. Below this, a second diagram shows the mass M after the collision, moving at an angle below the horizontal. A dashed line indicates the original direction of the photon. A wavy arrow points vertically upwards from the collision point, representing the scattered photon.

Fig. 12.24

### 12.27. Perpendicular photon \*

A photon with energy  $E$  collides with a mass  $M$ . The mass  $M$  scatters at an angle. If the resulting photon moves perpendicular to the incident photon's direction, as shown in Fig. 12.24, what is its energy?

### 12.28. Another perpendicular photon \*

A mass  $m$  moving at speed  $4c/5$  collides with another mass  $m$  at rest. The collision produces a photon with energy  $E$  traveling perpendicular to the original direction, and a mass  $M$  traveling in another direction,

as shown in Fig. 12.25. In terms of  $E$  and  $m$ , what is  $M$ ? What is the largest value of  $E$  (in terms of  $m$ ) for which this setup is possible?

### **12.29. Decay into photons \***

A mass  $m$  moving at speed  $v$  decays into two photons. One photon moves perpendicular to the original direction, and the other photon moves off at an angle  $\theta$ , as shown in Fig. 12.26. Show that if  $\tan \theta = 1/2$ , then  $v/c = (\sqrt{5} - 1)/2$ , which just happens to be the inverse of the golden ratio.

### **12.30. Maximum mass \***

A photon and a mass  $m$  move directly toward each other. They collide head-on and create a new particle. If the total energy of the system is  $E$ , how should it be divided between the photon and the mass  $m$  so that the mass of the resulting particle is as large as possible?

### **12.31. Equal angles \***

A photon with energy  $E$  collides with a stationary mass  $m$ . If the mass  $m$  and the resulting photon (with unknown energy) scatter at equal angles  $\theta$  with respect to the initial photon direction, as shown in Fig. 12.27, what is  $\theta$  in terms of  $E$  and  $m$ ? What is  $\theta$  in the limit  $E \ll mc^2$ ?

## *Section 12.4: Particle-physics units*

### **12.32. Pion–muon race \***

A pion and a muon have a 100 m race. If they both have an energy of 10 GeV, by how much distance does the muon win?

### **12.33. Higgs production \***

The *Higgs boson* is a proposed elementary particle that should be experimentally detected in a few years, assuming it exists. One strategy for producing it in a high-energy particle accelerator is to collide protons and antiprotons together. Taking the rest energy of a proton (and antiproton) to be about 1 GeV, and assuming that the rest energy of the Higgs is about 100 GeV, how much energy is required to produce the Higgs if:

- A moving proton collides with a stationary antiproton?
- A proton and antiproton have equal and opposite momenta?

### **12.34. Maximum energy \*\***

- A particle of mass  $M$  decays into a number of particles, some of which may be photons. If one of the particles has mass  $m$ , and

![Diagram for Fig. 12.25: A particle of mass m moves to the right with velocity 4c/5. It decays into two photons, one moving vertically upwards with energy E, and another moving downwards and to the right to a particle of mass M. A dashed horizontal line indicates the original direction of motion.](d9d1f5681249a21d8b120ee0795f302e_img.jpg)

Diagram for Fig. 12.25: A particle of mass m moves to the right with velocity 4c/5. It decays into two photons, one moving vertically upwards with energy E, and another moving downwards and to the right to a particle of mass M. A dashed horizontal line indicates the original direction of motion.

Fig. 12.25

![Diagram for Fig. 12.26: A particle of mass m moves to the right with velocity v. It decays into two photons. One photon moves upwards and to the right at an angle theta from the horizontal dashed line. The other photon moves vertically downwards.](2441e3d4bbac6d15b095e0a1a9b8adba_img.jpg)

Diagram for Fig. 12.26: A particle of mass m moves to the right with velocity v. It decays into two photons. One photon moves upwards and to the right at an angle theta from the horizontal dashed line. The other photon moves vertically downwards.

Fig. 12.26

![Diagram for Fig. 12.27: A photon with energy E moves to the right and collides with a stationary particle of mass m. After the collision, the particle of mass m moves downwards and to the right at an angle theta from the horizontal dashed line. The resulting photon moves upwards and to the right at an angle theta from the horizontal dashed line.](837c36a1eda399490423994fc6001e83_img.jpg)

Diagram for Fig. 12.27: A photon with energy E moves to the right and collides with a stationary particle of mass m. After the collision, the particle of mass m moves downwards and to the right at an angle theta from the horizontal dashed line. The resulting photon moves upwards and to the right at an angle theta from the horizontal dashed line.

Fig. 12.27

if the sum of the masses of all the other products is  $\mu$ , what is the maximum possible energy that  $m$  can have? *Hint:* Write the conservation of energy and momentum statements as  $P_M - P_m = P_\mu$ , where  $P_\mu$  is the total 4-momentum of the other products, and then square. The technique of Problem 12.5 may be useful.

- (b) In beta decay, a neutron decays into a proton, an electron, and a neutrino (which is essentially a photon, for the present purposes). The rest energies are  $E_n = 939.6$  MeV,  $E_p = 938.3$  MeV,  $E_e = 0.5$  MeV, and  $E_\nu \approx 0$ . What is the maximum energy that the electron can have? The neutrino? Interpret your results.

## Section 12.5: Force

### 12.35. Force and a collision \*

Two identical masses  $m$  are initially at rest, a distance  $x$  apart. A constant force  $F$  accelerates one of them toward the other until they collide and stick together. What is the mass of the resulting particle?

### 12.36. Pushing on a mass \*\*

- (a) A mass  $m$  starts at rest. You push on it with a constant force  $F$ . How much time  $t$  does it take for the mass to move a distance  $x$ ? (Both  $t$  and  $x$  here are measured in the lab frame.)
- (b) After a very long time,  $m$ 's speed will approach  $c$ . It turns out that it approaches  $c$  sufficiently fast so that after a very long time,  $m$  will remain (approximately) a constant distance (as measured in the lab frame) behind a photon that was emitted at  $t = 0$  from the starting position of  $m$ . What is this distance?

![Diagram showing two equal masses connected by a massless string with tension T. The masses are moving with speed v along parallel lines. Dashed lines indicate the paths of the masses after the string is cut, showing they will move towards each other and collide.](08157ac7077f00d6c8bd67bb2c0f8678_img.jpg)

The diagram shows two masses, represented by black dots, connected by a vertical line labeled  $T$ . Both masses have a horizontal velocity  $v$  to the right, indicated by arrows above and below the dots. Two dashed lines extend from the masses to the right, curving slightly towards each other, representing their trajectories after the string is cut.

Diagram showing two equal masses connected by a massless string with tension T. The masses are moving with speed v along parallel lines. Dashed lines indicate the paths of the masses after the string is cut, showing they will move towards each other and collide.

Fig. 12.28

### 12.37. Momentum paradox \*\*\*\*

Two equal masses are connected by a massless string with tension  $T$ . The masses are constrained to move with speed  $v$  along parallel lines, as shown in Fig. 12.28. The constraints are then removed, and the masses are drawn together. They collide and make one blob which continues to move to the right. Is the following reasoning correct? If your answer is “no,” state what is invalid about whichever of the four sentences is/are invalid.

“The forces on the masses point in the  $y$  direction. Therefore, there is no change in the momentum of the masses in the  $x$  direction. But the mass of the resulting blob is greater than the sum of the initial masses (because they collide with some relative speed). Therefore, the speed of the resulting blob must be less than  $v$  (to keep  $p_x$  constant), so the whole apparatus slows down in the  $x$  direction.”

## Section 12.6: Rocket motion

### 12.38. **Rocket energy** \*\*

As mentioned near the end of the first solution to the rocket problem in Section 12.6, the energy of the rocket in the ground frame equals  $M/(1 + v)$ . Derive this result again, by integrating up the amount of energy that the photons have in the ground frame.

## Section 12.7: Relativistic strings

### 12.39. **Two masses** \*

A mass  $m$  is placed right in front of an identical one. They are connected by a relativistic string with tension  $T$ . The front mass suddenly acquires a speed  $3c/5$ . How far from the starting point will the masses collide with each other?

### 12.40. **Relativistic bucket** \*\*

One of the results in part (d) of Problem 12.19 is that the bucket moves toward the wall at constant speed  $\sqrt{T/(T + \rho)}$ . Derive this again, without using the technique of taking the  $N \rightarrow \infty$  limit of many masses.

## 12.10 Solutions

### 12.1. **Deriving $E$ and $p$**

Let's derive the energy formula,  $E = \gamma mc^2$ , first. Let the given mass decay into two photons, and let  $E_0$  be the energy of the mass in its rest frame. Then each of the resulting photons has energy  $E_0/2$  in this frame.

Now look at the decay in a frame where the mass moves at speed  $v$ . From Eq. (11.51), the frequencies of the photons are Doppler-shifted by the factors  $\sqrt{(1 + v)/(1 - v)}$  and  $\sqrt{(1 - v)/(1 + v)}$ . Since the energies of the photons are given by  $E = h\nu$ , they are shifted by the same Doppler factors, relative to the  $E_0/2$  value in the original frame. The total energy of the photons in the frame where the mass moves at speed  $v$  is therefore

$$E = \frac{E_0}{2} \sqrt{\frac{1 + v}{1 - v}} + \frac{E_0}{2} \sqrt{\frac{1 - v}{1 + v}} = \frac{E_0}{\sqrt{1 - v^2}} \equiv \gamma E_0. \quad (12.91)$$

By conservation of energy, this is the energy of the mass  $m$  moving at speed  $v$ . So we see that a moving mass has an energy that is  $\gamma$  times its rest energy.

We can now use the correspondence principle (which says that relativistic formulas must reduce to the familiar nonrelativistic ones in the nonrelativistic limit) to find  $E_0$  in terms of  $m$  and  $c$ . We just found that the difference between the energies of a moving mass and a stationary mass is  $\gamma E_0 - E_0$ . This must reduce to the familiar kinetic energy,  $mv^2/2$ , in the limit  $v \ll c$ . In other words,

$$\frac{mv^2}{2} \approx \frac{E_0}{\sqrt{1 - v^2/c^2}} - E_0 \approx E_0 \left( 1 + \frac{v^2}{2c^2} \right) - E_0 = \left( \frac{E_0}{c^2} \right) \frac{v^2}{2}, \quad (12.92)$$

where we have used the Taylor series,  $1/\sqrt{1 - \epsilon} \approx 1 + \epsilon/2$ . Therefore  $E_0 = mc^2$ , and so  $E = \gamma mc^2$ .

We can derive the momentum formula,  $p = \gamma mv$ , in a similar way. Let the magnitude of the photons' (equal and opposite) momenta in the particle's rest frame be  $p_0/2$ .<sup>16</sup> Since the photons' momenta are given by  $E = h\nu/c$ , we can use the Doppler-shifted frequencies as we did above to say that the total momentum of the photons in the frame where the mass moves at speed  $v$  is

$$p = \frac{p_0}{2} \sqrt{\frac{1+v}{1-v}} - \frac{p_0}{2} \sqrt{\frac{1-v}{1+v}} = \gamma p_0 v. \quad (12.93)$$

Putting the  $c$ 's back in, we have  $p = \gamma p_0 v/c$ . By conservation of momentum, this is the momentum of the mass  $m$  moving at speed  $v$ .

We can now use the correspondence principle to find  $p_0$  in terms of  $m$  and  $c$ . If  $p = \gamma(p_0/c)v$  is to reduce to the familiar  $p = mv$  result in the limit  $v \ll c$ , then we must have  $p_0 = mc$ . Therefore,  $p = \gamma mv$ .

### 12.2. Colliding photons

The 4-momenta of the photons are (see Fig. 12.29)

$$P_{\gamma_1} = (E, E, 0, 0), \quad \text{and} \quad P_{\gamma_2} = (E, E \cos \theta, E \sin \theta, 0). \quad (12.94)$$

Energy and momentum are conserved, so the 4-momentum of the final particle is  $P_M = (2E, E + E \cos \theta, E \sin \theta, 0)$ . Therefore,

$$M^2 = P_M \cdot P_M = (2E)^2 - (E + E \cos \theta)^2 - (E \sin \theta)^2, \quad (12.95)$$

which gives

$$M = E \sqrt{2(1 - \cos \theta)}. \quad (12.96)$$

If  $\theta = 180^\circ$  then  $M = 2E$ , as it should (none of the final energy is kinetic). And if  $\theta = 0^\circ$  then  $M = 0$ , as it should (all of the final energy is kinetic; we simply have a photon with twice the energy).

### 12.3. Increase in mass

In the lab frame, the energy of the resulting object is  $\gamma M + m$ , and the momentum is  $\gamma MV$ . The mass of the object is therefore

$$M' = \sqrt{(\gamma M + m)^2 - (\gamma MV)^2} = \sqrt{M^2 + 2\gamma Mm + m^2}. \quad (12.97)$$

The  $m^2$  term is negligible compared with the other two terms, so we may approximate  $M'$  as

$$M' \approx M \sqrt{1 + \frac{2\gamma m}{M}} \approx M \left( 1 + \frac{\gamma m}{M} \right) = M + \gamma m, \quad (12.98)$$

where we have used the Taylor series,  $\sqrt{1 + \epsilon} \approx 1 + \epsilon/2$ . Therefore, the increase in mass is  $\gamma$  times the mass of the stationary object. This increase is greater than the nonrelativistic answer of " $m$ ," because heat is generated during the collision, and this heat shows up as mass in the final object.

**REMARK:** The  $\gamma m$  result is clear if we work in the frame where  $M$  is initially at rest. In this frame, the mass  $m$  comes flying in with energy  $\gamma m$ , and then essentially all of this energy shows up as mass in the final object. That is, essentially none of it shows up as overall kinetic energy of the object. This negligible-kinetic-energy result is a general one whenever a small object hits a stationary large one. It follows from the fact that the speed of the large object is proportional to  $m/M$ , by momentum

<sup>16</sup> With the given information that a photon has  $E = h\nu$  and  $p = h\nu/c$ , we can use the preceding  $E_0 = mc^2$  result to quickly conclude that  $p_0 = mc$ . But let's pretend that we haven't found  $E_0$  yet. This will give us an excuse to use the correspondence principle again.

![Diagram showing two photons, labeled gamma_1 and gamma_2, colliding. Photon gamma_1 is moving horizontally to the right. Photon gamma_2 is moving at an angle theta below the horizontal. The angle theta is indicated between the horizontal direction and the path of gamma_2. A coordinate system with x and y axes is shown to the right of the collision point.](cd3196869de3ab2e83c479c3cf6977bc_img.jpg)

Diagram showing two photons, labeled gamma\_1 and gamma\_2, colliding. Photon gamma\_1 is moving horizontally to the right. Photon gamma\_2 is moving at an angle theta below the horizontal. The angle theta is indicated between the horizontal direction and the path of gamma\_2. A coordinate system with x and y axes is shown to the right of the collision point.

Fig. 12.29

conservation (there's a factor of  $\gamma$  if things are relativistic), so the kinetic energy goes like  $Mv^2 \propto M(m/M)^2 \approx 0$ , if  $M \gg m$ . In other words, the smallness of  $v$  wins out over the largeness of  $M$ . When a snowball hits a tree, all (essentially) of the initial energy goes into heat. None of it goes into changing the kinetic energy of the earth. ♣

### 12.4. Two-body decay

$B$  and  $C$  have equal and opposite momenta. Therefore,

$$E_B^2 - M_B^2 = p^2 = E_C^2 - M_C^2. \quad (12.99)$$

Also, conservation of energy gives

$$E_B + E_C = M_A. \quad (12.100)$$

Solving the two previous equations for  $E_B$  and  $E_C$  gives (using the shorthand  $a \equiv M_A$ , etc.)

$$E_B = \frac{a^2 + b^2 - c^2}{2a}, \quad \text{and} \quad E_C = \frac{a^2 + c^2 - b^2}{2a}. \quad (12.101)$$

Equation (12.99) then gives the momentum of the particles as

$$p = \frac{1}{2a} \sqrt{a^4 + b^4 + c^4 - 2a^2b^2 - 2a^2c^2 - 2b^2c^2}. \quad (12.102)$$

REMARK: It turns out that the quantity under the radical can be factored into

$$(a + b + c)(a + b - c)(a - b + c)(a - b - c). \quad (12.103)$$

This makes it clear that if  $a = b + c$ , then  $p = 0$ , because there is no leftover energy for the particles to be able to move. Interestingly, the form of  $p$  in Eq. (12.102) looks very much like the area of a triangle with sides  $a, b, c$ , which is given by Heron's formula as

$$A = \frac{1}{4} \sqrt{2a^2b^2 + 2a^2c^2 + 2b^2c^2 - a^4 - b^4 - c^4}. \quad \text{♣} \quad (12.104)$$

### 12.5. Threshold energy

The initial 4-momenta in the lab frame are

$$(E, p, 0, 0), \quad \text{and} \quad (m, 0, 0, 0), \quad (12.105)$$

where  $p = \sqrt{E^2 - m^2}$ . Therefore, the total 4-momentum of the final particles in the lab frame is  $(E + m, p, 0, 0)$ . The quantity  $E_{\text{total}}^2 - p_{\text{total}}^2$  is frame independent, and it equals the square of the energy in the CM frame (where  $p = 0$ ). So we have, with the subscript "f" for "final,"

$$\begin{aligned} (E + m)^2 - (\sqrt{E^2 - m^2})^2 &= (E_f^{\text{CM}})^2 \\ \implies 2Em + 2m^2 &= (E_f^{\text{CM}})^2. \end{aligned} \quad (12.106)$$

We see that minimizing  $E$  is equivalent to minimizing  $E_f^{\text{CM}}$ . But  $E_f^{\text{CM}}$  is clearly minimized when all the final particles are at rest in the CM frame, so that there is no kinetic energy added to the rest energy. So the energy in the CM frame at threshold is simply the sum of the rest energies. In other words,  $E_f^{\text{CM}} = Nm$ . We therefore have

$$2Em + 2m^2 = (Nm)^2 \implies E = \left( \frac{N^2}{2} - 1 \right) m. \quad (12.107)$$

Since there is no relative motion among the final particles in the CM frame at threshold there is also no relative motion in any other frame. This means that at threshold the  $N$  masses travel together as a blob in the lab frame. The threshold  $E$  is larger than the naive answer of  $(N-1)m$ , because the final state has inevitable “wasted” energy in the form of kinetic energy (which is necessitated by conservation of momentum) in the lab frame. Note that  $E \propto N^2$  for large  $N$ .

### 12.6. Head-on collision

The 4-momenta before the collision are

$$P_M = (E, p, 0, 0), \quad P_m = (m, 0, 0, 0), \quad (12.108)$$

where  $p = \sqrt{E^2 - M^2}$ . The 4-momenta after the collision are

$$P'_M = (E', p', 0, 0), \quad P'_m = (\text{we won't need this}), \quad (12.109)$$

where  $p' = \sqrt{E'^2 - M^2}$ . Conservation of energy and momentum give  $P_M + P_m = P'_M + P'_m$ . Therefore,

$$\begin{aligned} P_m'^2 &= (P_M + P_m - P'_M)^2 & (12.110) \\ \implies P_m'^2 &= P_M^2 + P_m^2 + P_M'^2 + 2P_m \cdot (P_M - P'_M) - 2P_M \cdot P'_M \\ \implies m^2 &= M^2 + m^2 + M^2 + 2m(E - E') - 2(EE' - pp') \\ \implies -pp' &= M^2 - EE' + m(E - E') \\ \implies 0 &= \left( (M^2 - EE') + m(E - E') \right)^2 - \left( \sqrt{E^2 - M^2} \sqrt{E'^2 - M^2} \right)^2 \\ \implies 0 &= M^2(E^2 - 2EE' + E'^2) + 2(M^2 - EE')m(E - E') + m^2(E - E')^2. \end{aligned}$$

As claimed,  $E' = E$  is a root of this equation, as it must be, because  $E' = E$  and  $p' = p$  certainly satisfy conservation of energy and momentum with the initial conditions, by definition. Dividing through by  $(E - E')$  gives

$$M^2(E - E') + 2m(M^2 - EE') + m^2(E - E') = 0. \quad (12.111)$$

Solving for  $E'$  gives the desired result,

$$E' = \frac{2mM^2 + E(m^2 + M^2)}{2Em + m^2 + M^2}. \quad (12.112)$$

REMARK: Let's look at some limits:

1.  $E \approx M$  (barely moving): then  $E' \approx M$ , because  $M$  is still barely moving.
2.  $M = m$ : then  $E' = M$ , because  $M$  stops, and  $m$  picks up all the energy that  $M$  had.
3.  $m \gg E$  ( $> M$ ) (brick wall): then  $E' \approx E$ , because the heavy mass  $m$  picks up essentially no energy.
4.  $(E >) M \gg m$  and  $M^2 \gg Em$ : then  $E' \approx E$ , because it's essentially like  $m$  isn't there.
5.  $(E >) M \gg m$  but  $Em \gg M^2$ : then  $E' \approx M^2/2m$ . This isn't obvious, but it's interesting that it doesn't depend on  $E$ . This means that no matter how fast you throw a big object at a small one (head-on), the big one will always (as long as you throw it hard enough) end up with the same energy,  $M^2/2m$ . And since

we're assuming  $M^2 \ll Em$ , this resulting energy is much less than  $E$ . So most of the (very large) initial energy ends up in  $m$ .

- 6.  $E \gg m \gg M$ : then  $E' \approx m/2$ . This isn't obvious, but it's similar to an analogous limit in the Compton scattering in Problem 12.7. As above, no matter how fast you throw a small object at a big one (head-on), the small one will always (as long as you throw it hard enough) end up with the same energy,  $m/2$ . ♣

### 12.7. Compton scattering

The 4-momenta before the collision are (see Fig. 12.30)

$$P_\gamma = \left( \frac{hc}{\lambda}, \frac{hc}{\lambda}, 0, 0 \right), \quad P_m = (mc^2, 0, 0, 0). \quad (12.113)$$

The 4-momenta after the collision are

$$P'_\gamma = \left( \frac{hc}{\lambda'}, \frac{hc}{\lambda'} \cos \theta, \frac{hc}{\lambda'} \sin \theta, 0 \right), \quad P'_m = (\text{we won't need this}). \quad (12.114)$$

If we wanted to, we could write  $P'_m$  in terms of its momentum and scattering angle. But we're not concerned with these quantities, and the nice thing about the following method is that we don't need to introduce them. Conservation of energy and momentum give  $P_\gamma + P_m = P'_\gamma + P'_m$ . Therefore,

$$\begin{aligned} P_m'^2 &= (P_\gamma + P_m - P'_\gamma)^2 \\ \implies P_m'^2 &= P_\gamma^2 + P_m^2 + P_\gamma'^2 + 2P_m \cdot (P_\gamma - P'_\gamma) - 2P_\gamma \cdot P'_\gamma \\ \implies m^2 c^4 &= 0 + m^2 c^4 + 0 + 2mc^2 \left( \frac{hc}{\lambda} - \frac{hc}{\lambda'} \right) - 2 \frac{hc}{\lambda} \frac{hc}{\lambda'} (1 - \cos \theta). \end{aligned} \quad (12.115)$$

Canceling the  $m^2 c^4$  terms and multiplying through by  $\lambda \lambda' / (2hmc^3)$  gives the desired result,

$$\lambda' = \lambda + \frac{h}{mc} (1 - \cos \theta). \quad (12.116)$$

The nice thing about this solution is that all the unknown garbage in  $P'_m$  disappeared when we squared it.

REMARK: Let's look at some limits:

1. If  $\theta \approx 0$  (that is, not much scattering), then  $\lambda' \approx \lambda$ , as expected.
2. If  $\theta = \pi$  (that is, backward scattering), then  $\lambda' = \lambda + 2h/mc$ .
3. If  $\theta = \pi$  and additionally  $\lambda \ll h/mc$  (that is,  $mc^2 \ll hc/\lambda = E_\gamma$ , so the photon's energy is much larger than the electron's rest energy), then  $\lambda' \approx 2h/mc$ , so

$$E'_\gamma = \frac{hc}{\lambda'} \approx \frac{hc}{2h/mc} = \frac{1}{2} mc^2. \quad (12.117)$$

Therefore, the photon bounces back with an essentially fixed  $E'_\gamma$ , independent of the initial  $E_\gamma$  (as long as  $E_\gamma$  is large enough). This isn't obvious. In fact, it's not even obvious that the photon *can* bounce straight back. You might think that if it has enough energy, it will end up moving forward along with the electron. However, in the CM frame, the photon bounces backward in a head-on collision. So it must bounce backward in every frame, because a photon's direction can't switch when going from one frame to another. ♣

![Diagram of Compton scattering. An incident photon with wavelength λ moves horizontally from left to right. An electron with mass m is initially at rest. After the collision, the photon is scattered at an angle θ with wavelength λ', and the electron recoils. A coordinate system with x and y axes is shown, with the x-axis along the initial photon direction and the y-axis perpendicular to it. The scattered photon's path is shown in the first quadrant, and the electron's path is shown in the fourth quadrant.](0fc7759e4ecd20d6e727e806fca97fca_img.jpg)

Diagram of Compton scattering. An incident photon with wavelength λ moves horizontally from left to right. An electron with mass m is initially at rest. After the collision, the photon is scattered at an angle θ with wavelength λ', and the electron recoils. A coordinate system with x and y axes is shown, with the x-axis along the initial photon direction and the y-axis perpendicular to it. The scattered photon's path is shown in the first quadrant, and the electron's path is shown in the fourth quadrant.

Fig. 12.30

### 12.8. System of masses

Let the speed of the stick go from zero to  $\epsilon$ , where  $\epsilon \ll v$ . Then the final speeds of the two masses are obtained by relativistically adding or subtracting  $\epsilon$  from  $v$ . (Assume that the time involved is small, so that the masses are still essentially moving horizontally.) Repeating the derivation leading to Eq. (12.26), we see that the final momenta of the two masses have magnitudes  $\gamma_v \gamma_\epsilon (v \pm \epsilon)m$ . But since  $\epsilon$  is small, we can set  $\gamma_\epsilon \approx 1$ , to first order. Therefore, the forward-moving mass has momentum  $\gamma_v(v + \epsilon)m$ , and the backward-moving mass has momentum  $-\gamma_v(v - \epsilon)m$ . So the net increase in momentum is  $\Delta p = 2\gamma m\epsilon$ , where  $\gamma \equiv \gamma_v$ . Hence,

$$F \equiv \frac{\Delta p}{\Delta t} = 2\gamma m \frac{\epsilon}{\Delta t} \equiv 2\gamma ma = Ma. \quad (12.118)$$

### 12.9. Relativistic harmonic oscillator

$F = dp/dt$  gives  $-m\omega^2 x = d(m\gamma v)/dt$ . Using Eq. (12.54), we have

$$-\omega^2 x = \gamma^3 \frac{dv}{dt}. \quad (12.119)$$

We must somehow solve this differential equation. A helpful thing to do is to multiply both sides by  $v$  (which is equivalent to rewriting  $dv/dt$  as  $v dv/dx$ ) to obtain  $-\omega^2 x \dot{x} = \gamma^3 v \dot{v}$ . But from Eq. (12.53), the right-hand side of this is  $d\gamma/dt$ . Integration then gives  $-\omega^2 x^2/2 + C = \gamma$ , where  $C$  is a constant of integration. We know that  $\gamma = 1$  when  $x = b$ , so we find

$$\gamma = 1 + \frac{\omega^2}{2c^2}(b^2 - x^2), \quad (12.120)$$

where we have put the  $c$ 's back in to make the units right. The period is given by

$$T = 4 \int_0^b \frac{dx}{v}. \quad (12.121)$$

But  $\gamma \equiv 1/\sqrt{1 - v^2/c^2}$ , which gives  $v = c\sqrt{\gamma^2 - 1}/\gamma$ . Therefore,

$$T = \frac{4}{c} \int_0^b \frac{\gamma}{\sqrt{\gamma^2 - 1}} dx. \quad (12.122)$$

REMARK: In the limit  $\omega b \ll c$  (so that  $\gamma \approx 1$ , from Eq. (12.120), which means that the speed is always small), we must recover the Newtonian limit. And indeed, to lowest order,  $\gamma^2 \approx 1 + (\omega^2/c^2)(b^2 - x^2)$ , so Eq. (12.122) gives

$$T \approx \frac{4}{c} \int_0^b \frac{dx}{(\omega/c)\sqrt{b^2 - x^2}}. \quad (12.123)$$

This is the correct result, because conservation of energy for a nonrelativistic spring gives

$$\frac{1}{2}k(b^2 - x^2) = \frac{1}{2}mv^2 \implies \omega^2(b^2 - x^2) = v^2. \quad (12.124)$$

Using this  $v$  in the general expression for  $T$  given in Eq. (12.121) yields Eq. (12.123). ♣

### **12.10. Relativistic rocket**

The relation between  $m$  and  $v$  obtained in Eq. (12.67) is independent of the rate at which mass is converted into photons. The point of this problem is to assume a certain rate, in order to obtain a relation between  $v$  and  $t$ .

In the frame of the rocket, we are given  $dm = -\sigma d\tau$ . The usual time-dilation effect gives  $dt = \gamma d\tau$ , so we have  $dm = -(\sigma/\gamma) dt$  in the ground frame. Differentiating Eq. (12.67) to obtain another expression for  $dm$ , we have

$$dm = \frac{-M dv}{(1+v)\sqrt{1-v^2}}. \quad (12.125)$$

Equating the two expressions for  $dm$  gives

$$\int_0^t \frac{\sigma dt}{M} = \int_0^v \frac{dv}{(1+v)(1-v^2)}. \quad (12.126)$$

We could use a computer to do this  $dv$  integral, but let's do it from scratch. Using a few partial-fraction tricks, we have

$$\begin{aligned} \int \frac{dv}{(1+v)(1-v^2)} &= \int \frac{dv}{(1+v)(1-v)(1+v)} \\ &= \frac{1}{2} \int \left( \frac{1}{1+v} + \frac{1}{1-v} \right) \frac{dv}{1+v} \\ &= \frac{1}{2} \int \frac{dv}{(1+v)^2} + \frac{1}{4} \int \left( \frac{1}{1+v} + \frac{1}{1-v} \right) dv \\ &= -\frac{1}{2(1+v)} + \frac{1}{4} \ln\left(\frac{1+v}{1-v}\right). \end{aligned} \quad (12.127)$$

Equation (12.126) therefore gives

$$\frac{\sigma t}{M} = \frac{1}{2} - \frac{1}{2(1+v)} + \frac{1}{4} \ln\left(\frac{1+v}{1-v}\right) = \frac{v}{2(1+v)} + \frac{1}{4} \ln\left(\frac{1+v}{1-v}\right). \quad (12.128)$$

**REMARKS:** If  $v \ll 1$  (or rather, if  $v \ll c$ ), we can Taylor-expand the two terms in Eq. (12.128) to obtain  $\sigma t/M \approx v$ , which can be written as  $\sigma \approx M(v/t) \equiv Ma$ . But  $\sigma$  equals the force acting on the rocket (or rather  $\sigma c$ , to make the units correct), because  $-\sigma$  is the rate of change in momentum of the photons (since their momentum is  $p = -E/c = -(dm c^2)/c$ ). We therefore obtain the expected nonrelativistic  $F = ma$  equation.

If  $v = 1 - \epsilon$ , where  $\epsilon$  is very small (that is, if  $v$  is very close to  $c$ ), then we can make approximations in Eq. (12.128) to obtain  $\epsilon \approx (2e)e^{-4\sigma t/M}$ . We see that the difference between  $v$  and 1 decreases exponentially with  $t$ . ♣

### **12.11. Relativistic dustpan I**

This problem is essentially the same as Problem 12.3. Let  $M'$  be the mass of the dustpan-plus-dust-inside system (which we'll label " $S$ ") when its speed is  $v$ . After a small time  $dt$  in the lab frame,  $S$  has moved a distance  $v dt$ , so it has basically collided with an infinitesimal mass  $\lambda v dt$ . Its energy therefore increases to  $\gamma M + \lambda v dt$ . Its momentum is still  $\gamma M v$ , so its mass is now

$$M' = \sqrt{(\gamma M + \lambda v dt)^2 - (\gamma M v)^2} \approx \sqrt{M^2 + 2\gamma M \lambda v dt}, \quad (12.129)$$

where we have dropped the second-order  $dt^2$  terms. Using the Taylor series  $\sqrt{1+\epsilon} \approx 1 + \epsilon/2$ , we can approximate  $M'$  as

$$M' \approx M \sqrt{1 + \frac{2\gamma\lambda v dt}{M}} \approx M \left( 1 + \frac{\gamma\lambda v dt}{M} \right) = M + \gamma\lambda v dt. \quad (12.130)$$

The rate of increase in  $S$ 's mass is therefore  $\gamma\lambda v$ . As in Problem 12.3, this increase is greater than the nonrelativistic answer of " $\lambda v$ ," because heat is generated during the collision, and this heat shows up as mass in the final object.

**REMARKS:** As explained in the remark in the solution to Problem 12.3, this result is clear if we work in the dustpan frame. In this frame, the above-mentioned infinitesimal mass  $\lambda v dt$  comes flying in with energy  $\gamma(\lambda v dt)$ , and essentially all of this energy shows up as mass in the final object.

Note that the rate at which the mass increases, as measured in the dustpan frame, is  $\gamma^2\lambda v$ , due to time dilation. The dust-entering-dustpan events happen at the same location in the dustpan frame, so we have indeed put the extra  $\gamma$  factor in the correct place. Alternatively, you can think in terms of length contraction.  $S$  sees the dust contracted, so its density is increased to  $\gamma\lambda$ . And the other  $\gamma$  factor comes from the fact that the dust is moving in the dustpan frame, so there is a  $\gamma$  factor in the energy. ♣

### 12.12. Relativistic dustpan II

The initial momentum is  $\gamma_V MV \equiv P$ . There are no external forces, so the momentum of the dustpan-plus-dust-inside system (denoted by " $S$ ") always equals  $P$ . That is,  $\gamma m v = P$ , where  $m$  and  $v$  are the mass and speed of  $S$  at any later time.

Let's find  $v(x)$  first. The energy of  $S$ , namely  $\gamma m$ , increases due to the acquisition of new dust. Therefore,  $d(\gamma m) = \lambda dx$ , which we can write as

$$d\left(\frac{P}{v}\right) = \lambda dx. \quad (12.131)$$

Integrating this, and using the fact that the initial speed is  $V$ , gives  $P/v - P/V = \lambda x$ . Therefore,

$$v(x) = \frac{V}{1 + (V\lambda x/P)}. \quad (12.132)$$

For large  $x$ , this approaches  $P/(\lambda x)$ . This makes sense, because the mass of  $S$  is essentially equal to  $\lambda x$ , and it is moving at a slow, nonrelativistic speed.

To find  $v(t)$ , write the  $dx$  in Eq. (12.131) as  $v dt$  to obtain  $(-P/v^2) dv = \lambda v dt$ . This gives

$$-\int_V^v \frac{P dv}{v^3} = \int_0^t \lambda dt \implies \frac{P}{v^2} - \frac{P}{V^2} = 2\lambda t \implies v(t) = \frac{V}{\sqrt{1 + (2V^2\lambda t/P)}}. \quad (12.133)$$

Integrating this to obtain  $x(t)$  gives

$$x(t) = \frac{P}{V\lambda} \left( \sqrt{1 + \frac{2V^2\lambda t}{P}} - 1 \right). \quad (12.134)$$

If you want, you can rewrite all of these answers in terms of  $M$  via  $P \equiv \gamma_V MV$ .

#### REMARKS:

1. You can also obtain the result in Eq. (12.134) by equating the expressions for  $v$  in Eqs. (12.132) and (12.133). Or you can write the  $v$  in Eq. (12.132) as  $dx/dt$ , and then separate variables and integrate.
2. For small  $t$ , you can show that Eq. (12.134) reduces to  $x = Vt$ , as it should. For large  $t$ ,  $x$  has the interesting property of being proportional to  $\sqrt{t}$ .
3. Given  $P$ , all the results in this problem (when expressed in terms of  $P$ ) are actually the same as the ones obtained in the nonrelativistic case, because Eq. (12.131) is still true there; it's simply the expression for how the mass changes in the nonrelativistic case. From that point on, relativity never entered into the reasoning. ♣

### 12.13. Relativistic dustpan III

DUSTPAN FRAME: Let  $S$  denote the dustpan-plus-dust-inside system at a given time, and consider a small bit of dust (call this system  $s$ ) that enters the dustpan. In  $S$ 's frame, the density of the dust is  $\gamma\lambda$ , due to length contraction. Therefore, in a time  $d\tau$  (where  $\tau$  is the time in the dustpan frame), a little  $s$  system of dust with mass  $\gamma\lambda v d\tau$  crashes into  $S$  and loses its negative momentum of  $-\gamma(\gamma\lambda v d\tau)v = -\gamma^2 v^2 \lambda d\tau$ . The force on  $s$  is therefore  $F = dp/d\tau = \gamma^2 v^2 \lambda$ . The desired force on  $S$  is equal and opposite to this, so

$$F = -\gamma^2 v^2 \lambda. \quad (12.135)$$

LAB FRAME: In a time  $dt$ , where  $t$  is the time in the lab frame, a little  $s$  system of dust with mass  $\lambda v dt$  gets picked up by the dustpan. What is the change in momentum of  $s$ ? It is tempting to say that it is  $\gamma(\lambda v dt)v$ , but this would lead to a force of  $-\gamma v^2 \lambda$  on the dustpan, which doesn't agree with the result we found above in the dustpan frame. This would be a problem, because longitudinal forces should be the same in different frames.

The key point to realize is that the mass of whatever is moving increases at a rate  $\gamma\lambda v$ , and not  $\lambda v$  (see Problem 12.11). We therefore see that the change in momentum of the additional moving mass is  $\gamma(\gamma\lambda v dt)v = \gamma^2 v^2 \lambda dt$ . The original moving system  $S$  therefore loses this much momentum, and so the force on it is  $F = dp/dt = -\gamma^2 v^2 \lambda$ , in agreement with the result in the dustpan frame.

### 12.14. Relativistic cart I

GROUND FRAME (YOUR FRAME): Using reasoning similar to that in Problem 12.3 and Problem 12.11, we see that the mass of the cart-plus-sand-inside system increases at a rate  $\gamma\sigma$ . Therefore, its momentum increases at a rate (using the fact that  $v$  is constant)

$$\frac{dp}{dt} = \gamma \left( \frac{dm}{dt} \right) v = \gamma(\gamma\sigma)v = \gamma^2 \sigma v. \quad (12.136)$$

Since  $F = dp/dt$ , this is the force that you exert on the cart. Therefore, it is also the force that the ground exerts on your feet, because the net force on you is zero (since your momentum is constant, and in fact zero).

CART FRAME: The sand-entering-cart events happen at the same location in the ground frame, so time dilation says that the sand enters the cart at a slower rate in the cart frame, that is, at a rate  $\sigma/\gamma$ . The sand flies in at speed  $v$ , and then eventually comes to rest on the cart, so its momentum decreases at a rate  $\gamma(\sigma/\gamma)v = \sigma v$ . This must therefore be the force that your hand applies to the cart.

If this were the only change in momentum in the problem, then we would have a problem, because the force on your feet would be  $\sigma v$  in the cart frame, whereas we found above that it is  $\gamma^2 \sigma v$  in the ground frame. This would contradict the fact that longitudinal forces are the same in different frames. What is the resolution to this apparent paradox? The resolution is that while you are pushing on the cart, *your mass is decreasing*. You are moving at speed  $v$  in the cart frame, and mass is continually being transferred from you (who are moving) to the cart (which is at rest), as we will show. This is the missing change in momentum that we need. The quantitative reasoning is as follows.

Go back to the ground frame for a moment. We saw above that the mass of the cart-plus-sand-inside system (call this system “ $C$ ”) increases at a rate  $\gamma \sigma$  in the ground frame. Therefore, the energy of  $C$  increases at a rate  $\gamma(\gamma \sigma)$  in the ground frame. The sand provides  $\sigma$  of this energy, so you must provide the remaining  $(\gamma^2 - 1)\sigma$  part. Therefore, since you are losing energy at this rate, you must also be losing mass at this rate in the ground frame (because you are at rest there).

Now go back to the cart frame. Due to time dilation, you lose mass at a rate of only  $(\gamma^2 - 1)\sigma/\gamma$ . This mass goes from moving at speed  $v$  (that is, along with you), to speed zero (that is, at rest on the cart). Therefore, the rate of decrease in momentum of this mass is  $\gamma((\gamma^2 - 1)\sigma/\gamma)v = (\gamma^2 - 1)\sigma v$ . Adding this result to the  $\sigma v$  result we found for the sand, we see that the total rate of decrease in momentum is  $\gamma^2 \sigma v$ . This is therefore the force that the ground applies to your feet, in agreement with the above calculation in the ground frame.

Note that the reason why we didn’t have to worry about your changing mass when doing the calculation in the ground frame was that your speed there was zero. Your momentum was therefore always zero, independent of what was happening to your mass.

### 12.15. Relativistic cart II

**GROUND FRAME:** Using reasoning similar to that in Problem 12.3 and Problem 12.11, we see that the mass of the cart-plus-sand-inside system increases at a rate  $\gamma \sigma$ . Therefore, its momentum increases at a rate  $\gamma(\gamma \sigma)v = \gamma^2 \sigma v$ . However, this is *not* the force that your hand exerts on the cart. The reason is that your hand is receding from the location where the sand enters the cart, so your hand cannot immediately be aware of the need for additional momentum. No matter how rigid the cart is, it can’t transmit information faster than  $c$ . In a sense, there is a sort of Doppler effect going on, and your hand needs to be responsible for only a certain fraction of the momentum increase. Let’s be quantitative about this.

Consider two grains of sand that enter the cart a time  $t$  apart. What is the difference between the two times that your hand becomes aware that the grains have entered the cart? Assuming maximal rigidity (that is, assuming that signals propagate along the cart at speed  $c$ ), the relative speed (as measured by someone on the ground) of the signals and your hand is  $c - v$ . The distance between the two signals is  $ct$ . Therefore, they arrive at your hand separated by a time of  $ct/(c - v)$ . In other words, the rate at which you feel sand entering the cart is  $(c - v)/c$  times the given  $\sigma$  rate. This is the factor by which we must multiply the naive  $\gamma^2 \sigma v$  result for the force we found above. The force you apply is therefore (dropping the  $c$ ’s)

$$F = \left(1 - \frac{v}{c}\right) \gamma^2 \sigma v = \frac{\sigma v}{1 + v}. \quad (12.137)$$

**CART FRAME (YOUR FRAME):** The sand-entering-cart events happen at the same location in the ground frame, so time dilation says that the sand enters the cart at a slower rate in the cart frame, that is, at a rate  $\sigma/\gamma$ . The sand flies in at speed  $v$ , and then eventually comes to rest on the cart, so its momentum decreases at a rate  $\gamma(\sigma/\gamma)v = \sigma v$ . But again, this is *not* the force that your hand exerts on the cart. As above, the sand enters the cart at a location that is receding from your hand, so your hand cannot immediately be aware of the need for additional momentum. Let's be quantitative about this.

Consider two grains of sand that enter the cart a time  $t$  apart. What is the difference between the two times that your hand becomes aware that the grains have entered the cart? Assuming maximal rigidity (that is, assuming that signals propagate along the cart at speed  $c$ ), the relative speed (as measured by someone on the cart) of the signals and your hand is  $c$ , because you are at rest. The distance between the two signals is  $ct + vt$ , because the sand source is moving away from you at speed  $v$ . Therefore, the signals arrive at your hand separated by a time of  $(c + v)t/c$ . In other words, the rate at which you feel sand entering the cart is  $c/(c + v)$  times the time-dilated  $\sigma/\gamma$  rate. This is the factor by which we must multiply the naive  $\sigma v$  result for the force we found above. The force you apply is therefore (dropping the  $c$ 's)

$$F = \left( \frac{1}{1 + v/c} \right) \sigma v = \frac{\sigma v}{1 + v}, \quad (12.138)$$

in agreement with Eq. (12.137).

In a nutshell, the two naive results in the two frames,  $\gamma^2 \sigma v$  and  $\sigma v$ , differ by two factors of  $\gamma$ . But the ratio of the two “Doppler-effect” factors (which arose from the impossibility of absolute rigidity) precisely remedies this discrepancy. The reason why we didn't need to consider this Doppler effect in Problem 12.14 is that there your hand is always right next to the point where the sand enters the cart.

### 12.16. Different frames

- (a) The energy of the resulting blob is  $2m + T\ell$ . Since the blob is at rest, we have

$$M = 2m + T\ell. \quad (12.139)$$

- (b) Let the new frame be  $S$ . Let the original frame be  $S'$ . The critical point to realize is that in frame  $S$ , the left mass starts to accelerate before the right mass does. This is due to the loss of simultaneity between the frames.

Consider the two events at which the two masses start to move. Let the left mass and right mass start moving at positions  $x_l$  and  $x_r$  in  $S$ . The Lorentz transformation  $\Delta x = \gamma(\Delta x' + v\Delta t')$  tells us that  $x_r - x_l = \gamma\ell$ , because  $\Delta x' = \ell$  and  $\Delta t' = 0$  for these events. Alternatively, this follows from length contraction, because if we picture things in the original  $S'$  frame, then the length  $\gamma\ell$  in  $S$  is what is length contracted down to  $\ell$  in  $S'$ .

Let the masses collide at position  $x_c$  in  $S$ . Then the gain in energy of the left mass is  $T(x_c - x_l)$ , and the gain in energy of the right mass is  $(-T)(x_c - x_r)$  which is negative if  $x_c > x_r$ . We have used the fact that the longitudinal force is the same in the two frames, so the masses still feel a tension  $T$  in frame  $S$ . The gain in the sum of the energies of the two masses is therefore

$$\Delta E = T(x_c - x_l) + (-T)(x_c - x_r) = T(x_r - x_l) = T\gamma\ell. \quad (12.140)$$

The initial sum of the energies was  $2\gamma m$ , so the final energy is

$$E = 2\gamma m + T\gamma\ell = \gamma M, \quad (12.141)$$

as desired.

### 12.17. **Splitting mass**

We'll calculate the times for the two parts of the process to occur. The energy of the mass right before it splits is (with the subscript b for "before")  $E_b = M + T(\ell/2)$ , so the momentum is  $p_b = \sqrt{E_b^2 - M^2} = \sqrt{MT\ell + T^2\ell^2/4}$ . Using  $F = dp/dt \implies t = \Delta p/T$ , the time for the first part of the process is

$$t_1 = \frac{\sqrt{MT\ell + T^2\ell^2/4}}{T} = \sqrt{\frac{M\ell}{T} + \frac{\ell^2}{4}}. \quad (12.142)$$

The momentum of the front half of the mass immediately after it splits is  $p_a = p_b/2 = (1/2)\sqrt{MT\ell + T^2\ell^2/4}$ . The energy at the wall is  $E_w = E_b/2 + T(\ell/2) = M/2 + 3T\ell/4$ , so the momentum at the wall is  $p_w = \sqrt{E_w^2 - (M/2)^2} = (1/2)\sqrt{3MT\ell + 9T^2\ell^2/4}$ . The change in momentum during the second part of the process is therefore

$$\Delta p = p_w - p_a = (1/2)\sqrt{3MT\ell + 9T^2\ell^2/4} - (1/2)\sqrt{MT\ell + T^2\ell^2/4}. \quad (12.143)$$

Since we have  $t = \Delta p/T$ , the time for the second part is

$$t_2 = \frac{1}{2}\sqrt{\frac{3M\ell}{T} + \frac{9\ell^2}{4}} - \frac{1}{2}\sqrt{\frac{M\ell}{T} + \frac{\ell^2}{4}}. \quad (12.144)$$

The total time is  $t_1 + t_2$ , which simply changes the minus sign in this expression to a plus sign.

### 12.18. **Relativistic leaky bucket**

- (a) Let the wall be at  $x = 0$ , and let the initial position be  $x = \ell$ . Consider a small interval during which the bucket moves from  $x$  to  $x + dx$  (where  $dx$  is negative). The bucket's energy changes by  $(-T) dx$  due to the string (this is positive), and also changes by a fraction  $dx/x$ , due to the leaking (this is negative). Therefore,  $dE = (-T) dx + E dx/x$ , or

$$\frac{dE}{dx} = -T + \frac{E}{x}. \quad (12.145)$$

In solving this differential equation, it is convenient to introduce the variable  $y \equiv E/x$ . With this definition, we have  $E' = (xy)' = xy' + y$ , where a prime denotes differentiation with respect to  $x$ . Equation (12.145) then becomes  $xy' = -T$ , or  $dy = -T dx/x$ . Integration gives  $y = -T \ln x + C$ , which we can write as  $y = -T \ln(x/\ell) + B$ , in order to have a dimensionless argument in the log. Since  $E = xy$ , we therefore have

$$E(x) = Bx - Tx \ln(x/\ell), \quad (12.146)$$

where  $B$  is a constant of integration. The reasoning up to this point is valid for *both* the total energy and the kinetic energy, because they both change in the two ways described above. Let's look at each case.

TOTAL ENERGY: Equation (12.146) gives

$$E = M(x/\ell) - Tx \ln(x/\ell), \quad (12.147)$$

where the constant of integration,  $B$ , has been chosen to be  $M/\ell$  so that  $E = M$  when  $x = \ell$ . In terms of the fraction  $z \equiv x/\ell$ , we have  $E = Mz - T\ell z \ln z$ . Setting  $dE/dz = 0$  to find the maximum gives

$$\ln z_{\max} = \frac{M}{T\ell} - 1 \implies E_{\max} = \frac{T\ell}{e} e^{M/T\ell}. \quad (12.148)$$

The fraction  $z$  must satisfy  $z \leq 1$ , so we must have  $\ln z \leq 0$ . Therefore, a solution for  $z$  exists only if  $M \leq T\ell$ . If  $M \geq T\ell$ , then the total energy decreases all the way to the wall.

REMARKS: If  $M$  is slightly less than  $T\ell$ , then  $z_{\max}$  is slightly less than 1, so  $E$  quickly achieves a maximum of slightly more than  $M$ , then decreases for the rest of the way to the wall.

If  $M \ll T\ell$ , then  $E$  achieves its maximum at  $z_{\max} \approx 1/e$ , where it has the value  $T\ell/e$ . Essentially all of the energy is kinetic in this case, so this result must agree with the result for the kinetic energy below, which it indeed will. ♣

KINETIC ENERGY: Equation (12.146) gives

$$K = -Tx \ln(x/\ell), \quad (12.149)$$

where the constant of integration,  $B$ , has been chosen to be zero so that  $K = 0$  when  $x = \ell$ . Equivalently,  $E - K$  must equal the mass  $M(x/\ell)$ . In terms of the fraction  $z \equiv x/\ell$ , we have  $K = -T\ell z \ln z$ . Setting  $dK/dz = 0$  to find the maximum gives

$$z_{\max} = \frac{1}{e} \implies K_{\max} = \frac{T\ell}{e}, \quad (12.150)$$

which is independent of  $M$ . This result must reduce properly in the nonrelativistic limit. But since there's nothing that needs reducing (there aren't any terms that are small compared with others when  $v \ll c$ ), this result must exactly equal the nonrelativistic result. And indeed, the analogous "Leaky bucket" problem in Chapter 5 (Problem 5.17) gives the same answer.

- (b) With  $z \equiv x/\ell$ , the momentum of the bucket is  $p = \sqrt{E^2 - m^2} = \sqrt{E^2 - (Mz)^2}$ , so Eq. (12.147) gives

$$p = \sqrt{(Mz - T\ell z \ln z)^2 - (Mz)^2} = \sqrt{-2MT\ell z^2 \ln z + T^2\ell^2 z^2 \ln^2 z}. \quad (12.151)$$

Setting the derivative equal to zero gives  $T\ell \ln^2 z + (T\ell - 2M) \ln z - M = 0$ . The maximum momentum therefore occurs at

$$\ln z_{\max} = \frac{2M - T\ell - \sqrt{T^2\ell^2 + 4M^2}}{2T\ell}. \quad (12.152)$$

We have ignored the other root, because it gives  $\ln z > 0 \implies z > 1$ .

REMARKS:

1. If  $M \ll T\ell$ , then  $\ln z_{\max} \approx -1 \implies z_{\max} \approx 1/e$ . In this case, the bucket immediately moves with  $v \approx c$ , so we have  $E \approx pc$ . Therefore,  $E$  and  $p$  should achieve their maxima at the same location. And indeed, we saw above that  $E_{\max}$  occurs at  $z_{\max} \approx 1/e$ .
2. If  $M \gg T\ell$ , then  $\ln z_{\max} \approx -1/2 \implies z_{\max} \approx 1/\sqrt{e}$ . In this case, the bucket is nonrelativistic, so this result should agree with Problem 5.17, which it does.
3. If  $M = T\ell$ , then  $\ln z_{\max} = (1 - \sqrt{5})/2$ , which is the negative of the inverse of the golden ratio. ♣

### 12.19. Relativistic bucket

- (a) The energy of the mass right before it hits the wall is  $E = m + T\ell$ . Therefore, the momentum right before it hits the wall is  $p = \sqrt{E^2 - m^2} = \sqrt{2mT\ell + T^2\ell^2}$ . So  $F = dp/dt$  gives (using the fact that the tension is constant)

$$\Delta t = \frac{\Delta p}{F} = \frac{\sqrt{2mT\ell + T^2\ell^2}}{T}. \quad (12.153)$$

If  $m \ll T\ell$ , then  $\Delta t \approx \ell$  (or  $\ell/c$  in normal units), which makes sense, because the mass travels at essentially speed  $c$ . And if  $m \gg T\ell$ , then  $\Delta t \approx \sqrt{2m\ell/T}$ . This is the nonrelativistic limit, and it agrees with the result obtained from the familiar expression,  $\ell = at^2/2$ , where  $a = T/m$  is the acceleration.

- (b) **STRAIGHTFORWARD METHOD:** The energy of the blob right before it hits the wall is  $E_w = 2m + 2T\ell$  (with the subscript *w* for “wall”). If we can find the mass,  $M$ , of the blob, then we can use  $p = \sqrt{E^2 - M^2}$  to get the momentum, and then use  $\Delta t = \Delta p/F$  to get the time.<sup>17</sup>

From part (a), the momentum right before the collision is  $p_b = \sqrt{2mT\ell + T^2\ell^2}$ , and this is also the momentum of the blob right after the collision,  $p_a$ . The energy of the blob right after the collision is  $E_a = 2m + T\ell$ . So the mass of the blob after the collision is  $M = \sqrt{E_a^2 - p_a^2} = \sqrt{4m^2 + 2mT\ell}$ . Therefore, the momentum at the wall is  $p_w = \sqrt{E_w^2 - M^2} = \sqrt{6mT\ell + 4T^2\ell^2}$ , and so

$$\Delta t = \frac{\Delta p}{F} = \frac{\sqrt{6mT\ell + 4T^2\ell^2}}{T}. \quad (12.154)$$

If  $m = 0$  then  $\Delta t = 2\ell$ , as expected.

**BETTER METHOD:** In the notation in the hint in the statement of the problem, the change in  $p^2$  from the start to just before the collision is  $\Delta(p^2) = E_2^2 - E_1^2$ . This is true because

$$E_1^2 - m^2 = p_1^2, \quad \text{and} \quad E_2^2 - m^2 = p_2^2, \quad (12.155)$$

and since  $m$  is the same throughout the first half of the process, we have  $\Delta(E^2) = \Delta(p^2)$ . Likewise, the change in  $p^2$  during the second half of the process is  $\Delta(p^2) = E_4^2 - E_3^2$ , because

$$E_3^2 - M^2 = p_3^2, \quad \text{and} \quad E_4^2 - M^2 = p_4^2, \quad (12.156)$$

and since  $M$  is the same throughout the second half of the process,<sup>18</sup> we have  $\Delta(E^2) = \Delta(p^2)$ . The total change in  $p^2$  is the sum of the above two changes, so the final  $p^2$  is

$$\begin{aligned} p^2 &= (E_2^2 - E_1^2) + (E_4^2 - E_3^2) \\ &= ((m + T\ell)^2 - m^2) + ((2m + 2T\ell)^2 - (2m + T\ell)^2) \\ &= 6mT\ell + 4T^2\ell^2, \end{aligned} \quad (12.157)$$

as in Eq. (12.154). The first solution in effect performed the same calculation, but in a more obscure manner.

- (c) The reasoning in part (b) tells us that the final  $p^2$  equals the sum of the  $\Delta(E^2)$  terms over the  $N$  parts of the process. So we have, using an indexing notation

<sup>17</sup> Although the tension  $T$  acts on two different things (the mass  $m$  initially, and then the blob), it is valid to use the total  $\Delta p$  to obtain the total time via  $\Delta t = \Delta p/F$ , because if we wanted to, we could break up the  $\Delta p$  into its two parts, and then find the two partial times, and then add them back together to get the total  $\Delta t$ .

<sup>18</sup> From the first solution,  $M$  happens to be  $\sqrt{4m^2 + 2mT\ell}$ , but the nice thing about this solution is that we don't need to know this. All we need to know is that it is constant.

analogous to that in part (b),

$$\begin{aligned}
 p^2 &= \sum_{k=1}^N (E_{2k}^2 - E_{2k-1}^2) = \sum_{k=1}^N \left( (km + kT\ell)^2 - (km + (k-1)T\ell)^2 \right) \\
 &= \sum_{k=1}^N \left( 2kmT\ell + (k^2 - (k-1)^2)T^2\ell^2 \right) \\
 &= N(N+1)mT\ell + N^2T^2\ell^2. \quad (12.158)
 \end{aligned}$$

Therefore,

$$\Delta t = \frac{\Delta p}{F} = \frac{\sqrt{N(N+1)mT\ell + N^2T^2\ell^2}}{T}. \quad (12.159)$$

This agrees with the results from parts (a) and (b), for  $N = 1$  and 2.

- (d) We want to take the limit  $N \rightarrow \infty$ ,  $\ell \rightarrow 0$ ,  $m \rightarrow 0$ , with the restrictions that  $N\ell = L$  and  $Nm = M$ . Written in terms of  $M$  and  $L$ , Eq. (12.159) becomes

$$\Delta t = \frac{\sqrt{(1+1/N)MTL + T^2L^2}}{T} \longrightarrow \frac{\sqrt{MTL + T^2L^2}}{T}, \quad (12.160)$$

as  $N \rightarrow \infty$ . This  $\Delta t$  is the same as the time it takes for one particle of mass  $m = M/2$  to reach the wall, from part (a). The mass of the bucket at the wall is

$$\begin{aligned}
 M_w &= \sqrt{E_w^2 - p_w^2} = \sqrt{(M + TL)^2 - (MTL + T^2L^2)} \\
 &= \sqrt{M^2 + MTL}. \quad (12.161)
 \end{aligned}$$

If  $TL \ll M$ , then  $M_w \approx M$ , which makes sense. If  $M \ll TL$ , then  $M_w \approx \sqrt{MTL}$ , which means that  $M_w$  is the geometric mean between the given mass and the energy stored in the string. This isn't entirely obvious. The speed of the bucket right before it hits the wall is

$$\begin{aligned}
 v_w &= \frac{p_w}{E_w} = \frac{\sqrt{MTL + T^2L^2}}{M + TL} \\
 &= \sqrt{\frac{TL}{M + TL}} = \sqrt{\frac{T}{T + \rho}} \longrightarrow c\sqrt{\frac{T}{T + \rho c^2}}, \quad (12.162)
 \end{aligned}$$

where  $\rho \equiv M/L$  is the mass density.

REMARK: Note that  $v_w$  depends only on  $T$  and  $\rho$ . This means that if we change  $L$  by moving the wall to any other position, the speed at the wall will still be  $v_w$ . In other words, the bucket moves toward the wall at the *constant* speed  $v_w$ . (The task of Exercise 12.40 is to derive this result without taking the  $N \rightarrow \infty$  limit of many masses.) This constant-speed result must also hold in the nonrelativistic limit (that is,  $T \ll \rho c^2$ ), for which we have  $v_w \approx \sqrt{T/\rho}$ . And indeed, this agrees with the result for Problem 5.27 ("Pulling a chain again"), which is essentially the same problem, in different language. ♣