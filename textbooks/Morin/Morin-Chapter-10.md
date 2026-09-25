# Chapter 10 Accelerating frames of reference

Newton's laws hold only in inertial frames of reference. However, there are many noninertial (that is, accelerating) frames that we might reasonably want to consider, such as elevators, merry-go-rounds, and so on. Is there any possible way to modify Newton's laws so that they hold in noninertial frames, or do we have to give up entirely on  $\mathbf{F} = m\mathbf{a}$ ? It turns out that we can in fact hold on to our good friend  $\mathbf{F} = m\mathbf{a}$ , provided that we introduce some new “fictitious” forces. These are forces that a person in the accelerating frame thinks exist. If she applies  $\mathbf{F} = m\mathbf{a}$  while including these new forces, then she will get the correct answer for the acceleration  $\mathbf{a}$ , as measured with respect to her frame.

To be quantitative about all this, we'll have to spend some time figuring out how the coordinates (and their derivatives) in an accelerating frame relate to those in an inertial frame. But before diving into that, let's look at a simple example that demonstrates the basic idea of fictitious forces.

---

**Example (A train):** Imagine that you are standing on a train that is accelerating to the right with acceleration  $a$ . If you are to remain at the same spot on the train, then there must be a friction force between the floor and your feet with magnitude  $F_f = ma$ , pointing to the right. Someone standing in the inertial frame of the ground simply interprets the situation as, “The friction force  $F_f$ , which equals  $ma$ , causes your acceleration  $a$ .”

How do you interpret the situation in the frame of the train? Assume that there are no windows, so that all you see is the inside of the train. As we will show below in Eq. (10.11), you will feel a fictitious *translation* force,  $F_{\text{trans}} = -ma$ , pointing to the left. You therefore interpret the situation as, “In my frame (the frame of the train), the friction force  $F_f = ma$  pointing to my right exactly cancels the mysterious  $F_{\text{trans}} = -ma$  force pointing to my left, resulting in zero acceleration (in my frame).”

Of course, if the floor of the train is frictionless so that there is no force at your feet, then you will say that the net force on you is  $F_{\text{trans}} = -ma$ , pointing to the left. You will therefore accelerate with acceleration  $a$  to the left, with respect to your frame (the train). In other words, you will remain motionless (or move with constant velocity, if you happened to be moving initially) with respect to the inertial frame of the ground, which is all quite obvious to someone standing on the ground.

In the case where the friction force at your feet is nonzero, but not large enough to balance out the whole  $F_{\text{trans}} = -ma$  force, you will end up being accelerated toward

the back of the train (in the frame of the train), with an acceleration that is less than  $a$ . This undesired motion will continue until you make the required adjustments with your feet or hands to balance out all of the  $F_{\text{trans}}$  force.

Let's now derive the fictitious forces in their full generality. The main task here is to relate the coordinates in an accelerating frame to those in an inertial frame, so this endeavor will require a bit of math.

## 10.1 Relating the coordinates

Consider an inertial coordinate system with axes  $\hat{x}_I$ ,  $\hat{y}_I$ , and  $\hat{z}_I$ , and let there be another (possibly accelerating) coordinate system with axes  $\hat{x}$ ,  $\hat{y}$ , and  $\hat{z}$ . These latter axes are allowed to change in an arbitrary manner with respect to the inertial frame. That is, the origin may undergo acceleration, and the axes may rotate (this is the most general possible motion, as we saw in Section 9.1). These axes may be considered to be functions of the inertial axes.

Let  $O_I$  and  $O$  be the origins of the two coordinate systems. Let the vector from  $O_I$  to  $O$  be  $\mathbf{R}$ , let the vector from  $O_I$  to a given particle be  $\mathbf{r}_I$ , and let the vector from  $O$  to the particle be  $\mathbf{r}$ . See Fig. 10.1 for the 2-D case. Then

$$\mathbf{r}_I = \mathbf{R} + \mathbf{r}. \quad (10.1)$$

These vectors have an existence that is independent of any specific coordinate system, but let's write them in terms of some definite coordinates. We may write

$$\begin{aligned} \mathbf{R} &= X\hat{x}_I + Y\hat{y}_I + Z\hat{z}_I, \\ \mathbf{r}_I &= x_I\hat{x}_I + y_I\hat{y}_I + z_I\hat{z}_I, \\ \mathbf{r} &= x\hat{x} + y\hat{y} + z\hat{z}. \end{aligned} \quad (10.2)$$

For reasons that will become clear, we have chosen to write  $\mathbf{R}$  and  $\mathbf{r}_I$  in terms of the inertial-frame coordinates, and  $\mathbf{r}$  in terms of the accelerating-frame coordinates. If desired, Eq. (10.1) may be written as

$$x_I\hat{x}_I + y_I\hat{y}_I + z_I\hat{z}_I = (X\hat{x}_I + Y\hat{y}_I + Z\hat{z}_I) + (x\hat{x} + y\hat{y} + z\hat{z}). \quad (10.3)$$

Our goal is to take the second time derivative of Eq. (10.1) and to then interpret the result in an  $\mathbf{F} = m\mathbf{a}$  form. The second derivative of  $\mathbf{r}_I$  is the acceleration of the particle with respect to the inertial system, so Newton's second law tells us that  $\mathbf{F} = m\ddot{\mathbf{r}}_I$ . The second derivative of  $\mathbf{R}$  is the acceleration of the origin of the moving system. The second derivative of  $\mathbf{r}$  is the tricky part. In view of its form in Eq. (10.2), changes in  $\mathbf{r}$  can come about in two ways. First, the coordinates  $(x, y, z)$  of  $\mathbf{r}$ , which are measured with respect to the moving axes, may change. And second, the axes  $\hat{x}$ ,  $\hat{y}$ ,  $\hat{z}$  themselves may change. The point is that  $\mathbf{r}$  is *not*

![Figure 10.1: A 2D diagram illustrating the relationship between two coordinate systems. An inertial frame (O_I, x_I, y_I) is shown with axes x_I and y_I. A second, accelerating frame (O, x, y) is shown with its origin O displaced from O_I by vector R. A particle is shown at position r_I from O_I and position r from O. The vectors R, r, and r_I are shown as arrows originating from O_I, O, and the particle respectively.](3b27e5ede475dec21297cf486c7e179a_img.jpg)

Figure 10.1: A 2D diagram illustrating the relationship between two coordinate systems. An inertial frame (O\_I, x\_I, y\_I) is shown with axes x\_I and y\_I. A second, accelerating frame (O, x, y) is shown with its origin O displaced from O\_I by vector R. A particle is shown at position r\_I from O\_I and position r from O. The vectors R, r, and r\_I are shown as arrows originating from O\_I, O, and the particle respectively.

Fig. 10.1

just the ordered triplet  $(x, y, z)$ . It is the whole expression,  $\mathbf{r} = x\hat{\mathbf{x}} + y\hat{\mathbf{y}} + z\hat{\mathbf{z}}$ . So even if  $(x, y, z)$  are fixed, meaning that  $\mathbf{r}$  doesn't change with respect to the moving system,  $\mathbf{r}$  can still change with respect to the inertial system if the  $\hat{\mathbf{x}}, \hat{\mathbf{y}}, \hat{\mathbf{z}}$  axes are moving. Let's be quantitative about this.

#### Calculation of $d^2\mathbf{r}/dt^2$

We should clarify our goal here. We would like to obtain  $d^2\mathbf{r}/dt^2$  in terms of the coordinates in the *accelerating* frame, because we want to be able to work entirely in terms of these coordinates so that a person in the accelerating frame can write down an  $\mathbf{F} = m\mathbf{a}$  equation in terms of her coordinates only, without having to consider the underlying inertial frame at all. In terms of the *inertial* frame,  $d^2\mathbf{r}/dt^2$  is simply  $d^2(\mathbf{r}_1 - \mathbf{R})/dt^2$ , but this isn't very enlightening by itself.

The following exercise in taking derivatives works for a general vector  $\mathbf{A} = A_x\hat{\mathbf{x}} + A_y\hat{\mathbf{y}} + A_z\hat{\mathbf{z}}$  in the moving frame; it isn't necessary that it be a position vector. So we'll work with a general  $\mathbf{A}$  and then set  $\mathbf{A} = \mathbf{r}$  when we're done. To take  $d/dt$  of  $\mathbf{A} = A_x\hat{\mathbf{x}} + A_y\hat{\mathbf{y}} + A_z\hat{\mathbf{z}}$ , we can use the product rule to obtain

$$\frac{d\mathbf{A}}{dt} = \left( \frac{dA_x}{dt} \hat{\mathbf{x}} + \frac{dA_y}{dt} \hat{\mathbf{y}} + \frac{dA_z}{dt} \hat{\mathbf{z}} \right) + \left( A_x \frac{d\hat{\mathbf{x}}}{dt} + A_y \frac{d\hat{\mathbf{y}}}{dt} + A_z \frac{d\hat{\mathbf{z}}}{dt} \right). \quad (10.4)$$

Yes, the product rule works with vectors too. We're doing nothing more than expanding  $(A_x + dA_x)(\hat{\mathbf{x}} + d\hat{\mathbf{x}}) - A_x\hat{\mathbf{x}}$ , etc., to first order. Note that although we have expressed the vector  $\mathbf{A}$  in terms of the coordinate axes of the moving frame, the total derivative  $d\mathbf{A}/dt$  is measured with respect to the *inertial* frame. As mentioned above, the total rate of change of  $\mathbf{A}$  comes from two effects, namely the two groups of terms in Eq. (10.4). The first group gives the rate of change of  $\mathbf{A}$ , as measured with respect to the moving frame. We'll denote this quantity by  $\delta\mathbf{A}/\delta t$ .

The second group arises because the coordinate axes are moving. In what manner are they moving? We have already extracted the motion of the origin of the accelerating system by introducing the vector  $\mathbf{R}$ , so the only thing left is a rotation about some axis  $\boldsymbol{\omega}$  through this origin (see Theorem 9.1). The axis  $\boldsymbol{\omega}$  may change with time, but at any instant a unique axis of rotation describes the system. The fact that the axis may change will be relevant in finding the second derivative of  $\mathbf{r}$ , but not in finding the first derivative.

We saw in Theorem 9.2 that a vector  $\mathbf{B}$  that has fixed length (the coordinate axes here do indeed have fixed length) and that rotates with angular velocity  $\boldsymbol{\omega} \equiv \omega\hat{\boldsymbol{\omega}}$  changes at a rate  $d\mathbf{B}/dt = \boldsymbol{\omega} \times \mathbf{B}$ . In particular,  $d\hat{\mathbf{x}}/dt = \boldsymbol{\omega} \times \hat{\mathbf{x}}$ , etc. So in Eq. (10.4), the  $A_x(d\hat{\mathbf{x}}/dt)$  term equals  $A_x(\boldsymbol{\omega} \times \hat{\mathbf{x}}) = \boldsymbol{\omega} \times (A_x\hat{\mathbf{x}})$ . Likewise for the  $y$  and  $z$  terms. Combining them gives  $\boldsymbol{\omega} \times (A_x\hat{\mathbf{x}} + A_y\hat{\mathbf{y}} + A_z\hat{\mathbf{z}})$ , which is just  $\boldsymbol{\omega} \times \mathbf{A}$ . Therefore, Eq. (10.4) becomes

$$\frac{d\mathbf{A}}{dt} = \frac{\delta\mathbf{A}}{\delta t} + \boldsymbol{\omega} \times \mathbf{A}. \quad (10.5)$$

This agrees with the result obtained in Section 9.5, Eq. (9.41). We've basically given the same proof here, but with a little more mathematical rigor.

We still have to take one more time derivative. Using the product rule, the time derivative of Eq. (10.5) is

$$\frac{d^2\mathbf{A}}{dt^2} = \frac{d}{dt} \left( \frac{\delta\mathbf{A}}{\delta t} \right) + \frac{d\boldsymbol{\omega}}{dt} \times \mathbf{A} + \boldsymbol{\omega} \times \frac{d\mathbf{A}}{dt}. \quad (10.6)$$

Applying Eq. (10.5) to the first term on the right (with  $\delta\mathbf{A}/\delta t$  in place of  $\mathbf{A}$ ), and plugging Eq. (10.5) into the third term, gives

$$\begin{aligned} \frac{d^2\mathbf{A}}{dt^2} &= \left( \frac{\delta^2\mathbf{A}}{\delta t^2} + \boldsymbol{\omega} \times \frac{\delta\mathbf{A}}{\delta t} \right) + \left( \frac{d\boldsymbol{\omega}}{dt} \times \mathbf{A} \right) + \boldsymbol{\omega} \times \left( \frac{\delta\mathbf{A}}{\delta t} + (\boldsymbol{\omega} \times \mathbf{A}) \right) \\ &= \frac{\delta^2\mathbf{A}}{\delta t^2} + \boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{A}) + 2\boldsymbol{\omega} \times \frac{\delta\mathbf{A}}{\delta t} + \frac{d\boldsymbol{\omega}}{dt} \times \mathbf{A}. \end{aligned} \quad (10.7)$$

At this point we will set  $\mathbf{A} = \mathbf{r}$ , which gives

$$\frac{d^2\mathbf{r}}{dt^2} = \mathbf{a} + \boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r}) + 2\boldsymbol{\omega} \times \mathbf{v} + \frac{d\boldsymbol{\omega}}{dt} \times \mathbf{r}, \quad (10.8)$$

where  $\mathbf{r}$ ,  $\mathbf{v} \equiv \delta\mathbf{r}/\delta t$ , and  $\mathbf{a} \equiv \delta^2\mathbf{r}/\delta t^2$  are the position, velocity, and acceleration of the particle, as measured *with respect to the accelerating frame*. In other words, if the accelerating frame is enclosed in a windowless box, and if a person inside the box paints a coordinate grid on the floor, then she can (assuming that she has a clock at her disposal) measure  $\mathbf{r}$ ,  $\mathbf{v}$ , and  $\mathbf{a}$  without caring at all about what is going on in the outside world.

You might be concerned that the  $\mathbf{r}$ ,  $\mathbf{v}$ , and  $\mathbf{a}$  on the right-hand side of Eq. (10.8) are measured by someone in the rotating frame, whereas the  $d^2\mathbf{r}/dt^2$  on the left-hand side is measured by someone in the inertial frame. But this apparent discrepancy is a nonissue, because Eq. (10.8) is a statement about vectors, and these vectors have an existence that is independent of the coordinate system that is used to describe them. For example, the vector  $\mathbf{a}$  points in a certain direction (say, toward the distant star Sirius) and has a certain magnitude, independent of whoever chooses to describe it with whatever coordinates.

## 10.2 The fictitious forces

From Eq. (10.1) we have

$$\frac{d^2\mathbf{r}}{dt^2} = \frac{d^2\mathbf{r}_I}{dt^2} - \frac{d^2\mathbf{R}}{dt^2}. \quad (10.9)$$

We can equate this expression for  $d^2\mathbf{r}/dt^2$  with the expression in Eq. (10.8), and then multiply through by the mass  $m$  of the particle. Recognizing that

$m(d^2\mathbf{r}_1/dt^2)$  is the force  $\mathbf{F}$  acting on the particle ( $\mathbf{F}$  may be gravity, a normal force, friction, tension, etc.), we can solve for  $m\mathbf{a}$  to obtain

$$\begin{aligned} m\mathbf{a} &= \mathbf{F} - m\frac{d^2\mathbf{R}}{dt^2} - m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r}) - 2m\boldsymbol{\omega} \times \mathbf{v} - m\frac{d\boldsymbol{\omega}}{dt} \times \mathbf{r} \\ &\equiv \mathbf{F} + \mathbf{F}_{\text{translation}} + \mathbf{F}_{\text{centrifugal}} + \mathbf{F}_{\text{Coriolis}} + \mathbf{F}_{\text{azimuthal}}, \end{aligned} \quad (10.10)$$

where the *fictitious forces* are defined as

$$\begin{aligned} \mathbf{F}_{\text{trans}} &\equiv -m\frac{d^2\mathbf{R}}{dt^2}, \\ \mathbf{F}_{\text{cent}} &\equiv -m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r}), \\ \mathbf{F}_{\text{cor}} &\equiv -2m\boldsymbol{\omega} \times \mathbf{v}, \\ \mathbf{F}_{\text{az}} &\equiv -m\frac{d\boldsymbol{\omega}}{dt} \times \mathbf{r}. \end{aligned} \quad (10.11)$$

We have taken the liberty of calling these quantities “forces,” because the left-hand side of Eq. (10.10) is  $m\mathbf{a}$ , where  $\mathbf{a}$  is measured by someone in the accelerating frame. This person should therefore be able to interpret the right-hand side as some effective force. In other words, if a person in the accelerating frame wishes to calculate  $m\mathbf{a}$ , she simply needs to take the true force  $\mathbf{F}$ , and then add on all the other terms on the right-hand side of Eq. (10.10), which she will then quite reasonably interpret as forces (in her frame). She will consider Eq. (10.10) to be an  $\mathbf{F} = m\mathbf{a}$  statement in the form,

$$m\mathbf{a} = \sum \mathbf{F}_{\text{acc}}, \quad (10.12)$$

where  $\mathbf{F}_{\text{acc}}$  represents all the forces, real or fictitious, in the accelerating frame. All we’ve really done is transfer some terms to the other side of an equation and reinterpret the result. The last three terms on the right-hand side of Eq. (10.8) are nothing more than various pieces of the acceleration. But if we transfer them to the left-hand side and solve for  $\mathbf{a}$ , we can then interpret them (after multiplying by  $m$ ) as forces in Eq. (10.10).

Of course, the extra terms in Eq. (10.10) are not actual forces. The constituents of  $\mathbf{F}$  are the only real forces in the problem (and they are the same in any frame). All we are saying is that if our friend in the moving frame assumes that the extra terms are real forces, and if she adds them to  $\mathbf{F}$ , then she will get the correct answer for  $m\mathbf{a}$ , as measured in her frame.

For example, consider a box (far away from other objects, in outer space) that accelerates at a rate of  $g = 10 \text{ m/s}^2$  in some direction. A person in the box feels a fictitious force of  $\mathbf{F}_{\text{trans}} = mg$  down into the floor. For all she knows, she is in a box on the surface of the earth. If she performs various experiments under this assumption, the results will always be what she expects. The surprising fact that no local experiment can distinguish between the fictitious force in the

accelerating box and the real gravitational force on the earth is what led Einstein to his Equivalence Principle and his theory of General Relativity (discussed in Chapter 14). These fictitious forces are more meaningful than you might think.

As Einstein explored elevators,  
 And studied the spinning ice-skaters,  
 He eyed as suspicious,  
 The forces, fictitious,  
 Of gravity's great imitators.

Note that in addition to the sum of all the real forces,  $\mathbf{F}$ , there are two different types of quantities on the right-hand side of Eq. (10.10). The quantities  $\mathbf{r}$  and  $\mathbf{v}$  are measured by someone inside the accelerating frame; they depend on what the particle is doing. But  $d^2\mathbf{R}/dt^2$  and  $\boldsymbol{\omega}$  are properties of the frame. In general, the person inside needs to be given their values, although it is possible for her to figure out what they are in certain special cases (see Problem 10.9).

Let's now look at each of the fictitious forces in detail. The translation and centrifugal forces are fairly easy to understand. The Coriolis force is a little more difficult. And the azimuthal force can be easy or difficult, depending on exactly how  $\boldsymbol{\omega}$  is changing.

#### 10.2.1 Translation force: $-m d^2\mathbf{R}/dt^2$

This is the most intuitive of the fictitious forces. We've already discussed this force in the train example in the introduction to this chapter. If  $\mathbf{R}$  is the position of the train, then  $\mathbf{F}_{\text{trans}} \equiv -m d^2\mathbf{R}/dt^2$  is the fictitious translation force you feel in the accelerating frame.

#### 10.2.2 Centrifugal force: $-m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r})$

This force goes hand-in-hand with the  $mv^2/r = mr\omega^2$  centripetal acceleration as viewed by someone in an inertial frame.

![Diagram of a person standing on a rotating carousel. A vertical arrow labeled ω points upwards from the center of the carousel. A horizontal arrow labeled F_cent points radially outward from a point on the carousel's edge.](336ae99f53d024f5307234178a6078fc_img.jpg)

Diagram of a person standing on a rotating carousel. A vertical arrow labeled ω points upwards from the center of the carousel. A horizontal arrow labeled F\_cent points radially outward from a point on the carousel's edge.

Fig. 10.2

**Example (Standing on a carousel):** Consider a person standing motionless with respect to a carousel, a distance  $r$  from the center. Let the carousel rotate in the  $x$ - $y$  plane with angular velocity  $\boldsymbol{\omega} = \omega\hat{\mathbf{z}}$  (see Fig. 10.2). What is the centrifugal force felt by the person?

**Solution:**  $\boldsymbol{\omega} \times \mathbf{r}$  has magnitude  $\omega r$  and points in the tangential direction, in the direction of motion. Therefore,  $m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r})$  has magnitude  $mr\omega^2$  and points radially inward. Hence, the centrifugal force  $-m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r})$  has magnitude  $mr\omega^2$  and points radially outward.

**REMARK:** If the person is not moving with respect to the carousel, and if  $\boldsymbol{\omega}$  is constant, then the centrifugal force is the only nonzero fictitious force in Eq. (10.10). Since the

person is not accelerating in her rotating frame, the net force (as measured in her frame) must be zero. The forces in her frame are (1) gravity pulling downward, (2) the normal force pushing upward (which cancels gravity), (3) the friction force pushing inward at her feet, and (4) the centrifugal force pulling outward. We conclude that the last two of these must cancel. So the friction force must point inward with magnitude  $mr\omega^2$ .

Someone standing on the ground observes only the first three of these forces, so the net force is not zero. And indeed, there is a centripetal acceleration,  $v^2/r = r\omega^2$ , due to the friction force. To sum up: in the inertial frame, the friction force exists to provide a centripetal acceleration. In the rotating frame, the friction force exists to balance out the mysterious new centrifugal force, in order to yield zero acceleration. ♣

**Example (Effective gravity force,  $mg_{\text{eff}}$ ):** Consider a person standing motionless on the earth, at a polar angle  $\theta$ ; the way we've defined it,  $\theta$  equals  $\pi/2$  minus the latitude angle. In the rotating frame of the earth, the person feels a centrifugal force (directed away from the axis) in addition to the gravitational force,  $mg$ ; see Fig. 10.3, although this figure is somewhat misleading, as explained in the first remark below. Note that we're using  $\mathbf{g}$  to denote the acceleration due solely to the gravitational force. This isn't the "g-value" that the person measures, as we'll shortly see.

The sum of the gravitational and centrifugal forces (that is, what the person thinks is gravity) doesn't point radially, unless the person is at the equator or at a pole. Let us denote the sum by  $mg_{\text{eff}}$ . To calculate  $mg_{\text{eff}}$ , we must calculate  $\mathbf{F}_{\text{cent}} = -m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r})$ . The  $\boldsymbol{\omega} \times \mathbf{r}$  part has magnitude  $R\omega \sin \theta$ , where  $R$  is the radius of the earth, and it is directed tangentially along the latitude circle of radius  $R \sin \theta$ . So  $-m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r})$  points outward from the axis, with magnitude  $mR\omega^2 \sin \theta$ , which is just what we expect for something traveling at frequency  $\omega$  in a circle of radius  $R \sin \theta$ . Therefore, the effective gravitational force,

$$mg_{\text{eff}} \equiv m(\mathbf{g} - \boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r})), \quad (10.13)$$

points slightly in the southerly direction (for someone in the northern hemisphere), as shown in Fig. 10.4. The magnitude of the correction term,  $mR\omega^2 \sin \theta$ , is small compared with  $g$ . Using  $\omega \approx 7.3 \cdot 10^{-5} \text{ s}^{-1}$  (that is, one revolution per day, which is  $2\pi$  radians per 86 400 seconds) and  $R \approx 6.4 \cdot 10^6 \text{ m}$ , we find  $R\omega^2 \approx 0.03 \text{ m/s}^2$ . Therefore, the correction to  $g$  is about 0.3% at the equator (but zero at the poles). However, this result does *not* imply that the value of  $g_{\text{eff}}$  is 0.3% smaller at the equator than at the poles, because the value of  $g$  itself (which we've defined to be the acceleration due to the gravitational force only) varies over the surface of the earth, due to its slightly nonspherical shape. (It also varies on a local scale due to density fluctuations and altitude.) When the centrifugal effect is combined with the nonspherical effect, the result is that  $g_{\text{eff}}$  is about 0.5% smaller at the equator; see Iona (1978).

#### REMARKS:

1. We found above that the sum of the gravitational and centrifugal forces doesn't point radially. Interestingly, there are *two* reasons for this. The first, as we just saw, is that under the (seemingly obvious) assumption that the earth's gravitational force is radial, the centrifugal force causes the sum not to be radial. The second reason is that

![Figure 10.3: A diagram of a circle representing a cross-section of the Earth. A vertical arrow labeled ω points upwards from the center, representing the angular velocity vector. A point on the circle is at a polar angle θ from the vertical axis. A vector labeled mg points from this point towards the center. A vector labeled F_cent points from the same point, directed away from the vertical axis (outward from the axis of rotation). A label 'north pole' is at the top of the vertical axis.](cbc139dea50a5cecfb41c09ca0c2c5da_img.jpg)

Figure 10.3: A diagram of a circle representing a cross-section of the Earth. A vertical arrow labeled ω points upwards from the center, representing the angular velocity vector. A point on the circle is at a polar angle θ from the vertical axis. A vector labeled mg points from this point towards the center. A vector labeled F\_cent points from the same point, directed away from the vertical axis (outward from the axis of rotation). A label 'north pole' is at the top of the vertical axis.

Fig. 10.3

![Figure 10.4: A vector diagram showing the relationship between gravitational force mg, centrifugal force -mω × (ω × r), and effective gravity mg_eff. The vector mg points downwards and to the left. The vector -mω × (ω × r) points horizontally to the right. The vector mg_eff is the resultant of these two, pointing downwards and to the right. Dashed lines show the components of mg_eff along the directions of mg and the centrifugal force.](195177d316735f07a9486e555d3a2ed2_img.jpg)

Figure 10.4: A vector diagram showing the relationship between gravitational force mg, centrifugal force -mω × (ω × r), and effective gravity mg\_eff. The vector mg points downwards and to the left. The vector -mω × (ω × r) points horizontally to the right. The vector mg\_eff is the resultant of these two, pointing downwards and to the right. Dashed lines show the components of mg\_eff along the directions of mg and the centrifugal force.

Fig. 10.4

![Diagram of the Earth showing the north pole, angular velocity vector ω, centrifugal force F_cent, and gravitational force mg. The angle θ is shown between the radial direction and the effective gravity direction.](abe516cb67698cbcad10a25fa0c83106_img.jpg)

The diagram shows a cross-section of the Earth. A vertical arrow labeled  $\omega$  points upwards from the center, labeled 'north pole'. A horizontal line represents the equator. A point on the surface is shown with a radial line from the center. A vector  $\mathbf{F}_{\text{cent}}$  points radially outward from this point. A vector  $m\mathbf{g}$  points from the point towards the center. The angle between the radial line and the  $m\mathbf{g}$  vector is labeled  $\theta$ .

Diagram of the Earth showing the north pole, angular velocity vector ω, centrifugal force F\_cent, and gravitational force mg. The angle θ is shown between the radial direction and the effective gravity direction.

Fig. 10.5

the earth's gravitational force actually *isn't* radial; the bulge at the equator causes the gravitational force to point slightly away from the center of the earth (except at the equator or at a pole). This is believable, because the extra mass at the nearby part of the bulge tends to shift the gravitational force in that direction. An exaggerated picture of the situation is shown in Fig. 10.5. The result of the nonradial  $\mathbf{g}$  is that the effective gravitational force points even further from the radial direction than expected. It turns out that the effect from the nonradial  $\mathbf{g}$  on the direction of  $\mathbf{g}_{\text{eff}}$  is roughly equal to the effect from the centrifugal force.

So there is a feedback effect: The spinning of the earth causes  $\mathbf{g}_{\text{eff}}$  to point away from the radial, which causes the earth to bulge (because the surface of the earth is, on average, perpendicular to  $\mathbf{g}_{\text{eff}}$ ), which then causes  $\mathbf{g}_{\text{eff}}$  to point a little further from the radial, which causes the earth to bulge a little more, and so on. Problem 10.12 works out some of the details of this, but see Mohazzabi and James (2000) for further discussion.

- In the construction of buildings, and in similar matters, it is  $\mathbf{g}_{\text{eff}}$ , and not  $\mathbf{g}$ , that determines the “upward” direction in which the building should point. The exact directions of the earth's gravitational force and center of the earth are irrelevant. A plumb bob hanging from the top of a skyscraper touches exactly at the base. Both the bob and the building point in a direction slightly different from both the radial and  $\mathbf{g}$ , but no one cares.
- If you look in a table and find the value for the acceleration due to gravity in Boston, remember that the number is the  $g_{\text{eff}}$  value and not the  $g$  value (which describes only the gravitational force, in our terminology). The way we've defined it, the  $g$  value is the acceleration with which things would fall if the earth kept its same shape but somehow stopped spinning. The exact value of  $g$  is therefore generally irrelevant. ♣

#### 10.2.3 Coriolis force: $-2m\boldsymbol{\omega} \times \mathbf{v}$

While the centrifugal force is a very intuitive concept (we've all gone around a corner in a car), the same thing cannot be said about the Coriolis force. This force requires a nonzero velocity  $\mathbf{v}$  relative to the accelerating frame, and people normally don't move with an appreciable  $\mathbf{v}$  with respect to their car while rounding a corner. To get a feel for this force, let's look at two special cases.

![Diagram of a carousel rotating counterclockwise with angular velocity ω. A person is moving radially inward with velocity v, and the Coriolis force F_cor is shown acting perpendicular to the velocity.](f414d359f23cf7e3bd5a55c8aed00ede_img.jpg)

The diagram shows a circle representing a carousel. In the center, there is a dot with a circle around it, labeled  $\omega$ , indicating rotation out of the page. A point on the right side of the circle has a horizontal arrow pointing left, labeled  $\mathbf{v}$ , representing radial inward motion. From this point, a vertical arrow points upwards, labeled  $\mathbf{F}_{\text{cor}}$ , representing the Coriolis force.

Diagram of a carousel rotating counterclockwise with angular velocity ω. A person is moving radially inward with velocity v, and the Coriolis force F\_cor is shown acting perpendicular to the velocity.

Fig. 10.6

**Case 1 (Moving radially on a carousel):** A carousel rotates counterclockwise with constant angular speed  $\omega$ . Consider someone walking radially inward on the carousel (imagine a radial line painted on the carousel; the person walks along this line), at speed  $v$  with respect to the carousel, at radius  $r$ . The angular velocity vector  $\boldsymbol{\omega}$  points out of the page, where we've signified the “out” direction in Fig. 10.6 by a little circle with a dot inside.

**REMARK:** This remark might be a little picky, but I'll say it anyway. The direction of rotation is sometimes denoted by a curved arrow pointing tangentially along the circumference of the carousel. But this is technically not correct, because it would imply that the carousel is rotating in the rotating frame, which it isn't; it's just sitting there. And it's understood that Fig. 10.6 is in fact drawn in the rotating frame, and not the lab frame, because it includes a fictitious force, which has nothing to do with the lab frame. (If you

wanted to draw things in the lab frame, then you wouldn't draw any fictitious forces, and the velocity  $\mathbf{v}$  would have a tangential component, at least in this setup.) ♣

The Coriolis force,  $-2m\boldsymbol{\omega} \times \mathbf{v}$ , points tangentially in the direction of the motion of the carousel, that is, to the person's right in our scenario. It has magnitude

$$F_{\text{cor}} = 2m\omega v. \quad (10.14)$$

The person will have to counter this force with a tangential friction force of  $2m\omega v$  (pointing to his left) at his feet, so that he continues to walk on the same radial line. Note that there is also the centrifugal force, which is countered by a radial friction force at the person's feet. But this effect won't be important here.

Why does this Coriolis force exist? It exists so that the resultant friction force changes the angular momentum of the person (measured with respect to the lab frame) in the proper way, according to  $\tau = dL/dt$ . To see this, take  $d/dt$  of  $L = mr^2\omega$ , where  $\omega$  is the person's angular speed with respect to the lab frame, which is also the carousel's angular speed. Using  $dr/dt = -v$ , we have

$$\frac{dL}{dt} = -2mr\omega v + mr^2(d\omega/dt). \quad (10.15)$$

But  $d\omega/dt = 0$ , because the person remains on one radial line, and we are assuming that the carousel is arranged to keep a constant  $\omega$ . Equation (10.15) then gives  $dL/dt = -2mr\omega v$ . So the  $L$  (with respect to the lab frame) of the person changes at a rate  $-(2m\omega v)r$ . This is simply the radius times the tangential friction force applied by the carousel. In other words, it is the torque applied to the person.

**REMARK:** What if the person doesn't apply a tangential friction force at his feet? Then the Coriolis force of  $2m\omega v$  produces a tangential acceleration of  $2\omega v$  in the rotating frame, and hence also in the lab frame (initially, before the direction of the motion in the rotating frame has a chance to change), because the frames are related by a constant  $\omega$ . This acceleration exists essentially to keep the person's angular momentum (with respect to the lab frame) constant. (It is constant in this scenario, because there are no tangential forces in the lab frame.) To see that this tangential acceleration is consistent with conservation of angular momentum, set  $dL/dt = 0$  in Eq. (10.15) to obtain  $2\omega v = r(d\omega/dt)$  (this is the person's  $\omega$  here, which is changing). The right-hand side of this is by definition the tangential acceleration. Therefore, saying that  $L$  is conserved is the same as saying that  $2\omega v$  is the tangential acceleration (for this situation where the inward radial speed is  $v$ ). ♣

**Case 2 (Moving tangentially on a carousel):** Now consider someone walking tangentially on a carousel in the direction of the carousel's motion, with speed  $v$  (relative to the carousel) at constant radius  $r$  (see Fig. 10.7). The Coriolis force  $-2m\boldsymbol{\omega} \times \mathbf{v}$  points radially outward with magnitude  $2m\omega v$ . Assume that the person applies the friction force necessary to continue moving at radius  $r$ .

There is a simple way to see why this outward force of  $2m\omega v$  exists. Let  $V \equiv \omega r$  be the speed of a point on the carousel at radius  $r$ , as viewed by an outside observer. If the person moves tangentially (in the same direction as the spinning) with speed  $v$  relative to the carousel, then his speed as viewed by the outside observer is  $V + v$ . The outside observer therefore sees the person walking in a circle of radius  $r$  at speed

![Diagram of a carousel rotating with angular velocity omega (indicated by a dot in a circle). A person is walking tangentially on the carousel at radius r. The person's velocity relative to the carousel is v (upward arrow). The Coriolis force F_cor is shown as a horizontal arrow pointing radially outward from the center of the carousel.](42c2483e10b1c1b532c7e74d2dd3ba28_img.jpg)

Diagram of a carousel rotating with angular velocity omega (indicated by a dot in a circle). A person is walking tangentially on the carousel at radius r. The person's velocity relative to the carousel is v (upward arrow). The Coriolis force F\_cor is shown as a horizontal arrow pointing radially outward from the center of the carousel.

Fig. 10.7

$V + v$ . The acceleration of the person with respect to the ground frame is therefore  $(V + v)^2/r$ . This acceleration must be caused by an inward-pointing friction force at the person's feet, so

$$F_{\text{friction}} = \frac{m(V + v)^2}{r} = \frac{mV^2}{r} + \frac{2mVv}{r} + \frac{mv^2}{r}. \quad (10.16)$$

This friction force is the same in any frame. How, then, does our person on the carousel interpret the three pieces of the inward-pointing friction force in Eq. (10.16)? The first term balances the outward centrifugal force due to the rotation of the frame, which he always feels. The third term is the inward force his feet must apply if he is to walk in a circle of radius  $r$  at speed  $v$ , which is exactly what he is doing in the rotating frame. The middle term is the additional inward friction force he must apply to balance the outward Coriolis force of  $2m\omega v$  (using  $V \equiv \omega r$ ). Said in an equivalent way, the person on the carousel will write down an  $F = ma$  equation of the form (taking radially inward to be positive),

$$\begin{aligned} m \frac{v^2}{r} &= \frac{m(V + v)^2}{r} - \frac{mV^2}{r} - \frac{2mVv}{r} \\ \implies m\mathbf{a} &= \mathbf{F}_{\text{friction}} + \mathbf{F}_{\text{cent}} + \mathbf{F}_{\text{cor}}. \end{aligned} \quad (10.17)$$

We see that the net force he feels does indeed equal his  $ma$ , where  $a$  is measured with respect to the rotating frame. Physically, the difference between the interpretations of Eqs. (10.16) and (10.17) is the existence of fictitious forces in the rotating frame. Mathematically, the difference is simply the rearrangement of terms.

---

For cases in between the two special cases above, things aren't so clear, but that's the way it goes. Note that no matter what direction you move on a carousel, the Coriolis force always points in the same perpendicular direction relative to your motion. Whether it's to your right or to your left depends on the direction of the rotation. But given  $\omega$ , you're stuck with the same relative direction of the force.

On a merry-go-round in the night,  
 Coriolis was shaken with fright.  
 Despite how he walked,  
 'Twas like he was stalked  
 By some fiend always pushing him right.

Let's do some more examples . . .

---

**Example (Dropped ball):** A ball is dropped from height  $h$ , at a polar angle  $\theta$  (measured down from the north pole). How far to the east is the ball deflected, by the time it hits the ground?

**Solution:** The angle between  $\omega$  and  $\mathbf{v}$  is  $\pi - \theta$ , so the Coriolis force  $-2m\omega \times \mathbf{v}$  is directed eastward with magnitude  $2m\omega v \sin \theta$ , where  $v = gt$  is the speed at time

$t$  ( $t$  runs from zero to the usual  $\sqrt{2h/g}$ ).<sup>1</sup> Note that the ball is deflected to the east, independent of which hemisphere it is in. The eastward acceleration at time  $t$  is therefore  $2\omega g t \sin \theta$ . Integrating this to obtain the eastward speed (with an initial eastward speed of zero) gives  $v_{\text{east}} = \omega g t^2 \sin \theta$ . Integrating again to obtain the eastward deflection (with an initial eastward deflection of zero) gives  $d_{\text{east}} = \omega g t^3 \sin \theta / 3$ . Plugging in  $t = \sqrt{2h/g}$  gives

$$d_{\text{east}} = \frac{2\omega h \sin \theta}{3} \sqrt{\frac{2h}{g}}. \quad (10.18)$$

The frequency of the earth's rotation is  $\omega \approx 7.3 \cdot 10^{-5} \text{ s}^{-1}$ , so if we pick  $\theta = \pi/2$  and  $h = 100 \text{ m}$ , for example, then we have  $d_{\text{east}} \approx 2 \text{ cm}$ .

**REMARK:** We can also solve this problem by working in an inertial frame; see Stirling (1983). Figure 10.8 shows the setup where a ball is dropped from a tower of height  $h$  located at the equator (the view is from the south pole). The earth is rotating in the inertial frame, so the initial sideways speed of the ball,  $(R+h)\omega$ , is larger than the sideways speed of the base of the tower,  $R\omega$ . This is the basic cause of the eastward deflection.

However, after the ball has moved to the right, the gravitational force on it picks up a component pointing to the left, and this slows down the sideways speed. If the ball has moved a distance  $x$  to the right, then the leftward component of gravity equals  $g \sin \phi \approx g(x/R)$ . Now, to leading order we have  $x = R\omega t$ , so the sideways acceleration of the ball is  $a = -g(R\omega t/R) = -\omega g t$ . Integrating this, and using the initial speed of  $(R+h)\omega$ , gives a rightward speed of  $(R+h)\omega - \omega g t^2/2$ . Integrating again gives a rightward distance of  $(R+h)\omega t - \omega g t^3/6$ . Subtracting off the rightward position of the base of the tower (namely  $R\omega t$ ), and using  $t \approx \sqrt{2h/g}$  (neglecting higher-order effects such as the curvature of the earth and the variation of  $g$  with altitude), we obtain an eastward deflection of  $\omega h \sqrt{2h/g} (1 - 1/3) = (2/3)\omega h \sqrt{2h/g}$ , relative to the base of the tower. If the ball is dropped at a polar angle  $\theta$  instead of at the equator, then the only modification is that all speeds are decreased by a factor of  $\sin \theta$ , so we obtain the result in Eq. (10.18). ♣

![Figure 10.8: A diagram showing a cross-section of the Earth with radius R. A tower of height h is located at the equator. A ball is dropped from the top of the tower. The Earth is rotating with angular velocity ω. The ball's path is shown as a dashed line, and the base of the tower is shown as a solid line. The angle φ is shown between the vertical and the line from the center to the ball's position. The distance x is shown between the base of the tower and the ball's position.](4b08bd0d3f0460f63e79e7041d4dd3b1_img.jpg)

Figure 10.8: A diagram showing a cross-section of the Earth with radius R. A tower of height h is located at the equator. A ball is dropped from the top of the tower. The Earth is rotating with angular velocity ω. The ball's path is shown as a dashed line, and the base of the tower is shown as a solid line. The angle φ is shown between the vertical and the line from the center to the ball's position. The distance x is shown between the base of the tower and the ball's position.

Fig. 10.8

**Example (Foucault's pendulum):** This is the classic example of a consequence of the Coriolis force. It unequivocally shows that the earth rotates. The basic idea is that due to the rotation of the earth, the plane of a swinging pendulum rotates slowly, with a calculable frequency. In the special case where the pendulum is at one of the poles, this rotation is easy to understand. Consider the north pole. An external observer, hovering above the north pole and watching the earth rotate, sees the pendulum's plane stay fixed (with respect to the distant stars) while the earth rotates counterclockwise beneath it.<sup>2</sup> Therefore, to an observer on the earth, the pendulum's plane rotates clockwise (viewed from above). The frequency of this rotation is of course just the frequency of the earth's rotation, so the earth-based observer sees the pendulum's plane make one revolution each day.

<sup>1</sup> Technically,  $v = gt$  isn't quite correct. Due to the Coriolis force, the ball will pick up a small eastward velocity component (this is the point of the problem). This component will then produce a second-order Coriolis force that affects the vertical speed (see Exercise 10.21). But we can ignore this small effect in this problem. Also, we really mean  $g_{\text{eff}}$  instead of  $g$ , but any ambiguity in this will have a negligible effect.

<sup>2</sup> Assume that the pivot of the pendulum is a frictionless bearing, so that it can't provide any torque to twist the plane of the pendulum.

![Diagram showing a circular pendulum bob in a coordinate system. The vertical axis is labeled y, and a horizontal axis is labeled z. A vector ω points vertically upwards along the y-axis. Another vector ω is shown at an angle θ from the vertical y-axis, pointing towards the z-axis. The angle between the vertical y-axis and the tilted ω vector is labeled θ.](689f2941b150045ffd5966329ce2412b_img.jpg)

Diagram showing a circular pendulum bob in a coordinate system. The vertical axis is labeled y, and a horizontal axis is labeled z. A vector ω points vertically upwards along the y-axis. Another vector ω is shown at an angle θ from the vertical y-axis, pointing towards the z-axis. The angle between the vertical y-axis and the tilted ω vector is labeled θ.

Fig. 10.9

What if the pendulum is not at one of the poles? What is the frequency of the precession? Let the pendulum be located at a polar angle  $\theta$ . We will work in the approximation where the velocity of the pendulum bob is horizontal (with respect to the earth's surface). This is essentially true if the pendulum's string is very long; the correction due to the rising and falling of the bob is negligible. The Coriolis force  $-2m\boldsymbol{\omega} \times \mathbf{v}$  points in some complicated direction, but fortunately we are concerned only with the component that lies in the horizontal plane (that is, the plane of the ground). The vertical component serves only to modify the apparent force of gravity and is therefore negligible. Although the frequency of the pendulum does depend on  $g$ , the resulting modification is very small. With this in mind, let's break  $\boldsymbol{\omega}$  into vertical and horizontal components in a coordinate system located at the pendulum. From Fig. 10.9, we see that

$$\boldsymbol{\omega} = \omega \cos \theta \hat{\mathbf{z}} + \omega \sin \theta \hat{\mathbf{y}}. \quad (10.19)$$

We'll ignore the  $y$  component, because it produces a Coriolis force in the  $z$  direction, since  $\mathbf{v}$  lies in the horizontal  $x$ - $y$  plane. So for our purposes,  $\boldsymbol{\omega}$  is essentially equal to  $\omega \cos \theta \hat{\mathbf{z}}$ . From this point on, the problem of finding the frequency of precession can be done in numerous ways. We'll present two solutions.

**First solution (The slick way):** The horizontal component of the Coriolis force has magnitude

$$F_{\text{cor}}^{\text{horiz}} = |-2m(\omega \cos \theta \hat{\mathbf{z}}) \times \mathbf{v}| = 2m(\omega \cos \theta)v, \quad (10.20)$$

and it is perpendicular to  $\mathbf{v}(t)$ . Therefore, as far as the pendulum is concerned, it is located at the north pole of a planet called Terra Costhetica which has rotational frequency of  $\omega \cos \theta$ .<sup>3</sup> But as we saw above, the precessional frequency of a Foucault pendulum located at the north pole of such a planet is simply

$$\omega_F = \omega \cos \theta, \quad (10.21)$$

in the clockwise direction. So that's our answer.

**Second solution (In the pendulum's frame):** Let's work in the frame of the plane that the Foucault pendulum sweeps through. Our goal is to find the rate of precession of this frame. With respect to a frame fixed on the earth (with axes  $\hat{\mathbf{x}}$ ,  $\hat{\mathbf{y}}$ , and  $\hat{\mathbf{z}}$  as above), we know that this plane rotates with frequency  $\boldsymbol{\omega}_F = -\omega \hat{\mathbf{z}}$  if we're at the north pole ( $\theta = 0$ ), and with frequency  $\boldsymbol{\omega}_F = \mathbf{0}$  if we're at the equator ( $\theta = \pi/2$ ). So it's a good bet that the general answer is  $\boldsymbol{\omega}_F = -\omega \cos \theta \hat{\mathbf{z}}$ , and that's what we'll now show.

Working in the frame of the plane of the pendulum is useful, because we can take advantage of the fact that the pendulum feels no sideways forces in this frame, because otherwise it would move out of the plane (which it doesn't, by definition). The frame fixed on the earth rotates with frequency  $\boldsymbol{\omega} = \omega \cos \theta \hat{\mathbf{z}} + \omega \sin \theta \hat{\mathbf{y}}$ , with respect to the inertial frame. Let the pendulum's plane rotate with frequency  $\boldsymbol{\omega}_F = \omega_F \hat{\mathbf{z}}$  with

<sup>3</sup> As mentioned above, the setup isn't *exactly* like the one on the new planet. There is also a vertical component of the Coriolis force for the pendulum on the earth, but this effect is negligible.

respect to the earth frame. Then the angular velocity of the pendulum's frame with respect to the inertial frame is

$$\boldsymbol{\omega} + \boldsymbol{\omega}_F = (\omega \cos \theta + \omega_F)\hat{\mathbf{z}} + \omega \sin \theta \hat{\mathbf{y}}. \quad (10.22)$$

To find the horizontal component of the Coriolis force in this rotating frame, we care only about the  $\hat{\mathbf{z}}$  part of this frequency. The horizontal Coriolis force therefore has magnitude  $2m(\omega \cos \theta + \omega_F)v$ . But in the frame of the pendulum, there must be zero horizontal force, so this must be zero. Therefore,

$$\omega_F = -\omega \cos \theta. \quad (10.23)$$

This agrees with Eq. (10.21), where we just wrote down the magnitude of  $\omega_F$ .

#### 10.2.4 Azimuthal force: $-m(d\boldsymbol{\omega}/dt) \times \mathbf{r}$

In this section, we will restrict ourselves to the simple and intuitive case where  $\boldsymbol{\omega}$  changes only in magnitude, that is, not in direction (this more complicated case is the subject of Problem 10.10). The azimuthal force may then be written as

$$\mathbf{F}_{az} = -m\dot{\omega}\hat{\boldsymbol{\omega}} \times \mathbf{r}. \quad (10.24)$$

This force is easily understood by considering a person standing at rest with respect to a rotating carousel. If the carousel speeds up, then the person must feel a tangential friction force at his feet if he is to remain fixed on the carousel. This friction force equals  $ma_{\text{tan}}$ , where  $a_{\text{tan}} = r\dot{\omega}$  is the tangential acceleration as measured in the ground frame. But from the person's point of view in the rotating frame, he is not moving, so there must be some other mysterious force that balances the friction. This is the azimuthal force. Quantitatively, when  $\hat{\boldsymbol{\omega}}$  is orthogonal to  $\mathbf{r}$ , we have  $|\hat{\boldsymbol{\omega}} \times \mathbf{r}| = r$ , so the azimuthal force in Eq. (10.24) has magnitude  $mr\dot{\omega}$ . This is the same as the magnitude of the friction force, as it should be.

What we have here is exactly the same effect that we had with the translation force on the accelerating train. If the floor speeds up beneath you, then you must apply a friction force if you don't want to be thrown backward with respect to the floor. If you shut your eyes and ignore the centrifugal force, then you can't tell if you are on a linearly accelerating train, or on an angularly accelerating carousel. The translation and azimuthal forces both arise from the acceleration of the floor. (Well, for that matter, the centrifugal force does too.)

We can also view things in terms of rotational quantities, instead of the linear  $a_{\text{tan}}$  acceleration above. If the carousel speeds up, then a torque must be applied to the person if he is to remain fixed on the carousel, because his angular momentum in the fixed frame increases. Therefore, he must feel a friction

force at his feet. Let's show that this friction force, which produces the change in angular momentum of the person in the fixed frame, exactly cancels the azimuthal force in the rotating frame, thereby yielding zero net force in the rotating frame. Since  $L = mr^2\omega$ , we have  $dL/dt = mr^2\dot{\omega}$  (assuming  $r$  is fixed). And since  $dL/dt = \tau = rF$ , we see that the required friction force is  $F = mr\dot{\omega}$ . And as we saw above, when  $\hat{\omega}$  is orthogonal to  $\mathbf{r}$ , the azimuthal force in Eq. (10.24) also equals  $mr\dot{\omega}$ , in the direction opposite to the carousel's motion. So the tangential forces in the rotating frame do indeed cancel. This was basically the same calculation as the one above, but with an extra factor of  $r$  in the  $\tau = dL/dt$  equation.

**Example (Spinning ice skater):** We have all seen ice skaters increase their angular speed by bringing their arms in close to their body. This can be understood in terms of angular momentum; a smaller moment of inertia requires a larger  $\omega$  in order to keep  $L$  constant. But let's analyze the situation in terms of fictitious forces. We'll idealize things by giving the skater massive hands at the ends of massless arms attached to a massless body.<sup>4</sup> Let the hands have total mass  $m$ , and let them be drawn in radially.

Look at things in the skater's frame (which has an increasing  $\omega$ ), defined by the vertical plane containing the hands. The crucial thing to realize here is that the skater always remains in the skater's frame (a fine tautology, indeed). Therefore, the skater must feel zero net tangential force in her frame, because otherwise she would accelerate with respect to it. Her hands are being drawn in by a muscular force that works against the centrifugal force, but there can be no net tangential force on the hands in the skater's frame, by definition.

What are the tangential forces in the skater's frame? Let the hands be drawn in at speed  $v$  (see Fig. 10.10). Then there is a Coriolis force (in the same direction as the spinning) with magnitude  $2m\omega v$ . There is also an azimuthal force with magnitude  $mr\dot{\omega}$  (in the direction opposite to the spinning, as you can check). Since the net tangential force is zero in the skater's frame, we must have

$$2m\omega v = mr\dot{\omega}. \quad (10.25)$$

Does this relation make sense? Well, let's look at things in the ground frame. The total angular momentum of the hands in the ground frame is constant. Therefore,  $d(mr^2\omega)/dt = 0$ . Taking this derivative and using  $dr/dt \equiv -v$  gives Eq. (10.25).

![Diagram illustrating the forces on a hand being drawn in by a spinning ice skater. A hand (represented by a dot) is at the end of a massless arm of length r. The arm is rotating with angular velocity ω (indicated by a circle with a dot). The hand is moving radially inward with velocity v. Two fictitious forces are shown acting on the hand: the Coriolis force F_cor, which is perpendicular to the arm and points in the direction of rotation, and the azimuthal force F_az, which is also perpendicular to the arm and points opposite to the direction of rotation.](a090c7d291f37dbdad10a59d0c4ec708_img.jpg)

Diagram illustrating the forces on a hand being drawn in by a spinning ice skater. A hand (represented by a dot) is at the end of a massless arm of length r. The arm is rotating with angular velocity ω (indicated by a circle with a dot). The hand is moving radially inward with velocity v. Two fictitious forces are shown acting on the hand: the Coriolis force F\_cor, which is perpendicular to the arm and points in the direction of rotation, and the azimuthal force F\_az, which is also perpendicular to the arm and points opposite to the direction of rotation.

Fig. 10.10

A word of advice about using fictitious forces: Decide which frame you are going to work in (the lab frame or the accelerating frame), and then stick with it. The common mistake is to work a little in one frame and a little in the other without realizing it. For example, you might introduce a centrifugal force on someone sitting at rest on a carousel, but then also give her a centripetal

<sup>4</sup> This reminds me of a joke about a spherical cow.

acceleration. This is incorrect. In the lab frame, there is a centripetal acceleration (caused by the friction force) and no centrifugal force. In the rotating frame, there is a centrifugal force (which cancels the friction force) and no centripetal acceleration (because the person is sitting at rest on the carousel). In short, if you ever mention the words “centrifugal” or “Coriolis,” etc., then you had better be working in an accelerating frame.

### 10.3 Tides

The tides on the earth exist because the gravitational force from a point mass (or a spherical mass, in particular the moon or the sun) is not uniform; the direction of the force is not constant (the force lines converge to the source), and the magnitude is not constant (it falls off like  $1/r^2$ ). On the earth, these effects cause the oceans to bulge around the earth, producing the observed tides. The study of tides is useful in part because tides are a very real phenomenon in the world, and in part because the following analysis gives us an excuse to use fictitious forces and play around with Taylor series approximations. Before considering the general case of tidal forces, let’s look at two special cases.

#### Longitudinal tidal force

In order to isolate the tidal effect, let’s consider a somewhat contrived setup instead of the earth–sun or earth–moon system (we’ll eventually get to these). Consider three masses in a line, as shown in Fig. 10.11. The right mass  $M$  is very large and exerts a gravitational force on  $m_1$  and  $m_2$ . But  $m_1$  and  $m_2$  are sufficiently small so that they don’t exert much of a gravitational force on each other. Furthermore, assume  $m_2 \gg m_1$ . Let  $R$  be the distance from  $M$  to  $m_2$ , and let  $x$  be the distance from  $m_1$  to  $m_2$ . Assume  $x \ll R$ .

The masses  $m_1$  and  $m_2$  accelerate radially inward toward  $M$ . In the accelerating reference frame of  $m_2$ , what is the force on  $m_1$ ? To answer this, we must add the fictitious translation force on  $m_1$  (which points to the left) to the actual gravitational force on  $m_1$  (which points to the right). So in the accelerating frame of  $m_2$ , the net force on  $m_1$  is

$$\begin{aligned}\mathbf{F}_{\text{net}} &= \mathbf{F}_{\text{grav}} + \mathbf{F}_{\text{trans}} = \frac{GMm_1}{(R-x)^2} \hat{\mathbf{x}} - m_1 a_2 \hat{\mathbf{x}} \\ &= \frac{GMm_1}{(R-x)^2} \hat{\mathbf{x}} - \frac{GMm_1}{R^2} \hat{\mathbf{x}}.\end{aligned}\quad (10.26)$$

This is equivalent to the statement that  $m_2$  sees  $m_1$  accelerate away with acceleration

$$\frac{F_{\text{net}}}{m_1} = \frac{GM}{(R-x)^2} - \frac{GM}{R^2} = a_1 - a_2, \quad (10.27)$$

![Diagram showing three masses in a line. From left to right, they are m2, m1, and M. The distance between m1 and m2 is labeled x. The distance between m2 and M is labeled R.](71a7781c82f4ea2a449eaa2310a0f09c_img.jpg)

Diagram showing three masses in a line. From left to right, they are m2, m1, and M. The distance between m1 and m2 is labeled x. The distance between m2 and M is labeled R.

Fig. 10.11

which is just the difference in accelerations you would intuitively expect. Using  $x \ll R$  to make suitable approximations in Eq. (10.26), we have

$$\begin{aligned} F_{\text{net}} &\approx \frac{GMm_1}{R^2 - 2Rx} - \frac{GMm_1}{R^2} = \frac{GMm_1}{R^2} \left( \frac{1}{1 - 2x/R} - 1 \right) \\ &\approx \frac{GMm_1}{R^2} ((1 + 2x/R) - 1) = \frac{2GMm_1x}{R^3}. \end{aligned} \quad (10.28)$$

This is, of course, simply  $x$  times the derivative of the gravitational force. It points to the right, so its effect is to increase the separation of the masses.

If you are riding along on  $m_2$ , and if a black box encloses  $m_1$  and  $m_2$ , then as far as you are concerned, you may as well be in a black box floating freely in outer space (from Einstein's Equivalence Principle, discussed in Chapter 14). But if you are floating in outer space, and if you see  $m_1$  accelerating away from you with acceleration  $F_{\text{net}}/m_1 = 2GMx/R^3$ , then you will naturally conclude that in your reference frame, there must be a mysterious force of

$$"F_{\text{tidal}}" \equiv F_{\text{net}} = \frac{2GMm_1x}{R^3} \quad (10.29)$$

pulling  $m_1$  away from you. This force is called the *tidal force* because it is what causes the tides, as we'll see in detail below. Note that the tidal force is linear in the separation  $x$  and inversely proportional to the *cube* of the distance from the source. If  $x$  is negative, so that  $m_1$  is on the left side of  $m_2$ , then the tidal force is negative, which means that  $m_1$  accelerates leftward away from you. So the effect of the longitudinal tidal force is to increase the separation between the masses, independent of the sign of  $x$ .

If you want to keep  $m_1$  at rest with respect to you, then you will have to tie it down with a string, and the tension in the string will be  $2GMm_1x/R^3$ .<sup>5</sup> Any experiment you do inside the black box will indicate that there is a force pulling  $m_1$  away from you. The only actual force on  $m_1$  is the gravitational force from  $M$  equal to  $GMm_1/(R - x)^2$ , but because  $M$  gives  $m_2$  nearly the same acceleration as  $m_1$ , you perceive only the small  $F_{\text{tidal}}$  in Eq. (10.29). It is indeed small, because it is the actual gravitational force times the quantity  $2x/R \ll 1$ .

#### Transverse tidal force

Consider now the setup shown in Fig. 10.12, with  $m_2$  at the corner of a right triangle that has  $y \ll R$ . The masses  $m_1$  and  $m_2$  accelerate radially inward toward  $M$ . In the accelerating frame of  $m_2$ , what is the force on  $m_1$ ? As above, we must add the fictitious translation force on  $m_1$  (which points to the left) to the actual gravitational force on  $m_1$  (which points to the right and slightly downward).

![Diagram showing a right triangle with vertices m1, m2, and M. M is at the rightmost vertex. m2 is at the bottom-left vertex. m1 is at the top-left vertex, directly above m2. The horizontal distance from m2 to M is labeled R. The vertical distance from m2 to m1 is labeled y. A right angle symbol is at m2. The angle at M between the horizontal line to m2 and the line to m1 is labeled theta.](145db1ef8b9c66e598cbc9251afb37c6_img.jpg)

Diagram showing a right triangle with vertices m1, m2, and M. M is at the rightmost vertex. m2 is at the bottom-left vertex. m1 is at the top-left vertex, directly above m2. The horizontal distance from m2 to M is labeled R. The vertical distance from m2 to m1 is labeled y. A right angle symbol is at m2. The angle at M between the horizontal line to m2 and the line to m1 is labeled theta.

Fig. 10.12

<sup>5</sup> The tension in the string won't affect the acceleration of  $m_2$ , because  $m_2$  is assumed to be much larger than  $m_1$ . So our accelerating frame is still defined to be the one that accelerates with acceleration  $a_2 = GM/R^2$ . This is where the  $m_2 \gg m_1$  assumption comes in.

In this case, however, the *magnitudes* of the gravitational accelerations of  $m_1$  and  $m_2$  are essentially equal, because they are both a distance  $R$  from mass  $M$ , up to second-order effects in  $y/R$  (by the Pythagorean theorem). The *direction* is the only thing that is different, to first order in  $y/R$ . So in the accelerating frame of  $m_2$ , the net force (which we'll call the tidal force from now on) on  $m_1$  is

$$\begin{aligned}\mathbf{F}_{\text{tidal}} &= \mathbf{F}_{\text{grav}} + \mathbf{F}_{\text{trans}} \approx \frac{GMm_1}{R^2}(\cos \theta \hat{\mathbf{x}} - \sin \theta \hat{\mathbf{y}}) - \frac{GMm_1}{R^2} \hat{\mathbf{x}} \\ &\approx \frac{GMm_1}{R^2}(-\sin \theta \hat{\mathbf{y}}) \approx -\frac{GMm_1 y}{R^3} \hat{\mathbf{y}},\end{aligned}\quad (10.30)$$

where we have used  $\cos \theta \approx 1$  and  $\sin \theta \approx y/R$ . This difference is simply the  $y$  component of the force on  $m_1$ , which is what you would expect. It points along the line joining the masses, and its effect is to pull them together. As in the longitudinal case, the transverse tidal force is linear in the separation and inversely proportional to the cube of the distance from the source.

#### General tidal force

We will now calculate the tidal force on a mass  $m$  located at an arbitrary point on a circle of radius  $r$  (for example, this circle could represent a cross section of the earth), due to a mass  $M$  located at the vector  $-\mathbf{R}$  (so the vector from  $M$  to  $m$  is  $\mathbf{R} + \mathbf{r}$ ); see Fig. 10.13. We will calculate the tidal force relative to the center of the circle. That is, we will find the net force on  $m$  in the accelerating frame whose origin is the center of the circle. As usual, assume  $r \ll R$ . And for now let's ignore any orbital motion of the circle around  $M$  (although it turns out that this isn't relevant to tides anyway; see the third remark below), so the circle just accelerates radially inward toward  $M$ .

The gravitational force on  $m$  may be written as  $\mathbf{F}_{\text{grav}} = -GMm(\mathbf{R} + \mathbf{r})/|\mathbf{R} + \mathbf{r}|^3$ . The cube is in the denominator because the vector in the numerator contains one power of the distance. As above, adding on the fictitious translation force due to the acceleration of the center of the circle (which is independent of whatever mass we put there) yields a tidal force of

$$\frac{\mathbf{F}_{\text{tidal}}(\mathbf{r})}{GMm} = \frac{-(\mathbf{R} + \mathbf{r})}{|\mathbf{R} + \mathbf{r}|^3} - \frac{-\mathbf{R}}{|\mathbf{R}|^3}. \quad (10.31)$$

This is the exact expression for the tidal force. However, it is rather useless.<sup>6</sup> Let us therefore make some approximations in Eq. (10.31) and transform it into something technically incorrect (as approximations tend to be), but far more useful. The first thing we need to do is rewrite the  $|\mathbf{R} + \mathbf{r}|$  term. We have

![Diagram illustrating the geometry for calculating the tidal force. A circle of radius r is centered at the origin. A mass m is located on the circle at position vector r. A mass M is located at position vector -R. The vector from M to m is R + r. The diagram shows the vectors r, R, and R+r, and the positions of m and M relative to the center of the circle.](76445d2a92a73ce47da52acf60eac318_img.jpg)

Diagram illustrating the geometry for calculating the tidal force. A circle of radius r is centered at the origin. A mass m is located on the circle at position vector r. A mass M is located at position vector -R. The vector from M to m is R + r. The diagram shows the vectors r, R, and R+r, and the positions of m and M relative to the center of the circle.

Fig. 10.13

<sup>6</sup> This reminds me of a joke about two people lost in a hot-air balloon.

(using  $r \ll R$  and ignoring higher-order terms)

$$\begin{aligned}
 |\mathbf{R} + \mathbf{r}| &= \sqrt{(\mathbf{R} + \mathbf{r}) \cdot (\mathbf{R} + \mathbf{r})} = \sqrt{R^2 + r^2 + 2\mathbf{R} \cdot \mathbf{r}} \\
 &\approx R\sqrt{1 + 2\mathbf{R} \cdot \mathbf{r}/R^2} \\
 &\approx R\left(1 + \frac{\mathbf{R} \cdot \mathbf{r}}{R^2}\right). \quad (10.32)
 \end{aligned}$$

Therefore (again using  $r \ll R$ ),

$$\begin{aligned}
 \frac{\mathbf{F}_{\text{tidal}}(\mathbf{r})}{GMm} &\approx -\frac{\mathbf{R} + \mathbf{r}}{R^3(1 + \mathbf{R} \cdot \mathbf{r}/R^2)^3} + \frac{\mathbf{R}}{R^3} \\
 &\approx -\frac{\mathbf{R} + \mathbf{r}}{R^3(1 + 3\mathbf{R} \cdot \mathbf{r}/R^2)} + \frac{\mathbf{R}}{R^3} \\
 &\approx -\frac{\mathbf{R} + \mathbf{r}}{R^3} \left(1 - \frac{3\mathbf{R} \cdot \mathbf{r}}{R^2}\right) + \frac{\mathbf{R}}{R^3}. \quad (10.33)
 \end{aligned}$$

Letting  $\hat{\mathbf{R}} \equiv \mathbf{R}/R$ , this finally simplifies to (once again using  $r \ll R$ )

$$\mathbf{F}_{\text{tidal}}(\mathbf{r}) \approx \frac{GMm}{R^3} (3\hat{\mathbf{R}}(\hat{\mathbf{R}} \cdot \mathbf{r}) - \mathbf{r}). \quad (10.34)$$

This is the general expression for the tidal force. We can put it in a simpler form if we let  $M$  lie on the positive  $x$  axis, which we can arrange for with a rotation of the axes. We then have  $\hat{\mathbf{R}} = -\hat{\mathbf{x}}$ , and so  $\hat{\mathbf{R}} \cdot \mathbf{r} = -x$ . Equation (10.34) then tells us that the tidal force on a mass  $m$  at position  $\mathbf{r} \equiv (x, y)$ , due to a mass  $M$  at position  $(R, 0)$ , equals

$$\mathbf{F}_{\text{tidal}}(x, y) \approx \frac{GMm}{R^3} (3x\hat{\mathbf{x}} - (x\hat{\mathbf{x}} + y\hat{\mathbf{y}})) = \frac{GMm}{R^3} (2x, -y). \quad (10.35)$$

![Diagram showing a circle with arrows representing tidal forces. The arrows point towards the center of the circle at the top and bottom, and away from the center at the sides, illustrating the stretching effect of tidal forces.](5090ae07773373de4f88145b8ba950df_img.jpg)

Diagram showing a circle with arrows representing tidal forces. The arrows point towards the center of the circle at the top and bottom, and away from the center at the sides, illustrating the stretching effect of tidal forces.

Fig. 10.14

This reduces properly in the longitudinal and transverse cases considered above. The tidal forces at various points on the circle are shown in Fig. 10.14. Since our setup with  $M$  on the  $x$  axis is invariant under rotations around the  $x$  axis, this picture of forces is also invariant. And because of the left-right symmetry, the picture would look the same if  $M$  were placed on the negative  $x$  axis.

The potential energy associated with the tidal force in Eq. (10.35) is proportional to  $-x^2 + y^2/2$ , because the negative gradient of this yields the  $(2x, -y)$  vector. Using  $x = r \cos \theta$  and  $y = r \sin \theta$ , the potential can be written as

$$V_{\text{tidal}}(r, \theta) \approx \frac{GMmr^2}{2R^3} (-2 \cos^2 \theta + \sin^2 \theta) = \frac{GMmr^2}{2R^3} (1 - 3 \cos^2 \theta). \quad (10.36)$$

If the earth were a rigid body, then the tidal force would have no effect on it. But the water in the oceans is free to slosh around, so it bulges along the line from the earth to the moon, and also along the line from the earth to the sun.

And it also gets drawn in and forms a dip along the directions transverse to the moon and sun.<sup>7</sup> We'll see below that the moon's effect is about twice the sun's. As the earth rotates beneath the bulge and dip, a person on the earth sees them rotate in the other direction relative to the earth. From Fig. 10.14, we see that this produces *two* high tides and two low tides per day.<sup>8</sup> It's actually not exactly two per day, because the moon moves around the earth. But this motion is fairly slow, taking about a month, so it's a reasonable approximation to think of the moon as motionless.

Note that it is *not* the case that the moon pushes the water away on the far side of the earth. It pulls on that water, too; it just does so in a weaker manner than it pulls on the rigid part of the earth. With tides, it's not the force that matters, but rather the *difference* in force. Tides are a *comparative* effect. A child playing with a shovel and a pail on a beach will be able to do so only until the earth rotates to a point where the beach enters the region where the moon pulls on the water sufficiently more (or less) than it pulls on the rigid earth.

Whether besieged by an army more grand,  
 Or swamped by the tides in the sand,  
 It's a matter of course  
 That the difference in force  
 Is what leads to a castle's last stand.

#### REMARKS:

1. Consider a mass on the surface of the earth. It turns out that the gravitational force from the sun on it is (much) larger than that from the moon, whereas the tidal force from the sun on it is (slightly) weaker than that from the moon. Quantitatively, the ratio of the gravitational forces is

$$\frac{F_S}{F_M} = \left( \frac{GM_S}{R_{E,S}^2} \right) / \left( \frac{GM_M}{R_{E,M}^2} \right) = \frac{5.9 \cdot 10^{-3} \text{ m/s}^2}{3.3 \cdot 10^{-5} \text{ m/s}^2} \approx 175. \quad (10.37)$$

And the ratio of the tidal forces is

$$\frac{F_{t,S}}{F_{t,M}} = \left( \frac{GM_S}{R_{E,S}^3} \right) / \left( \frac{GM_M}{R_{E,M}^3} \right) = \frac{3.9 \cdot 10^{-14} \text{ s}^{-2}}{8.7 \cdot 10^{-14} \text{ s}^{-2}} \approx 0.45. \quad (10.38)$$

<sup>7</sup> There's actually a lag effect as the earth rotates, due to various complicated things, so the bulge doesn't point directly toward the moon or sun. But let's not worry about that here.

<sup>8</sup> We've made the incorrect but fairly reasonable approximation that the moon lies in the plane of the earth's equator. If you solve the problem exactly by taking into account the position of the moon relative to the equator, you will find that there is a piece of the tides (known as the diurnal tide) that has a period of one day, in addition to the piece we just found (the semidiurnal tide) with a period of half a day. See Horsfield (1976). If you want to derive this result yourself, a hint is that you'll need to use Eqs. (10.36) and (B.7).

Depending on the relative positions of the sun and moon with respect to the earth, their tidal effects may add (when the three bodies are collinear; this is called a “spring” tide), or they may partially cancel (when the sun and moon make a 90° angle in the sky; this is called a “neap” tide).

- Equation (10.38) shows that the moon’s tidal effect is roughly twice the sun’s. This has the following interesting implication about the densities of the moon and sun. The tidal force from, say, the moon is proportional to

$$\left( \frac{GM_M}{R_{E,M}^3} \right) = \left( \frac{G(\frac{4}{3}\pi r_M^3)\rho_M}{R_{E,M}^3} \right) \propto \rho_M \left( \frac{r_M}{R_{E,M}} \right)^3 \approx \rho_M \theta_M^3, \quad (10.39)$$

where  $\theta_M$  is half of the angular size of the moon in the sky. Likewise for the sun’s tidal force. But it just so happens that the angular sizes of the sun and the moon are essentially equal, as you can see by looking at them (preferably quickly in the case of the sun, and through some thick haze), or by noting that total solar eclipses barely exist. Therefore, the combination of Eq. (10.38) and Eq. (10.39) tells us that the moon’s density is about twice the sun’s. It is quite remarkable that, at least roughly, you can experimentally determine the ratio of the densities of two celestial bodies by spending a few weeks at the beach.

- There is one effect that we’ve glossed over, but fortunately it turns out not to be relevant. In the above analysis, we derived the tidal force by subtracting the fictitious translation force from the gravitational force. But in the actual case of the earth, the fictitious force is generally interpreted as a centrifugal force, because the earth is rotating around the earth–moon CM, and this CM is also rotating around the sun. And, of course, the earth is rotating around its axis. Basically, there’s a lot of rotation going on.

Now, because the centrifugal force (from the sum of all the rotations) depends on position, there is a difference between the centrifugal force at the center of the earth and at a point on the surface. Shouldn’t this difference come into play when calculating the net force in the accelerating frame whose origin is the center of the earth? Well, yes ... and no ...

There are many ways of breaking up the earth’s motion, but for the present purposes the most useful way is the following. The motion of any object can be described as the sum of the translation of a nonrotating frame (for example, the seat on a ferris wheel), plus a rotation around a point in that frame (the seat on an old-fashioned ferris wheel wouldn’t have any such rotation, but the seat on a more modern scary kind of amusement park ride undoubtedly would).

The first of these two motions accounts for the motion of the earth as a whole around the earth–moon CM and also for the motion of this CM around the sun.<sup>9</sup> The only relevant fictitious force here is the translation force (at any instant in this motion, every atom in the earth has the same acceleration vector, so there is no need to think in terms of rotation), and this translation force is what we used in the above derivation of the tidal force.<sup>10</sup> The second of the two motions accounts for the rotation of the earth on its axis. This most certainly does create a centrifugal force difference between the center of the earth and a point on the surface, but this difference doesn’t contribute to the tides; it contributes only to the uniform bulge of the earth at the equator. Since the force is uniform, it doesn’t cause water to slosh around, so it therefore doesn’t have anything to do with the tides.

<sup>9</sup> Just imagine grabbing the earth with a very large hand and sliding it around without twisting your hand, so that a given point on the earth always has the same view of stars in the sky.

<sup>10</sup> If you insist on thinking in terms of circular motion as you slide the earth in a circle around the sun without twisting your hand, you can indeed view every point in the earth as moving in a circle. But all of these circles have the same radius; they simply have offset centers. The centrifugal forces are therefore all the same (in both magnitude and direction), and so there are no differences to worry about.

So the answers to the above question are: Yes, because the difference really does contribute to the net force. But no, because it doesn't contribute to the tides, which is what we're concerned with here.

If you work out the actual numbers, you'll see that the centrifugal force completely dominates the tidal force. This is consistent with the fact that the equatorial bulge is on the order of kilometers, whereas the tides are on the order of meters. But the point is that the centrifugal force doesn't affect the tides because it is uniform around the earth. The tidal force, on the other hand, has the nonuniform shape in Fig. 10.14. The football-shaped bulge it creates therefore moves around relative to the earth as the earth rotates beneath it. To sum up: with the tidal force (which we define as the force that produces the tides), we are not concerned with the total difference in force between a point on the earth and the center, but rather only with the part of the difference that isn't invariant under rotations of the earth. ♣

## 10.4 Problems

### Section 10.2: The fictitious forces

#### 10.1. Which way down? \*

You are floating high up in a balloon, at rest with respect to the earth. Give three quasi-reasonable definitions for which point on the ground is right “below” you.

#### 10.2. Longjumping in $g_{\text{eff}}$ \*

If a longjumper can jump 8 meters at the north pole, how far can he jump at the equator? Assume that  $g_{\text{eff}}$  is 0.5% less at the equator than at the north pole (although this is only approximate). Ignore effects of wind resistance, temperature, and runways made of ice.

#### 10.3. $g_{\text{eff}}$ vs. $g$ \*

For what angle  $\theta$  (down from the north pole) is the angle between  $g_{\text{eff}}$  and  $g$  maximum?

#### 10.4. Lots of circles \*

- Two circles in a plane,  $C_1$  and  $C_2$ , each rotate with frequency  $\omega$  relative to an inertia frame. The center of  $C_1$  is fixed in the inertia frame, and the center of  $C_2$  is fixed on  $C_1$ , as shown in Fig. 10.15. A mass is fixed on  $C_2$ . The position of the mass relative to the center of  $C_1$  is  $\mathbf{R}(t)$ . Find the fictitious force felt by the mass.
- $N$  circles in a plane,  $C_i$ , each rotate with frequency  $\omega$  relative to an inertia frame. The center of  $C_1$  is fixed in the inertia frame, and the center of  $C_i$  is fixed on  $C_{i-1}$  (for  $i = 2, \dots, N$ ), as shown in Fig. 10.16. A mass is fixed on  $C_N$ . The position of the mass relative to the center of  $C_1$  is  $\mathbf{R}(t)$ . Find the fictitious force felt by the mass.

![Figure 10.15: A diagram showing two circles, C1 and C2, in a plane. Circle C1 is larger and has its center fixed. Circle C2 is smaller and its center is fixed on the circumference of C1. Both circles are shown rotating with angular frequency omega, indicated by curved arrows.](c37bd494d75d0a653f0927d6eb8f737d_img.jpg)

Figure 10.15: A diagram showing two circles, C1 and C2, in a plane. Circle C1 is larger and has its center fixed. Circle C2 is smaller and its center is fixed on the circumference of C1. Both circles are shown rotating with angular frequency omega, indicated by curved arrows.

Fig. 10.15

![Figure 10.16: A diagram showing a chain of N circles, C1, C2, C3, and C4. Circle C1 is the largest and has its center fixed. The center of C2 is fixed on C1. The center of C3 is fixed on C2. The center of C4 is fixed on C3. Each circle Ci rotates with angular frequency omega relative to an inertia frame, as indicated by curved arrows.](dcb92ff093456314f9b70793cf55e844_img.jpg)

Figure 10.16: A diagram showing a chain of N circles, C1, C2, C3, and C4. Circle C1 is the largest and has its center fixed. The center of C2 is fixed on C1. The center of C3 is fixed on C2. The center of C4 is fixed on C3. Each circle Ci rotates with angular frequency omega relative to an inertia frame, as indicated by curved arrows.

Fig. 10.16

#### **10.5. Mass on a turntable \***

A mass is at rest with respect to the lab frame, while a frictionless turntable rotates beneath it. The frequency of the turntable is  $\omega$ , and the mass is located at radius  $r$ . In the frame of the turntable, find the forces acting on the mass, and verify that  $\mathbf{F} = m\mathbf{a}$ .

#### **10.6. Released mass \***

A mass is bolted down to a frictionless turntable. The frequency of rotation is  $\omega$ , and the mass is located at radius  $a$ . The mass is then released. Viewed from an inertial frame, it travels in a straight line. In the rotating frame, what path does the mass take? Specify  $r(t)$  and  $\theta(t)$ , where  $\theta$  is the angle with respect to the initial radius, as measured in the rotating frame. Solve this by working in the inertial frame. (Exercise 10.25 deals with the more difficult task of working in the rotating frame.)

#### **10.7. Coriolis circles \***

A puck slides with speed  $v$  on frictionless ice. The surface is “level” in the sense that it is orthogonal to  $\mathbf{g}_{\text{eff}}$  at all points. Show that the puck moves in a circle, as seen in the earth’s rotating frame. What is the radius of the circle? What is the frequency of the motion? Assume that the radius of the circle is small compared with the radius of the earth.

#### **10.8. $\boldsymbol{\tau} = d\mathbf{L}/dt$ \*\***

In Section 8.4.3, we derived the three conditions under which it is valid to write  $\sum \boldsymbol{\tau}_i^{\text{ext}} = d\mathbf{L}/dt$ . Rederive these conditions by working entirely in the (possibly) accelerating frame. As in Section 8.4.3, assume that the frame isn’t rotating (so at most, the origin is accelerating).

#### **10.9. Determining your frame \*\***

Imagine that you are on a large rotating disk, with  $\boldsymbol{\omega}$  perpendicular to the disk at its center. Assume that you know that the center of the disk is fixed, and that no real forces act on anything on the disk (except gravity pulling down, which is canceled by the normal force). Assume that  $\boldsymbol{\omega}$  changes only in magnitude, and that this rate of change is constant. Is it possible for you to determine  $\boldsymbol{\omega}$  and  $d\boldsymbol{\omega}/dt$ , and also the location of the center of the disk, by performing experiments in the rotating frame only?

#### **10.10. Changing $\boldsymbol{\omega}$ ’s direction \*\*\***

Consider the special case where a reference frame’s  $\boldsymbol{\omega}$  changes only in direction (that is, not in magnitude). In particular, consider a cone

rolling on a table, which is a natural example of such a situation. Let the origin of the cone frame be the tip of the cone. This point remains fixed in the inertial frame. The instantaneous  $\boldsymbol{\omega}$  for a rolling cone points along its line of contact with the table, because these are the points that are instantaneously at rest. This line precesses around the origin. Let the frequency of the precession be  $\Omega$ .

In order to isolate the azimuthal force, paint a dot on the surface of the cone (call it point  $P$ ), and consider the moment when the dot lies on the instantaneous  $\boldsymbol{\omega}$  (see Fig. 10.17). From Eq. (10.11), we see that there are no contributions from the centrifugal force (because  $P$  lies on  $\boldsymbol{\omega}$ ), the Coriolis force (because  $P$  is not moving in the cone frame), or the translation force (because the tip of the cone is fixed). The only remaining fictitious force is the azimuthal force, and it exists due to the fact that  $\boldsymbol{\omega}$  is changing. Equivalently, it arises from the fact that  $P$  is accelerating up away from the table.

![Diagram of a rolling cone on a horizontal surface. The tip of the cone is at the origin. A solid line represents the cone's surface, making an angle beta with the horizontal. A dashed line represents the cone's axis, also making an angle beta with the horizontal. A point P is marked on the surface. A curved arrow indicates the rotation of the cone. A vector omega is shown pointing along the line of contact between the cone and the surface, which passes through point P.](21ccf422a0903f68d04af3b3bbbac846_img.jpg)

Diagram of a rolling cone on a horizontal surface. The tip of the cone is at the origin. A solid line represents the cone's surface, making an angle beta with the horizontal. A dashed line represents the cone's axis, also making an angle beta with the horizontal. A point P is marked on the surface. A curved arrow indicates the rotation of the cone. A vector omega is shown pointing along the line of contact between the cone and the surface, which passes through point P.

Fig. 10.17

- Find the acceleration of  $P$ .
- Use Eq. (10.11) to calculate the azimuthal force on a mass  $m$  located at  $P$ , and show that the result is consistent with the acceleration you found in part (a).

#### 10.11. Unwinding string \*\*\*\*

A wheel with radius  $R$  is placed flat on a table. A massless string with one end attached to the rim of the wheel is wrapped clockwise around the wheel a large number of times. When the string is wrapped completely around the wheel, a point mass  $m$  is attached to the free end and glued to the wheel. The wheel is then made to rotate with constant angular speed  $\omega$ . At some point, the glue on the mass breaks, and the mass and string gradually unwind (with the speed of the wheel kept constant at  $\omega$  by a motor, if necessary). Show that the length of the unwound string increases at the constant rate  $R\omega$ , for both the clockwise and counterclockwise directions for  $\omega$ . (The latter is the tricky one.)

#### 10.12. Shape of the earth \*\*\*\*

The earth bulges slightly at the equator, due to the centrifugal force in the earth's rotating frame. The goal of this exercise is to find the shape of the earth, first incorrectly, and then correctly.

- The common incorrect method is to assume that the gravitation force from the slightly nonspherical earth points toward the center, and to then calculate the equipotential surface (incorporating both the gravitational and centrifugal forces). Show that this method leads to a surface whose height (relative to a

spherical earth of the same volume) is given by

$$h(\theta) = R \left( \frac{R\omega^2}{6g} \right) (3 \sin^2 \theta - 2), \quad (10.40)$$

where  $\theta$  is the polar angle (the angle down from the north pole), and  $R$  is the radius of the earth.

- (b) The above method is incorrect, because the slight distortion of the earth causes the gravitational force to *not* point toward the center of the earth (except at the equator and the poles). This tilt in the force direction then changes the slope of the equipotential surface, and it turns out (although this is by no means obvious) that this effect is of the same order as the slope of the surface found in part (a). Your task: Assuming that the density of the earth is constant,<sup>11</sup> and that the correct height takes the form of some constant factor  $f$  times the result found in part (a),<sup>12</sup> show that  $f = 5/2$ .<sup>13</sup> Do this by demanding that the potential at a pole equals the potential at the equator. Feel free to do things numerically.

#### 10.13. Southward deflection \*\*\*\*

A ball is dropped from height  $h$  (small compared with the radius of the earth) at a polar angle  $\theta$ . Assume (incorrectly) that the earth is a perfect sphere. Show that a second-order Coriolis effect leads to a *southward* deflection (in the northern hemisphere) equal to  $(2/3)(\omega^2 h^2/g) \sin \theta \cos \theta$ .<sup>14</sup>

It turns out that the actual southward deflection is larger than this; it equals  $4(\omega^2 h^2/g) \sin \theta \cos \theta$ . So apparently there are other effects at work. The main task of this problem is to show how the factor of  $2/3$  turns into a factor of 4. In what follows, we will keep terms up to order  $\omega^2$  (or technically  $\omega^2 R/g$ ) and order  $h/R$ . Also, it will be easiest to calculate southward distances relative to the point on the ground

<sup>11</sup> This isn't true, but it's a very difficult problem to solve with a nonconstant density, assuming that we even know what the density is as a function of radius.

<sup>12</sup> Satellite data show that the general shape found in Eq. (10.40) is essentially correct, up to some factor. This is known as the *quadrupole* shape; the  $(3 \sin^2 \theta - 2)$  term is often written as  $(1 - 3 \cos^2 \theta)$ . I can't think of a clean theoretical way to justify the assumption that the shape is of this form, so let's just accept it. It still makes for a very nice problem.

<sup>13</sup> If  $\Delta h$  is the difference between the equatorial and polar radii, then this factor of  $5/2$  takes the incorrect  $\Delta h$  of about 11 km (as you can show) in Eq. (10.40) and turns it into about 28 km, which is reasonably close to the observed value of 21.5 km. The discrepancy arises from the fact that the density of the earth isn't constant; it decreases with the radius.

<sup>14</sup> By this we mean that the Coriolis effect causes the ball to land this far south of the point where a plumb bob (hanging from where the ball is dropped) touches the ground. Measuring the deflection relative to the point on the ground along the radius to the dropping point would be impractical, because there is no way of knowing where the center of the earth is.

along the radius to the dropping point; call this point  $P$ . But our final goal will be to determine the southward distance relative to a hanging plumb bob.

- Show that the distance between the plumb bob and  $P$  is  $(\omega^2 Rh/g) \sin \theta \cos \theta (1 - h/R)$ .
- The fact that the gravitational force decreases with height implies that the ball takes more time than the standard  $\sqrt{2h/g}$  to hit the ground. Show that the time equals  $\sqrt{2h/g}(1 + 5h/6R)$ .
- Let  $y$  be the height above the ground, and let  $z$  be the southward distance away from the radial line to the dropping point. Show that the centrifugal force yields a southward acceleration away from the radial line equal to  $\ddot{z} = \omega^2(R + y) \sin \theta \cos \theta$ .
- Show that the gravitational force yields a northward acceleration back toward the radial line equal to  $\ddot{z} = -g(z/R)$ .
- Combine parts (b), (c), and (d) to show that the centrifugal and gravitational forces lead to a southward deflection away from  $P$  equal to  $(\omega^2 Rh/g) \sin \theta \cos \theta (1 + 7h/3R)$ . Adding on the above Coriolis effect and subtracting off the position of the plumb bob then quickly yields the desired factor of 4. (This problem is based on Belorizky and Sivardiere (1987).)

### Section 10.3: Tides

#### 10.14. Bead on a hoop \*\*

A bead of mass  $m$  is constrained to move on a frictionless hoop of radius  $r$  that is located a distance  $R$  from an object of mass  $M$ . Assume that  $R \gg r$ , and assume that  $M$  is much larger than the mass of the hoop, which is much larger than  $m$ .

- If the hoop is held fixed and the bead is released from a point close to the rightmost point, as shown in Fig. 10.18, what is the frequency of small oscillations?
- If the hoop is released and the bead starts at a point close to the rightmost point, what is the frequency of small oscillations? Assume that you grab  $M$  and move it to the right to keep it a distance  $R$  from the hoop. (The time scale of oscillations turns out to be on the same order as the time scale of the hoop reaching  $M$ , if  $M$  stays fixed.)

![Diagram for problem 10.14 showing a hoop of radius r with a bead of mass m at its rightmost point. A mass M is located to the right of the hoop at a distance R from its center. A dashed horizontal line with arrows at both ends connects the center of the hoop to mass M.](e25c788cf559895b5643b3bbc9e2c518_img.jpg)

Diagram for problem 10.14 showing a hoop of radius r with a bead of mass m at its rightmost point. A mass M is located to the right of the hoop at a distance R from its center. A dashed horizontal line with arrows at both ends connects the center of the hoop to mass M.

Fig. 10.18

#### 10.15. Precession of the equinoxes \*\*\*

Because the earth bulges at the equator, and because its axis of rotation is tilted with respect to the plane of the ecliptic (the plane containing the sun and (nearly) the moon), the tidal forces from the sun and the moon produce a torque on the earth, which causes the axis of rotation

to precess. The rate of precession is slow; the period is about 26 000 years. Derive (approximately) this result in the following way.<sup>15</sup>

We'll be making some rough approximations here, but our goal is simply to understand intuitively what's going on, and to get an answer that's in the right ballpark. Assume that: (1) the axis of the earth is tilted at  $23^\circ$  with respect to the plane of the ecliptic; (2) the equatorial bulge can be approximated by two point masses located on the equator, at the highest and lowest points relative to the plane of the ecliptic; (3) the mass of each of these effective point masses comes from a patch on the earth with an area of, say,  $r^2$ , where  $r$  is the radius of the earth (this is just a guess); (4) the patch has an essentially constant height of  $h \approx 21$  km, which is the difference between the equatorial and polar radii; (5) the mass density of the patch is roughly the average density of the earth (which isn't true); (6) the earth spends half of its time in the summer/winter orientation, and half in the spring/fall orientation; (7) the moon's tidal effect is twice the sun's. Numerical values of various constants can be found in Appendix J.

### 10.5 Exercises

### *Section 10.2: The fictitious forces*

#### 10.16. **Swirling down a drain \***

Does the Coriolis force cause the rotation you often see in water going down a drain? That is, does the water rotate in different directions in the northern and southern hemispheres? A rough order-of-magnitude argument is sufficient. See Shapiro (1962) for a discussion of this.

#### 10.17. **Magnitude of $\mathbf{g}_{\text{eff}}$ \***

Consider (unrealistically) a perfectly spherical rotating planet whose  $g$  value is constant over the surface. What is the magnitude of  $\mathbf{g}_{\text{eff}}$  as a function of  $\theta$ ? Give your answer to the leading-order correction in  $\omega$ .

#### 10.18. **Oscillations across the equator \***

Consider (unrealistically) a perfectly spherical rotating planet whose  $g$  value is constant over the surface. A bead lies on a frictionless wire that lies in the north–south direction across the equator. The wire takes the form of an arc of a circle; all points are the same distance from the center of the earth. The bead is released from rest, a short distance from the

<sup>15</sup> It's possible to derive this by taking into account the exact shape of the earth, but this is very complicated. It's also possible to derive it to a good approximation by treating the earth's equatorial bulge as a thin ring of mass at the equator, but this is likewise fairly involved; see Haisch (1981). So we'll use a simplified point-mass model, which will still give a reasonable answer.

equator. Because  $\mathbf{g}_{\text{eff}}$  does not point directly toward the earth's center, the bead will head toward the equator and undergo oscillatory motion. What is the frequency of these oscillations?

#### 10.19. Circular pendulum \*

Consider a circular pendulum of mass  $m$  and length  $\ell$ , as shown in Fig. 10.19. The mass swings around in a horizontal circle with the (massless) string always making an angle  $\theta$  with the vertical. Find the angular speed,  $\omega$ , of the mass. Solve this in:

- The lab frame. Draw the free-body diagram for the mass, and write down the  $F = ma$  equations in the vertical and horizontal directions.
- The rotating frame of the pendulum. Draw the free-body diagram for the mass, and write down the  $F = ma$  equations in the vertical and horizontal directions.

![Diagram of a circular pendulum. A mass m is suspended by a string of length l from a fixed point. The string makes an angle theta with the vertical dashed line. The mass moves in a horizontal circle, indicated by a dashed ellipse and a curved arrow showing the direction of motion.](94acff6ac8ab459447a3989b7adf36fc_img.jpg)

Diagram of a circular pendulum. A mass m is suspended by a string of length l from a fixed point. The string makes an angle theta with the vertical dashed line. The mass moves in a horizontal circle, indicated by a dashed ellipse and a curved arrow showing the direction of motion.

Fig. 10.19

#### 10.20. Spinning bucket \*\*

An upright bucket of water is spun at frequency  $\omega$  around its vertical symmetry axis. If the water is at rest with respect to the bucket, find the shape of the water's surface.

#### 10.21. Corrections to gravity \*\*

A mass is dropped from a point directly above the equator. Consider the moment when the object has fallen a distance  $d$ . If we consider only the centrifugal force, then you can quickly show that the correction to  $g_{\text{eff}}$  at this point (relative to the release point) is an increase by  $\omega^2 d$ . There is, however, also a second-order Coriolis effect. What is the sum of these corrections?<sup>16</sup>

#### 10.22. Bug on a hoop \*\*

A hoop of radius  $R$  is made to rotate at constant angular speed  $\omega$  around a diameter, as shown in Fig. 10.20. A small bug of mass  $m$  walks at constant angular speed  $\Omega$  around the hoop. Let  $\mathbf{N}$  be the total force that the hoop applies to the bug when the bug is at the angle  $\theta$  shown, and let  $N_{\perp}$  be the component of  $\mathbf{N}$  that is perpendicular to the plane of the hoop. Find  $N_{\perp}$  in two ways (ignore gravity in this problem):

- Work in the lab frame: At the angle  $\theta$ , find the rate of change of the bug's angular momentum around the rotation axis, and then consider the torque on the bug.
- Work in the rotating frame of the hoop: At the angle  $\theta$ , find the relevant fictitious force, and then take it from there.

![Diagram of a bug on a rotating hoop. A circular hoop of radius R is shown. A vertical dashed line represents the axis of rotation. The hoop rotates with angular speed omega around this axis. A bug is located on the hoop at an angle theta from the vertical axis. The bug walks around the hoop with angular speed Omega relative to the hoop.](74356a412b43925d22f4c67212475b94_img.jpg)

Diagram of a bug on a rotating hoop. A circular hoop of radius R is shown. A vertical dashed line represents the axis of rotation. The hoop rotates with angular speed omega around this axis. A bug is located on the hoop at an angle theta from the vertical axis. The bug walks around the hoop with angular speed Omega relative to the hoop.

Fig. 10.20

<sup>16</sup> The value of  $g$  also varies with height, and this produces an increase in  $g_{\text{eff}}$  equal to  $g(2d/R)$ . You can show that this is much larger than the above centrifugal and Coriolis effects.

#### **10.23. Maximum normal force \*\***

A hoop of radius  $R$  is made to rotate at constant angular speed  $\omega$  around a diameter. A bead on the hoop starts on this diameter and is then given a tiny kick. Let  $\mathbf{N}$  be the total force that the hoop applies to the bead, and let  $N_{\perp}$  be the component of  $\mathbf{N}$  that is perpendicular to the plane of the hoop. At what position(s) along the hoop is  $N_{\perp}$  maximum? What is the magnitude of the total normal force? (Ignore gravity in this problem.)

#### **10.24. Projectile with Coriolis \*\***

At a polar angle  $\theta$ , a projectile is fired eastward at an inclination angle  $\alpha$  above the ground. Find the westward and southward deflections due to the Coriolis force. In terms of  $\theta$ , what angle  $\alpha_{\max}$  yields the maximum total distance of deflection? What is  $\alpha_{\max}$  when  $\theta$  equals  $60^\circ$ ,  $45^\circ$ , and (approximately)  $0^\circ$ ? What about values of  $\theta$  larger than  $60^\circ$ ?

#### **10.25. Free-particle motion \*\***

A particle slides on a frictionless turntable that rotates counterclockwise with constant frequency  $\omega$ . When viewed in an inertial frame, the particle simply travels in a straight line. But in the rotating frame of the turntable, show that the  $F = ma$  equations take the form,

$$\begin{aligned}\ddot{x} &= \omega^2 x + 2\omega\dot{y}, \\ \ddot{y} &= \omega^2 y - 2\omega\dot{x},\end{aligned}\quad (10.41)$$

and verify that the solutions to these differential equations are<sup>17</sup>

$$\begin{aligned}x(t) &= (A + Bt) \cos \omega t + (C + Dt) \sin \omega t, \\ y(t) &= -(A + Bt) \sin \omega t + (C + Dt) \cos \omega t.\end{aligned}\quad (10.42)$$

#### **10.26. Coin on a turntable \*\*\***

A coin stands upright at an arbitrary point on a rotating turntable, and spins (without slipping) at the required angular speed to make its center remain motionless in the lab frame. In the frame of the turntable, the coin rolls around in a circle with the same frequency as that of the turntable. In the frame of the turntable, show that

- (a)  $\mathbf{F} = d\mathbf{p}/dt$ , and
- (b)  $\boldsymbol{\tau} = d\mathbf{L}/dt$  (Hint: Coriolis).

#### **10.27. Precession viewed from rotating frame \*\*\***

Consider a top made of a wheel with all its mass on the rim. A massless rod (perpendicular to the plane of the wheel) connects the CM to a pivot.

<sup>17</sup> If you want, you can derive these solutions in the spirit of Chapter 4 by guessing exponential solutions to the  $F = ma$  equations. You will find that there are degenerate solutions, which lead to the  $(A + Bt)$  type terms that we saw in the critically damped case in Section 4.3.

Initial conditions have been set up so that the top undergoes precession, with the rod always horizontal. In the language of Fig. 9.30, we may write the angular velocity of the top as  $\boldsymbol{\omega} = \Omega \hat{\mathbf{z}} + \omega' \hat{\mathbf{x}}_3$  (where  $\hat{\mathbf{x}}_3$  is horizontal here).

Consider things in the frame rotating around the  $\hat{\mathbf{z}}$  axis with angular speed  $\Omega$ . In this frame, the top spins with angular speed  $\omega'$  around its *fixed* symmetry axis. Therefore, in this frame we must have  $\boldsymbol{\tau} = 0$ , because  $\mathbf{L}$  is constant. Verify explicitly that  $\boldsymbol{\tau} = 0$  (calculated with respect to the pivot) in this rotating frame (you will need to find the relation between  $\omega'$  and  $\Omega$ ). In other words, show that the torque due to gravity is exactly canceled by the torque due to the Coriolis force (you can quickly show that the centrifugal force provides no net torque).

### Section 10.3: Tides

#### 10.28. Maximum tangential force \*

At what angle from the horizontal is the tangential component of the tidal force in Eq. (10.35) maximum?

#### 10.29. Bead on a hoop \*\*

A bead of mass  $m$  is constrained to move on a frictionless hoop of radius  $r$  that is located a distance  $R$  from an object of mass  $M$ . Assume  $R \gg r$ , and assume that  $M$  is much larger than the mass of the hoop, which is much larger than  $m$ .

- If the hoop is held fixed and the bead is released from the top point, as shown in Fig. 10.21, what is its speed when it gets to the rightmost point on the hoop?
- If the hoop is released and the bead starts at a point just slightly to the right of the top point, what is its speed with respect to the hoop when it gets to the rightmost point on the hoop? Assume that you grab  $M$  and move it to the right to keep it a distance  $R$  from the hoop.

![Diagram for Fig. 10.21 showing a bead of mass m on a hoop of radius r. The hoop is centered at a distance R from a large mass M. The bead is at the top of the hoop.](677e05bc3c1aefaed52a2eeaf9d008c5_img.jpg)

The diagram shows a circular hoop of radius  $r$  with a bead of mass  $m$  at its top point. To the right of the hoop is a large mass  $M$ . A horizontal dashed line with arrows at both ends connects the center of the hoop to the mass  $M$ , and is labeled  $R$ .

Diagram for Fig. 10.21 showing a bead of mass m on a hoop of radius r. The hoop is centered at a distance R from a large mass M. The bead is at the top of the hoop.

Fig. 10.21

### 10.30. Facing the planet \*\*

A bead of mass  $m$  is constrained to move on a frictionless hoop of radius  $r$  that orbits a planet of mass  $M$ , a distance  $R$  from it. Initial conditions have been set up so that the plane of the hoop is always perpendicular to the line from it to the planet. Assume  $R \gg r$ , and assume that the mass of the hoop is much larger than  $m$ . Draw the force lines in the reference frame of the hoop (in the spirit of Fig. 10.14). If the bead is released from a point close to the front point on the hoop, what is the frequency of small oscillations?

#### **10.31. Roche limit \*\***

A small spherical rock covered with sand falls in radially toward a planet. Let the planet have radius  $R$  and density  $\rho_p$ , and let the rock have density  $\rho_r$ . It turns out that when the rock gets close enough to the planet, the tidal force ripping the sand off the rock will be larger than the gravitational force attracting the sand to the rock. The cutoff distance is called the Roche limit.<sup>18</sup> Show that it is given by (note the lack of dependence on the rock's radius)

$$d = R \left( \frac{2\rho_p}{\rho_r} \right)^{1/3}. \quad (10.43)$$

#### **10.32. Roche limit with rotation \*\***

If an object orbits a planet in a nonspinning manner (such as the seat of a ferris wheel), then the Roche limit is the same as for the radially falling object in the previous exercise (as you can show). However, show that if an object orbits a planet in such a way that the same side always faces the planet, then the Roche limit is given by

$$d = R \left( \frac{3\rho_p}{\rho_r} \right)^{1/3}. \quad (10.44)$$

## **10.6 Solutions**

### **10.1. Which way down?**

There are actually (at least) four possible definitions for the point “below” you on the ground: (1) the point that lies along the line between you and the center of the earth, (2) the point that lies along the direction of the earth's gravitational force, (3) the point where a hanging plumb bob rests (that is, the point that lies along the direction of the effective gravitational force), and (4) the point where a dropped object hits the ground.

The third definition is the most reasonable, because it defines the upward direction in which buildings are constructed. At any rate, the third and fourth definitions are the only ones you can make any practical use of. The third differs from the second due to the centrifugal force, which makes  $\mathbf{g}_{\text{eff}}$  point in a slightly southward direction (in the northern hemisphere) relative to the gravitational force  $\mathbf{g}$ . It additionally differs from the first due to the fact that  $\mathbf{g}$  isn't radial (see the first remark at the end of Section 10.2.2). And it differs from the fourth due to the Coriolis force, which causes a falling object to be deflected slightly eastward. Note that all four definitions are equivalent at the poles. And the first three are equivalent at the equator.

### **10.2. Longjumping in $\mathbf{g}_{\text{eff}}$**

Let the jumper take off with speed  $v$ , at an angle  $\theta$ . The time to the top of the motion is given by  $g_{\text{eff}}(t/2) = v \sin \theta$ , so the total time is  $t = 2v \sin \theta / g_{\text{eff}}$ . The distance

<sup>18</sup> The Roche limit gives the radial distance below which loose objects won't collect into larger blobs. Our moon (which is a sphere of rock and sand) lies outside the earth's Roche limit. But Saturn's rings (which consist of loose ice particles) lie inside its Roche limit.

traveled is therefore the standard

$$d = v_x t = v t \cos \theta = \frac{2v^2 \sin \theta \cos \theta}{g_{\text{eff}}} = \frac{v^2 \sin 2\theta}{g_{\text{eff}}}. \quad (10.45)$$

This is maximum when  $\theta = \pi/4$ , as we well know. So we see that  $d \propto 1/g_{\text{eff}}$ . Taking  $g_{\text{eff}} \approx 10 \text{ m/s}^2$  at the north pole, and  $g_{\text{eff}} \approx (10 - 0.05) \text{ m/s}^2$  at the equator, we find that the jump at the equator is approximately 1.005 times as long as the one at the north pole. So the longjumper gains about four centimeters. This would be completely washed out by even the tiniest wind effect.

REMARK: For a longjumper, the optimal angle of takeoff is undoubtedly not  $\pi/4$ . The act of changing the direction abruptly from horizontal to such a large angle would entail a significant loss in speed. The optimal angle is some hard-to-determine angle less than  $\pi/4$ . But this won't change our general  $d \propto 1/g_{\text{eff}}$  result (which follows from dimensional analysis). However, we've also made the assumption that the CM of the longjumper starts and ends at the same height, which is definitely not true in longjumping; it is lower at the end. This in fact does change the  $d \propto 1/g_{\text{eff}}$  result. But using the result from Problem 3.17, we see that the effect is small (using values of  $h \approx 1 \text{ m}$  and  $v \approx 10 \text{ m/s}$ ). ♣

### 10.3. $g_{\text{eff}}$ vs. $\mathbf{g}$

The forces  $m\mathbf{g}$  and  $\mathbf{F}_{\text{cent}}$  are shown in Fig. 10.22. The magnitude of  $\mathbf{F}_{\text{cent}}$  is  $mR\omega^2 \sin \theta$ , so the component of  $\mathbf{F}_{\text{cent}}$  perpendicular to  $m\mathbf{g}$  is  $mR\omega^2 \sin \theta \cos \theta = mR\omega^2 (\sin 2\theta)/2$ . For small  $\mathbf{F}_{\text{cent}}$ , maximizing the angle between  $\mathbf{g}_{\text{eff}}$  and  $\mathbf{g}$  is equivalent to maximizing this perpendicular component. Therefore, we obtain the maximum angle when  $\sin 2\theta = 1 \implies \theta = \pi/4$ . The maximum angle turns out to be

$$\phi \approx \tan \phi \approx (mR\omega^2 (\sin \pi/2)/2)/mg = R\omega^2/2g \approx 1.7 \cdot 10^{-3}, \quad (10.46)$$

which is about  $0.1^\circ$ . Because the earth bulges at the equator, the distance from the axis isn't exactly  $R \sin \theta$ , the angle of  $\mathbf{g}$  isn't exactly  $\theta$  (see the first remark at the end of Section 10.2.2), and the magnitude of  $\mathbf{g}$  isn't exactly constant over the surface of the earth. But these effects are negligible, and the optimal  $\theta$  is still essentially  $\pi/4$ .

REMARK: The above solution is an approximate one which is valid only when the magnitude of  $\mathbf{F}_{\text{cent}}$  is much smaller than  $m\mathbf{g}$ . We'll now give an exact solution which is valid when the magnitude of  $\mathbf{F}_{\text{cent}}$  is comparable to  $m\mathbf{g}$ , but which is valid only in the unrealistic case where the planet is a perfect sphere, even though it is spinning. No planet would ever take a spherical shape, because planets aren't rigid. But you could imagine a large spherical rock.

To solve the problem exactly, we can break  $\mathbf{F}_{\text{cent}}$  into components parallel and perpendicular to  $\mathbf{g}$  and make use of the parallel component, in addition to the perpendicular component we used above. If  $\phi$  is the angle between  $\mathbf{g}_{\text{eff}}$  and  $\mathbf{g}$ , then from Fig. 10.22 we have

$$\tan \phi = \frac{mR\omega^2 \sin \theta \cos \theta}{mg - mR\omega^2 \sin^2 \theta}. \quad (10.47)$$

We can then maximize  $\phi$  by taking a derivative. But we need to be careful if  $R\omega^2 > g$ , in which case maximizing  $\phi$  doesn't mean maximizing  $\tan \phi$ . You can work this out, and we'll instead give the following slick geometric solution.

In Fig. 10.23, draw the  $\mathbf{F}_{\text{cent}}$  vectors for various  $\theta$ , relative to  $m\mathbf{g}$  (so we've chosen  $m\mathbf{g}$  always to be vertical in this figure, in contrast with  $\mathbf{F}_{\text{cent}}$  always being horizontal in Fig. 10.22). Since the lengths of the  $\mathbf{F}_{\text{cent}}$  vectors are proportional to  $\sin \theta$ , you can show that the tips of the  $\mathbf{F}_{\text{cent}}$  vectors form a circle. The maximum  $\phi$  is therefore achieved when  $\mathbf{g}_{\text{eff}}$  is tangent to this circle, as shown in Fig. 10.24. In the limit where  $g \gg R\omega^2$  (that is, in the limit of a small circle), we want the point of tangency to

![Figure 10.22: A vector diagram showing the forces acting on an object. A vertical vector labeled mg points downwards. A horizontal vector labeled F_cent points to the right. A dashed vector labeled mg_eff points downwards and to the right, representing the resultant of mg and F_cent. The angle between mg and mg_eff is labeled phi. The angle between mg and the horizontal is labeled theta. A right triangle is formed with mg as the vertical leg, F_cent as the horizontal leg, and mg_eff as the hypotenuse. The angle theta is also shown between mg and the horizontal dashed line.](75eb241c064245881eb44bf6aba9de76_img.jpg)

Figure 10.22: A vector diagram showing the forces acting on an object. A vertical vector labeled mg points downwards. A horizontal vector labeled F\_cent points to the right. A dashed vector labeled mg\_eff points downwards and to the right, representing the resultant of mg and F\_cent. The angle between mg and mg\_eff is labeled phi. The angle between mg and the horizontal is labeled theta. A right triangle is formed with mg as the vertical leg, F\_cent as the horizontal leg, and mg\_eff as the hypotenuse. The angle theta is also shown between mg and the horizontal dashed line.

Fig. 10.22

![Figure 10.23: A geometric diagram illustrating the construction of the effective gravity vector. A vertical vector labeled mg originates from a point. Several vectors labeled F_cent originate from the same point and point in various directions, forming a semi-circle. The tips of these F_cent vectors lie on a circle. A vector labeled mg_eff is shown as a tangent to this circle from the tip of the mg vector. The angle between mg and mg_eff is labeled phi. The angle between the horizontal and the F_cent vectors is labeled theta.](d4a8dcbb31fb0226254c53da4a1f5486_img.jpg)

Figure 10.23: A geometric diagram illustrating the construction of the effective gravity vector. A vertical vector labeled mg originates from a point. Several vectors labeled F\_cent originate from the same point and point in various directions, forming a semi-circle. The tips of these F\_cent vectors lie on a circle. A vector labeled mg\_eff is shown as a tangent to this circle from the tip of the mg vector. The angle between mg and mg\_eff is labeled phi. The angle between the horizontal and the F\_cent vectors is labeled theta.

Fig. 10.23

![Diagram illustrating the forces on a mass in a rotating frame. A vertical dashed line represents the axis of rotation. A circle of radius R is centered on this axis. A mass is located on the circle at an angle theta from the vertical. The centrifugal force F_cent is shown as a vector pointing horizontally to the right from the mass. The gravitational force mg is shown as a vector pointing vertically downwards from the mass. The effective gravitational force mg_eff is shown as a vector pointing downwards and to the right, representing the vector sum of mg and F_cent. The angle phi is shown between the vertical axis and the mg_eff vector. A right-angle symbol indicates that mg_eff is perpendicular to the radius vector from the center of the circle to the mass. The expression mR*omega^2/2 is written near the center of the circle, with arrows indicating the rotation.](1d401188b8071886dead44afc4e0d564_img.jpg)

Diagram illustrating the forces on a mass in a rotating frame. A vertical dashed line represents the axis of rotation. A circle of radius R is centered on this axis. A mass is located on the circle at an angle theta from the vertical. The centrifugal force F\_cent is shown as a vector pointing horizontally to the right from the mass. The gravitational force mg is shown as a vector pointing vertically downwards from the mass. The effective gravitational force mg\_eff is shown as a vector pointing downwards and to the right, representing the vector sum of mg and F\_cent. The angle phi is shown between the vertical axis and the mg\_eff vector. A right-angle symbol indicates that mg\_eff is perpendicular to the radius vector from the center of the circle to the mass. The expression mR\*omega^2/2 is written near the center of the circle, with arrows indicating the rotation.

Fig. 10.24

be the rightmost point on the circle, so the maximum  $\phi$  is achieved when  $\theta = \pi/4$ , in which case  $\phi \approx \sin \phi \approx (R\omega^2/2)/g$ , as we found above. But in the general case, Fig. 10.24 shows that the maximum  $\phi$  is given by

$$\sin \phi_{\max} = \frac{\frac{1}{2}mR\omega^2}{mg - \frac{1}{2}mR\omega^2}. \quad (10.48)$$

In the limit of small  $\omega$ , this is approximately  $R\omega^2/2g$ , as above. Note that this reasoning holds only if  $R\omega^2 < g$ . In the case where  $R\omega^2 > g$  (that is, the circle extends above the top end of the  $mg$  segment), the maximum  $\phi$  is simply  $\pi$ , and it is achieved at  $\theta = \pi/2$ . ♣

### 10.4. Lots of circles

- (a) The fictitious force,  $\mathbf{F}_f$ , on the mass has an  $\mathbf{F}_{\text{cent}}$  part and an  $\mathbf{F}_{\text{trans}}$  part, because the center of  $C_2$  is moving. So the fictitious force is

$$\mathbf{F}_f = m\omega^2\mathbf{r}_2 + \mathbf{F}_{\text{trans}}, \quad (10.49)$$

where  $\mathbf{r}_2$  is the position of the mass in the frame of  $C_2$ . But  $\mathbf{F}_{\text{trans}}$ , which arises from the acceleration of the center of  $C_2$ , equals the centrifugal force felt by a point on  $C_1$ . Therefore,

$$\mathbf{F}_{\text{trans}} = m\omega^2\mathbf{r}_1, \quad (10.50)$$

where  $\mathbf{r}_1$  is the position of the center of  $C_2$  in the frame of  $C_1$ . Substituting this into Eq. (10.49) gives

$$\mathbf{F}_f = m\omega^2(\mathbf{r}_2 + \mathbf{r}_1) = m\omega^2\mathbf{R}(t). \quad (10.51)$$

- (b) The fictitious force,  $\mathbf{F}_f$ , on the mass has an  $\mathbf{F}_{\text{cent}}$  part and an  $\mathbf{F}_{\text{trans}}$  part, because the center of the  $N$ th circle is moving. So the fictitious force is

$$\mathbf{F}_f = m\omega^2\mathbf{r}_N + \mathbf{F}_{\text{trans},N}, \quad (10.52)$$

where  $\mathbf{r}_N$  is the position of the mass in the frame of  $C_N$ . But  $\mathbf{F}_{\text{trans},N}$  equals the centrifugal force felt by a point on the  $(N-1)$ th circle, plus the translation force coming from the movement of the center of the  $(N-1)$ th circle. Therefore,

$$\mathbf{F}_{\text{trans},N} = m\omega^2\mathbf{r}_{N-1} + \mathbf{F}_{\text{trans},N-1}. \quad (10.53)$$

Substituting this into Eq. (10.52) and successively rewriting the  $\mathbf{F}_{\text{trans},i}$  terms in a similar manner, gives

$$\mathbf{F}_f = m\omega^2(\mathbf{r}_N + \mathbf{r}_{N-1} + \cdots + \mathbf{r}_1) = m\omega^2\mathbf{R}(t). \quad (10.54)$$

This turns out so clean because  $\mathbf{F}_{\text{cent}}$  is linear in  $\mathbf{r}$ , and also because all the  $\omega$ 's are the same.

**REMARK:** A much easier way to see that  $\mathbf{F}_f = m\omega^2\mathbf{R}(t)$  is the following. Since all the circles rotate with the same  $\omega$ , they may as well all be glued together. Such a rigid setup does indeed yield the same  $\omega$  for all the circles, just as in the case of the moon rotating once on its axis for every revolution it makes around the earth, thereby causing the same side to always face the earth. It is then clear that the mass simply moves in a circle at frequency  $\omega$ , yielding a fictitious centrifugal force of  $m\omega^2\mathbf{R}(t)$ . And as a bonus, we see that the magnitude of  $\mathbf{R}(t)$  is constant. ♣

### 10.5. Mass on turntable

In the lab frame, the net force on the mass is zero, because it is sitting at rest. (The normal force cancels the gravitational force.) But in the rotating frame, the mass travels in a circle of radius  $r$  with frequency  $\omega$ . So its speed is  $v = \omega r$ . Therefore, in

the rotating frame there must be a net force of  $mv^2/r = m\omega^2r$  inward to account for the centripetal acceleration. And indeed, the mass feels a centrifugal force of  $m\omega^2r$  outward, and a Coriolis force of  $2m\omega v = 2m\omega^2r$  inward, which sum to the desired force (see Fig. 10.25).

**REMARK:** The net inward force in this problem is a little different from the force on a person swinging around in a circle of radius  $r$  and frequency  $\omega$  in an inertial frame. If a skater, for example, maintains a circular path by holding a rope whose other end is attached to a pole, then she has to use her muscles to maintain the position of her torso with respect to her arm, and her head with respect to her torso, etc. But if a person takes the place of the mass in the present problem, then she doesn't need to exert any effort at all to keep her body moving in the circle (which is clear, when viewed from the inertial frame), because each atom in her body is moving at (essentially) the same speed and radius, and therefore feels the same centrifugal and Coriolis forces. So she doesn't really *feel* the net force of  $m\omega^2r$ , in the same sense that someone doesn't feel gravity when in free-fall with no air resistance, because gravity acts on each bit of mass in the same way. (As mentioned on page 462, this similarity with gravity is what led Einstein to his Equivalence Principle.) ♣

![Diagram of a mass moving in a circle of radius r with angular velocity omega. At a point on the circle, three force vectors are shown: a centrifugal force F_cent = m*omega^2*r pointing radially outward, a Coriolis force F_cor = 2*m*omega^2*r pointing radially inward, and a velocity vector v = omega*r pointing tangentially to the circle.](ab6b5d07f4254c95a7cfe6c68a9bd9bc_img.jpg)

Diagram of a mass moving in a circle of radius r with angular velocity omega. At a point on the circle, three force vectors are shown: a centrifugal force F\_cent = m\*omega^2\*r pointing radially outward, a Coriolis force F\_cor = 2\*m\*omega^2\*r pointing radially inward, and a velocity vector v = omega\*r pointing tangentially to the circle.

Fig. 10.25

### 10.6. Released mass

Let the  $x'$  and  $y'$  axes of the rotating frame coincide with the  $x$  and  $y$  axes of the inertial frame at the moment the mass is released (at  $t = 0$ ). Let the mass initially be located on the  $x'$  axis. Then after a time  $t$ , the situation looks like that in Fig. 10.26. The speed of the mass is  $v = a\omega$ , so it has traveled a distance  $a\omega t$ . The angle that its position vector makes with the inertial  $x$  axis is therefore  $\tan^{-1} \omega t$ , with counterclockwise taken to be positive. Hence, the angle that its position vector makes with the rotating  $x'$  axis is

$$\theta(t) = -(wt - \tan^{-1} \omega t). \quad (10.55)$$

And the radius is

$$r(t) = a\sqrt{1 + \omega^2 t^2}. \quad (10.56)$$

For large  $t$ , we have  $r(t) \approx a\omega t$  and  $\theta(t) \approx -wt + \pi/2$ , which make sense because the particle approaches an inertial-frame angle of  $\pi/2$ .

![Diagram showing the position of a mass in a rotating frame. The inertial frame has axes x and y, and the rotating frame has axes x' and y'. The mass is at a distance a*omega*t from the origin. The angle between the x' axis and the position vector is theta. The angle between the x axis and the position vector is tan^-1(omega*t). The initial position is on the x' axis at distance a from the origin.](94e5036c67dc15a2287cbb54c4d944f8_img.jpg)

Diagram showing the position of a mass in a rotating frame. The inertial frame has axes x and y, and the rotating frame has axes x' and y'. The mass is at a distance a\*omega\*t from the origin. The angle between the x' axis and the position vector is theta. The angle between the x axis and the position vector is tan^-1(omega\*t). The initial position is on the x' axis at distance a from the origin.

Fig. 10.26

### 10.7. Coriolis circles

By construction (with the surface being orthogonal to  $\mathbf{g}_{\text{eff}}$  at all points), the normal force from the ice exactly cancels all effects of the gravitational and centrifugal forces in the rotating frame of the earth. We therefore need only concern ourselves with the Coriolis force,  $-2m\boldsymbol{\omega} \times \mathbf{v}$ .

Let the angle down from the north pole be  $\theta$ . We're assuming that the circle is small enough so that  $\theta$  is essentially constant throughout the motion. The component of the Coriolis force that points horizontally along the surface has magnitude  $f = 2mv(\omega \cos \theta)$  and is perpendicular to the direction of motion. (The vertical component of the Coriolis force, which comes from the component of  $\boldsymbol{\omega}$  that points along the surface, simply modifies the required normal force.) Because this force is perpendicular to the direction of motion,  $v$  does not change. Therefore,  $f = 2mv\omega \cos \theta$  is constant. But a constant force perpendicular to the motion of a particle produces a circular path.<sup>19</sup> The radius of the circle is given by

$$2mv\omega \cos \theta = \frac{mv^2}{r} \implies r = \frac{v}{2\omega \cos \theta}. \quad (10.57)$$

The frequency of the circular motion is

$$\omega' = \frac{v}{r} = 2\omega \cos \theta. \quad (10.58)$$

<sup>19</sup> If you want to be mathematical about this, see Footnote 34 in Chapter 9.

To get a rough idea of the size of the circle, you can show (using  $\omega \approx 7.3 \cdot 10^{-5} \text{ s}^{-1}$ ) that  $r \approx 10 \text{ km}$  when  $v = 1 \text{ m/s}$  and  $\theta = 45^\circ$ . Even the tiniest bit of friction will clearly make this effect impossible to see. In the special case of  $\theta \approx \pi/2$  (that is, near the equator), the component of the Coriolis force along the surface is negligible, so  $r$  becomes large, and  $\omega'$  goes to 0.

REMARK: In the limit  $\theta \approx 0$  (that is, near the north pole), the Coriolis force essentially points along the surface. The above equations give  $r \approx v/(2\omega)$ , and  $\omega' \approx 2\omega$ . For the special case where the center of the circle is the north pole, this  $\omega' \approx 2\omega$  result might seem incorrect, because you might want to say that the circular motion should be achieved by having the puck remain motionless in the inertial frame, while the earth rotates beneath it (thus making  $\omega' = \omega$ ). The error in this reasoning is that the “level” earth is not spherical, due to the nonradial direction of  $\mathbf{g}_{\text{eff}}$ . If the puck starts out motionless in the inertial frame, it will be drawn toward the north pole, due to the component of the gravitational force along the nonspherical “level” earth. In order not to fall toward the pole, the puck needs to travel with frequency  $\omega$  (relative to the inertial frame) in the direction opposite<sup>20</sup> to the earth’s rotation. The reason for this is that in the rotating frame of the puck, the puck feels the same centrifugal force that it would feel if it were at rest in the frame of the earth, spinning along with it, because these two frames have the same magnitude of  $\omega$ ; the  $\omega$ ’s point in opposite directions, but this doesn’t affect the centrifugal force. The puck therefore happily stays at the same  $\theta$  value on the “level” surface, just as a puck at rest on the earth does. The angular velocity of the puck with respect to the earth is therefore  $(-\omega) - (\omega) = -2\omega$ , where the minus sign signifies the backward direction. ♣

#### 10.8. $\boldsymbol{\tau} = d\mathbf{L}/dt$ \*

Let  $\mathbf{r}'_i$  be the position vector in the accelerating frame. (In terms of the quantities in Section 8.4.3,  $\mathbf{r}'_i$  equals  $\mathbf{r}_i - \mathbf{r}_0$ .) The total angular momentum of an object in the accelerating frame is

$$\mathbf{L} = \sum_i \mathbf{r}'_i \times m_i \dot{\mathbf{r}}'_i. \quad (10.59)$$

Therefore,

$$\begin{aligned} \frac{d\mathbf{L}}{dt} &= \sum_i \dot{\mathbf{r}}'_i \times m_i \dot{\mathbf{r}}'_i + \sum_i \mathbf{r}'_i \times m_i \ddot{\mathbf{r}}'_i \\ &= 0 + \sum_i \mathbf{r}'_i \times \mathbf{F}_i^{\text{total}} \\ &= \sum_i \mathbf{r}'_i \times (\mathbf{F}_i^{\text{real,ext}} + \mathbf{F}_i^{\text{real,int}} + \mathbf{F}_i^{\text{fictitious}}). \end{aligned} \quad (10.60)$$

The first term,  $\sum \mathbf{r}'_i \times \mathbf{F}_i^{\text{real,ext}}$ , equals the total external torque measured relative to the origin of the accelerating frame, as desired. The second term,  $\sum \mathbf{r}'_i \times \mathbf{F}_i^{\text{real,int}}$ , equals the total torque from internal forces, which is zero by the same reasoning as in Section 8.4.3. The third term,  $\sum \mathbf{r}'_i \times \mathbf{F}_i^{\text{fictitious}}$ , is the tricky one. Since the frame isn’t rotating, we have at most the fictitious translation force. So this term equals

$$\sum \mathbf{r}'_i \times (-m_i \ddot{\mathbf{r}}_0) = -\sum m_i \mathbf{r}'_i \times \ddot{\mathbf{r}}_0 = -M \mathbf{r}'_{\text{CM}} \times \ddot{\mathbf{r}}_0, \quad (10.61)$$

where  $\mathbf{r}'_{\text{CM}}$  is the position of the object’s CM in the accelerating frame, and  $\mathbf{r}_0$  is the position of the origin of the frame with respect to the inertial lab frame. This result

<sup>20</sup> Of course, the puck can also move with frequency  $\omega$  in the *same* direction as the earth’s rotation. But in this case, the puck simply sits at one spot on the earth.

agrees with the second term in Eq. (8.45), where  $\mathbf{r}'_{\text{CM}}$  is written as  $\mathbf{R} - \mathbf{r}_0$ . The three conditions under which the third term vanishes are therefore: (1)  $\mathbf{r}'_{\text{CM}} = 0$ , that is, the CM is located at the origin of the accelerating frame. The fictitious translation force acts just like a gravitational force, so as far as the torque is concerned, the translation force acts at the CM. Therefore, if the CM is located at the origin, the translation force has no lever arm and thus provides no torque. (2)  $\ddot{\mathbf{r}}_0 = 0$ , that is, the origin is not accelerating, so there is no translation force. (3)  $\mathbf{r}'_{\text{CM}}$  is parallel to  $\ddot{\mathbf{r}}_0$ . This means that if the translation force is considered to be a gravitational force, then the CM lies directly “above” or “below” the origin. So there is no lever arm and thus no torque.

If the frame is rotating in addition to translating, then in general there will be torques from the centrifugal, Coriolis, and azimuthal forces, even if the CM is chosen as the origin. This is true because these fictitious forces involve  $\mathbf{r}$  (or  $\dot{\mathbf{r}}$ ), which results in the torque not being linear in  $\mathbf{r}$  (because there is already an  $\mathbf{r}$  in  $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ ). This then means that the  $\mathbf{r}'_{\text{CM}}$  position vector doesn’t arise in the calculation of  $d\mathbf{L}/dt$  as it did in Eq. (10.61).

#### 10.9. Determining your frame

Yes. You can determine  $\omega$  and  $d\omega/dt$  as follows. Simultaneously measure the forces on particles of mass  $m$  at rest at positions  $\mathbf{r}_1$  and  $\mathbf{r}_2$ . The centrifugal and azimuthal are the relevant forces, so the difference in the forces at the two locations is

$$\Delta \mathbf{F} \equiv \mathbf{F}_1 - \mathbf{F}_2 = -m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times (\mathbf{r}_1 - \mathbf{r}_2)) - m \frac{d\boldsymbol{\omega}}{dt} \times (\mathbf{r}_1 - \mathbf{r}_2). \quad (10.62)$$

Using the fact that the cross product of two vectors is perpendicular to each vector, we see that the magnitudes of the components of  $\Delta \mathbf{F}$  parallel and perpendicular to  $\mathbf{r}_1 - \mathbf{r}_2$  are  $F_{\parallel} = m\omega^2|\mathbf{r}_1 - \mathbf{r}_2|$  and  $F_{\perp} = m(d\omega/dt)|\mathbf{r}_1 - \mathbf{r}_2|$ . So we have

$$\omega = \sqrt{\frac{F_{\parallel}}{m|\mathbf{r}_1 - \mathbf{r}_2|}}, \quad \text{and} \quad \frac{d\omega}{dt} = \frac{F_{\perp}}{m|\mathbf{r}_1 - \mathbf{r}_2|}. \quad (10.63)$$

These expressions give  $\omega$  and  $d\omega/dt$  in terms of measured quantities. Note that we needed to measure the force at two points here. Measuring the force of  $-m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r}) - m(d\boldsymbol{\omega}/dt) \times \mathbf{r}$  at only one point  $\mathbf{r}$  doesn’t give us anything, because we don’t yet know where the origin is, so we don’t know the value of  $\mathbf{r}$ . But with two points, the difference  $\mathbf{r}_1 - \mathbf{r}_2$  is independent of the location of the origin.

If you want, you can check the result for  $\omega$  by finding the difference between the forces on two objects at essentially the same location, one of which is at rest and the other of which is moving with velocity  $\mathbf{v}$ . Because the  $\mathbf{r}$  values are the same, only the Coriolis term survives in the difference. This gives  $\omega = |\Delta \mathbf{F}|/(2mv)$ .

To find the center of the disk, measure the force on a particle at a given location. Break this force into orthogonal components in the ratio of  $d\omega/dt$  to  $\omega^2$ , by drawing a line at an angle of  $\tan^{-1}(d\omega/dt)/\omega^2$  with respect to the force. Whether this line is to the right or to the left of the force depends on whether the  $\mathbf{r}_1 - \mathbf{r}_2$  vector above was to the right or to the left of the  $\Delta \mathbf{F}$  vector. This line contains the component proportional to  $\omega^2$ , which is the radial component. The line therefore passes through the center of the disk. So if we repeat the process with the particle at another location (not along the line) and draw a similar line, then the intersection of the two lines is the center of the disk.

REMARK: If we remove the restriction that there aren’t any real forces, then it isn’t possible to determine the three desired quantities, because someone could claim that  $\omega$ ,  $d\omega/dt$ , and the location of the center are different from what you found, and he could then just say that there are a bunch of (contrived) real forces that conspire to make the total force be what you observe. ♣

![Figure 10.27: A 3D diagram showing a cone rotating with angular velocity ω around its vertical axis. A point P is on the base of the cone at a distance r from the axis. A point Q is on the axis at a height h above P. A dashed line shows the path of Q as it moves horizontally with speed v_Q = ωh. The angular speed of the cone is ω, so Q moves a distance ωht to the side. The distance ωht is also the horizontal distance between P and P'.](75b87dd9c4793fecf72360657d2a885e_img.jpg)

Figure 10.27: A 3D diagram showing a cone rotating with angular velocity ω around its vertical axis. A point P is on the base of the cone at a distance r from the axis. A point Q is on the axis at a height h above P. A dashed line shows the path of Q as it moves horizontally with speed v\_Q = ωh. The angular speed of the cone is ω, so Q moves a distance ωht to the side. The distance ωht is also the horizontal distance between P and P'.

Fig. 10.27

![Figure 10.28: Horizontal end views of the cone. The top view shows point Q on the axis and point P on the base. The bottom view shows point Q on the axis and point P' on the base, with a distance ωht between P and P'. The height h is indicated.](c66b7d4486c4239b444f4fc9f83b9868_img.jpg)

Figure 10.28: Horizontal end views of the cone. The top view shows point Q on the axis and point P on the base. The bottom view shows point Q on the axis and point P' on the base, with a distance ωht between P and P'. The height h is indicated.

Fig. 10.28

#### 10.10. Changing $\omega$ 's direction

- (a) Let  $Q$  be the point on the axis of the cone directly above  $P$ , and let its height above  $P$  be  $h$  (see Fig. 10.27). Consider the situation an infinitesimal time  $t$  later. Let  $P'$  be the point that is now directly below  $Q$  (see Fig. 10.28). The angular speed of the cone is  $\omega$ , so  $Q$  moves horizontally with speed  $v_Q = \omega h$ . Therefore, in the infinitesimal time  $t$ ,  $Q$  moves a distance  $\omega h t$  to the side.

This distance  $\omega h t$  is also (essentially) the horizontal distance between  $P$  and  $P'$ . Therefore, a little geometry tells us that  $P$  is now a height

$$y(t) = h - \sqrt{h^2 - (\omega h t)^2} = h - h\sqrt{1 - (\omega t)^2} \approx \frac{(\omega t)^2 h}{2} = \frac{1}{2}(\omega^2 h)t^2 \quad (10.64)$$

above the table. Since  $P$  started on the table with zero speed, this means that  $P$  undergoes an acceleration of  $\omega^2 h$  in the vertical direction. A mass  $m$  located at  $P$  must therefore feel a real force (normal force or whatever) of  $F_P = m\omega^2 h$  in the upward direction, if it is to remain motionless with respect to the cone.

- (b) The precession frequency  $\Omega$  (which is how fast  $\omega$  swings around the origin) is equal to the speed of  $Q$  divided by  $r$ , where  $r$  is the distance from  $Q$  to the  $z$  axis (that is, the radius of the circle  $Q$  travels in). Therefore,  $\Omega$  has magnitude  $v_Q/r = \omega h/r$ , and it points in the  $-\hat{z}$  direction, for the situation shown in Fig. 10.27. Hence,  $d\omega/dt = \Omega \times \omega$  has magnitude  $\omega^2 h/r$ , and it points out of the page in Fig. 10.27 (or to the left in Fig. 10.28). Therefore,  $\mathbf{F}_{az} = -m(d\omega/dt) \times \mathbf{r}$  has magnitude  $m\omega^2 h$ , and it points in the  $-\hat{z}$  direction.

A person of mass  $m$  at point  $P$  therefore interprets the situation as, “I am not accelerating with respect to the cone. Therefore, the net force on me in the cone frame is zero. And indeed, the upward normal force  $F_P$  from the cone, with magnitude  $m\omega^2 h$ , is exactly balanced by the mysterious downward force  $F_{az}$ , also with magnitude  $m\omega^2 h$ .”

Note that this azimuthal force is still basically the same effect as with the translation force, the centrifugal force, and the simpler case of the azimuthal force discussed in Section 10.2.4. In all of these cases, the “ground” accelerates, so you feel like you are getting flung in the opposite direction with respect to the accelerating frame.

### 10.11. Unwinding string

Consider the clockwise direction. This case is easily solved by working in the lab frame. After the glue breaks, the mass moves in the straight line of the tangent, because the string can't provide a transverse force unless the mass has already diverged from this straight line, which it hasn't. The speed at which the mass starts this straight-line motion (when the glue breaks) is  $R\omega$ . And it continues to move at this speed because the angular speed of the wheel allows the string to unwind at a rate  $R\omega$ , which is exactly the rate needed. Note that the string has zero tension in it, so it's just like it's not there.

The counterclockwise direction is trickier, because simple linear motion isn't consistent with the constraint that the mass stays tied to the string. There is now a tension in the string, and the mass undergoes a spiral motion, which makes things more difficult. It's possible to solve this problem with  $F = ma$ , and also with the Lagrangian method. But we'll solve it here by using a slick argument in a rotating frame. Part of the trickiness of this approach is choosing which rotating frame to use. The most obvious frame is the rotating frame of the wheel, but this frame isn't too helpful, because the mass undergoes a spiral motion which is hard to get a handle on (however, see the fourth remark below). It would be nice to work in a frame where the mass undergoes a simple kind of motion. It turns out that if we consider the frame that rotates counterclockwise at  $2\omega$  instead of  $\omega$ , things turn out to be simple.

The general idea is the following. In this new frame that rotates counterclockwise at  $2\omega$ , the wheel rotates *clockwise* at  $\omega$ . Therefore, if there were no such things as fictitious forces, then we would have exactly the same situation as in the clockwise case we solved above, so we would be done. The bad news, however, is that fictitious forces do exist. And so without any miraculous cancellation, these forces will lead to a transverse force, causing the string's contact point to move one way or another, thereby causing the unwound length to increase at a rate other than  $R\omega$ . But the good news is that such a miraculous cancellation does indeed occur. Let's see why.

In the frame that rotates counterclockwise at  $2\omega$ , consider the moment right after the mass leaves the wheel, as shown in Fig. 10.29. The velocity of the mass at this time is  $v = R\omega$ , directed to the right. What are the forces on the mass? There may be a tension (it happens to be zero right at the start, but then it grows, as we'll see below), and then there are also the centrifugal and Coriolis forces. The centrifugal force is initially (right when the glue breaks) directed radially upward with magnitude  $mR(2\omega)^2 = 4mR\omega^2$ . The Coriolis force is (as you can verify) initially directed downward with magnitude  $2m(2\omega)v = 2m(2\omega)(R\omega) = 4mR\omega^2$ . These two forces cancel, so the mass feels no transverse force, so it continues to move in a straight line to the right.

What about a later time? Assume (in an inductive spirit) that the mass is still on the straight line determined by its initial motion and moving with speed  $R\omega$ . The Coriolis force is still directed downward with magnitude  $4mR\omega^2$ . And the centrifugal force is directed radially outward with magnitude  $mr(2\omega)^2$ , where  $r$  is the present radius, as shown in Fig. 10.30. The vertical component of this force is obtained by multiplying by  $R/r$ , so we again obtain an upward vertical component of  $4mR\omega^2$ . This therefore cancels the Coriolis force, and we again have the result that there is no transverse force. So we see that if the mass is presently moving in the straight line determined by its initial motion, then it will continue to move in this straight line. And since it is by definition initially moving in this line, we see inductively that it moves in this line for all time, as we wanted to show. Note that the horizontal component of the centrifugal force needs to be canceled by the tension (because the string doesn't stretch), so the tension is nonzero in this scenario, in contrast with the clockwise scenario above. Since the string is always taut, the speed of the mass is determined by the rate at which the wheel rotates, which means that the speed of the mass is always  $R\omega$  in this frame. The rate of increase in the unwound string's length is therefore  $R\omega$  (in any frame).

#### REMARKS:

1. The tension equals the longitudinal component of the centrifugal force. This component is obtained by multiplying the centrifugal force by  $d/r$ , where  $d$  is the length of unwound string. The tension therefore equals  $4md\omega^2$ , so it grows linearly with  $d$ .
2. Even if the string is massive, and even if the density varies, the unwound length still increases at a rate  $R\omega$ , because the above reasoning can be used with every atom in the string. This result is a bit surprising, because when viewed in the lab frame, it is by no means obvious that a massive string remains straight.
3. If we hadn't been told in the statement of the problem that the unwound string's length increases at a rate  $R\omega$ , then the problem would of course be more difficult. For all we'd know, the rate might not even be constant. Aside from making a lucky guess that the rate is  $R\omega$ , we'd have to solve the problem with  $F = ma$  or the Lagrangian method. The former is rather tricky, but the latter isn't so bad.
4. There's actually an even slicker solution for the counterclockwise case than the one we gave above. It goes as follows. First consider the simpler *clockwise* case, and look at the setup in the rotating frame of the wheel. In this case, the centrifugal and Coriolis forces conspire to make the mass move in a backward spiral, the beginning of which is shown in Fig. 10.31. We know from our lab-frame reasoning above that in the lab frame the string provides no force during

![Figure 10.29: A diagram showing a wheel rotating clockwise with angular velocity ω. A mass is at the top of the wheel, moving to the right with velocity Rω. The wheel's center is marked with a circle and a dot, and the angular velocity is labeled 2ω.](fee8df3753006e6fb206b361826fd114_img.jpg)

Figure 10.29: A diagram showing a wheel rotating clockwise with angular velocity ω. A mass is at the top of the wheel, moving to the right with velocity Rω. The wheel's center is marked with a circle and a dot, and the angular velocity is labeled 2ω.

view in “ $2\omega$ ”  
rotating frame

Fig. 10.29

![Figure 10.30: A diagram showing a wheel rotating clockwise with angular velocity ω. A mass is at a distance r from the center, moving to the right with velocity Rω. The centrifugal force Fcent is directed radially outward, and the Coriolis force Fcor is directed downward. The horizontal distance from the center to the mass is d.](8dfb90a5c34302e5f557c8f7ca7b1cc0_img.jpg)

Figure 10.30: A diagram showing a wheel rotating clockwise with angular velocity ω. A mass is at a distance r from the center, moving to the right with velocity Rω. The centrifugal force Fcent is directed radially outward, and the Coriolis force Fcor is directed downward. The horizontal distance from the center to the mass is d.

view in “ $2\omega$ ”  
rotating frame

Fig. 10.30

![Figure 10.31: A diagram showing a wheel rotating clockwise with angular velocity ω. A mass is at a distance r from the center, moving to the right with velocity Rω. The centrifugal and Coriolis forces conspire to make the mass move in a backward spiral, the beginning of which is shown.](fdf7e7713f3f8923440e5c8a11d3b654_img.jpg)

Figure 10.31: A diagram showing a wheel rotating clockwise with angular velocity ω. A mass is at a distance r from the center, moving to the right with velocity Rω. The centrifugal and Coriolis forces conspire to make the mass move in a backward spiral, the beginning of which is shown.

view in rotating  
frame

Fig. 10.31

this motion, but that it does in fact remain straight. And the rate of change of the unwound length is  $R\omega$ .

Now consider the more difficult counterclockwise case in the rotating frame of the wheel. The only difference from the clockwise case is that the  $\omega$  vector has switched direction, and now points out of the page. The centrifugal force is therefore still the same function of  $\mathbf{r}$ , but the Coriolis force has switched signs, as a function of  $\mathbf{v}$ . However, the centrifugal force is the only force that does work on the mass (because the Coriolis force and the tension are perpendicular to the velocity), so the mass ends up moving at the same speed as a function of  $\mathbf{r}$  as in the clockwise case. The string constrains the mass to move along the same path as in the clockwise case (because the string is straight in both cases), and the only effect of the Coriolis force is to increase the tension. The motion is therefore exactly the same (same path, same speed as a function of  $\mathbf{r}$ ), so the rate of change of the unwound length is again  $R\omega$ . ♣

#### 10.12. Shape of the earth

- (a) The potential energy function derived from the sum of the gravitational and centrifugal forces must be constant along the surface. Otherwise, a piece of the earth would want to move along the surface, which would mean that we didn't have the correct surface to begin with.

If  $x$  is the distance from the earth's axis, then the centrifugal force is  $F_c = m\omega^2 x$ , directed outward. The potential energy function for this force is  $V_c = -m\omega^2 x^2/2$ , up to an arbitrary additive constant. Under the assumption that the distortion of the earth doesn't change the gravitational force (which isn't correct, as we'll see below), the potential energy for the gravitation force is  $mgh$ , where we've arbitrarily chosen the original spherical surface to correspond to  $h = 0$ . The equal-potential condition is therefore

$$mgh - \frac{m\omega^2 x^2}{2} = C, \quad (10.65)$$

where  $C$  is a constant to be determined. Using  $x = r \sin \theta$ , we obtain

$$h = \frac{\omega^2 r^2 \sin^2 \theta}{2g} + B, \quad (10.66)$$

where  $B \equiv C/(mg)$  is another constant. We may replace the  $r$  here with the radius of the earth,  $R$ , with negligible error.

Depending what the constant  $B$  is, this equation describes a whole family of surfaces. We can determine the correct value of  $B$  by demanding that the volume of the distorted earth be the same as it would be in its spherical shape if the centrifugal force were turned off. This is equivalent to demanding that the integral of  $h$  over the surface of the earth is zero. The integral of  $(a \sin^2 \theta + b)$  over the surface of the earth is (the integral is easy if we write  $\sin^2 \theta$  as  $1 - \cos^2 \theta$ )

$$\begin{aligned} & \int_0^\pi (a(1 - \cos^2 \theta) + b) 2\pi R^2 \sin \theta \, d\theta \\ &= \int_0^\pi (-a \cos^2 \theta + (a + b)) 2\pi R^2 \sin \theta \, d\theta \\ &= 2\pi R^2 \left( \frac{a \cos^3 \theta}{3} - (a + b) \cos \theta \right) \Big|_0^\pi \\ &= 2\pi R^2 \left( -\frac{2a}{3} + 2(a + b) \right). \end{aligned} \quad (10.67)$$

Therefore, we need  $b = -(2/3)a$  for this integral to be zero. Plugging this result into Eq. (10.66) gives

$$h = R \left( \frac{R\omega^2}{6g} \right) (3 \sin^2 \theta - 2), \quad (10.68)$$

as desired.

- (b) For convenience, let the correct height be  $h \equiv \beta(3 \sin^2 \theta - 2)$ , with  $\beta \equiv fR(R\omega^2/6g)$ , where  $f$  is the desired fraction.

Consider the earth to be the superposition of the  $h = 0$  sphere plus an effective shell of positive or negative mass, depending on the sign of  $h$  at a given location. The potential energy of a mass  $m$  at a given point on the surface of the distorted earth is the sum of the potentials due to (1) gravity from the sphere, (2) the centrifugal force, and (3) gravity from the shell. From Eq. (10.68), the standard  $mgh$  contributions from (1) at a pole and the equator are essentially  $mg\beta(-2)$  and  $mg\beta(1)$ , respectively. The contributions from (2) at a pole and the equator are 0 and  $-m\omega^2 R^2/2$ , respectively. The contributions from (3) are trickier. We need to calculate the integral  $-\int Gm dM/\ell$ , where  $dM$  runs over the shell, and  $\ell$  is the distance from  $m$  to each  $dM$ . The mass of a small element in the shell is

$$dM = \rho dV = \rho h dA = \rho \beta (3 \sin^2 \theta - 2) (R d\theta) (R \sin \theta d\phi). \quad (10.69)$$

The distance from the north pole to a point with polar angle  $\theta$  equals  $\ell = 2R \sin(\theta/2) = R\sqrt{2(1 - \cos \theta)}$ . Using the Pythagorean theorem, the distance from a point on the equator, say  $(R, 0, 0)$ , to a point with polar angle  $\theta$  whose general form is  $(R \sin \theta \cos \phi, R \sin \theta \sin \phi, R \cos \theta)$  equals  $\ell = R\sqrt{2(1 - \sin \theta \cos \phi)}$ . Demanding that the total potential at the north pole be equal to the total potential at the equator then gives

$$\begin{aligned} mg\beta(-2) + 0 - \int_0^\pi \int_0^{2\pi} \frac{Gm \cdot \rho \beta (3 \sin^2 \theta - 2) (R d\theta) (R \sin \theta d\phi)}{R\sqrt{2(1 - \cos \theta)}} \\ = mg\beta(1) - \frac{m\omega^2 R^2}{2} - \int_0^\pi \int_0^{2\pi} \frac{Gm \cdot \rho \beta (3 \sin^2 \theta - 2) (R d\theta) (R \sin \theta d\phi)}{R\sqrt{2(1 - \sin \theta \cos \phi)}}. \end{aligned} \quad (10.70)$$

Letting  $\beta \equiv fR(R\omega^2/6g)$ , and using

$$g \equiv \frac{GM_E}{R^2} = \frac{G(4\pi R^3 \rho/3)}{R^2} \implies G\rho = \frac{3g}{4\pi R}, \quad (10.71)$$

we can rewrite Eq. (10.70) as

$$\begin{aligned} \frac{m\omega^2 R^2}{2} = 3mgfR \left( \frac{R\omega^2}{6g} \right) \\ - \int_0^\pi \int_0^{2\pi} \left( \frac{3g}{4\pi R} \right) mfR \left( \frac{R\omega^2}{6g} \right) (3 \sin^2 \theta - 2) (R d\theta) (R \sin \theta d\phi) \\ \times \left( \frac{1}{R\sqrt{2(1 - \sin \theta \cos \phi)}} - \frac{1}{R\sqrt{2(1 - \cos \theta)}} \right). \end{aligned} \quad (10.72)$$

After canceling common factors, we end up with

$$\begin{aligned} 1 = f - f \int_0^\pi \int_0^{2\pi} \frac{(3 \sin^2 \theta - 2) \sin \theta}{4\sqrt{2}\pi} \\ \times \left( \frac{1}{\sqrt{1 - \sin \theta \cos \phi}} - \frac{1}{\sqrt{1 - \cos \theta}} \right) d\phi d\theta. \end{aligned} \quad (10.73)$$

Evaluating this integral numerically gives essentially 0.6, which then yields  $f = 5/2$ , as desired.

REMARK: The  $f = 5/2$  result leads to a difference in polar and equatorial radii of  $\Delta h = (5/2)(R^2\omega^2/6g)(3) \approx 28\,000\text{ m} = 28\text{ km}$ . The fact that this is larger than the correct value of 21.5 km makes sense for the following reason. If all of the earth's mass were concentrated at the center, then the thin distortion shell at the surface would have no effect on the potential, because it would be massless. So the naive calculation in part (a) would in fact be correct, and  $\Delta h$  would be about 11 km. The actual density of the earth decreases with radius, which means that the density lies somewhere between the case of a concentrated center and the case of uniform density. The actual value of  $\Delta h$  should therefore lie somewhere between the corresponding  $\Delta h$  values of 11 km and 28 km. And 21.5 km indeed does. ♣

### 10.13. Southward deflection

The Coriolis force is  $2m\omega v \sin \theta$  eastward. But  $v \approx gt$ , so the eastward acceleration is  $2\omega gt \sin \theta$ . Integrating this gives an eastward speed of  $\omega gt^2 \sin \theta$ . This eastward speed produces a Coriolis force in the direction away from the earth's axis, so the acceleration in this direction is  $2\omega(\omega gt^2 \sin \theta)$ . The component of this acceleration along the surface of the earth (that is, in the southward direction) is  $2\omega^2 gt^2 \sin \theta \cos \theta$ . Integrating this gives a southward speed of  $(2/3)\omega^2 gt^3 \sin \theta \cos \theta$ . Integrating again gives a southward deflection of  $(1/6)\omega^2 gt^4 \sin \theta \cos \theta$ . But  $gt^2/2 \approx h \Rightarrow t^2 \approx 2h/g$ . So the southward deflection due to the Coriolis force is  $(2/3)(\omega^2 h^2/g) \sin \theta \cos \theta$ .

Now for the rest of the problem. To be precise, we'll define  $\theta$  to be the polar angle at the point  $P$  on the radial line to the dropping point. However, we would still obtain the same answer if we defined  $\theta$  to be the polar angle at the location of the plumb bob, because the difference between these two angles is of order  $\omega^2$  (since it is due to the centrifugal contribution to the effective gravity). And this difference yields a negligible effect of order  $\omega^4$  in the  $4(\omega^2 h^2/g) \sin \theta \cos \theta$  result, because this already contains a factor of  $\omega^2$ .

![Diagram illustrating the southward deflection of a falling object. A radial line from the north pole to a dropping point P has length R. A plumb bob line is shown at point B, which is a distance d from P. The angle between the radial line and the plumb bob line at P is phi. The angle between the radial line and the effective gravity vector g_eff at P is beta. The angle between the radial line and the effective gravity vector g_eff at B is also beta. The angle between the radial line and the vertical at the north pole is theta. The distance from the north pole to P is R, and the distance from the north pole to B is R + h.](1dcb3f747f8f838a9a28a3af3726c3b9_img.jpg)

Diagram illustrating the southward deflection of a falling object. A radial line from the north pole to a dropping point P has length R. A plumb bob line is shown at point B, which is a distance d from P. The angle between the radial line and the plumb bob line at P is phi. The angle between the radial line and the effective gravity vector g\_eff at P is beta. The angle between the radial line and the effective gravity vector g\_eff at B is also beta. The angle between the radial line and the vertical at the north pole is theta. The distance from the north pole to P is R, and the distance from the north pole to B is R + h.

Fig. 10.32

- (a) At point  $P$ , the magnitude of  $\mathbf{F}_{\text{cent}}$  is  $m\omega^2 R \sin \theta$ , so (using Fig. 10.22 in the solution to Problem 10.3) the component of  $\mathbf{F}_{\text{cent}}$  perpendicular to  $m\mathbf{g}$  is  $F_{\text{cent}}^{\perp} = m\omega^2 R \sin \theta \cos \theta$ . The angle that  $\mathbf{g}_{\text{eff}}$  makes with the radial at  $P$  is therefore essentially equal to  $F_{\text{cent}}^{\perp}/mg = (\omega^2 R/g) \sin \theta \cos \theta$ . However, the direction of the plumb bob line is determined by the  $\mathbf{g}_{\text{eff}}$  vector at the location of the plumb bob (call this point  $B$ ), and not at  $P$ ; see Fig. 10.32. Now, the angle we just found between  $\mathbf{g}_{\text{eff}}$  and  $\mathbf{g}$  (that is, the radial) at  $P$  is the same as the angle between  $\mathbf{g}_{\text{eff}}$  and  $\mathbf{g}$  at  $B$  (at least to order  $\omega^2$ , by the argument in the preceding paragraph). Therefore, since the  $\mathbf{g}$  vector at  $B$  is tilted at the angle  $\beta$  (shown) relative to the  $\mathbf{g}$  vector at  $P$ , we see that  $\mathbf{g}_{\text{eff}}$  at  $B$  makes an angle of  $\phi = (\omega^2 R/g) \sin \theta \cos \theta - \beta$  relative to the radial at  $P$ . The angle  $\beta$  is given by  $d/R$ , where  $d$  is the distance between  $P$  and  $B$ . So in the thin triangle  $DPB$ , the relation  $d \approx h\phi$  gives

$$\begin{aligned} d &\approx h \left( (\omega^2 R/g) \sin \theta \cos \theta - d/R \right) \\ \Rightarrow d &\approx \frac{h(\omega^2 R/g) \sin \theta \cos \theta}{1 + h/R} \\ &\approx \frac{\omega^2 Rh}{g} \sin \theta \cos \theta \left( 1 - \frac{h}{R} \right). \end{aligned} \quad (10.74)$$

- (b) The gravitational acceleration at height  $y$  above the earth is

$$\frac{GM}{(R+y)^2} \approx \frac{GM}{R^2(1+2y/R)} \approx \frac{GM}{R^2} \left( 1 - \frac{2y}{R} \right) \equiv g \left( 1 - \frac{2y}{R} \right). \quad (10.75)$$

(There are also corrections due to the centrifugal and Coriolis forces, but these are negligible; see Exercise 10.21.) So we have  $\ddot{y} = -g(1 - 2y/R)$ . Writing  $\ddot{y}$  as  $v dv/dy$ , and separating variables and integrating, gives

$$\begin{aligned} \int_0^v v dv &= - \int_h^y g \left(1 - \frac{2y}{R}\right) dy \\ \implies v &= -\sqrt{2g(h-y) - (2g/R)(h^2 - y^2)} \\ &\approx -\sqrt{2g(h-y)} \left(1 - \frac{h+y}{2R}\right). \end{aligned} \quad (10.76)$$

Writing  $v \equiv dy/dt$ , and separating variables and integrating, gives

$$\int_0^T dt \approx - \int_h^0 \frac{dy}{\sqrt{2g(h-y)} \left(1 - \frac{h+y}{2R}\right)} \approx - \int_h^0 \frac{1 + \frac{h+y}{2R}}{\sqrt{2g(h-y)}} dy. \quad (10.77)$$

You can show that the “1” here gives the leading-order time of  $\sqrt{2h/g}$ . The additional time comes from the other term, which yields (with  $z \equiv y/h$ )

$$\Delta t = - \frac{1}{2R\sqrt{2g}} \int_h^0 \frac{h+y}{\sqrt{h-y}} dy = - \frac{h\sqrt{h}}{2R\sqrt{2g}} \int_1^0 \frac{1+z}{\sqrt{1-z}} dz. \quad (10.78)$$

Looking up this integral gives

$$\Delta t = \frac{h\sqrt{h}}{2R\sqrt{2g}} \cdot \frac{2}{3} (5+z)\sqrt{1-z} \Big|_1^0 = \sqrt{\frac{2h}{g}} \left(\frac{5h}{6R}\right). \quad (10.79)$$

The total time is therefore  $\sqrt{2h/g}(1 + 5h/6R)$ , as we wanted to show.

- (c) At height  $y$ , the distance from the center of the earth is  $R + y$ . So from the  $F_{\text{cent}}^\perp$  reasoning in part (a), the acceleration in the southward direction is  $\ddot{z} = \omega^2(R + y) \sin \theta \cos \theta$ .
- (d) If the ball is a distance  $z$  away from the radial line through  $P$  (call this line  $L$ ), then the radial line to the ball makes an angle of approximately  $z/R$  with respect to  $L$ . The component of the gravitational force on the ball perpendicular to  $L$  is therefore  $\ddot{z} = -g(z/R)$ , where the minus sign signifies toward  $L$  (that is, northward).
- (e) Parts (c) and (d) give

$$\ddot{z} = \omega^2(R + y) \sin \theta \cos \theta - g(z/R). \quad (10.80)$$

The  $R$  term here dominates, so to leading order we have  $\ddot{z} = \omega^2 R \sin \theta \cos \theta \implies z \approx (\omega^2 R \sin \theta \cos \theta) t^2 / 2$ . Also, to leading order,  $y \approx h - gt^2/2$ . Plugging these values of  $z$  and  $y$  into Eq. (10.80) gives

$$\begin{aligned} \ddot{z} &= \omega^2 \sin \theta \cos \theta \left( R + \left( h - \frac{gt^2}{2} \right) - \frac{gt^2}{2} \right) \\ \implies z &= \omega^2 \sin \theta \cos \theta \left( \frac{Rt^2}{2} + \left( \frac{ht^2}{2} - \frac{gt^4}{24} \right) - \frac{gt^4}{24} \right). \end{aligned} \quad (10.81)$$

Plugging in the total time  $t = \sqrt{2h/g}(1 + 5h/6R)$  gives, to leading order, a total  $z$  value equal to

$$\begin{aligned} z &= \omega^2 \sin \theta \cos \theta \left( \frac{R}{2} \cdot \frac{2h}{g} \left( 1 + \frac{5h}{3R} \right) \right. \\ &\quad \left. + \left( \frac{h}{2} \cdot \frac{2h}{g} - \frac{g}{24} \cdot \frac{4h^2}{g^2} \right) - \frac{g}{24} \cdot \frac{4h^2}{g^2} \right) \\ &= \frac{\omega^2 Rh}{g} \sin \theta \cos \theta \left( 1 + \frac{h}{R} \left( \frac{5}{3} + \frac{5}{6} - \frac{1}{6} \right) \right) \\ &= \frac{\omega^2 Rh}{g} \sin \theta \cos \theta \left( 1 + \frac{7h}{3R} \right). \end{aligned} \quad (10.82)$$

When we subtract off the plumb bob's position in Eq. (10.74), the leading terms proportional to  $R$  cancel. Adding on the Coriolis result then gives a total southward deflection (relative to the plumb bob) equal to

$$\frac{\omega^2 h^2}{g} \sin \theta \cos \theta \left( \frac{7}{3} - (-1) + \frac{2}{3} \right) = \frac{4\omega^2 h^2}{g} \sin \theta \cos \theta, \quad (10.83)$$

as we wanted to show. From the third line in Eq. (10.82), we see that the  $7/3$  result can be broken up into a  $5/3$  that comes from the extra time it takes the ball to hit the ground due to the decrease in the gravitational force with altitude, a  $5/6$  that comes from the dependence of the centrifugal force on height, and a  $-1/6$  that comes from the slightly northward component of the gravitational force.

![Diagram of a sphere representing Earth. A dashed circle represents a latitude circle. A solid circle represents a great circle. A point P is marked on the sphere, and a dashed line shows the path of a ball from P to point A on the great circle. An arrow labeled omega indicates rotation.](0e9a07f0dcc73c6c4ae238eee8b7381c_img.jpg)

Diagram of a sphere representing Earth. A dashed circle represents a latitude circle. A solid circle represents a great circle. A point P is marked on the sphere, and a dashed line shows the path of a ball from P to point A on the great circle. An arrow labeled omega indicates rotation.

Fig. 10.33

REMARK: We can also solve this problem by working in an inertial frame. In this frame, the ball has an initial sideways motion due to the rotation of the earth, and this motion causes the ball to travel in the path shown in Fig. 10.33. Because only gravity acts on the ball, its path lies in the plane determined by its initial velocity and radius. The intersection of this plane with the surface of the earth is the great circle shown, and the ball hits the earth at a point  $A$  on this great circle.

The distance  $\ell$  that the ball travels along the great circle is essentially equal to the distance it travels in the eastward direction (that is, along the latitude circle). This eastward distance equals the distance that point  $P$  rotates due to the spinning of the earth, plus the extra Coriolis eastward deflection  $d_{\text{cor}}$  that we found in Eq. (10.18). (In the spirit of working in an inertial frame, let's assume that we found this deflection by the method given in the remark after Eq. (10.18).) So we have  $\ell \approx R \sin \theta \omega t + d_{\text{cor}}$ . The task now is to determine the distance between  $A$  and the latitude circle through  $P$ . This distance should equal the result in Eq. (10.82) plus the southward Coriolis deflection. (We'll then subtract off the distance from the pendulum bob to  $P$ , given in Eq. (10.74), as we did above.)<sup>21</sup> This task is equivalent to answering the question: If a circle of radius  $r = R \sin \theta$  (the latitude circle) sits on a plane (the plane of the great circle) and is inclined at an angle  $\theta$  with respect to the normal to the plane, how far above the plane is a point on the circle with an "x" coordinate equal to  $\ell$  (with  $\ell \ll r$ )? Using a Taylor series approximation for the length  $\sqrt{r^2 - \ell^2}$  in the right triangle in Fig. 10.34, we see that if the circle is perpendicular to the plane, then the desired distance is  $\ell^2/2r$ . Tilting the circle by an angle  $\theta$  simply brings in a factor of  $\cos \theta$ , so the distance is  $(\ell^2/2r) \cos \theta = (\ell^2/2R \sin \theta) \cos \theta$ .

![Diagram of a circle representing a latitude circle sitting on a horizontal line representing the plane of a great circle. A right triangle is formed with the center of the circle, a point on the circle at distance l from the plane, and the projection of that point onto the plane. The hypotenuse is the radius r, and the base is sqrt(r^2 - l^2). The distance from the projection to the point on the plane is labeled l^2/2r.](d7dccd0edee596de010af45648968669_img.jpg)

Diagram of a circle representing a latitude circle sitting on a horizontal line representing the plane of a great circle. A right triangle is formed with the center of the circle, a point on the circle at distance l from the plane, and the projection of that point onto the plane. The hypotenuse is the radius r, and the base is sqrt(r^2 - l^2). The distance from the projection to the point on the plane is labeled l^2/2r.

Fig. 10.34

<sup>21</sup> If you want, you can derive the distance from the pendulum bob to  $P$  by working in the inertial frame, to maintain the spirit of this solution. The  $m\omega^2 R$  type term we found in part (a) above simply shows up through the centripetal acceleration instead of through the centrifugal force.

Using the time of flight obtained above in part (b), and also the  $d_{\text{cor}}$  from Eq. (10.18), we obtain a southward deflection relative to  $P$  equal to (dropping higher order terms)

$$\begin{aligned}
 z &= \frac{\ell^2 \cos \theta}{2R \sin \theta} \\
 &= \frac{(R \sin \theta \omega t + d_{\text{cor}})^2 \cos \theta}{2R \sin \theta} \\
 &\approx R\omega^2 \sin \theta \cos \theta t^2/2 + \omega d_{\text{cor}} \cos \theta t \\
 &\approx \frac{R\omega^2 \sin \theta \cos \theta}{2} \cdot \frac{2h}{g} \left(1 + \frac{5h}{3R}\right) + \omega \left(\frac{2\omega h \sin \theta}{3} \sqrt{\frac{2h}{g}}\right) \cos \theta \sqrt{\frac{2h}{g}} \\
 &\approx \frac{\omega^2 Rh}{g} \sin \theta \cos \theta \left(1 + \frac{h}{R} \left(\frac{5}{3} + \frac{4}{3}\right)\right). \quad (10.84)
 \end{aligned}$$

As expected, the factor of 9/3 here equals the 7/3 from Eq. (10.82) plus the 2/3 from the southward Coriolis deflection. Subtracting off the position of the plumb bob given in Eq. (10.74) yields the desired southward deflection from the plumb bob,  $(4\omega^2 h^2/g) \sin \theta \cos \theta$ . ♣

### 10.14. Bead on a hoop

- (a) The gravitational force on the bead is essentially  $GMm/(R-r)^2$ , directed essentially to the right. But to leading order, we can neglect the  $r$  here. If the bead is at an angle  $\theta$  up from the horizontal, then we need to multiply this rightward force by  $\sin \theta \approx \theta$  to obtain the force component along the hoop. Therefore, the  $F = ma$  equation along the hoop is

$$-\frac{GMm\theta}{R^2} = mr\ddot{\theta} \implies \omega = \sqrt{\frac{GM}{rR^2}}. \quad (10.85)$$

This is just the usual  $\sqrt{g/r}$  result for a pendulum, in disguised form.

- (b) From Eq. (10.35), the tidal force is  $(GMm/R^3)(2x, -y)$ . The force along the hoop comes not only from the horizontal component of this (when multiplied by negative  $\sin \theta$ ), but also from the vertical component (when multiplied by  $\cos \theta$ ). So the force along the hoop is (using  $x = r \cos \theta$  and  $y = r \sin \theta$ )

$$\frac{GMm}{R^3} (2(r \cos \theta)(-\sin \theta) + (-r \sin \theta) \cos \theta) = -\frac{GMm}{R^3} (3r \sin \theta \cos \theta). \quad (10.86)$$

Using  $\sin \theta \approx \theta$  and  $\cos \theta \approx 1$ , the  $F = ma$  equation along the hoop is

$$-\frac{3GMmr\theta}{R^3} = mr\ddot{\theta} \implies \omega = \sqrt{\frac{3GM}{R^3}}. \quad (10.87)$$

Note that this is independent of  $r$ . It is smaller than the result in part (a) by a factor  $\sqrt{3r/R}$ .

#### 10.15. Precession of the equinoxes

We'll calculate the effect due to the sun, and then multiply by 3 to obtain the total effect, because the moon's effect is twice the sun's. Consider the case where the earth is in the summer/winter orientation. From Eq. (10.35), the tidal force on the effective point mass  $m$  is  $(GM_{\text{sun}}/R^3)(2x, -y)$ . Both components are relevant here, so the tidal forces on the two masses are shown in Fig. 10.35, where  $r$  is the radius of the earth, and  $k \equiv GM_{\text{sun}}/R^3$ . The torque due to these forces has magnitude

$$2(2kr \cos \beta)(r \sin \beta) + kr \sin \beta(r \cos \beta) = 6kr^2 \sin \beta \cos \beta, \quad (10.88)$$

and it is directed into the page. For the case where the earth is in the spring/fall orientation (that is, where the sun is positioned where your nose is, as you look

![Diagram illustrating the tidal forces on a mass m due to the sun. The mass m is at a distance r from the center of the earth. The sun is in the direction to the right. The tidal force components are shown as vectors: a horizontal component of 2kr cos beta pointing to the right, and a vertical component of kr sin beta pointing upwards. The angle beta is measured from the horizontal line connecting the mass to the sun. The equator is indicated by a dashed line.](463e6705f9f72e74acc9c48d45bf8715_img.jpg)

Diagram illustrating the tidal forces on a mass m due to the sun. The mass m is at a distance r from the center of the earth. The sun is in the direction to the right. The tidal force components are shown as vectors: a horizontal component of 2kr cos beta pointing to the right, and a vertical component of kr sin beta pointing upwards. The angle beta is measured from the horizontal line connecting the mass to the sun. The equator is indicated by a dashed line.

Fig. 10.35

at Fig. 10.35), there is no torque, because the longitudinal component of the tidal force is zero, and the transverse component is radial. Each of the summer/winter and spring/fall cases is applicable for half the time (by assumption 6), so the time-averaged torque is

$$\bar{\tau}_{\text{sun}} = \frac{1}{2}(6kr^2 \sin \beta \cos \beta + 0) = 3kr^2 \sin \beta \cos \beta. \quad (10.89)$$

Adding on the effect of the moon gives an average total torque of

$$\bar{\tau}_{\text{total}} = 9kr^2 \sin \beta \cos \beta = \frac{9GM_{\text{S}}mr^2 \sin \beta \cos \beta}{R^3}. \quad (10.90)$$

The angular momentum of the earth is  $I_3\omega_3$ . The “horizontal” component of this is  $I_3\omega_3 \sin \beta$ , so  $|d\mathbf{L}/dt| = \Omega I_3\omega_3 \sin \beta$ , where  $\Omega$  is the frequency of precession. Equating this with the torque gives

$$\Omega = \frac{9GM_{\text{S}}mr^2 \cos \beta}{R^3 I_3\omega_3}. \quad (10.91)$$

But from assumptions 3, 4, and 5, we have  $m = \rho r^2 h$ , where  $\rho$  is the average density of the earth. And  $I_3 = (2/5)(4\pi r^3 \rho/3)r^2 = (8\pi/15)\rho r^5$ , so<sup>22</sup>

$$\Omega = \frac{9GM_{\text{S}}(\rho r^2 h)r^2 \cos \beta}{R^3(8\pi \rho r^5/15)\omega_3} = \frac{135 GM_{\text{S}}h \cos \beta}{8\pi r R^3 \omega_3}. \quad (10.92)$$

Plugging in the numerical values gives

$$\begin{aligned} \Omega &= \frac{135(6.67 \cdot 10^{-11} \text{ m}^3/\text{kg s}^2)(2 \cdot 10^{30} \text{ kg})(21 \cdot 10^3 \text{ m}) \cos 23^\circ}{8\pi(6.4 \cdot 10^6 \text{ m})(1.5 \cdot 10^{11} \text{ m})^3(7.3 \cdot 10^{-5} \text{ s}^{-1})} \approx 8.8 \cdot 10^{-12} \text{ s}^{-1}. \\ \Rightarrow T &= \frac{2\pi}{\Omega} \approx \frac{2\pi}{8.8 \cdot 10^{-12} \text{ s}^{-1}} \approx 7.1 \cdot 10^{11} \text{ s} \approx 23\,000 \text{ years}. \end{aligned} \quad (10.93)$$

This answer actually came out a little too good. We had no right to expect that it would come out so close to 26 000 years, considering the various approximations we made. But we *did* have a right to expect it to come out within a factor of, say, 5 or so, because our approximations could be off by only so much. At any rate, Eq. (10.92) does at least give the correct dependence on the various parameters. Note that Eq. (10.40) says that  $h \propto r^2 \omega_3^2/g$ . Using this along with  $g = G(4\pi r^3 \rho_{\text{E}}/3)/r^2$  in Eq. (10.92), and ignoring all numerical factors, gives  $\Omega \propto \omega_3 M_{\text{S}}/(\rho_{\text{E}} R^3) \propto \omega_3 (M_{\text{S}}/M_{\text{c}})$ , where  $M_{\text{c}}$  is the mass of a colossal object whose density equals the earth’s and whose radius equals the earth–sun distance. (This relation also holds if we consider the moon instead of the sun.)

**REMARK:** Interestingly, the time of  $T = 26\,000$  years is large enough to allow us to treat the axis of rotation as essentially constant, but small enough to have a noticeable effect over the ages. The star we see in the northern direction nowadays is a different northern star from the one people saw, say, 2000 years ago. And the signs of the zodiac that we see now are shifted by approximately one place compared with what they were 2000 years ago. The “precession of the equinoxes” name comes from the fact that if you consider, for example, a distant galaxy that the sun blocks out when the earth is in the spring equinox position now, and if you consider the analogous galaxy 13 000 years ago, then the two galaxies are in opposite directions in the universe, relative to the earth. ♣

<sup>22</sup> The mass  $m$  is actually smaller than this, because the earth’s crust is less dense than its interior. But  $I_3$  is smaller than this too, because the earth’s core is denser than the mantle. These effects somewhat cancel each other, because  $m$  appears in the numerator and  $I_3$  appears in the denominator. But we’re just doing things roughly anyway.