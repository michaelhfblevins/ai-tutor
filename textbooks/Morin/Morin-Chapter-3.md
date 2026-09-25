# Chapter 3 Using $F = ma$

The general goal of classical mechanics is to determine what happens to a given set of objects in a given physical situation. In order to figure this out, we need to know what makes the objects move the way they do. There are two main ways of going about this task. The first one, which you are undoubtedly familiar with, involves Newton's laws. This is the subject of the present chapter. The second one, which is more advanced, is the *Lagrangian* method. This is the subject of Chapter 6. It should be noted that each of these methods is perfectly sufficient for solving any problem, and they both produce the same information in the end. But they are based on vastly different principles. We'll talk more about this in Chapter 6.

## 3.1 Newton's laws

In 1687 Newton published his three laws in his *Principia Mathematica*. These laws are fairly intuitive, although I suppose it's questionable to attach the adjective "intuitive" to a set of statements that weren't written down until a mere 300 years ago. At any rate, the laws may be stated as follows.

- **First law:** A body moves with constant velocity (which may be zero) unless acted on by a force.
- **Second law:** The time rate of change of the momentum of a body equals the force acting on the body.
- **Third law:** For every force on one body, there is an equal and opposite force on another body.

We could discuss for days on end the degree to which these statements are physical laws, and the degree to which they are definitions. Sir Arthur Eddington once made the unflattering remark that the first law essentially says that "every particle continues in its state of rest or uniform motion in a straight line except insofar as it doesn't." However, although the three laws might seem somewhat light on content at first glance, there's actually more to them than Eddington's comment implies. Let's look at each in turn.<sup>1</sup>

<sup>1</sup> A disclaimer: This section represents my view on which parts of the laws are definitions and which parts have content. But you should take all of this with a grain of salt. For further reading, see Anderson (1990), Keller (1987), O'Sullivan (1980), and Eisenbud (1958).

### **First law**

One thing this law does is give a definition of zero force. Another thing it does is give a definition of an *inertial frame*, which is defined simply as a frame of reference in which the first law holds; since the term “velocity” is used, we have to state what frame we’re measuring the velocity with respect to. The first law does *not* hold in an arbitrary frame. For example, it fails in the frame of a rotating turntable.<sup>2</sup> Intuitively, an inertial frame is one that moves with constant velocity. But this is ambiguous, because we have to say what the frame is moving with constant velocity *with respect to*. But all this aside, an inertial frame is defined as the special type of frame in which the first law holds.

So, what we now have are two intertwined definitions of “force” and “inertial frame.” Not much physical content here. But the important point is that the law holds for *all* particles. So if we have a frame in which one free particle moves with constant velocity, then *all* free particles move with constant velocity. This is a statement with content. We can’t have a bunch of free particles moving with constant velocity while another one is doing a fancy jig.

### **Second law**

Momentum is defined<sup>3</sup> to be  $m\mathbf{v}$ . If  $m$  is constant,<sup>4</sup> then the second law says that

$$\mathbf{F} = m\mathbf{a}, \quad (3.1)$$

where  $\mathbf{a} \equiv d\mathbf{v}/dt$ . This law holds only in an inertial frame, which is defined by the first law.

For things moving free or at rest,  
 Observe what the first law does best.  
 It defines a key frame,  
 “Inertial” by name,  
 Where the second law then is expressed.

You might think that the second law merely gives a definition of force, but there is more to it than that. There is a tacit implication in the law that this “force” is something that has an existence that isn’t completely dependent on the particle whose “ $m$ ” appears in the law (more on this in the third law below). A spring force, for example, doesn’t depend at all on the particle on which it acts. And the gravitational force,  $GMm/r^2$ , depends partly on the particle and partly on something else (another mass).

<sup>2</sup> It’s possible to modify things so that Newton’s laws hold in such a frame, provided that we introduce the so-called “fictitious” forces. But we’ll save this discussion for Chapter 10.

<sup>3</sup> We’re doing everything nonrelativistically here, of course. Chapter 12 gives the relativistic modification to the  $m\mathbf{v}$  expression.

<sup>4</sup> We’ll assume in this chapter that  $m$  is constant. But don’t worry, we’ll get plenty of practice with changing mass (in rockets and such) in Chapter 5.

If you feel like just making up definitions, then you can define a new quantity,  $\mathbf{G} = m^2 \mathbf{a}$ . This is a perfectly legal thing to do; you can't really go wrong in making a definition (well, unless you've already defined the quantity to be something else). However, this definition is completely useless. You can define it for every particle in the world, and for any acceleration, but the point is that the definitions don't have anything to do with each other. There is simply no (uncontrived) quantity in this world that gives accelerations in the ratio of 4 to 1 when "acting" on masses  $m$  and  $2m$ . The quantity  $\mathbf{G}$  has nothing to do with anything except the particle you defined it for. The main thing the second law says is that there does indeed exist a quantity  $\mathbf{F}$  that gives the same  $m\mathbf{a}$  when acting on different particles. The statement of the existence of such a thing is far more than a definition.

Along this same line, note that the second law says that  $\mathbf{F} = m\mathbf{a}$ , and not, for example,  $\mathbf{F} = m\mathbf{v}$ , or  $\mathbf{F} = m d^3 \mathbf{x} / dt^3$ . In addition to being inconsistent with the real world, these expressions are inconsistent with the first law.  $\mathbf{F} = m\mathbf{v}$  would say that a nonzero velocity requires a force, in contrast with the first law. And  $\mathbf{F} = m d^3 \mathbf{x} / dt^3$  would say that a particle moves with constant acceleration (instead of constant velocity) unless acted on by a force, also in contrast with the first law.

As with the first law, it is important to realize that the second law holds for *all* particles. In other words, if the same force (for example, the same spring stretched by the same amount) acts on two particles with masses  $m_1$  and  $m_2$ , then Eq. (3.1) says that their accelerations are related by

$$\frac{a_1}{a_2} = \frac{m_2}{m_1}. \quad (3.2)$$

This relation holds regardless of what the common force is. Therefore, once we've used one force to find the relative masses of two objects, then we know what the ratio of their  $a$ 's will be when they are subjected to any other force. Of course, we haven't really defined *mass* yet. But Eq. (3.2) gives an experimental method for determining an object's mass in terms of a standard (say, 1 kg) mass. All we have to do is compare its acceleration with that of the standard mass, when acted on by the same force.

Note that  $\mathbf{F} = m\mathbf{a}$  is a vector equation, so it is really three equations in one. In Cartesian coordinates, it says that  $F_x = ma_x$ ,  $F_y = ma_y$ , and  $F_z = ma_z$ .

### Third law

One thing this law says is that if we have two isolated particles interacting through some force, then their accelerations are opposite in direction and inversely proportional to their masses. Equivalently, the third law essentially postulates that

the total momentum of an isolated system is conserved (that is, independent of time). To see this, consider two particles, each of which interacts only with the other particle and nothing else in the universe. Then we have

$$\begin{aligned}\frac{d\mathbf{p}_{\text{total}}}{dt} &= \frac{d\mathbf{p}_1}{dt} + \frac{d\mathbf{p}_2}{dt} \\ &= \mathbf{F}_1 + \mathbf{F}_2,\end{aligned}\tag{3.3}$$

where  $\mathbf{F}_1$  and  $\mathbf{F}_2$  are the forces acting on  $m_1$  and  $m_2$ , respectively. This demonstrates that momentum conservation (that is,  $d\mathbf{p}_{\text{total}}/dt = 0$ ) is equivalent to Newton's third law (that is,  $\mathbf{F}_1 = -\mathbf{F}_2$ ). Similar reasoning holds with more than two particles, but we'll save this more general case, along with many other aspects of momentum, for Chapter 5.

There isn't much left to be defined via this law, so this is a law of pure content. It can't be a definition, anyway, because it's actually not always valid. It holds for forces of the "pushing" and "pulling" type, but it fails for the magnetic force, for example. In that case, momentum is carried off in the electromagnetic field (so the total momentum of the particles *and* the field is conserved). But we won't deal with fields here. Just particles. So the third law will always hold in any situation we'll be concerned with.

The third law contains an extremely important piece of information. It says that we will never find a particle accelerating unless there's some other particle accelerating somewhere else. The other particle might be far away, as with the earth–sun system, but it's always out there somewhere. Note that if we were given only the second law, then it would be perfectly possible for a given particle to spontaneously accelerate with nothing else happening in the universe, as long as a similar particle with twice the mass accelerated with half the acceleration when placed in the same spot, etc. This would all be fine, as far as the second law goes. We would say that a force with a certain value is acting at the point, and everything would be consistent. But the third law says that this is simply not the way the world (at least the one we live in) works. In a sense, a force without a counterpart seems somewhat like magic, whereas a force with an equal and opposite counterpart has a "cause and effect" nature, which seems (and apparently is) more physical.

In the end, however, we shouldn't attach too much significance to Newton's laws, because although they were a remarkable intellectual achievement and work spectacularly for everyday physics, they are the laws of a theory that is only approximate. Newtonian physics is a limiting case of the more correct theories of relativity and quantum mechanics, which are in turn limiting cases of yet more correct theories. The way in which particles (or waves, or strings, or whatever) interact on the most fundamental level surely doesn't bear any resemblance to what we call forces.

## 3.2 Free-body diagrams

The law that allows us to be quantitative is the second law. Given a force, we can apply  $\mathbf{F} = m\mathbf{a}$  to find the acceleration. And knowing the acceleration, we can determine the behavior of a given object (that is, the position and velocity), provided that we are given the initial position and velocity. This process sometimes takes a bit of work, but there are two basic types of situations that commonly arise.

- In many problems, all you are given is a physical situation (for example, a block resting on a plane, strings connecting masses, etc.), and it is up to you to find all the forces acting on all the objects, using  $\mathbf{F} = m\mathbf{a}$ . The forces generally point in various directions, so it's easy to lose track of them. It therefore proves useful to isolate the objects and draw all the forces acting on each of them. This is the subject of the present section.
- In other problems, you are *given* the force explicitly as a function of time, position, or velocity, and the task immediately becomes the mathematical one of solving the  $F = ma \equiv m\ddot{x}$  equation (we'll just deal with one dimension here). These *differential equations* can be difficult (or impossible) to solve exactly. They are the subject of Section 3.3.

Let's consider here the first of these two types of scenarios, where we are presented with a physical situation and we must determine all the forces involved. The term *free-body diagram* is used to denote a diagram with all the forces drawn on a given object. After drawing such a diagram for each object in the setup, we simply write down all the  $F = ma$  equations they imply. The result will be a system of linear equations in various unknown forces and accelerations, for which we can then solve. This procedure is best understood through an example.

---

**Example (A plane and masses):** Mass  $M_1$  is held on a plane with inclination angle  $\theta$ , and mass  $M_2$  hangs over the side. The two masses are connected by a massless string which runs over a massless pulley (see Fig. 3.1). The coefficient of kinetic friction between  $M_1$  and the plane is  $\mu$ .  $M_1$  is released from rest. Assuming that  $M_2$  is sufficiently large so that  $M_1$  gets pulled up the plane, what is the acceleration of the masses? What is the tension in the string?

**Solution:** The first thing to do is draw all the forces on the two masses. These are shown in Fig. 3.2. The forces on  $M_2$  are gravity and the tension. The forces on  $M_1$  are gravity, friction, the tension, and the normal force. Note that the friction force points down the plane, because we are assuming that  $M_1$  moves up the plane.

Having drawn all the forces, we can now write down all the  $F = ma$  equations. When dealing with  $M_1$ , we could break things up into horizontal and vertical components, but it is much cleaner to use the components parallel and perpendicular to the

![Diagram of a mass M1 on an inclined plane connected by a string over a pulley to a hanging mass M2.](04519be9bd73b202914a1bb3da732edd_img.jpg)

The diagram shows a block of mass  $M_1$  on an inclined plane at an angle  $\theta$  to the horizontal. A string is attached to  $M_1$ , runs parallel to the incline, and goes over a pulley at the top. A second block of mass  $M_2$  hangs vertically from the other end of the string. The coefficient of friction  $\mu$  is indicated on the incline.

Diagram of a mass M1 on an inclined plane connected by a string over a pulley to a hanging mass M2.

Fig. 3.1

![Free-body diagrams for masses M1 and M2.](e6751f2eb226d6663ce80a2cb1603dec_img.jpg)

The diagram shows two free-body diagrams. The top one is for mass  $M_1$  on the incline, showing four force vectors: the normal force  $N$  perpendicular to the incline, the tension  $T$  pointing up the incline, the friction force  $f$  pointing down the incline, and the weight  $M_1g$  pointing vertically downwards. The bottom one is for mass  $M_2$ , showing two force vectors: the tension  $T$  pointing upwards and the weight  $M_2g$  pointing downwards.

Free-body diagrams for masses M1 and M2.

Fig. 3.2

plane.<sup>5</sup> These two components of  $\mathbf{F} = m\mathbf{a}$ , along with the vertical  $F = ma$  equation for  $M_2$ , give

$$\begin{aligned} T - f - M_1 g \sin \theta &= M_1 a, \\ N - M_1 g \cos \theta &= 0, \\ M_2 g - T &= M_2 a, \end{aligned} \quad (3.4)$$

where we have used the fact that the two masses accelerate at the same rate (and we have defined the positive direction for  $M_2$  to be downward). We have also used the fact that the tension is the same at both ends of the string, because otherwise there would be a net force on some part of the string which would then undergo infinite acceleration, because it is massless.

There are four unknowns in Eq. (3.4) (namely  $T$ ,  $a$ ,  $N$ , and  $f$ ), but only three equations. Fortunately, we have a fourth equation:  $f = \mu N$ , because we are assuming that  $M_1$  is in fact moving, so we can use the expression for kinetic friction. Using this in the second equation above gives  $f = \mu M_1 g \cos \theta$ . The first equation then becomes  $T - \mu M_1 g \cos \theta - M_1 g \sin \theta = M_1 a$ . Adding this to the third equation leaves us with only  $a$ , so we find

$$a = \frac{g(M_2 - \mu M_1 \cos \theta - M_1 \sin \theta)}{M_1 + M_2} \implies T = \frac{M_1 M_2 g (1 + \mu \cos \theta + \sin \theta)}{M_1 + M_2}. \quad (3.5)$$

Note that in order for  $M_1$  to in fact accelerate upward (that is,  $a > 0$ ), we must have  $M_2 > M_1(\mu \cos \theta + \sin \theta)$ . This is clear from looking at the forces along the plane.

**REMARK:** If we instead assume that  $M_1$  is sufficiently large so that it slides down the plane, then the friction force points up the plane, and we find (as you can check),

$$a = \frac{g(M_2 + \mu M_1 \cos \theta - M_1 \sin \theta)}{M_1 + M_2}, \quad \text{and} \quad T = \frac{M_1 M_2 g (1 - \mu \cos \theta + \sin \theta)}{M_1 + M_2}. \quad (3.6)$$

In order for  $M_1$  to in fact accelerate downward (that is,  $a < 0$ ), we must have  $M_2 < M_1(\sin \theta - \mu \cos \theta)$ . Therefore, the range of  $M_2$  for which the system doesn't accelerate (that is, it just sits there, assuming that it started at rest) is

$$M_1(\sin \theta - \mu \cos \theta) \leq M_2 \leq M_1(\sin \theta + \mu \cos \theta). \quad (3.7)$$

If  $\mu$  is very small, then  $M_2$  must essentially be equal to  $M_1 \sin \theta$  if the system is to be static. Equation (3.7) also implies that if  $\tan \theta \leq \mu$ , then  $M_1$  won't slide down, even if  $M_2 = 0$ . ♣

---

In problems like the one above, it's clear which things you should pick as the objects you're going to draw forces on. But in other problems, where there are

<sup>5</sup> When dealing with inclined planes, it's usually the case that one of these two coordinate systems works much better than the other. Sometimes it isn't clear which one, but if things get messy with one system, you can always try the other.

various different subsystems you can choose, you must be careful to include all the relevant forces on a given subsystem. Which subsystems you want to pick depends on what quantities you’re trying to find. Consider the following example.

**Example (Platform and pulley):** A person stands on a platform-and-pulley system, as shown in Fig. 3.3. The masses of the platform, person, and pulley<sup>6</sup> are  $M$ ,  $m$ , and  $\mu$ , respectively.<sup>7</sup> The rope is massless. Let the person pull up on the rope so that she has acceleration  $a$  upward. (Assume that the platform is somehow constrained to stay level, perhaps by having the ends run along some rails.) Find the tension in the rope, the normal force between the person and the platform, and the tension in the rod connecting the pulley to the platform.

**Solution:** To find the tension in the rope, we simply want to let our subsystem be the whole system (except the ceiling). If we imagine putting the system in a black box (to emphasize the fact that we don’t care about any internal forces within the system), then the forces we see “protruding” from the box are the three weights ( $Mg$ ,  $mg$ , and  $\mu g$ ) downward, and the tension  $T$  upward. Applying  $F = ma$  to the whole system gives

$$T - (M + m + \mu)g = (M + m + \mu)a \implies T = (M + m + \mu)(g + a). \quad (3.8)$$

To find the normal force  $N$  between the person and the platform, and also the tension  $f$  in the rod connecting the pulley to the platform, it is not sufficient to consider the system as a whole. This is true because these forces are internal forces to this system, so they won’t show up in any  $F = ma$  equations (which involve only external forces to a system). So we must consider subsystems:

- Let’s apply  $F = ma$  to the person. The forces acting on the person are gravity, the normal force from the platform, and the tension from the rope (pulling downward on her hand). So we have

$$N - T - mg = ma. \quad (3.9)$$

- Now apply  $F = ma$  to the platform. The forces acting on the platform are gravity, the normal force from the person, and the force upward from the rod. So we have

$$f - N - Mg = Ma. \quad (3.10)$$

- Now apply  $F = ma$  to the pulley. The forces acting on the pulley are gravity, the force downward from the rod, and *twice* the tension in the rope (because it pulls

![Diagram of a person on a platform with a pulley system.](dc5460bda0c59ba9317dd5ba9b416b0b_img.jpg)

The diagram shows a stick figure representing a person of mass  $m$  standing on a horizontal platform of mass  $M$ . A pulley of mass  $\mu$  is attached to the top of the platform by a vertical rod. A rope is attached to the ceiling, passes under the pulley, and then goes up to the person's hands. An upward arrow labeled  $a$  indicates the acceleration of the person.

Diagram of a person on a platform with a pulley system.

Fig. 3.3

<sup>6</sup> Assume that the pulley’s mass is concentrated at its center, so that we don’t have to worry about any rotational dynamics (the subject of Chapter 8).

<sup>7</sup> My apologies for using  $\mu$  as a mass here, since it usually denotes a coefficient of friction. Alas, there are only so many symbols for “ $m$ .”

up on both sides). So we have

$$2T - f - \mu g = \mu a. \quad (3.11)$$

Note that if we add up the three previous equations, we obtain the  $F = ma$  equation in Eq. (3.8), as should be the case, because the whole system is the sum of the three above subsystems. Equations (3.9)–(3.11) are three equations in the three unknowns,  $T$ ,  $N$ , and  $f$ . Their sum yields the  $T$  in (3.8), and then Eqs. (3.9) and (3.11) give, respectively, as you can show,

$$N = (M + 2m + \mu)(g + a), \quad \text{and} \quad f = (2M + 2m + \mu)(g + a). \quad (3.12)$$

![Free-body diagram of a pulley subsystem. A dashed box encloses a pulley. Two upward arrows from the top of the box are labeled T. A downward arrow from the bottom center of the box is labeled f. A downward arrow from the bottom right of the box is labeled μg.](5860ad6bd2a2dd8d1ab12864b8f90f37_img.jpg)

Free-body diagram of a pulley subsystem. A dashed box encloses a pulley. Two upward arrows from the top of the box are labeled T. A downward arrow from the bottom center of the box is labeled f. A downward arrow from the bottom right of the box is labeled μg.

Fig. 3.4

**REMARKS:** You can also obtain these results by considering subsystems different from the ones we chose above. For example, you can choose the pulley-plus-platform subsystem, etc. But no matter how you choose to break up the system, you will need to produce three independent  $F = ma$  equations in order to solve for the three unknowns,  $T$ ,  $N$ , and  $f$ .

In problems like this one, it's easy to forget to include certain forces, such as the second  $T$  in Eq. (3.11). The safest thing to do is to always isolate each subsystem, draw a box around it, and then draw all the forces that “protrude” from the box. In other words, draw the free-body diagram. Figure 3.4 shows the free-body diagram for the subsystem consisting of only the pulley. ♣

Another class of problems, similar to the above example, goes by the name of *Atwood's machines*. An Atwood's machine is the name used for any system consisting of a combination of masses, strings, and pulleys.<sup>8</sup> In general, the pulleys and strings can have mass, but we'll deal only with massless ones in this chapter. As we'll see in the following example, there are two basic steps in solving an Atwood's problem: (1) write down all the  $F = ma$  equations, and (2) relate the accelerations of the various masses by noting that the length of the string(s) doesn't change, a fact that we call “conservation of string.”

![Diagram of an Atwood's machine. A string is attached to a ceiling support. It passes over a pulley on the left, which has a mass m1 hanging from it. The string then passes under a second pulley on the right, which has a mass m2 hanging from it. The string is then attached back to the ceiling support.](1c94fd3cebf58af136144f14160d128e_img.jpg)

Diagram of an Atwood's machine. A string is attached to a ceiling support. It passes over a pulley on the left, which has a mass m1 hanging from it. The string then passes under a second pulley on the right, which has a mass m2 hanging from it. The string is then attached back to the ceiling support.

Fig. 3.5

**Example (Atwood's machine):** Consider the pulley system in Fig. 3.5, with masses  $m_1$  and  $m_2$ . The strings and pulleys are massless. What are the accelerations of the masses? What is the tension in the string?

**Solution:** The first thing to note is that the tension  $T$  is the same everywhere throughout the massless string, because otherwise there would be an infinite acceleration of some part of the string. It then follows that the tension in the short string connected to  $m_2$  is  $2T$ . This is true because there must be zero net force on the massless right pulley, because otherwise it would have infinite acceleration. The  $F = ma$

<sup>8</sup> George Atwood (1746–1807) was a tutor at Cambridge University. He published the description of the first of his machines in Atwood (1784). For a history of Atwood's machines, see Greenslade (1985).

equations for the two masses are therefore (with upward taken to be positive)

$$\begin{aligned} T - m_1g &= m_1a_1, \\ 2T - m_2g &= m_2a_2. \end{aligned} \quad (3.13)$$

We now have two equations in the three unknowns,  $a_1$ ,  $a_2$ , and  $T$ . So we need one more equation. This is the “conservation of string” fact, which relates  $a_1$  and  $a_2$ . If we imagine moving  $m_2$  and the right pulley up a distance  $d$ , then a length  $2d$  of string has disappeared from the two parts of the string touching the right pulley. This string has to go somewhere, so it ends up in the part of the string touching  $m_1$  (see Fig. 3.6). Therefore,  $m_1$  goes down a distance  $2d$ . In other words,  $y_1 = -2y_2$ , where  $y_1$  and  $y_2$  are measured relative to the initial locations of the masses. Taking two time derivatives of this statement gives our desired relation between  $a_1$  and  $a_2$ ,

$$a_1 = -2a_2. \quad (3.14)$$

Combining this with Eq. (3.13), we can now solve for  $a_1$ ,  $a_2$ , and  $T$ . The result is

$$a_1 = g \frac{2m_2 - 4m_1}{4m_1 + m_2}, \quad a_2 = g \frac{2m_1 - m_2}{4m_1 + m_2}, \quad T = \frac{3m_1m_2g}{4m_1 + m_2}. \quad (3.15)$$

![Diagram of a pulley system. A fixed support at the top holds a pulley. A string is attached to this support, goes down to a pulley (pulley 2) holding mass m2, goes up to a second pulley (pulley 1), and then down to mass m1. The string is also attached to the fixed support at the top. The distance from the fixed support to pulley 1 is labeled 2d. The distance from pulley 1 to pulley 2 is labeled d. The distance from pulley 2 to mass m2 is labeled d. Mass m1 is shown as a solid black circle, and mass m2 is also a solid black circle. Dashed lines indicate the vertical positions of the masses and pulleys.](e2eb8b8c35f32b665245d2c24d337dca_img.jpg)

Diagram of a pulley system. A fixed support at the top holds a pulley. A string is attached to this support, goes down to a pulley (pulley 2) holding mass m2, goes up to a second pulley (pulley 1), and then down to mass m1. The string is also attached to the fixed support at the top. The distance from the fixed support to pulley 1 is labeled 2d. The distance from pulley 1 to pulley 2 is labeled d. The distance from pulley 2 to mass m2 is labeled d. Mass m1 is shown as a solid black circle, and mass m2 is also a solid black circle. Dashed lines indicate the vertical positions of the masses and pulleys.

Fig. 3.6

**REMARKS:** There are all sorts of limits and special cases that we can check here. A couple are: (1) If  $m_2 = 2m_1$ , then Eq. (3.15) gives  $a_1 = a_2 = 0$ , and  $T = m_1g$ . Everything is at rest. (2) If  $m_2 \gg m_1$ , then Eq. (3.15) gives  $a_1 = 2g$ ,  $a_2 = -g$ , and  $T = 3m_1g$ . In this case,  $m_2$  is essentially in free fall, while  $m_1$  gets yanked up with acceleration  $2g$ . The value of  $T$  is exactly what is needed to make the net force on  $m_1$  equal to  $m_1(2g)$ , because  $T - m_1g = 3m_1g - m_1g = m_1(2g)$ . You can check the case where  $m_1 \gg m_2$ .

For the more general case where there are  $N$  masses instead of two, the “conservation of string” statement is a single equation that relates all  $N$  accelerations. It is most easily obtained by imagining moving  $N - 1$  of the masses, each by an arbitrary amount, and then seeing what happens to the last mass. Note that these arbitrary motions undoubtedly do *not* correspond to the actual motions of the masses. This is fine; the single “conservation of string” equation has nothing to do with the  $N F = ma$  equations. The combination of all  $N + 1$  equations is needed to constrain the motions down to a unique set. ♣

In the problems and exercises for this chapter, you will encounter some strange Atwood’s setups. But no matter how complicated they get, there are only two things you need to do to solve them, as mentioned above: write down the  $F = ma$  equations for all the masses (which may involve relating the tensions in various strings), and then relate the accelerations of the masses, using “conservation of string.”

It may seem, with the angst it can bring,  
That an Atwood’s machine’s a cruel thing.  
But you just need to say  
That  $F$  is  $ma$ ,  
And use conservation of string!

## 3.3 Solving differential equations

Let's now consider the type of problem where we are *given* the force as a function of time, position, or velocity, and our task is to solve the  $F = ma \equiv m\ddot{x}$  differential equation to find the position,  $x(t)$ , as a function of time.<sup>9</sup> In what follows, we will develop a few techniques for solving differential equations. The ability to apply these techniques dramatically increases the number of systems we can understand.

It's also possible for the force  $F$  to be a function of higher derivatives of  $x$ , in addition to the quantities  $t$ ,  $x$ , and  $v \equiv \dot{x}$ . But these cases don't arise much, so we won't worry about them. The  $F = ma$  differential equation we want to solve is therefore (we'll just work in one dimension here)

$$m\ddot{x} = F(t, x, v). \quad (3.16)$$

In general, this equation cannot be solved exactly for  $x(t)$ .<sup>10</sup> But for most of the problems we'll deal with, it can be solved. The problems we'll encounter will often fall into one of three special cases, namely, where  $F$  is a function of  $t$  only, or  $x$  only, or  $v$  only. In all of these cases, we must invoke the given initial conditions,  $x_0 \equiv x(t_0)$  and  $v_0 \equiv v(t_0)$ , to obtain our final solutions. These initial conditions will appear in the limits of the integrals in the following discussion.<sup>11</sup>

*Note:* You may want to just skim the following page and a half, and then refer back as needed. Don't try to memorize all the different steps. We present them only for completeness. The whole point here can basically be summarized by saying that sometimes you want to write  $\ddot{x}$  as  $dv/dt$ , and sometimes you want to write it as  $v\,dv/dx$  (see Eq. (3.20)). Then you “simply” have to separate variables and integrate. We'll go through the three special cases, and then we'll do some examples.

- $F$  is a function of  $t$  only:  $F = F(t)$ .

Since  $a = d^2x/dt^2$ , we just need to integrate  $F = ma$  twice to obtain  $x(t)$ . Let's do this in a very systematic way, to get used to the general procedure. First, write  $F = ma$  as

$$m \frac{dv}{dt} = F(t). \quad (3.17)$$

<sup>9</sup> In some setups, such as in Problem 3.11, the force isn't given, so you have to figure out what it is. But the main part of the problem is still solving the resulting differential equation.

<sup>10</sup> You can always solve for  $x(t)$  *numerically*, to any desired accuracy. This topic is discussed in Section 1.4.

<sup>11</sup> It is no coincidence that we need *two* initial conditions to completely specify the solution to our *second-order* (meaning the highest derivative of  $x$  that appears is the second one)  $F = m\ddot{x}$  differential equation. It is a general result (which we'll just accept here) that the solution to an  $n$ th-order differential equation has  $n$  free parameters, which are determined by the initial conditions.

Then separate variables and integrate both sides to obtain<sup>12</sup>

$$m \int_{v_0}^{v(t)} dv' = \int_{t_0}^t F(t') dt'. \quad (3.18)$$

We have put primes on the integration variables so that we don't confuse them with the limits of integration, but in practice we usually don't bother with them. The integral of  $dv'$  is just  $v'$ , so Eq. (3.18) yields  $v$  as a function of  $t$ , that is,  $v(t)$ . We can then separate variables in  $dx/dt \equiv v(t)$  and integrate to obtain

$$\int_{x_0}^{x(t)} dx' = \int_{t_0}^t v(t') dt'. \quad (3.19)$$

This yields  $x$  as a function of  $t$ , that is,  $x(t)$ . This procedure might seem like a cumbersome way to simply integrate something twice. That's because it is. But the technique proves more useful in the following case.

- $F$  is a function of  $x$  only:  $F = F(x)$ .

We will use

$$a = \frac{dv}{dt} = \frac{dx}{dt} \frac{dv}{dx} = v \frac{dv}{dx} \quad (3.20)$$

to write  $F = ma$  as

$$mv \frac{dv}{dx} = F(x). \quad (3.21)$$

Now separate variables and integrate both sides to obtain

$$m \int_{v_0}^{v(x)} v' dv' = \int_{x_0}^x F(x') dx'. \quad (3.22)$$

The integral of  $v'$  is  $v'^2/2$ , so the left-hand side involves the square of  $v(x)$ . Taking the square root, this gives  $v$  as a function of  $x$ , that is,  $v(x)$ . Separating variables in  $dx/dt \equiv v(x)$  then yields

$$\int_{x_0}^{x(t)} \frac{dx'}{v(x')} = \int_{t_0}^t dt'. \quad (3.23)$$

Assuming that we can do the integral on the left-hand side, this equation gives  $t$  as a function of  $x$ . We can then (in principle) invert the result to obtain  $x$  as a function of  $t$ , that is,  $x(t)$ . The unfortunate thing about this case is that the integral in Eq. (3.23) might not be doable. And even if it is, it might not be possible to invert  $t(x)$  to produce  $x(t)$ .

<sup>12</sup> If you haven't seen such a thing before, the act of multiplying both sides by the infinitesimal quantity  $dt$  might make you feel a bit uneasy. But it is in fact quite legal. If you wish, you can imagine working with the small (but not infinitesimal) quantities  $\Delta v$  and  $\Delta t$ , for which it is certainly legal to multiply both sides by  $\Delta t$ . Then you can take a discrete sum over many  $\Delta t$  intervals, and then finally take the limit  $\Delta t \rightarrow 0$ , which results in the integral in Eq. (3.18).

- $F$  is a function of  $v$  only:  $F = F(v)$ .

Write  $F = ma$  as

$$m \frac{dv}{dt} = F(v). \quad (3.24)$$

Separate variables and integrate both sides to obtain

$$m \int_{v_0}^{v(t)} \frac{dv'}{F(v')} = \int_{t_0}^t dt'. \quad (3.25)$$

Assuming that we can do this integral, it yields  $t$  as a function of  $v$ , and hence (in principle)  $v$  as a function of  $t$ , that is,  $v(t)$ . We can then integrate  $dx/dt \equiv v(t)$  to obtain  $x(t)$  from

$$\int_{x_0}^{x(t)} dx' = \int_{t_0}^t v(t') dt'. \quad (3.26)$$

*Note:* In this  $F = F(v)$  case, if we want to find  $v$  as a function of  $x$ ,  $v(x)$ , then we should write  $a$  as  $v(dv/dx)$  and integrate

$$m \int_{v_0}^{v(x)} \frac{v' dv'}{F(v')} = \int_{x_0}^x dx'. \quad (3.27)$$

We can then obtain  $x(t)$  from Eq. (3.23), if desired.

When dealing with the initial conditions, we have chosen to put them in the limits of integration above. If you wish, you can perform the integrals without any limits, and just tack on a constant of integration to your result. The constant is then determined by the initial conditions.

Again, as mentioned above, you do *not* have to memorize the above three procedures, because there are variations, depending on what you're given and what you want to solve for. All you have to remember is that  $\ddot{x}$  can be written as either  $dv/dt$  or  $v dv/dx$ . One of these will get the job done (namely, the one that makes only two of the three variables,  $t$ ,  $x$ , and  $v$ , appear in your differential equation). And then be prepared to separate variables and integrate as many times as needed.<sup>13</sup>

*a* is  $dv$  by  $dt$ .

Is this useful? There's no guarantee.

If it leads to "Oh, heck!"s,

Take  $dv$  by  $dx$ ,

And then write down its product with  $v$ .

<sup>13</sup> We want only two of the variables to appear in the differential equation because the goal is to separate variables and integrate, and because equations have only two sides. If equations were triangles, it would be a different story.

**Example (Gravitational force):** A particle of mass  $m$  is subject to a constant force  $F = -mg$ . The particle starts at rest at height  $h$ . Because this constant force falls into all of the above three categories, we should be able to solve for  $y(t)$  in two ways:

- (a) Find  $y(t)$  by writing  $a$  as  $dv/dt$ .
- (b) Find  $y(t)$  by writing  $a$  as  $v dv/dy$ .

**Solution:**

- (a)  $F = ma$  gives  $dv/dt = -g$ . Multiplying by  $dt$  and integrating yields  $v = -gt + A$ , where  $A$  is a constant of integration.<sup>14</sup> The initial condition  $v(0) = 0$  gives  $A = 0$ . Therefore,  $dy/dt = -gt$ . Multiplying by  $dt$  and integrating yields  $y = -gt^2/2 + B$ . The initial condition  $y(0) = h$  gives  $B = h$ . Therefore,

$$y = h - \frac{1}{2}gt^2. \quad (3.28)$$

- (b)  $F = ma$  gives  $v dv/dy = -g$ . Separating variables and integrating yields  $v^2/2 = -gy + C$ . The initial condition  $v(h) = 0$  gives  $v^2/2 = -gy + gh$ . Therefore,  $v \equiv dy/dt = -\sqrt{2g(h-y)}$ . We have chosen the negative square root because the particle is falling. Separating variables gives

$$\int \frac{dy}{\sqrt{h-y}} = -\sqrt{2g} \int dt. \quad (3.29)$$

This yields  $2\sqrt{h-y} = \sqrt{2g}t$ , where we have used the initial condition  $y(0) = h$ . Hence,  $y = h - gt^2/2$ , as in part (a). In part (b) here, we essentially derived conservation of energy, as we'll see in Chapter 5.

**Example (Dropped ball):** A beach ball is dropped from rest at height  $h$ . Assume that the drag force<sup>15</sup> from the air takes the form of  $F_d = -\beta v$ . Find the velocity and height as a function of time.

**Solution:** For simplicity in future formulas, let's write the drag force as  $F_d = -\beta v \equiv -\alpha v$  (otherwise we'd have a bunch of  $1/m$ 's floating around). Taking upward to be the positive  $y$  direction, the force on the ball is

$$F = -mg - \alpha v. \quad (3.30)$$

<sup>14</sup> We'll do this example by adding on constants of integration which are then determined by the initial conditions. We'll do the following example by putting the initial conditions in the limits of integration.

<sup>15</sup> The drag force is roughly proportional to  $v$  as long as the speed is fairly small (say, less than 10 m/s). For large speeds (say, greater than 100 m/s), the drag force is roughly proportional to  $v^2$ . But these approximate cutoffs depend on various things, and in any event there is a messy transition region between the two cases.

Note that  $v$  is negative here, because the ball is falling, so the drag force points upward, as it should. Writing  $F = m dv/dt$  and separating variables gives

$$\int_0^{v(t)} \frac{dv'}{g + \alpha v'} = - \int_0^t dt'. \quad (3.31)$$

Integration yields  $\ln(1 + \alpha v/g) = -\alpha t$ . Exponentiation then gives

$$v(t) = -\frac{g}{\alpha} (1 - e^{-\alpha t}). \quad (3.32)$$

Writing  $dy/dt \equiv v(t)$ , and then separating variables and integrating to obtain  $y(t)$ , yields

$$\int_h^{y(t)} dy' = -\frac{g}{\alpha} \int_0^t (1 - e^{-\alpha t'}) dt'. \quad (3.33)$$

Therefore,

$$y(t) = h - \frac{g}{\alpha} \left( t - \frac{1}{\alpha} (1 - e^{-\alpha t}) \right). \quad (3.34)$$

#### REMARKS:

1. Let's look at some limiting cases. If  $t$  is very small (more precisely, if  $\alpha t \ll 1$ ), then we can use  $e^{-x} \approx 1 - x + x^2/2$  to make approximations to leading order in  $t$ . You can show that Eq. (3.32) gives  $v(t) \approx -gt$ . This makes sense, because the drag force is negligible at the start, so the ball is essentially in freefall. And likewise you can show that Eq. (3.34) gives  $y(t) \approx h - gt^2/2$ , which is again the freefall result.

We can also look at large  $t$ . In this case,  $e^{-\alpha t}$  is essentially equal to zero, so Eq. (3.32) gives  $v(t) \approx -g/\alpha$ . (This is the “terminal velocity.” Its value makes sense, because it is the velocity for which the total force,  $-mg - m\alpha v$ , vanishes.) And Eq. (3.34) gives  $y(t) \approx h - (g/\alpha)t + g/\alpha^2$ . Interestingly, we see that for large  $t$ ,  $g/\alpha^2$  is the distance our ball lags behind another ball that started out already at the terminal velocity,  $-g/\alpha$ .

2. You might think that the velocity in Eq. (3.32) doesn't depend on  $m$ , since no  $m$ 's appear. However, there is an  $m$  hidden in  $\alpha$ . The quantity  $\alpha$  (which we introduced just to make our formulas look a little nicer) was defined by  $F_d = -\beta v \equiv -m\alpha v$ . But the quantity  $\beta \equiv m\alpha$  is roughly proportional to the cross-sectional area,  $A$ , of the ball. Therefore,  $\alpha \propto A/m$ . Two balls of the same size, one made of lead and one made of styrofoam, have the same  $A$  but different  $m$ 's. So their  $\alpha$ 's are different, and they fall at different rates.

If we have a solid ball with density  $\rho$  and radius  $r$ , then  $\alpha \propto A/m \propto r^2 / (\rho r^3) = 1/\rho r$ . For large dense objects in a thin medium such as air, the quantity  $\alpha$  is small, so the drag effects are not very noticeable over short times (because if we include the next term in the expansion for  $v$ , we obtain  $v(t) \approx -gt + \alpha gt^2/2$ ). Large dense objects therefore all fall at roughly the same rate, with an acceleration essentially equal to  $g$ . But if the air were much thicker, then all the  $\alpha$ 's would be larger, and maybe it would have taken Galileo a bit longer to come to his conclusions.

What would you have thought, Galileo,

If instead you dropped cows and did say, “Oh!

To lessen the sound  
 Of the moos from the ground,  
 They should fall not through air, but through mayo!<sup>16</sup> ♣

## 3.4 Projectile motion

Consider a ball thrown through the air, not necessarily vertically. We will neglect air resistance in the following discussion. Things get a bit more complicated when this is included, as Exercise 3.53 demonstrates.

Let  $x$  and  $y$  be the horizontal and vertical positions, respectively. The force in the  $x$  direction is  $F_x = 0$ , and the force in the  $y$  direction is  $F_y = -mg$ . So  $\mathbf{F} = m\mathbf{a}$  gives

$$\ddot{x} = 0, \quad \text{and} \quad \ddot{y} = -g. \quad (3.35)$$

Note that these two equations are “decoupled.” That is, there is no mention of  $y$  in the equation for  $\ddot{x}$ , and vice versa. The motions in the  $x$  and  $y$  directions are therefore completely independent. The classic demonstration of the independence of the  $x$  and  $y$  motions is the following. Fire a bullet horizontally (or, preferably, just imagine firing a bullet horizontally), and at the same time drop a bullet from the height of the gun. Which bullet will hit the ground first? (Neglect air resistance, the curvature of the earth, etc.) The answer is that they will hit the ground at the same time, because the effect of gravity on the two  $y$  motions is exactly the same, independent of what is going on in the  $x$  direction.

If the initial position and velocity are  $(X, Y)$  and  $(V_x, V_y)$ , then we can easily integrate Eq. (3.35) to obtain

$$\dot{x}(t) = V_x, \quad \text{and} \quad \dot{y}(t) = V_y - gt. \quad (3.36)$$

Integrating again gives

$$x(t) = X + V_x t, \quad \text{and} \quad y(t) = Y + V_y t - \frac{1}{2}gt^2. \quad (3.37)$$

These equations for the speeds and positions are all you need to solve a projectile problem.

<sup>16</sup> It's actually much more likely that Galileo obtained his “all objects fall at the same rate in a vacuum” result by rolling balls down planes than by dropping balls from the Tower of Pisa; see Adler and Coulter (1978). So I suppose this limerick is relevant only in the approximation of the proverbial spherical cow.

### **Example (Throwing a ball):**

- (a) For a given initial speed, at what inclination angle should a ball be thrown so that it travels the maximum horizontal distance by the time it returns to the ground? Assume that the ground is horizontal, and that the ball is released from ground level.
- (b) What is the optimal angle if the ground is sloped upward at an angle  $\beta$  (or downward, if  $\beta$  is negative)?

#### **Solution:**

- (a) Let the inclination angle be  $\theta$ , and let the initial speed be  $V$ . Then the horizontal speed is always  $V_x = V \cos \theta$ , and the initial vertical speed is  $V_y = V \sin \theta$ . The first thing we need to do is find the time  $t$  in the air. We know that the vertical speed is zero at time  $t/2$ , because the ball is moving horizontally at the highest point. So the second of Eqs. (3.36) gives  $V_y = g(t/2)$ . Therefore,  $t = 2V_y/g$ .<sup>17</sup> The first of Eqs. (3.37) tells us that the horizontal distance traveled is  $d = V_x t$ . Using  $t = 2V_y/g$  in this gives

$$d = \frac{2V_x V_y}{g} = \frac{V^2(2 \sin \theta \cos \theta)}{g} = \frac{V^2 \sin 2\theta}{g}. \quad (3.38)$$

The  $\sin 2\theta$  factor has a maximum at  $\theta = \pi/4$ . The maximum horizontal distance traveled is then  $d_{\max} = V^2/g$ .

**REMARK:** For  $\theta = \pi/4$ , you can show that the maximum height achieved is  $V^2/4g$ . This is half the maximum height of  $V^2/2g$  (as you can show) if the ball is thrown straight up. Note that any possible distance you might want to find in this problem must be proportional to  $V^2/g$ , by dimensional analysis. The only question is what the numerical factor is. ♣

- (b) As in part (a), the first thing we need to do is find the time  $t$  in the air. If the ground is sloped at an angle  $\beta$ , then the equation for the line of the ground is  $y = (\tan \beta)x$ . The path of the ball is given in terms of  $t$  by

$$x = (V \cos \theta)t, \quad \text{and} \quad y = (V \sin \theta)t - \frac{1}{2}gt^2, \quad (3.39)$$

where  $\theta$  is the angle of the throw, as measured with respect to the horizontal (not the ground). We must solve for the  $t$  that makes  $y = (\tan \beta)x$ , because this gives the time when the path of the ball intersects the line of the ground. Using Eq. (3.39), we find that  $y = (\tan \beta)x$  when

$$t = \frac{2V}{g}(\sin \theta - \tan \beta \cos \theta). \quad (3.40)$$

<sup>17</sup> Alternatively, the time of flight can be found from the second of Eqs. (3.37), which says that the ball returns to the ground when  $V_y t = gt^2/2$ . We will have to use this second strategy in part (b), where the trajectory is not symmetric around the maximum.

(There is, of course, also the solution  $t = 0$ .) Plugging this into the expression for  $x$  in Eq. (3.39) gives

$$x = \frac{2V^2}{g} (\sin \theta \cos \theta - \tan \beta \cos^2 \theta). \quad (3.41)$$

We must now maximize this value for  $x$ , which is equivalent to maximizing the distance along the slope. Setting the derivative with respect to  $\theta$  equal to zero, and using the double-angle formulas,  $\sin 2\theta = 2 \sin \theta \cos \theta$  and  $\cos 2\theta = \cos^2 \theta - \sin^2 \theta$ , we find  $\tan \beta = -\cot 2\theta$ . This can be rewritten as  $\tan \beta = -\tan(\pi/2 - 2\theta)$ . Therefore,  $\beta = -(\pi/2 - 2\theta)$ , so we have

$$\theta = \frac{1}{2} \left( \beta + \frac{\pi}{2} \right). \quad (3.42)$$

In other words, the throwing angle should bisect the angle between the ground and the vertical.

#### REMARKS:

1. For  $\beta \approx \pi/2$ , we have  $\theta \approx \pi/2$ , as should be the case. For  $\beta = 0$ , we have  $\theta = \pi/4$ , as we found in part (a). And for  $\beta \approx -\pi/2$ , we have  $\theta \approx 0$ , which makes sense.
2. A quicker method of obtaining the time in Eq. (3.40) is the following. Consider the set of tilted axes parallel and perpendicular to the ground; let these be the  $x'$  and  $y'$  axes, respectively. The initial velocity in the  $y'$  direction is  $V \sin(\theta - \beta)$ , and the acceleration in this direction is  $g \cos \beta$ . The time in the air is twice the time it takes the ball to reach the maximum “height” above the ground (measured in the  $y'$  direction), which occurs when the velocity in the  $y'$  direction is instantaneously zero. The total time is therefore  $2V \sin(\theta - \beta)/(g \cos \beta)$ , which you can show is equivalent to the time in Eq. (3.40). Note that the  $g \sin \beta$  acceleration in the  $x'$  direction is irrelevant in calculating this time. In the present example, using these tilted axes doesn’t save a huge amount of time, but in some situations (see Exercise 3.50) the tilted axes can save you a lot of grief.
3. An interesting fact about the motion of the ball in the maximum-distance case is that the initial and final velocities are perpendicular to each other. The demonstration of this is the task of Problem 3.16.
4. Substituting the value of  $\theta$  from Eq. (3.42) into Eq. (3.41), you can show (after a bit of algebra) that the maximum distance traveled along the tilted ground is

$$d = \frac{x}{\cos \beta} = \frac{V^2/g}{1 + \sin \beta}. \quad (3.43)$$

Solving for  $V$ , we have  $V^2 = g(d + d \sin \beta)$ . This can be interpreted as saying that the minimum speed at which a ball must be thrown in order to pass over a wall of height  $h$ , at a distance  $L$  away on level ground, is given by  $V^2 = g(\sqrt{L^2 + h^2} + h)$ . This checks in the limits of  $h \rightarrow 0$  and  $L \rightarrow 0$ .

5. A compilation of many other projectile results can be found in Buckmaster (1985). ♣

Along with the bullet example mentioned above, another classic example of the independence of the  $x$  and  $y$  motions is the “hunter and monkey” problem. In it, a hunter aims an arrow (a toy one, of course) at a monkey hanging from a branch in a tree. The monkey, thinking he’s being clever, tries to avoid the arrow by letting go of the branch right when he sees the arrow released. The unfortunate consequence of this action is that he in fact *will* get hit, because gravity acts on both him and the arrow in the same way; they both fall the same distance relative to where they would have been if there were no gravity. And the monkey *would* get hit in such a case, because the arrow is initially aimed at him. You can work this out in Exercise 3.44, in a more peaceful setting involving fruit.

If a monkey lets go of a tree,  
 The arrow will hit him, you see,  
 Because both heights are pared  
 By a half  $gt^2$   
 From what they would be with no  $g$ .

![Figure 3.7: A diagram showing a point in a 2D Cartesian coordinate system. A vector of length r is drawn from the origin to the point. The angle between the positive x-axis and the vector is labeled theta. A dashed vertical line connects the point to the x-axis, and its length is labeled y.](ef25c3cf1fdb334fc8679e85ab5265ca_img.jpg)

Figure 3.7: A diagram showing a point in a 2D Cartesian coordinate system. A vector of length r is drawn from the origin to the point. The angle between the positive x-axis and the vector is labeled theta. A dashed vertical line connects the point to the x-axis, and its length is labeled y.

Fig. 3.7

## 3.5 Motion in a plane, polar coordinates

When dealing with problems where the motion lies in a plane, it is often convenient to work with polar coordinates,  $r$  and  $\theta$ . These are related to the Cartesian coordinates by (see Fig. 3.7)

$$x = r \cos \theta, \quad \text{and} \quad y = r \sin \theta. \quad (3.44)$$

Depending on the problem, either Cartesian or polar coordinates are easier to use. It is usually clear from the setup which is better. For example, if the problem involves circular motion, then polar coordinates are a good bet. But to use polar coordinates, we need to know what Newton’s second law looks like when written in terms of them. Therefore, the goal of the present section is to determine what  $\mathbf{F} = m\mathbf{a} \equiv m\ddot{\mathbf{r}}$  looks like when written in terms of polar coordinates.

At a given position  $\mathbf{r}$  in the plane, the basis vectors in polar coordinates are  $\hat{\mathbf{r}}$ , which is a unit vector pointing in the radial direction; and  $\hat{\boldsymbol{\theta}}$ , which is a unit vector pointing in the counterclockwise tangential direction. In polar coordinates, a general vector may be written as

$$\mathbf{r} = r\hat{\mathbf{r}}. \quad (3.45)$$

Since the goal of this section is to find  $\ddot{\mathbf{r}}$ , we must, in view of Eq. (3.45), get a handle on the time derivative of  $\hat{\mathbf{r}}$ . And we’ll eventually need the derivative of  $\hat{\boldsymbol{\theta}}$ , too. In contrast with the fixed Cartesian basis vectors ( $\hat{\mathbf{x}}$  and  $\hat{\mathbf{y}}$ ), the polar basis vectors ( $\hat{\mathbf{r}}$  and  $\hat{\boldsymbol{\theta}}$ ) change as a point moves around in the plane. We can

find  $\dot{\mathbf{r}}$  and  $\dot{\hat{\theta}}$  in the following way. In terms of the Cartesian basis, Fig. 3.8 shows that

$$\begin{aligned}\hat{\mathbf{r}} &= \cos \theta \hat{\mathbf{x}} + \sin \theta \hat{\mathbf{y}}, \\ \hat{\hat{\theta}} &= -\sin \theta \hat{\mathbf{x}} + \cos \theta \hat{\mathbf{y}}.\end{aligned}\quad (3.46)$$

![Figure 3.8: A diagram showing a circle centered at the origin of a Cartesian coordinate system (x, y). A vector r points from the origin to a point on the circle at an angle theta from the positive x-axis. Two unit vectors are shown: r-hat, which points in the same direction as r, and theta-hat, which is perpendicular to r-hat and points counter-clockwise. The components of r-hat are cos(theta) along the x-axis and sin(theta) along the y-axis. The components of theta-hat are -sin(theta) along the x-axis and cos(theta) along the y-axis. Dashed lines indicate these projections.](8935d7297fc189503125ecbbd7c41f27_img.jpg)

Figure 3.8: A diagram showing a circle centered at the origin of a Cartesian coordinate system (x, y). A vector r points from the origin to a point on the circle at an angle theta from the positive x-axis. Two unit vectors are shown: r-hat, which points in the same direction as r, and theta-hat, which is perpendicular to r-hat and points counter-clockwise. The components of r-hat are cos(theta) along the x-axis and sin(theta) along the y-axis. The components of theta-hat are -sin(theta) along the x-axis and cos(theta) along the y-axis. Dashed lines indicate these projections.

Fig. 3.8

Taking the time derivative of these equations gives

$$\begin{aligned}\dot{\mathbf{r}} &= -\sin \theta \dot{\theta} \hat{\mathbf{x}} + \cos \theta \dot{\theta} \hat{\mathbf{y}}, \\ \dot{\hat{\theta}} &= -\cos \theta \dot{\theta} \hat{\mathbf{x}} - \sin \theta \dot{\theta} \hat{\mathbf{y}}.\end{aligned}\quad (3.47)$$

Using Eq. (3.46), we arrive at the nice clean expressions,

$$\dot{\mathbf{r}} = \dot{\theta} \hat{\hat{\theta}}, \quad \text{and} \quad \dot{\hat{\theta}} = -\dot{\theta} \hat{\mathbf{r}}. \quad (3.48)$$

These relations are fairly evident if you look at what happens to the basis vectors as  $\mathbf{r}$  moves a tiny distance in the tangential direction. Note that the basis vectors do not change as  $\mathbf{r}$  moves in the radial direction. We can now start differentiating Eq. (3.45). One derivative gives (yes, the product rule works fine here)

$$\dot{\mathbf{r}} = \dot{r} \hat{\mathbf{r}} + r \dot{\mathbf{r}} = \dot{r} \hat{\mathbf{r}} + r \dot{\theta} \hat{\hat{\theta}}. \quad (3.49)$$

This makes sense, because  $\dot{r}$  is the velocity in the radial direction, and  $r\dot{\theta}$  is the velocity in the tangential direction, often written as  $r\omega$  (where  $\omega \equiv \dot{\theta}$  is the angular velocity, or “angular frequency”).<sup>18</sup> Differentiating Eq. (3.49) then gives

$$\begin{aligned}\ddot{\mathbf{r}} &= \ddot{r} \hat{\mathbf{r}} + \dot{r} \dot{\mathbf{r}} + \dot{r} \dot{\theta} \hat{\hat{\theta}} + r \ddot{\theta} \hat{\hat{\theta}} + r \dot{\theta} \dot{\hat{\theta}} \\ &= \ddot{r} \hat{\mathbf{r}} + \dot{r}(\dot{\theta} \hat{\hat{\theta}}) + \dot{r} \dot{\theta} \hat{\hat{\theta}} + r \ddot{\theta} \hat{\hat{\theta}} + r \dot{\theta}(-\dot{\theta} \hat{\mathbf{r}}) \\ &= (\ddot{r} - r \dot{\theta}^2) \hat{\mathbf{r}} + (r \ddot{\theta} + 2\dot{r} \dot{\theta}) \hat{\hat{\theta}}.\end{aligned}\quad (3.50)$$

Finally, equating  $m\ddot{\mathbf{r}}$  with  $\mathbf{F} \equiv F_r \hat{\mathbf{r}} + F_\theta \hat{\hat{\theta}}$  gives the radial and tangential forces as

$$\begin{aligned}F_r &= m(\ddot{r} - r \dot{\theta}^2), \\ F_\theta &= m(r \ddot{\theta} + 2\dot{r} \dot{\theta}).\end{aligned}\quad (3.51)$$

(See Exercise 3.67 for a slightly different derivation of these equations.) Let’s look at each of the four terms on the right-hand sides of Eqs. (3.51).

- The  $m\ddot{r}$  term is quite intuitive. For radial motion, it simply states that  $F = ma$  along the radial direction.

<sup>18</sup> For  $r\dot{\theta}$  to be the tangential velocity, we must measure  $\theta$  in radians and not degrees. Then  $r\theta$  is by definition the position along the circumference, so  $r\dot{\theta}$  is the velocity along the circumference.

- The  $mr\ddot{\theta}$  term is also quite intuitive. For circular motion, it states that  $F = ma$  along the tangential direction, because  $r\ddot{\theta}$  is the second derivative of the distance  $r\theta$  along the circumference.
- The  $-mr\dot{\theta}^2$  term is also fairly clear. For circular motion, it says that the radial force is  $-m(r\dot{\theta})^2/r = -mv^2/r$ , which is the familiar force that causes the centripetal acceleration,  $v^2/r$ . See Problem 3.20 for an alternate (and quicker) derivation of this  $v^2/r$  result.
- The  $2m\dot{r}\dot{\theta}$  term isn't so obvious. It is associated with the *Coriolis* force. There are various ways to look at this term. One is that it exists in order to keep angular momentum conserved. We'll have a great deal to say about the Coriolis force in Chapter 10.

![Diagram of a circular pendulum. A mass m is suspended by a string of length l from a fixed horizontal support. The string makes a constant angle beta with the vertical. The mass moves in a horizontal circle, indicated by a dashed ellipse and a curved arrow showing the direction of motion.](63c666b05041841b01fdef9fa4153ff7_img.jpg)

Diagram of a circular pendulum. A mass m is suspended by a string of length l from a fixed horizontal support. The string makes a constant angle beta with the vertical. The mass moves in a horizontal circle, indicated by a dashed ellipse and a curved arrow showing the direction of motion.

Fig. 3.9

**Example (Circular pendulum):** A mass hangs from a massless string of length  $\ell$ . Conditions have been set up so that the mass swings around in a horizontal circle, with the string making a constant angle  $\beta$  with the vertical (see Fig. 3.9). What is the angular frequency,  $\omega$ , of this motion?

**Solution:** The mass travels in a circle, so the horizontal radial force must be  $F_r = mr\dot{\theta}^2 \equiv m\omega^2$  (with  $r = \ell \sin \beta$ ), directed radially inward. The forces on the mass are the tension in the string,  $T$ , and gravity,  $mg$  (see Fig. 3.10). There is no acceleration in the vertical direction, so  $F = ma$  in the vertical and radial directions gives, respectively,

$$\begin{aligned} T \cos \beta - mg &= 0, \\ T \sin \beta &= m(\ell \sin \beta)\omega^2. \end{aligned} \quad (3.52)$$

Solving for  $\omega$  gives

$$\omega = \sqrt{\frac{g}{\ell \cos \beta}}. \quad (3.53)$$

If  $\beta \approx 90^\circ$ , then  $\omega \rightarrow \infty$ , which makes sense. And if  $\beta \approx 0$ , then  $\omega \approx \sqrt{g/\ell}$ , which happens to equal the frequency of a plane pendulum of length  $\ell$ . The task of Exercise 3.60 is to explain why.

![Free-body diagram of the circular pendulum. The mass m is shown with two forces acting on it: tension T, directed along the string at an angle beta from the vertical, and gravity mg, directed vertically downward.](a251a846ffb8c1750262be87b489eeec_img.jpg)

Free-body diagram of the circular pendulum. The mass m is shown with two forces acting on it: tension T, directed along the string at an angle beta from the vertical, and gravity mg, directed vertically downward.

Fig. 3.10

![Diagram of Atwood's machine. A massless pulley is suspended from a fixed horizontal support. A massless string passes over the pulley, with two masses, m1 and m2, hanging from its ends.](a7b0ce8ddbb18a80bb6f57334023059d_img.jpg)

Diagram of Atwood's machine. A massless pulley is suspended from a fixed horizontal support. A massless string passes over the pulley, with two masses, m1 and m2, hanging from its ends.

Fig. 3.11

## 3.6 Problems

## Section 3.2: Free-body diagrams

### 3.1. Atwood's machine \*

A massless pulley hangs from a fixed support. A massless string connecting two masses,  $m_1$  and  $m_2$ , hangs over the pulley (see Fig. 3.11). Find the acceleration of the masses and the tension in the string.

### 3.2. **Double Atwood's machine \*\***

A double Atwood's machine is shown in Fig. 3.12, with masses  $m_1$ ,  $m_2$ , and  $m_3$ . Find the accelerations of the masses.

![Diagram of a double Atwood's machine. A string is attached to a ceiling, passes over a top pulley, and then splits into two branches. The left branch has a mass m1. The right branch passes over a second pulley and has masses m2 and m3 hanging from its ends.](cc777601b892d144a2c0b69f56ef03bf_img.jpg)

Diagram of a double Atwood's machine. A string is attached to a ceiling, passes over a top pulley, and then splits into two branches. The left branch has a mass m1. The right branch passes over a second pulley and has masses m2 and m3 hanging from its ends.

Fig. 3.12

### 3.3. **Infinite Atwood's machine \*\*\***

Consider the infinite Atwood's machine shown in Fig. 3.13. A string passes over each pulley, with one end attached to a mass and the other end attached to another pulley. All the masses are equal to  $m$ , and all the pulleys and strings are massless. The masses are held fixed and then simultaneously released. What is the acceleration of the top mass? (You may define this infinite system as follows. Consider it to be made of  $N$  pulleys, with a nonzero mass replacing what would have been the  $(N + 1)$ th pulley. Then take the limit as  $N \rightarrow \infty$ .)

![Diagram of an infinite Atwood's machine. A top pulley is suspended from a ceiling. A string passes over it, with a mass m on the left and another pulley on the right. This pattern repeats, with each pulley having a mass m on one side and another pulley on the other side. The diagram shows the first three levels and ends with an ellipsis.](8c88a2b2e156c28098d47bdd093e67e0_img.jpg)

Diagram of an infinite Atwood's machine. A top pulley is suspended from a ceiling. A string passes over it, with a mass m on the left and another pulley on the right. This pattern repeats, with each pulley having a mass m on one side and another pulley on the other side. The diagram shows the first three levels and ends with an ellipsis.

Fig. 3.13

### 3.4. **Line of pulleys \***

$N + 2$  equal masses hang from a system of pulleys, as shown in Fig. 3.14. What are the accelerations of all the masses?

![Diagram of a line of pulleys. A horizontal string is attached to a ceiling at both ends. It passes under a series of pulleys. There are three pulleys shown, each with a mass hanging from it. The string passes over the top of each pulley. The label N=3 is below the diagram.](0a522c7f4d133c9242b6e250f77d8e9b_img.jpg)

Diagram of a line of pulleys. A horizontal string is attached to a ceiling at both ends. It passes under a series of pulleys. There are three pulleys shown, each with a mass hanging from it. The string passes over the top of each pulley. The label N=3 is below the diagram.

Fig. 3.14

### 3.5. **Ring of pulleys \*\***

Consider the system of pulleys shown in Fig. 3.15. The string (which is a loop with no ends) hangs over  $N$  fixed pulleys that circle around the underside of a ring.  $N$  masses,  $m_1, m_2, \dots, m_N$ , are attached to  $N$  pulleys that hang on the string. What are the accelerations of all the masses?

![Diagram of a ring of pulleys. A large ring is suspended from a ceiling. A continuous string loop passes over the underside of the ring. Hanging from the string are several pulleys, each with a mass attached. The masses are labeled mN, m1, m2, and there are ellipses indicating more masses.](906b2c6ba479621b00429a51cbcce897_img.jpg)

Diagram of a ring of pulleys. A large ring is suspended from a ceiling. A continuous string loop passes over the underside of the ring. Hanging from the string are several pulleys, each with a mass attached. The masses are labeled mN, m1, m2, and there are ellipses indicating more masses.

Fig. 3.15

### 3.6. **Sliding down a plane \*\***

- A block starts at rest and slides down a frictionless plane inclined at an angle  $\theta$ . What should  $\theta$  be so that the block travels a given horizontal distance in the minimum amount of time?
- Same question, but now let there be a coefficient of kinetic friction  $\mu$  between the block and the plane.

### 3.7. **Sliding sideways on a plane \*\*\***

A block is placed on a plane inclined at an angle  $\theta$ . The coefficient of friction between the block and the plane is  $\mu = \tan \theta$ . The block is given a kick so that it initially moves with speed  $V$  horizontally along the plane (that is, in the direction perpendicular to the direction pointing straight down the plane). What is the speed of the block after a very long time?

### 3.8. **Moving plane \*\*\***

A block of mass  $m$  is held motionless on a frictionless plane of mass  $M$  and angle of inclination  $\theta$  (see Fig. 3.16). The plane rests on a frictionless horizontal surface. The block is released. What is the horizontal acceleration of the plane?

![Diagram of a block on a moving plane. A block of mass m is on an inclined plane of mass M. The plane is on a horizontal surface and is accelerating to the left, as indicated by an arrow. The angle of inclination is theta.](d8849b6b8f23b67e6c7f86bd39bf4552_img.jpg)

Diagram of a block on a moving plane. A block of mass m is on an inclined plane of mass M. The plane is on a horizontal surface and is accelerating to the left, as indicated by an arrow. The angle of inclination is theta.

Fig. 3.16

## Section 3.3: Solving differential equations

### 3.9. Exponential force \*

A particle of mass  $m$  is subject to a force  $F(t) = ma_0 e^{-bt}$ . The initial position and speed are zero. Find  $x(t)$ .

### 3.10. $-kx$ force \*\*

A particle of mass  $m$  is subject to a force  $F(x) = -kx$ , with  $k > 0$ . The initial position is  $x_0$ , and the initial speed is zero. Find  $x(t)$ .

### 3.11. Falling chain \*\*

A chain with length  $\ell$  is held stretched out on a frictionless horizontal table, with a length  $y_0$  hanging down through a hole in the table. The chain is released. As a function of time, find the length that hangs down through the hole (don't bother with  $t$  after the chain loses contact with the table). Also, find the speed of the chain right when it loses contact with the table.<sup>19</sup>

### 3.12. Throwing a beach ball \*\*\*

A beach ball is thrown upward with initial speed  $v_0$ . Assume that the drag force from the air is  $F_d = -m\alpha v$ . What is the speed of the ball,  $v_f$ , right before it hits the ground? (An implicit equation is sufficient.) Does the ball spend more time or less time in the air than it would if it were thrown in vacuum?

### 3.13. Balancing a pencil \*\*\*

Consider a pencil that stands upright on its tip and then falls over. Let's idealize the pencil as a mass  $m$  sitting at the end of a massless rod of length  $\ell$ .<sup>20</sup>

- (a) Assume that the pencil makes an initial (small) angle  $\theta_0$  with the vertical, and that its initial angular speed is  $\omega_0$ . The angle will eventually become large, but while it is small (so that  $\sin \theta \approx \theta$ ), what is  $\theta$  as a function of time?
- (b) You might think that it should be possible (theoretically, at least) to make the pencil balance for an arbitrarily long time, by making the initial  $\theta_0$  and  $\omega_0$  sufficiently small. However, it turns out that due to Heisenberg's uncertainty principle (which puts a constraint on how well we can know the position and momentum of

<sup>19</sup> Assume that the hole is actually a short frictionless tube bent into a gradual right angle, so that the chain's horizontal momentum doesn't cause it to overshoot the hole. For a description of what happens in a similar problem when this constraint is removed, see Calkin (1989).

<sup>20</sup> It actually involves only a trivial modification to do the problem correctly using the moment of inertia and the torque. But the point-mass version is quite sufficient for the present purposes.

a particle), it is impossible to balance the pencil for more than a certain amount of time. The point is that you can't be sure that the pencil is initially both at the top *and* at rest. The goal of this problem is to be quantitative about this. The time limit is sure to surprise you.

Without getting into quantum mechanics, let's just say that the uncertainty principle says (up to factors of order 1) that  $\Delta x \Delta p \geq \hbar$ , where  $\hbar = 1.05 \cdot 10^{-34}$  J s is Planck's constant. The implications of this are somewhat vague, but we'll just take it to mean that the initial conditions satisfy  $(\ell\theta_0)(m\ell\omega_0) \geq \hbar$ . With this constraint, your task is to find the maximum time it can take your  $\theta(t)$  solution in part (a) to become of order 1. In other words, determine (roughly) the maximum time the pencil can balance. Assume  $m = 0.01$  kg, and  $\ell = 0.1$  m.

## Section 3.4: Projectile motion

### 3.14. Maximum trajectory area \*

A ball is thrown at speed  $v$  from zero height on level ground. At what angle should it be thrown so that the area under the trajectory is maximum?

### 3.15. Bouncing ball \*

A ball is thrown straight upward so that it reaches a height  $h$ . It falls down and bounces repeatedly. After each bounce, it returns to a certain fraction  $f$  of its previous height. Find the total distance traveled, and also the total time, before it comes to rest. What is its average speed?

### 3.16. Perpendicular velocities \*\*

In the maximum-distance case in part (b) of the example in Section 3.4, show that the initial and final velocities are perpendicular to each other.<sup>21</sup>

### 3.17. Throwing a ball from a cliff \*\*

A ball is thrown with speed  $v$  from the edge of a cliff of height  $h$ . At what inclination angle should it be thrown so that it travels the maximum horizontal distance? What is this maximum distance? Assume that the ground below the cliff is horizontal.

<sup>21</sup> You can grind through this problem and explicitly find the final angle, but there's a quicker way. This quicker method makes use of the conservation-of-energy statement that the difference in the squares of the initial and final speeds depends only on the change in height (the relation happens to be  $v_i^2 - v_f^2 = 2gh$ , but you don't need this actual expression). *Hint:* Consider the reverse path.

### **3.18. Redirected motion \*\***

A ball is dropped from rest at height  $h$  above level ground, and it bounces off a surface at height  $y$  (with no loss in speed). The surface is inclined so that the ball bounces off at an angle  $\theta$  with respect to the horizontal. What should  $y$  and  $\theta$  be so that the ball travels the maximum horizontal distance by the time it hits the ground?

### **3.19. Maximum trajectory length \*\*\***

A ball is thrown at speed  $v$  from zero height on level ground. Let  $\theta_0$  be the angle at which the ball should be thrown so that the length of the trajectory is maximum. Show that  $\theta_0$  satisfies

$$\sin \theta_0 \ln \left( \frac{1 + \sin \theta_0}{\cos \theta_0} \right) = 1. \quad (3.54)$$

You can show numerically that  $\theta_0 \approx 56.5^\circ$ .

## *Section 3.5: Motion in a plane, polar coordinates*

### **3.20. Centripetal acceleration \***

Show that the magnitude of the acceleration of a particle moving in a circle is  $v^2/r$ . Do this by drawing the position and velocity vectors at two nearby times, and then making use of some similar triangles.

### **3.21. Vertical acceleration \*\***

A bead rests at the top of a fixed frictionless hoop of radius  $R$  that lies in a vertical plane. The bead is given a tiny push so that it slides down and around the hoop. At what points on the hoop is the bead's acceleration vertical?<sup>22</sup> What is this vertical acceleration? *Note:* We haven't studied conservation of energy yet, but use the fact that the bead's speed after it has fallen a height  $h$  is given by  $v = \sqrt{2gh}$ .

### **3.22. Circling around a pole \*\***

A mass, which is free to move on a horizontal frictionless surface, is attached to one end of a massless string that wraps partially around a frictionless vertical pole of radius  $r$  (see the top view in Fig. 3.17). You hold on to the other end of the string. At  $t = 0$ , the mass has speed  $v_0$  in the tangential direction along the dotted circle of radius  $R$  shown. Your task is to pull on the string so that the mass keeps moving along the

![Diagram showing a top view of a mass moving in a circular path around a central pole. The pole is a shaded circle of radius r. The mass is a black dot on a dashed circle of radius R. A string connects the mass to a hand at the bottom right. Arrows indicate the direction of motion along the dashed circle.](d63dcf9b188f03572093f2f604d7b8ed_img.jpg)

Diagram showing a top view of a mass moving in a circular path around a central pole. The pole is a shaded circle of radius r. The mass is a black dot on a dashed circle of radius R. A string connects the mass to a hand at the bottom right. Arrows indicate the direction of motion along the dashed circle.

**Fig. 3.17**

<sup>22</sup> One such point is the bottom of the hoop. Another point is technically the top, where  $a \approx 0$ . Find the other two more interesting points (one on each side).

dotted circle. You are required to do this in such a way that the string remains in contact with the pole at all times. (You will have to move your hand around the pole, of course.) What is the speed of the mass as a function of time? There is a special value of the time; what is it and why is it special?

### 3.23. **A force $F_\theta = m\dot{r}\dot{\theta}$ \*\***

Consider a particle that feels an angular force only, of the form  $F_\theta = m\dot{r}\dot{\theta}$ . Show that  $\dot{r} = \sqrt{A \ln r + B}$ , where  $A$  and  $B$  are constants of integration, determined by the initial conditions. (There's nothing all that physical about this force. It simply makes the  $F = ma$  equations solvable.)

### 3.24. **Free particle \*\*\***

Consider a free particle in a plane. With Cartesian coordinates, it is easy to use  $F = ma$  to show that the particle moves in a straight line. The task of this problem is to demonstrate this result in a much more cumbersome way, using polar coordinates and Eq. (3.51). More precisely, show that  $\cos \theta = r_0/r$  for a free particle, where  $r_0$  is the radius at closest approach to the origin, and  $\theta$  is measured with respect to this radius.

![Diagram of a pulley system with masses m, m/2, m/4, and m/2^{n-1}.](8d325fc12b494e42c9ea7ed2a7f327a6_img.jpg)

A vertical pulley system. A string is attached to a ceiling, goes down around a pulley with mass  $m$ , up around a second pulley with mass  $m/2$ , down around a third pulley with mass  $m/4$ , and finally up to a fourth pulley with mass  $m/2^{n-1}$ . The string ends at a small open circle labeled with a question mark.

Diagram of a pulley system with masses m, m/2, m/4, and m/2^{n-1}.

Fig. 3.18

### 3.7 Exercises

## Section 3.2: Free-body diagrams

### 3.25. **A peculiar Atwood's machine**

- (a) The Atwood's machine in Fig. 3.18 consists of  $n$  masses,  $m, m/2, m/4, \dots, m/2^{n-1}$ . All the pulleys and strings are massless. Put a mass  $m/2^{n-1}$  at the free end of the bottom string. What are the accelerations of all the masses?
- (b) Remove the mass  $m/2^{n-1}$  (which was arbitrarily small, for very large  $n$ ) that was attached in part (a). What are the accelerations of all the masses, now that you've removed this infinitesimal piece?

![Diagram of an Atwood's machine with masses M, m1, and m2.](c8e5b3ef81948bb13d5c6c3c326799ea_img.jpg)

An Atwood's machine. A string is attached to a ceiling, goes down around a pulley with mass  $M$ , and then splits into two separate vertical strings, each supporting a mass:  $m_1$  on the left and  $m_2$  on the right.

Diagram of an Atwood's machine with masses M, m1, and m2.

Fig. 3.19

### 3.26. **Keeping the mass still \***

In the Atwood's machine in Fig. 3.19, what should  $M$  be, in terms of  $m_1$  and  $m_2$ , so that it doesn't move?

### 3.27. **Atwood's 1 \***

Consider the Atwood's machine in Fig. 3.20. It consists of three pulleys, a short piece of string connecting one mass to the bottom pulley, and a continuous long piece of string that wraps twice around the bottom

![Diagram of a complex pulley system with masses m and 2m.](8f97292132f64747f6ce17984bba1bf5_img.jpg)

A complex pulley system. A string is attached to a ceiling, goes down around a pulley with mass  $m$ , up around a second pulley, down around a third pulley with mass  $2m$ , and finally up to the ceiling. A short string connects the mass  $m$  to the bottom pulley.

Diagram of a complex pulley system with masses m and 2m.

Fig. 3.20

![Diagram of an Atwood's machine (Fig. 3.21). A string is attached to a ceiling, goes down around a pulley with mass m, up around another pulley, down around a third pulley with mass m, and finally up to the ceiling. The string is continuous and passes under all three pulleys.](0ccbf2e1f1d9d0aae8865d824a1fc322_img.jpg)

Diagram of an Atwood's machine (Fig. 3.21). A string is attached to a ceiling, goes down around a pulley with mass m, up around another pulley, down around a third pulley with mass m, and finally up to the ceiling. The string is continuous and passes under all three pulleys.

Fig. 3.21

![Diagram of an Atwood's machine (Fig. 3.22). A string is attached to a ceiling, goes down around a pulley with mass m, up around another pulley, down around a third pulley with mass 2m, and finally up around a fourth pulley with mass 3m before going up to the ceiling. The string is continuous and passes under all four pulleys.](daff947a443eb2a4735e3a81b6f756d9_img.jpg)

Diagram of an Atwood's machine (Fig. 3.22). A string is attached to a ceiling, goes down around a pulley with mass m, up around another pulley, down around a third pulley with mass 2m, and finally up around a fourth pulley with mass 3m before going up to the ceiling. The string is continuous and passes under all four pulleys.

Fig. 3.22

![Diagram of an Atwood's machine (Fig. 3.23). A string is attached to a ceiling, goes down around a pulley with mass m, up around another pulley, down around a third pulley, up around a fourth pulley, and finally up to the ceiling. The string is continuous and passes under all four pulleys.](55fb58e14ec092ccc4fe111de0dc6278_img.jpg)

Diagram of an Atwood's machine (Fig. 3.23). A string is attached to a ceiling, goes down around a pulley with mass m, up around another pulley, down around a third pulley, up around a fourth pulley, and finally up to the ceiling. The string is continuous and passes under all four pulleys.

Fig. 3.23

![Diagram of three identical cylinders (Fig. 3.24). The bottom cylinder is on the ground. The other two cylinders are placed on top of it, one on the left and one on the right, forming a triangle. A string is attached to the ceiling, goes down around the left cylinder, up around the right cylinder, and finally up to the ceiling.](eaa5fbc353eb95b90302cfbe7c299576_img.jpg)

Diagram of three identical cylinders (Fig. 3.24). The bottom cylinder is on the ground. The other two cylinders are placed on top of it, one on the left and one on the right, forming a triangle. A string is attached to the ceiling, goes down around the left cylinder, up around the right cylinder, and finally up to the ceiling.

Fig. 3.24

side of the bottom pulley, and once around the top side of the top two pulleys. The two masses are  $m$  and  $2m$ . Assume that the parts of the string connecting the pulleys are essentially vertical. Find the accelerations of the masses.

### 3.28. Atwood's 2 \*

Consider the Atwood's machine in Fig. 3.21, with two masses  $m$ . The axle of the bottom pulley has two string ends attached to it, as shown. Find the accelerations of the masses.

### 3.29. Atwood's 3 \*

Consider the Atwood's machine in Fig. 3.22, with masses  $m$ ,  $2m$ , and  $3m$ . Find the accelerations of the masses.

### 3.30. Atwood's 4 \*\*

Consider the Atwood's machine in Fig. 3.23 (and also on the front cover). If the number of pulleys that have string passing beneath them is  $N$  instead of the 3 shown, find the accelerations of the masses.

### 3.31. Atwood's 5 \*\*

Consider the Atwood's machine in Fig. 3.24. The two shaded pulleys have mass  $m$ , and the string slides *frictionlessly* along all of the pulleys (so you don't have to worry about any rotational motion). Find the accelerations of the two shaded pulleys.

### 3.32. Atwood's 6 \*\*

Consider the Atwood's machine in Fig. 3.25. Find the accelerations of the masses. (This is a strange one.)

### 3.33. Accelerating plane \*\*

A block of mass  $m$  rests on a plane inclined at an angle  $\theta$ . The coefficient of static friction between the block and the plane is  $\mu$ . The plane is accelerated to the right with acceleration  $a$  (which may be negative); see Fig. 3.26. For what range of  $a$  does the block remain at rest with respect to the plane? In terms of  $\mu$ , there are two special values of  $\theta$ ; what are they, and why are they special?

### 3.34. Accelerating cylinders \*\*

Three identical cylinders are arranged in a triangle as shown in Fig. 3.27, with the bottom two lying on the ground. The ground and the cylinders are frictionless. You apply a constant horizontal force (directed to the right) on the left cylinder. Let  $a$  be the acceleration you give to the system. For what range of  $a$  will all three cylinders remain in contact with each other?

### 3.35. **Leaving the sphere \*\***

A small mass rests on top of a fixed sphere of radius  $R$ . The coefficient of friction is  $\mu$ . The mass is given a sideways kick that produces an initial angular speed  $\omega_0$ . Let  $\theta$  be the angle down from the top of the sphere. In terms of  $\theta$  and its derivatives, what is the tangential  $F = ma$  equation? Depending on the value of  $\omega_0$ , the mass either comes to rest on the sphere or flies off it. If  $g = 10 \text{ m/s}^2$ ,  $R = 1 \text{ m}$ , and  $\mu = 1$ , write a program to numerically determine the minimum  $\omega_0$  for which the mass leaves the sphere. For this cutoff case, give the angle at which the mass loses contact, and describe (roughly) what the plot of  $\dot{\theta}$  versus  $\theta$  looks like. See Prior and Mele (2007) for the exact solution for  $\dot{\theta}$  in terms of  $\theta$ .

![Diagram of a pulley system. A rope is attached to a ceiling, goes down around a pulley, up around a second pulley, down around a third pulley, and finally down to a mass m. A fourth mass m is attached to the rope between the second and third pulleys.](537621e5080a52b8b7b39881b862f198_img.jpg)

Diagram of a pulley system. A rope is attached to a ceiling, goes down around a pulley, up around a second pulley, down around a third pulley, and finally down to a mass m. A fourth mass m is attached to the rope between the second and third pulleys.

Fig. 3.25

### 3.36. **Comparing the times \*\*\***

A block of mass  $m$  is projected up along the surface of a plane inclined at an angle  $\theta$ . The initial speed is  $v_0$ , and the coefficients of static and kinetic friction are both equal to  $\mu$ . The block reaches a highest point and then slides back down to the starting point.

- Show that for the block to in fact slide back down instead of remaining at rest at the highest point,  $\tan \theta$  must be greater than  $\mu$ .
- Assuming that  $\tan \theta > \mu$ , is the total up and down time longer or shorter than the total time it would take if the plane were frictionless? Or does the answer depend on what  $\theta$  and  $\mu$  are?
- Assuming that  $\tan \theta > \mu$ , show that for a given  $\theta$ , the value of  $\mu$  that yields the minimum total time is given by  $\mu \approx (0.397) \tan \theta$ . (You will need to solve something numerically.) This minimum time turns out to be about 90% of the time it would take if the plane were frictionless.

![Diagram of a block of mass m on an inclined plane at angle theta. The block is accelerating up the incline with acceleration a. The coefficient of friction is mu.](a3f81dedbdc5b702f397d07ef476d53e_img.jpg)

Diagram of a block of mass m on an inclined plane at angle theta. The block is accelerating up the incline with acceleration a. The coefficient of friction is mu.

Fig. 3.26

## Section 3.3: Solving differential equations

### 3.37. **$-bv^2$ force \***

A particle of mass  $m$  is subject to a force  $F(v) = -bv^2$ . The initial position is zero, and the initial speed is  $v_0$ . Find  $x(t)$ .

### 3.38. **$kx$ force \*\***

A particle of mass  $m$  is subject to a force  $F(x) = kx$ , with  $k > 0$ . The initial position is  $x_0$ , and the initial speed is zero. Find  $x(t)$ .

![Diagram of three identical spheres stacked on a horizontal surface. Two spheres are at the bottom, touching each other and the surface. A third sphere is placed on top of them, touching both. A horizontal force F is applied to the left on the bottom-left sphere.](9ef85261dd66d80c4c63eaf89c06c2a1_img.jpg)

Diagram of three identical spheres stacked on a horizontal surface. Two spheres are at the bottom, touching each other and the surface. A third sphere is placed on top of them, touching both. A horizontal force F is applied to the left on the bottom-left sphere.

Fig. 3.27

## Section 3.4: Projectile motion

### 3.39. **Equal distances \***

At what angle should a ball be thrown so that its maximum height equals the horizontal distance traveled?

### **3.40. Redirected motion \***

A ball is dropped from rest at height  $h$ . At height  $y$ , it bounces off a surface with no loss in speed. The surface is inclined at  $45^\circ$ , so the ball bounces off horizontally. What should  $y$  be so that the ball travels the maximum horizontal distance? What is this maximum distance?

### **3.41. Throwing in the wind \***

A ball is thrown horizontally to the right, from the top of a vertical cliff of height  $h$ . A wind blows horizontally to the left, and assume (simplistically) that the effect of the wind is to provide a constant force to the left, equal in magnitude to the weight of the ball. How fast should the ball be thrown so that it lands at the foot of the cliff?

### **3.42. Throwing in the wind again \***

A ball is thrown eastward across level ground. A wind blows horizontally to the east, and assume (simplistically) that the effect of the wind is to provide a constant force to the east, equal in magnitude to the weight of the ball. At what angle  $\theta$  should the ball be thrown so that it travels the maximum horizontal distance?

### **3.43. Increasing gravity \***

At  $t = 0$  on the planet Gravitus Increaseicus, a projectile is fired with speed  $v_0$  at an angle  $\theta$  above the horizontal. This planet is a strange one, in that the acceleration due to gravity increases linearly with time, starting with a value of zero when the projectile is fired. In other words,  $g(t) = \beta t$ , where  $\beta$  is a given constant. What horizontal distance does the projectile travel? What should  $\theta$  be to maximize this distance?

![Diagram for problem 3.44 showing a stick figure on the left throwing a rock towards a tree on the right. The tree has several apples, and one apple is positioned directly above the stick figure. A dashed line indicates the trajectory of the rock from the stick figure to the apple.](87e2b787935b07b9a745a7f10d3c28fb_img.jpg)

Diagram for problem 3.44 showing a stick figure on the left throwing a rock towards a tree on the right. The tree has several apples, and one apple is positioned directly above the stick figure. A dashed line indicates the trajectory of the rock from the stick figure to the apple.

Fig. 3.28

### **3.44. Newton's apple \***

Newton is tired of apples falling on his head, so he decides to throw a rock at one of the larger and more formidable-looking apples positioned directly above his favorite sitting spot. Forgetting all about his work on gravitation, he aims the rock directly at the apple (see Fig. 3.28). To his surprise, the apple falls from the tree just as he releases the rock. Show, by calculating the rock's height when it reaches the horizontal position of the apple, that the rock hits the apple.<sup>23</sup>

![Diagram for problem 3.45 showing two balls on a horizontal surface separated by a distance d. The left ball is fired at an angle with speed u. The right ball is fired vertically upwards with speed v.](5382fb12706bd13c17895a4d20a18f95_img.jpg)

Diagram for problem 3.45 showing two balls on a horizontal surface separated by a distance d. The left ball is fired at an angle with speed u. The right ball is fired vertically upwards with speed v.

Fig. 3.29

### **3.45. Colliding projectiles \***

Two balls are fired from ground level, a distance  $d$  apart. The right one is fired vertically with speed  $v$  (see Fig. 3.29). You wish to simultaneously

<sup>23</sup> This problem suggests a way in which William Tell and his son might survive their ordeal if they were plopped down, with no time to practice, on a planet with an unknown gravitational constant (provided that the son weren't too short or that  $g$  weren't too big).

fire the left one at the appropriate velocity  $\mathbf{u}$  so that it collides with the right ball when they reach their highest point. What should  $\mathbf{u}$  be (give the horizontal and vertical components)? Given  $d$ , what should  $v$  be so that the speed  $u$  is minimum?

### 3.46. **Equal tilts \***

A plane tilts down at an angle  $\theta$  below the horizontal. On this plane, a projectile is fired with speed  $v$  at an angle  $\theta$  above the horizontal, as shown in Fig. 3.30. What is the distance,  $d$ , along the plane that the projectile travels? What is  $d$  in the limit  $\theta \rightarrow 90^\circ$ ? What  $\theta$  yields the maximum *horizontal* distance?

![Diagram for problem 3.46 showing a projectile launched from an inclined plane.](a4f8ab9085cf6977168da3fa62e04b7e_img.jpg)

The diagram shows a thick gray line representing an inclined plane that slopes downwards from left to right. A dashed horizontal line is drawn above the plane. A dashed parabolic curve represents the trajectory of a projectile. The projectile starts at a point on the plane, moving upwards and to the right at an angle  $\theta$  above the horizontal dashed line. The initial velocity vector is labeled  $v$ . The projectile lands back on the inclined plane at a point further down the slope. The distance along the inclined plane between the launch and landing points is labeled  $d$ .

Diagram for problem 3.46 showing a projectile launched from an inclined plane.

Fig. 3.30

### 3.47. **Throwing at a wall \***

You throw a ball with speed  $v_0$  at a vertical wall, a distance  $\ell$  away. At what angle should you throw the ball so that it hits the wall as high as possible? Assume  $\ell < v_0^2/g$  (why?).

### 3.48. **Firing a cannon \*\***

A cannon, when aimed vertically, is observed to fire a ball to a maximum height of  $L$ . Another ball is then fired with this same speed, but with the cannon aimed up along a plane of length  $L$ , inclined at an angle  $\theta$ , as shown in Fig. 3.31. What should  $\theta$  be so that the ball travels the largest horizontal distance,  $d$ , by the time it returns to the height of the top of the plane?

![Diagram for problem 3.48 showing a cannon on an inclined plane.](90713a587dbcb17a4f5f78ec7694b297_img.jpg)

The diagram shows a horizontal surface at the bottom. Above it, a thick gray line represents an inclined plane of length  $L$ , starting from the horizontal surface and sloping upwards to the right at an angle  $\theta$  to the horizontal. A dashed parabolic curve represents the trajectory of a ball fired from the top of the inclined plane. The ball is launched at an angle  $\theta$  above the inclined plane. The ball lands back on the horizontal surface. The horizontal distance from the base of the inclined plane to the landing point is labeled  $d$ .

Diagram for problem 3.48 showing a cannon on an inclined plane.

Fig. 3.31

### 3.49. **Perpendicular and horizontal \*\***

A plane is inclined at an angle  $\theta$  below the horizontal. A person throws a ball with speed  $v_0$  from the surface of the plane. How far down along the plane does the ball hit, if the person throws the ball (a) perpendicular to the plane? (b) horizontally?

### 3.50. **Cart, ball, and plane \*\***

A cart is held at rest on an inclined plane. A tube is positioned in the cart with its axis perpendicular to the plane. The cart is released, and at some later time a ball is fired from the tube. Will the ball eventually land back in the tube? *Hint:* Choose your coordinate system wisely.

### 3.51. **Perpendicular to plane \*\***

A hill is sloped downward at an angle  $\beta$  with respect to the horizontal. A projectile is fired with an initial velocity perpendicular to the hill. When it eventually lands on the hill, let its velocity make an angle  $\theta$  with respect to the horizontal. What is  $\theta$ ? What  $\beta$  yields the minimum value of  $\theta$ ? What is this minimum  $\theta$ ?

### **3.52. Increasing distance \*\***

- (a) What is the maximum angle at which you can throw a ball so that its distance from you never decreases during its flight?  
 (b) This maximum angle equals the minimum  $\theta$  from Exercise 3.51. Explain why this is true. (It isn't necessary to have done that exercise.)

### **3.53. Projectile with drag \*\*\***

A ball is thrown with speed  $v_0$  at an angle  $\theta$ . Let the drag force from the air take the form  $\mathbf{F}_d = -\beta\mathbf{v} \equiv -m\alpha\mathbf{v}$ .

- (a) Find  $x(t)$  and  $y(t)$ .  
 (b) Assume that the drag coefficient takes the value that makes the magnitude of the initial drag force equal to the weight of the ball. If your goal is to have  $x$  be as large as possible when  $y$  achieves its maximum value (you don't care what this maximum value actually is), show that  $\theta$  should satisfy  $\sin\theta = (\sqrt{5} - 1)/2$ , which just happens to be the inverse of the golden ratio.

## *Section 3.5: Motion in a plane, polar coordinates*

### **3.54. Low-orbit satellite**

What is the speed of a satellite whose orbit is just above the earth's surface? Give the numerical value.

### **3.55. Weight at the equator \***

A person stands on a scale at the equator. If the earth somehow stopped spinning but kept its same shape, would the reading on the scale increase or decrease? By what fraction?

### **3.56. Banking an airplane \***

An airplane flies at speed  $v$  in a horizontal circle of radius  $R$ . At what angle should the plane be banked so that you don't feel like you are getting flung to the side in your seat? At this angle, what is your apparent weight (that is, what is the normal force from the seat)?

### **3.57. Rotating hoop \***

A bead lies on a frictionless hoop of radius  $R$  that rotates around a vertical diameter with constant angular frequency  $\omega$ , as shown in Fig. 3.32. What should  $\omega$  be so that the bead maintains the same position on the hoop, at an angle  $\theta$  with respect to the vertical? There is a special value of  $\omega$ ; what is it, and why is it special?

![Diagram of a bead on a rotating hoop. A circle represents the hoop, with a vertical dashed line through its center representing the axis of rotation. A bead is located on the right side of the hoop. A dashed line connects the center of the hoop to the bead, forming an angle theta with the vertical dashed line. The radius of the hoop is labeled R. A curved arrow at the top of the vertical axis indicates rotation with angular frequency omega.](2e8db9844a19f26ba509fc3a29941950_img.jpg)

Diagram of a bead on a rotating hoop. A circle represents the hoop, with a vertical dashed line through its center representing the axis of rotation. A bead is located on the right side of the hoop. A dashed line connects the center of the hoop to the bead, forming an angle theta with the vertical dashed line. The radius of the hoop is labeled R. A curved arrow at the top of the vertical axis indicates rotation with angular frequency omega.

**Fig. 3.32**

### **3.58. Swinging in circles \***

A large number of masses are attached by strings of various lengths to a point on the ceiling. All of the masses swing around in horizontal circles of various radii with the *same* frequency  $\omega$  (one such circle is drawn in Fig. 3.33). If you take a picture (from the side) of the setup at an instant when all the masses lie in the plane of the paper (as shown for four masses), what does the “curve” formed by the masses look like?

![Diagram for Problem 3.58 showing a pivot point on a ceiling from which several strings of different lengths are suspended. The masses at the end of the strings are shown at different horizontal distances from the vertical axis of rotation, forming a horizontal circle. A dashed line indicates the vertical axis, and a curved arrow labeled ω indicates the angular velocity.](5bd2e409e2ed67e06109635cc3a56e25_img.jpg)

Diagram for Problem 3.58 showing a pivot point on a ceiling from which several strings of different lengths are suspended. The masses at the end of the strings are shown at different horizontal distances from the vertical axis of rotation, forming a horizontal circle. A dashed line indicates the vertical axis, and a curved arrow labeled ω indicates the angular velocity.

Fig. 3.33

### **3.59. Swinging triangle \***

Two masses  $m$  are attached to two vertices of an equilateral triangle made of three massless rods of length  $\ell$ . A pivot is located at the third vertex, and the triangle is free to swing back and forth in a vertical plane, as shown in Fig. 3.34. If it is initially released from rest when one of the rods is vertical (as shown), find the tensions in all three rods (and specify tension or compression), and also the accelerations of the masses, at the instant *right after* it is released.

![Diagram for Problem 3.59 showing an equilateral triangle of side length ℓ pivoted at its top vertex. Two masses m are at the bottom vertices. One rod is vertical, and the other two are at 60-degree angles. A dashed arc at the bottom left indicates the direction of swing. A downward arrow labeled g indicates gravity.](011d7628370283ec23a24c1772507121_img.jpg)

Diagram for Problem 3.59 showing an equilateral triangle of side length ℓ pivoted at its top vertex. Two masses m are at the bottom vertices. One rod is vertical, and the other two are at 60-degree angles. A dashed arc at the bottom left indicates the direction of swing. A downward arrow labeled g indicates gravity.

Fig. 3.34

### **3.60. Circular and plane pendulums \***

Consider the circular pendulum in the example in Section 3.5. Let the  $x$ - $y$  plane be the horizontal plane of the circle. For small  $\beta$ , what (approximately) is the  $F_x$  component of the force on the mass when it is at the position  $(x, y)$  on the circle?

Consider now a standard plane pendulum where the mass swings back and forth in the vertical plane containing the  $x$  axis. Let the maximum angle of the pendulum be the same small angle  $\beta$ .<sup>24</sup> What (approximately) is the  $F_x$  component of the force on the mass in terms of its  $x$  coordinate?

Your two results should be the same, which means that the  $x$  motions of the two systems are the same, because when they are each at their maximum  $x$  value ( $\ell \sin \beta$ ), they have the same  $x$  speed (zero), and we just showed that they always have the same  $x$  acceleration, independent of any  $y$  motion. So the frequencies of the two systems must be equal. (We'll see in Section 4.2 that the frequency of a plane pendulum is  $\sqrt{g/\ell}$ , in agreement with this observation.)

### **3.61. Rolling wheel \***

If you paint a dot on the rim of a rolling wheel, the coordinates of the dot may be written as<sup>25</sup>

$$(x, y) = (R\theta + R \sin \theta, R + R \cos \theta). \quad (3.55)$$

<sup>24</sup> It's actually not required that this be the same angle, as long as it's small. See Problem 3.10.

<sup>25</sup> This follows from writing  $(x, y)$  as  $(R\theta, R) + (R \sin \theta, R \cos \theta)$ . The first term here is the position of the center of the wheel, and the second term is the position of the dot relative to the center, where  $\theta$  is measured clockwise from the top.

The path of the dot is called a *cycloid*. Assume that the wheel is rolling at constant speed, which implies  $\theta = \omega t$ .

- Find  $\mathbf{v}(t)$  and  $\mathbf{a}(t)$  of the dot.
- At the instant the dot is at the top of the wheel, what is the radius of curvature of its path? The radius of curvature is defined to be the radius of the circle that matches up with the path locally at a given point. *Hint:* You know  $v$  and  $a$ .

### 3.62. Radius of curvature \*\*

A projectile is fired at speed  $v_0$  and angle  $\theta$ . What is the radius of curvature (defined in Exercise 3.61) of the parabolic motion

- at the top?
- at the beginning?
- At what angle should the projectile be fired so that the radius of curvature at the top equals half the maximum height, as shown in Fig. 3.35?

![Figure 3.35: A diagram showing a parabolic trajectory of a projectile above a horizontal ground line. A dashed circle is drawn at the peak of the parabola, representing the osculating circle at that point.](aa7a4ea43951479b7e7b4c530ea5bc2d_img.jpg)

Figure 3.35: A diagram showing a parabolic trajectory of a projectile above a horizontal ground line. A dashed circle is drawn at the peak of the parabola, representing the osculating circle at that point.

Fig. 3.35

### 3.63. Driving on tilted ground \*\*

A driver encounters a large tilted parking lot, where the angle of the ground with respect to the horizontal is  $\theta$ . The driver wishes to drive in a circle of radius  $R$  at constant speed. The coefficient of friction between the tires and the ground is  $\mu$ .

- What is the largest speed the driver can have if he wants to avoid slipping?
- What is the largest speed the driver can have, assuming he is concerned only with whether or not he slips at one of the “side” points on the circle (that is, halfway between the top and bottom points; see Fig. 3.36)?

![Figure 3.36: A diagram showing a circular path on a tilted surface. The surface is inclined at an angle theta to the horizontal. A circle is drawn on the surface, and a point on the circle is labeled 'side point'. Arrows indicate the direction of motion around the circle.](cec7ab64a78bdec0c4c092884a602b8c_img.jpg)

Figure 3.36: A diagram showing a circular path on a tilted surface. The surface is inclined at an angle theta to the horizontal. A circle is drawn on the surface, and a point on the circle is labeled 'side point'. Arrows indicate the direction of motion around the circle.

Fig. 3.36

### 3.64. Car on a banked track \*\*

A car travels around a circular banked track of radius  $R$ . The angle of the bank is  $\theta$ , and the coefficient of friction between the tires and the track is  $\mu$ . For what range of speeds does the car not slip?

### 3.65. Horizontal acceleration \*\*

A bead rests at the top of a fixed frictionless hoop of radius  $R$  that lies in a vertical plane. The bead is given a tiny push so that it slides down and around the hoop. At what points on the hoop is the bead's acceleration horizontal? *Note:* We haven't studied conservation of energy yet, but use the fact that the bead's speed after it has fallen a height  $h$  is given by  $v = \sqrt{2gh}$ .

### 3.66. **Maximum horizontal force \*\***

A bead rests at the top of a fixed frictionless hoop of radius  $R$  that lies in a vertical plane. The bead is given a tiny push so that it slides down and around the hoop. Consider the horizontal component of the force from the hoop on the bead. At what points on the hoop does this component achieve a local maximum or minimum? As in Exercise 3.65, use  $v = \sqrt{2gh}$ .

### 3.67. **Derivation of $F_r$ and $F_\theta$ \***

In Cartesian coordinates, a general vector takes the form,

$$\mathbf{r} = x\hat{\mathbf{x}} + y\hat{\mathbf{y}} = r \cos \theta \hat{\mathbf{x}} + r \sin \theta \hat{\mathbf{y}}. \quad (3.56)$$

Derive Eq. (3.51) by taking two derivatives of this expression for  $\mathbf{r}$ , and then using Eq. (3.46) to show that the result can be written in the form of Eq. (3.50). Note that unlike  $\hat{\mathbf{r}}$  and  $\hat{\theta}$ , the vectors  $\hat{\mathbf{x}}$  and  $\hat{\mathbf{y}}$  do not change with time.

### 3.68. **A force $F_\theta = 3mr\dot{\theta}$ \*\***

Consider a particle that feels an angular force only, of the form  $F_\theta = 3mr\dot{\theta}$ . Show that  $\dot{r} = \pm\sqrt{Ar^4 + B}$ , where  $A$  and  $B$  are constants of integration, determined by the initial conditions. Also, show that if the particle starts with  $\dot{\theta} \neq 0$  and  $\dot{r} > 0$ , it reaches  $r = \infty$  in a finite time. (As in Problem 3.23, there's nothing all that physical about this force. It simply makes the  $F = ma$  equations solvable.)

### 3.69. **A force $F_\theta = 2mr\dot{\theta}$ \*\***

Consider a particle that feels an angular force only, of the form  $F_\theta = 2mr\dot{\theta}$ . Show that  $r = Ae^\theta + Be^{-\theta}$ , where  $A$  and  $B$  are constants of integration, determined by the initial conditions. (This force is actually a physical one. If you put a bead on a stick and swing the stick around one end at a constant rate, then the normal force from the stick happens to be  $2mr\dot{\theta}$ .<sup>26</sup>)

### 3.70. **Stopping on a cone \*\***

When viewed from the side, the cone in Fig. 3.37 subtends an angle  $2\theta$  at its tip. A block of mass  $m$  is connected to the tip by a massless string and moves in a horizontal circle of radius  $R$  around the surface. If the

![Diagram of a cone with a block of mass m moving in a horizontal circle of radius R. The cone has a half-angle theta at its tip. The block is at the edge of the circle, and a string connects it to the tip. The radius R is shown as a dashed line from the tip to the block.](f7dfad3cc77e45d57991405785f5a411_img.jpg)

Diagram of a cone with a block of mass m moving in a horizontal circle of radius R. The cone has a half-angle theta at its tip. The block is at the edge of the circle, and a string connects it to the tip. The radius R is shown as a dashed line from the tip to the block.

Fig. 3.37

<sup>26</sup> Depending on what is meant by “physical,” the forces in Exercise 3.68 and Problem 3.23 might also be considered to be physical. They correspond to putting a bead on a stick and swinging the stick around with angular speeds proportional to the bead’s  $r$  or  $1/r$ , respectively (as is evident from the values of  $\dot{\theta}$  in the solutions). This can also be deduced from  $\tau = dL/dt$ , but we won’t get to torque until Chapter 8.

initial speed is  $v_0$ , and if the coefficient of kinetic friction between the block and the cone is  $\mu$ , how much time does it take the block to stop? (The answer is a little messy, but there are some limits you can check that will make you feel better about it.)

### 3.71. **Motorcycle circle \*\*\***

A motorcyclist wishes to travel in a circle of radius  $R$  on level ground. The coefficient of friction between the tires and the ground is  $\mu$ . The motorcycle starts at rest. What is the minimum distance it must travel in order to achieve its maximum allowable speed, that is, the speed above which it will skid out of the circular path?<sup>27</sup> Solve this in two ways:

- (a) Write down the radial and tangential  $F = ma$  equations (you'll want to write  $a$  as  $v dv/dx$ ), and then demand that the magnitude of the friction force equals  $\mu mg$  in the optimal case. Take it from there.
- (b) Let the friction force make an angle  $\beta(t)$  with respect to the tangential direction. Write down the radial and tangential  $F = ma$  equations (you'll want to write  $a$  as  $dv/dt$ ), and then take the derivative of the radial equation. Take it from there (this is the slick way).

## 3.8 Solutions

### 3.1. **Atwood's machine**

Let  $T$  be the tension in the string, and let  $a$  be the acceleration of  $m_1$  (with upward taken to be positive). Then  $-a$  is the acceleration of  $m_2$ . So the  $F = ma$  equations are

$$T - m_1g = m_1a, \quad \text{and} \quad T - m_2g = m_2(-a). \quad (3.57)$$

Solving these two equations for  $a$  and  $T$  gives

$$a = \frac{(m_2 - m_1)g}{m_2 + m_1}, \quad \text{and} \quad T = \frac{2m_1m_2g}{m_2 + m_1}. \quad (3.58)$$

**REMARKS:** As a double-check,  $a$  has the correct limits when  $m_2 \gg m_1$ ,  $m_1 \gg m_2$ , and  $m_2 = m_1$  (namely  $a \approx g$ ,  $a \approx -g$ , and  $a = 0$ , respectively). As far as  $T$  goes, if  $m_1 = m_2 = m$ , then  $T = mg$ , as it should. And if  $m_1 \ll m_2$ , then  $T \approx 2m_1g$ . This is correct, because it makes the net upward force on  $m_1$  equal to  $m_1g$ , which means that its acceleration is  $g$  upward, which is consistent with the fact that  $m_2$  is essentially in free fall. ♣

### 3.2. **Double Atwood's machine**

Let the tension in the lower string be  $T$ . Then the tension in the upper string is  $2T$  (by balancing the forces on the bottom pulley). The three  $F = ma$  equations are therefore (with all the  $a$ 's taken to be positive upward)

$$2T - m_1g = m_1a_1, \quad T - m_2g = m_2a_2, \quad T - m_3g = m_3a_3. \quad (3.59)$$

<sup>27</sup> This problem can be traced to an old edition of the Russian magazine *Kvant*.

And conservation of string says that the acceleration of  $m_1$  is

$$a_1 = -\left(\frac{a_2 + a_3}{2}\right). \quad (3.60)$$

This follows from the fact that the average position of  $m_2$  and  $m_3$  moves the same distance as the bottom pulley, which in turn moves the same distance (but in the opposite direction) as  $m_1$ . We now have four equations in the four unknowns,  $a_1$ ,  $a_2$ ,  $a_3$ , and  $T$ . With a little work, we can solve for the accelerations,

$$\begin{aligned} a_1 &= g \frac{4m_2m_3 - m_1(m_2 + m_3)}{4m_2m_3 + m_1(m_2 + m_3)}, \\ a_2 &= -g \frac{4m_2m_3 + m_1(m_2 - 3m_3)}{4m_2m_3 + m_1(m_2 + m_3)}, \\ a_3 &= -g \frac{4m_2m_3 + m_1(m_3 - 3m_2)}{4m_2m_3 + m_1(m_2 + m_3)}. \end{aligned} \quad (3.61)$$

REMARKS: There are many limits we can check here. A couple are: (1) If  $m_2 = m_3 = m_1/2$ , then all the  $a$ 's are zero, which is correct. (2) If  $m_3$  is much less than both  $m_1$  and  $m_2$ , then  $a_1 = -g$ ,  $a_2 = -g$ , and  $a_3 = 3g$ . To understand this  $3g$ , convince yourself that if  $m_1$  and  $m_2$  go down by  $d$ , then  $m_3$  goes up by  $3d$ .

Note that  $a_1$  can be written as

$$a_1 = g \left( \frac{4m_2m_3}{m_2 + m_3} - m_1 \right) / \left( \frac{4m_2m_3}{m_2 + m_3} + m_1 \right). \quad (3.62)$$

In view of the result for  $a$  in Eq. (3.58) in Problem 3.1, we see that as far as  $m_1$  is concerned here, the  $m_2, m_3$  pulley system acts just like a mass of  $4m_2m_3/(m_2 + m_3)$ . This has the expected properties of equaling zero when either  $m_2$  or  $m_3$  is zero, and equaling  $2m$  if  $m_2 = m_3 = m$ . ♣

### 3.3. Infinite Atwood's machine

FIRST SOLUTION: If the strength of gravity on the earth were multiplied by a factor  $\eta$ , then the tension in all of the strings in the Atwood's machine would likewise be multiplied by  $\eta$ . This is true because the only way to produce a quantity with the units of tension (that is, force) is to multiply a mass by  $g$ . Conversely, if we put the Atwood's machine on another planet and discover that all of the tensions are multiplied by  $\eta$ , then we know that the gravity there must be  $\eta g$ .

Let the tension in the string above the first pulley be  $T$ . Then the tension in the string above the second pulley is  $T/2$  (because the pulley is massless). Let the downward acceleration of the second pulley be  $a_2$ . Then the second pulley effectively lives in a world where gravity has strength  $g - a_2$ . Consider the subsystem of all the pulleys except the top one. This infinite subsystem is identical to the original infinite system of all the pulleys. Therefore, by the arguments in the above paragraph, we must have

$$\frac{T}{g} = \frac{T/2}{g - a_2}, \quad (3.63)$$

which gives  $a_2 = g/2$ . But  $a_2$  is also the acceleration of the top mass, so our answer is  $g/2$ .

REMARKS: You can show that the relative acceleration of the second and third pulleys is  $g/4$ , and that of the third and fourth is  $g/8$ , etc. The acceleration of a mass far down in the system therefore equals  $g(1/2 + 1/4 + 1/8 + \dots) = g$ , which makes intuitive sense.

Note that  $T = 0$  also makes Eq. (3.63) true. But this corresponds to putting a mass of zero at the end of a finite pulley system (see the following solution). ♣

![Figure 3.38: Two setups for a physics problem. The first setup shows a single mass m hanging from a string attached to a fixed support. The second setup shows a pulley system where a string is attached to a fixed support, passes over a pulley, and then splits to hang two masses, m1 and m2. Both setups have an acceleration as indicated by a downward arrow.](02f9c911b69504d90bd20e0bc61c4bbb_img.jpg)

Figure 3.38: Two setups for a physics problem. The first setup shows a single mass m hanging from a string attached to a fixed support. The second setup shows a pulley system where a string is attached to a fixed support, passes over a pulley, and then splits to hang two masses, m1 and m2. Both setups have an acceleration as indicated by a downward arrow.

Fig. 3.38

SECOND SOLUTION: Consider the following auxiliary problem.

**Problem:** Two setups are shown in Fig. 3.38. The first contains a hanging mass  $m$ . The second contains two masses,  $m_1$  and  $m_2$ , hanging over a pulley. Let both supports have acceleration  $a_s$  downward. What should  $m$  be, in terms of  $m_1$  and  $m_2$ , so that the tension  $T$  in the top string is the same in both cases?

**Answer:** In the first case, we have

$$mg - T = ma_s. \quad (3.64)$$

In the second case, let  $a$  be the acceleration of  $m_2$  relative to the support (with downward taken to be positive). Then we have

$$m_1g - \frac{T}{2} = m_1(a_s - a), \quad \text{and} \quad m_2g - \frac{T}{2} = m_2(a_s + a). \quad (3.65)$$

If we define  $g' \equiv g - a_s$ , then we may write the above three equations as

$$mg' = T, \quad m_1g' - \frac{T}{2} = -m_1a, \quad m_2g' - \frac{T}{2} = m_2a. \quad (3.66)$$

Eliminating  $a$  from the last two of these equations gives  $T = 4m_1m_2g'/(m_1 + m_2)$ . Using this value of  $T$  in the first equation then gives

$$m = \frac{4m_1m_2}{m_1 + m_2}. \quad (3.67)$$

Note that the value of  $a_s$  is irrelevant. We effectively have a fixed support in a world where the acceleration due to gravity is  $g'$  (see Eq. (3.66)), and the desired  $m$  can't depend on  $g'$ , by dimensional analysis. This auxiliary problem shows that for any  $a_s$  the two-mass system in the second case can equivalently be treated like a mass  $m$ , given by Eq. (3.67), as far as the upper string is concerned. ■

Now let's look at our infinite Atwood's machine. Assume that the system has  $N$  pulleys, where  $N \rightarrow \infty$ . Let the bottom mass be  $x$ . Then the auxiliary problem shows that the bottom two masses,  $m$  and  $x$ , can be treated like an effective mass  $f(x)$ , where

$$f(x) = \frac{4mx}{m+x} = \frac{4x}{1+(x/m)}. \quad (3.68)$$

We can then treat the combination of the mass  $f(x)$  and the next  $m$  as an effective mass  $f(f(x))$ . These iterations can be repeated, until we finally have a mass  $m$  and a mass  $f^{(N-1)}(x)$  hanging over the top pulley. So we must determine the behavior of  $f^N(x)$ , as  $N \rightarrow \infty$ . This behavior is clear if we look at the plot of  $f(x)$  in Fig. 3.39. We see that  $x = 3m$  is a fixed point of  $f(x)$ . That is,  $f(3m) = 3m$ . This plot shows that no matter what  $x$  we start with, the iterations approach  $3m$  (unless we start at  $x = 0$ , in which case we remain there). These iterations are shown graphically by the directed lines in the plot. After reaching the value  $f(x)$  on the curve, the line moves horizontally to the  $x$  value of  $f(x)$ , and then vertically to the value  $f(f(x))$  on the curve, and so on. Therefore, since  $f^N(x) \rightarrow 3m$  as  $N \rightarrow \infty$ , our infinite Atwood's machine is equivalent to (as far as the top mass is concerned) just two masses,  $m$  and  $3m$ . You can then quickly show that the acceleration of the top mass is  $g/2$ . Note that as far as the support is concerned, the whole apparatus is equivalent to a mass  $3m$ . So  $3mg$  is the upward force exerted by the support.

### 3.4. Line of pulleys

Let  $m$  be the common mass, and let  $T$  be the tension in the string. Let  $a$  be the acceleration of the end masses, and let  $a'$  be the acceleration of the other  $N$  masses, with upward taken to be positive. These  $N$  accelerations are indeed all equal, because the same net force acts on all of the internal  $N$  masses, namely  $2T$  upwards and  $mg$  downwards. The  $F = ma$  equations for the end and internal masses are, respectively,

$$T - mg = ma, \quad \text{and} \quad 2T - mg = ma'. \quad (3.69)$$

![Figure 3.39: A graph showing a curve y = f(x) and a line y = x. The x-axis is labeled with m, 2m, 3m, 4m, 5m. The y-axis is labeled with m, 2m, 3m, 4m. A series of horizontal and vertical line segments (a staircase path) connects the origin to the point (5m, 3m) on the curve y = f(x). The line y = x passes through the origin and the point (3m, 3m).](65a73373b57df71e5c2ce1ce0eb7b65d_img.jpg)

Figure 3.39: A graph showing a curve y = f(x) and a line y = x. The x-axis is labeled with m, 2m, 3m, 4m, 5m. The y-axis is labeled with m, 2m, 3m, 4m. A series of horizontal and vertical line segments (a staircase path) connects the origin to the point (5m, 3m) on the curve y = f(x). The line y = x passes through the origin and the point (3m, 3m).

Fig. 3.39 Problem 3.3, second solution

But the string has fixed length. Therefore,

$$N(2a') + a + a = 0. \quad (3.70)$$

The “2” here comes from the fact that if one of the inside masses goes up by a distance  $d$ , then a length  $2d$  of string has disappeared and must therefore appear somewhere else (namely, in the outer two segments). Eliminating  $T$  from Eq. (3.69) gives  $a' = 2a + g$ . Combining this with Eq. (3.70) then gives

$$a = -\frac{Ng}{2N+1}, \quad \text{and} \quad a' = \frac{g}{2N+1}. \quad (3.71)$$

REMARKS: For  $N = 1$ , we have  $a = -g/3$  and  $a' = g/3$ . For larger  $N$ ,  $a$  increases in magnitude and approaches  $-g/2$  as  $N \rightarrow \infty$ , and  $a'$  decreases in magnitude and approaches zero as  $N \rightarrow \infty$ . The signs of  $a$  and  $a'$  in Eq. (3.71) may be surprising. You might think that if, say,  $N = 100$ , then these 100 masses will “win” out over the two end masses, so that the  $N$  masses will fall. But this is not correct, because there are many ( $2N$ , in fact) tensions acting up on the  $N$  masses. They do *not* behave like a mass  $Nm$  hanging below one pulley. In fact, two masses of  $m/2$  on the ends will balance any number  $N$  of masses  $m$  in the interior (with the help of the upward forces from the top row of pulleys). ♣

### 3.5. Ring of pulleys

Let  $T$  be the tension in the string. Then  $F = ma$  for  $m_i$  gives

$$2T - m_i g = m_i a_i, \quad (3.72)$$

with upward taken to be positive. The  $a_i$ 's are related by the fact that the string has fixed length, which implies that the sum of the displacements of all the masses is zero. In other words,

$$a_1 + a_2 + \cdots + a_N = 0. \quad (3.73)$$

If we divide Eq. (3.72) by  $m_i$ , and then add the  $N$  such equations together and use Eq. (3.73), we find that  $T$  is given by

$$2T \left( \frac{1}{m_1} + \frac{1}{m_2} + \cdots + \frac{1}{m_N} \right) - Ng = 0. \quad (3.74)$$

Therefore,

$$T = \frac{NMg}{2}, \quad \text{where} \quad \frac{1}{M} \equiv \frac{1}{m_1} + \frac{1}{m_2} + \cdots + \frac{1}{m_N} \quad (3.75)$$

is the so-called *reduced mass* of the system. Substituting this value for  $T$  into (3.72) gives

$$a_i = g \left( \frac{NM}{m_i} - 1 \right). \quad (3.76)$$

REMARK: A few special cases are: If all the masses are equal, then all the  $a_i = 0$ . If  $m_k = 0$  (and all the others are not zero), then  $a_k = (N - 1)g$ , and all the other  $a_i = -g$ . If  $N - 1$  of the masses are equal and much smaller than the remaining one,  $m_k$ , then  $m_k \approx -g$ , and all the other  $a_i \approx g/(N - 1)$ . ♣

### 3.6. Sliding down a plane

- (a) The component of gravity along the plane is  $g \sin \theta$ . The acceleration in the horizontal direction is therefore  $a_x = (g \sin \theta) \cos \theta$ . Our goal is to maximize  $a_x$ . By taking the derivative, or by noting that  $\sin \theta \cos \theta = (\sin 2\theta)/2$ , we obtain  $\theta = \pi/4$ . The maximum  $a_x$  is then  $g/2$ .
- (b) The normal force from the plane is  $mg \cos \theta$ , so the kinetic friction force is  $\mu mg \cos \theta$ . The acceleration along the plane is therefore  $g(\sin \theta - \mu \cos \theta)$ , and so the acceleration in the horizontal direction is  $a_x = g(\sin \theta - \mu \cos \theta) \cos \theta$ . We want to maximize this. Setting the derivative equal to zero gives

$$\begin{aligned} (\cos^2 \theta - \sin^2 \theta) + 2\mu \sin \theta \cos \theta = 0 &\implies \cos 2\theta + \mu \sin 2\theta = 0 \\ &\implies \tan 2\theta = -\frac{1}{\mu}. \end{aligned} \quad (3.77)$$

For  $\mu \rightarrow 0$ , this gives the  $\pi/4$  result in part (a). For  $\mu \rightarrow \infty$ , we obtain  $\theta \approx \pi/2$ , which makes sense.

REMARKS: The time to travel a horizontal distance  $d$  is obtained from  $a_x t^2/2 = d$ . In part (a), this gives a minimum time of  $2\sqrt{d/g}$ . In part (b), you can show that the maximum  $a_x$  is  $(g/2)(\sqrt{1 + \mu^2} - \mu)$ , which then leads to a minimum time of  $2\sqrt{d/g}(\sqrt{1 + \mu^2} + \mu)^{1/2}$ . This has the correct  $\mu \rightarrow 0$  limit, and it behaves like  $2\sqrt{2\mu d/g}$  for  $\mu \rightarrow \infty$ . ♣

### 3.7. Sliding sideways on a plane

The normal force from the plane is  $N = mg \cos \theta$ . Therefore, the friction force on the block is  $\mu N = (\tan \theta)(mg \cos \theta) = mg \sin \theta$ . This force acts in the direction opposite to the motion. The block also feels the gravitational force of  $mg \sin \theta$  pointing down the plane.

Because the magnitudes of the friction force and the gravitational force along the plane are equal, the acceleration along the direction of motion equals the negative of the acceleration in the direction down the plane. Therefore, in a small increment of time, the speed that the block loses along its direction of motion exactly equals the speed that it gains in the direction down the plane. Letting  $v$  be the total speed of the

block, and letting  $v_y$  be the component of the velocity in the direction down the plane, we therefore have

$$v + v_y = C, \quad (3.78)$$

where  $C$  is a constant.  $C$  is given by its initial value, which is  $V + 0 = V$ . The final value of  $C$  is  $V_f + V_f = 2V_f$  (where  $V_f$  is the final speed of the block), because the block is essentially moving straight down the plane after a very long time. Therefore,

$$2V_f = V \implies V_f = \frac{V}{2}. \quad (3.79)$$

### 3.8. Moving plane

Let  $N$  be the normal force between the block and the plane. Note that we *cannot* assume that  $N = mg \cos \theta$ , because the plane recoils. We can see that  $N = mg \cos \theta$  is in fact incorrect, because in the limiting case where  $M = 0$ , we have no normal force at all.

The various  $F = ma$  equations (vertical and horizontal for the block, and horizontal for the plane) are

$$\begin{aligned} mg - N \cos \theta &= ma_y, \\ N \sin \theta &= ma_x, \\ N \sin \theta &= MA_x, \end{aligned} \quad (3.80)$$

where we have chosen the positive directions for  $a_y$ ,  $a_x$ , and  $A_x$  to be downward, rightward, and leftward, respectively. There are four unknowns here:  $a_x$ ,  $a_y$ ,  $A_x$ , and  $N$ , so we need one more equation. This fourth equation is the constraint that the block remains in contact with the plane. The horizontal distance between the block and its starting point on the plane is  $(a_x + A_x)t^2/2$ , and the vertical distance is  $a_y t^2/2$ . The ratio of these distances must equal  $\tan \theta$  if the block is to remain on the plane (imagine looking at things in the frame of the plane). Therefore, we must have

$$\frac{a_y}{a_x + A_x} = \tan \theta. \quad (3.81)$$

Using Eq. (3.80) to solve for  $a_y$ ,  $a_x$ , and  $A_x$  in terms of  $N$ , and then plugging the results into Eq. (3.81), gives

$$\frac{g - \frac{N}{m} \cos \theta}{\frac{N}{m} \sin \theta + \frac{N}{M} \sin \theta} = \tan \theta \implies N = g \left( \sin \theta \tan \theta \left( \frac{1}{m} + \frac{1}{M} \right) + \frac{\cos \theta}{m} \right)^{-1}. \quad (3.82)$$

(In the limit  $M \rightarrow \infty$ , this reduces to  $N = mg \cos \theta$ , as it should.) Having found  $N$ , the third of Eqs. (3.80) gives  $A_x$ , which may be written as

$$A_x = \frac{N \sin \theta}{M} = \frac{mg \sin \theta \cos \theta}{M + m \sin^2 \theta}. \quad (3.83)$$

#### REMARKS:

1. For given  $M$  and  $m$ , you can show that the angle  $\theta_0$  that maximizes  $A_x$  is  $\tan \theta_0 = \sqrt{M/(M+m)}$ . If  $M \ll m$ , then  $\theta_0 \approx 0$ ; this makes sense, because the plane gets squeezed out very fast. If  $M \gg m$ , then  $\theta_0 \approx \pi/4$ ; this is consistent with the  $\pi/4$  result from Problem 3.6(a).
2. In the limit  $M \ll m$ , Eq. (3.83) gives  $A_x \approx g/\tan \theta$ . This makes sense, because  $m$  falls essentially straight down with acceleration  $g$ , and the plane gets squeezed out to the left.
3. In the limit  $M \gg m$ , Eq. (3.83) gives  $A_x \approx g(m/M) \sin \theta \cos \theta$ . The correctness of this is more transparent if we instead look at  $a_x = (M/m)A_x \approx g \sin \theta \cos \theta$ . Since the plane is essentially at rest in this limit, this value of  $a_x$  implies that the acceleration of  $m$  along the plane equals  $a_x/\cos \theta \approx g \sin \theta$ , as expected. ♣

### 3.9. Exponential force

$F = ma$  gives  $\ddot{x} = a_0 e^{-bt}$ . Integrating this with respect to time gives  $v(t) = -a_0 e^{-bt}/b + A$ . Integrating again gives  $x(t) = a_0 e^{-bt}/b^2 + At + B$ . The initial condition  $v(0) = 0$  gives  $-a_0/b + A = 0 \implies A = a_0/b$ . And the initial condition  $x(0) = 0$  gives  $a_0/b^2 + B = 0 \implies B = -a_0/b^2$ . Therefore,

$$x(t) = a_0 \left( \frac{e^{-bt}}{b^2} + \frac{t}{b} - \frac{1}{b^2} \right). \quad (3.84)$$

For  $t \rightarrow \infty$  (more precisely, for  $bt \rightarrow \infty$ ),  $v$  approaches  $a_0/b$ , and  $x$  approaches  $a_0(t/b - 1/b^2)$ . We see that the particle eventually lags a distance  $a_0/b^2$  behind another particle that starts at the same position but moves with the constant speed  $v = a_0/b$ . For  $t \approx 0$  (more precisely, for  $bt \approx 0$ ), we can expand  $e^{-bt}$  in its Taylor series to obtain  $x(t) \approx a_0 t^2/2$ . This makes sense, because the exponential factor in the force is essentially equal to 1, so we essentially have a constant force with constant acceleration.

### 3.10. $-kx$ force

This is simply a Hooke's-law spring force, which we'll see much more of in Chapter 4.  $F = ma$  gives  $-kx = mv dv/dx$ . Separating variables and integrating yields

$$-\int_{x_0}^x kx dx = \int_0^v mv dv \implies \frac{1}{2}kx_0^2 - \frac{1}{2}kx^2 = \frac{1}{2}mv^2. \quad (3.85)$$

Solving for  $v \equiv dx/dt$  and then separating variables and integrating again gives

$$\int_{x_0}^x \frac{dx}{\sqrt{x_0^2 - x^2}} = \pm \int_0^t \sqrt{\frac{k}{m}} dt. \quad (3.86)$$

You can look up this integral, or you can solve it with a trig substitution. Letting  $x \equiv x_0 \cos \theta$  gives  $dx = -x_0 \sin \theta d\theta$ , and so we have

$$\int_0^\theta \frac{-x_0 \sin \theta d\theta}{x_0 \sin \theta} = \pm \sqrt{\frac{k}{m}} t \implies \theta = \mp \sqrt{\frac{k}{m}} t. \quad (3.87)$$

From the definition of  $\theta$ , the solution for  $x(t)$  is therefore

$$x(t) = x_0 \cos \left( \sqrt{\frac{k}{m}} t \right). \quad (3.88)$$

We see that the particle oscillates back and forth sinusoidally. It completes a full oscillation when the argument of the cosine increases by  $2\pi$ . So the period of the motion is  $T = 2\pi \sqrt{m/k}$ , which interestingly is independent of  $x_0$ . It increases with  $m$  and decreases with  $k$ , as expected.

### 3.11. Falling chain

Let the density of the chain be  $\rho$ , and let  $y(t)$  be the length hanging down through the hole at time  $t$ . Then the total mass is  $\rho \ell$ , and the mass hanging below the hole is  $\rho y$ . The net downward force on the chain is  $(\rho y)g$ , so  $F = ma$  gives

$$\rho g y = (\rho \ell) \ddot{y} \implies \ddot{y} = \frac{g}{\ell} y. \quad (3.89)$$

At this point, there are two ways we can proceed:

**FIRST METHOD:** Since we have a function whose second derivative is proportional to itself, a good bet for the solution is an exponential function. And indeed, a quick check shows that the solution is

$$y(t) = Ae^{\alpha t} + Be^{-\alpha t}, \quad \text{where } \alpha \equiv \sqrt{\frac{g}{\ell}}. \quad (3.90)$$

Taking the derivative of this to obtain  $\dot{y}(t)$ , and using the given information that  $\dot{y}(0) = 0$ , we find  $A = B$ . Using  $y(0) = y_0$ , we then find  $A = B = y_0/2$ . So the length that hangs below the hole is

$$y(t) = \frac{y_0}{2} (e^{\alpha t} + e^{-\alpha t}) \equiv y_0 \cosh(\alpha t). \quad (3.91)$$

And the speed is

$$\dot{y}(t) = \frac{\alpha y_0}{2} (e^{\alpha t} - e^{-\alpha t}) \equiv \alpha y_0 \sinh(\alpha t). \quad (3.92)$$

The time  $T$  that satisfies  $y(T) = \ell$  is given by  $\ell = y_0 \cosh(\alpha T)$ . Using  $\sinh x = \sqrt{\cosh^2 x - 1}$ , we find that the speed of the chain right when it loses contact with the table is

$$\dot{y}(T) = \alpha y_0 \sinh(\alpha T) = \alpha \sqrt{\ell^2 - y_0^2} \equiv \sqrt{g\ell} \sqrt{1 - \eta_0^2}, \quad (3.93)$$

where  $\eta_0 \equiv y_0/\ell$  is the initial fraction hanging below the hole. If  $\eta_0 \approx 0$ , then the speed at time  $T$  is  $\sqrt{g\ell}$  (this quickly follows from conservation of energy, which is the subject of Chapter 5). Also, you can show that Eq. (3.91) implies that  $T$  goes to infinity logarithmically as  $\eta_0 \rightarrow 0$ .

SECOND METHOD: Write  $\ddot{y}$  as  $v dv/dy$  in Eq. (3.89), and then separate variables and integrate to obtain

$$\int_0^v v dv = \alpha^2 \int_{y_0}^y y dy \implies v^2 = \alpha^2 (y^2 - y_0^2), \quad (3.94)$$

where  $\alpha \equiv \sqrt{g/\ell}$ . Now write  $v$  as  $dy/dt$  and separate variables again to obtain

$$\int_{y_0}^y \frac{dy}{\sqrt{y^2 - y_0^2}} = \alpha \int_0^t dt. \quad (3.95)$$

The integral on the left-hand side is  $\cosh^{-1}(y/y_0)$ , so we arrive at  $y(t) = y_0 \cosh(\alpha t)$ , in agreement with Eq. (3.91). The solution then proceeds as above. However, an easier way to obtain the final speed with this method is to simply use the result for  $v$  in Eq. (3.94). This tells us that the speed of the chain when it leaves the table (that is, when  $y = \ell$ ) is  $v = \alpha \sqrt{\ell^2 - y_0^2}$ , in agreement with Eq. (3.93).

### 3.12. Throwing a beach ball

On both the way up and the way down, the total force on the ball is

$$F = -mg - m\alpha v. \quad (3.96)$$

On the way up,  $v$  is positive, so the drag force points downward, as it should. And on the way down,  $v$  is negative, so the drag force points upward. Our strategy for finding  $v_f$  will be to produce two different expressions for the maximum height  $h$ , and then equate them. We'll find these two expressions by considering the upward and then the downward motion of the ball. In doing so, we will need to write the acceleration of the ball as  $a = v dv/dy$ . For the upward motion,  $F = ma$  gives

$$-mg - m\alpha v = mv \frac{dv}{dy} \implies \int_0^h dy = - \int_{v_0}^0 \frac{v dv}{g + \alpha v}. \quad (3.97)$$

where we have taken advantage of the fact that the speed of the ball at the top is zero. Writing  $v/(g + \alpha v)$  as  $[1 - g/(g + \alpha v)]/\alpha$ , the integral yields

$$h = \frac{v_0}{\alpha} - \frac{g}{\alpha^2} \ln \left( 1 + \frac{\alpha v_0}{g} \right). \quad (3.98)$$

Now consider the downward motion. Let  $v_f$  be the final speed, which is a positive quantity. The final velocity is then the negative quantity,  $-v_f$ . Using  $F = ma$ , we obtain

$$\int_h^0 dy = - \int_0^{-v_f} \frac{v dv}{g + \alpha v}. \quad (3.99)$$

Performing the integration (or just replacing the  $v_0$  in Eq. (3.98) with  $-v_f$ ) gives

$$h = -\frac{v_f}{\alpha} - \frac{g}{\alpha^2} \ln \left( 1 - \frac{\alpha v_f}{g} \right). \quad (3.100)$$

Equating the expressions for  $h$  in Eqs. (3.98) and (3.100) gives an implicit equation for  $v_f$  in terms of  $v_0$ ,

$$v_0 + v_f = \frac{g}{\alpha} \ln \left( \frac{g + \alpha v_0}{g - \alpha v_f} \right). \quad (3.101)$$

**REMARKS:** In the limit of small  $\alpha$  (more precisely, in the limit  $\alpha v_0/g \ll 1$ ), we can use  $\ln(1+x) = x - x^2/2 + \dots$  to obtain approximate values for  $h$  in Eqs. (3.98) and (3.100). The results are, as expected,

$$h \approx \frac{v_0^2}{2g}, \quad \text{and} \quad h \approx \frac{v_f^2}{2g}. \quad (3.102)$$

We can also make approximations for large  $\alpha$  (or large  $\alpha v_0/g$ ). In this limit, the log term in Eq. (3.98) is negligible, so we obtain  $h \approx v_0/\alpha$ . And Eq. (3.100) gives  $v_f \approx g/\alpha$ , because the argument of the log must be very small in order to give a very large negative number, which is needed to produce a positive  $h$  on the left-hand side. There is no way to relate  $v_f$  and  $h$  in this limit, because the ball quickly reaches the terminal velocity of  $-g/\alpha$  (which is the velocity that makes the net force equal to zero), independent of  $h$ . ♣

Let's now find the times it takes for the ball to go up and to go down. We'll present two methods for doing this.

**FIRST METHOD:** Let  $T_1$  be the time for the upward path. If we write the acceleration of the ball as  $a = dv/dt$ , then  $F = ma$  gives  $-mg - \alpha v = m dv/dt$ . Separating variables and integrating yields

$$\int_0^{T_1} dt = - \int_{v_0}^0 \frac{dv}{g + \alpha v} \implies T_1 = \frac{1}{\alpha} \ln \left( 1 + \frac{\alpha v_0}{g} \right). \quad (3.103)$$

In a similar manner, we find that the time  $T_2$  for the downward path is

$$T_2 = -\frac{1}{\alpha} \ln \left( 1 - \frac{\alpha v_f}{g} \right). \quad (3.104)$$

Therefore,

$$T_1 + T_2 = \frac{1}{\alpha} \ln \left( \frac{g + \alpha v_0}{g - \alpha v_f} \right) = \frac{v_0 + v_f}{g}, \quad (3.105)$$

where we have used Eq. (3.101). This result is shorter than the time in vacuum (namely  $2v_0/g$ ) because  $v_f < v_0$ .

**SECOND METHOD:** The very simple form of Eq. (3.105) suggests that there is a cleaner way of deriving it. And indeed, if we integrate  $m dv/dt = -mg - \alpha v$  with respect to time on the way up, we obtain  $-v_0 = -gT_1 - \alpha h$  (because  $\int v dt = h$ ). Likewise, if we integrate  $m dv/dt = -mg - \alpha v$  with respect to time on the way down, we obtain  $-v_f = -gT_2 + \alpha h$  (because  $\int v dt = -h$ ). Adding these two results gives Eq. (3.105). Note that this procedure works only because the drag force is proportional to  $v$ .

**REMARK:** The fact that the time here is shorter than the time in vacuum isn't obvious. On one hand, the ball doesn't travel as high in air as it would in vacuum, so you might think that  $T_1 + T_2 < 2v_0/g$ . But on the other hand, the ball moves slower in air on the way down, so you might think that  $T_1 + T_2 > 2v_0/g$ . It isn't obvious which effect wins, without doing a calculation.<sup>28</sup> For any  $\alpha$ , you can use Eq. (3.103) to show that  $T_1 < v_0/g$ . But  $T_2$  is harder to get a handle on, because it is given in terms of  $v_f$ . But in the limit of large  $\alpha$ , the ball quickly reaches terminal velocity, so we have  $T_2 \approx h/v_f$ . Using the results from the previous remark, this becomes  $T_2 \approx (v_0/\alpha)/(g/\alpha) = v_0/g$ . Interestingly, this equals the downward (and upward) time for a ball thrown in vacuum. ♣

### 3.13. Balancing a pencil

- (a) The component of gravity in the tangential direction is  $mg \sin \theta \approx mg\theta$ . Therefore, the tangential  $F = ma$  equation is  $mg\theta = m\ell\ddot{\theta}$ , which may be written as  $\ddot{\theta} = (g/\ell)\theta$ . The general solution to this equation is<sup>29</sup>

$$\theta(t) = Ae^{t/\tau} + Be^{-t/\tau}, \quad \text{where } \tau \equiv \sqrt{\ell/g}. \quad (3.106)$$

The constants  $A$  and  $B$  are found from the initial conditions,

$$\begin{aligned} \theta(0) = \theta_0 &\implies A + B = \theta_0, \\ \dot{\theta}(0) = \omega_0 &\implies (A - B)/\tau = \omega_0. \end{aligned} \quad (3.107)$$

Solving for  $A$  and  $B$ , and then plugging the results into Eq. (3.106) gives

$$\theta(t) = \frac{1}{2}(\theta_0 + \omega_0\tau)e^{t/\tau} + \frac{1}{2}(\theta_0 - \omega_0\tau)e^{-t/\tau}. \quad (3.108)$$

- (b) The constants  $A$  and  $B$  will turn out to be small (they will each be of order  $\sqrt{h}$ ). Therefore, by the time the positive exponential has increased enough to make  $\theta$  of order 1, the negative exponential will have become negligible. We will therefore ignore this term from here on. In other words,

$$\theta(t) \approx \frac{1}{2}(\theta_0 + \omega_0\tau)e^{t/\tau}. \quad (3.109)$$

The goal is to keep  $\theta$  small for as long as possible. Hence, we want to minimize the coefficient of the exponential, subject to the uncertainty-principle constraint,  $(\ell\theta_0)(m\ell\omega_0) \geq h$ . This constraint gives  $\omega_0 \geq h/(m\ell^2\theta_0)$ . Therefore,

$$\theta(t) \geq \frac{1}{2}\left(\theta_0 + \frac{h\tau}{m\ell^2\theta_0}\right)e^{t/\tau}. \quad (3.110)$$

Taking the derivative with respect to  $\theta_0$  to minimize the coefficient, we find that the minimum value occurs at  $\theta_0 = \sqrt{h\tau/m\ell^2}$ . Substituting this back into Eq. (3.110) gives

$$\theta(t) \geq \sqrt{\frac{h\tau}{m\ell^2}}e^{t/\tau}. \quad (3.111)$$

Setting  $\theta \approx 1$ , and then solving for  $t$  gives (using  $\tau \equiv \sqrt{\ell/g}$ )

$$t \leq \frac{1}{4}\sqrt{\frac{\ell}{g}}\ln\left(\frac{m^2\ell^3g}{h^2}\right). \quad (3.112)$$

<sup>28</sup> For a similar setup where it again isn't obvious (for good reason) which effect wins, see Exercise 3.36.

<sup>29</sup> If you want, you can derive this by separating variables and integrating. The solution is essentially the same as in the second method presented in the solution to Problem 3.11.

With the given values,  $m = 0.01$  kg and  $\ell = 0.1$  m, along with  $g = 10$  m/s<sup>2</sup> and  $\hbar = 1.06 \cdot 10^{-34}$  J s, we obtain

$$t \leq \frac{1}{4}(0.1 \text{ s}) \ln(9 \cdot 10^{61}) \approx 3.5 \text{ s.} \quad (3.113)$$

No matter how clever you are, and no matter how much money you spend on the newest cutting-edge pencil balancing equipment, you can never get a pencil to balance for more than about four seconds.

#### REMARKS:

1. The smallness of this answer is quite amazing. It is remarkable that a quantum effect on a macroscopic object can produce an everyday value for a time scale. Basically, the point is that the fast exponential growth of  $\theta$  (which gives rise to the log in the final result for  $t$ ) wins out over the smallness of  $\hbar$ , and produces a result for  $t$  of order 1. When push comes to shove, exponential effects always win.
2. The above value for  $t$  depends strongly on  $\ell$  and  $g$ , through the  $\sqrt{\ell/g}$  term. But the dependence on  $m$ ,  $\ell$ , and  $g$  in the log term is very weak, because  $\hbar$  is so small. If  $m$  is increased by a factor of 1000, for example, the result for  $t$  increases by only about 10%. This implies that any factors of order 1 that we neglected throughout this problem are completely irrelevant. They will appear in the argument of the log term, and will therefore have negligible effect.
3. Note that dimensional analysis, which is generally a very powerful tool, won't get you too far in this problem. The quantity  $\sqrt{\ell/g}$  has dimensions of time, and the quantity  $\eta = m^2 \ell^3 g / \hbar^2$  is dimensionless (it is the only such quantity), so the balancing time must take the form,

$$t \approx \sqrt{\frac{\ell}{g}} f(\eta), \quad (3.114)$$

where  $f$  is some function. If the leading term in  $f$  were a power (even, for example, a square root), then  $t$  would essentially be infinite ( $t \approx 10^{30}$  s  $\approx 10^{22}$  years for the square root). But  $f$  in fact turns out to be a log (which you can't know without solving the problem), which completely cancels out the smallness of  $\hbar$ , reducing an essentially infinite time down to a few seconds. ♣

### 3.14. Maximum trajectory area

Let  $\theta$  be the angle at which the ball is thrown. Then the coordinates are given by  $x = (v \cos \theta)t$  and  $y = (v \sin \theta)t - gt^2/2$ . The total time in the air is  $2(v \sin \theta)/g$ , so the area under the trajectory,  $A = \int y \, dx$ , is

$$\int_0^{x_{\max}} y \, dx = \int_0^{2v \sin \theta / g} \left( (v \sin \theta)t - \frac{gt^2}{2} \right) (v \cos \theta) \, dt = \frac{2v^4}{3g^2} \sin^3 \theta \cos \theta. \quad (3.115)$$

Taking the derivative of this, we find that the maximum occurs when  $\tan \theta = \sqrt{3}$ , that is, when  $\theta = 60^\circ$ . The maximum area is then  $A_{\max} = \sqrt{3}v^4/8g^2$ . Note that by dimensional analysis we know that the area, which has dimensions of distance squared, must be proportional to  $v^4/g^2$ .

### 3.15. Bouncing ball

The ball travels  $2h$  during the first up-and-down journey. It travels  $2hf$  during the second, then  $2hf^2$  during the third, and so on. Therefore, the total distance traveled is

$$D = 2h(1 + f + f^2 + f^3 + \cdots) = \frac{2h}{1-f}. \quad (3.116)$$

The time it takes to fall down during the first up-and-down is obtained from  $h = gt^2/2$ . Therefore, the time for the first up-and-down equals  $2t = 2\sqrt{2h/g}$ . Likewise, the time for the second up-and-down equals  $2\sqrt{2(hf)/g}$ . Each successive up-and-down time decreases by a factor of  $\sqrt{f}$ , so the total time is

$$T = 2\sqrt{\frac{2h}{g}}(1 + f^{1/2} + f^1 + f^{3/2} + \dots) = 2\sqrt{\frac{2h}{g}} \cdot \frac{1}{1 - \sqrt{f}}. \quad (3.117)$$

The average speed is therefore

$$\frac{D}{T} = \frac{\sqrt{gh/2}}{1 + \sqrt{f}}. \quad (3.118)$$

**REMARK:** The average speed for  $f \approx 1$  is roughly half of the average speed for  $f \approx 0$ . This may seem counterintuitive, because in the  $f \approx 0$  case the ball slows down far more quickly than in the  $f \approx 1$  case. But the  $f \approx 0$  case consists of essentially only one bounce, and the average speed for that one bounce is the largest of any bounce. Both  $D$  and  $T$  are smaller for  $f \approx 0$  than for  $f \approx 1$ , but  $T$  is smaller by a larger factor. ♣

### 3.16. Perpendicular velocities

In the maximum-distance case, let  $v_i$  be the initial speed of the ball, and let  $v_f$  be the final speed right before it hits the plane (so  $v_f = \sqrt{v_i^2 - 2gh}$ , where  $h$  is the final height of the ball). Let the parabolic path be labeled  $P$ , and let the beginning and ending points be  $A$  and  $B$ , as shown in Fig. 3.40.

Consider the question, “Given an initial speed  $v_f$ , at what inclination angle should a ball be thrown *down* the plane from point  $B$  so that it travels the maximum distance?” The answer is that it should be thrown along the same path  $P$ , tracing out the path backward. This is certainly a possible physical trajectory (reversing time still leads to a solution to  $F = ma$  for projectile motion), and we claim that it does indeed yield the maximum distance. This can be seen in the following way.

Assume (in search of a contradiction) that with initial speed  $v_f$ , the maximum distance down the plane is obtained via some other path  $P'$  that lands farther down the plane, as shown in Fig. 3.40. Then if we decrease the initial speed  $v_f$  by an appropriate amount, we can have the ball land at point  $A$  via some path  $P''$  (not shown, lest the figure get too cluttered). From the conservation-of-energy result, the final speed at  $A$  in this case is less than  $v_i$ . But if we simply reverse the motion along path  $P''$ , we see that we can get from  $A$  to  $B$  by using an initial speed that is less than  $v_i$ . So if we then increase the speed up to  $v_i$ , we can hit a point above  $B$  on the plane via some other path  $P'''$ , contradicting the fact that  $B$  was the endpoint of the maximum-distance trajectory starting at  $A$  with initial speed  $v_i$ . This contradiction shows that the maximum distance down the plane, starting at  $B$  with speed  $v_f$ , must in fact be attained via the path  $P$ .

Now, from the example in Section 3.4, we know that in the maximum-distance case, the throwing angle bisects the angle between the ground and the vertical. We therefore have the situation shown in Fig. 3.41, because the same path gives the maximum distance for both the upward and downward throws. Since  $2\alpha + 2\gamma = 180^\circ$ , we see that  $\alpha + \gamma = 90^\circ$ , as we wanted to show.

### 3.17. Throwing a ball from a cliff

Let the inclination angle be  $\theta$ . Then the horizontal speed is  $v_x = v \cos \theta$ , and the initial vertical speed is  $v_y = v \sin \theta$ . The time it takes for the ball to hit the ground is given by  $h + (v \sin \theta)t - gt^2/2 = 0$ . Therefore,

$$t = \frac{v}{g} \left( \sin \theta + \sqrt{\sin^2 \theta + \beta} \right), \quad \text{where } \beta \equiv \frac{2gh}{v^2}. \quad (3.119)$$

![Figure 3.40: A diagram showing a parabolic path P starting at point A and ending at point B on an inclined plane. A dashed line represents a path P' starting at A and landing further down the plane. Another dashed line represents a path P''' starting at B and landing above B. The path P is the maximum distance path from A to B.](512d7b2b01a50faa796a3d87a71d48f1_img.jpg)

Figure 3.40: A diagram showing a parabolic path P starting at point A and ending at point B on an inclined plane. A dashed line represents a path P' starting at A and landing further down the plane. Another dashed line represents a path P''' starting at B and landing above B. The path P is the maximum distance path from A to B.

Fig. 3.40

![Figure 3.41: A diagram showing a ball thrown from a cliff at an angle alpha to the horizontal. The ball follows a parabolic path and lands on the ground at an angle gamma to the horizontal. The angle between the vertical and the path at the start is alpha, and at the end is gamma. The angle between the ground and the vertical is theta. The diagram shows that alpha + gamma = 90 degrees.](6770ab4155192461bafadf86196b91b6_img.jpg)

Figure 3.41: A diagram showing a ball thrown from a cliff at an angle alpha to the horizontal. The ball follows a parabolic path and lands on the ground at an angle gamma to the horizontal. The angle between the vertical and the path at the start is alpha, and at the end is gamma. The angle between the ground and the vertical is theta. The diagram shows that alpha + gamma = 90 degrees.

Fig. 3.41

(The “ $-$ ” solution for  $t$  from the quadratic formula corresponds to the ball being thrown backward down through the cliff.) The horizontal distance traveled is  $d = (v \cos \theta)t$ , which gives

$$d = \frac{v^2}{g} \cos \theta \left( \sin \theta + \sqrt{\sin^2 \theta + \beta} \right). \quad (3.120)$$

We want to maximize this function of  $\theta$ . Taking the derivative, multiplying through by  $\sqrt{\sin^2 \theta + \beta}$ , and setting the result equal to zero, gives

$$(\cos^2 \theta - \sin^2 \theta) \sqrt{\sin^2 \theta + \beta} = \sin \theta (\beta - (\cos^2 \theta - \sin^2 \theta)). \quad (3.121)$$

Using  $\cos^2 \theta = 1 - \sin^2 \theta$ , and then squaring and simplifying this equation, gives an optimal angle of

$$\sin \theta_{\max} = \frac{1}{\sqrt{2 + \beta}} \equiv \frac{1}{\sqrt{2 + 2gh/v^2}}. \quad (3.122)$$

Plugging this into Eq. (3.120), and simplifying, gives a maximum distance of

$$d_{\max} = \frac{v^2}{g} \sqrt{1 + \beta} \equiv \frac{v^2}{g} \sqrt{1 + \frac{2gh}{v^2}}. \quad (3.123)$$

If  $h = 0$ , then  $\theta_{\max} = \pi/4$  and  $d_{\max} = v^2/g$ , in agreement with the example in Section 3.4. If  $h \rightarrow \infty$  or  $v \rightarrow 0$ , then  $\theta_{\max} \approx 0$ , which makes sense.

**REMARK:** If we make use of conservation of energy (discussed in Chapter 5), it turns out that the final speed of the ball when it hits the ground is  $v_f = \sqrt{v^2 + 2gh}$ . The maximum distance in Eq. (3.123) can therefore be written as (with  $v_i \equiv v$  being the initial speed)

$$d_{\max} = \frac{v_i v_f}{g}. \quad (3.124)$$

Note that this is symmetric in  $v_i$  and  $v_f$ , as it must be, because we could imagine the trajectory running backward. Also, it equals zero if  $v_i$  is zero, and it reduces to  $v^2/g$  on level ground, as it should. We can also write the angle  $\theta$  in Eq. (3.122) in terms of  $v_f$  (instead of  $h$ ). You can show that the result is  $\tan \theta = v_i/v_f$ . This implies that the initial and final velocities are perpendicular to each other, because running the trajectory backward interchanges  $v_i$  and  $v_f$ , which means that the product of the tangents of the two angles equals 1. This is basically the same result as in Problem 3.16. ♣

### 3.18. Redirected motion

**FIRST SOLUTION:** We will use the results of Problem 3.17, namely Eqs. (3.123) and (3.122), which say that an object projected from height  $y$  at speed  $v$  travels a maximum horizontal distance of

$$d_{\max} = \frac{v^2}{g} \sqrt{1 + \frac{2gy}{v^2}}, \quad (3.125)$$

and the optimal angle yielding this distance is

$$\sin \theta = \frac{1}{\sqrt{2 + 2gy/v^2}}. \quad (3.126)$$

In the problem at hand, the object is dropped from height  $h$ , so the kinematic relation  $v_f^2 = v_i^2 + 2ad$  gives the speed at height  $y$  as  $v = \sqrt{2g(h-y)}$ . Plugging this into Eq. (3.125) tells us that the maximum horizontal distance, as a function of  $y$ , is

$$d_{\max}(y) = 2\sqrt{h(h-y)}. \quad (3.127)$$

This is maximum when  $y = 0$  (assuming we can't have negative  $y$ ), in which case the distance is  $d_{\max} = 2h$ . Equation (3.126) gives the associated optimal angle as  $\theta = 45^\circ$ .

**SECOND SOLUTION:** Assume that the greatest distance  $d_0$  is obtained when the surface is at  $y = y_0$ . We will show that  $y_0$  must be 0. We will do this by assuming  $y_0 \neq 0$  and explicitly constructing a situation that yields a greater distance.

Let  $P$  be the point where the ball finally hits the ground after it bounces off the surface at height  $y_0$ . Consider a second scenario where a ball is dropped from height  $h$  directly above  $P$ . The speed of this ball at  $P$  will be the same as the speed of the original ball at  $P$ . This follows from conservation of energy. (Or, since we haven't covered energy yet, you can use the kinematic relation  $v_f^2 = v_i^2 + 2ad$  for the  $y$  speeds of the two balls; apply it in two steps for the first ball.)

Now imagine putting a surface at  $P$  at the appropriate angle so that the second ball bounces off in the direction from which the first ball came. Then the second ball will travel backward along the parabolic trajectory of the first one. But this means that after the second ball gets to the location of the platform at  $y_0$  (which we have now removed), it will cover more horizontal distance before it hits the ground. We have therefore constructed a setup in which the ball travels farther horizontally than in our proposed maximal case. So the optimal setup must have  $y_0 = 0$ , in which case the example in Section 3.4 says that the optimal angle is  $\theta = 45^\circ$ . If we want the ball to go even farther, we can simply dig a (wide enough) hole in the ground and have the ball bounce from the bottom of the hole.

### 3.19. Maximum trajectory length

Let  $\theta$  be the angle at which the ball is thrown. Then the coordinates are given by  $x = (v \cos \theta)t$  and  $y = (v \sin \theta)t - gt^2/2$ . The ball reaches its maximum height at  $t = v \sin \theta/g$ , so the length of the trajectory is

$$\begin{aligned} L &= 2 \int_0^{v \sin \theta/g} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt \\ &= 2 \int_0^{v \sin \theta/g} \sqrt{(v \cos \theta)^2 + (v \sin \theta - gt)^2} dt \\ &= 2v \cos \theta \int_0^{v \sin \theta/g} \sqrt{1 + \left(\tan \theta - \frac{gt}{v \cos \theta}\right)^2} dt. \end{aligned} \quad (3.128)$$

Letting  $z \equiv \tan \theta - gt/v \cos \theta$ , we obtain

$$L = -\frac{2v^2 \cos^2 \theta}{g} \int_{\tan \theta}^0 \sqrt{1 + z^2} dz. \quad (3.129)$$

We can look up this integral, or we can derive it by making a  $z \equiv \sinh \alpha$  substitution. The result is

$$\begin{aligned} L &= \frac{2v^2 \cos^2 \theta}{g} \cdot \frac{1}{2} \left( z \sqrt{1 + z^2} + \ln(z + \sqrt{1 + z^2}) \right) \Big|_0^{\tan \theta} \\ &= \frac{v^2}{g} \left( \sin \theta + \cos^2 \theta \ln \left( \frac{\sin \theta + 1}{\cos \theta} \right) \right). \end{aligned} \quad (3.130)$$

As an intermediate check, you can verify that  $L = 0$  when  $\theta = 0$ , and  $L = v^2/g$  when  $\theta = 90^\circ$ . Taking the derivative of Eq. (3.130) to find the maximum, we obtain

$$\begin{aligned} 0 &= \cos \theta - 2 \cos \theta \sin \theta \ln \left( \frac{1 + \sin \theta}{\cos \theta} \right) \\ &\quad + \cos^2 \theta \left( \frac{\cos \theta}{1 + \sin \theta} \right) \frac{\cos^2 \theta + (1 + \sin \theta) \sin \theta}{\cos^2 \theta}. \end{aligned} \quad (3.131)$$

![Figure 3.42: A graph showing several parabolic trajectories of a projectile launched from the origin (0,0) in the xy-plane. The trajectories are labeled with their launch angles. One trajectory is specifically labeled 'theta=45 degrees path' and is shown as a solid line. The x-axis is labeled 'x' and the y-axis is labeled 'y'.](9857175bc98d86591d24a161fe615f12_img.jpg)

Figure 3.42: A graph showing several parabolic trajectories of a projectile launched from the origin (0,0) in the xy-plane. The trajectories are labeled with their launch angles. One trajectory is specifically labeled 'theta=45 degrees path' and is shown as a solid line. The x-axis is labeled 'x' and the y-axis is labeled 'y'.

Fig. 3.42

![Figure 3.43: A diagram showing two position vectors, r1 and r2, originating from a common point. These vectors point to two nearby points on a curved path. Corresponding velocity vectors, v1 and v2, are shown at these points, tangent to the path. The angle between r1 and r2 is the same as the angle between v1 and v2.](015a4afa77810a7cfad7dc795369bf3f_img.jpg)

Figure 3.43: A diagram showing two position vectors, r1 and r2, originating from a common point. These vectors point to two nearby points on a curved path. Corresponding velocity vectors, v1 and v2, are shown at these points, tangent to the path. The angle between r1 and r2 is the same as the angle between v1 and v2.

Fig. 3.43

![Figure 3.44: Two diagrams illustrating vector relationships. The top diagram shows two velocity vectors, v1 and v2, with their difference vector Delta v = v2 - v1. The angle between v1 and v2 is labeled theta. The bottom diagram shows two position vectors, r1 and r2, with their difference vector Delta r = r2 - r1. The angle between r1 and r2 is also labeled theta, showing that the triangles formed by these vectors are similar.](26ff7a3373e19cdf04ff8d02ad38ba6b_img.jpg)

Figure 3.44: Two diagrams illustrating vector relationships. The top diagram shows two velocity vectors, v1 and v2, with their difference vector Delta v = v2 - v1. The angle between v1 and v2 is labeled theta. The bottom diagram shows two position vectors, r1 and r2, with their difference vector Delta r = r2 - r1. The angle between r1 and r2 is also labeled theta, showing that the triangles formed by these vectors are similar.

Fig. 3.44

![Figure 3.45: A diagram of a bead on a circular hoop of radius R. The bead is at an angle theta from the vertical. Two acceleration vectors are shown: the tangential acceleration at and the radial acceleration ar. The total acceleration vector is the sum of these two components.](77a3fc2cc806f951f7e873a9dfaac7d1_img.jpg)

Figure 3.45: A diagram of a bead on a circular hoop of radius R. The bead is at an angle theta from the vertical. Two acceleration vectors are shown: the tangential acceleration at and the radial acceleration ar. The total acceleration vector is the sum of these two components.

Fig. 3.45

This reduces to

$$1 = \sin \theta \ln \left( \frac{1 + \sin \theta}{\cos \theta} \right). \quad (3.132)$$

You can show numerically that the solution for  $\theta$  is  $\theta_0 \approx 56.5^\circ$ .

**REMARK:** A few possible trajectories are shown Fig. 3.42. Using the standard result that  $\theta = 45^\circ$  provides the maximum *horizontal* distance, it follows from the figure that the  $\theta_0$  that yields the maximum trajectory length must satisfy  $\theta_0 \geq 45^\circ$ . The exact angle, however, requires the above detailed calculation. ♣

### 3.20. Centripetal acceleration

The position and velocity vectors at two nearby times are shown in Fig. 3.43. Their differences,  $\Delta \mathbf{r} \equiv \mathbf{r}_2 - \mathbf{r}_1$  and  $\Delta \mathbf{v} \equiv \mathbf{v}_2 - \mathbf{v}_1$ , are shown in Fig. 3.44. The angle between the  $\mathbf{v}$ 's is the same as the angle between the  $\mathbf{r}$ 's, because each  $\mathbf{v}$  makes a right angle with the corresponding  $\mathbf{r}$ . Therefore, the triangles in Fig. 3.44 are similar, so we have

$$\frac{|\Delta \mathbf{v}|}{v} = \frac{|\Delta \mathbf{r}|}{r}, \quad (3.133)$$

where  $r \equiv |\mathbf{r}|$  and  $v \equiv |\mathbf{v}|$ . Dividing through by  $\Delta t$  gives

$$\frac{1}{v} \left| \frac{\Delta \mathbf{v}}{\Delta t} \right| = \frac{1}{r} \left| \frac{\Delta \mathbf{r}}{\Delta t} \right| \implies \frac{|\mathbf{a}|}{v} = \frac{|\mathbf{v}|}{r} \implies a = \frac{v^2}{r}. \quad (3.134)$$

We have assumed that  $\Delta t$  is infinitesimal here, which allows us to get rid of the  $\Delta$ 's in favor of instantaneous quantities.

### 3.21. Vertical acceleration

Let  $\theta$  be the angle down from the top of the hoop. The tangential acceleration is  $a_t = g \sin \theta$ , and the radial acceleration is  $a_r = v^2/R = 2gh/R$ . But the height fallen is  $h = R - R \cos \theta$ , so we have

$$a_r = \frac{2gR(1 - \cos \theta)}{R} = 2g(1 - \cos \theta). \quad (3.135)$$

We want the total acceleration to be vertical, which means that we want the horizontal components of  $\mathbf{a}_t$  and  $\mathbf{a}_r$  in Fig. 3.45 to cancel. That is,  $a_t \cos \theta = a_r \sin \theta$ . This gives

$$(g \sin \theta) \cos \theta = 2g(1 - \cos \theta) \sin \theta \implies \sin \theta = 0 \text{ or } \cos \theta = 2/3. \quad (3.136)$$

The  $\sin \theta = 0$  root corresponds to the top and bottom of the hoop ( $\theta = 0$  and  $\theta = \pi$ ). So we want the  $\cos \theta = 2/3 \implies \theta \approx \pm 48.2^\circ$  root. The vertical acceleration is the sum of the vertical components of  $\mathbf{a}_t$  and  $\mathbf{a}_r$ , so

$$\begin{aligned} a_y &= a_t \sin \theta + a_r \cos \theta = (g \sin \theta) \sin \theta + 2g(1 - \cos \theta) \cos \theta \\ &= g(\sin^2 \theta + 2 \cos \theta - 2 \cos^2 \theta). \end{aligned} \quad (3.137)$$

Using  $\cos \theta = 2/3$ , and hence  $\sin \theta = \sqrt{5}/3$ , we have

$$a_y = g \left( \frac{5}{9} + 2 \cdot \frac{2}{3} - 2 \cdot \frac{4}{9} \right) = g. \quad (3.138)$$

**REMARK:** The reason for this nice answer is the following. If there is no horizontal acceleration, then the normal force from the hoop must have no horizontal component. In other words,  $N \sin \theta = 0$ . Therefore, either  $\sin \theta = 0$  (which gives the top and bottom solutions of  $\theta = 0$  and  $\theta = \pi$ ), or  $N = 0$ , which means that there is no normal force, so the bead feels only gravity, so it's in freefall with  $a_y = g$ .

If we want, we can use this  $N = 0$  requirement as the starting point for a second solution. Using the  $a_r$  from above, the radial  $F = ma$  equation is  $mg \cos \theta - N = 2mg(1 - \cos \theta)$ , with positive  $N$  defined to point outward. Setting  $N = 0$  gives the desired result,  $\cos \theta = 2/3$ . ♣

### 3.22. Circling around a pole

Let  $F$  be the tension in the string. At the mass, the angle between the string and the radius of the dotted circle is  $\theta = \sin^{-1}(r/R)$ . In terms of  $\theta$ , the radial and tangential  $F = ma$  equations are

$$F \cos \theta = \frac{mv^2}{R}, \quad \text{and} \quad F \sin \theta = m\dot{v}. \quad (3.139)$$

Dividing these two equations gives  $\tan \theta = (R\dot{v})/v^2$ . Separating variables and integrating gives

$$\begin{aligned} \int_{v_0}^v \frac{dv}{v^2} &= \frac{\tan \theta}{R} \int_0^t dt \quad \Rightarrow \quad \frac{1}{v_0} - \frac{1}{v} = \frac{(\tan \theta)t}{R} \\ \Rightarrow \quad v(t) &= \left( \frac{1}{v_0} - \frac{(\tan \theta)t}{R} \right)^{-1}. \end{aligned} \quad (3.140)$$

The speed  $v$  becomes infinite when

$$t = T \equiv \frac{R}{v_0 \tan \theta}. \quad (3.141)$$

This means that you can keep the mass moving in the desired circle only up to time  $T$ . After that, it is impossible. (Of course, it will become impossible, for all practical purposes, long before  $v$  becomes infinite.) The total distance,  $d = \int v dt$ , is infinite, because this integral diverges (barely, like a log) as  $t$  approaches  $T$ .

### 3.23. A force $F_\theta = m\dot{r}\ddot{\theta}$

With the given force, Eq. (3.51) becomes

$$0 = m(\ddot{r} - r\dot{\theta}^2), \quad \text{and} \quad m\dot{r}\dot{\theta} = m(r\ddot{\theta} + 2\dot{r}\dot{\theta}). \quad (3.142)$$

The second of these equations gives  $-\dot{r}\dot{\theta} = r\ddot{\theta}$ . Therefore,

$$\int \frac{\ddot{\theta}}{\dot{\theta}} dt = - \int \frac{\dot{r}}{r} dt \quad \Rightarrow \quad \ln \dot{\theta} = -\ln r + C \quad \Rightarrow \quad \dot{\theta} = \frac{D}{r}, \quad (3.143)$$

where  $D = e^C$  is a constant of integration, determined by the initial conditions. Substituting this value of  $\dot{\theta}$  into the first of Eqs. (3.142), and then multiplying through by  $\dot{r}$  and integrating, gives

$$\ddot{r} = r \left( \frac{D}{r} \right)^2 \quad \Rightarrow \quad \int \ddot{r} dt = D^2 \int \frac{\dot{r}}{r} dt \quad \Rightarrow \quad \frac{\dot{r}^2}{2} = D^2 \ln r + E. \quad (3.144)$$

Therefore,

$$\dot{r} = \sqrt{A \ln r + B}, \quad (3.145)$$

where  $A \equiv 2D^2$  and  $B \equiv 2E$ .

### 3.24. Free particle

For zero force, Eq. (3.51) gives

$$\ddot{r} = r\dot{\theta}^2, \quad \text{and} \quad r\ddot{\theta} = -2\dot{r}\dot{\theta}. \quad (3.146)$$

Separating variables in the second equation and integrating yields

$$\int \frac{\ddot{\theta}}{\dot{\theta}} dt = - \int \frac{2\dot{r}}{r} dt \quad \Rightarrow \quad \ln \dot{\theta} = -2 \ln r + C \quad \Rightarrow \quad \dot{\theta} = \frac{D}{r^2}, \quad (3.147)$$

where  $D = e^C$  is a constant of integration, determined by the initial conditions.<sup>30</sup> Substituting this value of  $\dot{\theta}$  into the first of Eqs. (3.146), and then multiplying through by  $\dot{r}$  and integrating, gives

$$\ddot{r} = r \left( \frac{D}{r^2} \right)^2 \implies \int \ddot{r} dt = D^2 \int \frac{\dot{r}}{r^3} dt \implies \frac{\dot{r}^2}{2} = -\frac{D^2}{2r^2} + E. \quad (3.148)$$

We want  $\dot{r} = 0$  when  $r = r_0$ , which implies that  $E = D^2/2r_0^2$ . Therefore,

$$\dot{r} = V \sqrt{1 - \frac{r_0^2}{r^2}}, \quad (3.149)$$

where  $V \equiv D/r_0$ . Separating variables and integrating gives

$$\int \frac{r \dot{r} dt}{\sqrt{r^2 - r_0^2}} = \int V dt \implies \sqrt{r^2 - r_0^2} = Vt \implies r = \sqrt{r_0^2 + (Vt)^2}, \quad (3.150)$$

where the constant of integration is zero, because we have chosen  $t = 0$  to correspond to  $r = r_0$ . Plugging this value for  $r$  into the  $\dot{\theta} = D/r^2 \equiv Vr_0/r^2$  result in Eq. (3.147) gives

$$\int d\theta = \int \frac{Vr_0 dt}{r_0^2 + (Vt)^2} \implies \theta = \tan^{-1} \left( \frac{Vt}{r_0} \right) \implies \cos \theta = \frac{r_0}{\sqrt{r_0^2 + (Vt)^2}}. \quad (3.151)$$

Finally, combining this with the result for  $r$  in Eq. (3.150) gives  $\cos \theta = r_0/r$ , as desired.

<sup>30</sup> The statement that  $r^2 \dot{\theta}$  is constant is simply the statement of conservation of angular momentum, because  $r^2 \dot{\theta} = r(r\dot{\theta}) = rv_\theta$ , where  $v_\theta$  is the tangential velocity. More on this in Chapters 7 and 8.