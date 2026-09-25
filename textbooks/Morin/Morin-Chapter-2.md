# Chapter 2 Statics

The subject of statics often appears in later chapters in other books, after force and torque have been discussed. However, the way that force and torque are used in statics problems is fairly minimal, at least compared with what we'll be doing later in this book. Therefore, since we won't be needing much of the machinery that we'll be developing later on, I'll introduce here the bare minimum of force and torque concepts necessary for statics problems. This will open up a whole class of problems for us. But even though the underlying principles of statics are quick to state, statics problems can be unexpectedly tricky. So be sure to tackle a lot of them to make sure you understand things.

## 2.1 Balancing forces

A “static” setup is one where all the objects are motionless. If an object remains motionless, then Newton's second law,  $F = ma$  (which we'll discuss in great detail in the next chapter), tells us that the total external force acting on the object must be zero. The converse is not true, of course. The total external force on an object is also zero if it moves with constant nonzero velocity. But we'll deal only with statics problems here. The whole goal in a statics problem is to find out what the various forces have to be so that there is zero net force acting on each object (and zero net torque, too, but that's the topic of Section 2.2). Because a force is a vector, this goal involves breaking the force up into its components. You can pick Cartesian coordinates, polar coordinates, or another set. It is usually clear from the problem which system will make your calculations easiest. Once you pick a system, you simply have to demand that the total external force in each direction is zero.

There are many different types of forces in the world, most of which are large-scale effects of complicated things going on at smaller scales. For example, the tension in a rope comes from the chemical bonds that hold the molecules in the rope together, and these chemical forces are electrical forces. In doing a mechanics problem involving a rope, there is certainly no need to analyze all the details of the forces taking place at the molecular scale. You just call the force in

the rope a “tension” and get on with the problem. Four types of forces come up repeatedly:

### *Tension*

Tension is the general name for a force that a rope, stick, etc., exerts when it is pulled on. Every piece of the rope feels a tension force in both directions, except the end points, which feel a tension on one side and a force on the other side from whatever object is attached to the end. In some cases, the tension may vary along the rope. The “Rope wrapped around a pole” example at the end of this section is a good illustration of this. In other cases, the tension must be the same everywhere. For example, in a hanging massless rope, or in a massless rope hanging over a frictionless pulley, the tension must be the same at all points, because otherwise there would be a net force on at least some part of the rope, and then  $F = ma$  would yield an infinite acceleration for this (massless) piece.

### *Normal force*

This is the force perpendicular to a surface that the surface applies to an object. The total force applied by a surface is usually a combination of the normal force and the friction force (see below). But for frictionless surfaces such as greasy ones or ice, only the normal force exists. The normal force comes about because the surface actually compresses a tiny bit and acts like a very rigid spring. The surface gets squashed until the restoring force equals the force necessary to keep the object from squashing in any more.

For the most part, the only difference between a “tension” and a “normal force” is the direction of the force. Both situations can be modeled by a spring. In the case of a tension, the spring (a rope, a stick, or whatever) is stretched, and the force on the given object is directed toward the spring. In the case of a normal force, the spring is compressed, and the force on the given object is directed away from the spring. Things like sticks can provide both normal forces and tensions. But a rope, for example, has a hard time providing a normal force. In practice, in the case of elongated objects such as sticks, a compressive force is usually called a “compressive tension,” or a “negative tension,” instead of a normal force. So by these definitions, a tension can point either way. At any rate, it’s just semantics. If you use any of these descriptions for a compressed stick, people will know what you mean.

### *Friction*

Friction is the force parallel to a surface that a surface applies to an object. Some surfaces, such as sandpaper, have a great deal of friction. Some, such as greasy ones, have essentially no friction. There are two types of friction, called “kinetic” friction and “static” friction. Kinetic friction (which we won’t cover in this chapter) deals with two objects moving relative to each other. It is usually a good approximation to say that the kinetic friction between two objects is

proportional to the normal force between them. The constant of proportionality is called  $\mu_k$  (the “coefficient of kinetic friction”), where  $\mu_k$  depends on the two surfaces involved. Thus,  $F = \mu_k N$ , where  $N$  is the normal force. The direction of the force is opposite to the motion.

Static friction deals with two objects at rest relative to each other. In the static case, we have  $F \leq \mu_s N$  (where  $\mu_s$  is the “coefficient of static friction”). Note the inequality sign. All we can say prior to solving a problem is that the static friction force has a *maximum* value equal to  $F_{\max} = \mu_s N$ . In a given problem, it is most likely less than this. For example, if a block of large mass  $M$  sits on a surface with coefficient of friction  $\mu_s$ , and you give the block a tiny push to the right (tiny enough so that it doesn’t move), then the friction force is of course not equal to  $\mu_s N = \mu_s Mg$  to the left. Such a force would send the block sailing off to the left. The true friction force is simply equal and opposite to the tiny force you apply. What the coefficient  $\mu_s$  tells us is that if you apply a force larger than  $\mu_s Mg$  (the maximum friction force on a horizontal table), then the block will end up moving to the right.

### Gravity

Consider two point objects, with masses  $M$  and  $m$ , separated by a distance  $R$ . Newton’s gravitational force law says that the force between these objects is attractive and has magnitude  $F = GMm/R^2$ , where  $G = 6.67 \cdot 10^{-11} \text{ m}^3/(\text{kg s}^2)$ . As we’ll show in Chapter 5, the same law also applies to spheres of nonzero size. That is, a sphere may be treated like a point mass located at its center. Therefore, an object on the surface of the earth feels a gravitational force equal to

$$F = m \left( \frac{GM}{R^2} \right) \equiv mg, \quad (2.1)$$

where  $M$  is the mass of the earth, and  $R$  is its radius. This equation defines  $g$ . Plugging in the numerical values, we obtain  $g \approx 9.8 \text{ m/s}^2$ , as you can check. Every object on the surface of the earth feels a force of  $mg$  downward ( $g$  varies slightly over the surface of the earth, but let’s ignore this). If the object is not accelerating, then there must be other forces present (normal forces, etc.) to make the total force be equal to zero.

Another common force is the Hooke’s-law spring force,  $F = -kx$ . But we’ll postpone the discussion of springs until Chapter 4, where we’ll spend a whole chapter on them in depth.

![Diagram of a block of mass M on an inclined plane at angle theta. A horizontal force Mg is applied to the block.](b8ba7baf04110999c137dd115388324f_img.jpg)

The diagram shows a right-angled triangle representing an inclined plane. The angle between the horizontal base and the hypotenuse is labeled  $\theta$ . A rectangular block labeled  $M$  is placed on the hypotenuse. A horizontal arrow labeled  $Mg$  points to the right, originating from the left side of the block.

Diagram of a block of mass M on an inclined plane at angle theta. A horizontal force Mg is applied to the block.

Fig. 2.1

**Example (Block on a plane):** A block of mass  $M$  rests on a fixed plane inclined at an angle  $\theta$ . You apply a horizontal force of  $Mg$  on the block, as shown in Fig. 2.1. Assume that the friction force between the block and the plane is large enough to keep the block at rest. What are the normal and friction forces (call them  $N$  and  $F_f$ ) that the plane exerts on the block? If the coefficient of static friction is  $\mu$ , for what range of angles  $\theta$  will the block in fact remain at rest?

**Solution:** Let's break the forces up into components parallel and perpendicular to the plane. (The horizontal and vertical components would also work, but the calculation would be a little longer.) The forces are  $N$ ,  $F_f$ , the applied  $Mg$ , and the weight  $Mg$ , as shown in Fig. 2.2. Balancing the forces parallel and perpendicular to the plane gives, respectively (with upward along the plane taken to be positive),

$$\begin{aligned} F_f &= Mg \sin \theta - Mg \cos \theta, \\ N &= Mg \cos \theta + Mg \sin \theta. \end{aligned} \quad (2.2)$$

### INTERMEDIATE REMARKS:

1. If  $\tan \theta > 1$ , then  $F_f$  is positive (that is, it points up the plane). And if  $\tan \theta < 1$ , then  $F_f$  is negative (that is, it points down the plane). There is no need to worry about which way it points when drawing the diagram. Just pick a direction to be positive, and if  $F_f$  comes out to be negative (as it does in the figure above, because  $\theta < 45^\circ$ ), then it actually points in the other direction.
2.  $F_f$  ranges from  $-Mg$  to  $Mg$  as  $\theta$  ranges from 0 to  $\pi/2$  (convince yourself that these limiting values make sense). As an exercise, you can show that  $N$  is maximum when  $\tan \theta = 1$ , in which case  $N = \sqrt{2}Mg$  and  $F_f = 0$ .
3. The  $\sin \theta$  and  $\cos \theta$  factors in Eq. (2.2) follow from the angles  $\theta$  drawn in Fig. 2.2. However, when solving problems like this one, it's easy to make a mistake in the geometry and then label an angle as  $\theta$  when it really should be  $90^\circ - \theta$ . So two pieces of advice: (1) Never draw an angle close to  $45^\circ$  in a figure, because if you do, you won't be able to tell the  $\theta$  angles from the  $90^\circ - \theta$  ones. (2) Always check your results by letting  $\theta$  go to 0 or  $90^\circ$  (in other words, does virtually all of a force, or virtually none of it, act in a certain direction when the plane is, say, horizontal). Once you do this a few times, you'll realize that you probably don't even need to work out the geometry in the first place. Since you know that any given component is going to involve either  $\sin \theta$  or  $\cos \theta$ , you can just pick the one that works correctly in a certain limit. ♣

![Diagram showing a block on an inclined plane at angle theta. The weight Mg is shown acting vertically downwards. The normal force N is shown acting perpendicular to the plane. The friction force F_f is shown acting up the plane. The angle theta is indicated between the plane and the horizontal.](7509891667b4ab61b40634de8cf13af3_img.jpg)

Diagram showing a block on an inclined plane at angle theta. The weight Mg is shown acting vertically downwards. The normal force N is shown acting perpendicular to the plane. The friction force F\_f is shown acting up the plane. The angle theta is indicated between the plane and the horizontal.

Fig. 2.2

The coefficient  $\mu$  tells us that  $|F_f| \leq \mu N$ . Using Eq. (2.2), this inequality becomes

$$Mg|\sin \theta - \cos \theta| \leq \mu Mg(\cos \theta + \sin \theta). \quad (2.3)$$

The absolute value here signifies that we must consider two cases:

- If  $\tan \theta \geq 1$ , then Eq. (2.3) becomes

$$\sin \theta - \cos \theta \leq \mu(\cos \theta + \sin \theta) \implies \tan \theta \leq \frac{1 + \mu}{1 - \mu}. \quad (2.4)$$

We divided by  $1 - \mu$ , so this inequality is valid only if  $\mu < 1$ . But if  $\mu \geq 1$ , we see from the first inequality here that any value of  $\theta$  (subject to our assumption,  $\tan \theta \geq 1$ ) works.

- If  $\tan \theta \leq 1$ , then Eq. (2.3) becomes

$$-\sin \theta + \cos \theta \leq \mu(\cos \theta + \sin \theta) \implies \tan \theta \geq \frac{1 - \mu}{1 + \mu}. \quad (2.5)$$

Putting these two ranges for  $\theta$  together, we have

$$\frac{1 - \mu}{1 + \mu} \leq \tan \theta \leq \frac{1 + \mu}{1 - \mu}. \quad (2.6)$$

REMARKS: For very small  $\mu$ , these bounds both approach 1, which means that  $\theta$  must be very close to  $45^\circ$ . This makes sense. If there is very little friction, then the components along the plane of the horizontal and vertical  $Mg$  forces must nearly cancel; hence,  $\theta \approx 45^\circ$ . A special value for  $\mu$  is 1, because from Eq. (2.6), we see that  $\mu = 1$  is the cutoff value that allows  $\theta$  to reach both 0 and  $\pi/2$ . If  $\mu \geq 1$ , then any tilt of the plane is allowed. We've been assuming throughout this example that  $0 \leq \theta \leq \pi/2$ . The task of Exercise 2.20 is to deal with the case where  $\theta > \pi/2$ , where the block is under an overhang. ♣

Let's now do an example involving a rope in which the tension varies with position. We'll need to consider differential pieces of the rope to solve this problem.

**Example (Rope wrapped around a pole):** A rope wraps an angle  $\theta$  around a pole. You grab one end and pull with a tension  $T_0$ . The other end is attached to a large object, say, a boat. If the coefficient of static friction between the rope and the pole is  $\mu$ , what is the largest force the rope can exert on the boat, if the rope is not to slip around the pole?

![Diagram of a small piece of rope wrapped around a pole. The piece subtends an angle dθ. Tension forces T act at both ends, tangent to the circle. The normal force N_dθ acts radially outward from the center of the pole. The inward components of the tension forces are shown as dashed arrows, each with magnitude T sin(dθ/2).](69350f1ebebf4e4b2d5644dfc6671d7c_img.jpg)

Diagram of a small piece of rope wrapped around a pole. The piece subtends an angle dθ. Tension forces T act at both ends, tangent to the circle. The normal force N\_dθ acts radially outward from the center of the pole. The inward components of the tension forces are shown as dashed arrows, each with magnitude T sin(dθ/2).

Fig. 2.3

**Solution:** Consider a small piece of the rope that subtends an angle  $d\theta$ . Let the tension in this piece be  $T$  (which varies slightly over the small length). As shown in Fig. 2.3, the pole exerts a small outward normal force,  $N_{d\theta}$ , on the piece. This normal force exists to balance the “inward” components of the tensions at the ends. These inward components have magnitude  $T \sin(d\theta/2)$ .<sup>1</sup> Therefore,  $N_{d\theta} = 2T \sin(d\theta/2)$ . The small-angle approximation,  $\sin x \approx x$ , allows us to write this as  $N_{d\theta} = T d\theta$ .

The friction force on the little piece of rope satisfies  $F_{d\theta} \leq \mu N_{d\theta} = \mu T d\theta$ . This friction force is what gives rise to the difference in tension between the two ends of the piece. In other words, the tension, as a function of  $\theta$ , satisfies

$$\begin{aligned} T(\theta + d\theta) &\leq T(\theta) + \mu T d\theta \\ \implies dT &\leq \mu T d\theta \\ \implies \int \frac{dT}{T} &\leq \int \mu d\theta \\ \implies \ln T &\leq \mu \theta + C \\ \implies T &\leq T_0 e^{\mu \theta}, \end{aligned} \quad (2.7)$$

<sup>1</sup> One of them actually has magnitude  $(T + dT) \sin(d\theta/2)$ , where  $dT$  is the increase in tension along the small piece. But the extra term this produces,  $(dT) \sin(d\theta/2)$ , is a second-order small quantity, so it can be ignored.

where we have used the fact that  $T = T_0$  when  $\theta = 0$ . The exponential behavior here is quite strong (as exponential behaviors tend to be). If we let  $\mu = 1$ , then just a quarter turn around the pole produces a factor of  $e^{\pi/2} \approx 5$ . One full revolution yields a factor of  $e^{2\pi} \approx 530$ , and two full revolutions yield a factor of  $e^{4\pi} \approx 300\,000$ . Needless to say, the limiting factor in such a case is not your strength, but rather the structural integrity of the pole around which the rope winds.

## 2.2 Balancing torques

In addition to balancing forces in a statics problem, we must also balance torques. We'll have much more to say about torque in Chapters 8 and 9, but we'll need one important fact here. Consider the situation in Fig. 2.4, where three forces are applied perpendicular to a stick, which is assumed to remain motionless.  $F_1$  and  $F_2$  are the forces at the ends, and  $F_3$  is the force in the interior. We have, of course,  $F_3 = F_1 + F_2$ , because the stick is at rest. But we also have the following relation:

**Claim 2.1** *If the system is motionless, then  $F_3a = F_2(a + b)$ . In other words, the torques (force times distance) around the left end cancel.<sup>2</sup> And you can show that they cancel around any other point, too.*

We'll prove this claim in Chapter 8 by using angular momentum, but let's give a short proof here.

**Proof:** We'll make one reasonable assumption, namely, that the correct relationship between the forces and distances is of the form,

$$F_3f(a) = F_2f(a + b), \quad (2.8)$$

where  $f(x)$  is a function to be determined.<sup>3</sup> Applying this assumption with the roles of “left” and “right” reversed in Fig. 2.4 gives

$$F_3f(b) = F_1f(a + b). \quad (2.9)$$

Adding Eqs. (2.8) and (2.9), and using  $F_3 = F_1 + F_2$ , yields

$$f(a) + f(b) = f(a + b). \quad (2.10)$$

This equation implies that  $f(rx) = rf(x)$  for any  $x$  and for any rational number  $r$ , as you can show (see Exercise 2.28). Therefore, assuming  $f(x)$  is continuous,

<sup>2</sup> Another proof of this claim is given in Problem 2.11.

<sup>3</sup> What we're doing here is simply assuming linearity in  $F$ . That is, two forces of  $F$  applied at a point should be the same as a force of  $2F$  applied at that point. You can't really argue with that.

![Diagram of a horizontal stick with three forces applied perpendicularly. Force F1 is an upward arrow at the left end. Force F2 is an upward arrow at the right end. Force F3 is a downward arrow at a point between the ends. The distance from the left end to the point of application of F3 is labeled 'a'. The distance from the point of application of F3 to the right end is labeled 'b'.](95711bcdc2664c457840a3dc799edb9f_img.jpg)

Diagram of a horizontal stick with three forces applied perpendicularly. Force F1 is an upward arrow at the left end. Force F2 is an upward arrow at the right end. Force F3 is a downward arrow at a point between the ends. The distance from the left end to the point of application of F3 is labeled 'a'. The distance from the point of application of F3 to the right end is labeled 'b'.

Fig. 2.4

it must be a linear function,  $f(x) = Ax$ , as we wanted to show. The constant  $A$  is irrelevant, because it cancels in Eq. (2.8). ■

Note that dividing Eq. (2.8) by Eq. (2.9) gives  $F_1 f(a) = F_2 f(b)$ , and hence  $F_1 a = F_2 b$ , which says that the torques cancel around the point where  $F_3$  is applied. You can show that the torques cancel around any arbitrary pivot point. When adding up all the torques in a given physical setup, it is of course required that you use the same pivot point when calculating each torque.

In the case where the forces aren't perpendicular to the stick, the above claim applies to the components of the forces perpendicular to the stick. This makes sense, because the components parallel to the stick have no effect on the rotation of the stick around the pivot point. Therefore, referring to Figs. 2.5 and 2.6, the equality of the torques can be written as

$$F_a a \sin \theta_a = F_b b \sin \theta_b. \quad (2.11)$$

![Figure 2.5: A diagram showing a horizontal lever arm with a pivot point. A force F_a is applied at a distance 'a' to the left of the pivot, at an angle theta_a to the lever arm. A dashed line indicates the perpendicular component of the force, labeled F_a sin theta_a. A force F_b is applied at a distance 'b' to the right of the pivot, at an angle theta_b to the lever arm. A dashed line indicates the perpendicular component of the force, labeled F_b sin theta_b.](967e08f00a4fffdc167c53c3bad53c84_img.jpg)

Figure 2.5: A diagram showing a horizontal lever arm with a pivot point. A force F\_a is applied at a distance 'a' to the left of the pivot, at an angle theta\_a to the lever arm. A dashed line indicates the perpendicular component of the force, labeled F\_a sin theta\_a. A force F\_b is applied at a distance 'b' to the right of the pivot, at an angle theta\_b to the lever arm. A dashed line indicates the perpendicular component of the force, labeled F\_b sin theta\_b.

Fig. 2.5

This equation can be viewed in two ways:

- $(F_a \sin \theta_a)a = (F_b \sin \theta_b)b$ . In other words, we effectively have smaller forces acting on the given “lever arms,” as shown in Fig. 2.5.
- $F_a(a \sin \theta_a) = F_b(b \sin \theta_b)$ . In other words, we effectively have the given forces acting on smaller “lever arms,” as shown in Fig. 2.6.

![Figure 2.6: A diagram showing the same lever arm setup as Fig. 2.5, but illustrating the forces acting on smaller lever arms. The lever arms are represented by dashed lines perpendicular to the forces. The effective lever arm for F_a is labeled a sin theta_a, and for F_b it is labeled b sin theta_b. The angles theta_a and theta_b are shown between the original lever arm and the forces.](9d16b6273716dfae7a450ce9f52f47f0_img.jpg)

Figure 2.6: A diagram showing the same lever arm setup as Fig. 2.5, but illustrating the forces acting on smaller lever arms. The lever arms are represented by dashed lines perpendicular to the forces. The effective lever arm for F\_a is labeled a sin theta\_a, and for F\_b it is labeled b sin theta\_b. The angles theta\_a and theta\_b are shown between the original lever arm and the forces.

Fig. 2.6

Claim 2.1 shows that even if you apply only a tiny force, you can balance the torque due to a very large force, provided that you make your lever arm sufficiently long. This fact led a well-known mathematician of long ago to claim that he could move the earth if given a long enough lever arm.

One morning while eating my Wheaties,  
I felt the earth move ‘neath my feeties.  
The cause for alarm  
Was a long lever arm,  
At the end of which grinned Archimedes!

One handy fact that comes up often is that the gravitational torque on a stick of mass  $M$  is the same as the gravitational torque due to a point-mass  $M$  located at the center of the stick. The truth of this statement relies on the fact that torque is a linear function of the distance to the pivot point (see Exercise 2.27). More generally, the gravitational torque on an object of mass  $M$  may be treated simply as the gravitational torque due to a force  $Mg$  located at the center of mass.

We'll talk more about torque in Chapters 8 and 9, but for now we'll just use the fact that in a statics problem the torques around any given point must balance.

**Example (Leaning ladder):** A ladder leans against a frictionless wall. If the coefficient of friction with the ground is  $\mu$ , what is the smallest angle the ladder can make with the ground and not slip?

**Solution:** Let the ladder have mass  $m$  and length  $\ell$ . As shown in Fig. 2.7, we have three unknown forces: the friction force  $F$ , and the normal forces  $N_1$  and  $N_2$ . And to solve for these three forces we fortunately have three equations:  $\Sigma F_{\text{vert}} = 0$ ,  $\Sigma F_{\text{horiz}} = 0$ , and  $\Sigma \tau = 0$  ( $\tau$  is the standard symbol for torque). Looking at the vertical forces, we see that  $N_1 = mg$ . And then looking at the horizontal forces, we see that  $N_2 = F$ . So we have quickly reduced the unknowns from three to one.

We will now use  $\Sigma \tau = 0$  to find  $N_2$  (or  $F$ ). But first we must pick the “pivot” point around which we will calculate the torques. Any stationary point will work fine, but certain choices make the calculation easier than others. The best choice for the pivot is generally the point at which the most forces act, because then the  $\Sigma \tau = 0$  equation will have the smallest number of terms in it (because a force provides no torque around the point where it acts, since the lever arm is zero). In this problem, there are two forces acting at the bottom end of the ladder, so this is the point we’ll choose for the pivot (but you should verify that other choices for the pivot, for example, the middle or top of the ladder, give the same result). Balancing the torques due to gravity and  $N_2$ , we have

$$N_2 \ell \sin \theta = mg(\ell/2) \cos \theta \implies N_2 = \frac{mg}{2 \tan \theta}. \quad (2.12)$$

This is also the value of the friction force  $F$ . The condition  $F \leq \mu N_1 = \mu mg$  therefore becomes

$$\frac{mg}{2 \tan \theta} \leq \mu mg \implies \tan \theta \geq \frac{1}{2\mu}. \quad (2.13)$$

**REMARKS:** Note that the total force exerted on the ladder by the floor points up at an angle given by  $\tan \beta = N_1/F = (mg)/(mg/2 \tan \theta) = 2 \tan \theta$ . We see that this force does *not* point along the ladder. There is simply no reason why it should. But there *is* a nice reason why it should point upward with twice the slope of the ladder. This is the direction that causes the lines of the three forces on the ladder to be concurrent (that is, pass through a common point), as shown in Fig. 2.8. This concurrency is a neat little theorem for statics problems involving three forces. The proof is simple. If the three lines weren’t concurrent, then one force would produce a nonzero torque around the intersection point of the other two lines of force.<sup>4</sup>

This theorem provides a quick way to solve the ladder problem in the more general case where the center of mass is a fraction  $f$  of the way up. In this case, the concurrency theorem tells us that the slope of the total force from the floor is  $(1/f) \tan \theta$ , consistent with the  $f = 1/2$  result from above. The vertical component is still  $mg$ , so the horizontal (friction) component is now  $fmg/\tan \theta$ . Demanding that this be less than or equal to  $\mu mg$  gives  $\tan \theta \geq f/\mu$ , consistent with the  $f = 1/2$  result. Since this result depends

![Diagram of a ladder leaning against a wall. The ladder has length l and makes an angle theta with the ground. The forces acting on it are: N2 (normal force from the wall, horizontal, pointing right) at the top; mg (weight, vertical, pointing down) at the center; N1 (normal force from the ground, vertical, pointing up) and F (friction force from the ground, horizontal, pointing left) at the bottom.](27e73929f5b2213f05a03780069c9f9b_img.jpg)

Diagram of a ladder leaning against a wall. The ladder has length l and makes an angle theta with the ground. The forces acting on it are: N2 (normal force from the wall, horizontal, pointing right) at the top; mg (weight, vertical, pointing down) at the center; N1 (normal force from the ground, vertical, pointing up) and F (friction force from the ground, horizontal, pointing left) at the bottom.

Fig. 2.7

![Diagram showing the concurrency of the three forces acting on the ladder. The forces are N2 (horizontal, right), mg (vertical, down), and F_floor (total force from the floor, pointing up and to the right). Dashed lines extend from the lines of action of N2 and mg, and they intersect at a point. The line of action of F_floor also passes through this intersection point, demonstrating concurrency.](4ffe526d9c3143a38cd267b2f79a4062_img.jpg)

Diagram showing the concurrency of the three forces acting on the ladder. The forces are N2 (horizontal, right), mg (vertical, down), and F\_floor (total force from the floor, pointing up and to the right). Dashed lines extend from the lines of action of N2 and mg, and they intersect at a point. The line of action of F\_floor also passes through this intersection point, demonstrating concurrency.

Fig. 2.8

<sup>4</sup> The one exception to this reasoning is where no two of the lines intersect, that is, where all three lines are parallel. Equilibrium is certainly possible in such a scenario, as we saw in Claim 2.1. But you can hang on to the concurrency theorem in this case if you consider the parallel lines to meet at infinity.

only on the location of the center of mass, and not on the exact distribution of mass, a corollary is that if you climb up a ladder (resting on a frictionless wall), your presence makes the ladder more likely to slip if you are above the center of mass (because you have raised the center of mass of the entire system and thus increased  $f$ ), and less likely if you are below. ♣

The examples we've done in this chapter have consisted of only one object. But many problems involve more than one object (as you'll find in the problems and exercises for this chapter), and there's one additional fact you'll often need to invoke for these, namely Newton's third law. This states that the force that object  $A$  exerts on object  $B$  is equal and opposite to the force that  $B$  exerts on  $A$  (we'll talk more about Newton's laws in Chapter 3). So if you want to find, say, the normal force between two objects, you might be able to figure it out by looking at forces and torques on either object, depending on how much you already know about the other forces acting on each. Once you've found the force by dealing with, say, object  $A$ , you can then use the equal and opposite force to help figure out things about  $B$ . Depending on the problem, one object is often more useful than the other to use first.

Note, however, that if you pick your subsystem (on which you're going to consider forces and torques) to include both  $A$  and  $B$ , then this won't tell you anything at all about the normal force (or friction) between them. This is true because the normal force is an *internal* force between the objects (when considered together as a system), whereas only *external* forces are relevant in calculating the total force and torque on the system (because all the internal forces cancel in pairs, by Newton's third law). The only way to determine a given force is to deal with it as an external force on some subsystem(s).

Statics problems often involve a number of decisions. If there are various parts to the system, then you must decide which subsystems you want to balance the external forces and torques on. And furthermore, you must decide which point to use as the origin for calculating the torques. There are invariably many choices that will give you the information you need, but some will make your calculations much cleaner than others (Exercise 2.35 is a good example of this). The only way to know how to choose wisely is to start solving problems, so you may as well tackle some . . .

## 2.3 Problems

### Section 2.1: Balancing forces

#### 2.1. Hanging rope

A rope with length  $L$  and mass density per unit length  $\rho$  is suspended vertically from one end. Find the tension as a function of height along the rope.

#### 2.2. Block on a plane

A block sits on a plane that is inclined at an angle  $\theta$ . Assume that the friction force is large enough to keep the block at rest. What are the horizontal components of the friction and normal forces acting on the block? For what  $\theta$  are these horizontal components maximum?

#### 2.3. Motionless chain \*

A frictionless tube lies in the vertical plane and is in the shape of a function that has its endpoints at the same height but is otherwise arbitrary. A chain with uniform mass per unit length lies in the tube from end to end, as shown in Fig. 2.9. Show, by considering the net force of gravity along the curve, that the chain doesn't move.

![Diagram of a chain in a wavy tube.](1675c9ac5116bd7a283fe5bdbf53f969_img.jpg)

A diagram showing a wavy, tube-like structure in a vertical plane. A chain is shown inside the tube, conforming to its shape. The endpoints of the tube are at the same height.

Diagram of a chain in a wavy tube.

Fig. 2.9

#### 2.4. Keeping a book up \*

A book of mass  $M$  is positioned against a vertical wall. The coefficient of friction between the book and the wall is  $\mu$ . You wish to keep the book from falling by pushing on it with a force  $F$  applied at an angle  $\theta$  with respect to the horizontal ( $-\pi/2 < \theta < \pi/2$ ), as shown in Fig. 2.10.

- For a given  $\theta$ , what is the minimum  $F$  required?
- For what  $\theta$  is this minimum  $F$  the smallest? What is the corresponding minimum  $F$ ?
- What is the limiting value of  $\theta$ , below which there does not exist an  $F$  that keeps the book up?

![Diagram of a book against a wall with a force F applied.](845eb03ced798e39f70d8e3cc96f040f_img.jpg)

A diagram showing a rectangular block of mass

 $M$ 

against a vertical wall. A force

 $F$ 

is applied to the block at an angle

 $\theta$ 

above the horizontal. The coefficient of friction between the block and the wall is

 $\mu$ 

.

Diagram of a book against a wall with a force F applied.

Fig. 2.10

#### 2.5. Rope on a plane \*

A rope with length  $L$  and mass density per unit length  $\rho$  lies on a plane inclined at an angle  $\theta$  (see Fig. 2.11). The top end is nailed to the plane, and the coefficient of friction between the rope and the plane is  $\mu$ . What are the possible values for the tension at the top of the rope?

![Diagram of a rope on an inclined plane.](5cdf7bb3c1fa5a586edd6ff715fb133c_img.jpg)

A diagram showing a rope of length

 $L$ 

on an inclined plane at an angle

 $\theta$ 

to the horizontal. The top end of the rope is fixed to the plane. The coefficient of friction between the rope and the plane is

 $\mu$ 

.

Diagram of a rope on an inclined plane.

Fig. 2.11

#### 2.6. Supporting a disk \*\*

- A disk of mass  $M$  and radius  $R$  is held up by a massless string, as shown in Fig. 2.12. The surface of the disk is frictionless. What is the tension in the string? What is the normal force per unit length that the string applies to the disk?
- Let there now be friction between the disk and the string, with coefficient  $\mu$ . What is the smallest possible tension in the string at its lowest point?

![Diagram of a disk supported by a string.](32e18551bae542425ec96044f8818887_img.jpg)

A diagram showing a circular disk of mass

 $M$ 

and radius

 $R$ 

suspended by a string. The string is attached to two fixed points above the disk and wraps around the bottom half of the disk.

Diagram of a disk supported by a string.

Fig. 2.12

#### 2.7. Objects between circles \*\*

Each of the following planar objects is placed, as shown in Fig. 2.13, between two frictionless circles of radius  $R$ . The mass density per unit

![Figure 2.13: Three diagrams showing two circles of radius R in contact, with a third object of length L pressing them together. (a) An isosceles triangle with common side length L. (b) A rectangle with height L. (c) A circle. In each case, a horizontal force F is applied to the left and right circles, and the angle theta is shown between the horizontal and the line connecting the center of a circle to the point of contact with the third object.](01712d1aeaf42b2237e90a7cb423fe99_img.jpg)

Figure 2.13: Three diagrams showing two circles of radius R in contact, with a third object of length L pressing them together. (a) An isosceles triangle with common side length L. (b) A rectangle with height L. (c) A circle. In each case, a horizontal force F is applied to the left and right circles, and the angle theta is shown between the horizontal and the line connecting the center of a circle to the point of contact with the third object.

Fig. 2.13

![Figure 2.14: A diagram of a hanging chain (catenary) between two vertical walls. The horizontal distance between the walls is d, the vertical distance between the support points is lambda, and the total length of the chain is l.](48e4a08eda427e3eca16c3cb8ef68e61_img.jpg)

Figure 2.14: A diagram of a hanging chain (catenary) between two vertical walls. The horizontal distance between the walls is d, the vertical distance between the support points is lambda, and the total length of the chain is l.

Fig. 2.14

![Figure 2.15: A diagram of a hanging chain (catenary) between two vertical walls. The horizontal distance between the walls is 2d, and the total length of the chain is l = ?.](46a3aaaa16c32e851710b0223cd1c656_img.jpg)

Figure 2.15: A diagram of a hanging chain (catenary) between two vertical walls. The horizontal distance between the walls is 2d, and the total length of the chain is l = ?.

Fig. 2.15

![Figure 2.16: A diagram of a conical mountain with apex angle alpha. A rope is draped over the top and hangs down both sides.](33edb527bae42a1b04818001d817a1cd_img.jpg)

Figure 2.16: A diagram of a conical mountain with apex angle alpha. A rope is draped over the top and hangs down both sides.

Fig. 2.16

area of each object is  $\sigma$ , and the radii to the points of contact make an angle  $\theta$  with the horizontal. For each case, find the horizontal force that must be applied to the circles to keep them together. For what  $\theta$  is this force maximum or minimum?

- An isosceles triangle with common side length  $L$ .
- A rectangle with height  $L$ .
- A circle.

#### 2.8. Hanging chain \*\*\*\*

- A chain with uniform mass density per unit length hangs between two given points on two walls. Find the general shape of the chain. Aside from an arbitrary additive constant, the function describing the shape should contain one unknown constant. (The shape of a hanging chain is known as a *catenary*.)
- The unknown constant in your answer depends on the horizontal distance  $d$  between the walls, the vertical distance  $\lambda$  between the support points, and the length  $\ell$  of the chain (see Fig. 2.14). Find an equation involving these given quantities that determines the unknown constant.

#### 2.9. Hanging gently \*\*

A chain with uniform mass density per unit length hangs between two supports located at the same height, a distance  $2d$  apart (see Fig. 2.15). What should the length of the chain be so that the magnitude of the force at the supports is minimized? You may use the fact that a hanging chain takes the form,  $y(x) = (1/\alpha) \cosh(\alpha x)$ . You will eventually need to solve an equation numerically.

#### 2.10. Mountain climber \*\*\*\*

A mountain climber wishes to climb up a frictionless conical mountain. He wants to do this by throwing a lasso (a rope with a loop) over the top and climbing up along the rope. Assume that the climber is of negligible height, so that the rope lies along the mountain, as shown in Fig. 2.16. At the bottom of the mountain are two stores. One sells “cheap” lassos (made of a segment of rope tied to a loop of *fixed* length); see Fig. 2.17. The other sells “deluxe” lassos (made of one piece of rope with a loop of *variable* length; the loop’s length may change without any friction of the rope with itself). When viewed from the side, the conical mountain has an angle  $\alpha$  at its peak. For what angles  $\alpha$  can the climber climb up along the mountain if he uses a “cheap” lasso? A “deluxe” lasso? (Hint: The answer in the “cheap” case isn’t  $\alpha < 90^\circ$ .)

### Section 2.2: Balancing torques

#### 2.11. Equality of torques \*\*

This problem gives another way of demonstrating Claim 2.1, using an inductive argument. We'll get you started, and then you can do the general case.

Consider the situation where forces  $F$  are applied upward at the ends of a stick of length  $\ell$ , and a force  $2F$  is applied downward at the midpoint (see Fig. 2.18). The stick doesn't rotate (by symmetry), and it doesn't translate (because the net force is zero). If we wish, we may consider the stick to have a pivot at the left end. If we then erase the force  $F$  on the right end and replace it with a force  $2F$  at the middle, then the two  $2F$  forces in the middle cancel, so the stick remains at rest.<sup>5</sup> Therefore, we see that a force  $F$  applied at a distance  $\ell$  from a pivot is equivalent to a force  $2F$  applied at a distance  $\ell/2$  from the pivot, in the sense that they both have the same effect in canceling out the rotational effect of the downwards  $2F$  force.

Now consider the situation where forces  $F$  are applied upward at the ends, and forces  $F$  are applied downward at the  $\ell/3$  and  $2\ell/3$  marks (see Fig. 2.19). The stick doesn't rotate (by symmetry), and it doesn't translate (because the net force is zero). Consider the stick to have a pivot at the left end. From the above paragraph, the force  $F$  at  $2\ell/3$  is equivalent to a force  $2F$  at  $\ell/3$ . Making this replacement, we now have a total force of  $3F$  at the  $\ell/3$  mark. Therefore, we see that a force  $F$  applied at a distance  $\ell$  is equivalent to a force  $3F$  applied at a distance  $\ell/3$ .

Your task is to now use induction to show that a force  $F$  applied at a distance  $\ell$  is equivalent to a force  $nF$  applied at a distance  $\ell/n$ , and to then argue why this demonstrates Claim 2.1.

#### 2.12. Direction of the tension \*

Show that the tension in a completely flexible rope, massive or massless, points along the rope everywhere in the rope.

#### 2.13. Find the force \*

A stick of mass  $M$  is held up by supports at each end, with each support providing a force of  $Mg/2$ . Now put another support somewhere in the middle, say, at a distance  $a$  from one support and  $b$  from the other; see Fig. 2.20. What forces do the three supports now provide? Is this solvable?

![Figure 2.17: Two balloons, one labeled 'cheap' and one labeled 'deluxe', are shown. The 'cheap' balloon is smaller and has a shorter string, while the 'deluxe' balloon is larger and has a longer string. Both are tied to a surface.](c85353bfa7e71d857da0c32ffd918904_img.jpg)

Figure 2.17: Two balloons, one labeled 'cheap' and one labeled 'deluxe', are shown. The 'cheap' balloon is smaller and has a shorter string, while the 'deluxe' balloon is larger and has a longer string. Both are tied to a surface.

Fig. 2.17

![Figure 2.18: A diagram of a horizontal stick. At the left end, there is a pivot point (a black dot). Upward forces F are applied at both ends. A downward force 2F is applied at the midpoint. A curved arrow on the right indicates a clockwise rotation.](aba440c20fd6423e8fc87d4873038d2d_img.jpg)

Figure 2.18: A diagram of a horizontal stick. At the left end, there is a pivot point (a black dot). Upward forces F are applied at both ends. A downward force 2F is applied at the midpoint. A curved arrow on the right indicates a clockwise rotation.

Fig. 2.18

![Figure 2.19: A diagram of a horizontal stick. Upward forces F are applied at both ends. Downward forces F are applied at the 1/3 and 2/3 marks. A curved arrow on the right indicates a clockwise rotation. Below this, a simplified diagram shows a pivot at the left end, an upward force F at the right end, and a combined downward force of 3F (labeled as F and 2F) at the 1/3 mark.](17fbb61d96bf2b8aa145613d861caa83_img.jpg)

Figure 2.19: A diagram of a horizontal stick. Upward forces F are applied at both ends. Downward forces F are applied at the 1/3 and 2/3 marks. A curved arrow on the right indicates a clockwise rotation. Below this, a simplified diagram shows a pivot at the left end, an upward force F at the right end, and a combined downward force of 3F (labeled as F and 2F) at the 1/3 mark.

Fig. 2.19

![Figure 2.20: A diagram of a horizontal stick of mass M. It is supported by three triangular supports. The left support is at the left end. The middle support is at a distance a from the left end. The right support is at a distance b from the middle support.](e1a67bec86e5e247d641cc827b3654a2_img.jpg)

Figure 2.20: A diagram of a horizontal stick of mass M. It is supported by three triangular supports. The left support is at the left end. The middle support is at a distance a from the left end. The right support is at a distance b from the middle support.

Fig. 2.20

<sup>5</sup> There is now a different force applied at the pivot, namely zero, but the purpose of the pivot is to simply apply whatever force is necessary to keep the left end motionless.

![Diagram for Fig. 2.21: Two sticks are joined at a right angle. One stick is horizontal on the ground, and the other stick leans against it, making an angle theta with the horizontal ground.](e71e57d5079f0622e5d3f6612ecce02e_img.jpg)

Diagram for Fig. 2.21: Two sticks are joined at a right angle. One stick is horizontal on the ground, and the other stick leans against it, making an angle theta with the horizontal ground.

Fig. 2.21

![Diagram for Fig. 2.22: A ladder of length L and mass M is hinged to the ground at an angle theta with the horizontal. A massless stick of length l is also hinged to the ground and is perpendicular to the ladder.](8e77aa74bd5ab059077bf9bdb397e287_img.jpg)

Diagram for Fig. 2.22: A ladder of length L and mass M is hinged to the ground at an angle theta with the horizontal. A massless stick of length l is also hinged to the ground and is perpendicular to the ladder.

Fig. 2.22

![Diagram for Fig. 2.23: A semi-infinite stick is balanced on a triangular support. The support is located at a distance l from the end of the stick.](a23d68fbeac8dd79417a4531ed4e0ed1_img.jpg)

Diagram for Fig. 2.23: A semi-infinite stick is balanced on a triangular support. The support is located at a distance l from the end of the stick.

Fig. 2.23

![Diagram for Fig. 2.24: A spool with an inner axle of radius r and an outer circle of radius R is on a horizontal surface. A thread is wrapped around the axle and is pulled with tension T at an angle theta with the horizontal.](ff33a4fbb84f26cd8f8935ef70fcc166_img.jpg)

Diagram for Fig. 2.24: A spool with an inner axle of radius r and an outer circle of radius R is on a horizontal surface. A thread is wrapped around the axle and is pulled with tension T at an angle theta with the horizontal.

Fig. 2.24

![Diagram for Fig. 2.25: A stick of length l rests on a circle of radius R. The stick is tangent to the circle at its upper end and makes an angle theta with the horizontal ground.](8d728307c6c2c88ee65044a1cc5e54c6_img.jpg)

Diagram for Fig. 2.25: A stick of length l rests on a circle of radius R. The stick is tangent to the circle at its upper end and makes an angle theta with the horizontal ground.

Fig. 2.25

#### **2.14. Leaning sticks \***

One stick leans on another as shown in Fig. 2.21. A right angle is formed where they meet, and the right stick makes an angle  $\theta$  with the horizontal. The left stick extends infinitesimally beyond the end of the right stick. The coefficient of friction between the two sticks is  $\mu$ . The sticks have the same mass density per unit length and are both hinged at the ground. What is the minimum angle  $\theta$  for which the sticks don't fall?

#### **2.15. Supporting a ladder \***

A ladder of length  $L$  and mass  $M$  has its bottom end attached to the ground by a pivot. It makes an angle  $\theta$  with the horizontal and is held up by a massless stick of length  $l$  that is also attached to the ground by a pivot (see Fig. 2.22). The ladder and the stick are perpendicular to each other. Find the force that the stick exerts on the ladder.

#### **2.16. Balancing the stick \*\***

Given a semi-infinite stick (that is, one that goes off to infinity in one direction), determine how its density should depend on position so that it has the following property: If the stick is cut at an arbitrary location, the remaining semi-infinite piece will balance on a support that is located a distance  $l$  from the end (see Fig. 2.23).

#### **2.17. The spool \*\***

A spool consists of an axle of radius  $r$  and an outside circle of radius  $R$  which rolls on the ground. A thread is wrapped around the axle and is pulled with tension  $T$  at an angle  $\theta$  with the horizontal (see Fig. 2.24).

- Given  $R$  and  $r$ , what should  $\theta$  be so that the spool doesn't move? Assume that the friction between the spool and the ground is large enough so that the spool doesn't slip.
- Given  $R$ ,  $r$ , and the coefficient of friction  $\mu$  between the spool and the ground, what is the largest value of  $T$  for which the spool remains at rest?
- Given  $R$  and  $\mu$ , what should  $r$  be so that you can make the spool slip from the static position with as small a  $T$  as possible? That is, what should  $r$  be so that the upper bound on  $T$  in part (b) is as small as possible? What is the resulting value of  $T$ ?

#### **2.18. Stick on a circle \*\***

A stick of mass density per unit length  $\rho$  rests on a circle of radius  $R$  (see Fig. 2.25). The stick makes an angle  $\theta$  with the horizontal and is tangent to the circle at its upper end. Friction exists at all points of contact, and assume that it is large enough to keep the system at rest. Find the friction force between the ground and the circle.

#### **2.19. Leaning sticks and circles \*\*\***

A large number of sticks (with mass density per unit length  $\rho$ ) and circles (with radius  $R$ ) lean on each other, as shown in Fig. 2.26. Each stick makes an angle  $\theta$  with the horizontal and is tangent to the next circle at its upper end. The sticks are hinged to the ground, and every other surface is *frictionless* (unlike in the previous problem). In the limit of a very large number of sticks and circles, what is the normal force between a stick and the circle it rests on, very far to the right? Assume that the last circle leans against a wall, to keep it from moving.

![Diagram for Problem 2.19 showing a series of circles and sticks leaning against each other. The first stick is hinged to the ground at an angle theta and is tangent to the first circle of radius R. Subsequent circles lean against the previous stick and each other, extending to the right.](56e84c995475881d51fe00e91918d129_img.jpg)

Diagram for Problem 2.19 showing a series of circles and sticks leaning against each other. The first stick is hinged to the ground at an angle theta and is tangent to the first circle of radius R. Subsequent circles lean against the previous stick and each other, extending to the right.

Fig. 2.26

## **2.4 Exercises**

### *Section 2.1: Balancing forces*

#### **2.20. Block under an overhang \***

A block of mass  $M$  is positioned underneath an overhang that makes an angle  $\beta$  with the horizontal. You apply a horizontal force of  $Mg$  on the block, as shown in Fig. 2.27. Assume that the friction force between the block and the overhang is large enough to keep the block at rest. What are the normal and friction forces (call them  $N$  and  $F_f$ ) that the overhang exerts on the block? If the coefficient of static friction is  $\mu$ , for what range of angles  $\beta$  does the block in fact remain at rest?

![Diagram for Problem 2.20 showing a block of mass M on a horizontal surface. A diagonal overhang is positioned above the block, making an angle beta with the horizontal. A horizontal force Mg is applied to the block towards the overhang.](404d225c4e3f13274e5aa6389f270125_img.jpg)

Diagram for Problem 2.20 showing a block of mass M on a horizontal surface. A diagonal overhang is positioned above the block, making an angle beta with the horizontal. A horizontal force Mg is applied to the block towards the overhang.

Fig. 2.27

#### **2.21. Pulling a block \***

A person pulls on a block with a force  $F$ , at an angle  $\theta$  with respect to the horizontal. The coefficient of friction between the block and the ground is  $\mu$ . For what  $\theta$  is the  $F$  required to make the block slip a minimum? What is the corresponding  $F$ ?

#### **2.22. Holding a cone \***

With two fingers, you hold an ice cream cone motionless upside down, as shown in Fig. 2.28. The mass of the cone is  $m$ , and the coefficient of static friction between your fingers and the cone is  $\mu$ . When viewed from the side, the angle of the tip is  $2\theta$ . What is the minimum normal force you must apply with each finger in order to hold up the cone? In terms of  $\theta$ , what is the minimum value of  $\mu$  that allows you to hold up the cone? Assume that you can supply as large a normal force as needed.

![Diagram for Problem 2.22 showing an inverted cone held by two fingers. The fingers are positioned on opposite sides of the cone's tip, each at an angle theta from the vertical dashed line. The cone has a mass m.](654146f2023ad445ec1208a6d7ef7cfd_img.jpg)

Diagram for Problem 2.22 showing an inverted cone held by two fingers. The fingers are positioned on opposite sides of the cone's tip, each at an angle theta from the vertical dashed line. The cone has a mass m.

Fig. 2.28

#### **2.23. Keeping a book up \*\***

The task of Problem 2.4 is to find the minimum force required to keep a book up. What is the maximum allowable force, as a function of  $\theta$  and  $\mu$ ? Is there a special angle that arises? Given  $\mu$ , make a rough plot of the allowed values of  $F$  for  $-\pi/2 < \theta < \pi/2$ .

![Figure 2.29: Two truss bridge diagrams. The top diagram shows a bridge made of three equilateral triangles with a mass m at the center. The bottom diagram shows a bridge made of seven equilateral triangles with a mass m at the center.](4c8721520bc36623aa6c19562146bab9_img.jpg)

Figure 2.29: Two truss bridge diagrams. The top diagram shows a bridge made of three equilateral triangles with a mass m at the center. The bottom diagram shows a bridge made of seven equilateral triangles with a mass m at the center.

Fig. 2.29

#### 2.24. Bridges \*\*

- Consider the first bridge in Fig. 2.29, made of three equilateral triangles of beams. Assume that the seven beams are massless and that the connection between any two of them is a hinge. If a car of mass  $m$  is located at the middle of the bridge, find the forces (and specify tension or compression) in the beams. Assume that the supports provide no horizontal forces on the bridge.
- Same question, but now with the second bridge in Fig. 2.29, made of seven equilateral triangles.
- Same question, but now with the general case of  $4n - 1$  equilateral triangles.

![Figure 2.30: A diagram showing a rope resting on two inclined platforms. The platforms are inclined at an angle theta to the horizontal. The rope forms a symmetric curve, with a portion of it not touching the platforms.](f0c43dde3e240812a7dbfd4ea880149b_img.jpg)

Figure 2.30: A diagram showing a rope resting on two inclined platforms. The platforms are inclined at an angle theta to the horizontal. The rope forms a symmetric curve, with a portion of it not touching the platforms.

Fig. 2.30

#### 2.25. Rope between inclines \*\*

A rope rests on two platforms that are both inclined at an angle  $\theta$  (which you are free to pick), as shown in Fig. 2.30. The rope has uniform mass density, and the coefficient of friction between it and the platforms is 1. The system has left-right symmetry. What is the largest possible fraction of the rope that does not touch the platforms? What angle  $\theta$  allows this maximum fraction?

#### 2.26. Hanging chain \*\*

A chain with mass  $M$  hangs between two walls, with its ends at the same height. The chain makes an angle  $\theta$  with each wall, as shown in Fig. 2.31. Find the tension in the chain at the lowest point. Solve this in two different ways:

![Figure 2.31: A diagram showing a hanging chain between two vertical walls. The chain is symmetric and makes an angle theta with each wall. The mass of the chain is M.](e4601e06bf50b50d72d9f0c551859b19_img.jpg)

Figure 2.31: A diagram showing a hanging chain between two vertical walls. The chain is symmetric and makes an angle theta with each wall. The mass of the chain is M.

Fig. 2.31

- Consider the forces on half of the chain. (This is the quick way.)
- Use the fact (see Problem 2.8) that the height of a hanging chain is given by  $y(x) = (1/\alpha) \cosh(\alpha x)$ , and consider the vertical forces on an infinitesimal piece at the bottom. This will give you the tension in terms of  $\alpha$ . Then find an expression for  $\alpha$  in terms of the given angle  $\theta$ . (This is the long way.)

### Section 2.2: Balancing torques

#### 2.27. Gravitational torque

A horizontal stick of mass  $M$  and length  $L$  is pivoted at one end. Integrate the gravitational torque along the stick (relative to the pivot), and show that the result is the same as the torque due to a mass  $M$  located at the center of the stick.

#### 2.28. Linear function \*

Show that if a function satisfies  $f(a) + f(b) = f(a + b)$ , then  $f(rx) = rf(x)$  for any  $x$  and for any rational number  $r$ .

#### **2.29. Direction of the force \***

A stick is connected to other parts of a static system by hinges at its ends. Show that (1) if the stick is massless, then the forces it feels at the hinges are directed along the stick, but (2) if the stick is massive, then the forces need not point along the stick.

#### **2.30. Ball on a wall \***

A ball is held up by a string, as shown in Fig. 2.32, with the string tangent to the ball. If the angle between the string and the wall is  $\theta$ , what is the minimum coefficient of static friction between the ball and the wall that keeps the ball from falling?

![Diagram for problem 2.30: A ball of radius r is held against a vertical wall by a string. The string is tangent to the top of the ball and makes an angle theta with the wall. The coefficient of static friction between the ball and the wall is mu.](6217eb6fdcc300d854c2ba3651151539_img.jpg)

Diagram for problem 2.30: A ball of radius r is held against a vertical wall by a string. The string is tangent to the top of the ball and makes an angle theta with the wall. The coefficient of static friction between the ball and the wall is mu.

Fig. 2.32

#### **2.31. Cylinder and hanging mass \***

A uniform cylinder of mass  $M$  sits on a fixed plane inclined at an angle  $\theta$ . A string is tied to the cylinder's rightmost point, and a mass  $m$  hangs from the string, as shown in Fig. 2.33. Assume that the coefficient of friction between the cylinder and the plane is sufficiently large to prevent slipping. What is  $m$ , in terms of  $M$  and  $\theta$ , if the setup is static?

![Diagram for problem 2.31: A cylinder of mass M is on an inclined plane at angle theta. A string is attached to the rightmost point of the cylinder and hangs vertically, supporting a mass m.](2e4c7df328c9438c5f0049f94b92f762_img.jpg)

Diagram for problem 2.31: A cylinder of mass M is on an inclined plane at angle theta. A string is attached to the rightmost point of the cylinder and hangs vertically, supporting a mass m.

Fig. 2.33

#### **2.32. Ladder on a corner \*\***

A ladder of mass  $M$  and length  $L$  leans against a frictionless wall, with a quarter of its length hanging over a corner, as shown in Fig. 2.34. It makes an angle  $\theta$  with the horizontal. What angle  $\theta$  requires the smallest coefficient of friction at the corner to keep the ladder at rest? (Different values of  $\theta$  require different ladder lengths, but assume that the mass is  $M$  for any length.)

![Diagram for problem 2.32: A ladder of length L and mass M is leaning against a vertical wall. A corner is located at a distance of L/4 from the bottom of the ladder. The ladder makes an angle theta with the horizontal.](9ce5929a8236e075f91db45143c90e83_img.jpg)

Diagram for problem 2.32: A ladder of length L and mass M is leaning against a vertical wall. A corner is located at a distance of L/4 from the bottom of the ladder. The ladder makes an angle theta with the horizontal.

Fig. 2.34

#### **2.33. Stick on a corner \*\***

You support one end of a stick of mass  $M$  and length  $L$  with the tip of your finger. A quarter of the way up the stick, it rests on a frictionless corner of a table, as shown in Fig. 2.35. The stick makes an angle  $\theta$  with the horizontal. What is the magnitude of the force your finger must apply to keep the stick in this position? For what angle  $\theta$  does your force point horizontally?

![Diagram for problem 2.33: A stick of length L and mass M is resting on a table corner. The stick makes an angle theta with the horizontal. A finger is shown supporting the left end of the stick.](967adb6a526d81170601333ef3ceb015_img.jpg)

Diagram for problem 2.33: A stick of length L and mass M is resting on a table corner. The stick makes an angle theta with the horizontal. A finger is shown supporting the left end of the stick.

Fig. 2.35

#### **2.34. Stick and a cylinder \*\***

A horizontal stick of mass  $m$  has its left end attached to a pivot on a plane inclined at an angle  $\theta$ , while its right end rests on the top of a cylinder also of mass  $m$  which in turn rests on the plane, as shown in Fig. 2.36. The coefficient of friction between the cylinder and both the stick and the plane is  $\mu$ .

![Diagram for problem 2.34: A stick of mass m is pivoted at its left end on an inclined plane at angle theta. The right end of the stick rests on a cylinder of mass m, which is also on the inclined plane. The coefficient of friction is mu.](e0d4e713efbe03067ab52243012f2459_img.jpg)

Diagram for problem 2.34: A stick of mass m is pivoted at its left end on an inclined plane at angle theta. The right end of the stick rests on a cylinder of mass m, which is also on the inclined plane. The coefficient of friction is mu.

Fig. 2.36

- (a) Assuming that the system is at rest, what is the normal force from the plane on the cylinder?

![Diagram for Fig. 2.37: Two sticks of mass m and length l are connected by a hinge at their top ends. They each make an angle theta with the vertical. A massless string connects the bottom of the left stick to the right stick, perpendicularly as shown. The whole setup stands on a frictionless table.](3a57f64da209a9901b8b669b80a6d7fd_img.jpg)

Diagram for Fig. 2.37: Two sticks of mass m and length l are connected by a hinge at their top ends. They each make an angle theta with the vertical. A massless string connects the bottom of the left stick to the right stick, perpendicularly as shown. The whole setup stands on a frictionless table.

Fig. 2.37

- (b) What is the smallest value of  $\mu$  (in terms of  $\theta$ ) for which the system doesn't slip anywhere?

#### **2.35. Two sticks and a string \*\***

Two sticks, each of mass  $m$  and length  $\ell$ , are connected by a hinge at their top ends. They each make an angle  $\theta$  with the vertical. A massless string connects the bottom of the left stick to the right stick, perpendicularly as shown in Fig. 2.37. The whole setup stands on a frictionless table.

- (a) What is the tension in the string?  
 (b) What force does the left stick exert on the right stick at the hinge?  
*Hint: No messy calculations required!*

![Diagram for Fig. 2.38: Two sticks are connected by hinges to each other and to a wall. The bottom stick is horizontal and has length L. The sticks make an angle theta with each other. The wall is vertical.](c59c57aa32d1de24f1b0cfca10bd7dd9_img.jpg)

Diagram for Fig. 2.38: Two sticks are connected by hinges to each other and to a wall. The bottom stick is horizontal and has length L. The sticks make an angle theta with each other. The wall is vertical.

Fig. 2.38

#### **2.36. Two sticks and a wall \*\***

Two sticks are connected, with hinges, to each other and to a wall. The bottom stick is horizontal and has length  $L$ , and the sticks make an angle of  $\theta$  with each other, as shown in Fig. 2.38. If both sticks have the same mass per unit length,  $\rho$ , find the horizontal and vertical components of the force that the wall exerts on the top hinge, and show that the magnitude goes to infinity for both  $\theta \rightarrow 0$  and  $\theta \rightarrow \pi/2$ .<sup>6</sup>

#### **2.37. Stick on a circle \*\***

Using the results from Problem 2.18 for the setup shown in Fig. 2.39, show that if the system is to remain at rest, then the coefficient of friction:

- (a) between the stick and the circle must satisfy

$$\mu \geq \frac{\sin \theta}{1 + \cos \theta}. \quad (2.14)$$

- (b) between the stick and the ground must satisfy<sup>7</sup>

$$\mu \geq \frac{\sin \theta \cos \theta}{(1 + \cos \theta)(2 - \cos \theta)}. \quad (2.15)$$

![Diagram for Fig. 2.39: A stick of length l is leaning against a circle of radius R. The stick makes an angle theta with the horizontal ground. The circle is on a horizontal surface.](80fe9170a209c78c645ea9ab0e0ccd67_img.jpg)

Diagram for Fig. 2.39: A stick of length l is leaning against a circle of radius R. The stick makes an angle theta with the horizontal ground. The circle is on a horizontal surface.

Fig. 2.39

#### **2.38. Stacking blocks \*\***

$N$  blocks of length  $\ell$  are stacked on top of each other at the edge of a table, as shown in Fig. 2.40 for  $N = 4$ . What is the largest horizontal

![Diagram for Fig. 2.40: Four blocks of length l are stacked on top of each other at the edge of a table. The blocks are offset from each other to maximize the overhang.](aedf08b81984d61fd838b2c21d9d1fa7_img.jpg)

Diagram for Fig. 2.40: Four blocks of length l are stacked on top of each other at the edge of a table. The blocks are offset from each other to maximize the overhang.

Fig. 2.40

<sup>6</sup> The force must therefore achieve a minimum at some intermediate angle. If you want to go through the algebra, you can show that this minimum occurs when  $\cos \theta = \sqrt{3} - 1$ , which gives  $\theta \approx 43^\circ$ .

<sup>7</sup> If you want to go through the algebra, you can show that the right-hand side achieves a maximum when  $\cos \theta = \sqrt{3} - 1$ , which gives  $\theta \approx 43^\circ$ . (Yes, I did just cut and paste this from the previous footnote. But it's still correct!) This is the angle for which the stick is most likely to slip on the ground.

distance the rightmost point on the top block can hang out beyond the table? How does your answer behave for  $N \rightarrow \infty$ ?<sup>8</sup>

## 2.5 Solutions

### 2.1. Hanging rope

Let  $T(y)$  be the tension as a function of height. Consider a small piece of the rope between  $y$  and  $y + dy$  ( $0 \leq y \leq L$ ). The forces on this piece are  $T(y + dy)$  upward,  $T(y)$  downward, and the weight  $\rho g dy$  downward. Since the rope is at rest, we have  $T(y + dy) = T(y) + \rho g dy$ . Expanding this to first order in  $dy$  gives  $T'(y) = \rho g$ . The tension in the bottom of the rope is zero, so integrating from  $y = 0$  up to a position  $y$  gives

$$T(y) = \rho gy. \quad (2.16)$$

As a double-check, at the top end we have  $T(L) = \rho gL$ , which is the weight of the entire rope, as it should be.

Alternatively, you can simply write down the answer,  $T(y) = \rho gy$ , by noting that the tension at a given point in the rope is what supports the weight of all the rope below it.

### 2.2. Block on a plane

Balancing the forces shown in Fig. 2.41, parallel and perpendicular to the plane, we see that  $F = mg \sin \theta$  and  $N = mg \cos \theta$ . The horizontal components of these are  $F \cos \theta = mg \sin \theta \cos \theta$  (to the right), and  $N \sin \theta = mg \cos \theta \sin \theta$  (to the left). These are equal, as they must be, because the net horizontal force on the block is zero. To maximize the value of  $mg \sin \theta \cos \theta$ , we can either take the derivative, or we can write it as  $(mg/2) \sin 2\theta$ , from which it is clear that the maximum occurs at  $\theta = \pi/4$ . The maximum value is  $mg/2$ .

![Diagram of a block on an inclined plane. The block is on a plane inclined at an angle theta to the horizontal. A normal force N acts perpendicular to the plane, and a force F acts parallel to the plane, pointing up the incline. The weight mg acts vertically downwards. The components of the weight parallel and perpendicular to the plane are shown as dashed arrows: mg sin theta pointing down the incline and mg cos theta pointing perpendicular to the incline.](065a5a5bfa37459e1d4a7bd53923f41c_img.jpg)

Diagram of a block on an inclined plane. The block is on a plane inclined at an angle theta to the horizontal. A normal force N acts perpendicular to the plane, and a force F acts parallel to the plane, pointing up the incline. The weight mg acts vertically downwards. The components of the weight parallel and perpendicular to the plane are shown as dashed arrows: mg sin theta pointing down the incline and mg cos theta pointing perpendicular to the incline.

Fig. 2.41

### 2.3. Motionless chain

Let the curve be described by the function  $f(x)$ , and let it run from  $x = a$  to  $x = b$ . Consider a little piece of the chain between  $x$  and  $x + dx$  (see Fig. 2.42). The length of this piece is  $\sqrt{1 + f'^2} dx$ , so its mass is  $\rho \sqrt{1 + f'^2} dx$ , where  $\rho$  is the mass per unit length. The component of the gravitational acceleration along the curve is  $-g \sin \theta = -gf' / \sqrt{1 + f'^2}$  (using  $\tan \theta = f'$ ), with positive corresponding to moving along the curve from  $a$  to  $b$ . The total force along the curve is therefore

$$\begin{aligned} F &= \int_a^b (-g \sin \theta) dm = \int_a^b \frac{-gf'}{\sqrt{1 + f'^2}} \cdot \rho \sqrt{1 + f'^2} dx \\ &= -g\rho \int_a^b f' dx \\ &= -g\rho(f(a) - f(b)) \\ &= 0. \end{aligned} \quad (2.17)$$

![Diagram of a curve segment. A curve is shown between x and x + dx. The vertical change is f' dx. The angle theta is shown between the horizontal and the curve. The length of the curve segment is indicated by a dashed line.](d29164f4cf3519c4bfa8d1ac4f237f6a_img.jpg)

Diagram of a curve segment. A curve is shown between x and x + dx. The vertical change is f' dx. The angle theta is shown between the horizontal and the curve. The length of the curve segment is indicated by a dashed line.

Fig. 2.42

### 2.4. Keeping a book up

- (a) The normal force from the wall is  $F \cos \theta$ , so the friction force  $F_f$  holding the book up is at most  $\mu F \cos \theta$ . The other vertical forces on the book are the

<sup>8</sup> It turns out that the method of stacking shown in Fig. 2.40 (with the blocks simply stacked on top of each other) doesn't yield the optimal overhang. See Hall (2005) for an interesting discussion of other methods.

gravitational force, which is  $-Mg$ , and the vertical component of  $F$ , which is  $F \sin \theta$ . If the book is to stay at rest, we must have  $F \sin \theta + F_f - Mg = 0$ . Combining this with the condition  $F_f \leq \mu F \cos \theta$  gives

$$F(\sin \theta + \mu \cos \theta) \geq Mg. \quad (2.18)$$

Therefore,  $F$  must satisfy

$$F \geq \frac{Mg}{\sin \theta + \mu \cos \theta}, \quad (2.19)$$

assuming that  $\sin \theta + \mu \cos \theta$  is positive. If it is negative, then there is no solution for  $F$ .

- (b) To minimize this lower bound, we must maximize the denominator. Taking the derivative gives  $\cos \theta - \mu \sin \theta = 0$ , so  $\tan \theta = 1/\mu$ . Plugging this value of  $\theta$  back into Eq. (2.19) gives

$$F \geq \frac{mg}{\sqrt{1 + \mu^2}} \quad (\text{with } \tan \theta = 1/\mu). \quad (2.20)$$

This is the smallest possible  $F$  that keeps the book up, and the angle must be  $\theta = \tan^{-1}(1/\mu)$  for it to work. We see that if  $\mu$  is very small, then to minimize your  $F$ , you should push essentially vertically with a force  $mg$ . But if  $\mu$  is very large, you should push essentially horizontally with a force  $mg/\mu$ .

- (c) There is no possible  $F$  that satisfies the condition in Eq. (2.19) if the right-hand side is infinite (more precisely, there is no  $F$  that satisfies Eq. (2.18) if the coefficient of  $F$  is zero or negative). This occurs when

$$\tan \theta = -\mu. \quad (2.21)$$

If  $\theta$  is more negative than this, then it is impossible to keep the book up, no matter how hard you push.

## 2.5. Rope on a plane

The component of the gravitational force along the plane is  $(\rho L)g \sin \theta$ , and the maximum value of the friction force is  $\mu N = \mu(\rho L)g \cos \theta$ . Therefore, you might think that the tension at the top of the rope is  $\rho Lg \sin \theta - \mu \rho Lg \cos \theta$ . However, this is not necessarily the case. The tension at the top depends on how the rope is placed on the plane. If, for example, the rope is placed on the plane without being stretched, then the friction force points upwards, and the tension at the top does indeed equal  $\rho Lg \sin \theta - \mu \rho Lg \cos \theta$ . Or it equals zero if  $\mu \rho Lg \cos \theta > \rho Lg \sin \theta$ , in which case the friction force need not achieve its maximum value.

If, on the other hand, the rope is placed on the plane after being stretched (or equivalently, it is dragged up along the plane and then nailed down at its top end), then the friction force points downwards, and the tension at the top equals  $\rho Lg \sin \theta + \mu \rho Lg \cos \theta$ .

Another special case occurs when the rope is placed on a frictionless plane, and then the coefficient of friction is “turned on” to  $\mu$ . The friction force is still zero. Changing the plane from ice to sandpaper (somehow without moving the rope) doesn’t suddenly cause there to be a friction force. Therefore, the tension at the top equals  $\rho Lg \sin \theta$ .

In general, depending on how the rope is placed on the plane, the tension at the top can take any value from a maximum of  $\rho Lg \sin \theta + \mu \rho Lg \cos \theta$ , down to a minimum of  $\rho Lg \sin \theta - \mu \rho Lg \cos \theta$  (or zero, whichever is larger). If the rope is replaced by a stick (which can support a compressive force), then the tension can achieve negative values down to  $\rho Lg \sin \theta - \mu \rho Lg \cos \theta$ , if this happens to be negative.

## 2.6. Supporting a disk

- (a) The gravitational force downward on the disk is  $Mg$ , and the force upward is  $2T$ . These forces must balance, so

$$T = \frac{Mg}{2}. \quad (2.22)$$

We can find the normal force per unit length that the string applies to the disk in two ways.

FIRST METHOD: Let  $N d\theta$  be the normal force on an arc of the disk that subtends an angle  $d\theta$ . Such an arc has length  $R d\theta$ , so  $N/R$  is the desired normal force per unit arclength. The tension in the string is the same throughout it, because the string is massless. So all points are equivalent, and hence  $N$  is constant, independent of  $\theta$ . The upward component of the normal force is  $N d\theta \cos \theta$ , where  $\theta$  is measured from the vertical (that is,  $-\pi/2 \leq \theta \leq \pi/2$  here). Since the total upward force is  $Mg$ , we must have

$$\int_{-\pi/2}^{\pi/2} N \cos \theta d\theta = Mg. \quad (2.23)$$

The integral equals  $2N$ , so we have  $N = Mg/2$ . The normal force per unit length,  $N/R$ , therefore equals  $Mg/2R$ .

SECOND METHOD: Consider the normal force,  $N d\theta$ , on a small arc of the disk that subtends an angle  $d\theta$ . The tension forces on each end of the corresponding small piece of string almost cancel, but they don't exactly, because they point in slightly different directions. Their nonzero sum is what produces the normal force on the disk. From Fig. 2.43, we see that the two forces have a sum of  $2T \sin(d\theta/2)$ , directed "inward". Since  $d\theta$  is small, we can use  $\sin x \approx x$  to approximate this as  $T d\theta$ . Therefore,  $N d\theta = T d\theta$ , and so  $N = T$ . The normal force per unit arclength,  $N/R$ , therefore equals  $T/R$ . Using  $T = Mg/2$  from Eq. (2.22), we arrive at  $N/R = Mg/2R$ .

- (b) Let  $T(\theta)$  be the tension, as a function of  $\theta$ , for  $-\pi/2 \leq \theta \leq \pi/2$ .  $T$  now depends on  $\theta$ , because there is a tangential friction force. Most of the work for this problem was already done in the "Rope wrapped around a pole" example in Section 2.1. We'll simply invoke Eq. (2.7), which in the present language says<sup>9</sup>

$$T(\theta) \leq T(0)e^{\mu\theta}. \quad (2.24)$$

Letting  $\theta = \pi/2$ , and using  $T(\pi/2) = Mg/2$ , gives  $Mg/2 \leq T(0)e^{\mu\pi/2}$ . We therefore see that the tension at the bottom point must satisfy

$$T(0) \geq \frac{Mg}{2} e^{-\mu\pi/2}. \quad (2.25)$$

REMARK: This minimum value of  $T(0)$  goes to  $Mg/2$  as  $\mu \rightarrow 0$ , as it should. And it goes to zero as  $\mu \rightarrow \infty$ , as it should (imagine a very rough surface, so that the friction force from the rope near  $\theta = \pi/2$  accounts for essentially all the weight). But interestingly, the tension at the bottom doesn't exactly equal zero, no matter how large  $\mu$  is. Basically, the smaller  $T$  is, the smaller  $N$  is. But the smaller  $N$  is, the smaller the change in  $T$  is (because  $N$  determines the friction force). So  $T$  doesn't decrease much when it's small, and this results in it never being able to reach zero. ♣

## 2.7. Objects between circles

- (a) Let  $N$  be the normal force between the circles and the triangle. The goal in this problem is to find the horizontal component of  $N$ , that is,  $N \cos \theta$ . From Fig. 2.44, we see that the upward force on the triangle from the normal forces is  $2N \sin \theta$ . This must equal the weight of the triangle, which is  $g\sigma$  times the area. Since the bottom angle of the isosceles triangle is  $2\theta$ , the top side has length

![Figure 2.43: A diagram showing a small arc of a disk subtending an angle dθ. Two tension forces T act at the ends of the arc, pointing away from the center. The resultant force of these two tensions is shown as a dashed vector pointing towards the center, labeled T sin(dθ/2).](95f52cee2f95f14f0e2ca400cf954e8b_img.jpg)

Figure 2.43: A diagram showing a small arc of a disk subtending an angle dθ. Two tension forces T act at the ends of the arc, pointing away from the center. The resultant force of these two tensions is shown as a dashed vector pointing towards the center, labeled T sin(dθ/2).

Fig. 2.43

![Figure 2.44: A diagram showing two circles in contact, supporting an isosceles triangle. The triangle's base is horizontal and its top vertex is between the circles. The normal force N is shown acting from the contact points on the triangle. The angle between the vertical and the line from the center of a circle to the contact point is θ. The bottom angle of the triangle is 2θ.](dfe0ca6e4e6faff98882161a24a65809_img.jpg)

Figure 2.44: A diagram showing two circles in contact, supporting an isosceles triangle. The triangle's base is horizontal and its top vertex is between the circles. The normal force N is shown acting from the contact points on the triangle. The angle between the vertical and the line from the center of a circle to the contact point is θ. The bottom angle of the triangle is 2θ.

Fig. 2.44

<sup>9</sup> This holds for  $\theta > 0$ . There would be a minus sign on the right-hand side if  $\theta < 0$ . But since the tension is symmetric around  $\theta = 0$  in the case we're concerned with, we'll just deal with  $\theta > 0$ .

![Diagram for Fig. 2.45 showing two circles of radius R in contact. A rectangle of length L and height N is placed on top of the right circle. A dashed line from the center of the right circle to the top of the rectangle makes an angle theta with the horizontal. The horizontal distance from the center to the top of the rectangle is R cos theta.](8ed1fcc71faf894c0fcd7cf17b85bcf9_img.jpg)

Diagram for Fig. 2.45 showing two circles of radius R in contact. A rectangle of length L and height N is placed on top of the right circle. A dashed line from the center of the right circle to the top of the rectangle makes an angle theta with the horizontal. The horizontal distance from the center to the top of the rectangle is R cos theta.

Fig. 2.45

$2L \sin \theta$ , and the altitude to this side is  $L \cos \theta$ . So the area of the triangle is  $L^2 \sin \theta \cos \theta$ . The mass is therefore  $\sigma L^2 \sin \theta \cos \theta$ . Equating the weight with the upward component of the normal forces gives  $N = (g\sigma L^2/2) \cos \theta$ . The horizontal component of  $N$  is therefore

$$N \cos \theta = \frac{g\sigma L^2 \cos^2 \theta}{2}. \quad (2.26)$$

This equals zero when  $\theta = \pi/2$ , and it increases as  $\theta$  decreases, even though the triangle is getting smaller. It has the interesting property of approaching the finite value  $g\sigma L^2/2$ , as  $\theta \rightarrow 0$ .

- (b) In Fig. 2.45, the base of the rectangle has length  $2R(1 - \cos \theta)$ . Its mass is therefore  $2\sigma RL(1 - \cos \theta)$ . Equating the weight with the upward component of the normal forces,  $2N \sin \theta$ , gives  $N = \sigma g RL(1 - \cos \theta)/\sin \theta$ . The horizontal component of  $N$  is therefore

$$N \cos \theta = \frac{\sigma g RL(1 - \cos \theta) \cos \theta}{\sin \theta}. \quad (2.27)$$

This equals zero for both  $\theta = \pi/2$  and  $\theta = 0$  (because  $1 - \cos \theta \approx \theta^2/2$  goes to zero faster than  $\sin \theta \approx \theta$ , for small  $\theta$ ). Taking the derivative to find where it reaches a maximum, we obtain (using  $\sin^2 \theta = 1 - \cos^2 \theta$ ),

$$\cos^3 \theta - 2 \cos \theta + 1 = 0. \quad (2.28)$$

Fortunately, there is an easy root of this cubic equation, namely  $\cos \theta = 1$ , which we know is not the maximum. Dividing through by the factor  $(\cos \theta - 1)$  gives  $\cos^2 \theta + \cos \theta - 1 = 0$ . The roots of this quadratic equation are

$$\cos \theta = \frac{-1 \pm \sqrt{5}}{2}. \quad (2.29)$$

We must choose the plus sign, because we need  $|\cos \theta| \leq 1$ . So our answer is  $\cos \theta \approx 0.618$ , which is the inverse of the golden ratio. The angle  $\theta$  is  $\approx 51.8^\circ$ .

- (c) In Fig. 2.46, the length of the hypotenuse shown is  $R \sec \theta$ , so the radius of the top circle is  $R(\sec \theta - 1)$ . Its mass is therefore  $\sigma \pi R^2(\sec \theta - 1)^2$ . Equating the weight with the upward component of the normal forces,  $2N \sin \theta$ , gives  $N = \sigma g \pi R^2(\sec \theta - 1)^2/(2 \sin \theta)$ . The horizontal component of  $N$  is therefore

$$N \cos \theta = \frac{\sigma g \pi R^2 \cos \theta}{2 \sin \theta} \left( \frac{1}{\cos \theta} - 1 \right)^2 = \frac{\sigma g \pi R^2 (1 - \cos \theta)^2}{2 \sin \theta \cos \theta}. \quad (2.30)$$

This equals zero when  $\theta = 0$  (using  $\cos \theta \approx 1 - \theta^2/2$  and  $\sin \theta \approx \theta$ , for small  $\theta$ ). For  $\theta \rightarrow \pi/2$ , it behaves like  $1/\cos \theta$ , which goes to infinity. In this limit,  $N$  points almost vertically, but its magnitude is so large that the horizontal component still approaches infinity.

![Diagram for Fig. 2.46 showing two circles of radius R in contact. A third, smaller circle is placed on top of the right circle. The center of the top circle is at a distance R sec theta from the center of the right circle. The radius of the top circle is R(sec theta - 1).](80b449039a0e0c83e77caa7cce498bda_img.jpg)

Diagram for Fig. 2.46 showing two circles of radius R in contact. A third, smaller circle is placed on top of the right circle. The center of the top circle is at a distance R sec theta from the center of the right circle. The radius of the top circle is R(sec theta - 1).

Fig. 2.46

## 2.8. Hanging chain

- (a) The key fact to note is that the horizontal component,  $T_x$ , of the tension is the same throughout the chain. This is true because the net horizontal force on any subpart of the chain must be zero. Label the constant value as  $T_x \equiv C$ .

Let the shape of the chain be described by the function  $y(x)$ . Since the tension points along the chain at all points (see Problem 2.12), its components satisfy  $T_y/T_x = y'$ , which gives  $T_y = Cy'$ . In other words,  $T_y$  is proportional to the slope of the chain.

Now consider a little piece of the chain, with endpoints at  $x$  and  $x + dx$ , as shown in Fig. 2.47. The difference in the  $T_y$  values at the endpoints is what balances the weight of the little piece,  $(dm)g$ . The length of the piece is  $ds = dx\sqrt{1 + y'^2}$ , so if  $\rho$  is the density, we have

![Diagram for Fig. 2.47 showing a small segment of a hanging chain. The segment has a horizontal length dx and a vertical length dy. The tension at the left end is T(x) and at the right end is T(x+dx). The weight of the segment is (dm)g.](76b00360af22b6b74a66544d7ab39141_img.jpg)

Diagram for Fig. 2.47 showing a small segment of a hanging chain. The segment has a horizontal length dx and a vertical length dy. The tension at the left end is T(x) and at the right end is T(x+dx). The weight of the segment is (dm)g.

Fig. 2.47

$$dT_y = (\rho ds)g = \rho g dx \sqrt{1 + y'^2} \implies \frac{dT_y}{dx} = \rho g \sqrt{1 + y'^2}. \quad (2.31)$$

Using the  $T_y = Cy'$  result from above, this becomes  $Cy'' = \rho g \sqrt{1 + y'^2}$ . Letting  $z \equiv y'$ , we can separate variables and integrate to obtain

$$\int \frac{dz}{\sqrt{1+z^2}} = \int \frac{\rho g dx}{C} \implies \sinh^{-1} z = \frac{\rho g x}{C} + A, \quad (2.32)$$

where  $A$  is a constant of integration. We can make this look a little cleaner if we define constants  $\alpha$  and  $a$  such that  $\alpha \equiv \rho g/C$  and  $a \equiv A/\alpha$ . We then obtain

$$\sinh^{-1} z = \alpha(x + a) \implies z = \sinh \alpha(x + a). \quad (2.33)$$

Recalling that  $z \equiv dy/dx$ , we can integrate again to obtain

$$y(x) = \frac{1}{\alpha} \cosh \alpha(x + a) + h. \quad (2.34)$$

The shape of the chain is therefore a hyperbolic cosine function. The constant  $h$  isn't too important, because it depends simply on where we pick the  $y = 0$  height. Furthermore, we can eliminate the need for the constant  $a$  if we pick  $x = 0$  to be where the lowest point of the chain is (or where it would be, in the case where the slope is always nonzero). In this case, using Eq. (2.34), we see that  $y'(0) = 0$  implies  $a = 0$ , as desired. We then have (ignoring the constant  $h$ ) the nice simple result,

$$y(x) = \frac{1}{\alpha} \cosh(\alpha x). \quad (2.35)$$

- (b) The constant  $\alpha$  can be determined from the locations of the endpoints and the length of the chain. As stated in the problem, the position of the chain may be described by giving (1) the horizontal distance  $d$  between the two endpoints, (2) the vertical distance  $\lambda$  between the two endpoints, and (3) the length  $\ell$  of the chain, as shown in Fig. 2.48. Note that it isn't obvious what the horizontal distances between the ends and the minimum point (which we have chosen as the  $x = 0$  point) are. If  $\lambda = 0$ , then these distances are  $d/2$ , by symmetry. But otherwise, they aren't so clear.

If we let the left endpoint be located at  $x = -x_0$ , then the first of the above three facts says that the right endpoint is located at  $x = d - x_0$ . We now have two unknowns,  $x_0$  and  $\alpha$ . The second fact tells us that (we'll take the right end to be higher than the left end, without loss of generality)

$$y(d - x_0) - y(-x_0) = \lambda. \quad (2.36)$$

And the third fact gives, using Eq. (2.35),

$$\ell = \int_{-x_0}^{d-x_0} \sqrt{1 + y'^2} dx = \frac{1}{\alpha} \sinh(\alpha x) \Big|_{-x_0}^{d-x_0}, \quad (2.37)$$

where we have used  $(d/du) \cosh u = \sinh u$ , and  $1 + \sinh^2 u = \cosh^2 u$ , and  $\int \cosh u = \sinh u$ . Writing out Eqs. (2.36) and (2.37) explicitly, we have

$$\begin{aligned} \cosh(\alpha(d - x_0)) - \cosh(-\alpha x_0) &= \alpha \lambda, \\ \sinh(\alpha(d - x_0)) - \sinh(-\alpha x_0) &= \alpha \ell. \end{aligned} \quad (2.38)$$

We can eliminate  $x_0$  by taking the difference of the squares of these two equations. Using the hyperbolic identities  $\cosh^2 u - \sinh^2 u = 1$  and  $\cosh u \cosh v - \sinh u \sinh v = \cosh(u - v)$ , we obtain

$$2 \cosh(\alpha d) - 2 = \alpha^2(\ell^2 - \lambda^2). \quad (2.39)$$

This is the desired equation that determines  $\alpha$ . Given  $d$ ,  $\lambda$ , and  $\ell$ , we can numerically solve for  $\alpha$ . Using a “half-angle” formula, you can show that Eq. (2.39) may also be written as

$$2 \sinh(\alpha d/2) = \alpha \sqrt{\ell^2 - \lambda^2}. \quad (2.40)$$

![Diagram of a catenary curve between two vertical supports. The horizontal distance between the supports is labeled 'd'. The vertical distance between the endpoints is labeled 'lambda'. The length of the chain is labeled 'l'. The endpoints are at horizontal positions -x_0 and d - x_0, with the minimum point at x = 0.](a8a1a6be83dea5e35b663e7d44d4ad49_img.jpg)

The figure shows a catenary curve representing a chain hanging between two vertical supports. The horizontal distance between the supports is labeled  $d$ . The vertical distance between the endpoints is labeled  $\lambda$ . The length of the chain is labeled  $\ell$ . The endpoints are located at horizontal positions  $-x_0$  and  $d - x_0$ , with the minimum point of the chain at  $x = 0$ .

Diagram of a catenary curve between two vertical supports. The horizontal distance between the supports is labeled 'd'. The vertical distance between the endpoints is labeled 'lambda'. The length of the chain is labeled 'l'. The endpoints are at horizontal positions -x\_0 and d - x\_0, with the minimum point at x = 0.

Fig. 2.48

REMARK: Let's check a couple limits. If  $\lambda = 0$  and  $\ell = d$  (that is, the chain forms a horizontal straight line), then Eq. (2.40) becomes  $2 \sinh(\alpha d/2) = \alpha d$ . The solution to this is  $\alpha = 0$ , which does indeed correspond to a horizontal straight line, because for small  $\alpha$ , we can use  $\cosh \epsilon \approx 1 + \epsilon^2/2$  to say that the  $y(x)$  in Eq. (2.35) behaves like  $\alpha x^2/2$  (up to an additive constant), which varies slowly with  $x$  for small  $\alpha$ . Another limit is where  $\ell$  is much larger than both  $d$  and  $\lambda$ . In this case, Eq. (2.40) becomes  $2 \sinh(\alpha d/2) \approx \alpha \ell$ . The solution to this is a large  $\alpha$  (or more precisely,  $\alpha \gg 1/d$ ), which corresponds to a “droopy” chain, because the  $y(x)$  in Eq. (2.35) varies rapidly with  $x$  for large  $\alpha$ . ♣

## 2.9. Hanging gently

We must first find the mass of the chain by calculating its length. Then we must determine the slope of the chain at the supports, so we can find the components of the force there. Using the given information,  $y(x) = (1/\alpha) \cosh(\alpha x)$ , the slope of the chain as a function of  $x$  is

$$y' = \frac{d}{dx} \left( \frac{1}{\alpha} \cosh(\alpha x) \right) = \sinh(\alpha x). \quad (2.41)$$

The total length is therefore (using  $1 + \sinh^2 z = \cosh^2 z$ )

$$\ell = \int_{-d}^d \sqrt{1 + y'^2} dx = \int_{-d}^d \cosh(\alpha x) dx = \frac{2}{\alpha} \sinh(\alpha d). \quad (2.42)$$

The weight of the rope is  $W = \rho \ell g$ , where  $\rho$  is the mass per unit length. Each support applies a vertical force of  $W/2$ . So this equals  $F \sin \theta$ , where  $F$  is the magnitude of the force at each support, and  $\theta$  is the angle it makes with the horizontal. Since  $\tan \theta = y'(d) = \sinh(\alpha d)$ , we see from Fig. 2.49 that  $\sin \theta = \tanh(\alpha d)$ . Therefore,

$$F = \frac{1}{\sin \theta} \cdot \frac{W}{2} = \frac{1}{\tanh(\alpha d)} \cdot \frac{\rho g \sinh(\alpha d)}{\alpha} = \frac{\rho g}{\alpha} \cosh(\alpha d). \quad (2.43)$$

Taking the derivative of this (as a function of  $\alpha$ ), and setting the result equal to zero to find the minimum, gives  $\tanh(\alpha d) = 1/(\alpha d)$ . This must be solved numerically. The result is

$$\alpha d \approx 1.1997 \equiv \eta. \quad (2.44)$$

So  $\alpha$  is given by  $\alpha = \eta/d$ , and the shape of the chain that requires the minimum  $F$  is thus

$$y(x) \approx \frac{d}{\eta} \cosh\left(\frac{\eta x}{d}\right). \quad (2.45)$$

From Eqs. (2.42) and (2.44), the length of the chain is  $\ell = (2d/\eta) \sinh(\eta) \approx (2.52)d$ . To further get an idea of what the chain looks like, we can calculate the ratio of the height,  $h$ , to the width,  $2d$ .

$$\frac{h}{2d} = \frac{y(d) - y(0)}{2d} = \frac{\cosh(\eta) - 1}{2\eta} \approx 0.338. \quad (2.46)$$

We can also calculate the angle of the rope at the supports, using  $\tan \theta = \sinh(\alpha d)$ . This gives  $\tan \theta = \sinh \eta$ , and so  $\theta \approx 56.5^\circ$ .

REMARK: We can also ask what shape the chain should take in order to minimize the horizontal or vertical component of  $F$ . The vertical component,  $F_y$ , is simply half the weight, so we want the shortest possible chain, namely a horizontal one (which requires an infinite  $F$ ). This corresponds to  $\alpha = 0$ . The horizontal component,  $F_x$ , equals  $F \cos \theta$ . From Fig. 2.49, we see that  $\cos \theta = 1/\cosh(\alpha d)$ . Therefore, Eq. (2.43) gives  $F_x = \rho g/\alpha$ . This goes to zero as  $\alpha \rightarrow \infty$ , which corresponds to a chain with infinite length, that is, a very “droopy” chain. ♣

![Diagram of a chain hanging between two supports, forming a catenary curve. A right triangle is drawn at the right support to illustrate the forces. The horizontal base of the triangle is labeled '1'. The vertical side is labeled 'sinh(alpha x)'. The hypotenuse is labeled 'cosh(alpha x)'. A force vector 'F' is shown acting along the chain at the support, making an angle 'theta' with the horizontal base. A dashed line labeled 'chain' indicates the curve of the chain.](b1939b29ae70227ffcce1e360e6a5a55_img.jpg)

Diagram of a chain hanging between two supports, forming a catenary curve. A right triangle is drawn at the right support to illustrate the forces. The horizontal base of the triangle is labeled '1'. The vertical side is labeled 'sinh(alpha x)'. The hypotenuse is labeled 'cosh(alpha x)'. A force vector 'F' is shown acting along the chain at the support, making an angle 'theta' with the horizontal base. A dashed line labeled 'chain' indicates the curve of the chain.

Fig. 2.49

## 2.10. Mountain climber

CHEAP LASSO: We will take advantage of the fact that a cone is “flat,” in the sense that we can make one out of a piece of paper, without crumpling the paper. Cut the cone along a straight line emanating from the peak and passing through the knot of the lasso, and roll the cone flat onto a plane. Call the resulting figure, which is a sector of a circle,  $S$  (see Fig. 2.50). If the cone is very sharp, then  $S$  looks like a thin “pie piece.” If the cone is very wide, with a shallow slope, then  $S$  looks like a pie with a piece taken out of it. Points on the straight-line boundaries of the sector  $S$  are identified with each other. Let  $P$  be the location of the lasso’s knot. Then  $P$  appears on each straight-line boundary, at equal distances from the tip of  $S$ . Let  $\beta$  be the angle of the sector  $S$ .

The key to this problem is to realize that the path of the lasso’s loop must be a straight line on  $S$ , as shown by the dotted line in Fig. 2.50. This is true because the rope takes the shortest distance between two points because there is no friction, and rolling the cone onto a plane doesn’t change distances. But a straight line between the two identified points  $P$  is possible if and only if the sector  $S$  is smaller than a semicircle. The condition for a climbable mountain is therefore  $\beta < 180^\circ$ .

What is this condition, in terms of the angle of the peak,  $\alpha$ ? Let  $C$  denote a cross-sectional circle of the mountain, a distance  $d$  (measured along the cone) from the top. (We are considering this circle for geometrical convenience. It is *not* the path of the lasso; see the remark below.) A semicircular  $S$  implies that the circumference of  $C$  equals  $\pi d$ . This then implies that the radius of  $C$  equals  $d/2$ . Therefore,

$$\sin(\alpha/2) < \frac{d/2}{d} = \frac{1}{2} \implies \alpha < 60^\circ. \quad (2.47)$$

This is the condition under which the mountain is climbable. In short, having  $\alpha < 60^\circ$  guarantees that there is a loop around the cone with shorter length than the distance straight to the peak and back.

REMARK: When viewed from the side, the rope will appear perpendicular to the side of the mountain at the point opposite the lasso’s knot. A common mistake is to assume that this implies that the climbable condition is  $\alpha < 90^\circ$ . This is not the case, because the loop does not lie in a plane. Lying in a plane, after all, would imply an elliptical loop. But the loop must certainly have a kink in it where the knot is, because there must exist a vertical component to the tension there to hold the climber up. If we had posed the problem with a planar, triangular mountain, then the condition would have been  $\alpha < 90^\circ$ . ♣

DELUXE LASSO: If the mountain is very steep, the climber can slide down the mountain by means of the loop growing larger. If the mountain has a shallow slope, the climber can slide down by means of the loop growing smaller. The only situation in which the climber doesn’t slide down is the one where the change in position of the knot along the mountain is exactly compensated by the change in length of the loop.

Roll the cone onto a plane as we did in the cheap-lasso case. In terms of the sector  $S$  in a plane, the above condition requires that if we move  $P$  a distance  $\ell$  up (or down) along the mountain, the distance between the identified points  $P$  must decrease (or increase) by  $\ell$ . In Fig. 2.50, we must therefore have an equilateral triangle, so  $\beta = 60^\circ$ .

What peak-angle  $\alpha$  does this correspond to? As in part the cheap-lasso case, let  $C$  be a cross-sectional circle of the mountain, a distance  $d$  (measured along the cone) from the top. Then  $\beta = 60^\circ$  implies that the circumference of  $C$  equals  $(\pi/3)d$ . This then implies that the radius of  $C$  equals  $d/6$ . Therefore,

$$\sin(\alpha/2) = \frac{d/6}{d} = \frac{1}{6} \implies \alpha \approx 19^\circ. \quad (2.48)$$

This is the condition under which the mountain is climbable. We see that there is exactly one angle for which the climber can climb up along the mountain. The cheap

![Figure 2.50: A diagram of a sector S of a circle. The sector is defined by two straight radii meeting at a central angle beta. The arc of the sector is at the bottom. Two points, both labeled P, are marked on the two straight radii at equal distances from the vertex. A horizontal dashed line connects these two points P, representing the path of the lasso's loop.](bffbd4616093a40496620fa4a100a805_img.jpg)

Figure 2.50: A diagram of a sector S of a circle. The sector is defined by two straight radii meeting at a central angle beta. The arc of the sector is at the bottom. Two points, both labeled P, are marked on the two straight radii at equal distances from the vertex. A horizontal dashed line connects these two points P, representing the path of the lasso's loop.

Fig. 2.50

![Diagram of a cone with N=4 sectors. A vertical line from the apex to the base center is shown. Four lines radiate from the apex to the base, dividing it into four equal sectors. Points P are marked on the base of each sector.](7ceeec9d5af3ae716cda774be552c9e4_img.jpg)

Diagram of a cone with N=4 sectors. A vertical line from the apex to the base center is shown. Four lines radiate from the apex to the base, dividing it into four equal sectors. Points P are marked on the base of each sector.

Fig. 2.51

lasso is therefore much more useful than the fancy deluxe lasso, assuming, of course, that you want to use it for climbing mountains, and not, say, for rounding up cattle.

REMARK: Another way to see the  $\beta = 60^\circ$  result is to note that the three directions of rope emanating from the knot must all have the same tension, because the deluxe lasso is one continuous piece of rope. They must therefore have  $120^\circ$  angles between themselves (to provide zero net force on the massless knot). This implies that  $\beta = 60^\circ$  in Fig. 2.50. ♣

FURTHER REMARKS: For each type of lasso, we can also ask the question: For what angles can the mountain be climbed if the lasso is looped  $N$  times around the top of the mountain? The solution here is similar to that above.

For the cheap lasso, roll the cone  $N$  times onto a plane, as shown in Fig. 2.51 for  $N = 4$ . The resulting figure,  $S_N$ , is a sector of a circle divided into  $N$  equal sectors, each representing a copy of the cone. As above,  $S_N$  must be smaller than a semicircle. The circumference of the circle  $C$  (defined above) must therefore be less than  $\pi d/N$ . Hence, the radius of  $C$  must be less than  $d/2N$ . Thus,

$$\sin(\alpha/2) < \frac{d/2N}{d} = \frac{1}{2N} \implies \alpha < 2 \sin^{-1}\left(\frac{1}{2N}\right). \quad (2.49)$$

For the deluxe lasso, again roll the cone  $N$  times onto a plane. From the original reasoning above, we must have  $N\beta = 60^\circ$ . The circumference of  $C$  must therefore be  $\pi d/3N$ , and so its radius must be  $d/6N$ . Therefore,

$$\sin(\alpha/2) = \frac{d/6N}{d} = \frac{1}{6N} \implies \alpha = 2 \sin^{-1}\left(\frac{1}{6N}\right). \quad \clubsuit \quad (2.50)$$

![Diagram showing the equivalence of forces on a stick. The top part shows a stick with a force F applied at each end and a series of downward arrows representing distributed forces. The bottom part shows the stick pivoted at the left end with a force F at the right end and a resultant force at a distance l/n from the pivot.](b34a43a7e61ed6e991db776841f2913e_img.jpg)

Diagram showing the equivalence of forces on a stick. The top part shows a stick with a force F applied at each end and a series of downward arrows representing distributed forces. The bottom part shows the stick pivoted at the left end with a force F at the right end and a resultant force at a distance l/n from the pivot.

Fig. 2.52

## 2.11. Equality of torques

The proof by induction is as follows. Assume that we have shown that a force  $F$  applied at a distance  $d$  is equivalent to a force  $kF$  applied at a distance  $d/k$ , for all integers  $k$  up to  $n - 1$ . We now want to show that the statement holds for  $k = n$ .

Consider the situation in Fig. 2.52. Forces  $F$  are applied at the ends of a stick, and forces  $2F/(n - 1)$  are applied at the  $j\ell/n$  marks (for  $1 \leq j \leq n - 1$ ). The stick doesn't rotate (by symmetry), and it doesn't translate (because the net force is zero). Consider the stick to have a pivot at the left end. Replacing the interior forces by their equivalent ones at the  $\ell/n$  mark (see Fig. 2.52) gives a total force there equal to

$$\frac{2F}{n-1} \left(1 + 2 + 3 + \dots + (n-1)\right) = \frac{2F}{n-1} \left(\frac{n(n-1)}{2}\right) = nF. \quad (2.51)$$

We therefore see that a force  $F$  applied at a distance  $\ell$  is equivalent to a force  $nF$  applied at a distance  $\ell/n$ , as was to be shown.

We can now show that Claim 2.1 holds, for arbitrary distances  $a$  and  $b$  (see Fig. 2.53). Consider the stick to be pivoted at its left end, and let  $\epsilon$  be a tiny distance (small compared with  $a$ ). Then a force  $F_3$  at a distance  $a$  is equivalent to a force  $F_3(a/\epsilon)$  at a distance  $\epsilon$ .<sup>10</sup> But a force  $F_3(a/\epsilon)$  at a distance  $\epsilon$  is equivalent to a force  $F_3(a/\epsilon)(\epsilon/(a+b)) = F_3a/(a+b)$  at a distance  $(a+b)$ . This equivalent force at the distance  $(a+b)$  must cancel the force  $F_2$  there, because the stick is motionless. Therefore, we have  $F_3a/(a+b) = F_2$ , which proves the claim.

![Diagram of a stick pivoted at its left end. A force F1 is applied upwards at the left end. A force F2 is applied upwards at a distance a+b from the pivot. A force F3 is applied downwards at a distance a from the pivot.](d919792efd20c6fc5603c02420775c17_img.jpg)

Diagram of a stick pivoted at its left end. A force F1 is applied upwards at the left end. A force F2 is applied upwards at a distance a+b from the pivot. A force F3 is applied downwards at a distance a from the pivot.

Fig. 2.53

## 2.12. Direction of the tension

Consider an infinitesimal piece of the rope, and look at the torque around one end. Any forces acting at this end provide no torque around it. If the tension at the other

<sup>10</sup> Technically, we can use the reasoning in the previous paragraph to say this only if  $a/\epsilon$  is an integer, but since  $a/\epsilon$  is very large, we can simply pick the closest integer to it, and there will be negligible error.

end is directed at a finite angle away from the direction of the rope, then this produces a certain torque. But this torque can't be canceled by the much smaller torque from the tiny gravitational force, because this force is proportional to the length of the tiny piece. Therefore, the tension must point along the rope. It actually points along the direction of the rope at the end of the little piece it acts on, which isn't quite along the direction of the rope at the end we're considering torques around, because the rope bends (assuming it's not vertical). So the tension ends up producing a very small torque which cancels the very small torque from gravity.

This argument doesn't work for a rigid stick, because the stick can produce finite torques around the end of a piece via forces *at* that end, because the end is really a cross section of finite size. There is a shearing action in the stick, and the large shearing forces act with tiny lever arms (relative to, say, a point at the middle of the cross section) to produce finite torques.

## 2.13. Find the force

In Fig. 2.54, let the supports at the ends exert forces  $F_1$  and  $F_2$ , and let the support in the interior exert a force  $F$ . Then

$$F_1 + F_2 + F = Mg. \quad (2.52)$$

Balancing torques around the left and right ends gives, respectively,

$$\begin{aligned} Fa + F_2(a+b) &= Mg \frac{a+b}{2}, \\ Fb + F_1(a+b) &= Mg \frac{a+b}{2}, \end{aligned} \quad (2.53)$$

where we have used the fact that the stick can be treated like a point mass at its center. Note that the equation for balancing the torques around the center of mass is redundant; it is obtained by taking the difference of the two previous equations and then dividing by 2. And balancing torques around the middle pivot also takes the form of a linear combination of these equations, as you can show.

It appears as though we have three equations and three unknowns, but we really have only two equations, because the sum of Eqs. (2.53) gives Eq. (2.52). Therefore, since we have two equations and three unknowns, the system is underdetermined. Solving Eqs. (2.53) for  $F_1$  and  $F_2$  in terms of  $F$ , we see that any forces of the form

$$(F_1, F_2) = \left( \frac{Mg}{2} - \frac{Fb}{a+b}, F, \frac{Mg}{2} - \frac{Fa}{a+b} \right) \quad (2.54)$$

are possible. In retrospect, it makes sense that the forces are not determined. By changing the height of the new support an infinitesimal distance, we can make  $F$  be anything from 0 up to  $Mg(a+b)/2b$ , which is when the stick comes off the left support (assuming  $b \geq a$ ).

## 2.14. Leaning sticks

Let  $M_l$  be the mass of the left stick, and let  $M_r$  be the mass of the right stick. Then  $M_l/M_r = \tan \theta$ . Let  $N$  and  $F_f$  be the normal and friction forces between the sticks (see Fig. 2.55).  $F_f$  has a maximum value of  $\mu N$ . Balancing the torques on the left stick (around the contact point with the ground) gives  $N = (M_l g/2) \sin \theta$ . Balancing the torques on the right stick (around the contact point with the ground) gives  $F_f = (M_r g/2) \cos \theta$ . The condition  $F_f \leq \mu N$  is therefore

$$M_r \cos \theta \leq \mu M_l \sin \theta \implies \tan^2 \theta \geq \frac{1}{\mu}, \quad (2.55)$$

where we have used  $M_l/M_r = \tan \theta$ . This answer checks in the two extremes: In the limit  $\mu \rightarrow 0$ , we see that  $\theta$  must be very close to  $\pi/2$ , which makes sense. And in the limit  $\mu \rightarrow \infty$  (that is, very sticky sticks), we see that  $\theta$  can be very small, which also makes sense.

![Diagram of a horizontal stick supported by three triangular supports. The left support exerts an upward force F1, the middle support exerts an upward force F, and the right support exerts an upward force F2. The stick has a total length a+b, with the middle support located at distance a from the left end and distance b from the right end. A downward force Mg is applied at the center of the stick, which is at distance (a+b)/2 from both ends.](375d486d1093bd780d5bcc918c835344_img.jpg)

Diagram of a horizontal stick supported by three triangular supports. The left support exerts an upward force F1, the middle support exerts an upward force F, and the right support exerts an upward force F2. The stick has a total length a+b, with the middle support located at distance a from the left end and distance b from the right end. A downward force Mg is applied at the center of the stick, which is at distance (a+b)/2 from both ends.

Fig. 2.54

![Diagram of two sticks leaning against each other on a horizontal surface. The left stick has mass M_l and the right stick has mass M_r. They meet at a top point. At the contact point, a normal force N acts perpendicular to the sticks and a friction force F_f acts parallel to the sticks. The angle theta is shown between the right stick and the horizontal ground.](00415a2f52e0243d9ca2bc0e5eefac47_img.jpg)

Diagram of two sticks leaning against each other on a horizontal surface. The left stick has mass M\_l and the right stick has mass M\_r. They meet at a top point. At the contact point, a normal force N acts perpendicular to the sticks and a friction force F\_f acts parallel to the sticks. The angle theta is shown between the right stick and the horizontal ground.

Fig. 2.55

## 2.15. **Supporting a ladder**

Let  $F$  be the desired force.  $F$  must be directed along the stick, because otherwise there would be a net torque on the (massless) stick relative to the pivot at its right end, and this would contradict the fact that it is at rest. Look at torques on the ladder around the pivot at its bottom. The gravitational force provides a clockwise torque of  $Mg(L/2) \cos \theta$ , and the force  $F$  from the stick provides a counterclockwise torque of  $F(\ell/\tan \theta)$ . Equating these two torques gives

$$F = \frac{MgL}{2\ell} \sin \theta. \quad (2.56)$$

REMARKS:  $F$  goes to zero as  $\theta \rightarrow 0$ , as it should.<sup>11</sup> And  $F$  increases to  $MgL/2\ell$  as  $\theta \rightarrow \pi/2$ , which isn't so obvious (the required torque from the stick is very small, but the lever arm is also very small). However, in the special case where the ladder is exactly vertical, no force is required. You can see that our calculations above are not valid in this case, because we divided by  $\cos \theta$ , which is zero when  $\theta = \pi/2$ .

The normal force at the pivot of the stick (which equals the vertical component of  $F$ , because the stick is massless) is equal to  $MgL \sin \theta \cos \theta / 2\ell$ . This has a maximum value of  $MgL/4\ell$  at  $\theta = \pi/4$ . ♣

![Diagram of a stick balanced on a pivot. The stick is horizontal, and the pivot is located at a distance x_0 + l from the left end. The left end of the stick is at position x_0.](4896c2da9b1a47e092ee7c98574fae04_img.jpg)

Diagram of a stick balanced on a pivot. The stick is horizontal, and the pivot is located at a distance x\_0 + l from the left end. The left end of the stick is at position x\_0.

Fig. 2.56

## 2.16. **Balancing the stick**

Let the stick go off to infinity in the positive  $x$  direction, and let it be cut at  $x = x_0$ . Then the pivot point is located at  $x = x_0 + \ell$  (see Fig. 2.56). Let the density be  $\rho(x)$ . The condition that the total gravitational torque relative to  $x_0 + \ell$  be zero is

$$\tau = \int_{x_0}^{\infty} \rho(x)(x - (x_0 + \ell))g \, dx = 0. \quad (2.57)$$

We want this to equal zero for all  $x_0$ , so the derivative of  $\tau$  with respect to  $x_0$  must be zero.  $\tau$  depends on  $x_0$  through both the limits of integration and the integrand. In taking the derivative, the former dependence requires finding the value of the integrand at the  $x_0$  limit, while the latter dependence requires taking the derivative of the integrand with respect to  $x_0$ , and then integrating. (To derive these two contributions, just replace  $x_0$  with  $x_0 + dx_0$  and expand things to first order in  $dx_0$ .) We obtain

$$0 = \frac{d\tau}{dx_0} = g\ell\rho(x_0) - g \int_{x_0}^{\infty} \rho(x) \, dx. \quad (2.58)$$

Taking the derivative of this equation with respect to  $x_0$  gives  $\ell\rho'(x_0) = -\rho(x_0)$ . The solution to this is (rewriting the arbitrary  $x_0$  as  $x$ )

$$\rho(x) = Ae^{-x/\ell}. \quad (2.59)$$

We therefore see that the density decreases exponentially with  $x$ . The smaller  $\ell$  is, the quicker it falls off. Note that the density at the pivot is  $1/e$  times the density at the left end. And you can show that  $1 - 1/e \approx 63\%$  of the mass is contained between the left end and the pivot.

## 2.17. **The spool**

(a) Let  $F_f$  be the friction force the ground provides. Balancing the horizontal forces on the spool gives (see Fig. 2.57)

$$T \cos \theta = F_f. \quad (2.60)$$

![Diagram of a spool on a horizontal surface. The spool has an outer radius R and an inner radius r. A string is wrapped around the inner radius and is pulled at an angle theta above the horizontal. The tension in the string is T. A friction force F_f acts to the left on the spool.](999a9bfba5f9b5910c792ff870cfcccc_img.jpg)

Diagram of a spool on a horizontal surface. The spool has an outer radius R and an inner radius r. A string is wrapped around the inner radius and is pulled at an angle theta above the horizontal. The tension in the string is T. A friction force F\_f acts to the left on the spool.

Fig. 2.57

<sup>11</sup> For  $\theta \rightarrow 0$ , we would need to lengthen the ladder with a massless extension, because the stick would have to be very far to the right to remain perpendicular to the ladder.

Balancing torques around the center of the spool gives

$$Tr = F_f R. \quad (2.61)$$

These two equations imply

$$\cos \theta = \frac{r}{R}. \quad (2.62)$$

The niceness of this result suggests that there is a quicker way to obtain it. And indeed, we see from Fig. 2.58 that  $\cos \theta = r/R$  is the angle that causes the line of the tension to pass through the contact point on the ground. Since gravity and friction provide no torque around this point, the total torque around it is therefore zero, and the spool remains at rest.

- (b) The normal force from the ground is

$$N = Mg - T \sin \theta. \quad (2.63)$$

Using Eq. (2.60), the statement  $F_f \leq \mu N$  becomes

$$T \cos \theta \leq \mu (Mg - T \sin \theta) \implies T \leq \frac{\mu Mg}{\cos \theta + \mu \sin \theta}, \quad (2.64)$$

where  $\theta$  is given in Eq. (2.62).

- (c) The maximum value of  $T$  is given in (2.64). This depends on  $\theta$ , which in turn depends on  $r$ . We want to find the  $r$  that minimizes this maximum  $T$ . Taking the derivative with respect to  $\theta$ , we find that the  $\theta$  that maximizes the denominator in Eq. (2.64) is given by  $\tan \theta_0 = \mu$ . You can then show that the value of  $T$  for this  $\theta_0$  is

$$T_0 = \frac{\mu Mg}{\sqrt{1 + \mu^2}}. \quad (2.65)$$

To find the corresponding  $r$ , we can use Eq. (2.62) to write  $\tan \theta = \sqrt{R^2 - r^2}/r$ . The relation  $\tan \theta_0 = \mu$  then yields

$$r_0 = \frac{R}{\sqrt{1 + \mu^2}}. \quad (2.66)$$

This is the  $r$  that yields the smallest upper bound on  $T$ . In the limit  $\mu = 0$ , we have  $\theta_0 = 0$ ,  $T_0 = 0$ , and  $r_0 = R$ . And in the limit  $\mu = \infty$ , we have  $\theta_0 = \pi/2$ ,  $T_0 = Mg$ , and  $r_0 = 0$ .

## 2.18. Stick on a circle

Let  $N$  be the normal force between the stick and the circle, and let  $F_f$  be the friction force between the ground and the circle (see Fig. 2.59). Then we immediately see that the friction force between the stick and the circle is also  $F_f$ , because the torques from the two friction forces on the circle must cancel. We've drawn all forces as acting on the circle. By Newton's third law,  $N$  and  $F_f$  act in the opposite directions on the stick at its top end.

Looking at torques on the stick around the point of contact with the ground, we have  $Mg(\ell/2) \cos \theta = N\ell$ , where  $M = \rho\ell$  is the mass of the stick, and  $\ell$  is its length. Therefore,  $N = (\rho\ell g/2) \cos \theta$ . Balancing the horizontal forces on the circle gives  $N \sin \theta = F_f + F_f \cos \theta$ , so we have

$$F_f = \frac{N \sin \theta}{1 + \cos \theta} = \frac{\rho\ell g \sin \theta \cos \theta}{2(1 + \cos \theta)}. \quad (2.67)$$

But from Fig. 2.59 we have  $\ell = R/\tan(\theta/2)$ . Using the identity  $\tan(\theta/2) = \sin \theta/(1 + \cos \theta)$ , we finally obtain

$$F_f = \frac{1}{2} \rho g R \cos \theta. \quad (2.68)$$

![Diagram of a spool on a horizontal surface. The spool has an outer radius R and an inner radius r. A tension force T is applied to the inner axle at an angle theta above the horizontal. The line of action of T passes through the contact point on the ground. The angle theta is shown between the horizontal and the line of tension, and also between the vertical radius and the line of tension.](5184b3db9c36844bbd80e16ee1934ed6_img.jpg)

Diagram of a spool on a horizontal surface. The spool has an outer radius R and an inner radius r. A tension force T is applied to the inner axle at an angle theta above the horizontal. The line of action of T passes through the contact point on the ground. The angle theta is shown between the horizontal and the line of tension, and also between the vertical radius and the line of tension.

Fig. 2.58

![Diagram of a stick of length l leaning against a circle of radius R. The stick is in contact with the circle at a point where the radius makes an angle theta/2 with the vertical. The stick's end is at a distance l from the contact point. The angle between the stick and the vertical is theta/2. Forces shown on the circle include: a normal force N from the stick acting at the contact point, a friction force F_f from the ground acting at the bottom of the circle, and a friction force F_f from the stick acting at the contact point. The angle theta/2 is also shown between the horizontal and the line from the center to the contact point.](59c0e5125192097eae58f43ef00adfcc_img.jpg)

Diagram of a stick of length l leaning against a circle of radius R. The stick is in contact with the circle at a point where the radius makes an angle theta/2 with the vertical. The stick's end is at a distance l from the contact point. The angle between the stick and the vertical is theta/2. Forces shown on the circle include: a normal force N from the stick acting at the contact point, a friction force F\_f from the ground acting at the bottom of the circle, and a friction force F\_f from the stick acting at the contact point. The angle theta/2 is also shown between the horizontal and the line from the center to the contact point.

Fig. 2.59