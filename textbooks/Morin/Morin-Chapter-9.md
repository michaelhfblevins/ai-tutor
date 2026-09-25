# Chapter 9 Angular momentum, Part II (General $\hat{\mathbf{L}}$ )

In Chapter 8, we discussed situations where the direction of the vector  $\mathbf{L}$  remained constant, and only its magnitude changed. In this chapter, we will look at more general situations where the direction of  $\mathbf{L}$  is allowed to change. The vector nature of  $\mathbf{L}$  will prove to be vital here, and we will arrive at all sorts of strange results for spinning tops and such things. This chapter is rather long, alas, but the general outline is that the first three sections cover general theory, then Section 9.4 introduces some actual physical setups, and then Section 9.6 begins the discussion of tops.

### 9.1 Preliminaries concerning rotations

#### 9.1.1 The form of general motion

Before getting started, we should make sure we're all on the same page concerning a few important things about rotations. Because rotations generally involve three dimensions, they can often be hard to visualize. A rough drawing on a piece of paper might not do the trick. For this reason, this chapter is one of the more difficult ones in this book. But to ease into it, the next few pages consist of some definitions and helpful theorems. This first theorem describes the general form of any motion. You might consider it obvious, but it's a little tricky to prove.

**Theorem 9.1** *(Chasles' theorem) Consider a rigid body undergoing arbitrary motion. Pick any point  $P$  in the body. Then at any instant (see Fig. 9.1), the motion of the body can be written as the sum of the translational motion of  $P$ , plus a rotation around some axis (which may change with time) through  $P$ .<sup>1</sup>*

**Proof:** The motion of the body can be written as the sum of the translational motion of  $P$ , plus some other motion relative to  $P$  (this is true because relative coordinates are additive quantities). We must show that this latter motion is a rotation. This seems quite plausible, and it holds because the body is rigid; that is,

<sup>1</sup> In other words, a person at rest with respect to a frame whose origin is  $P$ , and whose axes are parallel to the fixed-frame axes, sees the body undergoing a rotation around some axis through  $P$ .

![Diagram illustrating Chasles' theorem. A rigid body is shown in a 3D coordinate system with axes x, y, and z. A point P is marked on the body. A vector V is shown originating from P, representing the translational motion of P. A dashed line passes through P, representing the axis of rotation. A curved arrow around this axis is labeled ω, representing the angular velocity of the body's rotation around P.](0ac966635b7d7c8172ff34eaaedfed7d_img.jpg)

Diagram illustrating Chasles' theorem. A rigid body is shown in a 3D coordinate system with axes x, y, and z. A point P is marked on the body. A vector V is shown originating from P, representing the translational motion of P. A dashed line passes through P, representing the axis of rotation. A curved arrow around this axis is labeled ω, representing the angular velocity of the body's rotation around P.

Fig. 9.1

all points keep the same distances relative to each other. If the body weren't rigid, then this theorem wouldn't be true.

To be rigorous, consider a spherical shell fixed in the body, centered at  $P$ . The motion of the body is completely determined by the motion of the points on this sphere, so we need only examine what happens to the sphere. Because distances are preserved in the rigid body, the points on the sphere must always remain the same radial distance from  $P$ . And because we are looking at motion relative to  $P$ , we have therefore reduced the problem to the following: In what manner can a rigid sphere transform into itself? We claim that any such transformation has the property that there exist two points that end up where they started.<sup>2</sup> These two points must then be diametrically opposite points (assuming that the whole sphere doesn't end up back where it started, in which case every point ends up where it started), because distances are preserved; given one point that ends up where it started, the diametrically opposite point must also end up where it started, to maintain the distance of a diameter.

If this claim is true, then we are done, because for an infinitesimal transformation, a given point moves in only one direction, because there is no time to do any turning. So a point that ends up where it started must have remained fixed for the whole (infinitesimal) time. Therefore, all the points on the diameter joining the two fixed points must also have remained fixed the whole time, because distances are preserved. So we are left with a rotation around this axis.

This “two points ending up where they started” claim is quite believable, but nevertheless tricky to prove. Claims with these properties are always fun to think about, so I've left this one as a problem (Problem 9.2). Try to solve it on your own. ■

We will invoke this theorem repeatedly in this chapter (often without bothering to say so). Note that we are assuming that  $P$  is a point in the body, because we used the fact that  $P$  keeps the same distances from other points in the body.

![Diagram of a rigid body with a point P and two rotation axes.](b95f9d5491540e0383956e96aaa0bcad_img.jpg)

The diagram shows an irregularly shaped rigid body. A point  $P$  is located inside the body. A solid line passes through  $P$  and is labeled "stick". A curved arrow around this stick indicates rotation with angular velocity "old  $\omega$ ". A dashed line also passes through  $P$  at an angle to the stick. A curved arrow around this dashed line indicates rotation with angular velocity "new  $\omega$ ".

Diagram of a rigid body with a point P and two rotation axes.

Fig. 9.2

REMARK: A situation where this theorem isn't so obvious is the following (this setup contains only rotation, with no translation of the point  $P$ ). Consider an object rotating around a fixed axis, the stick shown in Fig. 9.2. But now imagine grabbing the stick and rotating it around some other axis (the dotted line shown). It isn't immediately obvious that the resulting motion is (instantaneously) a rotation around some new axis through the point  $P$  (which remains fixed). But indeed it is. We'll be quantitative about this in the “Rotating sphere” example later in this section. ♣

#### 9.1.2 The angular velocity vector

It is extremely useful to introduce the angular velocity vector,  $\boldsymbol{\omega}$ , which is defined as the vector that points along the axis of rotation, and whose magnitude equals

<sup>2</sup> This claim is actually true for *any* transformation of a rigid sphere into itself, but for the present purposes we are concerned only with infinitesimal transformations, because we are looking only at what happens at a given instant in time.

the angular speed. The choice of the two possible directions along the axis is given by the right-hand rule: if you curl your right-hand fingers in the direction of the spin, then your thumb points in the direction of  $\boldsymbol{\omega}$ . For example, a spinning record has  $\boldsymbol{\omega}$  perpendicular to the record, through the center (as shown in Fig. 9.3),<sup>3</sup> with its magnitude equal to the angular speed,  $\omega$ . The points on the axis of rotation are the ones that (instantaneously) do not move. Of course, the direction of  $\boldsymbol{\omega}$  may change over time, so the points that were formerly on the axis may now be moving.

![Diagram of a spinning record with an axis of rotation and angular velocity vector.](bb5e4bf4a5eeedff9a7db204a4488e86_img.jpg)

A diagram showing a horizontal elliptical disk representing a spinning record. A vertical arrow labeled

 $\boldsymbol{\omega}$ 

passes through the center of the disk, representing the axis of rotation. A curved arrow on the right edge of the disk, also labeled

 $\boldsymbol{\omega}$ 

, indicates the direction of rotation.

Diagram of a spinning record with an axis of rotation and angular velocity vector.

Fig. 9.3

##### REMARKS:

1. If you want, you can break the mold and use the left-hand rule to determine  $\boldsymbol{\omega}$ , as long as you use it consistently. The direction of  $\boldsymbol{\omega}$  will be the opposite, but that doesn't matter, because  $\boldsymbol{\omega}$  isn't really physical. Any physical result (for example, the velocity of a particle, given below in Theorem 9.2) will come out the same, independent of which hand you (consistently) use.

When studying vectors in school,  
 You'll use your right hand as a tool.  
 But look in a mirror,  
 And then you'll see clearer,  
 It's just like the left-handed rule.

2. The fact that we can specify a rotation by specifying a vector  $\boldsymbol{\omega}$  is a peculiarity to three dimensions. If we lived in one dimension, then there would be no such thing as a rotation. If we lived in two dimensions, then all rotations would take place in that plane, so we could label a rotation by simply giving its speed,  $\omega$ . In three dimensions, rotations take place in  $\binom{3}{2} = 3$  independent planes. And we choose to label these, for convenience, by the directions orthogonal to these planes, and by the angular speed in each plane. If we lived in four dimensions, then rotations could take place in  $\binom{4}{2} = 6$  planes, so we would have to label a rotation by giving 6 planes and 6 angular speeds. Note that a vector, which has four components in four dimensions, would not do the trick. ♣

In addition to specifying the points that are instantaneously motionless,  $\boldsymbol{\omega}$  also easily produces the velocity of any point in the rotating object. Consider the situation where the axis of rotation passes through the origin, which we'll generally assume to be the case in this chapter, unless otherwise stated. Then we have the following theorem.

**Theorem 9.2** *Given an object rotating with angular velocity  $\boldsymbol{\omega}$ , the velocity of a point at position  $\mathbf{r}$  is given by*

$$\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}. \quad (9.1)$$

**Proof:** Drop a perpendicular from the point in question (call it  $P$ ) to the axis  $\boldsymbol{\omega}$ . Let  $Q$  be the foot of the perpendicular, and let  $\mathbf{r}'$  be the vector from  $Q$  to  $P$

<sup>3</sup> It's actually meaningless to say that  $\boldsymbol{\omega}$  passes through the center of the record, because you can draw the vector anywhere, and it's still the same vector, as long as it has the correct magnitude and direction. Nevertheless, it's customary to draw  $\boldsymbol{\omega}$  along the axis of rotation and to say things like, "An object rotates around  $\boldsymbol{\omega}$  . . ."

![Diagram illustrating the cross product of vectors ω and r. A vector ω points upwards and to the right. A vector r points from the origin to a point P. A perpendicular vector r' is shown from the origin to the line through P parallel to ω. The angle between ω and r is θ. A right angle is marked at the intersection of r' and the line through P.](c5357d9f76f2146b7e50e457b5ddd242_img.jpg)

Diagram illustrating the cross product of vectors ω and r. A vector ω points upwards and to the right. A vector r points from the origin to a point P. A perpendicular vector r' is shown from the origin to the line through P parallel to ω. The angle between ω and r is θ. A right angle is marked at the intersection of r' and the line through P.

Fig. 9.4

(see Fig. 9.4). From the properties of the cross product (see Appendix B),  $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$  is orthogonal to  $\boldsymbol{\omega}$ ,  $\mathbf{r}$ , and also  $\mathbf{r}'$  because  $\mathbf{r}'$  is a linear combination of  $\boldsymbol{\omega}$  and  $\mathbf{r}$ . Therefore, the direction of  $\mathbf{v}$  is correct; it is always orthogonal to  $\boldsymbol{\omega}$  and  $\mathbf{r}'$ , so it describes circular motion around the axis  $\boldsymbol{\omega}$ . Also, by the right-hand rule in the cross product (or the left-hand rule, if you had chosen to be different and defined  $\boldsymbol{\omega}$  that way),  $\mathbf{v}$  has the proper orientation around  $\boldsymbol{\omega}$ , namely into the page at the instant shown. And since

$$|\mathbf{v}| = |\boldsymbol{\omega}||\mathbf{r}| \sin \theta = \omega r', \quad (9.2)$$

we see that  $\mathbf{v}$  has the correct magnitude, because  $\omega r'$  is the speed of the circular motion around  $\boldsymbol{\omega}$ . So  $\mathbf{v}$  is indeed the correct velocity vector. (If we have the special case where  $P$  lies along  $\boldsymbol{\omega}$ , then  $\mathbf{r}$  is parallel to  $\boldsymbol{\omega}$ , so the cross product gives a zero result for  $\mathbf{v}$ , as it should.) ■

We'll make good use of Eq. (9.1) and apply it repeatedly throughout this chapter. Even if it's hard to visualize what's going on in a given rotation, all you have to do to find the speed of any point is calculate the cross product  $\boldsymbol{\omega} \times \mathbf{r}$ . Conversely, if the speed of every point in a body is given by  $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$ , then the body must be undergoing a rotation with angular velocity  $\boldsymbol{\omega}$ , because all points on the axis  $\boldsymbol{\omega}$  are motionless, and all other points move with the proper speed for this rotation.

A very nice thing about angular velocities is that they simply add. Stated more precisely:

**Theorem 9.3** *Let coordinate systems  $S_1$ ,  $S_2$ , and  $S_3$  have a common origin. Let  $S_1$  rotate with angular velocity  $\boldsymbol{\omega}_{1,2}$  with respect to  $S_2$ , and let  $S_2$  rotate with angular velocity  $\boldsymbol{\omega}_{2,3}$  with respect to  $S_3$ . Then  $S_1$  rotates (instantaneously) with angular velocity*

$$\boldsymbol{\omega}_{1,3} = \boldsymbol{\omega}_{1,2} + \boldsymbol{\omega}_{2,3} \quad (9.3)$$

*with respect to  $S_3$ .*

**Proof:** If  $\boldsymbol{\omega}_{1,2}$  and  $\boldsymbol{\omega}_{2,3}$  point in the same direction, then the theorem is clear; the angular speeds just add. If, however, they don't point in the same direction, then things are a bit harder to visualize. But we can prove the theorem by making abundant use of the definition of  $\boldsymbol{\omega}$ .

Pick a point  $P_1$  at rest in  $S_1$ . Let  $\mathbf{r}$  be the vector from the origin to  $P_1$ . The velocity of  $P_1$  (relative to a very close point  $P_2$  at rest in  $S_2$ ) due to the rotation of  $S_1$  around  $\boldsymbol{\omega}_{1,2}$  is  $\mathbf{V}_{P_1P_2} = \boldsymbol{\omega}_{1,2} \times \mathbf{r}$ . The velocity of  $P_2$  (relative to a very close point  $P_3$  at rest in  $S_3$ ) due to the rotation of  $S_2$  around  $\boldsymbol{\omega}_{2,3}$  is  $\mathbf{V}_{P_2P_3} = \boldsymbol{\omega}_{2,3} \times \mathbf{r}$ , because  $P_2$  is also located essentially at position  $\mathbf{r}$ . Therefore, the velocity of  $P_1$  relative to  $P_3$  is  $\mathbf{V}_{P_1P_2} + \mathbf{V}_{P_2P_3} = (\boldsymbol{\omega}_{1,2} + \boldsymbol{\omega}_{2,3}) \times \mathbf{r}$ . This holds for any point  $P_1$  at rest in  $S_1$ , so the frame  $S_1$  rotates with angular velocity  $(\boldsymbol{\omega}_{1,2} + \boldsymbol{\omega}_{2,3})$  with

respect to  $S_3$ . We see that the proof basically comes down to the facts that (1) the linear velocities just add, as usual, and (2) the angular velocities differ from the linear velocities by a cross product with  $\mathbf{r}$ . ■

If  $\omega_{1,2}$  is constant in  $S_2$ , then the vector  $\omega_{1,3} = \omega_{1,2} + \omega_{2,3}$  will change with respect to  $S_3$  as time goes by, because  $\omega_{1,2}$ , which is fixed in  $S_2$ , is changing with respect to  $S_3$  (assuming that  $\omega_{1,2}$  and  $\omega_{2,3}$  aren't parallel). But at any instant,  $\omega_{1,3}$  may be obtained by adding the present values of  $\omega_{1,2}$  and  $\omega_{2,3}$ . Consider the following example.

**Example (Rotating sphere):** A sphere rotates with angular speed  $\omega_3$  around a stick that initially points in the  $\hat{\mathbf{z}}$  direction. You grab the stick and rotate it around the  $\hat{\mathbf{y}}$  axis with angular speed  $\omega_2$ . What is the angular velocity of the sphere, with respect to the lab frame, as time goes by?

**Solution:** In the language of Theorem 9.3, the sphere defines the  $S_1$  frame; the stick and the  $\hat{\mathbf{y}}$  axis define the  $S_2$  frame; and the lab frame is the  $S_3$  frame. The instant after you grab the stick, we are given that  $\omega_{1,2} = \omega_3 \hat{\mathbf{z}}$ , and  $\omega_{2,3} = \omega_2 \hat{\mathbf{y}}$ . Therefore, the angular velocity of the sphere with respect to the lab frame is  $\omega_{1,3} = \omega_{1,2} + \omega_{2,3} = \omega_3 \hat{\mathbf{z}} + \omega_2 \hat{\mathbf{y}}$ , as shown in Fig. 9.5. Convince yourself that the combination of these two rotations yields zero motion for the points along the line of  $\omega_{1,3}$ . As time goes by, the stick (and hence  $\omega_{1,2}$ ) rotates around the  $\mathbf{y}$  axis, so  $\omega_{1,3} = \omega_{1,2} + \omega_{2,3}$  traces out a cone around the  $\mathbf{y}$  axis, as shown.

![Figure 9.5: A diagram showing a sphere with a stick initially pointing along the z-axis. The stick is rotated around the y-axis with angular velocity omega_2,3. The sphere rotates around the stick with angular velocity omega_1,2. The resultant angular velocity omega_1,3 is shown as the vector sum of omega_1,2 and omega_2,3, tracing out a cone around the y-axis.](2241d31050b416cc6b67611916033d19_img.jpg)

Figure 9.5: A diagram showing a sphere with a stick initially pointing along the z-axis. The stick is rotated around the y-axis with angular velocity omega\_2,3. The sphere rotates around the stick with angular velocity omega\_1,2. The resultant angular velocity omega\_1,3 is shown as the vector sum of omega\_1,2 and omega\_2,3, tracing out a cone around the y-axis.

Fig. 9.5

**REMARK:** Note the different behavior of  $\omega_{1,3}$  for a slightly different statement of the problem: Let the sphere initially rotate with angular velocity  $\omega_2 \hat{\mathbf{y}}$  around a stick, and then grab the stick and rotate it with angular velocity  $\omega_3 \hat{\mathbf{z}}$ . For this situation,  $\omega_{1,3}$  initially points in the same direction as in the original statement of the problem (it initially equals  $\omega_2 \hat{\mathbf{y}} + \omega_3 \hat{\mathbf{z}}$ ). But as time goes by, it is now the horizontal component (defined by the stick) of  $\omega_{1,3}$  that changes, so  $\omega_{1,3} = \omega_{1,2} + \omega_{2,3}$  traces out a cone around the  $\mathbf{z}$  axis, as shown in Fig. 9.6. ♣

![Figure 9.6: A diagram showing a sphere with a stick initially pointing along the z-axis. The stick is rotated around the z-axis with angular velocity omega_1,2. The sphere rotates around the stick with angular velocity omega_2,3. The resultant angular velocity omega_1,3 is shown as the vector sum of omega_1,2 and omega_2,3, tracing out a cone around the z-axis.](384558ff1c5ba98ed1094afe740ad04d_img.jpg)

Figure 9.6: A diagram showing a sphere with a stick initially pointing along the z-axis. The stick is rotated around the z-axis with angular velocity omega\_1,2. The sphere rotates around the stick with angular velocity omega\_2,3. The resultant angular velocity omega\_1,3 is shown as the vector sum of omega\_1,2 and omega\_2,3, tracing out a cone around the z-axis.

Fig. 9.6

An important point concerning rotations is that they are defined with respect to a *coordinate system*. It makes no sense to ask how fast an object is rotating with respect to a certain point, or even a certain axis. Consider, for example, an object rotating with angular velocity  $\omega = \omega_3 \hat{\mathbf{z}}$  with respect to the lab frame. Saying only, “The object has angular velocity  $\omega = \omega_3 \hat{\mathbf{z}}$ ,” is not sufficient, because someone standing in the frame of the object would measure  $\omega = 0$ , and would therefore be very confused by your statement. Throughout this chapter, we’ll try to remember to state the coordinate system with respect to which  $\omega$  is measured. But if we forget, the default frame is the lab frame.

This section was definitely a bit abstract, so don’t worry too much about it at the moment. The best strategy is perhaps to read on, and then come back for a second pass after digesting a few more sections. At any rate, we’ll be

discussing many other aspects (probably more than you'd ever want to know) of  $\boldsymbol{\omega}$  in Section 9.7.2, so you're assured of getting a lot more practice with it. For now, if you want to strain some brain cells thinking about  $\boldsymbol{\omega}$  vectors, you are encouraged to solve Problem 9.3, and also to look at the three given solutions.

### 9.2 The inertia tensor

Given an object undergoing general motion, the *inertia tensor* is what relates the angular momentum,  $\mathbf{L}$ , to the angular velocity,  $\boldsymbol{\omega}$ . This tensor (which is just a fancy name for “matrix” in this context) depends on the geometry of the object, as we'll see. In finding the  $\mathbf{L}$  due to general motion, we'll follow the strategy of Section 8.1. We'll first look at the special case of rotation around an axis through the origin, then we'll look at the most general possible motion.

![Figure 9.7: A three-dimensional object in a Cartesian coordinate system (x, y, z). The object is shaded gray and has a dashed line indicating its internal structure. An arrow labeled ω points from the origin along the z-axis, representing the angular velocity vector.](d210d3e99620b863b5d00df9b4502537_img.jpg)

Figure 9.7: A three-dimensional object in a Cartesian coordinate system (x, y, z). The object is shaded gray and has a dashed line indicating its internal structure. An arrow labeled ω points from the origin along the z-axis, representing the angular velocity vector.

Fig. 9.7

#### 9.2.1 Rotation around an axis through the origin

The three-dimensional object in Fig. 9.7 rotates with angular velocity  $\boldsymbol{\omega}$ . Consider a little piece of the body, with mass  $dm$  and position  $\mathbf{r}$ . The velocity of this piece is  $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$ , so its angular momentum (relative to the origin) is  $\mathbf{r} \times \mathbf{p} = (dm)\mathbf{r} \times \mathbf{v} = (dm)\mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r})$ . The angular momentum of the entire body is therefore

$$\mathbf{L} = \int \mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r}) dm, \quad (9.4)$$

where the integration runs over the volume of the body. In the case where the rigid body is made up of a collection of point masses  $m_i$ , the angular momentum is

$$\mathbf{L} = \sum_i m_i \mathbf{r}_i \times (\boldsymbol{\omega} \times \mathbf{r}_i). \quad (9.5)$$

The double cross product in Eqs. (9.4) and (9.5) looks a bit intimidating, but it's actually not so bad. First, we have

$$\begin{aligned} \boldsymbol{\omega} \times \mathbf{r} &= \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ \omega_1 & \omega_2 & \omega_3 \\ x & y & z \end{vmatrix} \\ &= (\omega_2 z - \omega_3 y)\hat{\mathbf{x}} + (\omega_3 x - \omega_1 z)\hat{\mathbf{y}} + (\omega_1 y - \omega_2 x)\hat{\mathbf{z}}. \end{aligned} \quad (9.6)$$

We're using the notation  $\omega_1$  instead of  $\omega_x$ , etc., because there are already enough  $x, y, z$ 's floating around here. The double cross product is then

$$\begin{aligned} \mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r}) &= \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ x & y & z \\ (\omega_2 z - \omega_3 y) & (\omega_3 x - \omega_1 z) & (\omega_1 y - \omega_2 x) \end{vmatrix} \\ &= (\omega_1(y^2 + z^2) - \omega_2 xy - \omega_3 zx)\hat{\mathbf{x}} \end{aligned}$$

$$\begin{aligned}
 &+ \left( \omega_2(z^2 + x^2) - \omega_3 yz - \omega_1 xy \right) \hat{\mathbf{y}} \\
 &+ \left( \omega_3(x^2 + y^2) - \omega_1 zx - \omega_2 yz \right) \hat{\mathbf{z}}.
 \end{aligned} \quad (9.7)$$

The angular momentum in Eq. (9.4) may therefore be written in the concise matrix form,

$$\begin{aligned}
 \begin{pmatrix} L_1 \\ L_2 \\ L_3 \end{pmatrix} &= \begin{pmatrix} \int (y^2 + z^2) & -\int xy & -\int zx \\ -\int xy & \int (z^2 + x^2) & -\int yz \\ -\int zx & -\int yz & \int (x^2 + y^2) \end{pmatrix} \begin{pmatrix} \omega_1 \\ \omega_2 \\ \omega_3 \end{pmatrix} \\
 &\equiv \begin{pmatrix} I_{xx} & I_{xy} & I_{xz} \\ I_{yx} & I_{yy} & I_{yz} \\ I_{zx} & I_{zy} & I_{zz} \end{pmatrix} \begin{pmatrix} \omega_1 \\ \omega_2 \\ \omega_3 \end{pmatrix} \\
 &\equiv \mathbf{I}\boldsymbol{\omega}.
 \end{aligned} \quad (9.8)$$

For the sake of clarity, we have not bothered to write the  $dm$  part of each integral (and we'll continue to drop it for most of the remainder of this section). The matrix  $\mathbf{I}$  is called the *inertia tensor*. If the word “tensor” scares you, just ignore it.  $\mathbf{I}$  is simply a matrix. It acts on a vector (the angular velocity) and produces another vector (the angular momentum).

**Example (Cube with origin at corner):** Calculate the inertia tensor for a solid cube of mass  $M$  and side length  $L$ , with the coordinate axes parallel to the edges of the cube, and the origin at a corner (see Fig. 9.8).

**Solution:** Due to the symmetry of the cube, there are only two integrals we need to calculate in Eq. (9.8). The diagonal entries are all equal to  $\int (y^2 + z^2) dm$ , and the off-diagonal entries are all equal to  $-\int xy dm$ . With  $dm = \rho dx dy dz$ , and  $\rho = M/L^3$ , these two integrals are

$$\begin{aligned}
 \int_0^L \int_0^L \int_0^L (y^2 + z^2) \rho dx dy dz &= \rho L^2 \int_0^L y^2 dy + \rho L^2 \int_0^L z^2 dz = \frac{2}{3} ML^2, \\
 -\int_0^L \int_0^L \int_0^L xy \rho dx dy dz &= -\rho L \int_0^L x dx \int_0^L y dy = -\frac{ML^2}{4}.
 \end{aligned} \quad (9.9)$$

Therefore,

$$\mathbf{I} = ML^2 \begin{pmatrix} 2/3 & -1/4 & -1/4 \\ -1/4 & 2/3 & -1/4 \\ -1/4 & -1/4 & 2/3 \end{pmatrix}. \quad (9.10)$$

Having found  $\mathbf{I}$ , we can calculate the angular momentum associated with any given angular velocity. If, for example, the cube is rotating around the  $z$  axis with angular speed  $\omega$ , then we can apply the matrix  $\mathbf{I}$  to the vector  $(0, 0, \omega)$  to find that the angular momentum is  $\mathbf{L} = ML^2\omega(-1/4, -1/4, 2/3)$ . Note the somewhat odd fact

![Figure 9.8: A 3D diagram of a cube with side length L. The cube is positioned in a 3D coordinate system with axes labeled x, y, and z. The origin (0,0,0) is at one corner of the cube. The edges of the cube are parallel to the coordinate axes. The length of each edge is labeled L.](79aeb2b69e07d5c789e962d0acf2193b_img.jpg)

Figure 9.8: A 3D diagram of a cube with side length L. The cube is positioned in a 3D coordinate system with axes labeled x, y, and z. The origin (0,0,0) is at one corner of the cube. The edges of the cube are parallel to the coordinate axes. The length of each edge is labeled L.

Fig. 9.8

that  $L_x$  and  $L_y$  are nonzero, even though the rotation is only around the  $z$  axis. We'll discuss this issue after the following remarks.

##### REMARKS:

1. The inertia tensor in Eq. (9.8) is a rather formidable-looking object. You will therefore be very pleased to hear that you rarely have to use it. It's nice to know that it's there if you need it, but the concept of *principal axes* (discussed in Section 9.3) provides a way to avoid using the inertia tensor (or more precisely, to greatly simplify it) and is therefore much more useful in solving problems.
2.  $\mathbf{I}$  is a symmetric matrix, which is a fact that will be important in Section 9.3. There are therefore only six independent entries, instead of nine.
3. In the case where the rigid body is made up of a collection of point masses  $m_i$ , the entries in the matrix are just sums. For example, the upper left entry is  $\sum m_i(y_i^2 + z_i^2)$ .
4.  $\mathbf{I}$  depends only on the geometry of the object, and not on  $\boldsymbol{\omega}$ .
5. To construct an  $\mathbf{I}$ , you not only need to specify the origin, you also need to specify the  $x$ ,  $y$ ,  $z$  axes of your coordinate system. And the basis vectors must be orthogonal, because the cross product calculation above is valid only for an orthonormal basis. If someone else comes along and chooses a different orthonormal basis (but the same origin), then her  $\mathbf{I}$  will have different *entries*, as will her  $\boldsymbol{\omega}$ , as will her  $\mathbf{L}$ . But her  $\boldsymbol{\omega}$  and  $\mathbf{L}$  will be exactly the same *vectors* as your  $\boldsymbol{\omega}$  and  $\mathbf{L}$ . They will appear different only because they are written in a different coordinate system. A vector is what it is, independent of how you choose to look at it. If you each point your arm in the direction of what you calculate  $\mathbf{L}$  to be, then you will both be pointing in the same direction.
6. For the case of a pancake object rotating in the  $x$ - $y$  plane, we have  $z = 0$  for all points in the object. And  $\boldsymbol{\omega} = \omega_3 \hat{\mathbf{z}}$ , so  $\omega_1 = \omega_2 = 0$ . The only nonzero term in the  $\mathbf{L}$  in Eq. (9.8) is therefore  $L_3 = \int (x^2 + y^2) dm \omega_3$ , which is simply the  $L_z = I_z \omega$  result we found in Eq. (8.5). ♣

This is all perfectly fine. Given any rigid body, we can calculate  $\mathbf{I}$  (relative to a given origin, using a given set of axes). And given  $\boldsymbol{\omega}$ , we can then apply  $\mathbf{I}$  to it to find  $\mathbf{L}$ . But what do these entries in  $\mathbf{I}$  really mean? How do we interpret them? Note, for example, that  $\omega_3$  appears not only in  $L_3$  in Eq. (9.8), but also in  $L_1$  and  $L_2$ . But  $\omega_3$  is relevant to rotations around the  $z$  axis, so what in the world is it doing in  $L_1$  and  $L_2$ ? Consider the following examples.

![Diagram showing a point mass m rotating in the x-y plane. The z-axis is vertical, and the x and y axes are horizontal. A dashed circle of radius r is centered at the origin. A point mass m is shown on this circle. A vector omega points along the positive z-axis, indicating rotation. A vector r points from the origin to the mass m.](a151970ea97a67e6f597f8ab5bb5a9cc_img.jpg)

Diagram showing a point mass m rotating in the x-y plane. The z-axis is vertical, and the x and y axes are horizontal. A dashed circle of radius r is centered at the origin. A point mass m is shown on this circle. A vector omega points along the positive z-axis, indicating rotation. A vector r points from the origin to the mass m.

Fig. 9.9

**Example 1 (Point mass in the  $x$ - $y$  plane):** Consider a point mass  $m$  traveling in a circle of radius  $r$  (centered at the origin) in the  $x$ - $y$  plane, with frequency  $\omega_3$ , as shown in Fig. 9.9. Using  $\boldsymbol{\omega} = (0, 0, \omega_3)$ ,  $x^2 + y^2 = r^2$ , and  $z = 0$  in Eq. (9.8) (with a discrete sum of only one object, instead of the integrals), the angular momentum with respect to the origin is

$$\mathbf{L} = (0, 0, mr^2\omega_3). \quad (9.11)$$

The  $z$  component is  $mr(r\omega_3) = mrv$ , as it should be. And the  $x$  and  $y$  components are zero, as they should be. This case where  $\omega_1 = \omega_2 = 0$  and  $z = 0$  is simply the case we studied in Chapter 8, as mentioned in Remark 6 above.

**Example 2 (Point mass in space):** Consider a point mass  $m$  traveling in a circle of radius  $r$ , with frequency  $\omega_3$ . But now let the circle be centered at the point  $(0, 0, z_0)$ , with the plane of the circle parallel to the  $x$ - $y$  plane, as shown in Fig. 9.10. Using  $\boldsymbol{\omega} = (0, 0, \omega_3)$ ,  $x^2 + y^2 = r^2$ , and  $z = z_0$  in Eq. (9.8), the angular momentum with respect to the origin is

$$\mathbf{L} = m\omega_3(-xz_0, -yz_0, r^2). \quad (9.12)$$

The  $z$  component is  $mr^2\omega_3$ , as it should be. But surprisingly, we have nonzero  $L_1$  and  $L_2$ , even though the mass is just rotating around the  $z$  axis.  $\mathbf{L}$  does *not* point along  $\boldsymbol{\omega}$  here. What’s going on?

Consider an instant when the mass is in the  $y$ - $z$  plane, as shown in Fig. 9.10. The velocity of the mass is then in the  $-\hat{x}$  direction. Therefore, the particle most certainly has angular momentum around the  $y$  axis, as well as the  $z$  axis. Someone looking at a split-second movie of the mass at this point can’t tell whether it’s rotating around the  $y$  axis, the  $z$  axis, or undergoing some complicated motion. But the past and future motion is irrelevant; at any instant in time, as far as the angular momentum goes, we are concerned only with what is happening at this instant.

At this instant, the angular momentum around the  $y$  axis is  $L_2 = -mz_0v$ , because  $z_0$  is the distance from the  $y$  axis, and the minus sign comes from the right-hand rule. Using  $v = \omega_3 r = \omega_3 y$ , we have  $L_2 = -mz_0\omega_3 y$ , in agreement with Eq. (9.12). Also, at this instant,  $L_1$  is zero, because the velocity is parallel to the  $x$  axis. This agrees with Eq. (9.12), since  $x = 0$ . As an exercise, you can check that Eq. (9.12) is also correct when the mass is at a general point  $(x, y, z_0)$ .

We see that, for example, the  $I_{yz} \equiv -\int yz$  entry in  $\mathbf{I}$  tells us how much the  $\omega_3$  component of the angular velocity contributes to the  $L_2$  component of the angular momentum. And due to the symmetry of  $\mathbf{I}$ , the  $I_{yz} = I_{zy}$  entry in  $\mathbf{I}$  also tells us how much the  $\omega_2$  component of the angular velocity contributes to the  $L_3$  component of the angular momentum. In the former case, if we group the product of the various quantities as  $-\int (\omega_3 y)z$ , we see that this is simply the appropriate component of the velocity times the distance from the  $y$  axis. In the latter case with  $-\int (\omega_2 z)y$ , it is the opposite grouping. But in both cases there is one factor of  $y$  and one factor of  $z$ , hence the symmetry in  $\mathbf{I}$ .

**REMARK:** For a point mass,  $\mathbf{L}$  is actually more easily obtained by just calculating  $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ . The result for the instant shown in Fig. 9.10 is drawn in Fig. 9.11, where it is clear that  $\mathbf{L}$  has both  $y$  and  $z$  components, and thus also clear that  $\mathbf{L}$  doesn’t point along  $\boldsymbol{\omega}$ . For a more complicated object, the tensor  $\mathbf{I}$  is generally used, because it is necessary to perform the integral of the  $\mathbf{L} = \mathbf{r} \times \mathbf{p}$  contributions over the entire object, and the tensor has this integral built into it. At any rate, whatever method you use, you will find that except in special circumstances (see Section 9.3),  $\mathbf{L}$  doesn’t point along  $\boldsymbol{\omega}$ .

Consider the vector of  $\mathbf{L}$ ,  
 And that of  $\boldsymbol{\omega}$  as well.  
 The erroneous claim  
 That they must aim the same  
 Is a view that you’ve got to dispel! ♣

![Diagram showing a point mass rotating in a circle parallel to the x-y plane at height z_0. The angular velocity vector omega points along the z-axis. The position vector r is shown from the origin to the mass.](57aa46709bedbaefdc5b26b182af5626_img.jpg)

A 3D coordinate system with x, y, and z axes. A horizontal dashed circle of radius r is centered on the z-axis at height z\_0. A point mass is located on this circle in the y-z plane. A vector  $\boldsymbol{\omega}$  points upwards along the z-axis. A vector  $\mathbf{r}$  points from the origin to the mass.

Diagram showing a point mass rotating in a circle parallel to the x-y plane at height z\_0. The angular velocity vector omega points along the z-axis. The position vector r is shown from the origin to the mass.

Fig. 9.10

![Diagram showing the angular momentum vector L and linear momentum vector p for the point mass. L is shown with both y and z components, not aligned with omega.](7daf83b00b82863dbf295db2259e102a_img.jpg)

The same 3D coordinate system as Fig. 9.10. The point mass is at the same position. The angular momentum vector  $\mathbf{L}$  is shown originating from the origin and pointing into the y-z plane, making an angle with the z-axis. The linear momentum vector  $\mathbf{p}$  is shown as a circle with a cross (into the page) at the position of the mass. The vector  $\mathbf{r}$  is also shown.

Diagram showing the angular momentum vector L and linear momentum vector p for the point mass. L is shown with both y and z components, not aligned with omega.

Fig. 9.11

![Figure 9.12: A 3D coordinate system with x, y, and z axes. A vertical dashed line represents the z-axis. A horizontal dashed circle is centered on the z-axis at height z_0. A point on this circle is at distance r from the z-axis. A vector ω points upwards along the z-axis. A point mass m is shown at a point on the circle.](6bce4675fc0ab74606ce3fe5a625a332_img.jpg)

Figure 9.12: A 3D coordinate system with x, y, and z axes. A vertical dashed line represents the z-axis. A horizontal dashed circle is centered on the z-axis at height z\_0. A point on this circle is at distance r from the z-axis. A vector ω points upwards along the z-axis. A point mass m is shown at a point on the circle.

Fig. 9.12

**Example 3 (Two point masses):** Let's now add another point mass  $m$  to the previous example. Let it travel in the same circle, at the diametrically opposite point, as shown in Fig. 9.12. Using  $\omega = (0, 0, \omega_3)$ ,  $x^2 + y^2 = r^2$ , and  $z = z_0$  in Eq. (9.8), you can show that the angular momentum with respect to the origin is

$$\mathbf{L} = 2m\omega_3(0, 0, r^2). \quad (9.13)$$

Since  $v = \omega_3 r$ , the  $z$  component is  $2mr v$ , as it should be. And  $L_1$  and  $L_2$  are zero, unlike in the previous example, because these components of the  $\mathbf{L}$ 's of the two particles cancel. This occurs because of the symmetry of the masses around the  $z$  axis, which causes the  $I_{zx}$  and  $I_{zy}$  entries in the inertia tensor to vanish; they are each the sum of two terms, with opposite  $x$  values, or opposite  $y$  values. Alternatively, you can just note that adding on the mirror-image  $\mathbf{L}$  vector in Fig. 9.10 produces canceling  $x$  and  $y$  components.

Let's now look at the kinetic energy of our object, which is rotating around an axis passing through the origin. To find this, we must add up the kinetic energies of all the little pieces. A little piece has energy  $(dm) v^2/2 = dm |\omega \times \mathbf{r}|^2/2$ . Therefore, using Eq. (9.6), the total kinetic energy is

$$T = \frac{1}{2} \int \left( (\omega_2 z - \omega_3 y)^2 + (\omega_3 x - \omega_1 z)^2 + (\omega_1 y - \omega_2 x)^2 \right) dm. \quad (9.14)$$

Multiplying this out, we see (after a little work) that we can write  $T$  as

$$\begin{aligned} T &= \frac{1}{2} (\omega_1, \omega_2, \omega_3) \cdot \begin{pmatrix} \int (y^2 + z^2) & -\int xy & -\int zx \\ -\int xy & \int (z^2 + x^2) & -\int yz \\ -\int zx & -\int yz & \int (x^2 + y^2) \end{pmatrix} \begin{pmatrix} \omega_1 \\ \omega_2 \\ \omega_3 \end{pmatrix} \\ &= \frac{1}{2} \omega \cdot \mathbf{I} \omega = \frac{1}{2} \omega \cdot \mathbf{L}. \end{aligned} \quad (9.15)$$

If  $\omega = \omega_3 \hat{\mathbf{z}}$ , then this reduces to  $T = I_{zz} \omega_3^2/2$ , which agrees with the result in Eq. (8.8), with a slight change in notation.

![Figure 9.13: A 3D coordinate system with x, y, and z axes. A shaded, irregularly shaped object is shown. A vector v points from the origin to a point on the object. A vector ω points from the origin to another point on the object.](3226bba3dd4af9debc1359b4e2bdda1e_img.jpg)

Figure 9.13: A 3D coordinate system with x, y, and z axes. A shaded, irregularly shaped object is shown. A vector v points from the origin to a point on the object. A vector ω points from the origin to another point on the object.

Fig. 9.13

#### 9.2.2 General motion

How do we deal with general motion in space? That is, what if an object is both translating and rotating? For the motion in Fig. 9.13, the various pieces of mass aren't traveling in circles around the origin, so we can't write  $\mathbf{v} = \omega \times \mathbf{r}$ , as we did prior to Eq. (9.4).

To determine  $\mathbf{L}$  (relative to the origin), and also the kinetic energy  $T$ , we will use Theorem 9.1 to write the motion as the sum of a translation plus a rotation. In applying the theorem, we may choose any point in the body to be the point  $P$  in the theorem. However, only in the case where  $P$  is the object's CM can we extract anything useful, as we'll see. The theorem then says that the motion of

the body is the sum of the motion of the CM plus a rotation around the CM. So let the CM move with velocity  $\mathbf{V}$ , and let the body instantaneously rotate with angular velocity  $\boldsymbol{\omega}'$  around the CM (that is, with respect to the frame whose origin is the CM, and whose axes are parallel to the fixed-frame axes).<sup>4</sup>

Let the position of the CM relative to the origin be  $\mathbf{R} = (X, Y, Z)$ , and let the position of a given piece of mass relative to the CM be  $\mathbf{r}' = (x', y', z')$ . Then  $\mathbf{r} = \mathbf{R} + \mathbf{r}'$  is the position of a piece of mass relative to the origin (see Fig. 9.14). Let the velocity of a piece of mass relative to the CM be  $\mathbf{v}'$  (so  $\mathbf{v}' = \boldsymbol{\omega}' \times \mathbf{r}'$ ). Then  $\mathbf{v} = \mathbf{V} + \mathbf{v}'$  is the velocity relative to the origin.

Let's look at  $\mathbf{L}$  first. The angular momentum is

$$\begin{aligned}\mathbf{L} &= \int \mathbf{r} \times \mathbf{v} \, dm = \int (\mathbf{R} + \mathbf{r}') \times (\mathbf{V} + (\boldsymbol{\omega}' \times \mathbf{r}')) \, dm \\ &= \int (\mathbf{R} \times \mathbf{V}) \, dm + \int \mathbf{r}' \times (\boldsymbol{\omega}' \times \mathbf{r}') \, dm \\ &= M(\mathbf{R} \times \mathbf{V}) + \mathbf{L}_{\text{CM}},\end{aligned}\quad (9.16)$$

where the cross terms vanish because the integrands are linear in  $\mathbf{r}'$ . More precisely, the integrals involve  $\int \mathbf{r}' \, dm$ , which is zero by definition of the CM (because  $\int \mathbf{r}' \, dm/M$  is the position of the CM relative to the CM, which is zero).  $\mathbf{L}_{\text{CM}}$  is the angular momentum relative to the CM.<sup>5</sup>

We see that as in the pancake case in Section 8.1.2, the angular momentum (relative to the origin) of a body can be found by treating the body like a point mass located at the CM and finding the angular momentum of this point mass relative to the origin, and by then adding on the angular momentum of the body relative to the CM. Note that these two parts of the angular momentum need not point in the same direction, as they did in the case of the pancake moving in the  $x$ - $y$  plane.

Now let's look at  $T$ . The kinetic energy is

$$\begin{aligned}T &= \int \frac{1}{2} v^2 \, dm = \int \frac{1}{2} |\mathbf{V} + \mathbf{v}'|^2 \, dm \\ &= \int \frac{1}{2} V^2 \, dm + \int \frac{1}{2} v'^2 \, dm \\ &= \frac{1}{2} M V^2 + \int \frac{1}{2} |\boldsymbol{\omega}' \times \mathbf{r}'|^2 \, dm \\ &\equiv \frac{1}{2} M V^2 + \frac{1}{2} \boldsymbol{\omega}' \cdot \mathbf{L}_{\text{CM}},\end{aligned}\quad (9.17)$$

<sup>4</sup> It's not necessary to put the prime on the  $\boldsymbol{\omega}$  here, because the angular velocity vector in the CM frame is the same as in the lab frame. But we'll use the prime just because we'll have primes on the other CM quantities below.

<sup>5</sup> By this, we mean the angular momentum as measured in the coordinate system whose origin is the CM, and whose axes are parallel to the fixed-frame axes.

![Figure 9.14: A 3D coordinate system with axes x, y, and z. The origin is at the bottom left. A point labeled 'CM' is located at position vector R from the origin. A second point is located at position vector r from the origin. The vector from the CM to this second point is labeled r'.](9d6e3462ea6123b32635c3632f0c00b6_img.jpg)

Figure 9.14: A 3D coordinate system with axes x, y, and z. The origin is at the bottom left. A point labeled 'CM' is located at position vector R from the origin. A second point is located at position vector r from the origin. The vector from the CM to this second point is labeled r'.

Fig. 9.14

![Figure 9.15: A 3D diagram showing a rigid body in a Cartesian coordinate system with axes x, y, and z. The center of mass (CM) is marked within the body. Two angular velocity vectors, both labeled ω', are shown: one originating from the origin and another from the CM. The vectors are parallel, indicating that the body rotates with the same angular velocity about both points.](c81369ed8576a29a8f403352bfe13c27_img.jpg)

Figure 9.15: A 3D diagram showing a rigid body in a Cartesian coordinate system with axes x, y, and z. The center of mass (CM) is marked within the body. Two angular velocity vectors, both labeled ω', are shown: one originating from the origin and another from the CM. The vectors are parallel, indicating that the body rotates with the same angular velocity about both points.

Fig. 9.15

where the last line follows from the steps leading to Eq. (9.15). The cross term  $\int \mathbf{V} \cdot \mathbf{v}' dm = \int \mathbf{V} \cdot (\boldsymbol{\omega}' \times \mathbf{r}') dm$  vanishes because the integrand is linear in  $\mathbf{r}'$  and thus yields a zero integral, by definition of the CM. As in the pancake case in Section 8.1.2, the kinetic energy of a body can be found by treating the body like a point mass located at the CM, and by then adding on the kinetic energy of the body due to the rotation around the CM.

#### 9.2.3 The parallel-axis theorem

Consider the special case where the CM rotates around the origin with the same angular velocity at which the body rotates around the CM (see Fig. 9.15), that is,  $\mathbf{V} = \boldsymbol{\omega}' \times \mathbf{R}$ . This can be achieved, for example, by piercing the body with the base of a rigid “T” and then rotating the T and the body around the (fixed) line of the “upper” part of the T (the origin must pass through this line). We then have the nice situation where all points in the body travel in fixed circles around the axis of rotation. Mathematically, this follows from  $\mathbf{v} = \mathbf{V} + \mathbf{v}' = \boldsymbol{\omega}' \times \mathbf{R} + \boldsymbol{\omega}' \times \mathbf{r}' = \boldsymbol{\omega}' \times \mathbf{r}$ . Dropping the prime on  $\boldsymbol{\omega}$ , Eq. (9.16) becomes

$$\mathbf{L} = M\mathbf{R} \times (\boldsymbol{\omega} \times \mathbf{R}) + \int \mathbf{r}' \times (\boldsymbol{\omega} \times \mathbf{r}') dm \quad (9.18)$$

Expanding the double cross products as in the steps leading to Eq. (9.8), we can write this as

$$\begin{aligned} \begin{pmatrix} L_1 \\ L_2 \\ L_3 \end{pmatrix} &= M \begin{pmatrix} Y^2 + Z^2 & -XY & -ZX \\ -XY & Z^2 + X^2 & -YZ \\ -ZX & -YZ & X^2 + Y^2 \end{pmatrix} \begin{pmatrix} \omega_1 \\ \omega_2 \\ \omega_3 \end{pmatrix} \\ &+ \begin{pmatrix} \int (y'^2 + z'^2) & -\int x'y' & -\int z'x' \\ -\int x'y' & \int (z'^2 + x'^2) & -\int y'z' \\ -\int z'x' & -\int y'z' & \int (x'^2 + y'^2) \end{pmatrix} \begin{pmatrix} \omega_1 \\ \omega_2 \\ \omega_3 \end{pmatrix} \\ &\equiv (\mathbf{I}_R + \mathbf{I}_{CM})\boldsymbol{\omega}. \end{aligned} \quad (9.19)$$

This is the generalized parallel-axis theorem. It says that once you’ve calculated  $\mathbf{I}_{CM}$  relative to the CM, then if you want to calculate  $\mathbf{I}$  relative to another point, you simply have to add on the  $\mathbf{I}_R$  matrix, obtained by treating the object like a point mass at the CM. So you have to compute six extra numbers (there are six, instead of nine, because the  $\mathbf{I}_R$  matrix is symmetric) instead of just the one  $MR^2$  in the parallel-axis theorem in Chapter 8, given in Eq. (8.13). Problem 9.4 gives another derivation of the parallel-axis theorem, without mentioning the angular velocity.

**REMARK:** The name “parallel-axis” theorem is actually a misnomer here. The inertia tensor isn’t associated with one particular axis, as the moment of inertia in Chapter 8 was. The moment of inertia is just one of the diagonal entries (associated with a given axis) in the inertia tensor. The inertia tensor depends on the entire coordinate system. So in that sense we should call this

the “parallel-axes” theorem, because the coordinate axes in the CM frame are assumed to be parallel to the ones in the fixed frame. At any rate, the point is that the parallel-axis theorem in Chapter 8 dealt with shifting the axis, whereas the present theorem deals with shifting the origin (and hence all three axes in general). ♣

As far as the kinetic energy goes, if  $\boldsymbol{\omega}$  and  $\boldsymbol{\omega}'$  are equal, so that  $\mathbf{V} = \boldsymbol{\omega}' \times \mathbf{R}$ , then Eq. (9.17) gives (dropping the prime on  $\boldsymbol{\omega}$ )

$$T = \frac{1}{2}M|\boldsymbol{\omega} \times \mathbf{R}|^2 + \int \frac{1}{2}|\boldsymbol{\omega} \times \mathbf{r}'|^2 dm. \quad (9.20)$$

Performing the steps leading to Eq. (9.15), this becomes

$$T = \frac{1}{2}\boldsymbol{\omega} \cdot (\mathbf{I}_R + \mathbf{I}_{CM})\boldsymbol{\omega} = \frac{1}{2}\boldsymbol{\omega} \cdot \mathbf{L}. \quad (9.21)$$

### 9.3 Principal axes

The cumbersome expressions in the previous section may seem a bit unsettling, but it turns out that usually we can get by without them. The strategy for avoiding all of the above mess is to use the *principal axes* of a body, which we will define below.

In general, the inertia tensor  $\mathbf{I}$  in Eq. (9.8) has nine nonzero entries, of which six are independent due to the symmetry of  $\mathbf{I}$ . In addition to depending on the origin chosen, the inertia tensor depends on the set of orthonormal basis vectors chosen for the coordinate system; the  $x, y, z$  variables in the integrals in  $\mathbf{I}$  depend, of course, on the coordinate system they’re measured with respect to. Given a blob of material, and given an arbitrary origin,<sup>6</sup> any orthonormal set of basis vectors is usable, but there is one special set that makes all our calculations very nice. These special basis vectors are called the *principal axes*. They can be defined in various equivalent ways:

- The principal axes are the orthonormal basis vectors for which  $\mathbf{I}$  is diagonal, that is, for which<sup>7</sup>

$$\mathbf{I} = \begin{pmatrix} I_1 & 0 & 0 \\ 0 & I_2 & 0 \\ 0 & 0 & I_3 \end{pmatrix}. \quad (9.22)$$

$I_1, I_2$ , and  $I_3$  are called the *principal moments*. For many objects, it is quite obvious what the principal axes are. For example, consider a uniform rectangle in the  $x$ - $y$  plane. Pick the origin to be the CM, and let the  $x$  and  $y$  axes be parallel to the sides. Then the

<sup>6</sup> The CM is often chosen to be the origin, but it need not be. There are principal axes associated with any origin.

<sup>7</sup> Technically, we should be writing  $I_{11}$  or  $I_{xx}$  instead of  $I_1$ , etc., in this matrix, because the one-index object  $I_1$  looks like the component of a vector, not a matrix. But the two-index notation gets cumbersome, so we’ll be sloppy and just use  $I_1$ , etc.

principal axes are clearly the  $x$ ,  $y$ , and  $z$  axes, because all the off-diagonal elements in the inertia tensor in Eq. (9.8) vanish, by symmetry. For example,  $I_{xy} \equiv -\int xy \, dm$  equals zero, because for every point  $(x, y)$  in the rectangle, there is a corresponding point  $(-x, y)$ , so the contributions to  $\int xy \, dm$  cancel in pairs. Also, the integrals involving  $z$  are identically zero, because  $z = 0$ .

- A principal axis is an axis  $\hat{\boldsymbol{\omega}}$  for which  $\mathbf{I}\hat{\boldsymbol{\omega}} = I\hat{\boldsymbol{\omega}}$ . That is, a principal axis is a special direction with the property that if  $\boldsymbol{\omega}$  points along it, then so does  $\mathbf{L}$ . The principal axes of an object are then the orthonormal set of three vectors  $\hat{\boldsymbol{\omega}}_1, \hat{\boldsymbol{\omega}}_2, \hat{\boldsymbol{\omega}}_3$  with the property that

$$\mathbf{I}\hat{\boldsymbol{\omega}}_1 = I_1\hat{\boldsymbol{\omega}}_1, \quad \mathbf{I}\hat{\boldsymbol{\omega}}_2 = I_2\hat{\boldsymbol{\omega}}_2, \quad \mathbf{I}\hat{\boldsymbol{\omega}}_3 = I_3\hat{\boldsymbol{\omega}}_3. \quad (9.23)$$

The three statements in Eq. (9.23) are equivalent to Eq. (9.22), because the vectors  $\hat{\boldsymbol{\omega}}_1, \hat{\boldsymbol{\omega}}_2$ , and  $\hat{\boldsymbol{\omega}}_3$  are simply  $(1, 0, 0)$ ,  $(0, 1, 0)$ , and  $(0, 0, 1)$  in the frame in which they are the basis vectors.

- Consider an object rotating around a fixed axis with constant angular speed. Then this axis is a principal axis if there is no need for any torque. So in some sense, the object is “happy” to spin around a principal axis. A set of three orthonormal axes, each of which has this property, is by definition what we call a set of principal axes.

This definition of a principal axis is equivalent to the previous definition for the following reason. Assume that the object rotates around a fixed axis  $\hat{\boldsymbol{\omega}}_1$  for which  $\mathbf{L} = \mathbf{I}\hat{\boldsymbol{\omega}}_1 = I_1\hat{\boldsymbol{\omega}}_1$ , as in Eq. (9.23). Then since  $\hat{\boldsymbol{\omega}}_1$  is assumed to be fixed, we see that  $\mathbf{L}$  is also fixed. Therefore,  $\boldsymbol{\tau} = d\mathbf{L}/dt = \mathbf{0}$ .

Conversely, if the object is rotating around a fixed axis  $\hat{\boldsymbol{\omega}}_1$ , and if  $\boldsymbol{\tau} = d\mathbf{L}/dt = \mathbf{0}$ , then we claim that  $\mathbf{L}$  points along  $\hat{\boldsymbol{\omega}}_1$  (that is,  $\mathbf{L} = I_1\hat{\boldsymbol{\omega}}_1$ ). This is true because if  $\mathbf{L}$  does *not* point along  $\hat{\boldsymbol{\omega}}_1$ , then imagine painting a dot on the object somewhere along the line of  $\mathbf{L}$ . A little while later, the dot will have rotated around the fixed vector  $\hat{\boldsymbol{\omega}}_1$ . But the line of  $\mathbf{L}$  must always pass through the dot, because we could have rotated our axes around  $\hat{\boldsymbol{\omega}}_1$  and started the process at a slightly later time (this argument relies on  $\hat{\boldsymbol{\omega}}_1$  being fixed). Therefore, we see that  $\mathbf{L}$  has changed, in contradiction to the assumption that  $d\mathbf{L}/dt = \mathbf{0}$ . Hence,  $\mathbf{L}$  must in fact point along  $\hat{\boldsymbol{\omega}}_1$ .

For a rotation around a principal axis  $\hat{\boldsymbol{\omega}}$ , the lack of need for any torque means that if the object is pivoted at the origin, and if the origin is the only place where any force is applied (which implies that there is zero torque around it), then the object can undergo rotation with constant angular velocity  $\boldsymbol{\omega}$ . If you try to set up this scenario with a nonprincipal axis, it won’t work.

![Figure 9.16: A diagram showing a square in the xy-plane with its bottom-left corner at the origin. The square is shaded gray. Two dashed lines originate from the origin: one labeled ω̂₂ pointing into the square, and another labeled ω̂₁ pointing downwards and to the right, outside the square. The axes are labeled x̂ and ŷ.](3bbc3ec2785d851f63ae4097a31a93a5_img.jpg)

Figure 9.16: A diagram showing a square in the xy-plane with its bottom-left corner at the origin. The square is shaded gray. Two dashed lines originate from the origin: one labeled ω̂₂ pointing into the square, and another labeled ω̂₁ pointing downwards and to the right, outside the square. The axes are labeled x̂ and ŷ.

Fig. 9.16

**Example (Square with origin at corner):** Consider the uniform square in Fig. 9.16. In Appendix E, we show that the principal axes are the dotted lines drawn (and also the  $z$  axis perpendicular to the page). But there is no need to use the techniques in the appendix to see this, because in this new basis it is clear by symmetry that the integral  $\int x_1 x_2$  is zero; for every  $x_1$  in the integral, there is a  $-x_1$ . And  $x_3 \equiv z$

is identically zero, which makes all the other off-diagonal terms in  $\mathbf{I}$  also equal to zero. Therefore, since  $\mathbf{I}$  is diagonal in this new basis, these basis vectors are the principal axes.

Furthermore, it is intuitively clear that the square will be happy to rotate around any one of these axes indefinitely. During such a rotation, the pivot will certainly be applying a *force* (if the axis is  $\hat{\omega}_1$  or  $\hat{z}$ , but not if it is  $\hat{\omega}_2$ ), to produce the centripetal acceleration of the CM in its circular motion. But it won't be applying a *torque* relative to the origin (because the  $\mathbf{r}$  in  $\mathbf{r} \times \mathbf{F}$  is  $\mathbf{0}$ ). This is good, because for a rotation around one of these principal axes,  $d\mathbf{L}/dt = \mathbf{0}$ , so there is no need for any torque.

In contrast with the off-diagonal zeros in the new basis, the integral  $\int xy$  in the old basis is *not* zero, because every point gives a positive contribution. So the inertia tensor is not diagonal in the old basis, which means that  $\hat{x}$  and  $\hat{y}$  are not principal axes. Consistent with this, it is reasonably clear that it is impossible to make the square rotate around, say, the  $x$  axis, assuming that its only contact with the outside world is through a pivot (for example, a ball and socket) at the origin. The square simply doesn't want to remain in this circular motion. Mathematically,  $\mathbf{L}$  (relative to the origin) doesn't point along the  $x$  axis, so it therefore precesses around the  $x$  axis along with the square, tracing out the surface of a cone. This means that  $\mathbf{L}$  is changing. But there is no torque available (relative to the origin) to provide for this change in  $\mathbf{L}$ . Hence, such a rotation cannot exist.

---

At the moment, it is not at all obvious that an orthonormal set of principal axes exists for an arbitrary object. But this is indeed the case, as stated in Theorem 9.4 below. Assuming for now that principal axes do exist, then in this basis the  $\mathbf{L}$  and  $T$  in Eqs. (9.8) and (9.15) take on the particularly nice forms,

$$\begin{aligned}\mathbf{L} &= (I_1\omega_1, I_2\omega_2, I_3\omega_3), \\ T &= \frac{1}{2} \left( I_1\omega_1^2 + I_2\omega_2^2 + I_3\omega_3^2 \right).\end{aligned}\tag{9.24}$$

The quantities  $\omega_1$ ,  $\omega_2$ , and  $\omega_3$  here are the components of a general vector  $\boldsymbol{\omega}$  written in the principal-axis basis; that is,  $\boldsymbol{\omega} = \omega_1\hat{\omega}_1 + \omega_2\hat{\omega}_2 + \omega_3\hat{\omega}_3$ . Equation (9.24) is a vast simplification over the general formulas in Eqs. (9.8) and (9.15). We will therefore invariably work with principal axes in the remainder of this chapter.

Note that the directions of the principal axes (relative to the body) depend only on the geometry of the body. They may therefore be considered to be painted on (or in) it. Hence, they will generally move around in space as the body rotates. For example, if the object is rotating around a principal axis, then that axis stays fixed while the other two principal axes rotate around it. In relations like  $\boldsymbol{\omega} = (\omega_1, \omega_2, \omega_3)$  and  $\mathbf{L} = (I_1\omega_1, I_2\omega_2, I_3\omega_3)$ , the components  $\omega_i$  and  $I_i\omega_i$  are measured along the *instantaneous* principal axes  $\hat{\omega}_i$ . Since these axes change with time, it is quite possible that the components  $\omega_i$  and  $I_i\omega_i$  change with time, as we'll see in Section 9.5 (and onward).

Let's now state the theorem that implies that a set of principal axes does indeed exist for any body and any origin. The proof of this theorem involves a useful but rather slick technique, but it's slightly off the main line of thought, so we'll relegate it to Appendix D. Take a look at the proof if you wish, but if you want to just accept the fact that principal axes exist, that's fine.

**Theorem 9.4** *Given a real symmetric  $3 \times 3$  matrix,  $\mathbf{I}$ , there exist three orthonormal real vectors,  $\hat{\mathbf{\omega}}_k$ , and three real numbers,  $I_k$ , with the property that*

$$\mathbf{I}\hat{\mathbf{\omega}}_k = I_k\hat{\mathbf{\omega}}_k. \quad (9.25)$$

**Proof:** See Appendix D. ■

Since the inertia tensor in Eq. (9.8) is indeed symmetric for any body and any origin, this theorem says that we can always find three orthogonal basis vectors that satisfy Eq. (9.23). Or equivalently, we can always find three orthogonal basis vectors for which  $\mathbf{I}$  is a diagonal matrix, as in Eq. (9.22). In other words, principal axes always exist. Problem 9.7 gives another way to demonstrate the existence of principal axes in the special case of a pancake object.

Invariably, it is best to work in a coordinate system that has principal axes as its basis, due to the simplicity of Eq. (9.24). And as mentioned in Footnote 6, the origin is generally chosen to be the CM, because from Section 8.4.3 the CM is one of the origins for which  $\boldsymbol{\tau} = d\mathbf{L}/dt$  is a valid statement. But this choice is not necessary; there are principal axes associated with any origin.

For an object with a fair amount of symmetry, the principal axes are usually the obvious choices and can be written down by simply looking at the object (examples are given below). If, however, you are given an unsymmetrical body, then the only way to determine the principal axes is to pick an arbitrary basis, then find  $\mathbf{I}$  in this basis, and then go through a diagonalization procedure. This diagonalization procedure basically consists of the steps at the beginning of the proof of Theorem 9.4 (given in Appendix D), with the addition of one more step to get the actual vectors, so we'll relegate it to Appendix E. There's no need to worry much about this method. Virtually every system you encounter will involve an object with sufficient symmetry to enable you to just write down the principal axes.

Let's now prove two very useful (and very similar) theorems.

**Theorem 9.5** *If two principal moments are equal ( $I_1 = I_2 \equiv I$ ), then any axis (through the chosen origin) in the plane of the corresponding principal axes is a principal axis, and its moment is also  $I$ . Similarly, if all three principal moments are equal ( $I_1 = I_2 = I_3 \equiv I$ ), then any axis (through the chosen origin) in space is a principal axis, and its moment is also  $I$ .*

**Proof:** The first part was already proved at the end of the proof in Appendix D, but we'll do it again here. Since  $I_1 = I_2 \equiv I$ , we have  $\mathbf{I}\mathbf{u}_1 = I\mathbf{u}_1$ , and  $\mathbf{I}\mathbf{u}_2 = I\mathbf{u}_2$ ,

where the  $\mathbf{u}$ 's are the principal axes. Hence,  $\mathbf{I}(a\mathbf{u}_1 + b\mathbf{u}_2) = I(a\mathbf{u}_1 + b\mathbf{u}_2)$ , for any  $a$  and  $b$ . Therefore, any linear combination of  $\mathbf{u}_1$  and  $\mathbf{u}_2$  (that is, any vector in the plane spanned by  $\mathbf{u}_1$  and  $\mathbf{u}_2$ ) is a solution to  $\mathbf{I}\mathbf{u} = I\mathbf{u}$  and is thus a principal axis, by definition.

The proof of the second part proceeds in a similar manner. Since  $I_1 = I_2 = I_3 \equiv I$ , we have  $\mathbf{I}\mathbf{u}_1 = I\mathbf{u}_1$ ,  $\mathbf{I}\mathbf{u}_2 = I\mathbf{u}_2$ , and  $\mathbf{I}\mathbf{u}_3 = I\mathbf{u}_3$ . Hence,  $\mathbf{I}(a\mathbf{u}_1 + b\mathbf{u}_2 + c\mathbf{u}_3) = I(a\mathbf{u}_1 + b\mathbf{u}_2 + c\mathbf{u}_3)$ . Therefore, any linear combination of  $\mathbf{u}_1$ ,  $\mathbf{u}_2$ , and  $\mathbf{u}_3$  (that is, any vector in space) is a solution to  $\mathbf{I}\mathbf{u} = I\mathbf{u}$  and is thus a principal axis, by definition.

In short, if  $I_1 = I_2 \equiv I$ , then  $\mathbf{I}$  is the identity matrix (up to a multiple) in the space spanned by  $\mathbf{u}_1$  and  $\mathbf{u}_2$ . And if  $I_1 = I_2 = I_3 \equiv I$ , then  $\mathbf{I}$  is the identity matrix (up to a multiple) in the entire space. Note that it isn't required that the various  $\mathbf{u}_i$  vectors be orthogonal. All we need is that they span the relevant space. ■

If two or three moments are equal, so that there is freedom in choosing the principal axes, then it is possible to pick a nonorthogonal group of them. We will, however, always choose ones that are orthogonal. So when we say “a set of principal axes,” we mean an orthonormal set.

**Theorem 9.6** *If a pancake object is symmetric under a rotation through an angle  $\theta \neq 180^\circ$  in the  $x$ - $y$  plane (such as a hexagon), then every axis in the  $x$ - $y$  plane (with the origin chosen to be the center of the symmetry rotation) is a principal axis with the same moment.*

**Proof:** Let  $\hat{\omega}_0$  be a principal axis in the plane, and let  $\hat{\omega}_\theta$  be the axis obtained by rotating  $\hat{\omega}_0$  through the angle  $\theta$ . Then  $\hat{\omega}_\theta$  is also a principal axis with the same principal moment, due to the symmetry of the object. Therefore,  $\mathbf{I}\hat{\omega}_0 = I\hat{\omega}_0$ , and  $\mathbf{I}\hat{\omega}_\theta = I\hat{\omega}_\theta$ .

Now, any vector  $\omega$  in the  $x$ - $y$  plane can be written as a linear combination of  $\hat{\omega}_0$  and  $\hat{\omega}_\theta$ , provided that  $\theta \neq 180^\circ$  (or zero, of course). That is,  $\hat{\omega}_0$  and  $\hat{\omega}_\theta$  span the  $x$ - $y$  plane. Therefore, any vector  $\omega$  can be written as  $\omega = a\hat{\omega}_0 + b\hat{\omega}_\theta$ , and so

$$\mathbf{I}\omega = \mathbf{I}(a\hat{\omega}_0 + b\hat{\omega}_\theta) = aI\hat{\omega}_0 + bI\hat{\omega}_\theta = I\omega. \quad (9.26)$$

Hence,  $\omega$  is also a principal axis. Problem 9.8 gives another proof of this theorem. ■

The theorem actually holds even without the “pancake” restriction. That is, it holds for any object with a rotational symmetry around the  $z$  axis (excluding  $\theta \neq 180^\circ$ ). This can be seen as follows. The  $z$  axis is a principal axis, because if  $\omega$  points along  $\hat{z}$ , then  $\mathbf{L}$  must also point along  $\hat{z}$ , by symmetry. There are therefore (at least) two principal axes in the  $x$ - $y$  plane. Label one of these as  $\hat{\omega}_0$  and proceed as above.

Let's now do some quick examples. We'll state the principal axes for the objects listed below (relative to the origin). Your task is to show that they

are correct. Usually, a quick symmetry argument shows that

$$\mathbf{I} \equiv \begin{pmatrix} \int (y^2 + z^2) & -\int xy & -\int zx \\ -\int xy & \int (z^2 + x^2) & -\int yz \\ -\int zx & -\int yz & \int (x^2 + y^2) \end{pmatrix} \quad (9.27)$$

![Figure 9.17: Five diagrams illustrating different mass distributions and their principal axes. 1. A point mass at the origin of a 2D coordinate system. 2. A point mass at (x0, y0) in a 2D coordinate system. 3. A rectangle centered at the origin of a 2D coordinate system with x and y axes labeled. 4. A cylinder with its central axis along the z-axis of a 3D coordinate system with x, y, and z axes labeled. 5. A square with one corner at the origin of a 2D coordinate system with x and y axes labeled.](5b8179677b985c3749136f8cfabfaf08_img.jpg)

Figure 9.17: Five diagrams illustrating different mass distributions and their principal axes. 1. A point mass at the origin of a 2D coordinate system. 2. A point mass at (x0, y0) in a 2D coordinate system. 3. A rectangle centered at the origin of a 2D coordinate system with x and y axes labeled. 4. A cylinder with its central axis along the z-axis of a 3D coordinate system with x, y, and z axes labeled. 5. A square with one corner at the origin of a 2D coordinate system with x and y axes labeled.

**Fig. 9.17**

is diagonal. In all of these examples (see Fig. 9.17), the origin for the principal axes is understood to be the origin of the given coordinate system (which is not necessarily the CM). In describing the axes, they therefore all pass through the origin, in addition to having the other properties stated.

**Example 1:** Point mass at the origin.

*principal axes:* any axes.

**Example 2:** Point mass at the point  $(x_0, y_0, z_0)$ .

*principal axes:* axis through point, any axes perpendicular to this.

**Example 3:** Rectangle centered at the origin, as shown.

*principal axes:* the  $x$ ,  $y$ , and  $z$  axes.

**Example 4:** Cylinder with axis as  $z$  axis.

*principal axes:*  $z$  axis, any axes in  $x$ - $y$  plane.

**Example 5:** Square with one corner at origin, as shown.

*principal axes:*  $z$  axis, axis through CM, axis perpendicular to this.

### 9.4 Two basic types of problems

The previous three sections introduced a variety of abstract concepts. We will now finally look at some actual physical systems. The concept of principal axes gives us the ability to solve many kinds of problems. Two kinds, however, come up again and again. There are variations on these, of course, but they may be generally stated as follows.

- Strike a rigid object with an impulsive (that is, quick) blow. What is the motion of the object immediately after the blow?
- An object rotates around a fixed axis. A given torque is applied. What is the frequency of the rotation? Or conversely, given the frequency, what is the required torque?

We'll work through an example for each of these problems. In both cases, the solution involves a few standard steps, so we'll write them out explicitly.

#### 9.4.1 Motion after an impulsive blow

**Problem:** Consider the rigid object in Fig. 9.18. Three masses are connected by three massless rods, in the shape of an isosceles right triangle with hypotenuse length  $4a$ . The mass at the right angle is  $2m$ , and the other two masses are  $m$ . Label them  $A$ ,  $B$ ,  $C$ , as shown. Assume that the object is floating freely in outer space. Mass  $B$  is struck with a quick blow, directed into the page. Let the imparted impulse have magnitude  $\int F dt = P$ . (See Section 8.6 for a discussion of impulse and angular impulse.) What are the velocities of the three masses immediately after the blow?

![Diagram of a rigid object in the shape of an isosceles right triangle. The vertices are labeled A, B, and C. Masses are m at A, m at B, and 2m at C. The hypotenuse AB has length 4a. A force F is applied at B, directed into the page (indicated by a circle with a cross).](9090b1fbae1125eafb0a32c9b66a3c96_img.jpg)

Diagram of a rigid object in the shape of an isosceles right triangle. The vertices are labeled A, B, and C. Masses are m at A, m at B, and 2m at C. The hypotenuse AB has length 4a. A force F is applied at B, directed into the page (indicated by a circle with a cross).

Fig. 9.18

**Solution:** Our strategy will be to find the angular momentum of the system (relative to the CM) using the angular impulse, and then calculate the principal moments and find the angular velocity vector (which will give the velocities relative to the CM), and then finally add on the CM motion.

The altitude from the right angle to the hypotenuse has length  $2a$ , and the CM is easily seen to be located at its midpoint (see Fig. 9.19). Picking the CM as our origin, and letting the plane of the paper be the  $x$ - $y$  plane, the positions of the three masses are  $\mathbf{r}_A = (-2a, -a, 0)$ ,  $\mathbf{r}_B = (2a, -a, 0)$ , and  $\mathbf{r}_C = (0, a, 0)$ . There are now five standard steps that we must perform.

![Diagram showing the center of mass (CM) of the triangle as the origin of a coordinate system. The CM is at the midpoint of the altitude from C to AB. The positions of the masses are given by vectors r_A, r_B, and r_C. The angular momentum vector L and the angular velocity vector omega are shown originating from the CM. The hypotenuse AB is divided into two segments of length 2a each by the altitude.](8b1caff14ee985416572228a5dc9b471_img.jpg)

Diagram showing the center of mass (CM) of the triangle as the origin of a coordinate system. The CM is at the midpoint of the altitude from C to AB. The positions of the masses are given by vectors r\_A, r\_B, and r\_C. The angular momentum vector L and the angular velocity vector omega are shown originating from the CM. The hypotenuse AB is divided into two segments of length 2a each by the altitude.

Fig. 9.19

- **Find  $\mathbf{L}$ :** The positive  $z$  axis is directed out of the page, so the impulse vector is  $\mathbf{P} \equiv \int \mathbf{F} dt = (0, 0, -P)$ . Therefore, the angular momentum of the system (relative to the CM) is

$$\begin{aligned} \mathbf{L} &= \int \boldsymbol{\tau} dt = \int (\mathbf{r}_B \times \mathbf{F}) dt = \mathbf{r}_B \times \int \mathbf{F} dt \\ &= (2a, -a, 0) \times (0, 0, -P) = aP(1, 2, 0), \end{aligned} \quad (9.28)$$

as shown in Fig. 9.19. We have used the fact that  $\mathbf{r}_B$  is essentially constant during the blow (because the blow is assumed to happen very quickly) in taking  $\mathbf{r}_B$  outside the integral.

- **Calculate the principal moments:** The principal axes are the  $x$ ,  $y$ , and  $z$  axes, because the symmetry of the triangle makes  $\mathbf{I}$  diagonal in this basis, as you can quickly check. The moments (relative to the CM) are

$$\begin{aligned} I_x &= ma^2 + ma^2 + (2m)a^2 = 4ma^2, \\ I_y &= m(2a)^2 + m(2a)^2 + (2m)0^2 = 8ma^2, \\ I_z &= I_x + I_y = 12ma^2. \end{aligned} \quad (9.29)$$

We have used the perpendicular-axis theorem to obtain  $I_z$ , although it won't be needed to solve the problem.

- **Find  $\boldsymbol{\omega}$ :** We now have two expressions for the angular momentum of the system. One expression is in terms of the given impulse, Eq. (9.28). The other is in terms of the

moments and the angular velocity components, Eq. (9.24). Equating these gives

$$\begin{aligned} (I_x\omega_x, I_y\omega_y, I_z\omega_z) &= aP(1, 2, 0) \\ \implies (4ma^2\omega_x, 8ma^2\omega_y, 12ma^2\omega_z) &= aP(1, 2, 0) \\ \implies (\omega_x, \omega_y, \omega_z) &= \frac{P}{4ma}(1, 1, 0), \end{aligned} \quad (9.30)$$

as shown in Fig. 9.19.

- **Calculate the velocities relative to the CM:** Right after the blow, the object rotates around the CM with the angular velocity found in Eq. (9.30). The velocities relative to the CM are then  $\mathbf{u}_i = \boldsymbol{\omega} \times \mathbf{r}_i$ . Thus,

$$\begin{aligned} \mathbf{u}_A &= \boldsymbol{\omega} \times \mathbf{r}_A = \frac{P}{4ma}(1, 1, 0) \times (-2a, -a, 0) = (0, 0, P/4m), \\ \mathbf{u}_B &= \boldsymbol{\omega} \times \mathbf{r}_B = \frac{P}{4ma}(1, 1, 0) \times (2a, -a, 0) = (0, 0, -3P/4m), \\ \mathbf{u}_C &= \boldsymbol{\omega} \times \mathbf{r}_C = \frac{P}{4ma}(1, 1, 0) \times (0, a, 0) = (0, 0, P/4m). \end{aligned} \quad (9.31)$$

As a check, it makes sense that  $\mathbf{u}_B$  is three times as large as  $\mathbf{u}_A$  and  $\mathbf{u}_C$ , because  $B$  is three times as far from the axis of rotation as  $A$  and  $C$  are, as you can verify by doing a little geometry in Fig. 9.19.

- **Add on the velocity of the CM:** The impulse (that is, the change in linear momentum) supplied to the whole system is  $\mathbf{P} = (0, 0, -P)$ . The total mass of the system is  $M = 4m$ . Therefore, the velocity of the CM is

$$V_{\text{CM}} = \frac{\mathbf{P}}{M} = (0, 0, -P/4m). \quad (9.32)$$

The total velocities of the masses are therefore

$$\begin{aligned} \mathbf{v}_A &= \mathbf{u}_A + V_{\text{CM}} = (0, 0, 0), \\ \mathbf{v}_B &= \mathbf{u}_B + V_{\text{CM}} = (0, 0, -P/m), \\ \mathbf{v}_C &= \mathbf{u}_C + V_{\text{CM}} = (0, 0, 0). \end{aligned} \quad (9.33)$$

##### REMARKS:

1. We see that masses  $A$  and  $C$  are instantaneously at rest immediately after the blow, and mass  $B$  acquires all of the imparted impulse. In retrospect, this is clear. Basically, it is possible for both  $A$  and  $C$  to remain at rest while  $B$  moves a tiny bit, so this is what happens. If  $B$  moves into the page by a small distance  $\epsilon$ , then  $A$  and  $C$  won't know that  $B$  has moved, because their distances to  $B$  will change (assuming hypothetically that they don't move) by a distance of order only  $\epsilon^2$ . If we changed the problem and added a mass  $D$  at, say, the midpoint of the hypotenuse, then it would *not* be possible for  $A$ ,  $C$ , and  $D$  to remain at rest while  $B$  moved a tiny bit. So there would have to be some other motion in addition to  $B$ 's. This setup is the topic of Exercise 9.38.
2. As time goes on, the system undergoes a rather complicated motion. What happens is that the CM moves with constant velocity while the masses rotate around it in

- a messy manner. Since there are no torques acting on the system (after the initial blow), we know that  $\mathbf{L}$  forever remains constant. It turns out that  $\boldsymbol{\omega}$  moves around  $\mathbf{L}$  while the masses rotate around this changing  $\boldsymbol{\omega}$ . These matters are the subject of Section 9.6, although in that discussion we restrict ourselves to symmetric tops, that is, ones with two equal moments. But these issues aside, it's good to know that we can, without too much difficulty, determine what's going on immediately after the blow.
- 3. The object in this problem was assumed to be floating freely in space. If we instead have an object that is pivoted at a given fixed point, then we should use this pivot as our origin. There is then no need to perform the last step of adding on the velocity of the origin (which was the CM, above), because this velocity is now zero. Equivalently, just consider the pivot to be an infinite mass, which is therefore the location of the (motionless) CM. ♣

#### 9.4.2 Frequency of motion due to a torque

**Problem:** Consider a stick of length  $\ell$ , mass  $m$ , and uniform mass density. The stick is pivoted at its top end and swings around the vertical axis. Assume that conditions have been set up so that the stick always makes an angle  $\theta$  with the vertical, as shown in Fig. 9.20. What is the frequency,  $\omega$ , of this motion?

**Solution:** Our strategy will be to find the principal moments and then the angular momentum of the system (in terms of  $\omega$ ), and then find the rate of change of  $\mathbf{L}$ , and then calculate the torque and equate it with  $d\mathbf{L}/dt$ . We will choose the pivot to be the origin.<sup>8</sup> Again, there are five standard steps that we must perform.

- **Calculate the principal moments:** The principal axes are the axis along the stick, along with any two orthogonal axes perpendicular to the stick. So let the  $x$  and  $y$  axes be as shown in Fig. 9.21. The positive  $z$  axis then points out of the page. The moments (relative to the pivot) are  $I_x = m\ell^2/3$ ,  $I_y = 0$ , and  $I_z = m\ell^2/3$  (which won't be needed).
- **Find  $\mathbf{L}$ :** The angular velocity vector points vertically (however, see the third remark following this solution), so in the basis of the principal axes, the angular velocity vector is  $\boldsymbol{\omega} = (\omega \sin \theta, \omega \cos \theta, 0)$ , where  $\omega$  is yet to be determined. The angular momentum of the system (relative to the pivot) is therefore

$$\mathbf{L} = (I_x \omega_x, I_y \omega_y, I_z \omega_z) = ((1/3)m\ell^2 \omega \sin \theta, 0, 0). \quad (9.34)$$

- **Find  $d\mathbf{L}/dt$ :** The vector  $\mathbf{L}$  in Eq. (9.34) points up to the right, along the  $x$  axis (at the instant shown in Fig. 9.21), with magnitude  $L = (1/3)m\ell^2 \omega \sin \theta$ . As the stick rotates around the vertical axis,  $\mathbf{L}$  traces out the surface of a cone. That is, the tip of  $\mathbf{L}$  traces out a horizontal circle. The radius of this circle is the horizontal component of  $\mathbf{L}$ , which is  $L \cos \theta$ . The speed of the tip (which is the magnitude of  $d\mathbf{L}/dt$ ) is therefore

<sup>8</sup> This is a better choice than the CM because this way we won't have to worry about any messy forces acting at the pivot when computing the torque. The task of Exercise 9.41 is to work through the more complicated solution which has the CM as the origin.

![Diagram of a stick pivoted at its top end, making an angle theta with the vertical. The stick has length l and mass m. The angular velocity vector omega is shown as a vertical arrow with a question mark, indicating it is to be determined. The stick is shown in a dashed position to indicate rotation around the vertical axis.](d8a0cdda53eaca3084eb26f1302fcde9_img.jpg)

Diagram of a stick pivoted at its top end, making an angle theta with the vertical. The stick has length l and mass m. The angular velocity vector omega is shown as a vertical arrow with a question mark, indicating it is to be determined. The stick is shown in a dashed position to indicate rotation around the vertical axis.

Fig. 9.20

![Diagram showing the angular momentum vector L and the angular velocity vector omega. The stick is pivoted at the origin, making an angle theta with the vertical. The angular velocity vector omega is vertical. The angular momentum vector L is horizontal, pointing along the x-axis. The stick is shown in a dashed position to indicate rotation around the vertical axis. The x and y axes are shown, with the x-axis pointing out of the page.](7ca14003ae9fcb608c41942cc3aa7641_img.jpg)

Diagram showing the angular momentum vector L and the angular velocity vector omega. The stick is pivoted at the origin, making an angle theta with the vertical. The angular velocity vector omega is vertical. The angular momentum vector L is horizontal, pointing along the x-axis. The stick is shown in a dashed position to indicate rotation around the vertical axis. The x and y axes are shown, with the x-axis pointing out of the page.

Fig. 9.21

$(L \cos \theta) \omega$ , because  $\mathbf{L}$  rotates around the vertical axis with the same frequency as the stick. So  $d\mathbf{L}/dt$  has magnitude

$$\left| \frac{d\mathbf{L}}{dt} \right| = (L \cos \theta) \omega = \frac{1}{3} m \ell^2 \omega^2 \sin \theta \cos \theta, \quad (9.35)$$

and it points into the page.

REMARK: With more complicated objects where  $I_y \neq 0$ ,  $\mathbf{L}$  won't point nicely along a principal axis, so the length of its horizontal component (the radius of the circle that  $\mathbf{L}$  traces out) won't immediately be obvious. In this case, you can either explicitly calculate the horizontal component (see the spinning-top example in Section 9.7.5), or you can just do things the formal way by finding the rate of change of  $\mathbf{L}$  via the expression  $d\mathbf{L}/dt = \boldsymbol{\omega} \times \mathbf{L}$ , which holds for all the same reasons that  $\mathbf{v} \equiv d\mathbf{r}/dt = \boldsymbol{\omega} \times \mathbf{r}$  holds. In the present problem, we obtain

$$\begin{aligned} d\mathbf{L}/dt &= (\omega \sin \theta, \omega \cos \theta, 0) \times ((1/3)m\ell^2\omega \sin \theta, 0, 0) \\ &= (0, 0, -(1/3)m\ell^2\omega^2 \sin \theta \cos \theta), \end{aligned} \quad (9.36)$$

in agreement with Eq. (9.35). And the direction is correct, because the negative  $z$  axis points into the page. Note that we calculated this cross product in the principal-axis basis. Although these axes are changing in time, they present a perfectly good set of basis vectors at any instant. ♣

- **Calculate the torque:** The torque (relative to the pivot) is due to gravity, which effectively acts on the CM of the stick. So  $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$  has magnitude

$$\tau = rF \sin \theta = (\ell/2)(mg) \sin \theta, \quad (9.37)$$

and it points into the page.

- **Equate  $\boldsymbol{\tau}$  with  $d\mathbf{L}/dt$ :** The vectors  $d\mathbf{L}/dt$  and  $\boldsymbol{\tau}$  both point into the page, which is good, because they had better point in the same direction. Equating their magnitudes gives

$$\frac{m\ell^2\omega^2 \sin \theta \cos \theta}{3} = \frac{mg\ell \sin \theta}{2} \implies \omega = \sqrt{\frac{3g}{2\ell \cos \theta}}. \quad (9.38)$$

![Diagram of a stick of length l pivoted at one end, making an angle theta with the vertical. The stick is rotating with angular velocity omega around the vertical axis. A dashed circle of radius l sin theta shows the path of the tip of the stick. A vector omega' is shown perpendicular to the stick, representing an instantaneous rotation around an axis through the pivot.](4a718e0366bbb7088e20f347831b8297_img.jpg)

Diagram of a stick of length l pivoted at one end, making an angle theta with the vertical. The stick is rotating with angular velocity omega around the vertical axis. A dashed circle of radius l sin theta shows the path of the tip of the stick. A vector omega' is shown perpendicular to the stick, representing an instantaneous rotation around an axis through the pivot.

Fig. 9.22

REMARKS:

1. This frequency is slightly larger than the frequency that would arise if we instead had a mass on the end of a massless stick of length  $\ell$ . From Problem 9.12, the frequency in that case is  $\sqrt{g/\ell \cos \theta}$ . So, in some sense, a uniform stick of length  $\ell$  behaves like a mass on the end of a massless stick of length  $2\ell/3$ , as far as these rotations are concerned.
2. As  $\theta \rightarrow \pi/2$ , the frequency goes to  $\infty$ , which makes sense. And as  $\theta \rightarrow 0$ , it approaches  $\sqrt{3g/2\ell}$ , which isn't so obvious.
3. As explained in Problem 9.1, the instantaneous  $\boldsymbol{\omega}$  is not uniquely defined in some situations. At the instant shown in Fig. 9.20, the stick is moving directly into the page. What if someone else wants to think of the stick as (instantaneously) rotating around the  $\boldsymbol{\omega}'$  axis perpendicular to the stick (the  $x$  axis, in the above notation), instead of the vertical axis, as shown in Fig. 9.22. What is the angular speed  $\omega'$ ?

Well, if  $\omega$  is the angular speed of the stick around the vertical axis, then we may view the tip of the stick as instantaneously moving in a circle of radius  $\ell \sin \theta$  around the

vertical axis  $\omega$ . So  $\omega(\ell \sin \theta)$  is the speed of the tip of the stick. But we may also view the tip of the stick as instantaneously moving in a circle of radius  $\ell$  around  $\omega'$ , as shown. The speed of the tip is still  $\omega(\ell \sin \theta)$ , so the angular speed around this axis is given by  $\omega' \ell = \omega(\ell \sin \theta)$ . Hence  $\omega' = \omega \sin \theta$ , which is simply the  $x$  component of  $\omega$  that we found above, right before Eq. (9.34). The moment of inertia around  $\omega'$  is  $m\ell^2/3$ , so the angular momentum has magnitude  $(m\ell^2/3)(\omega \sin \theta)$ , in agreement with Eq. (9.34). And the direction is along the  $x$  axis, as it should be.

Note that although  $\omega$  is not uniquely defined at any instant,  $\mathbf{L} \equiv \int (\mathbf{r} \times \mathbf{p}) dm$  certainly is.<sup>9</sup> Choosing  $\omega$  to point vertically, as we did in the above solution, is in some sense the natural choice, because this  $\omega$  doesn't change with time. ♣

### 9.5 Euler's equations

Consider a rigid body instantaneously rotating around an axis  $\omega$ . This  $\omega$  may change as time goes on, but all we care about for now is what it is at a given instant. The angular momentum is given by Eq. (9.8) as  $\mathbf{L} = \mathbf{I}\omega$ , where  $\mathbf{I}$  is the inertia tensor, calculated with respect to a given origin and a given set of axes (and  $\omega$  is written in the same basis, of course).

As usual, things are much nicer if we use the principal axes (relative to the chosen origin) as the basis vectors of our coordinate system. Since these axes are fixed with respect to the rotating object, they will rotate with respect to the fixed reference frame. In this basis,  $\mathbf{L}$  takes the nice form,

$$\mathbf{L} = (I_1\omega_1, I_2\omega_2, I_3\omega_3), \quad (9.39)$$

where  $\omega_1$ ,  $\omega_2$ , and  $\omega_3$  are the components of  $\omega$  along the principal axes. In other words, if you take the vector  $\mathbf{L}$  in space and project it onto the instantaneous principal axes, then you get the components in Eq. (9.39).

On one hand, writing  $\mathbf{L}$  in terms of the rotating principal axes allows us to write it in the nice form of Eq. (9.39). But on the other hand, writing  $\mathbf{L}$  in this way makes it nontrivial to determine how it changes in time, because the principal axes themselves are changing. However, it turns out that the benefits outweigh the detriments, so we will invariably use the principal axes as our basis vectors.

The goal of this section is to find an expression for  $d\mathbf{L}/dt$ , and to then equate this with the torque. The result will be Euler's equations in Eq. (9.45).

#### Derivation of Euler's equations

If we write  $\mathbf{L}$  in terms of the body frame, which we'll choose to be described by the principal axes painted on the body, then  $\mathbf{L}$  can change (relative to the lab frame) due to two effects. It can change because its coordinates in the body frame change, and it can also change because of the rotation of the body frame. To be precise, let  $\mathbf{L}_0$  be the vector  $\mathbf{L}$  at a given instant. At this instant, imagine painting the vector  $\mathbf{L}_0$  onto the body frame, so that  $\mathbf{L}_0$  then rotates with the body. The rate

<sup>9</sup> The nonuniqueness of  $\omega$  arises from the fact that  $I_y = 0$  here. If all the moments are nonzero, then  $(L_x, L_y, L_z) = (I_x\omega_x, I_y\omega_y, I_z\omega_z)$  uniquely determines  $\omega$ , given  $\mathbf{L}$ .

of change of  $\mathbf{L}$  with respect to the lab frame may be written in the (identically true) way,

$$\frac{d\mathbf{L}}{dt} = \frac{d(\mathbf{L} - \mathbf{L}_0)}{dt} + \frac{d\mathbf{L}_0}{dt}. \quad (9.40)$$

The second term here is simply the rate of change of a body-fixed vector, which we know is  $\boldsymbol{\omega} \times \mathbf{L}_0$ , which equals  $\boldsymbol{\omega} \times \mathbf{L}$  at this instant. The first term is the rate of change of  $\mathbf{L}$  with respect to the body frame, which we'll denote by  $\delta\mathbf{L}/\delta t$ . This is what someone standing fixed on the body measures. So we end up with

$$\frac{d\mathbf{L}}{dt} = \frac{\delta\mathbf{L}}{\delta t} + \boldsymbol{\omega} \times \mathbf{L}. \quad (9.41)$$

This is actually a general statement, true for any vector in any rotating frame (we'll derive it in another more mathematical way in Chapter 10). There was nothing particular about  $\mathbf{L}$  that we used in the above derivation. Also, there was no need to restrict ourselves to principal axes. In words, what we've shown is that the total change equals the change relative to the rotating frame, plus the change of the rotating frame relative to the fixed frame. This is just the usual way of adding velocities when one frame moves with respect to another.

Let us now make use of our choice of the principal axes as the body axes. This will put Eq. (9.41) in a usable form. Using Eq. (9.39), we can rewrite Eq. (9.41) as

$$\frac{d\mathbf{L}}{dt} = \frac{d}{dt}(I_1\omega_1, I_2\omega_2, I_3\omega_3) + (\omega_1, \omega_2, \omega_3) \times (I_1\omega_1, I_2\omega_2, I_3\omega_3). \quad (9.42)$$

The  $\delta\mathbf{L}/\delta t$  term does indeed equal  $(d/dt)(I_1\omega_1, I_2\omega_2, I_3\omega_3)$ , because someone in the body frame measures the components of  $\mathbf{L}$  with respect to the principal axes to be  $(I_1\omega_1, I_2\omega_2, I_3\omega_3)$ . And  $\delta\mathbf{L}/\delta t$  is by definition the rate at which these components change.

Equation (9.42) equates two vectors. As is true for any vector, these (equal) vectors have an existence that is independent of the coordinate system we choose to describe them with (Eq. (9.41) makes no reference to a coordinate system). But since we've chosen an explicit frame on the right-hand side of Eq. (9.42), we should choose the same frame for the left-hand side. We can then equate the components on the left with the components on the right. Projecting  $d\mathbf{L}/dt$  onto the instantaneous principal axes, we have

$$\begin{aligned} \left( \left( \frac{d\mathbf{L}}{dt} \right)_1, \left( \frac{d\mathbf{L}}{dt} \right)_2, \left( \frac{d\mathbf{L}}{dt} \right)_3 \right) &= \frac{d}{dt}(I_1\omega_1, I_2\omega_2, I_3\omega_3) \\ &\quad + (\omega_1, \omega_2, \omega_3) \times (I_1\omega_1, I_2\omega_2, I_3\omega_3). \end{aligned} \quad (9.43)$$

**REMARK:** The left-hand side looks nastier than it really is. The reason we've written it in this cumbersome way is the following (this is a remark that has to be read very slowly). We

could have written the left-hand side as  $(d/dt)(L_1, L_2, L_3)$ , but this might cause confusion as to whether the  $L_i$  refer to the components with respect to the rotating axes, or the components with respect to the fixed set of axes that coincide with the rotating principal axes at this instant. That is, do we project  $\mathbf{L}$  onto the principal axes to obtain components, and then take the derivative of these components? Or do we take the derivative of  $\mathbf{L}$  and then project onto the principal axes to obtain components? The latter is what we mean in Eq. (9.43).<sup>10</sup> The way we've written the left-hand side of Eq. (9.43), it's clear that we're taking the derivative first. We are, after all, simply projecting Eq. (9.41) onto the principal axes. ♣

The time derivatives on the right-hand side of Eq. (9.43) are  $d(I_1\omega_1)/dt = I_1\dot{\omega}_1$ , etc., because the  $I$ 's are constant. Performing the cross product and equating the corresponding components on each side yields the three equations,

$$\begin{aligned}\left(\frac{d\mathbf{L}}{dt}\right)_1 &= I_1\dot{\omega}_1 + (I_3 - I_2)\omega_3\omega_2, \\ \left(\frac{d\mathbf{L}}{dt}\right)_2 &= I_2\dot{\omega}_2 + (I_1 - I_3)\omega_1\omega_3, \\ \left(\frac{d\mathbf{L}}{dt}\right)_3 &= I_3\dot{\omega}_3 + (I_2 - I_1)\omega_2\omega_1.\end{aligned}\tag{9.44}$$

We will now invoke the results of Section 8.4.3 to say that if we have chosen the origin of our rotating frame to be either a fixed point or the CM (as we always do), then we can equate  $d\mathbf{L}/dt$  with the torque,  $\boldsymbol{\tau}$ . We therefore have

$$\begin{aligned}\tau_1 &= I_1\dot{\omega}_1 + (I_3 - I_2)\omega_3\omega_2, \\ \tau_2 &= I_2\dot{\omega}_2 + (I_1 - I_3)\omega_1\omega_3, \\ \tau_3 &= I_3\dot{\omega}_3 + (I_2 - I_1)\omega_2\omega_1.\end{aligned}\tag{9.45}$$

These are *Euler's equations*. You need to remember only one of them, because the other two can be obtained by cyclic permutation of the indices.

#### REMARKS:

1. We repeat that the left- and right-hand sides of Eqs. (9.45) are components that are measured with respect to the instantaneous principal axes. Let's say we do a problem, for example, where  $\tau_3$  has a constant nonzero value, and  $\tau_1$  and  $\tau_2$  are always zero (as in the example in Section 9.4.2). This doesn't mean that  $\boldsymbol{\tau}$  is a constant vector. On the contrary,  $\boldsymbol{\tau}$  always points along the  $\hat{\mathbf{x}}_3$  vector in the rotating frame, but this vector is changing in the fixed frame (unless  $\hat{\mathbf{x}}_3$  points along  $\boldsymbol{\omega}$ ).
2. The two types of terms on the right-hand sides of Eqs. (9.44) are the two types of changes that  $\mathbf{L}$  can undergo.  $\mathbf{L}$  can change because its components with respect to the rotating frame change, and  $\mathbf{L}$  can also change because the body is rotating around  $\boldsymbol{\omega}$ .

<sup>10</sup> The former is  $\delta\mathbf{L}/\delta t$ , by definition. The two interpretations certainly give different results. For example, if instead of  $\mathbf{L}$  we consider a vector fixed in the body (such as the  $\mathbf{L}_0$  above), then the first interpretation gives a zero result, whereas the second interpretation gives a nonzero result. Considering what we mean by, say, the vector  $(\omega_1, \omega_2, \omega_3)$ , I think that the more logical interpretation of  $(d/dt)(L_1, L_2, L_3)$  is the first one, so it should definitely be avoided.

3. Section 9.6.1 on the free symmetric top (viewed from the body frame) provides a good example of the use of Euler's equations. Another interesting application is the famed "Tennis racket theorem" (Problem 9.14).
4. It should be noted that you never *have* to use Euler's equations. You can simply start from scratch and use Eq. (9.41) each time you solve a problem. The point is that we've done the calculation of  $d\mathbf{L}/dt$  once and for all, so you can just invoke the result in Eqs. (9.45). ♣

### 9.6 Free symmetric top

The free symmetric top is the classic example of an application of Euler's equations. Consider an object that has two of its principal moments equal, with the CM as the origin. Assume that the object is in outer space, far from any external forces. We will choose the object to have cylindrical symmetry around some axis (see Fig. 9.23), although this is not necessary; a square cross section, for example, would yield two equal moments. The principal axes are then the symmetry axis and any two orthogonal axes in the cross-section plane through the CM. Let the symmetry axis be chosen as the  $\hat{\mathbf{x}}_3$  axis. Then the moments are  $I_1 = I_2 \equiv I$ , and  $I_3$ .

![Diagram of a symmetric top with cylindrical symmetry. The center of mass (CM) is marked with a dot. A vertical axis passing through the CM is labeled x_3. The top has a bulbous shape with a dashed line indicating the cross-section plane.](08ef27a0c033801d77827151aa2d6576_img.jpg)

Diagram of a symmetric top with cylindrical symmetry. The center of mass (CM) is marked with a dot. A vertical axis passing through the CM is labeled x\_3. The top has a bulbous shape with a dashed line indicating the cross-section plane.

Fig. 9.23

We'll first look at things from the point of view of someone standing at rest on the body, and then we'll look at things from the point of view of someone standing at rest in an inertial frame. The mathematics involved here isn't so bad, but as with most types of top problems, it's hard to get an intuitive feel for what all the various vectors are doing. And the intuition is even more difficult in the following body-frame analysis because of the noninertial frame of reference. But let's see what we find.

#### 9.6.1 View from the body frame

Plugging  $I_1 = I_2 \equiv I$  into Euler's equations in Eq. (9.45), and using the fact that all the  $\tau_i$  are zero (since there are no torques, because the top is "free"), we have

$$\begin{aligned} 0 &= I\dot{\omega}_1 + (I_3 - I)\omega_3\omega_2, \\ 0 &= I\dot{\omega}_2 + (I - I_3)\omega_1\omega_3, \\ 0 &= I_3\dot{\omega}_3. \end{aligned} \quad (9.46)$$

The last equation says that  $\omega_3$  is constant. If we then define

$$\Omega \equiv \left( \frac{I_3 - I}{I} \right) \omega_3, \quad (9.47)$$

the first two equations become

$$\dot{\omega}_1 + \Omega\omega_2 = 0, \quad \text{and} \quad \dot{\omega}_2 - \Omega\omega_1 = 0. \quad (9.48)$$

Taking the derivative of the first of these, and then using the second to eliminate  $\dot{\omega}_2$ , gives

$$\ddot{\omega}_1 + \Omega^2\omega_1 = 0, \quad (9.49)$$

and likewise for  $\omega_2$ . This is a good old simple-harmonic-oscillator equation. We can therefore write  $\omega_1(t)$  as, say, a cosine. And then Eq. (9.48) yields a sine for  $\omega_2(t)$ . So we have

$$\omega_1(t) = A \cos(\Omega t + \phi), \quad \omega_2(t) = A \sin(\Omega t + \phi). \quad (9.50)$$

We see that  $\omega_1(t)$  and  $\omega_2(t)$  are the components of a circle in the body frame. Therefore, the  $\boldsymbol{\omega}$  vector traces out a cone around  $\hat{\mathbf{x}}_3$  (see Fig. 9.24), with frequency  $\Omega$ , as viewed by someone standing on the body. This frequency  $\Omega$  in Eq. (9.47) depends on the value of  $\omega_3$  and on the geometry of the object (through  $I_3$  and  $I$ ). But the radius,  $A$ , of the  $\boldsymbol{\omega}$  cone is determined by the initial values of  $\omega_1$  and  $\omega_2$ .

The angular momentum is

$$\mathbf{L} = (I_1\omega_1, I_2\omega_2, I_3\omega_3) = (IA \cos(\Omega t + \phi), IA \sin(\Omega t + \phi), I_3\omega_3), \quad (9.51)$$

so  $\mathbf{L}$  also traces out a cone around  $\hat{\mathbf{x}}_3$  with frequency  $\Omega$ , as viewed by someone standing on the body. This is shown in Fig. 9.24 for the case  $\Omega > 0$  (that is,  $I_3 > I$ ). In this case,  $I_3 > I$  implies  $L_3/L_2 > \omega_3/\omega_2$ , so the  $\mathbf{L}$  vector lies above the  $\boldsymbol{\omega}$  vector (that is, between  $\boldsymbol{\omega}$  and  $\hat{\mathbf{x}}_3$ ). An object with  $I_3 > I$ , such as a coin, is called an *oblate* top.

Figure 9.25 shows the case where  $\Omega < 0$  (that is,  $I_3 < I$ ). In this case,  $I_3 < I$  implies  $L_3/L_2 < \omega_3/\omega_2$ , so the  $\mathbf{L}$  vector lies below the  $\boldsymbol{\omega}$  vector, as shown. And since  $\Omega$  is negative, the  $\boldsymbol{\omega}$  and  $\mathbf{L}$  vectors precess around  $\hat{\mathbf{x}}_3$  in the opposite direction (clockwise, as viewed from above). An object with  $I_3 < I$ , such as a carrot, is called a *prolate* top.

![Figure 9.24: A 3D diagram showing the precession of the angular momentum vector L and the angular velocity vector omega around the x3 axis in the body frame. The x3 axis is vertical, and the x1 and x2 axes form a horizontal plane. The vector omega traces a cone around the x3 axis. The vector L also traces a cone around the x3 axis, but it is at a larger angle from the x3 axis than omega, indicating that L3/L2 > omega3/omega2. The diagram is labeled 'view from body frame, Omega > 0 (I3 > I)'.](61e9d7cb6966a0f28c704edcd7f0a23d_img.jpg)

Figure 9.24: A 3D diagram showing the precession of the angular momentum vector L and the angular velocity vector omega around the x3 axis in the body frame. The x3 axis is vertical, and the x1 and x2 axes form a horizontal plane. The vector omega traces a cone around the x3 axis. The vector L also traces a cone around the x3 axis, but it is at a larger angle from the x3 axis than omega, indicating that L3/L2 > omega3/omega2. The diagram is labeled 'view from body frame, Omega > 0 (I3 > I)'.

Fig. 9.24

![Figure 9.25: A 3D diagram showing the precession of the angular momentum vector L and the angular velocity vector omega around the x3 axis in the body frame. The x3 axis is vertical, and the x1 and x2 axes form a horizontal plane. The vector omega traces a cone around the x3 axis. The vector L also traces a cone around the x3 axis, but it is at a smaller angle from the x3 axis than omega, indicating that L3/L2 < omega3/omega2. The diagram is labeled 'view from body frame, Omega < 0 (I3 < I)'.](77dd80146a91d4dca1e071cac711adad_img.jpg)

Figure 9.25: A 3D diagram showing the precession of the angular momentum vector L and the angular velocity vector omega around the x3 axis in the body frame. The x3 axis is vertical, and the x1 and x2 axes form a horizontal plane. The vector omega traces a cone around the x3 axis. The vector L also traces a cone around the x3 axis, but it is at a smaller angle from the x3 axis than omega, indicating that L3/L2 < omega3/omega2. The diagram is labeled 'view from body frame, Omega < 0 (I3 < I)'.

Fig. 9.25

**Example (The earth):** Let's consider the earth to be our top. Then  $\omega_3 \approx 2\pi/(1 \text{ day})$ .<sup>11</sup> The bulge at the equator (caused by the spinning of the earth) makes  $I_3$  slightly larger than  $I$ , and it turns out that  $(I_3 - I)/I \approx 1/320$ . Therefore, Eq. (9.47) gives  $\Omega \approx (1/320) 2\pi/(1 \text{ day})$ . So the  $\boldsymbol{\omega}$  vector should precess around in its cone once every 320 days, as viewed by someone on the earth. The true value is more like 430 days. The difference has to do with various things, including the nonrigidity of the earth, but at least we got an answer in the right ballpark. This precession of  $\boldsymbol{\omega}$  is known as the “Chandler wobble.”

In practice, how can we determine the direction of  $\boldsymbol{\omega}$ ? Simply take an extended-time photograph exposure at night. The stars will form arcs of circles. At the center of all these circles is a point that doesn't move. This is the direction of  $\boldsymbol{\omega}$ . Fortunately,  $\Omega$  is much smaller than  $\omega$ , so the  $\boldsymbol{\omega}$  vector doesn't change much during an exposure time of, say, an hour. So the center of the circles is essentially well defined.

How big is the  $\boldsymbol{\omega}$  cone, for the earth? Equivalently, what is the value of  $A$  in Eq. (9.50)? Observation has shown that the  $\boldsymbol{\omega}$  vector pierces the earth at a point on

<sup>11</sup> This isn't quite correct, since the earth rotates 366 times for every 365 days, due to the motion around the sun, but it's close enough for the purposes here.

the order of 10 m from the north pole, although this distance fluctuates over time.<sup>12</sup> Hence,  $A/\omega_3 \approx (10 \text{ m})/R_E$ . The half-angle of the  $\boldsymbol{\omega}$  cone is therefore on the order of only  $10^{-4}$  degrees. So if you use an extended-time photograph exposure one night to see which point in the sky stands still, and then if you do the same thing 200 nights later, you probably won't be able to tell that they're really two different points.

#### 9.6.2 View from a fixed frame

Let's now see what our symmetric top looks like from a fixed frame. Euler's equations won't help much here, because they deal with the components of  $\boldsymbol{\omega}$  in the body frame. But fortunately we can solve for the motion from scratch. In terms of the (changing) principal axes,  $\hat{\mathbf{x}}_1$ ,  $\hat{\mathbf{x}}_2$ ,  $\hat{\mathbf{x}}_3$ , we have

$$\begin{aligned}\boldsymbol{\omega} &= (\omega_1 \hat{\mathbf{x}}_1 + \omega_2 \hat{\mathbf{x}}_2) + \omega_3 \hat{\mathbf{x}}_3, \\ \mathbf{L} &= I(\omega_1 \hat{\mathbf{x}}_1 + \omega_2 \hat{\mathbf{x}}_2) + I_3 \omega_3 \hat{\mathbf{x}}_3.\end{aligned}\quad (9.52)$$

Eliminating the  $(\omega_1 \hat{\mathbf{x}}_1 + \omega_2 \hat{\mathbf{x}}_2)$  term from these equations gives (in terms of the  $\Omega$  defined in Eq. (9.47))

$$\mathbf{L} = I(\boldsymbol{\omega} + \Omega \hat{\mathbf{x}}_3) \implies \boldsymbol{\omega} = \frac{L}{I} \hat{\mathbf{L}} - \Omega \hat{\mathbf{x}}_3, \quad (9.53)$$

![Diagram Fig. 9.26: View from a fixed frame for an oblate top (I3 > I, Omega > 0). A vertical vector L is shown. A vector omega precesses around L, forming a cone. A vector x3_hat is also shown, precessing around L. The vectors L, omega, and x3_hat are coplanar. The text 'view from fixed frame, Omega > 0 (I3 > I)' is below the diagram.](f7ab91e8973927a189e6ee2f0ec55bb0_img.jpg)

Diagram Fig. 9.26: View from a fixed frame for an oblate top (I3 > I, Omega > 0). A vertical vector L is shown. A vector omega precesses around L, forming a cone. A vector x3\_hat is also shown, precessing around L. The vectors L, omega, and x3\_hat are coplanar. The text 'view from fixed frame, Omega > 0 (I3 > I)' is below the diagram.

Fig. 9.26

where  $L = |\mathbf{L}|$ , and  $\hat{\mathbf{L}}$  is the unit vector in the  $\mathbf{L}$  direction. The linear relationship among  $\mathbf{L}$ ,  $\boldsymbol{\omega}$ , and  $\hat{\mathbf{x}}_3$  implies that these three vectors lie in a plane. But  $\mathbf{L}$  remains fixed, because there are no torques on the system. Therefore,  $\boldsymbol{\omega}$  and  $\hat{\mathbf{x}}_3$  precess (as we'll see below) around  $\mathbf{L}$ , with the three vectors always coplanar. See Fig. 9.26 for the case  $\Omega > 0$ , that is,  $I_3 > I$  (an oblate top), and Fig. 9.27 for the case  $\Omega < 0$ , that is,  $I_3 < I$  (a prolate top).

What is the frequency of this precession, as viewed from the fixed frame? The rate of change of  $\hat{\mathbf{x}}_3$  is  $\boldsymbol{\omega} \times \hat{\mathbf{x}}_3$ , because  $\hat{\mathbf{x}}_3$  is fixed in the body frame, so its change comes only from rotation around  $\boldsymbol{\omega}$ . Therefore, Eq. (9.53) gives

$$\frac{d\hat{\mathbf{x}}_3}{dt} = \left( \frac{L}{I} \hat{\mathbf{L}} - \Omega \hat{\mathbf{x}}_3 \right) \times \hat{\mathbf{x}}_3 = \left( \frac{L}{I} \hat{\mathbf{L}} \right) \times \hat{\mathbf{x}}_3. \quad (9.54)$$

![Diagram Fig. 9.27: View from a fixed frame for a prolate top (I3 < I, Omega < 0). A vertical vector L is shown. A vector omega precesses around L, forming a cone. A vector x3_hat is also shown, precessing around L. The vectors L, omega, and x3_hat are coplanar. The text 'view from fixed frame, Omega < 0 (I3 < I)' is below the diagram.](a5bc961c265833eb191e409a39b05de9_img.jpg)

Diagram Fig. 9.27: View from a fixed frame for a prolate top (I3 < I, Omega < 0). A vertical vector L is shown. A vector omega precesses around L, forming a cone. A vector x3\_hat is also shown, precessing around L. The vectors L, omega, and x3\_hat are coplanar. The text 'view from fixed frame, Omega < 0 (I3 < I)' is below the diagram.

Fig. 9.27

But this is simply the expression for the rate of change of a vector rotating around the fixed vector  $\tilde{\boldsymbol{\omega}} \equiv (L/I) \hat{\mathbf{L}}$ . The frequency of this rotation is  $|\tilde{\boldsymbol{\omega}}| = L/I$ . Therefore,  $\hat{\mathbf{x}}_3$  precesses around the fixed vector  $\mathbf{L}$  with frequency

$$\tilde{\omega} = \frac{L}{I}, \quad (9.55)$$

<sup>12</sup> This distance could theoretically be much larger or much smaller than 10 m. It happens to be of this order due to the nature of the driving force. The present consensus for this force is pressure changes at the bottom of the ocean and in the atmosphere; see Gross (2000). Without a driving force, the amplitude would head to zero, due to the nonrigidity of the earth.

in the fixed frame. And therefore  $\boldsymbol{\omega}$  does also, because it is coplanar with  $\hat{\mathbf{x}}_3$  and  $\mathbf{L}$ .

##### REMARKS:

1. We just found that  $\boldsymbol{\omega}$  precesses around  $\mathbf{L}$  with frequency  $L/I$ . What, then, is wrong with the following reasoning: “Just as the rate of change of  $\hat{\mathbf{x}}_3$  equals  $\boldsymbol{\omega} \times \hat{\mathbf{x}}_3$ , the rate of change of  $\boldsymbol{\omega}$  should equal  $\boldsymbol{\omega} \times \boldsymbol{\omega}$ , which is zero. Therefore,  $\boldsymbol{\omega}$  should remain constant.” The error is that the vector  $\boldsymbol{\omega}$  is not fixed in the body frame. A vector  $\mathbf{A}$  must be fixed in the body frame in order for its rate of change to be given by  $\boldsymbol{\omega} \times \mathbf{A}$ .
2. We found in Eqs. (9.51) and (9.47) that a person standing on the rotating body sees  $\mathbf{L}$  (and  $\boldsymbol{\omega}$ ) precess with frequency  $\Omega \equiv \omega_3(I_3 - I)/I$  around  $\hat{\mathbf{x}}_3$ . But we found in Eq. (9.55) that a person standing in the fixed frame sees  $\hat{\mathbf{x}}_3$  (and  $\boldsymbol{\omega}$ ) precess with frequency  $L/I$  around  $\mathbf{L}$ . Are these two facts compatible? Should we have obtained the same frequency from either point of view? (Answers: yes, no).

These two frequencies are indeed consistent, as can be seen by the following reasoning. Consider the plane (call it  $S$ ) containing the three vectors  $\mathbf{L}$ ,  $\boldsymbol{\omega}$ , and  $\hat{\mathbf{x}}_3$ . We know from Eq. (9.51) that  $S$  rotates with frequency  $\Omega \hat{\mathbf{x}}_3$  with respect to the body. Therefore, the body rotates with frequency  $-\Omega \hat{\mathbf{x}}_3$  with respect to  $S$ . And from Eq. (9.55),  $S$  rotates with frequency  $(L/I)\hat{\mathbf{L}}$  with respect to the fixed frame. Therefore, the total angular velocity of the body with respect to the fixed frame is (using the frame  $S$  as an intermediate step)

$$\boldsymbol{\omega}_{\text{total}} = \frac{L}{I} \hat{\mathbf{L}} - \Omega \hat{\mathbf{x}}_3. \tag{9.56}$$

But from Eq. (9.53), this is simply  $\boldsymbol{\omega}$ , as it should be. So the two frequencies in Eqs. (9.47) and (9.55) are indeed consistent.

For the earth,  $I_3$  and  $I$  are nearly the same, so  $\Omega \equiv \omega_3(I_3 - I)/I$  and  $L/I$  are quite different.  $L/I$  is roughly equal to  $L/I_3$ , which is essentially equal to  $\omega_3$ . On the other hand,  $\Omega$  is roughly equal to  $(1/300)\omega_3$ . Basically, an external observer sees  $\boldsymbol{\omega}$  precess around its cone at roughly the rate at which the earth spins. But it’s not exactly the same rate, and this difference is what causes the earth-based observer to see  $\boldsymbol{\omega}$  precess with a nonzero  $\Omega$ .

3. The fixed-frame precession of  $\hat{\mathbf{x}}_3$  around  $\mathbf{L}$  should not be confused with the “precession of the equinoxes” effect. See Problem 10.15 for a discussion of the latter. ♣

### 9.7 Heavy symmetric top

Consider now a heavy symmetrical top, that is, one that spins on a table, under the influence of gravity (see Fig. 9.28). Assume that the tip of the top is fixed on the table by a pivot. We’ll solve for the motion of the top in two different ways below in Sections 9.7.3 and 9.7.4. The first uses  $\boldsymbol{\tau} = d\mathbf{L}/dt$ , and the second uses the Lagrangian method.

#### 9.7.1 Euler angles

For both of these methods, it is convenient to use the *Euler angles*,  $\theta$ ,  $\phi$ ,  $\psi$ , which are shown in Fig. 9.29 and defined as follows.

- $\theta$ : Let  $\hat{\mathbf{x}}_3$  be the symmetry axis of the top. Define  $\theta$  to be the angle that  $\hat{\mathbf{x}}_3$  makes with the vertical  $\hat{\mathbf{z}}$  axis of the fixed frame.

![Diagram of a heavy symmetric top spinning on a horizontal surface. The top is tilted at an angle, and its symmetry axis is labeled x3. A dashed line indicates the vertical axis of rotation.](6e97b21dd83c59ced3f1a4efad42ae55_img.jpg)

Diagram of a heavy symmetric top spinning on a horizontal surface. The top is tilted at an angle, and its symmetry axis is labeled x3. A dashed line indicates the vertical axis of rotation.

Fig. 9.28

![Diagram illustrating the Euler angles for a heavy symmetric top. It shows a fixed point in the body, a vertical z-axis, and a horizontal x1-x2 plane. The top's symmetry axis x3 makes an angle theta with the z-axis. The angle phi is the azimuthal angle of x3 in the horizontal plane. The angle psi is the spin angle of the top around its own x3 axis.](85d5e9aebee631ddd18211feed46676b_img.jpg)

Diagram illustrating the Euler angles for a heavy symmetric top. It shows a fixed point in the body, a vertical z-axis, and a horizontal x1-x2 plane. The top's symmetry axis x3 makes an angle theta with the z-axis. The angle phi is the azimuthal angle of x3 in the horizontal plane. The angle psi is the spin angle of the top around its own x3 axis.

Fig. 9.29

- $\phi$ : Draw the plane orthogonal to  $\hat{\mathbf{x}}_3$ . Let  $\hat{\mathbf{x}}_1$  be the intersection of this plane with the horizontal  $x$ - $y$  plane. Define  $\phi$  to be the angle that  $\hat{\mathbf{x}}_1$  makes with the  $\hat{\mathbf{x}}$  axis in the fixed frame. Note that  $\hat{\mathbf{x}}_1$  is not necessarily fixed in the object.
- $\psi$ : Let  $\hat{\mathbf{x}}_2$  be orthogonal to  $\hat{\mathbf{x}}_3$  and  $\hat{\mathbf{x}}_1$ , as shown. As with  $\hat{\mathbf{x}}_1$ ,  $\hat{\mathbf{x}}_2$  is not necessarily fixed in the object. Let frame  $S$  be the frame whose axes are  $\hat{\mathbf{x}}_1$ ,  $\hat{\mathbf{x}}_2$ , and  $\hat{\mathbf{x}}_3$ . Define  $\psi$  to be the angle of rotation of the body around the  $\hat{\mathbf{x}}_3$  axis in frame  $S$ . So  $\dot{\psi}\hat{\mathbf{x}}_3$  is the angular velocity of the body with respect to  $S$ . And from the figure, we also see that the angular velocity of frame  $S$  with respect to the fixed frame is  $\dot{\phi}\hat{\mathbf{z}} + \dot{\theta}\hat{\mathbf{x}}_1$ .

The angular velocity of the body with respect to the fixed frame is equal to the angular velocity of the body with respect to frame  $S$ , plus the angular velocity of frame  $S$  with respect to the fixed frame. From above, we therefore have

$$\boldsymbol{\omega} = \dot{\psi}\hat{\mathbf{x}}_3 + (\dot{\phi}\hat{\mathbf{z}} + \dot{\theta}\hat{\mathbf{x}}_1). \quad (9.57)$$

It is often more convenient to rewrite  $\boldsymbol{\omega}$  entirely in terms of the orthogonal  $\hat{\mathbf{x}}_1$ ,  $\hat{\mathbf{x}}_2$ ,  $\hat{\mathbf{x}}_3$  basis vectors. Since  $\hat{\mathbf{z}} = \cos\theta\hat{\mathbf{x}}_3 + \sin\theta\hat{\mathbf{x}}_2$ , Eq. (9.57) gives

$$\boldsymbol{\omega} = (\dot{\psi} + \dot{\phi}\cos\theta)\hat{\mathbf{x}}_3 + \dot{\phi}\sin\theta\hat{\mathbf{x}}_2 + \dot{\theta}\hat{\mathbf{x}}_1. \quad (9.58)$$

This form of  $\boldsymbol{\omega}$  is generally more useful, because  $\hat{\mathbf{x}}_1$ ,  $\hat{\mathbf{x}}_2$ ,  $\hat{\mathbf{x}}_3$  are principal axes of the body. (We are assuming that we are working with a symmetrical top, with  $I_1 = I_2 \equiv I$ . This means that any axes in the  $\hat{\mathbf{x}}_1$ - $\hat{\mathbf{x}}_2$  plane are principal axes.) Although  $\hat{\mathbf{x}}_1$  and  $\hat{\mathbf{x}}_2$  are not fixed in the object, they are still good principal axes at any instant.

#### 9.7.2 Digression on the components of $\boldsymbol{\omega}$

The above expressions for  $\boldsymbol{\omega}$  might look a little scary, but there is a very helpful diagram we can draw (see Fig. 9.30) that makes it easier to see what's going on. Let's talk a bit about this before tackling the original problem of the spinning top. The diagram is rather dense (you might even say it looks scarier than the above  $\boldsymbol{\omega}$ ), so we'll go through it slowly. In the following discussion, we'll simplify things by setting  $\dot{\theta} = 0$ . All the interesting features of  $\boldsymbol{\omega}$  remain. The  $\dot{\theta}\hat{\mathbf{x}}_1$  component of  $\boldsymbol{\omega}$  in Eqs. (9.57) and (9.58) arises simply from the easily visualizable rising and falling of the top. We will therefore concentrate on the more complicated issues, namely the components of  $\boldsymbol{\omega}$  in the plane of  $\hat{\mathbf{x}}_3$ ,  $\hat{\mathbf{z}}$ , and  $\hat{\mathbf{x}}_2$ .

With  $\dot{\theta} = 0$ , Fig. 9.30 shows the vector  $\boldsymbol{\omega}$  in the  $\hat{\mathbf{x}}_3$ - $\hat{\mathbf{z}}$ - $\hat{\mathbf{x}}_2$  plane (the way we've drawn it,  $\hat{\mathbf{x}}_1$  points into the page, in contrast with Fig. 9.29). We'll refer to this figure many times in the problems for this chapter. There are numerous comments to be made about it, so we'll just list them out. The following discussion deals with the *kinematics* of  $\boldsymbol{\omega}$ , that is, the meaning of the various components and how they relate to each other. The discussion of the *dynamics* of  $\boldsymbol{\omega}$ , that is, why the components take on the values they do, given a certain physical system, is the subject of Section 9.7.3 onward.

![Figure 9.30: A 3D vector diagram showing the decomposition of the angular velocity vector ω. The diagram includes a vertical z-axis and a symmetry axis x̂₃. The vector ω is shown as the sum of its components Ω (along the symmetry axis) and ω' (perpendicular to it). The angle between ω and the symmetry axis is θ. The components of ω along the z-axis and x̂₃ axis are labeled ω_z and ω₃ respectively. The components of ω perpendicular to the z-axis and the symmetry axis are labeled ω₂ and ω' respectively. The angle between the z-axis and the symmetry axis is also θ. The diagram illustrates the relationship between these various components and angles.](316e16a7a3c8f7870fa71d9500b83b8f_img.jpg)

Figure 9.30: A 3D vector diagram showing the decomposition of the angular velocity vector ω. The diagram includes a vertical z-axis and a symmetry axis x̂₃. The vector ω is shown as the sum of its components Ω (along the symmetry axis) and ω' (perpendicular to it). The angle between ω and the symmetry axis is θ. The components of ω along the z-axis and x̂₃ axis are labeled ω\_z and ω₃ respectively. The components of ω perpendicular to the z-axis and the symmetry axis are labeled ω₂ and ω' respectively. The angle between the z-axis and the symmetry axis is also θ. The diagram illustrates the relationship between these various components and angles.

Fig. 9.30

1. If someone asks you to “decompose”  $\boldsymbol{\omega}$  into pieces along  $\hat{\mathbf{z}}$  and  $\hat{\mathbf{x}}_3$ , what would you do? Would you draw the lines perpendicular to these axes to obtain the lengths shown (which we’ll label as  $\omega_z$  and  $\omega_3$ ), or would you draw the lines parallel to these axes to obtain the lengths shown (which we’ll label as  $\Omega$  and  $\omega'$ )? There is no “correct” answer to this question. The four quantities,  $\omega_z$ ,  $\omega_3$ ,  $\Omega$ ,  $\omega'$  simply represent different things. We will interpret each of these below, along with  $\omega_2$  (the projection of  $\boldsymbol{\omega}$  along  $\hat{\mathbf{x}}_2$ ). It turns out that  $\Omega$  and  $\omega'$  are the frequencies that your eye can see the easiest, while  $\omega_2$  and  $\omega_3$  are what you want to use when doing calculations involving the angular momentum. But as far as I can see,  $\omega_z$  is not of much use.
2. Note that it is true that

$$\boldsymbol{\omega} = \omega' \hat{\mathbf{x}}_3 + \Omega \hat{\mathbf{z}}, \quad (9.59)$$

but it is *not* true that  $\boldsymbol{\omega} = \omega_3 \hat{\mathbf{x}}_3 + \omega_z \hat{\mathbf{z}}$ . Another true statement is

$$\boldsymbol{\omega} = \omega_3 \hat{\mathbf{x}}_3 + \omega_2 \hat{\mathbf{x}}_2. \quad (9.60)$$

3. In terms of the Euler angles, we see by comparing Eqs. (9.59) and (9.57), with  $\dot{\theta} = 0$ , that

$$\omega' = \dot{\psi}, \quad \text{and} \quad \Omega = \dot{\phi}. \quad (9.61)$$

And we also have, by comparing Eqs. (9.60) and (9.58), with  $\dot{\theta} = 0$ ,

$$\begin{aligned} \omega_3 &= \dot{\psi} + \dot{\phi} \cos \theta = \omega' + \Omega \cos \theta, \\ \omega_2 &= \dot{\phi} \sin \theta = \Omega \sin \theta. \end{aligned} \quad (9.62)$$

These are also clear from Fig. 9.30. There is therefore technically no need to introduce the new  $\omega_2$ ,  $\omega_3$ ,  $\Omega$ ,  $\omega'$  definitions in Fig. 9.30, because the Euler angles are quite

sufficient. But we will be referring back to this figure many times, and it is a little easier to work with these omegas than the various combinations of the Euler angles.

- 4.  $\Omega$  is the easiest of the frequencies to visualize. It is the frequency of precession of the top around the vertical  $\hat{\mathbf{z}}$  axis.<sup>13</sup> In other words, the symmetry axis  $\hat{\mathbf{x}}_3$  traces out a cone (assuming  $\dot{\theta} = 0$ ) around the  $\hat{\mathbf{z}}$  axis with frequency  $\Omega$ . The reason for this is the following. The vector  $\boldsymbol{\omega}$  is the vector that gives the speed of any point (at position  $\mathbf{r}$ ) fixed in the top as  $\boldsymbol{\omega} \times \mathbf{r}$ . Therefore, since the vector  $\hat{\mathbf{x}}_3$  is fixed in the top, we can write

$$\frac{d\hat{\mathbf{x}}_3}{dt} = \boldsymbol{\omega} \times \hat{\mathbf{x}}_3 = (\omega' \hat{\mathbf{x}}_3 + \Omega \hat{\mathbf{z}}) \times \hat{\mathbf{x}}_3 = (\Omega \hat{\mathbf{z}}) \times \hat{\mathbf{x}}_3. \quad (9.63)$$

But this is precisely the expression for the rate of change of a vector rotating around the  $\hat{\mathbf{z}}$  axis with frequency  $\Omega$ . (This is exactly the same type of proof as the one leading to Eq. (9.54).) Note that the precession frequency around the  $\hat{\mathbf{z}}$  axis is *not*  $\omega_z$ . It certainly can't be  $\omega_z$ , because we can imagine grabbing the symmetry axis and holding it in place, so that  $\boldsymbol{\omega}$  points along  $\hat{\mathbf{x}}_3$ . This scenario has a nonzero  $\omega_z$ , but no precession.

REMARK: In the derivation of Eq. (9.63), we basically just stripped off the part of  $\boldsymbol{\omega}$  that points along the  $\hat{\mathbf{x}}_3$  axis, because a rotation around  $\hat{\mathbf{x}}_3$  contributes nothing to the motion of  $\hat{\mathbf{x}}_3$ . Note, however, that there is in fact an infinite number of ways to strip off a piece along  $\hat{\mathbf{x}}_3$ . For example, we can also break  $\boldsymbol{\omega}$  up as, say,  $\boldsymbol{\omega} = \omega_3 \hat{\mathbf{x}}_3 + \omega_2 \hat{\mathbf{x}}_2$ . We then obtain  $d\hat{\mathbf{x}}_3/dt = (\omega_2 \hat{\mathbf{x}}_2) \times \hat{\mathbf{x}}_3$ , which means that  $\hat{\mathbf{x}}_3$  is instantaneously rotating around  $\hat{\mathbf{x}}_2$  with frequency  $\omega_2$ . Although this is true, it isn't as useful as the result in Eq. (9.63), because the  $\hat{\mathbf{x}}_2$  axis changes with time (it precesses around  $\hat{\mathbf{z}}$ ). The point here is that the instantaneous angular velocity vector around which the symmetry axis rotates is not well defined (Problem 9.1 discusses this issue).<sup>14</sup> But the  $\hat{\mathbf{z}}$  axis is the only one of these angular velocity vectors that is fixed. When we look at the top (or more precisely, the symmetry axis), we therefore see it precessing around the  $\hat{\mathbf{z}}$  axis. ♣

- 5.  $\omega'$  is also easy to visualize. Imagine that you are at rest in the frame that rotates around the  $\hat{\mathbf{z}}$  axis with frequency  $\Omega$ . Then you see the symmetry axis of the top remain perfectly still, and the only motion you see is the top spinning around this axis with frequency  $\omega'$ . (This is true because  $\boldsymbol{\omega} = \omega' \hat{\mathbf{x}}_3 + \Omega \hat{\mathbf{z}}$ , and the rotation of your frame causes you not to see the  $\Omega \hat{\mathbf{z}}$  part.) If you paint a dot somewhere on the top, then the dot traces out a fixed tilted circle, and the dot returns to, say, its maximum height at frequency  $\omega'$ . A person in the lab frame sees this dot undergo a rather complicated motion but must observe the same frequency at which the dot returns to its highest point. So  $\omega'$  is something quite physical in the lab frame also.
- 6.  $\omega_3$  is what you use to obtain the component of  $\mathbf{L}$  along  $\hat{\mathbf{x}}_3$ , because  $L_3 = I_3 \omega_3$ .  $\omega_3$  is a little harder to visualize than  $\Omega$  and  $\omega'$ , but it is the frequency with which the top

<sup>13</sup> Although we're using the same letter, this  $\Omega$  doesn't have anything to do with the  $\Omega$  defined in Eq. (9.47), except for the fact that they both represent the frequency of something precessing around an axis.

<sup>14</sup> The instantaneous angular velocity of the *whole body* is well defined, of course. There is a definite line of points in the body that are instantaneously at rest. But if you look at the symmetry axis by itself, then there is an ambiguity (see Footnote 9). In short, because only one point on the axis (the bottom end), instead of a whole line, is instantaneously at rest, the instantaneous angular velocity vector can point in any direction.

instantaneously rotates, as seen by someone at rest in the frame that rotates around the instantaneous  $\hat{\mathbf{x}}_2$  axis with frequency  $\omega_2$ . (This is true because  $\boldsymbol{\omega} = \omega_2 \hat{\mathbf{x}}_2 + \omega_3 \hat{\mathbf{x}}_3$ , and the rotation of the frame causes the person not to see the  $\omega_2 \hat{\mathbf{x}}_2$  part.) This rotation is harder to visualize in the lab frame, because the  $\hat{\mathbf{x}}_2$  axis changes with time.

There is one physical scenario in which  $\omega_3$  is the easily observed frequency. Imagine that the top is precessing around the  $\hat{\mathbf{z}}$  axis at constant  $\theta$  (we'll find in Section 9.7.5 that this is in fact a possible motion for the top), and imagine that the top has a frictionless rod protruding along its symmetry axis. If you grab the rod and stop the precession motion, so that the top is now spinning around its stationary symmetry axis, then this spinning has frequency  $\omega_3$ . This is true because when you grab the rod, your torque has no component along the  $\hat{\mathbf{x}}_3$  axis (because the rod lies along this axis, and because it is frictionless). Therefore,  $L_3$  doesn't change, and so neither does  $\omega_3$ .

7.  $\omega_2$  is similar to  $\omega_3$ , of course.  $\omega_2$  is what you use to obtain the component of  $\mathbf{L}$  along  $\hat{\mathbf{x}}_2$ , because  $L_2 = I_2 \omega_2$ . It is the frequency with which the top instantaneously rotates, as seen by someone at rest in the frame that rotates around the instantaneous  $\hat{\mathbf{x}}_3$  axis with frequency  $\omega_3$ . (This is true because  $\boldsymbol{\omega} = \omega_2 \hat{\mathbf{x}}_2 + \omega_3 \hat{\mathbf{x}}_3$ , and the rotation of the frame causes the person not to see the  $\omega_3 \hat{\mathbf{x}}_3$  part.) Again, this rotation is harder to visualize in the lab frame, because the  $\hat{\mathbf{x}}_3$  axis changes with time. Note that by “instantaneous  $\hat{\mathbf{x}}_3$  axis,” we mean the fixed axis in space that coincides with the symmetry axis at a given instant. The symmetry axis will therefore move away from this fixed axis, consistent with the fact that the person in the above-mentioned rotating frame sees the top rotate around the  $\hat{\mathbf{x}}_2$  axis.

The physical scenario that produces  $\omega_2$ , analogous to the scenario that produced  $\omega_3$  above, is the following. Imagine a frictionless rod glued to the top at its tip, perpendicular to the symmetry axis, so that they form a “T.” As this rod is spinning around (ignore the fact that it has to keep passing through the table), grab it at the instant it points along  $\hat{\mathbf{x}}_2$ . The top will then rotate with frequency  $\omega_2$  around the fixed rod. This is true for reasons analogous to the ones in the  $\omega_3$  case above.

8.  $\omega_z$  is not very useful, as far as I can see. The most important thing to note about  $\omega_z$  is that it is *not* the frequency of precession around the  $\hat{\mathbf{z}}$  axis, even though it is the projection of  $\boldsymbol{\omega}$  onto  $\hat{\mathbf{z}}$ . The frequency of the precession is  $\Omega$ , as we found above in Eq. (9.63). A true, but somewhat useless, fact about  $\omega_z$  is that if someone is at rest in the frame that rotates around the  $\hat{\mathbf{z}}$  axis with frequency  $\omega_z$ , then she sees all points in the top instantaneously rotating around the horizontal  $\hat{\mathbf{x}}$  axis with frequency  $\omega_x$ , where  $\omega_x$  is the projection of  $\boldsymbol{\omega}$  onto the  $\hat{\mathbf{x}}$  axis. (This is true because  $\boldsymbol{\omega} = \omega_x \hat{\mathbf{x}} + \omega_z \hat{\mathbf{z}}$ , and the rotation of the frame causes her not to see the  $\omega_z \hat{\mathbf{z}}$  part.)

#### 9.7.3 Torque method

Let's now finally solve for the motion of a heavy top. This first method involving torque is straightforward, although a bit tedious. We include it here to (1) show that the problem can be done without resorting to a Lagrangian, and to (2) get some practice using  $\boldsymbol{\tau} = d\mathbf{L}/dt$ . We'll make use of the form of  $\boldsymbol{\omega}$  given in

Eq. (9.58), because there it is broken up into the principal-axis components. For convenience, define  $\dot{\beta} = \dot{\psi} + \dot{\phi} \cos \theta$ , so that

$$\boldsymbol{\omega} = \dot{\beta} \hat{\mathbf{x}}_3 + \dot{\phi} \sin \theta \hat{\mathbf{x}}_2 + \dot{\theta} \hat{\mathbf{x}}_1. \quad (9.64)$$

Note that we've returned to the most general motion, where  $\dot{\theta}$  is not necessarily zero. For our origin, we'll choose the tip of the top, which is assumed to be fixed on the table.<sup>15</sup> Let the principal moments relative to this origin be  $I_1 = I_2 \equiv I$ , and  $I_3$ . The angular momentum of the top is then

$$\mathbf{L} = I_3 \dot{\beta} \hat{\mathbf{x}}_3 + I \dot{\phi} \sin \theta \hat{\mathbf{x}}_2 + I \dot{\theta} \hat{\mathbf{x}}_1. \quad (9.65)$$

We must now calculate  $d\mathbf{L}/dt$ . What makes this nontrivial is the fact that the  $\hat{\mathbf{x}}_1$ ,  $\hat{\mathbf{x}}_2$ , and  $\hat{\mathbf{x}}_3$  unit vectors change with time (they change with  $\theta$  and  $\phi$ ). But let's forge ahead and take the derivative of Eq. (9.65). Using the product rule (which works fine with the product of a scalar and a vector), we have

$$\begin{aligned} \frac{d\mathbf{L}}{dt} &= I_3 \frac{d\dot{\beta}}{dt} \hat{\mathbf{x}}_3 + I \frac{d(\dot{\phi} \sin \theta)}{dt} \hat{\mathbf{x}}_2 + I \frac{d\dot{\theta}}{dt} \hat{\mathbf{x}}_1 \\ &\quad + I_3 \dot{\beta} \frac{d\hat{\mathbf{x}}_3}{dt} + I \dot{\phi} \sin \theta \frac{d\hat{\mathbf{x}}_2}{dt} + I \dot{\theta} \frac{d\hat{\mathbf{x}}_1}{dt}. \end{aligned} \quad (9.66)$$

Using a little geometry, you can show that

$$\begin{aligned} \frac{d\hat{\mathbf{x}}_3}{dt} &= -\dot{\theta} \hat{\mathbf{x}}_2 + \dot{\phi} \sin \theta \hat{\mathbf{x}}_1, \\ \frac{d\hat{\mathbf{x}}_2}{dt} &= \dot{\theta} \hat{\mathbf{x}}_3 - \dot{\phi} \cos \theta \hat{\mathbf{x}}_1, \\ \frac{d\hat{\mathbf{x}}_1}{dt} &= -\dot{\phi} \sin \theta \hat{\mathbf{x}}_3 + \dot{\phi} \cos \theta \hat{\mathbf{x}}_2. \end{aligned} \quad (9.67)$$

As an exercise, you should verify these by making use of Fig. 9.29. In the first equation, for example, show that a change in  $\theta$  causes  $\hat{\mathbf{x}}_3$  to move a certain distance in the  $\hat{\mathbf{x}}_2$  direction; and show that a change in  $\phi$  causes  $\hat{\mathbf{x}}_3$  to move a certain distance in the  $\hat{\mathbf{x}}_1$  direction. Plugging the derivative expressions from Eq. (9.67) into Eq. (9.66) gives, after some algebra,

$$\begin{aligned} \frac{d\mathbf{L}}{dt} &= I_3 \ddot{\beta} \hat{\mathbf{x}}_3 + \left( I \ddot{\phi} \sin \theta + 2I \dot{\theta} \dot{\phi} \cos \theta - I_3 \dot{\beta} \dot{\theta} \right) \hat{\mathbf{x}}_2 \\ &\quad + \left( I \ddot{\theta} - I \dot{\phi}^2 \sin \theta \cos \theta + I_3 \dot{\beta} \dot{\phi} \sin \theta \right) \hat{\mathbf{x}}_1. \end{aligned} \quad (9.68)$$

Let's now look at the torque on the top. This arises from gravity pulling down on the CM. So from Fig. 9.29,  $\boldsymbol{\tau}$  points in the  $\hat{\mathbf{x}}_1$  direction and has magnitude

<sup>15</sup> We could use the CM as our origin, but then we would have to include the complicated forces acting at the pivot point, which is difficult. But see Problem 9.19 for the case where the tip is free to slide on a frictionless table.

$Mg\ell \sin \theta$ , where  $\ell$  is the distance from the pivot to the CM. Using Eq. (9.68), the third component of  $\boldsymbol{\tau} = d\mathbf{L}/dt$  quickly gives

$$\ddot{\beta} = 0. \quad (9.69)$$

Therefore,  $\dot{\beta}$  is a constant, which we'll call  $\omega_3$  (an obvious label, in view of Eq. (9.64)). The other two components of  $\boldsymbol{\tau} = d\mathbf{L}/dt$  then give

$$\begin{aligned} I\ddot{\phi} \sin \theta + \dot{\theta}(2I\dot{\phi} \cos \theta - I_3\omega_3) &= 0, \\ (Mg\ell + I\dot{\phi}^2 \cos \theta - I_3\omega_3\dot{\phi}) \sin \theta &= I\ddot{\theta}. \end{aligned} \quad (9.70)$$

We'll wait to fiddle with these equations until we have derived them again using the Lagrangian method.

#### 9.7.4 Lagrangian method

Equation (9.15) gives the kinetic energy of the top as  $T = \boldsymbol{\omega} \cdot \mathbf{L}/2$ . Using Eqs. (9.64) and (9.65), we have (writing  $\dot{\psi} + \dot{\phi} \cos \theta$  instead of the shorthand  $\dot{\beta}$ )<sup>16</sup>

$$T = \frac{1}{2} \boldsymbol{\omega} \cdot \mathbf{L} = \frac{1}{2} I_3 (\dot{\psi} + \dot{\phi} \cos \theta)^2 + \frac{1}{2} I (\dot{\phi}^2 \sin^2 \theta + \dot{\theta}^2). \quad (9.71)$$

The potential energy is

$$V = Mg\ell \cos \theta, \quad (9.72)$$

where  $\ell$  is the distance from the pivot to the CM. The Lagrangian is  $\mathcal{L} = T - V$  (we'll use “ $\mathcal{L}$ ” here to avoid confusion with the angular momentum “ $L$ ”), and so the equation of motion obtained from varying  $\psi$  is

$$\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{\psi}} = \frac{\partial \mathcal{L}}{\partial \psi} \implies \frac{d}{dt} (\dot{\psi} + \dot{\phi} \cos \theta) = 0. \quad (9.73)$$

Therefore,  $\dot{\psi} + \dot{\phi} \cos \theta$  is a constant. Call it  $\omega_3$ . The equations of motion obtained from varying  $\phi$  and  $\theta$  are then (making use of  $\dot{\psi} + \dot{\phi} \cos \theta = \omega_3$ )

$$\begin{aligned} \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{\phi}} &= \frac{\partial \mathcal{L}}{\partial \phi} \implies \frac{d}{dt} (I_3\omega_3 \cos \theta + I\dot{\phi} \sin^2 \theta) = 0, \\ \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{\theta}} &= \frac{\partial \mathcal{L}}{\partial \theta} \implies I\ddot{\theta} = (Mg\ell + I\dot{\phi}^2 \cos \theta - I_3\omega_3\dot{\phi}) \sin \theta. \end{aligned} \quad (9.74)$$

Taking the derivative in the first equation, we see that these equations are identical to those in Eq. (9.70).

<sup>16</sup> It was ok to use  $\beta$  in the previous subsection. We introduced it only because it was quicker to write. But we can't use it here, because it depends on the other coordinates, and the Lagrangian method requires the use of independent coordinates. The variational proof back in Chapter 6 assumed this independence.

Note that there are two conserved quantities, arising from the facts that  $\partial \mathcal{L} / \partial \psi$  and  $\partial \mathcal{L} / \partial \phi$  equal zero. The conserved quantities are the angular momenta in the  $\hat{\mathbf{x}}_3$  and  $\hat{\mathbf{z}}$  directions, respectively. This is true because from Eq. (9.65), the former is  $L_3 = I_3 \omega_3$  and the latter is  $L_z = L_3 \cos \theta + L_2 \sin \theta = (I_3 \omega_3) \cos \theta + (I \dot{\phi} \sin \theta) \sin \theta$ . These angular momenta are conserved because the torque points in the  $\hat{\mathbf{x}}_1$  direction, so there is no torque in the plane spanned by  $\hat{\mathbf{x}}_3$  and  $\hat{\mathbf{z}}$ .

#### 9.7.5 Spinning top with $\dot{\theta} = 0$

A special case of Eqs. (9.70) occurs when  $\dot{\theta} = 0$ . In this case, the first of Eqs. (9.70) says that  $\dot{\phi}$  is constant. The CM of the top therefore undergoes uniform circular motion in a horizontal plane. Let  $\Omega \equiv \dot{\phi}$  be the frequency of this motion (this is the same notation as in Eq. (9.61)). Then the second of Eqs. (9.70) becomes

$$I \Omega^2 \cos \theta - I_3 \omega_3 \Omega + Mg\ell = 0. \quad (9.75)$$

This quadratic equation can be solved to yield two possible precessional frequencies,  $\Omega$ , for the top. And yes, there are indeed two of them, provided that  $\omega_3$  is greater than a certain minimum value.

The previous pages in this “Heavy symmetric top” section have been a bit abstract, so let’s now take a breather and rederive Eq. (9.75) from scratch. That is, we’ll assume  $\dot{\theta} = 0$  from the start of the solution, and then solve things by finding  $\mathbf{L}$  and using  $\boldsymbol{\tau} = d\mathbf{L}/dt$ , in the spirit of Section 9.4.2. In practice, this strategy of starting from scratch is invariably the best route to take, as you’ll see in the problems and exercises for this chapter. The procedures in Sections 9.7.3 and 9.7.4 are good to know, but the technique in the following example provides a much more intuitive way of looking at things. This example is the classic “top” problem. We’ll warm up by solving it in an approximate way. Then we’ll do it for real.

![Diagram of a symmetric top spinning about its symmetry axis. The top is tilted at an angle theta from the vertical z-axis. The center of mass (CM) is at a distance l from the pivot. The top spins with frequency omega_3 about its symmetry axis. The symmetry axis precesses around the vertical axis with frequency Omega. The diagram shows the vertical axis, the symmetry axis, and the horizontal axis, with the angle theta between the vertical and symmetry axes.](8c8690f18b1a39528bc23cdc2eaf733c_img.jpg)

Diagram of a symmetric top spinning about its symmetry axis. The top is tilted at an angle theta from the vertical z-axis. The center of mass (CM) is at a distance l from the pivot. The top spins with frequency omega\_3 about its symmetry axis. The symmetry axis precesses around the vertical axis with frequency Omega. The diagram shows the vertical axis, the symmetry axis, and the horizontal axis, with the angle theta between the vertical and symmetry axes.

Fig. 9.31

**Example (The top):** A symmetric top of mass  $M$  has its CM a distance  $\ell$  from its pivot. The moments of inertia relative to the pivot are  $I_1 = I_2 \equiv I$ , and  $I_3$ . The top spins around its symmetry axis with frequency  $\omega_3$  (in the language of Section 9.7.2), and initial conditions have been set up so that the CM precesses in a circle around the vertical axis. The symmetry axis makes a constant angle  $\theta$  with the vertical (see Fig. 9.31).

- Assuming that the angular momentum due to  $\omega_3$  is much larger than any other angular momentum in the problem, find an approximate expression for the frequency,  $\Omega$ , of precession.
- Now solve the problem exactly. That is, find  $\Omega$  by considering all of the angular momentum.

##### **Solution:**

- (a) The angular momentum (relative to the pivot) due to the spinning of the top has magnitude  $L_3 = I_3\omega_3$ , and it is directed along  $\hat{\mathbf{x}}_3$ . Let's label this angular momentum vector as  $\mathbf{L}_3 \equiv L_3\hat{\mathbf{x}}_3$ . As the top precesses,  $\mathbf{L}_3$  traces out a cone around the vertical axis. So the tip of  $\mathbf{L}_3$  moves in a circle of radius  $L_3 \sin \theta$ . The frequency of this circular motion is the frequency of precession,  $\Omega$ . So  $d\mathbf{L}_3/dt$ , which is the velocity of the tip, has magnitude

$$\Omega(L_3 \sin \theta) = \Omega I_3\omega_3 \sin \theta, \quad (9.76)$$

and it is directed into the page.

The torque (relative to the pivot) is due to gravity acting on the CM, so it has magnitude  $Mg\ell \sin \theta$ , and it is directed into the page. Therefore,  $\boldsymbol{\tau} = d\mathbf{L}/dt$  gives

$$\Omega = \frac{Mg\ell}{I_3\omega_3}. \quad (9.77)$$

This is independent of  $\theta$ , and it is inversely proportional to  $\omega_3$ .

- (b) The error in the above analysis is that we omitted the angular momentum arising from the  $\hat{\mathbf{x}}_2$  (defined in Section 9.7.1) component of the angular velocity due to the precession of the top around the  $\hat{\mathbf{z}}$  axis. This component has magnitude  $\Omega \sin \theta$ .<sup>17</sup> Therefore, the angular momentum due to the angular velocity component in the  $\hat{\mathbf{x}}_2$  direction has magnitude

$$L_2 = I\Omega \sin \theta. \quad (9.78)$$

Let's label this part of the angular momentum as  $\mathbf{L}_2 \equiv L_2\hat{\mathbf{x}}_2$ . The total  $\mathbf{L} = \mathbf{L}_2 + \mathbf{L}_3$  is shown in Fig. 9.32.  $\mathbf{L}$  precesses around in a cone, so only its horizontal component (call it  $\mathbf{L}_\perp$ ) changes. From the figure, the length  $L_\perp$  is the difference in lengths of the horizontal components of  $\mathbf{L}_3$  and  $\mathbf{L}_2$ . Therefore,

$$L_\perp = L_3 \sin \theta - L_2 \cos \theta = I_3\omega_3 \sin \theta - I\Omega \sin \theta \cos \theta. \quad (9.79)$$

The magnitude of the rate of change of  $\mathbf{L}$  is<sup>18</sup>

$$\left| \frac{d\mathbf{L}}{dt} \right| = \Omega L_\perp = \Omega(I_3\omega_3 \sin \theta - I\Omega \sin \theta \cos \theta). \quad (9.80)$$

Both  $\boldsymbol{\tau}$  (which has magnitude  $Mg\ell \sin \theta$ ) and  $d\mathbf{L}/dt$  point into the page, so equating their magnitudes gives

$$I\Omega^2 \cos \theta - I_3\omega_3\Omega + Mg\ell = 0, \quad (9.81)$$

<sup>17</sup> The angular velocity due to the precession is  $\Omega\hat{\mathbf{z}}$ . We can break this up into components along the orthogonal directions  $\hat{\mathbf{x}}_2$  and  $\hat{\mathbf{x}}_3$ . The  $\Omega \cos \theta$  component along  $\hat{\mathbf{x}}_3$  was already absorbed into the definition of  $\omega_3$  (see Fig. 9.30).

<sup>18</sup> This result can also be obtained in a more formal way. Since  $\mathbf{L}$  precesses with angular velocity  $\Omega\hat{\mathbf{z}}$ , the rate of change of  $\mathbf{L}$  is  $d\mathbf{L}/dt = \Omega\hat{\mathbf{z}} \times \mathbf{L}$ . If you compute this cross product in the  $x_1, x_2, x_3$  basis, you will obtain the result in Eq. (9.80).

![Figure 9.32: A 3D vector diagram showing the angular momentum vectors of a heavy symmetric top. The vertical axis is labeled z. A horizontal axis is labeled x2, and another axis is labeled x3. The vector L3 is along the x3 axis, making an angle theta with the z-axis. The vector L2 is along the x2 axis. The total angular momentum vector L is the vector sum of L2 and L3. A horizontal vector L_perp is shown, representing the difference in the horizontal components of L3 and L2. Dashed lines indicate the projections of the vectors onto the horizontal plane.](0df4c1d2e462137900aa7d59de469c6e_img.jpg)

Figure 9.32: A 3D vector diagram showing the angular momentum vectors of a heavy symmetric top. The vertical axis is labeled z. A horizontal axis is labeled x2, and another axis is labeled x3. The vector L3 is along the x3 axis, making an angle theta with the z-axis. The vector L2 is along the x2 axis. The total angular momentum vector L is the vector sum of L2 and L3. A horizontal vector L\_perp is shown, representing the difference in the horizontal components of L3 and L2. Dashed lines indicate the projections of the vectors onto the horizontal plane.

**Fig. 9.32**

in agreement with Eq. (9.75), as we wanted to show. The quadratic formula quickly gives the two solutions for  $\Omega$ , which may be written as

$$\Omega_{\pm} = \frac{I_3 \omega_3}{2I \cos \theta} \left( 1 \pm \sqrt{1 - \frac{4Mg\ell \cos \theta}{I_3^2 \omega_3^2}} \right). \quad (9.82)$$

Note that if  $\theta = \pi/2$ , then Eq. (9.81) is actually a linear equation, so there is only one solution for  $\Omega$ , which is the one in Eq. (9.77). The reason for this is that  $\mathbf{L}_2$  points vertically, so it doesn't change. Only  $\mathbf{L}_3$  contributes to  $d\mathbf{L}/dt$ , so the approximate solution in part (a) is in fact an exact solution. Because of this simplification, a top is much easier to deal with when its symmetry axis is horizontal.

The two solutions in Eq. (9.82) are known as the *fast-precession* and *slow-precession* frequencies. For large  $\omega_3$ , you can show that the slow-precession frequency is

$$\Omega_- \approx \frac{Mg\ell}{I_3 \omega_3}, \quad (9.83)$$

in agreement with the solution found in Eq. (9.77).<sup>19</sup> This task, along with many other interesting features of this problem (including the interpretation of the fast-precession frequency,  $\Omega_+$ ), is the subject of Problem 9.17, which you are encouraged to do.

#### 9.7.6 An “explanation” of precession

The fact that a top can precess slowly around in a circle without simply falling down (as a simple pendulum would do) is rather bizarre. We showed above that this precession can be deduced perfectly well from  $\boldsymbol{\tau} = d\mathbf{L}/dt$ , but it would be nice if there was a more intuitive way to explain it, based at least somewhat on  $\mathbf{F} = m\mathbf{a}$ . Although a completely satisfactory intuitive explanation eludes me, I think the following discussion will clear some things up. This discussion will be qualitative (so no equations or numbers), but it should still suffice in explaining for the most part what's going on with precession.

![Diagram of a dumbbell system. A vertical stick is pivoted at its center. Two masses are at the ends of the stick. A coordinate system is shown with the y-axis pointing to the right and the z-axis pointing upwards. The x-axis points out of the page. A curved arrow indicates rotation around the y-axis. The top mass has a velocity vector v pointing out of the page (represented by a dot in a circle). The bottom mass has a velocity vector v pointing into the page (represented by a cross in a circle). The stick is labeled 'stick'.](b5400f73259ff7cb1580bab6db3ae0eb_img.jpg)

Diagram of a dumbbell system. A vertical stick is pivoted at its center. Two masses are at the ends of the stick. A coordinate system is shown with the y-axis pointing to the right and the z-axis pointing upwards. The x-axis points out of the page. A curved arrow indicates rotation around the y-axis. The top mass has a velocity vector v pointing out of the page (represented by a dot in a circle). The bottom mass has a velocity vector v pointing into the page (represented by a cross in a circle). The stick is labeled 'stick'.

Fig. 9.33

##### Impulse applied to a dumbbell

Let's first look at a simple system consisting of a dumbbell with a massless stick glued perpendicular to it at its center. The dumbbell rotates around the stick which is held fixed; see Fig. 9.33. Let the  $y$  and  $z$  axes be defined as shown, with the  $x$  axis pointing out of the page. The total angular momentum points to the right, in the positive  $y$  direction. We'll ignore gravity for now. Equivalently, we can have the dumbbell pivoted at its center.

<sup>19</sup> This is fairly clear. If  $\omega_3$  is large enough compared with  $\Omega$ , then we can ignore the first term in Eq. (9.81). That is, we can ignore the effects of  $\mathbf{L}_2$ , which is exactly what we did in the approximate solution in part (a).

At the instant the masses are in the plane of the paper, as shown (with the top one coming out of the page and the bottom one going in), we'll apply equal and opposite small impulses to the stick, upward on the right end and downward on the left; see Fig. 9.34.<sup>20</sup> Assume that the forces are applied for infinitesimal periods of time, but that the forces are large enough so that the impulse is nonzero. What happens to the masses? In particular, what happens to the plane of their rotation?

Because the structure is rigid, the impulsive forces on the stick cause the two masses to pick up small velocity components in the  $\pm y$  directions, as shown in Fig. 9.34. If the forces are applied for an infinitesimal time  $t$ , then these velocity components are of the form  $v = at$  (with  $t$  very small and  $a$  very large). Additionally, the masses move a distance  $d = at^2/2$  to the side. But because of the two powers of the infinitesimal time  $t$  here, this distance is negligible. In other words, the masses pick up a nonzero  $v$ , but essentially no  $d$ . This is a general result when an object is struck with a hammer: right after the blow, it has a nonzero speed, but essentially zero displacement.

A top view (with the  $z$  axis pointing out of the page) of the velocities of the two masses right after the blow is shown in Fig. 9.35. The dotted lines represent the velocity of the bottom mass which is behind (that is, below) the top mass. Now, if someone gives you these two velocities and doesn't tell you what was going on beforehand, then you will simply say that the dumbbell is rotating around in a circle that lies in the vertical plane defined by the line of the new velocity vectors in Fig. 9.35. In other words, the plane of the circular motion has been rotated around the vertical  $z$  axis. A top view of the situation is shown in Fig. 9.36. From this time onward, the masses rotate around in the new vertical plane. This means that the angular momentum of the dumbbell has picked up a component in the positive  $x$  direction (out of the page in Fig. 9.34 and downward in Fig. 9.36), consistent with the fact that the torque from the two applied forces points in the positive  $x$  direction.

This example illustrates the bizarre fact that if you smack the rotation axis in one direction (vertical here), it will head off in another direction (horizontal).

##### Impulse applied to a symmetric top

Let's now consider the more complicated situation where instead of the above dumbbell we have a symmetric top, for example, a flat disk with a stick poking through its center. (We'll still ignore gravity for the moment.) Things are more difficult now, because if we apply our impulsive forces to the stick, the plane of the disk can't instantaneously rotate as it did above, because this would involve the "side" points on the disk moving a finite distance in zero time, as they

![Figure 9.34: A diagram showing a vertical stick with two masses at its ends. The top mass has an initial velocity 'v' out of the page and a change in velocity 'Δv' to the left. The bottom mass has an initial velocity 'v' into the page and a change in velocity 'Δv' to the right. A downward force 'F' is applied to the top mass, and an upward force 'F' is applied to the bottom mass. A coordinate system with 'z' pointing up and 'y' pointing right is shown.](96b6236f016f5ce676c1bac1f5a1a2cd_img.jpg)

Figure 9.34: A diagram showing a vertical stick with two masses at its ends. The top mass has an initial velocity 'v' out of the page and a change in velocity 'Δv' to the left. The bottom mass has an initial velocity 'v' into the page and a change in velocity 'Δv' to the right. A downward force 'F' is applied to the top mass, and an upward force 'F' is applied to the bottom mass. A coordinate system with 'z' pointing up and 'y' pointing right is shown.

Fig. 9.34

![Figure 9.35: A top view diagram showing the velocities of the two masses. The original velocity 'v' is a vertical vector pointing down. The new velocity 'new v' is a vector pointing down and to the left. The change in velocity 'Δv' is a horizontal vector pointing to the left. Dotted lines represent the velocity of the bottom mass. A coordinate system with 'x' pointing right and 'y' pointing down is shown.](9060b4e26e1778d321be343b33e8b196_img.jpg)

Figure 9.35: A top view diagram showing the velocities of the two masses. The original velocity 'v' is a vertical vector pointing down. The new velocity 'new v' is a vector pointing down and to the left. The change in velocity 'Δv' is a horizontal vector pointing to the left. Dotted lines represent the velocity of the bottom mass. A coordinate system with 'x' pointing right and 'y' pointing down is shown.

Fig. 9.35

![Figure 9.36: A top view diagram showing the rotation of the plane of motion. The original plane is a vertical line, and the new plane is a line rotated around the vertical 'original axis'. The 'new axis' is also shown. Forces 'F' are applied at the ends of the stick. A coordinate system with 'x' pointing down and 'y' pointing right is shown.](63d5ff444afb67477c89ab6222492c96_img.jpg)

Figure 9.36: A top view diagram showing the rotation of the plane of motion. The original plane is a vertical line, and the new plane is a line rotated around the vertical 'original axis'. The 'new axis' is also shown. Forces 'F' are applied at the ends of the stick. A coordinate system with 'x' pointing down and 'y' pointing right is shown.

Fig. 9.36

<sup>20</sup> We're applying equal and opposite forces just so that the CM doesn't move. And we're doing this for no reason other than simplicity. The motion of the CM is irrelevant for the point we want to make in this dumbbell setup.

move from the old plane of rotation to the new plane. So what does the motion look like?

The rough answer is that our symmetric top is vaguely the same type of object as the above dumbbell, so the motion should look roughly the same. In other words, the axis of the top should end up pointing (in one way or another) a little bit in the  $x$  direction, as it did with the dumbbell. But the precise answer is that since we have a free top here, we know from the free-top discussion in Section 9.6.2 exactly what happens: the symmetry axis of the disk precesses (along with the angular velocity vector) in a thin cone around the new angular momentum vector, which points slightly out of the page due to the torque in the  $x$  direction. So although the symmetry axis of the disk doesn't point in the definite direction along  $\mathbf{L}$  as it did with the dumbbell, it points *on average* along  $\mathbf{L}$ , which is slightly in the  $x$  direction.

Let's now bring gravity into the setup. It turns out that we can consider a heavy top's precession to be the result of a succession of many little impulsive blows to a free top that is otherwise in freefall (where gravity provides no torque). The reasoning is as follows.

Imagine that we hold our spinning top (not pivoted anywhere) and move it sideways (perpendicular to the stick) at a given constant speed; this speed will have to be chosen to be a particular value (see Footnote 23 below). And then we let go. Gravity provides a force on the CM, but zero torque around the CM, so the top is simply in freefall with the constant horizontal speed that we gave it. But let's assume that immediately after we let go, we keep the top at a constant height by applying a very quick and very small upward strike to the end of the stick, and then waiting for a very short time while the CM rises and falls in its freefall motion, and then repeating the process indefinitely (let's say we make 100 tiny strikes each second). If we arrange for the time-averaged upward force to equal  $mg$ , then the CM stays at (essentially) a constant height.

After each strike, the axis of the top undergoes its free-top precession in a very thin cone, so if the CM of the top weren't moving, the end of the stick would end up pointing slightly to the side, along the direction of the new  $\mathbf{L}$ .<sup>21</sup> But the sideways motion of the top (due to the properly chosen original speed we gave it) exactly brings the end of the stick back to its original location; see the top view in Fig. 9.37. The dot in the figure represents a fixed point in space. We can imagine this process taking place in two steps. In step 1, the axis changes its direction due to the angular impulse relative to the CM. And in step 2, the top moves sideways (due to the original horizontal speed we gave it) during its rising and falling projectile motion. As the process repeats, the CM moves around in a circle,

![Figure 9.37: A top-down view diagram showing the precession of a spinning top's axis. The diagram is labeled '(top view)' and shows three stages: 'start:', 'step 1:', and 'step 2:'. In each stage, a vertical line represents the top's axis, with a dot at its base representing a fixed point in space. An arrow labeled 'v' points upwards from the base of the axis, indicating the direction of the angular velocity vector. In 'start:', the axis is perfectly vertical. In 'step 1:', the axis has tilted slightly to the right. In 'step 2:', the axis has tilted further to the right. A label 'disk' with an arrow points to the top of the axis in the 'start:' stage.](4820eaf26fcfc5fc443aa7158405f442_img.jpg)

Figure 9.37: A top-down view diagram showing the precession of a spinning top's axis. The diagram is labeled '(top view)' and shows three stages: 'start:', 'step 1:', and 'step 2:'. In each stage, a vertical line represents the top's axis, with a dot at its base representing a fixed point in space. An arrow labeled 'v' points upwards from the base of the axis, indicating the direction of the angular velocity vector. In 'start:', the axis is perfectly vertical. In 'step 1:', the axis has tilted slightly to the right. In 'step 2:', the axis has tilted further to the right. A label 'disk' with an arrow points to the top of the axis in the 'start:' stage.

**Fig. 9.37**

<sup>21</sup> Assume that the stick's tiny precession cone around  $\mathbf{L}$  somehow damps out, so that the stick eventually points in the definite direction along  $\mathbf{L}$ . Since we're eventually going to consider the end of the stick to be located at a pivot, this is a reasonable assumption.

with the end of the stick remaining (essentially) fixed.<sup>22</sup> In other words, we have recreated our precessing top.<sup>23</sup> And since we can consider the continuous upward force that a pivot applies to a heavy top to be a succession of quick infinitesimal strikes, we see that a heavy top precessing around a pivot is essentially the same as the above top precessing around the fixed dot in space in Fig. 9.37.

The above reasoning is only qualitative, but it should make the precession of a heavy top a little more believable. Of course, since we've argued that a heavy top pivoted at a point can be considered to be a free top undergoing a succession of impulsive and free-top motions, we've just shifted the burden of proof to an intuitive understanding of why a free top precesses the way it does. But that makes my head hurt, so I'll stop here. But at least we know that a free top should behave more or less like the dumbbell setup above, for which we showed (by actually looking at the forces) why the axis of rotation shifts to the side when vertical forces are applied.

#### 9.7.7 Nutation

We will now solve Eq. (9.70) in a somewhat more general case, where  $\theta$  is allowed to vary slightly. That is, we will consider a slight perturbation to the circular motion associated with Eq. (9.75). We will assume that  $\omega_3$  is large here, and we will assume that the original circular motion corresponds to the slow precession, so that  $\dot{\phi}$  is small. Under these assumptions, we will find that the top will bounce around slightly as it travels (roughly) in a circle. This bouncing is known as *nutation*.

Since  $\dot{\phi}$  is small compared with  $\omega_3$ , we can (to a good approximation) ignore the middle terms on the left-hand sides of Eqs. (9.70) to obtain

$$\begin{aligned} I\ddot{\phi} \sin \theta - \dot{\theta} I_3 \omega_3 &= 0, \\ (Mg\ell - I_3 \omega_3 \dot{\phi}) \sin \theta &= I\ddot{\theta}. \end{aligned} \quad (9.84)$$

We must somehow solve these equations for  $\theta(t)$  and  $\phi(t)$ . Taking the derivative of the first equation and dropping the quadratic term (which is negligible for sufficiently small perturbations) gives  $\ddot{\theta} = (I \sin \theta / I_3 \omega_3) d^2 \dot{\phi} / dt^2$ . Substituting this expression for  $\ddot{\theta}$  into the second equation gives

$$\frac{d^2 \dot{\phi}}{dt^2} + \omega_n^2 (\dot{\phi} - \Omega_s) = 0, \quad (9.85)$$

<sup>22</sup> We'll need to apply a force directed along the axis, to provide the centripetal acceleration of the precessing CM. But this force produces no torque around the CM, so it doesn't affect any of the other aspects of the problem.

<sup>23</sup> If the initial conditions aren't set up properly, then the top will bounce up and down as it precesses around (this is known as *nutation*, described below in Section 9.7.7). In particular, if you hold the axis at rest and then let go, the top will initially fall straight down. So your intuition works perfectly fine here. But as time goes by, more complicated things start to happen, as explained in Remark 6 in the nutation section below.

where

$$\omega_n \equiv \frac{I_3 \omega_3}{I} \quad \text{and} \quad \Omega_s = \frac{Mg\ell}{I_3 \omega_3} \quad (9.86)$$

are, respectively, the frequency of nutation (as we shall soon see) and the slow-precession frequency given in Eq. (9.77). Shifting variables to  $y \equiv \dot{\phi} - \Omega_s$  in Eq. (9.85) gives us the nice harmonic-oscillator equation,  $\ddot{y} + \omega_n^2 y = 0$ . Solving this and then shifting back to  $\dot{\phi}$  yields

$$\dot{\phi}(t) = \Omega_s + A \cos(\omega_n t + \gamma), \quad (9.87)$$

where  $A$  and  $\gamma$  are determined by the initial conditions. Integrating this gives

$$\phi(t) = \Omega_s t + \left( \frac{A}{\omega_n} \right) \sin(\omega_n t + \gamma), \quad (9.88)$$

plus an irrelevant constant.

Now let's solve for  $\theta(t)$ . Plugging our  $\phi(t)$  into the first of Eqs. (9.84) gives

$$\dot{\theta}(t) = - \left( \frac{I \sin \theta}{I_3 \omega_3} \right) A \omega_n \sin(\omega_n t + \gamma) = -A \sin \theta \sin(\omega_n t + \gamma), \quad (9.89)$$

where we have used the definition of  $\omega_n$  in Eq. (9.86). Since  $\theta(t)$  doesn't change much, we can set  $\sin \theta \approx \sin \theta_0$ , where  $\theta_0$  is, say, the initial value of  $\theta(t)$ . Any errors here will be second-order effects in small quantities. Integration then gives

$$\theta(t) = B + \left( \frac{A}{\omega_n} \sin \theta_0 \right) \cos(\omega_n t + \gamma), \quad (9.90)$$

where  $B$  is a constant of integration. Equations (9.88) and (9.90) show that both  $\phi$  (neglecting the uniform  $\Omega_s t$  part) and  $\theta$  oscillate with frequency  $\omega_n$ , and with amplitudes inversely proportional to  $\omega_n$ . Note that Eq. (9.86) says that  $\omega_n$  grows with  $\omega_3$ .

---

**Example (Sideways kick):** Assume that uniform circular precession is initially taking place with  $\theta = \theta_0$  and  $\dot{\phi} = \Omega_s$ . You then give the top a quick kick along the direction of motion, so that  $\dot{\phi}$  suddenly becomes  $\Omega_s + \Delta\Omega$  ( $\Delta\Omega$  may be positive or negative). Find  $\phi(t)$  and  $\theta(t)$ .

**Solution:** This is an exercise in initial conditions. We are given the initial values of  $\dot{\phi}$ ,  $\dot{\theta}$ , and  $\theta$  (namely  $\Omega_s + \Delta\Omega$ , 0, and  $\theta_0$ , respectively), and our goal is to solve for the unknowns  $A$ ,  $B$ , and  $\gamma$  in Eqs. (9.87), (9.89), and (9.90).  $\dot{\theta}$  is initially zero, so Eq. (9.89) gives  $\gamma = 0$  (or  $\pi$ , but this leads to the same answer). And  $\dot{\phi}$  is initially  $\Omega_s + \Delta\Omega$ , so Eq. (9.87) gives  $A = \Delta\Omega$ . Finally,  $\theta$  is initially  $\theta_0$ , so Eq. (9.90) gives  $B = \theta_0 - (\Delta\Omega/\omega_n) \sin \theta_0$ . Putting this all together, we have

$$\begin{aligned} \phi(t) &= \Omega_s t + \left( \frac{\Delta\Omega}{\omega_n} \right) \sin \omega_n t, \\ \theta(t) &= \theta_0 - \left( \frac{\Delta\Omega}{\omega_n} \sin \theta_0 \right) (1 - \cos \omega_n t). \end{aligned} \quad (9.91)$$

And for future reference (for the problems in this chapter), we'll also list the derivatives,

$$\begin{aligned}\dot{\phi}(t) &= \Omega_s + \Delta\Omega \cos \omega_n t, \\ \dot{\theta}(t) &= -\Delta\Omega \sin \theta_0 \sin \omega_n t.\end{aligned}\quad (9.92)$$

##### REMARKS:

1. Remember that all of this analysis holds only if  $\dot{\theta}$  and  $\dot{\phi}$  are small compared with  $\omega_3$ , and if  $\theta$  is always near  $\theta_0$ .
2. For the initial setup we have chosen (that is, for  $\dot{\theta} = 0$ ), Eq. (9.91) shows that  $\theta$  always stays on one side of  $\theta_0$ . If  $\Delta\Omega > 0$ , then  $\theta(t) \leq \theta_0$  for all  $t$  (that is, the top is always at a higher position, since  $\theta$  is measured from the vertical). If  $\Delta\Omega < 0$ , then  $\theta(t) \geq \theta_0$  for all  $t$  (that is, the top is always at a lower position).
3. Consider the point that is a distance  $\ell$  from the origin and that travels in a horizontal circle with angular coordinates given by  $(\phi, \theta)_{\text{avg}} = (\Omega_s t, \theta_0 - (\Delta\Omega/\omega_n) \sin \theta_0)$ . This is the “average” position of the CM, in the sense that Eq. (9.91) gives the angular coordinates of the CM relative to this point as

$$(\phi, \theta)_{\text{rel}} = \left( \frac{\Delta\Omega}{\omega_n} \right) (\sin \omega_n t, \sin \theta_0 \cos \omega_n t). \quad (9.93)$$

The  $\sin \theta_0$  in the second coordinate here implies that the amplitude of the  $\theta$  oscillation is  $\sin \theta_0$  times the amplitude of the  $\phi$  oscillation. This is precisely the factor needed to make the CM travel in a circle, as viewed by someone riding along with coordinates  $(\phi, \theta)_{\text{avg}}$ , because a change in  $\theta$  causes a displacement of  $\ell d\theta$ , whereas a change in  $\phi$  causes a displacement of  $\ell \sin \theta_0 d\phi$ .

4. Figure 9.38 shows plots of  $\theta(t)$  vs.  $\sin \theta_0 \phi(t)$  for various values of  $\Delta\Omega$ . The dots at the start of each of the nine plots all represent the same starting point at  $\theta = \theta_0$ . The plots are stacked on top of each other for comparison only; the vertical spacing between them is meaningless. We have chosen the horizontal axis to be  $\sin \theta_0 \phi(t)$  instead of  $\phi(t)$ , and we have chosen the vertical axis to have  $\theta$  increasing downward, so that these plots are exactly the paths you would see the CM trace out in space. We have picked arbitrary values of  $\Omega_s$  and  $\omega_n$  to generate the plots (hence no numbers on the axes, since they wouldn't mean much), but no matter what values are picked, the shapes of the plots are still the same (for example, the  $\Delta\Omega = \pm\Omega_s$  paths always have cusps). The oscillations have different frequencies and amplitudes, but both axes get scaled by the same amount (as you can check).
5. From the figure, we see that the motions associated with  $\Delta\Omega$  and  $-\Delta\Omega$  look the same except for being shifted vertically (relative to the starting dots, which represent the same point), and also horizontally by half a cycle. This can be seen from Eq. (9.91); changing  $\Delta\Omega$  to  $-\Delta\Omega$  has the effect of shifting the constant term in  $\theta(t)$ , and also shifting the time by half a cycle, because  $\Delta\Omega \sin \omega_n t = (-\Delta\Omega) \sin(\omega_n t + \pi)$ , and likewise for cosine.
6. In the  $\Delta\Omega = -\Omega_s$  case, the CM starts at rest. This corresponds to holding the axis of the top at rest and then dropping it. From Fig. 9.38 we see that initially the CM simply falls straight down, as your intuition suggests. (It might not be clear from the figure, but Problem 9.25 shows that the curve is indeed vertical at the high points in the motion.) But then the strangeness of angular momentum takes over, and the top ends up bouncing and precessing instead of continuing to fall as a point mass would. Qualitatively, we can understand this bouncing and precessing as follows. Let the axis and the angular momentum initially point to the right as you hold the axis, as

![Figure 9.38: A graph showing the time evolution of the angle theta(t) for various changes in angular velocity Delta Omega. The vertical axis is labeled theta(t) with a downward arrow. The horizontal axis is labeled sin(theta_0) phi(t) with a rightward arrow. The graph displays a series of horizontal lines, each corresponding to a different value of Delta Omega. The lines are labeled from top to bottom: Delta Omega = 10 Omega_s, Delta Omega = 4 Omega_s, Delta Omega = 2 Omega_s, Delta Omega = Omega_s, Delta Omega = 1/2 Omega_s, Delta Omega = 0, Delta Omega = -1/2 Omega_s, Delta Omega = -Omega_s, and Delta Omega = -2 Omega_s. The lines show different types of oscillatory motion: large loops for high Delta Omega, smaller loops for intermediate Delta Omega, and simple sinusoidal waves for low Delta Omega. The Delta Omega = 0 line is a straight horizontal line.](3fd4737856d671306b269e10f3ae9ec3_img.jpg)

Figure 9.38: A graph showing the time evolution of the angle theta(t) for various changes in angular velocity Delta Omega. The vertical axis is labeled theta(t) with a downward arrow. The horizontal axis is labeled sin(theta\_0) phi(t) with a rightward arrow. The graph displays a series of horizontal lines, each corresponding to a different value of Delta Omega. The lines are labeled from top to bottom: Delta Omega = 10 Omega\_s, Delta Omega = 4 Omega\_s, Delta Omega = 2 Omega\_s, Delta Omega = Omega\_s, Delta Omega = 1/2 Omega\_s, Delta Omega = 0, Delta Omega = -1/2 Omega\_s, Delta Omega = -Omega\_s, and Delta Omega = -2 Omega\_s. The lines show different types of oscillatory motion: large loops for high Delta Omega, smaller loops for intermediate Delta Omega, and simple sinusoidal waves for low Delta Omega. The Delta Omega = 0 line is a straight horizontal line.

Fig. 9.38

![Figure 9.39: A diagram of a spinning top. The top is shown as a vertical ellipse with a curved arrow indicating rotation. A horizontal line represents the axis of the top, which is pivoted at a point on the left. A vector labeled L points to the right from the center of the top, representing the angular momentum.](b1b6baa0f29d393553bf67899752ff8b_img.jpg)

Figure 9.39: A diagram of a spinning top. The top is shown as a vertical ellipse with a curved arrow indicating rotation. A horizontal line represents the axis of the top, which is pivoted at a point on the left. A vector labeled L points to the right from the center of the top, representing the angular momentum.

Fig. 9.39

- shown in Fig. 9.39. After you let go, a number of things happen: (1) Because of the downward gravitational force, the top starts to fall. The axis therefore now points slightly downward, which means that the angular momentum picks up a downward component. Relative to the CM, the force from the pivot must therefore provide a downward torque. By the right-hand rule, this force must point into the page. (2) From  $F = ma$ , this inward force causes the top to accelerate into the page. This makes the axis point slightly into the page, so the angular momentum picks up a component in that direction. By the right-hand rule, there must then be an upward force from the pivot to provide the necessary torque for this. (3) This upward force slows down the downward motion and in fact eventually becomes greater than  $mg$  and causes the CM to rise back up. This means that the angular momentum increases its vertical component, so by the right-hand rule there must be a force from the pivot that points out of the page to provide the necessary torque for this. (4) This outward force then slows down the motion into the page and eventually stops it, right when the top returns to its original height. The top is momentarily at rest, and then the process repeats itself. Of course, this qualitative reasoning doesn't show that all the details work out correctly, but at least it makes the motion a little more believable.
- 7. If you start by holding the axis of the top at rest, as in the previous remark, the  $\Delta\Omega = 0$  case corresponds to giving the axis the proper initial push into the page (instead of just dropping it, as above) so that the resulting change in angular momentum into the page requires an upward force of  $mg$  from the pivot. The CM then stays at the same height and simply moves in a horizontal circle without bouncing. ♣

### 9.8 Problems

### Section 9.1: Preliminaries concerning rotations

#### 9.1. Many different $\omega$ 's \*

Consider a particle at the point  $(a, 0, 0)$ , with velocity  $(0, v, 0)$ . At this instant, the particle may be considered to be rotating around many different  $\omega$  vectors passing through the origin. There isn't just one "correct"  $\omega$ . Find all the possible  $\omega$ 's (give their directions and magnitudes).

### 9.2. Fixed points on a sphere \*\*

Consider a transformation of a rigid sphere into itself. Show that two points on the sphere end up where they started.

#### 9.3. Rolling cone \*\*

A cone rolls without slipping on a table. The half-angle at the vertex is  $\alpha$ , and the axis has length  $h$  (see Fig. 9.40). Let the speed of the center of the base, point  $P$  in the figure, be  $v$ . What is the angular velocity of the cone with respect to the lab frame at the instant shown? There are many ways to do this problem, so you are encouraged to take a look at the three given solutions, even after solving it.

![Diagram of a cone rolling on a horizontal surface. The cone's vertex is at the origin, and its axis of length h makes an angle alpha with the vertical. The center of the base is point P. A dashed line shows the cone's position at a later time, and a curved arrow indicates the rotation.](fc1cde212d1092a7a422ef902900c375_img.jpg)

Diagram of a cone rolling on a horizontal surface. The cone's vertex is at the origin, and its axis of length h makes an angle alpha with the vertical. The center of the base is point P. A dashed line shows the cone's position at a later time, and a curved arrow indicates the rotation.

Fig. 9.40

### Section 9.2: The inertia tensor

#### 9.4. Parallel-axis theorem

Let  $(X, Y, Z)$  be the position of an object's CM, and let  $(x', y', z')$  be the position relative to the CM. Prove the parallel-axis theorem, Eq. (9.19), by setting  $x = X + x'$ ,  $y = Y + y'$ , and  $z = Z + z'$  in Eq. (9.8).

### Section 9.3: Principal axes

#### 9.5. A nice cylinder \*

What must the ratio of height to radius of a cylinder be so that every axis is a principal axis (with the CM as the origin)?

#### 9.6. Rotating square \*

Here's an exercise in geometry. Theorem 9.5 says that if the moments of inertia around two principal axes are equal, then any axis in the plane of these axes is a principal axis. This means that the object will happily rotate around any axis in this plane, that is, no torque is needed. Demonstrate this explicitly for four equal masses in the shape of a square, with the center as the origin, which obviously has two moments equal. Assume that the masses are connected by strings to the axis, as shown in Fig. 9.41, and that they all rotate with the same  $\omega$  around the axis, so that they remain in the shape of a square. Your task is to show that the tensions in the strings

![Diagram showing four masses (dots) arranged in a square, connected by strings to a central vertical axis of rotation. The axis is labeled with an angular velocity omega. The strings are shown as dashed lines.](385f77cc30987656c434c9897845ffe5_img.jpg)

Diagram showing four masses (dots) arranged in a square, connected by strings to a central vertical axis of rotation. The axis is labeled with an angular velocity omega. The strings are shown as dashed lines.

Fig. 9.41

are such that there is no net torque acting on the axis, relative to the center of the square.

#### 9.7. Existence of principal axes for a pancake \*

Given a pancake object in the  $x$ - $y$  plane, show that there exist principal axes by considering what happens to the integral  $\int xy$  when the coordinate axes are rotated about the origin by an angle of  $\pi/2$ .

#### 9.8. Symmetries and principal axes for a pancake \*\*

A rotation of the axes in the  $x$ - $y$  plane through an angle  $\theta$  transforms the coordinates according to (you can accept this)

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}. \quad (9.94)$$

Use this to show that if a pancake object in the  $x$ - $y$  plane has a symmetry under a rotation through  $\theta \neq \pi$ , then  $\int xy = 0$  for any choice of axes, which implies that all axes (through the origin) in the plane are principal axes.

![Diagram of a rectangle with width 'a' and height 'b'. A force 'F' is applied at the top-left corner, directed out of the page (indicated by a circle with a dot). Another force 'F' is applied at the bottom-right corner, directed into the page (indicated by a circle with a cross).](71665dea8564cd95493d0c0f7e37b018_img.jpg)

Diagram of a rectangle with width 'a' and height 'b'. A force 'F' is applied at the top-left corner, directed out of the page (indicated by a circle with a dot). Another force 'F' is applied at the bottom-right corner, directed into the page (indicated by a circle with a cross).

Fig. 9.42

![Diagram of a thin rod of length 'l' and mass 'm'. The rod is tilted at an angle 'theta' from the vertical. A vertical dashed line represents the axis of rotation. A curved arrow indicates an angular velocity 'omega' around this axis. The rod is perpendicular to the axis at both ends, as indicated by right-angle symbols.](f68a69ef7151355b76120c75fb47b0aa_img.jpg)

Diagram of a thin rod of length 'l' and mass 'm'. The rod is tilted at an angle 'theta' from the vertical. A vertical dashed line represents the axis of rotation. A curved arrow indicates an angular velocity 'omega' around this axis. The rod is perpendicular to the axis at both ends, as indicated by right-angle symbols.

Fig. 9.43

![Diagram of a stick of length 'l' and mass 'm'. The stick is tilted at an angle 'theta' from the vertical. The center of mass (CM) is marked on the stick. The top end of the stick slides along a horizontal dashed circle, indicating circular motion. A curved arrow indicates the direction of rotation.](2fc9d9a030ab35cec7bf60c7ebd6b54f_img.jpg)

Diagram of a stick of length 'l' and mass 'm'. The stick is tilted at an angle 'theta' from the vertical. The center of mass (CM) is marked on the stick. The top end of the stick slides along a horizontal dashed circle, indicating circular motion. A curved arrow indicates the direction of rotation.

Fig. 9.44

### Section 9.4: Two basic types of problems

#### 9.9. Striking a rectangle \*

A flat uniform rectangle with sides of length  $a$  and  $b$  sits in space, not rotating. You strike the corners at the ends of one diagonal, with equal and opposite forces (see Fig. 9.42). Show that the resulting initial  $\omega$  points along the other diagonal.

#### 9.10. Rotating stick \*\*

A stick of mass  $m$  and length  $\ell$  spins with frequency  $\omega$  around an axis, as shown in Fig. 9.43. The stick makes an angle  $\theta$  with the axis and is kept in its motion by two strings that are perpendicular to the axis. What is the tension in the strings? (Ignore gravity.)

#### 9.11. Stick under a ring \*\*

A stick of mass  $m$  and length  $\ell$  is arranged to have its CM motionless while its top end slides in a circle on a frictionless ring, as shown in Fig. 9.44. The stick makes an angle  $\theta$  with the vertical. What is the frequency of this motion?

#### 9.12. Circular pendulum \*\*

Consider a pendulum made of a massless rod of length  $\ell$  with a point mass  $m$  on the end. Assume conditions have been set up so that the mass moves in a horizontal circle. Let  $\theta$  be the constant angle the rod makes

with the vertical. Find the frequency,  $\Omega$ , of this circular motion in three different ways.

- Use  $\mathbf{F} = m\mathbf{a}$ . This method works only if you have a point mass. With an extended object, you have to use one of the following methods involving torque.
- Use  $\boldsymbol{\tau} = d\mathbf{L}/dt$  with the pendulum pivot as the origin.
- Use  $\boldsymbol{\tau} = d\mathbf{L}/dt$  with the mass as the origin.

#### 9.13. Rolling in a cone \*\*

A fixed cone stands on its tip, with its axis in the vertical direction. The half-angle at the vertex is  $\theta$ . A small ring of radius  $r$  rolls without slipping on the inside surface. Assume that conditions have been set up so that (1) the point of contact between the ring and the cone moves in a circle at height  $h$  above the tip, and (2) the plane of the ring is at all times perpendicular to the line joining the point of contact and the tip of the cone (see Fig. 9.45). What is the frequency,  $\Omega$ , of this circular motion? Work in the approximation where  $r$  is much smaller than the radius of the circular motion,  $h \tan \theta$ .

![Diagram of a ring rolling inside a cone. The cone has a half-angle 2θ at its vertex. A small ring is shown at a height h above the tip, moving in a circular path. The angular frequency of this circular motion is labeled Ω. The ring's plane is perpendicular to the line connecting the tip to the point of contact.](7a95b154fe373dc33292713e038366e7_img.jpg)

Diagram of a ring rolling inside a cone. The cone has a half-angle 2θ at its vertex. A small ring is shown at a height h above the tip, moving in a circular path. The angular frequency of this circular motion is labeled Ω. The ring's plane is perpendicular to the line connecting the tip to the point of contact.

Fig. 9.45

### Section 9.5: Euler's equations

#### 9.14. Tennis racket theorem \*\*\*

If you try to spin a tennis racket (or a book, etc.) around any of its three principal axes, you will find that different things happen with the different axes. Assuming that the principal moments (relative to the CM) are labeled according to  $I_1 > I_2 > I_3$  (see Fig. 9.46), you will find that the racket will spin nicely around the  $\hat{\mathbf{x}}_1$  and  $\hat{\mathbf{x}}_3$  axes, but it will wobble in a rather messy manner around the  $\hat{\mathbf{x}}_2$  axis. Verify this claim experimentally with a book (preferably lightweight, and wrapped with a rubber band), or a tennis racket, if you happen to study with one on hand.

Now verify this claim mathematically. The main point here is that you can't start the motion off with  $\boldsymbol{\omega}$  pointing *exactly* along a principal axis. Therefore, what you want to show is that the motion around the  $\hat{\mathbf{x}}_1$  and  $\hat{\mathbf{x}}_3$  axes is *stable* (that is, small errors in the initial conditions remain small), whereas the motion around the  $\hat{\mathbf{x}}_2$  axis is *unstable* (that is, small errors in the initial conditions get larger and larger, until the motion eventually doesn't resemble a rotation around the  $\hat{\mathbf{x}}_2$  axis).<sup>24</sup> Your task is to use Euler's equations to prove these statements about stability. (Exercise 9.33 gives another derivation of this result.)

![Diagram of a tennis racket in a 3D coordinate system. The axes are labeled x1, x2, and x3. The x3 axis is vertical, passing through the center of the racket's face. The x2 axis is horizontal, pointing to the right. The x1 axis is diagonal, pointing down and to the left. The racket's face is a grid pattern.](f916137f00267a7b5e68d436f3621c4c_img.jpg)

Diagram of a tennis racket in a 3D coordinate system. The axes are labeled x1, x2, and x3. The x3 axis is vertical, passing through the center of the racket's face. The x2 axis is horizontal, pointing to the right. The x1 axis is diagonal, pointing down and to the left. The racket's face is a grid pattern.

Fig. 9.46

<sup>24</sup> If you try for a long enough time, you'll probably be able to get the initial  $\boldsymbol{\omega}$  pointing close enough to  $\hat{\mathbf{x}}_2$  so that the book will remain rotating (almost) around  $\hat{\mathbf{x}}_2$  for the entire time of its flight. There is, however, undoubtedly a better use for your time, as well as for the book...

![Figure 9.47: A vector diagram showing the relationship between angular momentum L, angular velocity ω, and the symmetry axis x̂₃. L is a vertical vector. x̂₃ is a vector at an angle α from L. ω is a vector at an angle β from x̂₃. All three vectors lie in the same plane.](82c6ea9a13539ddfdfb0667001a9c4d9_img.jpg)

Figure 9.47: A vector diagram showing the relationship between angular momentum L, angular velocity ω, and the symmetry axis x̂₃. L is a vertical vector. x̂₃ is a vector at an angle α from L. ω is a vector at an angle β from x̂₃. All three vectors lie in the same plane.

Fig. 9.47

![Figure 9.48: A diagram of a spinning top. The top is an ellipsoid with a vertical axis of symmetry. An upward arrow from the top is labeled ω₃. A downward arrow from the bottom point is labeled ⊗ F, indicating a force directed into the page.](4e7b02d22ee6d4861403efd400a023cb_img.jpg)

Figure 9.48: A diagram of a spinning top. The top is an ellipsoid with a vertical axis of symmetry. An upward arrow from the top is labeled ω₃. A downward arrow from the bottom point is labeled ⊗ F, indicating a force directed into the page.

Fig. 9.48

![Figure 9.49: A diagram showing a series of N identical disks and massless sticks. The leftmost stick is attached to a vertical pole by a pivot. The sticks are arranged in a horizontal line, with each disk glued to the left stick and attached to the right stick by a pivot. The disks are shown in perspective, and the entire assembly is rotating about the vertical pole.](8371141e3e0bc56a01e2f04f1cffbc47_img.jpg)

Figure 9.49: A diagram showing a series of N identical disks and massless sticks. The leftmost stick is attached to a vertical pole by a pivot. The sticks are arranged in a horizontal line, with each disk glued to the left stick and attached to the right stick by a pivot. The disks are shown in perspective, and the entire assembly is rotating about the vertical pole.

Fig. 9.49

![Figure 9.50: A diagram of a heavy symmetric top spinning on a frictionless horizontal table. The top is shown in a tilted position, with its point of contact on the table. The word 'frictionless' is written on the table surface.](6478a6722d83cdc81f2e109b31ff5c8b_img.jpg)

Figure 9.50: A diagram of a heavy symmetric top spinning on a frictionless horizontal table. The top is shown in a tilted position, with its point of contact on the table. The word 'frictionless' is written on the table surface.

Fig. 9.50

### Section 9.6: Free symmetric top

#### 9.15. Free-top angles \*

In Section 9.6.2, we showed that for a free symmetric top, the angular momentum  $\mathbf{L}$ , the angular velocity  $\boldsymbol{\omega}$ , and the symmetry axis  $\hat{\mathbf{x}}_3$  all lie in a plane. Let  $\alpha$  be the angle between  $\hat{\mathbf{x}}_3$  and  $\mathbf{L}$ , and let  $\beta$  be the angle between  $\hat{\mathbf{x}}_3$  and  $\boldsymbol{\omega}$  (see Fig. 9.47). Find the relationship between  $\alpha$  and  $\beta$  in terms of the principal moments,  $I$  and  $I_3$ .

#### 9.16. Staying above \*\*

A top with  $I = nI_3$ , where  $n$  is a numerical factor, is initially spinning around its  $x_3$  axis with angular speed  $\omega_3$ . You apply a strike at the bottom point, directed into the page as shown in Fig. 9.48 (imagine that you hit a little peg protruding from the bottom). What is the largest value of  $n$  for which the total  $\boldsymbol{\omega}$  vector never dips below the horizontal axis in the subsequent motion, no matter how hard your strike is?

### Section 9.7: Heavy symmetric top

#### 9.17. The top \*\*

This problem deals with the spinning top example in Section 9.7.5. It uses the result for  $\Omega$  in Eq. (9.82).

- What is the minimum value of  $\omega_3$  for which circular precession is possible?
- Find approximate expressions for  $\Omega_{\pm}$  when  $\omega_3$  is very large. The phrase “very large,” however, is rather meaningless. What mathematical statement should replace it?

#### 9.18. Many tops \*\*

$N$  identical disks and massless sticks are arranged as shown in Fig. 9.49. Each disk is glued to the stick on its left and attached by a pivot to the stick on its right. The leftmost stick is attached by a pivot to a pole. You wish to set up circular precession with the sticks always forming a straight horizontal line. What should the relative angular speeds of the disks be so that this is possible?

#### 9.19. Heavy top on a slippery table \*\*

Solve the problem of a heavy symmetric top spinning on a frictionless table (see Fig. 9.50). You may do this by simply stating what modifications are needed in the derivation in Section 9.7.3 (or Section 9.7.4).

#### 9.20. **Fixed highest point \*\***

Consider a top made of a uniform disk of radius  $R$ , connected to the origin by a massless stick (which is glued perpendicular to the disk) of length  $\ell$ . Paint a dot on the top at its highest point, and label this as point  $P$  (see Fig. 9.51). You wish to set up uniform circular precession, with the stick making a constant angle  $\theta$  with the vertical ( $\theta$  can be chosen to be any angle between zero and  $\pi$ ), and with  $P$  always being the highest point on the top. What is the frequency of precession,  $\Omega$ ? What relation between  $R$  and  $\ell$  must be satisfied for this motion to be possible?

![Diagram of a spinning top precessing. The top is a disk of radius R, tilted at an angle theta from the vertical. A massless stick of length l connects the center of the disk to the origin. Point P is marked at the highest point on the disk. A dashed circle indicates the path of the top's center during precession.](bd569de7efaec305bd6b7a082700dc26_img.jpg)

Diagram of a spinning top precessing. The top is a disk of radius R, tilted at an angle theta from the vertical. A massless stick of length l connects the center of the disk to the origin. Point P is marked at the highest point on the disk. A dashed circle indicates the path of the top's center during precession.

Fig. 9.51

#### 9.21. **Basketball on a rim \*\*\***

A basketball rolls without slipping around a basketball rim in such a way that the contact points trace out a great circle on the ball, and the CM moves around in a horizontal circle with frequency  $\Omega$ . The radii of the ball and rim are  $r$  and  $R$ , respectively, and the ball's radius to the contact point makes an angle  $\theta$  with the horizontal (see Fig. 9.52). Assume that the ball's moment of inertia around its center is  $I = (2/3)mr^2$ . Find  $\Omega$ .

![Diagram of a basketball rolling around a rim. The ball has radius r and the rim has radius R. The ball's center of mass moves in a horizontal circle. The radius from the ball's center to the contact point makes an angle theta with the horizontal. The ball is shown rolling without slipping.](e18917caa2d8ae57b8f993cf1eb1a31a_img.jpg)

Diagram of a basketball rolling around a rim. The ball has radius r and the rim has radius R. The ball's center of mass moves in a horizontal circle. The radius from the ball's center to the contact point makes an angle theta with the horizontal. The ball is shown rolling without slipping.

Fig. 9.52

#### 9.22. **Rolling lollipop \*\*\***

Consider a lollipop made of a solid sphere of mass  $m$  and radius  $r$  that is radially pierced by a massless stick. The free end of the stick is pivoted on the ground (see Fig. 9.53). The sphere rolls on the ground without slipping, with its center moving in a circle of radius  $R$  with frequency  $\Omega$ . What is the normal force between the ground and the sphere?

![Diagram of a rolling lollipop. A solid sphere of mass m and radius r is attached to a massless stick of length R. The stick is pivoted at one end on the ground. The sphere rolls without slipping on the ground. The center of mass moves in a circle of radius R with frequency Omega.](40f565b14070825c83a05554ee8bf02d_img.jpg)

Diagram of a rolling lollipop. A solid sphere of mass m and radius r is attached to a massless stick of length R. The stick is pivoted at one end on the ground. The sphere rolls without slipping on the ground. The center of mass moves in a circle of radius R with frequency Omega.

Fig. 9.53

#### 9.23. **Rolling coin \*\*\***

Initial conditions have been set up so that a coin of radius  $r$  rolls around in a circle, as shown in Fig. 9.54. The contact point on the ground traces out a circle of radius  $R$ , and the coin makes a constant angle  $\theta$  with the horizontal. The coin rolls without slipping (assume that the friction with the ground is as large as needed). What is the frequency,  $\Omega$ , of the circular motion of the contact point on the ground? Show that such motion exists only if  $R > (5/6)r \cos \theta$ .

![Diagram of a rolling coin. A coin of radius r rolls around a circle of radius R on a horizontal surface. The coin makes a constant angle theta with the horizontal. The contact point traces out a circle of radius R.](94093ba17eef8fafa831d1aa8ac44bc4_img.jpg)

Diagram of a rolling coin. A coin of radius r rolls around a circle of radius R on a horizontal surface. The coin makes a constant angle theta with the horizontal. The contact point traces out a circle of radius R.

Fig. 9.54

#### 9.24. **Wobbling coin \*\*\***

If you spin a coin around a vertical diameter on a table, it will slowly lose energy and begin a wobbling motion. The angle between the coin and the table will gradually decrease, and eventually it will come to rest. Assume that this process is slow, and consider the motion when the coin makes an angle  $\theta$  with the table (see Fig. 9.55). You may assume that the CM is essentially motionless. Let  $R$  be the radius of the coin, and let  $\Omega$  be the frequency at which the contact point on the table traces out its circle. Assume that the coin rolls without slipping.

![Diagram of a wobbling coin. A coin of radius R is tilted at an angle theta from the horizontal table. The contact point traces out a circle of radius R on the table with frequency Omega. A coordinate system (x2, x3) is shown with the origin at the contact point.](5af13b9a44178253bffe66402e4362e8_img.jpg)

Diagram of a wobbling coin. A coin of radius R is tilted at an angle theta from the horizontal table. The contact point traces out a circle of radius R on the table with frequency Omega. A coordinate system (x2, x3) is shown with the origin at the contact point.

Fig. 9.55

- (a) Show that the angular velocity of the coin is  $\boldsymbol{\omega} = \Omega \sin \theta \hat{\mathbf{x}}_2$ , where  $\hat{\mathbf{x}}_2$  points upward along the coin, directly away from the contact point.
- (b) Show that

$$\Omega = 2\sqrt{\frac{g}{R \sin \theta}}. \quad (9.95)$$

- (c) Show that Abe (or Tom, Franklin, George, John, Dwight, Susan, or Sacagawea) appears to rotate, when viewed from above, with frequency

$$2(1 - \cos \theta)\sqrt{\frac{g}{R \sin \theta}}. \quad (9.96)$$

#### 9.25. Nutation cusps \*\*

- (a) Using the notation and initial conditions in the example in Section 9.7.7, prove that kinks occur in nutation if and only if  $\Delta\Omega = \pm\Omega_s$ . A kink is where the plot of  $\theta(t)$  vs.  $\phi(t)$  has a discontinuity in its slope.
- (b) Prove that these kinks are in fact cusps. A cusp is a kink where the plot reverses direction in the  $\phi$ - $\theta$  plane.

#### 9.26. Nutation circles \*\*

- (a) Using the notation and initial conditions in the example in Section 9.7.7, and assuming that  $\omega_3 \gg \Delta\Omega \gg \Omega_s$ , find (approximately) the direction of the angular momentum right after the sideways kick takes place.
- (b) Use Eq. (9.91) to show that the CM then travels (approximately) in a circle around  $\mathbf{L}$ . And show that this “circular” motion is just what you would expect from the free-top reasoning in Section 9.6.2, in particular, Eq. (9.55).

#### *Additional problems*

#### 9.27. Rolling without slipping \*

The standard way that a ball rolls without slipping on a flat surface is for the contact points on the ball to trace out a vertical great circle on the ball. Are there any other ways that a ball can roll without slipping?

#### 9.28. Rolling straight? \*\*

In some situations, such as the rolling-coin setup in Problem 9.23, the velocity of the CM of a rolling object changes direction as time goes by. Consider a uniform sphere that rolls on the ground without slipping (possibly in the nonstandard way described in the solution to Problem 9.27).

Is it possible for the CM's velocity to change direction? Justify your answer rigorously.

#### 9.29. **Ball on paper** \*\*\*

A uniform ball rolls without slipping on a table (possibly in the non-standard way described in the solution to Problem 9.27). It rolls onto a piece of paper, which you then slide around in an arbitrary (horizontal) manner. You may even give the paper abrupt, jerky motions, so that the ball slips with respect to it. After you allow the ball to come off the paper, it will eventually resume rolling without slipping on the table. Show that the final velocity equals the initial velocity.

#### 9.30. **Ball on a turntable** \*\*\*\*

A uniform ball rolls without slipping on a turntable (possibly in the nonstandard way described in the solution to Problem 9.27). As viewed from the inertial lab frame, show that the ball moves in a circle (not necessarily centered at the center of the turntable) with a frequency equal to  $2/7$  times the frequency of the turntable.

### 9.9 Exercises

### Section 9.1: Preliminaries concerning rotations

#### 9.31. **Rolling wheel** \*\*

A wheel with spokes rolls without slipping on the ground. A stationary camera takes a picture of it as it rolls by, from the side. Due to the nonzero exposure time of the camera, the spokes generally appear blurred. At what locations in the picture do the spokes *not* appear blurred? *Hint:* A common incorrect answer is that there is only one point.

### Section 9.2: The inertia tensor

#### 9.32. **Inertia tensor** \*

Calculate the  $\mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r})$  double cross product in Eq. (9.7) by using the vector identity,

$$\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A} \cdot \mathbf{C}) - \mathbf{C}(\mathbf{A} \cdot \mathbf{B}). \quad (9.97)$$

### Section 9.3: Principal axes

#### 9.33. **Tennis racket theorem** \*\*

Problem 9.14 gives the statement of the “tennis racket theorem,” and the solution there involves Euler's equations. Demonstrate the theorem here by writing down the conservation of  $L^2$  and conservation of  $E$  statements and then using them in the following way. Produce an equation that says

that if  $\omega_2$  and  $\omega_3$  (or  $\omega_1$  and  $\omega_2$ ) start small, then they must remain small. And produce the analogous equation that says that if  $\omega_1$  and  $\omega_3$  start small, then they need *not* remain small. (It's another matter to show that they actually *won't* remain small. But let's not worry about that here. Anything that *can* happen generally *does* happen in physics.)

#### 9.34. Moments for a cube \*\*

In the spirit of Appendix E, calculate the principal moments for a solid cube of mass  $m$  and side length  $\ell$ , with the coordinate axes parallel to the edges of the cube, and the origin at a corner.

#### 9.35. Tilted moments \*\*

- Consider a planar object in the  $x$ - $y$  plane. If the  $x$  and  $y$  axes are principal axes, use the rotation matrix in Eq. (9.94) to show that the moment of inertia around the  $x'$  axis, which makes an angle  $\theta$  with the  $x$  axis, is  $I_{x'} = I_x \cos^2 \theta + I_y \sin^2 \theta$ .
- Consider a general three-dimensional object whose principal axes are the  $x$ ,  $y$ , and  $z$  axes. Consider another axis that points along the unit vector  $(\alpha, \beta, \gamma)$ . Show that the moment of inertia around this axis is  $\alpha^2 I_x + \beta^2 I_y + \gamma^2 I_z$ . *Hint:* The cross product, discussed in Appendix B, provides a nice method of calculating the distance from a point to a line.

#### 9.36. Quadrupole \*\*

Consider an arbitrarily shaped body of mass  $m$  whose CM is at the origin. Using the law of cosines, the gravitational potential of a mass  $M$  at position  $\mathbf{R}$  is

$$V(\mathbf{R}) = - \int \frac{GM \, dm}{\sqrt{R^2 + r^2 - 2Rr \cos \beta}}, \quad (9.98)$$

where the integration runs over the volume of the body, and  $\beta$  is the angle that the position vector  $\mathbf{r}$  of an arbitrary point in the body makes with the vector  $\mathbf{R}$ .

- Assuming that all points in the body satisfy  $r \ll R$ , show that an approximate expression for the potential is

$$V(\mathbf{R}) \approx -\frac{GMm}{R} - \frac{GM}{2R^3} \int r^2 (3 \cos^2 \beta - 1) \, dm, \quad (9.99)$$

and then show that this can be written as

$$V(\mathbf{R}) \approx -\frac{GMm}{R} - \frac{GM}{2R^3} (I_1 + I_2 + I_3 - 3I_R), \quad (9.100)$$

where  $I_1$ ,  $I_2$ , and  $I_3$  are the moments around any three orthogonal axes (which we'll take to be principal axes in part (b)), and  $I_R$  is the moment around the axis along the  $\mathbf{R}$  vector.

- (b) Consider now a planet with rotational symmetry around  $\hat{\mathbf{x}}_3$ , such as the earth which bulges at the equator due to the spinning. Using the result of Exercise 9.35, show that the potential in Eq. (9.100) can be written as

$$V(\mathbf{R}) \approx -\frac{GMm}{R} - \frac{GM}{2R^3}(I_3 - I)(1 - 3 \cos^2\theta), \quad (9.101)$$

where  $I \equiv I_1 = I_2$ , and  $\theta$  is the angle that  $\mathbf{R}$  makes with  $\hat{\mathbf{x}}_3$ .

REMARK: The second term here is known as the *quadrupole* term. In electrostatics, a *dipole* consists of equal and opposite charges separated by some distance  $d$ . At a given point far away, the forces from these two charges partially cancel. But they don't exactly cancel, because the electrostatic force (which behaves like the gravitational force, with a  $1/r^2$  law) depends on the distance and direction to the charges, and the two charges are located at different points. If two dipoles are oriented in opposite directions and then placed side by side, a distance  $d$  apart (so that there are charges of  $q$  and  $-q$  alternating around the corners of a square) then the forces from the dipoles nearly cancel. But again, the cancellation isn't exact, because the dipoles are located in different places. This distribution of charge is called a *quadrupole*, and it is similar to the situation with a spinning (and bulging) planet, because such a planet consists of a spherical ball (which gives rise to the first term in Eq. (9.101)), plus a region of "negative" mass superimposed on the ball at the poles and a region of positive mass superimposed on the ball at the equator. Looking at the above square of charges from far out along the diagonal containing the two negative charges is similar to looking at the earth from far out along its rotation axis. ♣

### Section 9.4: Two basic types of problems

### 9.37. Sphere and points \*

A uniform sphere of mass  $m$  and radius  $R$  rotates around the vertical axis with angular speed  $\omega$ . Two particles of mass  $m/2$  are brought close to the sphere at diametrically opposite points, at an angle  $\theta$  from the vertical, as shown in Fig. 9.56. The masses, which are initially essentially at rest, abruptly stick to the sphere. What angle does the resulting  $\omega$  make with the vertical? (If you want, you can check your answer by showing that the  $\theta$  that makes this angle maximum is  $\sin^{-1} \sqrt{7/9} \approx 61.9^\circ$ .)

![Diagram for problem 9.37: A sphere of mass m is shown with a vertical dashed line representing its axis of rotation. Two small dots, each labeled m/2, are positioned on the sphere's surface at diametrically opposite points. A dashed line from the center to one of the dots makes an angle theta with the vertical axis. A curved arrow at the top indicates rotation with angular speed omega.](8b5ca8d563daa4711d645542df7f8f0a_img.jpg)

Diagram for problem 9.37: A sphere of mass m is shown with a vertical dashed line representing its axis of rotation. Two small dots, each labeled m/2, are positioned on the sphere's surface at diametrically opposite points. A dashed line from the center to one of the dots makes an angle theta with the vertical axis. A curved arrow at the top indicates rotation with angular speed omega.

Fig. 9.56

#### 9.38. Striking a triangle \*\*

Consider the rigid object in Fig. 9.57. Four masses lie at the points shown on a rigid isosceles right triangle with hypotenuse length  $4a$ . The mass at the right angle is  $3m$ , and the other three masses are  $m$ . Label them  $A, B, C, D$ , as shown. Assume that the object is floating freely in outer space. Mass  $C$  is struck with a quick blow, directed into the page. Let the impulse have magnitude  $\int F dt = P$ . What are the velocities of all the masses immediately after the blow?

![Diagram for problem 9.38: A right-angled triangle with vertices labeled A, B, C, and D. The right angle is at vertex D, which has a mass of 3m. The other three vertices, A, B, and C, each have a mass of m. The sides AB and BC are each labeled 2a. The hypotenuse AC is labeled 4a. An arrow labeled F points into the page at vertex C, indicating the direction of the impulse.](babcf88960d25fce6480e22f90e3b9cc_img.jpg)

Diagram for problem 9.38: A right-angled triangle with vertices labeled A, B, C, and D. The right angle is at vertex D, which has a mass of 3m. The other three vertices, A, B, and C, each have a mass of m. The sides AB and BC are each labeled 2a. The hypotenuse AC is labeled 4a. An arrow labeled F points into the page at vertex C, indicating the direction of the impulse.

Fig. 9.57

![Diagram for Fig. 9.58: An isosceles triangle with base length b and height h. A mass M is at the base, and a mass m is at the top vertex. A force F is applied at the right end of the base, directed into the page (indicated by a cross in a circle).](cc1930a199c2e5cb36ec7ceac9619e7c_img.jpg)

Diagram for Fig. 9.58: An isosceles triangle with base length b and height h. A mass M is at the base, and a mass m is at the top vertex. A force F is applied at the right end of the base, directed into the page (indicated by a cross in a circle).

Fig. 9.58

![Diagram for Fig. 9.59: Two identical uniform sticks. The top stick is horizontal and rotating with angular speed ω. The bottom stick is vertical and rotating with angular speed ω in the opposite direction. The sticks are about to collide at the center of the top stick.](20096e6f7e23ff1939d76bfad776c386_img.jpg)

Diagram for Fig. 9.59: Two identical uniform sticks. The top stick is horizontal and rotating with angular speed ω. The bottom stick is vertical and rotating with angular speed ω in the opposite direction. The sticks are about to collide at the center of the top stick.

Fig. 9.59

![Diagram for Fig. 9.60: A stick of mass m and length l is pivoted at one end. The stick makes an angle θ with a vertical dashed axis. The stick is rotating with angular speed ω around this axis.](0e0444dc8cfeae5cc9c98a5b6f4f3f3f_img.jpg)

Diagram for Fig. 9.60: A stick of mass m and length l is pivoted at one end. The stick makes an angle θ with a vertical dashed axis. The stick is rotating with angular speed ω around this axis.

Fig. 9.60

![Diagram for Fig. 9.61: Two wheels of mass m and moment of inertia I are connected by a massless axle of length l. The system rotates with angular speed Ω around a vertical axis through the center of the axle. The wheels also rotate with angular speed ω around the axle.](93e4e06433eab6b33367c6dc09751ade_img.jpg)

Diagram for Fig. 9.61: Two wheels of mass m and moment of inertia I are connected by a massless axle of length l. The system rotates with angular speed Ω around a vertical axis through the center of the axle. The wheels also rotate with angular speed ω around the axle.

Fig. 9.61

#### 9.39. **Striking another triangle \*\***

Consider the rigid object in Fig. 9.58. A uniform stick of mass  $M$  lies along the base of an isosceles triangle, and a mass  $m$  lies at the opposite vertex. The base has length  $b$ , and the height is  $h$ . Assume that the object is floating freely in outer space. The right end of the stick is struck with a quick blow, directed into the page. Let the impulse have magnitude  $\int F dt = P$ . What is the velocity of mass  $m$  immediately after the blow?

#### 9.40. **Sticking sticks \*\***

Two identical uniform sticks spin around their stationary centers with equal angular speeds, as shown in Fig. 9.59. The bottom stick is slowly raised until its top end collides with the center of the top stick. The sticks stick together to form a rigid “T.” Assume that the collision takes place when the top stick lies in the plane of the paper. Immediately after the collision, one point (in addition to the CM) on the T will instantaneously be at rest. Where is this point?

#### 9.41. **Circling stick again \*\***

Solve the problem in Section 9.4.2 again, but now use the CM as the origin.

#### 9.42. **Pivot and string \*\***

A stick of mass  $m$  and length  $l$  spins with frequency  $\omega$  around an axis, as shown in Fig. 9.60. The stick makes an angle  $\theta$  with the axis. One end is pivoted on the axis, and the other end is connected to the axis by a string that is perpendicular to the axis. What is the tension in the string, and what is the force that the pivot applies to the stick? (Ignore gravity.)

#### 9.43. **Rotating sheet \*\***

A uniform flat rectangular sheet of mass  $m$  and side lengths  $a$  and  $b$  rotates with angular speed  $\omega$  around a diagonal. What torque is required? Given a fixed area  $A$ , what should the rectangle look like if you want the required torque to be as large as possible? What is the upper bound on the torque?

#### 9.44. **Rotating axle \*\***

Two wheels of mass  $m$  and moment of inertia  $I$  are connected by a massless axle of length  $l$ , as shown in Fig. 9.61. The system rests on a frictionless surface, and the wheels rotate with frequency  $\omega$  around the axle. Additionally, the whole system rotates with frequency  $\Omega$  around the vertical axis through the center of the axle. What is the largest value of  $\Omega$  for which both wheels stay on the ground?

#### 9.45. **Stick on a ring \*\***

- (a) A stick of mass  $m$  and length  $2r$  is arranged to make a constant angle  $\theta$  with the horizontal, with its bottom end sliding in a circle on a frictionless ring of radius  $r$ , as shown in Fig. 9.62. What is the frequency of this motion? It turns out that there is a minimum  $\theta$  for which this motion is possible; what is it?
- (b) If the radius of the ring is now  $R$ , what is the largest value of  $r/R$  for which this motion is possible for  $\theta \rightarrow 0$ ?<sup>25</sup>

![Diagram for Fig. 9.62: A stick of mass m and length 2r is shown at an angle theta to the horizontal. Its bottom end is sliding on a circular ring of radius r. A curved arrow indicates the direction of motion along the ring.](7d315e09d67f12c4cb363d77e2103f04_img.jpg)

Diagram for Fig. 9.62: A stick of mass m and length 2r is shown at an angle theta to the horizontal. Its bottom end is sliding on a circular ring of radius r. A curved arrow indicates the direction of motion along the ring.

Fig. 9.62

### Section 9.6: Free symmetric top

#### 9.46. **Slightly wobbling \***

A coin of mass  $m$  and radius  $R$  is initially spinning around the axis perpendicular to its plane, with angular speed  $\omega_3$ . It is supported by a pivot at its center. You apply an infinitesimal downward strike at a point on the rim, as shown in Fig. 9.63, giving the coin an infinitesimal angular velocity component  $\omega_\perp$  in the plane of the coin. When the plane of the coin returns to its original plane for the first time, what (approximately) is the orientation of the coin?

![Diagram for Fig. 9.63: A coin is shown as a horizontal ellipse. A vertical arrow labeled omega_3 points upwards from the center, representing the initial spin. A downward arrow labeled F points from a point on the rim, representing the strike.](f495be26cc92d6fad04eb8158af70ffa_img.jpg)

Diagram for Fig. 9.63: A coin is shown as a horizontal ellipse. A vertical arrow labeled omega\_3 points upwards from the center, representing the initial spin. A downward arrow labeled F points from a point on the rim, representing the strike.

Fig. 9.63

#### 9.47. **Original orientation \*\***

A coin of mass  $m$  and radius  $R$  is initially spinning around the axis perpendicular to its plane, with angular speed  $\omega_3$ . It is supported by a pivot at its center. You apply a (nonzero) downward strike at a point on the rim, as shown in Fig. 9.63, giving the coin an angular velocity component  $\omega_\perp$  in the plane of the coin. Consider the  $n$ th time the plane of the coin returns to its original plane. What is the minimum value of  $n$  for which it is possible for the coin to have *exactly* the same orientation as when it started? What should  $\omega_\perp$  be in terms of  $\omega_3$  to achieve this?

#### 9.48. **Seeing tails \*\***

A coin (floating in outer space) of mass  $m$  and radius  $R$  is initially spinning around the axis perpendicular to its plane, with angular speed  $\omega_3$ . You view the coin directly from above, and you apply a downward strike at a point on the rim, as shown in Fig. 9.63. What is the minimum impulse,  $\int F dt$ , you must apply in order to be able to barely see the underside of the coin at some later time in its wobbling motion? Assuming that you apply this minimum impulse, how far will the center of the coin have moved by the time you are able to see the underside?

<sup>25</sup> You can also play around with both parts of this problem for the setup where the stick swings around below the ring, with its top end running along the ring.

![Diagram of a coin in flight. The coin is shown as an ellipse, tilted at an angle. A vertical arrow labeled ω₃ points upwards from the center of the coin, representing its angular velocity component along its symmetry axis. A dashed line represents the horizontal diameter of the coin. A cross symbol ⊗ labeled F points downwards from the bottom of the coin, representing the force of gravity.](8a8ebe865b59f25f9c7022890b9b5332_img.jpg)

Diagram of a coin in flight. The coin is shown as an ellipse, tilted at an angle. A vertical arrow labeled ω₃ points upwards from the center of the coin, representing its angular velocity component along its symmetry axis. A dashed line represents the horizontal diameter of the coin. A cross symbol ⊗ labeled F points downwards from the bottom of the coin, representing the force of gravity.

Fig. 9.64

#### 9.49. **Flipping a coin \*\***

Imagine flipping an initially horizontal heads-up coin. If the initial angular velocity is horizontal, then the coin will rotate around this horizontal diameter the entire time in the air. The fraction of the flight time that the coin spends heads-up is therefore 1/2. In practice, however, it is impossible to make the initial  $\boldsymbol{\omega}$  be *exactly* horizontal, so assume that the initial components are  $\omega_{\perp}$  and  $\omega_3$ , with  $\omega_3 \ll \omega_{\perp}$ . Show that in this limit, the fraction of the flight time that the coin spends heads-up is  $1/2 + (4\omega_3^2)/(\pi\omega_{\perp}^2)$ .<sup>26</sup>

#### 9.50. **Dipping low \*\***

A top with  $I = 3I_3$  floats in outer space and initially spins around its  $x_3$  axis with angular speed  $\omega_3$ . You apply a strike at the bottom point, directed into the page, as shown in Fig. 9.64, producing an angular velocity component,  $\omega_{\perp}$ , directed to the right. What should  $\omega_{\perp}$  be in terms of  $\omega_3$  in order to have the total  $\boldsymbol{\omega}$  vector dip as far below the horizontal as possible in the subsequent motion?

![Diagram of a sphere rolling on a horizontal surface. The sphere has mass m and radius r. A horizontal stick is attached to its center. The stick is pivoted at a point on a vertical pole. The distance from the pivot to the center of the sphere is R. The sphere is rotating with angular velocity Ω around the pivot. The stick is shown at an angle to the vertical.](c49125ee7e40221553b4da65d1298995_img.jpg)

Diagram of a sphere rolling on a horizontal surface. The sphere has mass m and radius r. A horizontal stick is attached to its center. The stick is pivoted at a point on a vertical pole. The distance from the pivot to the center of the sphere is R. The sphere is rotating with angular velocity Ω around the pivot. The stick is shown at an angle to the vertical.

Fig. 9.65

### Section 9.7: Heavy symmetric top

#### 9.51. **Rolling lollipop \***

Consider a lollipop made of a solid sphere of mass  $m$  and radius  $r$  that is radially pierced by a massless horizontal stick. The free end of the stick is pivoted on a pole (see Fig. 9.65), and the sphere rolls on the ground without slipping, with its center moving in a circle of radius  $R$  with frequency  $\Omega$ . What is the normal force between the ground and the sphere?

![Diagram of a heavy symmetric top. The top is shown as a shaded, irregular shape. Its center of mass (CM) is at a distance l from the pivot point. The top is tilted at an angle θ with the negative z-axis. The top is rotating with angular velocity Ω around the vertical axis.](1dc6eeaac7ffa2cf8331c7911e1615c6_img.jpg)

Diagram of a heavy symmetric top. The top is shown as a shaded, irregular shape. Its center of mass (CM) is at a distance l from the pivot point. The top is tilted at an angle θ with the negative z-axis. The top is rotating with angular velocity Ω around the vertical axis.

Fig. 9.66

#### 9.52. **Horizontal $\boldsymbol{\omega}$ \*\***

A top (with mass  $m$ , moments  $I$  and  $I_3$ , and distance  $\ell$  from the pivot to CM) undergoes uniform precession, with its axis making a constant angle  $\theta$  with the negative  $z$  axis, as shown in Fig. 9.66. If conditions are set up so that the top's  $\boldsymbol{\omega}$  is always horizontal, what is the frequency of precession? Can such motion exist if the top is up above the horizontal, making an angle  $\theta$  with the positive  $z$  axis?

<sup>26</sup> If the coin starts truly horizontal (or is at least not biased to tilt in any particular direction on average, which is still a condition that seems difficult to guarantee), and if you catch the coin in your hand to reduce random table-bouncing effects, then the result of this exercise implies that the coin is biased to come up heads. This effect is analyzed in detail in a paper by Persi Diaconis, Susan Holmes, and Richard Montgomery (to be published), who estimate that the probability of obtaining heads for a normally flipped coin is about 0.51.

#### 9.53. **Sliding lollipop \*\*\***

Consider a lollipop made of a solid sphere of mass  $m$  and radius  $r$  that is radially pierced by a massless stick. The free end of the stick is pivoted on the ground, which is frictionless (see Fig. 9.67). The sphere *slides* along the ground, with the same point on the sphere always touching the ground. The center moves in a circle of radius  $R$  with frequency  $\Omega$ . Show that the normal force between the ground and the sphere is  $N = mg + mr\Omega^2$ , which is independent of  $R$ . Solve this by:

- Using an  $\mathbf{F} = m\mathbf{a}$  argument.<sup>27</sup>
- Using the more complicated  $\boldsymbol{\tau} = d\mathbf{L}/dt$  argument.

![Diagram for problem 9.53: A sphere of mass m and radius r is attached to a massless stick pivoted at a point on a horizontal ground. The center of the sphere moves in a circle of radius R with frequency Omega. The stick is at an angle to the vertical.](5e50dcf22e38fbe1992c132b515e4265_img.jpg)

Diagram for problem 9.53: A sphere of mass m and radius r is attached to a massless stick pivoted at a point on a horizontal ground. The center of the sphere moves in a circle of radius R with frequency Omega. The stick is at an angle to the vertical.

Fig. 9.67

#### 9.54. **Rolling wheel and axle \*\*\***

A massless axle has one end attached to a wheel (a uniform disk of mass  $m$  and radius  $r$ ), with the other end pivoted on the ground (see Fig. 9.68). The wheel rolls on the ground without slipping, with the axle inclined at an angle  $\theta$ . The point of contact on the ground traces out a circle with frequency  $\Omega$ .

![Diagram for problem 9.54: A wheel of mass m and radius r is attached to a massless axle pivoted at a point on a horizontal ground. The axle is inclined at an angle theta to the vertical. The wheel rolls without slipping on the ground. The center of the wheel moves in a circle of radius R with frequency Omega.](22f0a2ebccc03193636e4b5ccccf5467_img.jpg)

Diagram for problem 9.54: A wheel of mass m and radius r is attached to a massless axle pivoted at a point on a horizontal ground. The axle is inclined at an angle theta to the vertical. The wheel rolls without slipping on the ground. The center of the wheel moves in a circle of radius R with frequency Omega.

Fig. 9.68

- Show that  $\boldsymbol{\omega}$  points horizontally to the right (at the instant shown), with magnitude  $\omega = \Omega / \tan \theta$ .
- Show that the normal force between the ground and the wheel is

$$N = mg \cos^2 \theta + mr\Omega^2 \left( \frac{1}{4} \cos \theta \sin^2 \theta + \frac{3}{2} \cos^3 \theta \right). \quad (9.102)$$

#### 9.55. **Ball under a cone \*\*\***

A hollow ball (with  $I = (2/3)mR^2$ ) rolls without slipping on the inside surface of a fixed cone, whose tip points upward, as shown in Fig. 9.69. The angle at the vertex of the cone is  $60^\circ$ . Initial conditions have been set up so that the contact point on the cone traces out a horizontal circle of radius  $\ell$  at frequency  $\Omega$ , while the contact point on the ball traces out a circle of radius  $R/2$ . Assume that the coefficient of friction between the ball and the cone is sufficiently large to prevent slipping. What is the frequency of precession,  $\Omega$ ? What does it reduce to in the limits  $\ell \gg R$  and  $\ell \rightarrow (\sqrt{3}/2)R$  (the ball has to fit inside the cone, of course). What relation between  $\ell$  and  $R$  must be satisfied if the setup is to work with a solid ball with  $I = (2/5)mR^2$ ?

![Diagram for problem 9.55: A ball of radius R is rolling without slipping on the inside surface of a fixed cone. The cone has a vertex angle of 60 degrees. The ball's center moves in a horizontal circle of radius l with frequency Omega. The contact point on the ball traces out a circle of radius R/2.](5f534a0b93678e8e98397d409e06b98e_img.jpg)

Diagram for problem 9.55: A ball of radius R is rolling without slipping on the inside surface of a fixed cone. The cone has a vertex angle of 60 degrees. The ball's center moves in a horizontal circle of radius l with frequency Omega. The contact point on the ball traces out a circle of radius R/2.

Fig. 9.69

#### 9.56. **Ball in a cone \*\*\*\***

A ball (with  $I = (2/5)MR^2$ ) rolls without slipping on the inside surface of a fixed cone, whose tip points downward. The half-angle at the vertex

<sup>27</sup> This method happens to work here, due to the unusually nice nature of the sphere's motion. For more general motion (for example, in Problem 9.22, where the sphere is spinning), you must use  $\boldsymbol{\tau} = d\mathbf{L}/dt$ .

of the cone is  $\theta$ . Initial conditions have been set up so that the contact point on the cone traces out a horizontal circle of radius  $\ell \gg R$ , at frequency  $\Omega$ , while the contact point on the ball traces out a circle of radius  $r$  (not necessarily equal to  $R$ , as would be the case for a great circle). Assume that the coefficient of friction between the ball and the cone is sufficiently large to prevent slipping. What is the frequency of precession,  $\Omega$ ? It turns out that  $\Omega$  can be made infinite if  $r/R$  takes on a particular value; what is this value? Work in the approximation where  $R \ll \ell$ .

![Figure 9.70: A graph showing a series of overlapping loops. The vertical axis is labeled theta(t) with a downward arrow. The horizontal axis is labeled sin(theta_0) phi(t) with a rightward arrow. The loops are tangent to each other at their peaks and troughs. Above the graph, the equation Delta Omega = k Omega_s is written.](3c7c1895c84b878e256651bda37d575d_img.jpg)

Figure 9.70: A graph showing a series of overlapping loops. The vertical axis is labeled theta(t) with a downward arrow. The horizontal axis is labeled sin(theta\_0) phi(t) with a rightward arrow. The loops are tangent to each other at their peaks and troughs. Above the graph, the equation Delta Omega = k Omega\_s is written.

Fig. 9.70

#### 9.57. Nutation loops \*\*

In Fig. 9.38, the loops don't quite intersect each other in the  $\Delta\Omega = 4\Omega_s$  case, but they very much do in the  $\Delta\Omega = 10\Omega_s$  case (a given loop there actually intersects the two on either side). Show that the value of  $k$  for which adjacent loops in the  $\Delta\Omega = k\Omega_s$  case barely touch each other (as shown in Fig. 9.70) is  $k \approx 4.6033$ . You will have to solve something numerically. *Hint:* The curve is vertical at the relevant points.

### 9.10 Solutions

### 9.1. Many different $\boldsymbol{\omega}$ 's

We want to find all the vectors  $\boldsymbol{\omega}$  with the property that  $\boldsymbol{\omega} \times a\hat{\mathbf{x}} = v\hat{\mathbf{y}}$ . Since  $\boldsymbol{\omega}$  is orthogonal to this cross product,  $\boldsymbol{\omega}$  must lie in the  $x$ - $z$  plane. We claim that if  $\boldsymbol{\omega}$  makes an angle  $\theta$  with the  $x$  axis and has magnitude  $v/(a \sin \theta)$ , then it satisfies  $\boldsymbol{\omega} \times a\hat{\mathbf{x}} = v\hat{\mathbf{y}}$ . Indeed,

$$\boldsymbol{\omega} \times a\hat{\mathbf{x}} = |\boldsymbol{\omega}| |a\hat{\mathbf{x}}| \sin \theta \hat{\mathbf{y}} = v\hat{\mathbf{y}}. \quad (9.103)$$

Alternatively, note that such an  $\boldsymbol{\omega}$  can be written as

$$\boldsymbol{\omega} = \frac{v}{a \sin \theta} (\cos \theta, 0, \sin \theta) = \left( \frac{v}{a \tan \theta}, 0, \frac{v}{a} \right). \quad (9.104)$$

Only the  $z$  component here is relevant in the cross product with  $a\hat{\mathbf{x}}$ , so we have  $\boldsymbol{\omega} \times a\hat{\mathbf{x}} = (v/a)\hat{\mathbf{z}} \times a\hat{\mathbf{x}} = v\hat{\mathbf{y}}$ . The answer to the problem is therefore that  $\boldsymbol{\omega}$  must take the form given in Eq. (9.104).

It makes sense that the magnitude of  $\boldsymbol{\omega}$  is  $v/(a \sin \theta)$ , because if we drop a perpendicular from the particle to the line of  $\boldsymbol{\omega}$ , we see that the particle may be considered to be instantaneously traveling in a circle of radius  $r = a \sin \theta$  around  $\boldsymbol{\omega}$ , at speed  $v$ . And so we have  $v = \omega r$ , as we should. Whether the particle actually does travel in this circle is irrelevant. The past and future motion doesn't matter in finding the instantaneous  $\boldsymbol{\omega}$ . All we need to know is the velocity at the given instant.

A few possible  $\boldsymbol{\omega}$ 's are drawn in Fig. 9.71. Technically, it is possible to have  $\pi < \theta < 2\pi$ , but then the  $v/(a \sin \theta)$  coefficient in Eq. (9.104) is negative, which means that  $\boldsymbol{\omega}$  really points upward in the  $x$ - $z$  plane (physically,  $\boldsymbol{\omega}$  must point upward if the particle's velocity is to be in the positive  $y$  direction). So we'll assume  $0 < \theta < \pi$ . And since the  $v/a$  value of  $\omega_z$  in Eq. (9.104) is independent of  $\theta$ , all of the possible  $\boldsymbol{\omega}$ 's look like those in Fig. 9.72.

For  $\theta = \pi/2$ , we have  $\boldsymbol{\omega} = v/a$ , which makes sense. If  $\theta$  is very small, then  $\boldsymbol{\omega}$  is very large, because  $\boldsymbol{\omega} \propto 1/\sin \theta$ . This also makes sense, because the particle is (instantaneously) traveling around in a very small circle at the given speed  $v$ .

![Figure 9.71: A 3D diagram showing several vectors omega in the x-z plane. The z-axis is vertical and the x-axis is horizontal. A dashed circle of radius a is centered at the origin in the x-z plane. The vectors omega originate from the origin and point to various locations on this circle. A vector labeled 'a' points from the origin to a point on the circle in the x-z plane.](6f1244daac9895ebc8d6d4c158035d2c_img.jpg)

Figure 9.71: A 3D diagram showing several vectors omega in the x-z plane. The z-axis is vertical and the x-axis is horizontal. A dashed circle of radius a is centered at the origin in the x-z plane. The vectors omega originate from the origin and point to various locations on this circle. A vector labeled 'a' points from the origin to a point on the circle in the x-z plane.

Fig. 9.71

![Figure 9.72: A 2D diagram in the x-z plane showing several vectors omega originating from the origin. The z-axis is vertical and the x-axis is horizontal. All vectors omega have the same vertical component, indicated by a dashed horizontal line at height v/a. The vectors are shown at various angles theta from the x-axis.](85bfa5375b5004494c107c294f74ef54_img.jpg)

Figure 9.72: A 2D diagram in the x-z plane showing several vectors omega originating from the origin. The z-axis is vertical and the x-axis is horizontal. All vectors omega have the same vertical component, indicated by a dashed horizontal line at height v/a. The vectors are shown at various angles theta from the x-axis.

Fig. 9.72

**REMARK:** The point of this problem is that the particle may be in the process of having its position vector trace out a cone around one of many possible axes, or perhaps it may be undergoing a more complicated motion. If we are handed only the given information on position and velocity, then it is impossible to determine which of these motions is happening. And it is likewise impossible to uniquely determine  $\omega$ . This is true for a collection of points that lie on at most one line through the origin. If the points, along with the origin, span more than a 1-D line, then  $\omega$  is in fact uniquely determined (see Footnote 9). ♣

### 9.2. Fixed points on a sphere

**FIRST SOLUTION:** For the purposes of Theorem 9.1, we need only show that two points end up where they started for an *infinitesimal* transformation. But since it's possible to prove this for a general transformation, we'll consider the general case here.

Consider the point  $A$  that ends up farthest away from where it started.<sup>28</sup> Label the ending point  $B$ . Draw the great circle,  $C_{AB}$ , through  $A$  and  $B$ . Draw the great circle,  $C_A$ , that is perpendicular to  $C_{AB}$  at  $A$ ; and draw the great circle,  $C_B$ , that is perpendicular to  $C_{AB}$  at  $B$ . We claim that the transformation must take  $C_A$  to  $C_B$ . This is true for the following reason. The image of  $C_A$  is certainly a great circle through  $B$ . And this great circle must be perpendicular to  $C_{AB}$ , because otherwise there would exist another point that ended up farther away from its starting point than  $A$  did (see Fig. 9.73). Since there is only one great circle through  $B$  that is perpendicular to  $C_{AB}$ , the image of  $C_A$  must in fact be  $C_B$ .

Now consider the two points,  $P_1$  and  $P_2$ , where  $C_A$  and  $C_B$  intersect (any two great circles intersect in two points). Look at  $P_1$ . The distances  $P_1A$  and  $P_1B$  are equal, because  $C_{AB}$  makes equal angles (namely  $90^\circ$ ) with  $C_A$  and  $C_B$ . Therefore, the point  $P_1$  is not moved by the transformation. This is true because  $P_1$  ends up on  $C_B$  (because  $C_B$  is the image of  $C_A$ , on which  $P_1$  started), and if it ended up at a point other than  $P_1$ , then its final distance from  $B$  would be different from its initial distance from  $A$ . This would contradict the fact that distances are preserved on the rigid sphere. Likewise for  $P_2$ . We have therefore found our two desired points.

Note that for a noninfinitesimal transformation, every point on the sphere may move at some time during the transformation. But what we've just shown is that two points end up back where they started, even if they've moved in the interim.

**SECOND SOLUTION:** In the spirit of the above solution, we can give a simpler solution, but one that is valid only in the case of infinitesimal transformations.

Pick any point  $A$  that moves during the transformation. Draw the great circle that passes through  $A$  and is perpendicular to the direction of  $A$ 's motion. (This direction is well defined, because we are considering an infinitesimal transformation, so  $A$  doesn't have time to change direction.) All points on this great circle must move (if they move at all) perpendicular to the great circle, because otherwise their distances from  $A$  would change. But they cannot all move in the same direction, because then the center of the great circle, and hence the sphere, would move (but it is assumed to be fixed). Therefore, at least one point on the great circle moves in the direction opposite to the direction in which  $A$  moves. Therefore, by continuity, some point (and hence also its diametrically opposite point) on the great circle must remain fixed.

### 9.3. Rolling cone

At the risk of overdoing it, we'll present three solutions. The second and third solutions are the type that might make your head hurt, so you may want to reread them after looking at the discussion of the angular velocity vector in Section 9.7.2.

![Figure 9.73: A geometric diagram on a sphere illustrating the proof of fixed points. A horizontal line represents a great circle C_AB. Point A is on this line. A vertical line segment AB is drawn, perpendicular to C_AB at A. A horizontal line segment C_A is drawn through A, perpendicular to AB. A dashed line segment extends from B, perpendicular to C_AB. A curved arrow indicates a rotation from C_A towards the dashed line. The dashed line is labeled 'impossible image of C_A'. The text 'moves farther than A' is written above the dashed line. The great circle C_AB is labeled at its intersection with the dashed line. The great circle C_A is labeled at its intersection with the horizontal line.](b1a62020283e0587b03446cf0feb8681_img.jpg)

Figure 9.73: A geometric diagram on a sphere illustrating the proof of fixed points. A horizontal line represents a great circle C\_AB. Point A is on this line. A vertical line segment AB is drawn, perpendicular to C\_AB at A. A horizontal line segment C\_A is drawn through A, perpendicular to AB. A dashed line segment extends from B, perpendicular to C\_AB. A curved arrow indicates a rotation from C\_A towards the dashed line. The dashed line is labeled 'impossible image of C\_A'. The text 'moves farther than A' is written above the dashed line. The great circle C\_AB is labeled at its intersection with the dashed line. The great circle C\_A is labeled at its intersection with the horizontal line.

Fig. 9.73

<sup>28</sup> If there is more than one such point, pick any one of them. Considering that the result of this problem is that the net motion of the sphere is a rotation around an axis, there will in fact be a whole great circle of points that move farthest.

![Figure 9.74: A diagram showing a cone with its apex at the origin of a coordinate system. The z-axis is vertical. A point P is on the surface of the cone. A dashed line of length h connects the apex to P. The angle between the z-axis and this line is alpha. A vector omega points along the line of contact of the cone with the horizontal plane. A dashed circle of radius d = h sin alpha is shown around the z-axis, with P on it. A curved arrow indicates the rotation of P around the z-axis.](559a64c52ca0f64780120ee5a96b2111_img.jpg)

Figure 9.74: A diagram showing a cone with its apex at the origin of a coordinate system. The z-axis is vertical. A point P is on the surface of the cone. A dashed line of length h connects the apex to P. The angle between the z-axis and this line is alpha. A vector omega points along the line of contact of the cone with the horizontal plane. A dashed circle of radius d = h sin alpha is shown around the z-axis, with P on it. A curved arrow indicates the rotation of P around the z-axis.

Fig. 9.74

FIRST SOLUTION: Without doing any calculations, we know that  $\omega$  points along the line of contact of the cone with the table, because these are the points on the cone that are instantaneously at rest. And we know that as time goes by,  $\omega$  rotates around in the horizontal plane with angular speed  $v/(h \cos \alpha)$ , because point  $P$  travels at speed  $v$  in a circle of radius  $h \cos \alpha$  around the  $z$  axis.

The magnitude of  $\omega$  can be found as follows. At a given instant,  $P$  may be considered to be rotating in a circle of radius  $d = h \sin \alpha$  around  $\omega$  (see Fig. 9.74). Since  $P$  moves with speed  $v$ , the angular speed of this rotation is  $\omega = v/d$ . Therefore,

$$\omega = \frac{v}{h \sin \alpha}. \quad (9.105)$$

![Figure 9.75: A diagram showing the cone and point P. It illustrates the angular velocity vectors omega_1,2 and omega_2,3. omega_1,2 is a vector of length v/r pointing along the base of the cone. omega_2,3 is a vector of length v/h pointing along the line of contact. The angle between them is alpha. A dashed circle of radius r is shown at the base of the cone.](94fa6e6d6f58a25b6f2a73de8643305c_img.jpg)

Figure 9.75: A diagram showing the cone and point P. It illustrates the angular velocity vectors omega\_1,2 and omega\_2,3. omega\_1,2 is a vector of length v/r pointing along the base of the cone. omega\_2,3 is a vector of length v/h pointing along the line of contact. The angle between them is alpha. A dashed circle of radius r is shown at the base of the cone.

Fig. 9.75

SECOND SOLUTION: We can use Theorem 9.3 with the following frames.  $S_1$  is fixed in the cone;  $S_3$  is the lab frame; and  $S_2$  is the frame that (instantaneously) rotates around the tilted  $\omega_{2,3}$  axis shown in Fig. 9.75, at the speed such that the axis of the cone remains fixed in  $S_2$ . The tip of  $\omega_{2,3}$  traces out a circle as it precesses around the  $z$  axis, so after the cone moves a little, we will need to use a new  $S_2$  frame. But at any moment,  $S_2$  instantaneously rotates around the axis perpendicular to the axis of the cone.

In the language of Theorem 9.3,  $\omega_{1,2}$  and  $\omega_{2,3}$  point in the directions shown. We must find their magnitudes and then add the vectors to determine the angular velocity of  $S_1$  with respect to  $S_3$ . First, we have

$$|\omega_{2,3}| = \frac{v}{h}, \quad (9.106)$$

because point  $P$  moves (instantaneously) with speed  $v$  in a circle of radius  $h$  around  $\omega_{2,3}$ . We now claim that

$$|\omega_{1,2}| = \frac{v}{r} = \frac{v}{h \tan \alpha}, \quad (9.107)$$

where  $r$  is the radius of the base of the cone. This is true because someone fixed in  $S_2$  sees the endpoint of the radius (the one drawn in Fig. 9.75) move “backward” at speed  $v$ , because it is stationary with respect to the table. Hence, the cone must be spinning with frequency  $v/r$  in  $S_2$ .

The addition of  $\omega_{1,2}$  and  $\omega_{2,3}$  is shown in Fig. 9.76. The result has magnitude  $v/(h \sin \alpha)$ , and it points horizontally because  $|\omega_{2,3}|/|\omega_{1,2}| = \tan \alpha$ .

![Figure 9.76: A vector diagram showing the addition of omega_1,2 and omega_2,3. omega_1,2 is a vector of length v/r = v/(h tan alpha) at an angle alpha to the horizontal. omega_2,3 is a vector of length v/h at an angle alpha to the vertical. Their sum omega is a horizontal vector of length v/(h sin alpha).](2c1d6960bc31ef7ebbc12cce646d0718_img.jpg)

Figure 9.76: A vector diagram showing the addition of omega\_1,2 and omega\_2,3. omega\_1,2 is a vector of length v/r = v/(h tan alpha) at an angle alpha to the horizontal. omega\_2,3 is a vector of length v/h at an angle alpha to the vertical. Their sum omega is a horizontal vector of length v/(h sin alpha).

Fig. 9.76

THIRD SOLUTION: We can use Theorem 9.3 with the following frames.  $S_1$  is fixed in the cone; and  $S_3$  is the lab frame (as in the second solution). But now let  $S_2$  be the frame that rotates around the (negative)  $z$  axis, at the speed such that the axis of the cone remains fixed in it. Note that we can keep using this same  $S_2$  frame as time goes by, unlike the  $S_2$  frame in the second solution.

$\omega_{1,2}$  and  $\omega_{2,3}$  point in the directions shown in Fig. 9.77. As above, we must find their magnitudes and then add the vectors to determine the angular velocity of  $S_1$  with respect to  $S_3$ . First, we have

$$|\omega_{2,3}| = \frac{v}{h \cos \alpha}, \quad (9.108)$$

because point  $P$  moves with speed  $v$  in a circle of radius  $h \cos \alpha$  around  $\omega_{2,3}$ .

It's a little trickier to find  $|\omega_{1,2}|$ . From the point of view of someone spinning around with  $S_2$ , the table rotates backward with frequency  $|\omega_{2,3}| = v/(h \cos \alpha)$ , from Eq. (9.108). Consider the circle of contact points on the table where the base of the cone touches it. This circle has a radius  $h/\cos \alpha$ , so someone spinning around with  $S_2$  sees the circle move backward with speed  $|\omega_{2,3}|(h/\cos \alpha) = v/\cos^2 \alpha$  around the vertical. Since there is no slipping, the contact point on the cone must also move with this speed in  $S_2$  around the axis of the cone (which is fixed in  $S_2$ ). And since the radius of the base is  $r$ , this means that the cone rotates with angular speed  $v/(r \cos^2 \alpha)$  with

![Figure 9.77: A diagram showing the cone and point P. It illustrates the angular velocity vectors omega_1,2 and omega_2,3. omega_1,2 is a vector of length v/r pointing along the base of the cone. omega_2,3 is a vector of length v/(h cos alpha) pointing along the line of contact. The angle between them is alpha. A dashed circle of radius r is shown at the base of the cone.](8247c74494a4dea704e05e0db64ae003_img.jpg)

Figure 9.77: A diagram showing the cone and point P. It illustrates the angular velocity vectors omega\_1,2 and omega\_2,3. omega\_1,2 is a vector of length v/r pointing along the base of the cone. omega\_2,3 is a vector of length v/(h cos alpha) pointing along the line of contact. The angle between them is alpha. A dashed circle of radius r is shown at the base of the cone.

Fig. 9.77

respect to  $S_2$ . Therefore, using  $r = h \tan \alpha$ , we have

$$|\omega_{1,2}| = \frac{v}{r \cos^2 \alpha} = \frac{v}{h \sin \alpha \cos \alpha}. \quad (9.109)$$

The addition of  $\omega_{1,2}$  and  $\omega_{2,3}$  is shown in Fig. 9.78. The result has magnitude  $v/(h \sin \alpha)$ , and it points horizontally because  $|\omega_{2,3}|/|\omega_{1,2}| = \sin \alpha$ .

**REMARK:** The difference between the  $\omega_{1,2}$  vectors in the second and third solutions comes down to the following fact. Let  $Q$  be the contact point on the base of the cone. Consider the ratio of the distance from  $Q$  to  $\omega_{2,3}$  to the distance from  $P$  to  $\omega_{2,3}$ . This ratio is 1 in the second solution, but  $1/\cos^2 \alpha$  in the third solution. This implies that the “backward” speed of  $Q$  relative to  $P$ , as measured in frame  $S_2$ , is a factor  $1/\cos^2 \alpha$  larger in the third solution. And since  $Q$  is the same distance  $r$  away from  $\omega_{1,2}$  in both cases, we see that  $\omega_{1,2}$  is a factor  $1/\cos^2 \alpha$  larger in the third solution. ♣

![Vector diagram for Fig. 9.78 showing the addition of two vectors. A horizontal vector labeled omega = v / (h sin alpha) is the result. A vector labeled omega_{1,2} = v / (h sin alpha cos alpha) is at an angle alpha above the horizontal. A vertical vector labeled omega_{2,3} = v / (h cos alpha) is added to omega_{1,2} to form the horizontal resultant vector omega. The angle alpha is shown between the horizontal and the omega_{1,2} vector.](3e2456bab2a2790dd297602b71aff386_img.jpg)

Vector diagram for Fig. 9.78 showing the addition of two vectors. A horizontal vector labeled omega = v / (h sin alpha) is the result. A vector labeled omega\_{1,2} = v / (h sin alpha cos alpha) is at an angle alpha above the horizontal. A vertical vector labeled omega\_{2,3} = v / (h cos alpha) is added to omega\_{1,2} to form the horizontal resultant vector omega. The angle alpha is shown between the horizontal and the omega\_{1,2} vector.

Fig. 9.78

### 9.4. Parallel-axis theorem

Consider one of the diagonal entries in  $\mathbf{I}$ , say  $I_{xx} \equiv \int (y^2 + z^2)$ . In terms of the new variables, this equals

$$\begin{aligned} I_{xx} &= \int ((Y + y')^2 + (Z + z')^2) = \int (Y^2 + Z^2) + \int (y'^2 + z'^2) \\ &= M(Y^2 + Z^2) + \int (y'^2 + z'^2), \end{aligned} \quad (9.110)$$

as desired. We have used the fact that the cross terms vanish because, for example,  $\int Yy' = Y \int y' = 0$ , by definition of the CM. Similarly, consider an off-diagonal entry in  $\mathbf{I}$ , say  $I_{xy} \equiv -\int xy$ . We have

$$I_{xy} = -\int (X + x')(Y + y') = -\int XY - \int x'y' = -M(XY) - \int x'y', \quad (9.111)$$

where the cross terms have likewise vanished. We therefore see that all of the terms in  $\mathbf{I}$  take the form of those in Eq. (9.19), as desired.

### 9.5. A nice cylinder

By symmetry, the principal axes are the symmetry axis of the cylinder, along with any diameters in the cross-section circle through the CM. Let the equal moments around the diameters be  $I$ . Then by Theorem 9.5, if the moment around the symmetry axis also equals  $I$ , then every axis is a principal axis.

Let the mass of the cylinder be  $M$ . Let its radius be  $R$  and its height be  $h$ . Then the moment around the symmetry axis is  $MR^2/2$ . Let  $D$  be a diameter through the CM. The moment around  $D$  can be calculated as follows. Slice the cylinder into horizontal disks of thickness  $dy$ . Let  $\rho$  be the mass per unit height (so  $\rho = M/h$ ). The mass of each disk is then  $\rho dy$ , so the moment around a diameter through the disk is  $(\rho dy)R^2/4$  (the usual result for a disk). Therefore, by the parallel-axis theorem, the moment of a disk at height  $y$  (where  $-h/2 \leq y \leq h/2$ ) around  $D$  is  $(\rho dy)R^2/4 + (\rho dy)y^2$ . Hence, the moment of the entire cylinder around  $D$  is

$$I = \int_{-h/2}^{h/2} \left( \frac{\rho R^2}{4} + \rho y^2 \right) dy = \frac{\rho R^2 h}{4} + \frac{\rho h^3}{12} = \frac{MR^2}{4} + \frac{Mh^2}{12}. \quad (9.112)$$

We want this to equal  $MR^2/2$ . Therefore,  $h = \sqrt{3}R$ .

As an exercise, you can show that if the origin were instead taken to be the center of one of the circular faces, then the answer would be  $h = \sqrt{3}R/2$ . Note that the  $I$  in Eq. (9.112) looks just like the moment of a disk around a diameter plus the moment of a stick around its center. This is no coincidence. The integral that yielded the  $Mh^2/12$  term here is the same integral that we would perform for a stick.

![Figure 9.79: A diagram showing a square with a center of mass (CM) at its center. Two masses, A and B, are located at opposite corners. A vertical axis passes through the CM. For mass A, the distance from the axis is l_A, the distance from the CM is r_A, and the angle between the axis and the line to the CM is theta. For mass B, the distance from the axis is l_B, the distance from the CM is r_B, and the angle between the axis and the line to the CM is also theta. Two shaded right-angled triangles are shown, one for each mass, with hypotenuses r_A and r_B respectively.](a4d9045fbdcffa155be0c961f39248d9_img.jpg)

Figure 9.79: A diagram showing a square with a center of mass (CM) at its center. Two masses, A and B, are located at opposite corners. A vertical axis passes through the CM. For mass A, the distance from the axis is l\_A, the distance from the CM is r\_A, and the angle between the axis and the line to the CM is theta. For mass B, the distance from the axis is l\_B, the distance from the CM is r\_B, and the angle between the axis and the line to the CM is also theta. Two shaded right-angled triangles are shown, one for each mass, with hypotenuses r\_A and r\_B respectively.

Fig. 9.79

### 9.6. Rotating square

Label two of the masses  $A$  and  $B$ , as shown in Fig. 9.79. Let  $\ell_A$  be the distance along the axis from the CM to  $A$ 's string, and let  $r_A$  be the length of  $A$ 's string. Likewise for  $B$ . The force,  $F_A$ , in  $A$ 's string must account for the centripetal acceleration of  $A$ . Hence,  $F_A = mr_A\omega^2$ . The torque around the CM due to  $F_A$  is therefore

$$\tau_A = mr_A\ell_A\omega^2. \quad (9.113)$$

Likewise, the torque around the CM due to  $B$ 's string is  $\tau_B = mr_B\ell_B\omega^2$ , in the opposite direction. But the two shaded triangles in Fig. 9.79 are congruent, because they have the same hypotenuse and the same angle  $\theta$ . Therefore,  $\ell_A = r_B$  and  $\ell_B = r_A$ . Hence,  $\tau_A = \tau_B$ , and the torques cancel. The torques from the other two masses likewise cancel. Note that a uniform square is made up of many sets of these squares of point masses, so we've also shown that no torque is needed for a uniform square.

**REMARK:** For a general  $N$ -gon of point masses, Problem 9.8 below shows that any axis in the plane is a principal axis. Let's prove this here by using the above torque argument. We'll use a math trick here that involves writing a trig function (a sine) as the imaginary part of a complex exponential. Using Eq. (9.113), we see that the torque from mass  $A$  in Fig. 9.80 is  $\tau_A = m\omega^2R^2 \sin\phi \cos\phi$ . Likewise, the torque from mass  $B$  is  $\tau_B = m\omega^2R^2 \sin(\phi + 2\pi/N) \cos(\phi + 2\pi/N)$ , and so on. The total torque around the CM is therefore

![Figure 9.80: A diagram showing a regular N-gon with a center of mass (CM) at its center. A vertical axis passes through the CM. Two masses, A and B, are located at vertices. The distance from the CM to any vertex is R. The angle between the axis and the line to mass A is phi. The angle between the lines to masses A and B is 2pi/N.](98dafc70778b3e55744b9e1c59eb57df_img.jpg)

Figure 9.80: A diagram showing a regular N-gon with a center of mass (CM) at its center. A vertical axis passes through the CM. Two masses, A and B, are located at vertices. The distance from the CM to any vertex is R. The angle between the axis and the line to mass A is phi. The angle between the lines to masses A and B is 2pi/N.

Fig. 9.80

$$\begin{aligned} \tau &= mR^2\omega^2 \sum_{k=0}^{N-1} \sin\left(\phi + \frac{2\pi k}{N}\right) \cos\left(\phi + \frac{2\pi k}{N}\right) \\ &= \frac{mR^2\omega^2}{2} \sum_{k=0}^{N-1} \sin\left(2\phi + \frac{4\pi k}{N}\right) \\ &= \frac{mR^2\omega^2}{2} \sum_{k=0}^{N-1} \text{Im}\left(e^{i(2\phi + 4\pi k/N)}\right) \\ &= \frac{mR^2\omega^2}{2} \text{Im}\left(e^{2i\phi} \left(1 + e^{4\pi i/N} + e^{8\pi i/N} + \dots + e^{4(N-1)\pi i/N}\right)\right) \\ &= \frac{mR^2\omega^2}{2} \text{Im}\left(e^{2i\phi} \left(\frac{e^{4N\pi i/N} - 1}{e^{4\pi i/N} - 1}\right)\right) \\ &= 0. \end{aligned} \quad (9.114)$$

To obtain the fifth line, we summed the geometric series. And to obtain the last line, we used the fact that  $e^{4\pi i} = 1$ . The one exception to this result is when  $N = 2$ , because the denominator in the fifth line is zero (but it's hard to have a 2-gon, anyway); this corresponds to the  $\theta \neq 180^\circ$  restriction in Theorem 9.6.

Note that what we've done here is show that  $\sum r_i \ell_i = 0$ , which implies that the total torque is zero (which is one of the definitions of a principal axis). In terms of the chosen axis, this is equivalent to showing that  $\sum xy = 0$ , that is, showing that the off-diagonal terms in the inertia tensor vanish (which is simply another definition of the principal axes). ♣

### 9.7. Existence of principal axes for a pancake

For a pancake object, the inertia tensor  $\mathbf{I}$  takes the form in Eq. (9.8), with  $z = 0$ . Therefore, if we can find a set of axes for which  $\int xy = 0$ , then  $\mathbf{I}$  will be diagonal, and we will have found our principal axes. We can prove, using a continuity argument, that such a set of axes exists.

Pick a set of axes, and write down the integral  $\int xy \equiv I_0$ . If  $I_0 = 0$ , then we are done. If  $I_0 \neq 0$ , then rotate these axes by an angle of  $\pi/2$ , so that the new  $\hat{\mathbf{x}}$  is the old  $\hat{\mathbf{y}}$ ,

and the new  $\hat{y}$  is the old  $-\hat{x}$  (see Fig. 9.81). Write down the new integral  $\int xy \equiv I_{\pi/2}$ . Since the new and old coordinates are related by  $x_{\text{new}} = y_{\text{old}}$  and  $y_{\text{new}} = -x_{\text{old}}$ , we have  $I_{\pi/2} = -I_0$ . Therefore, since  $\int xy$  switches sign during the (continuous) rotation of the axes, there must exist some intermediate angle for which the integral  $\int xy$  is zero.

### 9.8. Symmetries and principal axes for a pancake

In view of the form of the inertia tensor in Eq. (9.8), we want to show that if a pancake object has a symmetry under a rotation through  $\theta \neq \pi$ , then  $\int xy = 0$  for any set of axes (through the origin). Take an arbitrary set of axes and rotate them through an angle  $\theta \neq \pi$ . The new coordinates are  $x' = (x \cos \theta + y \sin \theta)$  and  $y' = (-x \sin \theta + y \cos \theta)$ , so the new matrix entries, in terms of the old ones, are

![Figure 9.81: A 2D coordinate system showing two sets of axes. The old axes are labeled x_old (horizontal, pointing right) and y_old (vertical, pointing up). The new axes are labeled x_new (horizontal, pointing left) and y_new (vertical, pointing down). The new axes are rotated by 90 degrees counter-clockwise relative to the old axes.](5453b9e0b8e77c0c896fb8cc9c8dcfee_img.jpg)

Figure 9.81: A 2D coordinate system showing two sets of axes. The old axes are labeled x\_old (horizontal, pointing right) and y\_old (vertical, pointing up). The new axes are labeled x\_new (horizontal, pointing left) and y\_new (vertical, pointing down). The new axes are rotated by 90 degrees counter-clockwise relative to the old axes.

Fig. 9.81

$$\begin{aligned} I'_{xx} &\equiv \int y'^2 = I_{yy} \sin^2 \theta + 2I_{xy} \sin \theta \cos \theta + I_{xx} \cos^2 \theta, \\ I'_{yy} &\equiv \int x'^2 = I_{yy} \cos^2 \theta - 2I_{xy} \sin \theta \cos \theta + I_{xx} \sin^2 \theta, \\ I'_{xy} &\equiv - \int x'y' = I_{yy} \sin \theta \cos \theta + I_{xy}(\cos^2 \theta - \sin^2 \theta) - I_{xx} \sin \theta \cos \theta. \end{aligned} \quad (9.115)$$

If the object looks exactly like it did before the rotation, then  $I'_{xx} = I_{xx}$ ,  $I'_{yy} = I_{yy}$ , and  $I'_{xy} = I_{xy}$ . The first two of these statements are actually equivalent (as you can show), so we'll just use the first and third. Using Eq. (9.116), along with  $1 - \cos^2 \theta = \sin^2 \theta$ , these two statements give

$$\begin{aligned} 0 &= -I_{xx} \sin^2 \theta + 2I_{xy} \sin \theta \cos \theta + I_{yy} \sin^2 \theta, \\ 0 &= -I_{xx} \sin \theta \cos \theta - 2I_{xy} \sin^2 \theta + I_{yy} \sin \theta \cos \theta. \end{aligned} \quad (9.116)$$

Multiplying the first of these by  $\cos \theta$  and the second by  $\sin \theta$ , and subtracting, gives

$$2I_{xy} \sin \theta = 0. \quad (9.117)$$

Under the assumption  $\theta \neq \pi$  (and  $\theta \neq 0$ , of course), we must therefore have  $I_{xy} = 0$ . Our initial axes were arbitrary; hence, any set of axes (through the origin) in the plane is a set of principal axes.

**REMARK:** If an object is invariant under a rotation through an angle  $\theta$ , then  $\theta$  must be of the form  $\theta = 2\pi/N$ , for some integer  $N$  (convince yourself of this). So consider a regular  $N$ -gon with “radius”  $R$  and with point masses  $m$  located at the vertices. Any object that is invariant under a rotation through  $\theta = 2\pi/N$  may be considered to be built out of regular point-mass  $N$ -gons of various sizes. Theorem 9.5 implies that all axes in the plane of a regular  $N$ -gon have the same moment (the two axes in this theorem aren't required to be orthogonal). Let's demonstrate this explicitly for a regular  $N$ -gon. This method we'll use here is similar to the one in the remark in Problem 9.6, except that now we'll write a trig function (a cosine) as the real part of a complex exponential. In Fig. 9.82 the distance from mass  $A$  to the axis is  $r_A = R \sin \phi$ . And the distance from  $B$  to the axis is  $r_B = R \sin(\phi + 2\pi/N)$ , and so on for the other masses. The moment of inertia around the axis is therefore

![Figure 9.82: A diagram of a regular N-gon. A vertical axis of rotation is shown passing through the center. Two vertices, A and B, are labeled. The angle between the vertical axis and the line to vertex A is phi. The distance from the center to vertex A is R. The angle between the lines to vertices A and B is 2pi/N. A curved arrow at the top indicates rotation around the vertical axis.](1aae852e797caaac9fd539dad7b0b307_img.jpg)

Figure 9.82: A diagram of a regular N-gon. A vertical axis of rotation is shown passing through the center. Two vertices, A and B, are labeled. The angle between the vertical axis and the line to vertex A is phi. The distance from the center to vertex A is R. The angle between the lines to vertices A and B is 2pi/N. A curved arrow at the top indicates rotation around the vertical axis.

Fig. 9.82

$$\begin{aligned} I_\phi &= mR^2 \sum_{k=0}^{N-1} \sin^2 \left( \phi + \frac{2\pi k}{N} \right) \\ &= \frac{mR^2}{2} \sum_{k=0}^{N-1} \left( 1 - \cos \left( 2\phi + \frac{4\pi k}{N} \right) \right) \end{aligned}$$

$$\begin{aligned}
 &= \frac{NmR^2}{2} - \frac{mR^2}{2} \sum_{k=0}^{N-1} \operatorname{Re}\left(e^{i(2\phi+4\pi k/N)}\right) \\
 &= \frac{NmR^2}{2} - \frac{mR^2}{2} \operatorname{Re}\left(e^{2i\phi}\left(1 + e^{4\pi i/N} + e^{8\pi i/N} + \dots + e^{4(N-1)\pi i/N}\right)\right) \\
 &= \frac{NmR^2}{2} - \frac{mR^2}{2} \operatorname{Re}\left(e^{2i\phi}\left(\frac{e^{4N\pi i/N} - 1}{e^{4\pi i/N} - 1}\right)\right), \quad (9.118)
 \end{aligned}$$

where we have summed the geometric series to obtain the last line. The numerator in the parentheses equals  $e^{4\pi i} - 1 = 0$ . And if  $N \neq 2$ , the denominator is not zero. Therefore, if  $N \neq 2$  (which is equivalent to the  $\theta \neq \pi$  restriction), we have

$$I_\phi = \frac{NmR^2}{2}, \quad (9.119)$$

which is independent of  $\phi$ . This result of  $NmR^2/2$  for the common value of all the moments makes sense, because the perpendicular-axis theorem says that this common value must be half of the moment around the axis perpendicular to the plane, which is  $NmR^2$ . ♣

![Figure 9.83: A diagram of a rectangle with width 'a' and height 'b'. A force 'F' is applied at the top-left corner, directed out of the page (indicated by a dot in a circle). Another force 'F' is applied at the bottom-right corner, directed into the page (indicated by a cross in a circle). A torque vector 'tau' is shown as an arrow pointing up and to the right from the center of the rectangle.](71f1b92bf7e084403bbd355b0d18298b_img.jpg)

Figure 9.83: A diagram of a rectangle with width 'a' and height 'b'. A force 'F' is applied at the top-left corner, directed out of the page (indicated by a dot in a circle). Another force 'F' is applied at the bottom-right corner, directed into the page (indicated by a cross in a circle). A torque vector 'tau' is shown as an arrow pointing up and to the right from the center of the rectangle.

Fig. 9.83

### 9.9. Striking a rectangle

If the force is out of the page at the upper left corner and into the page at the lower right corner, then the torque  $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$  points upward to the right, as shown in Fig. 9.83, with  $\boldsymbol{\tau} \propto (b, a)$ . The angular momentum equals  $\int \boldsymbol{\tau} dt$ , so immediately after the strike,  $\mathbf{L}$  is proportional to  $(b, a)$ . But the angular momentum may also be written as  $\mathbf{L} = (I_x \omega_x, I_y \omega_y)$ , where  $I_x = mb^2/12$  and  $I_y = ma^2/12$  are the principal moments. Therefore, we have

$$(I_x \omega_x, I_y \omega_y) \propto (b, a) \implies (\omega_x, \omega_y) \propto \left(\frac{b}{I_x}, \frac{a}{I_y}\right) \propto \left(\frac{b}{b^2}, \frac{a}{a^2}\right) \propto (a, b), \quad (9.120)$$

which is the direction of the other diagonal. This result checks in the special case  $a = b$ , and also in the limit where one of  $a$  and  $b$  is much larger than the other. Basically, if  $b$  is much larger than  $a$ , then this largeness matters more in the moment of inertia around the  $x$  axis (which is quadratic in length) than it does in the torque in the  $x$  direction (which is linear in length), so there is very little rotation around the  $x$  axis.

### 9.10. Rotating stick

The angular momentum around the CM can be found as follows. Break  $\boldsymbol{\omega}$  up into its components along the principal axes of the stick (which are parallel and perpendicular to the stick). The moment of inertia around the stick is zero. Therefore, only the component of  $\boldsymbol{\omega}$  perpendicular to the stick is relevant in calculating  $\mathbf{L}$ . This component is  $\omega \sin \theta$ , and the associated moment of inertia is  $m\ell^2/12$ . Hence, the angular momentum at any time has magnitude

$$L = \frac{1}{12} m\ell^2 \omega \sin \theta, \quad (9.121)$$

and it points as shown in Fig. 9.84. The tip of the vector  $\mathbf{L}$  traces out a circle in a horizontal plane with frequency  $\omega$ . The radius of this circle is the horizontal component of  $\mathbf{L}$ , which is  $L_\perp \equiv L \cos \theta$ . The rate of change of  $\mathbf{L}$  therefore has magnitude

$$\left|\frac{d\mathbf{L}}{dt}\right| = \omega L_\perp = \omega L \cos \theta = \omega \left(\frac{1}{12} m\ell^2 \omega \sin \theta\right) \cos \theta, \quad (9.122)$$

and it is directed into the page at the instant shown.

Let the tension in the strings be  $T$ . Then the torque due to the strings is  $\boldsymbol{\tau} = 2T(\ell/2) \cos \theta$ , directed into the page at the instant shown. Therefore,  $\boldsymbol{\tau} = d\mathbf{L}/dt$  gives

$$T\ell \cos \theta = \omega \left(\frac{1}{12} m\ell^2 \omega \sin \theta\right) \cos \theta \implies T = \frac{1}{12} m\ell \omega^2 \sin \theta. \quad (9.123)$$

![Figure 9.84: A diagram of a stick of length 'l' suspended by two strings of length 'l/2' from a horizontal ceiling. The stick makes an angle 'theta' with the vertical. A rotation vector 'omega' is shown as a curved arrow around the vertical axis. The angular momentum vector 'L' is shown as an arrow originating from the center of mass of the stick, pointing at an angle 'theta' from the vertical. The horizontal component of 'L' is labeled 'L_perp'.](f8349bf298c75500692fbeb4115775b4_img.jpg)

Figure 9.84: A diagram of a stick of length 'l' suspended by two strings of length 'l/2' from a horizontal ceiling. The stick makes an angle 'theta' with the vertical. A rotation vector 'omega' is shown as a curved arrow around the vertical axis. The angular momentum vector 'L' is shown as an arrow originating from the center of mass of the stick, pointing at an angle 'theta' from the vertical. The horizontal component of 'L' is labeled 'L\_perp'.

Fig. 9.84

REMARKS: For  $\theta \rightarrow 0$ , this goes to zero, which makes sense. For  $\theta \rightarrow \pi/2$ , it goes to the finite value  $m\ell\omega^2/12$ , which isn't so obvious. The lever arm and  $|d\mathbf{L}/dt|$  are both small in this limit, and they happen to be proportional to each other as they both head to zero.

Note that if we instead had a massless stick with equal masses  $m/2$  on the ends, so that the relevant moment of inertia is now  $m\ell^2/4$ , then our answer would be  $T = (1/4)m\ell\omega^2 \sin \theta$ . This makes sense if we write it as  $T = (m/2) \cdot (\ell/2) \sin \theta \cdot \omega^2$ , because each tension is responsible for simply keeping a mass  $m/2$  moving in a circle of radius  $(\ell/2) \sin \theta$  at frequency  $\omega$ . This simple force argument doesn't work for the original stick because of internal forces in the stick. ♣

#### 9.11. Stick under a ring

As in Problem 9.10, the angular momentum around the CM can be found by breaking  $\omega$  up into its components along the principal axes of the stick. The reasoning is exactly the same, so the angular momentum at any time has magnitude

$$L = \frac{1}{12}m\ell^2\omega \sin \theta, \quad (9.124)$$

and it points as shown in Fig. 9.85. The change in  $\mathbf{L}$  comes from its horizontal component. This has length  $L \cos \theta$  and travels in a circle at frequency  $\omega$ . Hence,  $|d\mathbf{L}/dt| = \omega L \cos \theta$ , and it is directed into the page at the instant shown.

The torque around the CM has magnitude  $mg(\ell/2) \sin \theta$ , and it points into the page at the instant shown. (This torque arises from the vertical force from the ring. There is no horizontal force from the ring, because the CM does not move.) Therefore,  $\tau = d\mathbf{L}/dt$  gives

$$\frac{mg\ell \sin \theta}{2} = \omega \left( \frac{m\ell^2\omega \sin \theta}{12} \right) \cos \theta \implies \omega = \sqrt{\frac{6g}{\ell \cos \theta}}. \quad (9.125)$$

![Diagram of a stick of length l pivoted at its top end, making an angle theta with the vertical. The center of mass is at l/2. A vector L represents angular momentum, perpendicular to the stick. A dashed circle shows the path of the horizontal component of L. A vertical dashed line indicates the direction of gravity mg and the angular velocity omega.](06b472a80fb398f89a3c942ed43bb093_img.jpg)

Diagram of a stick of length l pivoted at its top end, making an angle theta with the vertical. The center of mass is at l/2. A vector L represents angular momentum, perpendicular to the stick. A dashed circle shows the path of the horizontal component of L. A vertical dashed line indicates the direction of gravity mg and the angular velocity omega.

Fig. 9.85

REMARKS:

1. For  $\theta \rightarrow \pi/2$ , this goes to infinity, which makes sense. For  $\theta \rightarrow 0$ , it goes to  $\sqrt{6g/\ell}$ , which isn't so obvious.
2. The motion in this problem isn't possible if the bottom end of the stick, instead of the top end, slides along the ring. The magnitudes of all quantities are the same as in the original problem, but the torque points in the wrong direction, as you can check. But see Exercise 9.45 for a related setup.
3. Since the middle of the stick is motionless, you might be tempted to treat the bottom half as the stick in the example in Section 9.4.2. That is, you might just want to plug in  $\ell/2$  as the length in Eq. (9.38). This, however, does not yield the answer in Eq. (9.125). The error is that there are internal forces in the stick that provide torques. If a pivot were placed at the CM of the stick (connecting the two halves) in this problem, then the stick would not remain straight.
4. If we replace the stick by a massless string with equal masses  $m/2$  on the ends, then the relevant moment of inertia is  $m\ell^2/4$ , and we obtain  $\omega = \sqrt{2g/(\ell \cos \theta)}$ . This is in fact simply the  $\omega = \sqrt{g/[(\ell/2) \cos \theta]}$  answer for a point-mass circular pendulum of length  $\ell/2$  (see Problem 9.12), because the middle of the string is motionless, and because the flexible string can't provide the internal torques mentioned in the previous paragraph. ♣

![Diagram of a circular pendulum (Fig. 9.86). A mass is suspended by a rod of length l from a pivot. The rod makes an angle theta with the vertical. The mass moves in a horizontal circle, indicated by a dashed line. The forces acting on the mass are tension T (along the rod) and gravity mg (downward).](8f52325d81f967d3fb1ddbd96657a2de_img.jpg)

Diagram of a circular pendulum (Fig. 9.86). A mass is suspended by a rod of length l from a pivot. The rod makes an angle theta with the vertical. The mass moves in a horizontal circle, indicated by a dashed line. The forces acting on the mass are tension T (along the rod) and gravity mg (downward).

Fig. 9.86

![Diagram of a circular pendulum (Fig. 9.87). A mass is suspended by a rod of length l from a pivot. The rod makes an angle theta with the vertical. The mass moves in a horizontal circle, indicated by a dashed line. The forces acting on the mass are tension T (along the rod) and gravity mg (downward). The angular momentum vector L is shown pointing upward and to the right, perpendicular to the plane of the circle.](a13db1d08a99c18ee54857c04da13c00_img.jpg)

Diagram of a circular pendulum (Fig. 9.87). A mass is suspended by a rod of length l from a pivot. The rod makes an angle theta with the vertical. The mass moves in a horizontal circle, indicated by a dashed line. The forces acting on the mass are tension T (along the rod) and gravity mg (downward). The angular momentum vector L is shown pointing upward and to the right, perpendicular to the plane of the circle.

Fig. 9.87

![Diagram of a circular pendulum (Fig. 9.88). A mass is suspended by a rod of length l from a pivot. The rod makes an angle theta with the vertical. The mass moves in a horizontal circle, indicated by a dashed line. The forces acting on the mass are tension T (along the rod) and gravity mg (downward). The angular momentum vector L is shown pointing downward and to the right, perpendicular to the plane of the circle.](ec6e7a6d5598d0ba12349325a99183ea_img.jpg)

Diagram of a circular pendulum (Fig. 9.88). A mass is suspended by a rod of length l from a pivot. The rod makes an angle theta with the vertical. The mass moves in a horizontal circle, indicated by a dashed line. The forces acting on the mass are tension T (along the rod) and gravity mg (downward). The angular momentum vector L is shown pointing downward and to the right, perpendicular to the plane of the circle.

Fig. 9.88

### 9.12. Circular pendulum

- (a) The forces on the mass are gravity and the force from the rod (the tension), which points along the rod (see Fig. 9.86).<sup>29</sup> Since there is no vertical acceleration, we have  $T \cos \theta = mg$ . The unbalanced horizontal force from the tension is therefore  $T \sin \theta = mg \tan \theta$ . This force accounts for the centripetal acceleration,  $m(\ell \sin \theta) \Omega^2$ . Hence,

$$\Omega = \sqrt{\frac{g}{\ell \cos \theta}}. \quad (9.126)$$

For  $\theta \approx 0$ , this is the same as the  $\sqrt{g/\ell}$  frequency for a simple pendulum. For  $\theta \approx \pi/2$ , it goes to infinity, which makes sense. Note that  $\theta$  must be less than  $\pi/2$  for circular motion to be possible. (This restriction doesn't hold for a spinning top with extended mass.)

- (b) The only force that applies a torque relative to the pivot is the gravitational force, so the torque is  $\tau = mg\ell \sin \theta$ , directed into the page at the instant shown in Fig. 9.87.

At this moment, the mass has a speed  $(\ell \sin \theta) \Omega$ , directed into the page. Therefore,  $\mathbf{L} = \mathbf{r} \times \mathbf{p}$  has magnitude  $m\ell^2 \Omega \sin \theta$  and is directed upward to the right, as shown. The tip of  $\mathbf{L}$  traces out a circle of radius  $L \cos \theta$ , at frequency  $\Omega$ . Therefore,  $d\mathbf{L}/dt$  has magnitude  $\Omega L \cos \theta$  and is directed into the page. Hence,  $\tau = d\mathbf{L}/dt$  gives  $mg\ell \sin \theta = \Omega(m\ell^2 \Omega \sin \theta) \cos \theta$ , which yields Eq. (9.126).

- (c) The only force that applies a torque relative to the mass is the force from the pivot, which has two components (see Fig. 9.88). The vertical piece is  $mg$ . Relative to the mass, this provides a torque of  $mg(\ell \sin \theta)$ , directed into the page. There is also the horizontal piece, which accounts for the centripetal acceleration of the mass, so it equals  $m(\ell \sin \theta) \Omega^2$ . Relative to the mass, this provides a torque of  $m\ell \sin \theta \Omega^2(\ell \cos \theta)$ , directed out of the page.

Relative to the mass, there is no angular momentum. Therefore,  $d\mathbf{L}/dt = 0$ , and so there must be no torque. This means that the above two torques must cancel, which gives  $mg(\ell \sin \theta) = m\ell \sin \theta \Omega^2(\ell \cos \theta)$ . This yields Eq. (9.126).

In problems that are more complicated than this one, it is often easier to work with the fixed pivot (if there is one) as the origin, instead of the CM, because then you don't have to worry about the messy pivot forces contributing to the torque.

### 9.13. Rolling in a cone

The forces on the ring are gravity ( $mg$ ), the normal force ( $N$ ) from the cone, and the friction force ( $F$ ) pointing up along the cone (or perhaps down along the cone if  $F$  turns out to be negative, but we'll find that it won't). Since there is no net force in the vertical direction, we have

$$N \sin \theta + F \cos \theta = mg. \quad (9.127)$$

The inward horizontal force accounts for the centripetal acceleration, which gives

$$N \cos \theta - F \sin \theta = m(h \tan \theta) \Omega^2. \quad (9.128)$$

Solving the previous two equations for  $F$  gives

$$F = mg \cos \theta - m\Omega^2(h \tan \theta) \sin \theta, \quad (9.129)$$

<sup>29</sup> The force from the rod must point along the rod because it is massless. If there were a tangential force on the mass, then Newton's third law would say that there would also be a tangential force on the rod. This would then produce a nonzero torque on the rod (relative to the pivot) and hence an infinite angular acceleration, because there is no gravitational torque on the (massless) rod to counter it.

with upward along the cone taken to be positive (this is just a rearrangement of the  $F = ma$  equation along the cone). The torque on the ring (relative to its CM) is due only to this  $F$ , because gravity provides no torque, and  $N$  points through the center of the ring (by the second assumption in the problem). Therefore, the torque points out of the page with magnitude

$$\tau = rF = r(mg \cos \theta - m\Omega^2 h \tan \theta \sin \theta). \quad (9.130)$$

We must now find  $d\mathbf{L}/dt$ . Since we are assuming  $r \ll h \tan \theta$ , the frequency of the spinning of the ring (call it  $\omega$ ) is much greater than the frequency of precession,  $\Omega$ . We will therefore neglect the latter in finding  $\mathbf{L}$ . In this approximation,  $\mathbf{L}$  (relative to the CM) has magnitude  $mr^2\omega$ , and it points downward along the cone (for the direction of motion shown in Fig. 9.45). The horizontal component of  $\mathbf{L}$  has magnitude  $L_{\perp} \equiv L \sin \theta$ , and it traces out a circle at frequency  $\Omega$ . Therefore,  $d\mathbf{L}/dt$  points out of the page with magnitude

$$\left| \frac{d\mathbf{L}}{dt} \right| = \Omega L_{\perp} = \Omega L \sin \theta = \Omega (mr^2\omega) \sin \theta. \quad (9.131)$$

The nonslipping condition is  $r\omega = (h \tan \theta)\Omega$ ,<sup>30</sup> which gives  $\omega = (h \tan \theta)\Omega/r$ . Using this in Eq. (9.131) yields

$$\left| \frac{d\mathbf{L}}{dt} \right| = \Omega^2 m r h \tan \theta \sin \theta. \quad (9.132)$$

Equating this with the torque in Eq. (9.130) gives

$$\Omega = \frac{1}{\tan \theta} \sqrt{\frac{g}{2h}}. \quad (9.133)$$

REMARK: If you consider an object with moment of inertia  $\beta mr^2$  (our ring has  $\beta = 1$ ), then you can show by the above reasoning that the “2” in Eq. (9.133) is replaced by  $(1 + \beta)$ . This means that if we instead have a particle sliding around a frictionless cone (which is equivalent to a ring with  $\beta = 0$ ), then the frequency is  $\sqrt{g/h}/\tan \theta$ , as you can check from scratch. ♣

### 9.14. Tennis racket theorem

ROTATION AROUND  $\hat{\mathbf{x}}_1$ : If the racket is rotated (nearly) around the  $\hat{\mathbf{x}}_1$  axis, then the initial  $\omega_2$  and  $\omega_3$  are much smaller than  $\omega_1$ . To emphasize this, let’s relabel them as  $\omega_2 \rightarrow \epsilon_2$  and  $\omega_3 \rightarrow \epsilon_3$ . Then Eq. (9.45) becomes (with the torque equal to zero, because gravity provides no torque around the CM)

$$\begin{aligned} 0 &= \dot{\omega}_1 - A\epsilon_2\epsilon_3, \\ 0 &= \dot{\epsilon}_2 + B\omega_1\epsilon_3, \\ 0 &= \dot{\epsilon}_3 - C\omega_1\epsilon_2, \end{aligned} \quad (9.134)$$

where we have defined (for convenience)

$$A \equiv \frac{I_2 - I_3}{I_1}, \quad B \equiv \frac{I_1 - I_3}{I_2}, \quad C \equiv \frac{I_1 - I_2}{I_3}. \quad (9.135)$$

Note that  $A$ ,  $B$ , and  $C$  are all positive. This fact will be very important.

Our goal here is to show that if the  $\epsilon$ ’s start out small, then they remain small. Assuming that they are small (which is true initially), the first equation says that

<sup>30</sup> This is technically not quite correct, for the same reason that the earth spins around 366 times instead of 365 times in a year. But it’s valid enough in the limit of small  $r$ .

$\dot{\omega}_1 \approx 0$ , to first order in the  $\epsilon$ 's. Therefore, we may assume that  $\omega_1$  is essentially constant (when the  $\epsilon$ 's are small). Taking the derivative of the second equation then gives  $0 = \ddot{\epsilon}_2 + B\omega_1\dot{\epsilon}_3$ . Plugging the value of  $\dot{\epsilon}_3$  from the third equation into this yields

$$\ddot{\epsilon}_2 = -\left(BC\omega_1^2\right)\epsilon_2. \quad (9.136)$$

Because of the negative coefficient on the right-hand side, this equation describes simple harmonic motion. Therefore,  $\epsilon_2$  oscillates sinusoidally around zero. So if it starts small, it remains small. By the same reasoning,  $\epsilon_3$  remains small.

We therefore see that  $\boldsymbol{\omega} \approx (\omega_1, 0, 0)$  at all times, which implies that  $\mathbf{L} \approx (I_1\omega_1, 0, 0)$  at all times. That is,  $\mathbf{L}$  always points (nearly) along the  $\hat{\mathbf{x}}_1$  direction (which is fixed in the racket frame). But the direction of  $\mathbf{L}$  is fixed in the lab frame, because there is no torque. Therefore, the direction of  $\hat{\mathbf{x}}_1$  must also be (nearly) fixed in the lab frame. In other words, the racket doesn't wobble.

**ROTATION AROUND  $\hat{\mathbf{x}}_3$ :** This calculation goes through exactly as above, except with "1" and "3" interchanged. We find that if  $\epsilon_1$  and  $\epsilon_2$  start small, they remain small.

**ROTATION AROUND  $\hat{\mathbf{x}}_2$ :** If the racket is rotated (nearly) around the  $\hat{\mathbf{x}}_2$  axis, then the initial  $\omega_1$  and  $\omega_3$  are much smaller than  $\omega_2$ . As above, let's emphasize this by relabeling them as  $\omega_1 \rightarrow \epsilon_1$  and  $\omega_3 \rightarrow \epsilon_3$ . Then as above, Eq. (9.45) becomes

$$\begin{aligned} 0 &= \dot{\epsilon}_1 - A\omega_2\epsilon_3, \\ 0 &= \dot{\omega}_2 + B\epsilon_1\epsilon_3, \\ 0 &= \dot{\epsilon}_3 - C\omega_2\epsilon_1. \end{aligned} \quad (9.137)$$

Our goal here is to show that if the  $\epsilon$ 's start out small, then they do *not* remain small. Assuming that they are small (which is true initially), the second equation says that  $\dot{\omega}_2 \approx 0$ , to first order in the  $\epsilon$ 's. So we may assume that  $\omega_2$  is essentially constant (when the  $\epsilon$ 's are small). Taking the derivative of the first equation then gives  $0 = \ddot{\epsilon}_1 - A\omega_2\dot{\epsilon}_3$ . Plugging the value of  $\dot{\epsilon}_3$  from the third equation into this yields

$$\ddot{\epsilon}_1 = \left(AC\omega_2^2\right)\epsilon_1. \quad (9.138)$$

Because of the positive coefficient on the right-hand side, this equation describes an exponentially growing motion, instead of an oscillatory one. Therefore,  $\epsilon_1$  grows quickly from its initial small value. So even if it starts small, it becomes large. By the same reasoning,  $\epsilon_3$  becomes large. Of course, once the  $\epsilon$ 's become large, then our assumption of  $\dot{\omega}_2 \approx 0$  isn't valid anymore. But once the  $\epsilon$ 's become large, we've shown what we wanted to.

We see that  $\boldsymbol{\omega}$  does *not* remain (nearly) equal to  $(0, \omega_2, 0)$ , which implies that  $\mathbf{L}$  does *not* remain (nearly) equal to  $(0, I_2\omega_2, 0)$ . That is,  $\mathbf{L}$  does not always point (nearly) along the  $\hat{\mathbf{x}}_2$  direction (which is fixed in the racket frame). But the direction of  $\mathbf{L}$  is fixed in the lab frame, because there is no torque. Therefore, the direction of  $\hat{\mathbf{x}}_2$  must change in the lab frame. In other words, the racket wobbles.

### 9.15. Free-top angles

In terms of the principal axes,  $\hat{\mathbf{x}}_1, \hat{\mathbf{x}}_2, \hat{\mathbf{x}}_3$ , we have

$$\begin{aligned} \boldsymbol{\omega} &= (\omega_1\hat{\mathbf{x}}_1 + \omega_2\hat{\mathbf{x}}_2) + \omega_3\hat{\mathbf{x}}_3, \quad \text{and} \\ \mathbf{L} &= I(\omega_1\hat{\mathbf{x}}_1 + \omega_2\hat{\mathbf{x}}_2) + I_3\omega_3\hat{\mathbf{x}}_3. \end{aligned} \quad (9.139)$$

Let  $\boldsymbol{\omega}_\perp \hat{\boldsymbol{\omega}}_\perp \equiv (\omega_1\hat{\mathbf{x}}_1 + \omega_2\hat{\mathbf{x}}_2)$  be the component of  $\boldsymbol{\omega}$  orthogonal to  $\boldsymbol{\omega}_3$ . Then we have

$$\tan \beta = \frac{\omega_\perp}{\omega_3}, \quad \text{and} \quad \tan \alpha = \frac{I\omega_\perp}{I_3\omega_3}. \quad (9.140)$$

Therefore,

$$\frac{\tan \alpha}{\tan \beta} = \frac{I}{I_3}. \quad (9.141)$$

If  $I > I_3$ , then  $\alpha > \beta$ , and we have the situation shown in Fig. 9.89. A top with this property is called a “prolate top.” An example is an American football or a pencil.

If  $I < I_3$ , then  $\alpha < \beta$ , and we have the situation shown in Fig. 9.90. A top with this property is called an “oblate top.” An example is a coin or a Frisbee.

#### 9.16. Staying above

If  $I < I_3$  (oblate top), then the initial  $\hat{\mathbf{x}}_3$ ,  $\boldsymbol{\omega}$ , and  $\mathbf{L}$  vectors look like those in Fig. 9.91, with  $\mathbf{L}$  between  $\hat{\mathbf{x}}_3$  and  $\boldsymbol{\omega}$ . The  $\boldsymbol{\omega}$  vector traces out a cone around  $\mathbf{L}$  as shown, so it always stays above the horizontal (because it starts above the horizontal).

However, if  $I > I_3$  (prolate top), then the initial  $\hat{\mathbf{x}}_3$ ,  $\boldsymbol{\omega}$ , and  $\mathbf{L}$  vectors look like those in Fig. 9.92, with  $\boldsymbol{\omega}$  between  $\hat{\mathbf{x}}_3$  and  $\mathbf{L}$ . Depending on the values of  $I/I_3$  and  $\omega_{\perp}/\omega_3$  (where  $\omega_{\perp}$  is the component of  $\boldsymbol{\omega}$  orthogonal to  $\hat{\mathbf{x}}_3$ ), the  $\boldsymbol{\omega}$  cone might stay above the horizontal axis, or it might dip below it. We are concerned with the cutoff case where it just touches the axis, as shown.

From Fig. 9.92, the half-angle of the cone is  $\alpha - \beta$ , so if the cone reaches down to the horizontal axis, then we have  $\alpha + (\alpha - \beta) = 90^\circ$ . But  $\alpha$  and  $\beta$  are given by

$$\tan \beta = \frac{\omega_{\perp}}{\omega_3}, \quad \text{and} \quad \tan \alpha = \frac{L_{\perp}}{L_3} = \frac{I\omega_{\perp}}{I_3\omega_3}. \quad (9.142)$$

Therefore, the  $2\alpha - \beta = 90^\circ$  condition becomes

$$2 \tan^{-1} \left( \frac{I\omega_{\perp}}{I_3\omega_3} \right) - \tan^{-1} \left( \frac{\omega_{\perp}}{\omega_3} \right) = 90^\circ. \quad (9.143)$$

With  $n \equiv I/I_3$  and  $x \equiv \omega_{\perp}/\omega_3$ , this yields

$$\begin{aligned} 2 \tan^{-1}(nx) - \tan^{-1}(x) &= 90^\circ \\ \implies \tan(2 \tan^{-1}(nx)) &= \tan(90^\circ + \tan^{-1}(x)) \\ \implies \frac{2nx}{1 - n^2x^2} &= -\frac{1}{x} \\ \implies n(n-2)x^2 &= 1. \end{aligned} \quad (9.144)$$

We see that if  $n \leq 2$ , there is no solution for  $x$ . But if  $n > 2$ , there is a solution. Therefore, the answer to the problem is  $n = 2$ .

**REMARKS:** If  $n$  is only slightly larger than 2, then the solution for  $x$  in Eq. (9.144) (and hence  $\omega_{\perp}$ ) is large. This means that your strike needs to be large, in order to produce a large  $\omega_{\perp}$ .

There are three interesting limits of what can happen in the large- $n$  limit, so let's list them out. For these three cases, picture a thin stick spinning around its vertical  $x_3$  axis, and then imagine striking the bottom end with different impulses.

- If  $\omega_{\perp} \ll \omega_3$  and  $L_{\perp} \ll L_3$ , then both  $\boldsymbol{\omega}$  and  $\mathbf{L}$  point nearly straight upwards, so  $\boldsymbol{\omega}$  traces out a very thin cone around  $\mathbf{L}$  and is always nearly vertical.  $\hat{\mathbf{x}}_3$  is also always nearly vertical.
- If  $\omega_{\perp} \ll \omega_3$  but  $L_{\perp} \gg L_3$  (which is possible if  $n$  is sufficiently large), then  $\boldsymbol{\omega}$  points nearly straight upwards initially, whereas  $\mathbf{L}$  points nearly horizontally. So  $\boldsymbol{\omega}$  traces out a very wide cone and swings down almost to the negative vertical direction.  $\hat{\mathbf{x}}_3$  also traces out a very wide cone.
- If  $\omega_{\perp} \gg \omega_3$ , which implies  $L_{\perp} \gg L_3$ , then both  $\boldsymbol{\omega}$  and  $\mathbf{L}$  point nearly horizontally, so  $\boldsymbol{\omega}$  traces out a very thin cone around  $\mathbf{L}$  and is always nearly horizontal.

![Figure 9.89: A diagram showing a vertical vector L and two other vectors, omega and x_hat_3. Vector L is vertical. Vector x_hat_3 is at an angle beta from the vertical. Vector omega is at an angle alpha from the vertical. Since alpha > beta, omega is further from the vertical than x_hat_3. The angle between omega and x_hat_3 is alpha - beta.](db9ea96159d7def1737f22b5534df68c_img.jpg)

Figure 9.89: A diagram showing a vertical vector L and two other vectors, omega and x\_hat\_3. Vector L is vertical. Vector x\_hat\_3 is at an angle beta from the vertical. Vector omega is at an angle alpha from the vertical. Since alpha > beta, omega is further from the vertical than x\_hat\_3. The angle between omega and x\_hat\_3 is alpha - beta.

Fig. 9.89

![Figure 9.90: A diagram showing a vertical vector L and two other vectors, omega and x_hat_3. Vector L is vertical. Vector x_hat_3 is at an angle beta from the vertical. Vector omega is at an angle alpha from the vertical. Since alpha < beta, omega is closer to the vertical than x_hat_3. The angle between omega and x_hat_3 is beta - alpha.](8fe417506250e297ccdfb404e343b4f4_img.jpg)

Figure 9.90: A diagram showing a vertical vector L and two other vectors, omega and x\_hat\_3. Vector L is vertical. Vector x\_hat\_3 is at an angle beta from the vertical. Vector omega is at an angle alpha from the vertical. Since alpha < beta, omega is closer to the vertical than x\_hat\_3. The angle between omega and x\_hat\_3 is beta - alpha.

Fig. 9.90

![Figure 9.91: A diagram showing a vertical vector x_hat_3 and two other vectors, L and omega. Vector x_hat_3 is vertical. Vector L is at an angle beta from the vertical. Vector omega is at an angle alpha from the vertical. Since alpha > beta, omega is further from the vertical than L. A dashed cone is shown around L, representing the path of omega. The angle between omega and the horizontal dashed line is alpha - beta.](868b0e69c005ed4ca462e93e13c65a15_img.jpg)

Figure 9.91: A diagram showing a vertical vector x\_hat\_3 and two other vectors, L and omega. Vector x\_hat\_3 is vertical. Vector L is at an angle beta from the vertical. Vector omega is at an angle alpha from the vertical. Since alpha > beta, omega is further from the vertical than L. A dashed cone is shown around L, representing the path of omega. The angle between omega and the horizontal dashed line is alpha - beta.

Fig. 9.91

![Figure 9.92: A diagram showing a vertical vector x_hat_3 and two other vectors, omega and L. Vector x_hat_3 is vertical. Vector omega is at an angle beta from the vertical. Vector L is at an angle alpha from the vertical. Since alpha > beta, L is further from the vertical than omega. A dashed cone is shown around omega, representing the path of L. The angle between L and the horizontal dashed line is alpha - beta.](34485e3802ffdfe195b074ad5cd7e586_img.jpg)

Figure 9.92: A diagram showing a vertical vector x\_hat\_3 and two other vectors, omega and L. Vector x\_hat\_3 is vertical. Vector omega is at an angle beta from the vertical. Vector L is at an angle alpha from the vertical. Since alpha > beta, L is further from the vertical than omega. A dashed cone is shown around omega, representing the path of L. The angle between L and the horizontal dashed line is alpha - beta.

Fig. 9.92

$\hat{\mathbf{x}}_3$  still traces out a very wide cone, because it starts vertical (by assumption), independent of where  $\boldsymbol{\omega}$  and  $\mathbf{L}$  are. Note that your eye can't distinguish between the second and third cases here, because the  $\hat{\mathbf{x}}_3$  axis is doing the same thing in both cases. ♣

### 9.17. The top

- (a) In order for there to exist real solutions for  $\Omega$  in Eq. (9.82), the discriminant must be non-negative. If  $\theta > \pi/2$ , then  $\cos \theta < 0$ , so the discriminant is automatically positive, and any value of  $\omega_3$  is allowed. But if  $\theta < \pi/2$ , then the lower limit on  $\omega_3$  is

$$\omega_3 \geq \frac{\sqrt{4Mg\ell \cos \theta}}{I_3} \equiv \tilde{\omega}_3. \quad (9.145)$$

The special case of  $\theta = \pi/2$  requires a limit to be taken; it turns out that there is only one (noninfinite) solution, as we'll see in part (b). Note that at the critical value of  $\omega_3$  in Eq. (9.145), Eq. (9.82) gives

$$\Omega_+ = \Omega_- = \frac{I_3 \tilde{\omega}_3}{2I \cos \theta} = \sqrt{\frac{Mg\ell}{I \cos \theta}} \equiv \Omega_0. \quad (9.146)$$

- (b) Since  $\omega_3$  has units, “large  $\omega_3$ ” is a meaningless description. What we really mean is that the fraction in the square root in Eq. (9.82) is very small compared with 1. That is,  $\epsilon \equiv (4Mg\ell \cos \theta)/(I_3^2 \omega_3^2) \ll 1$ . In this case, we can use  $\sqrt{1 - \epsilon} \approx 1 - \epsilon/2 + \dots$  to write

$$\Omega_{\pm} \approx \frac{I_3 \omega_3}{2I \cos \theta} \left( 1 \pm \left( 1 - \frac{2Mg\ell \cos \theta}{I_3^2 \omega_3^2} \right) \right). \quad (9.147)$$

The two solutions for  $\Omega$  are then, to leading order in  $\omega_3$  (or rather, to leading order in  $\epsilon$ ),

$$\Omega_+ \approx \frac{I_3 \omega_3}{I \cos \theta}, \quad \text{and} \quad \Omega_- \approx \frac{Mg\ell}{I_3 \omega_3}. \quad (9.148)$$

These are known as the “fast” and “slow” frequencies of precession, respectively.  $\Omega_-$  is the approximate answer we found in Eq. (9.77). It was obtained here under the assumption  $\epsilon \ll 1$ , which is equivalent to

$$\omega_3 \gg \frac{\sqrt{4Mg\ell \cos \theta}}{I_3} \quad (\text{that is, } \omega_3 \gg \tilde{\omega}_3). \quad (9.149)$$

This, therefore, is the condition for the result in Eq. (9.77) to be a good approximation. If  $I$  is of the same order as  $I_3$ , so that they are both of order  $M\ell^2$  (assuming that the top is a reasonably shaped object without any strange tails), and if  $\cos \theta$  is of order 1, then this condition can be written as  $\omega_3 \gg \sqrt{g/\ell}$ , which is the frequency of a pendulum of length  $\ell$ .

##### REMARKS:

1. The  $\Omega_+$  solution is a fairly surprising result. Two strange features of  $\Omega_+$  are that it grows with  $\omega_3$ , and that it is independent of  $g$ . To see what is going on with this precession, note that  $\Omega_+$  is the value of  $\Omega$  that makes the  $L_{\perp}$  in Eq. (9.79) essentially equal to zero. So  $\mathbf{L}$  points nearly along the vertical axis. The rate of change of  $\mathbf{L}$  is the product of a very small horizontal radius (of the tiny circle the tip traces out) and a very large  $\Omega$  (assuming that  $\omega_3$  is large). The product of these equals the “medium sized” torque,  $Mg\ell \sin \theta$ .
2. In the limit of large  $\omega_3$ , the fast precession should look basically like the motion of a free top, because the  $\mathbf{L}$  here points essentially in a fixed direction, just as it does for a free top. And indeed,  $\Omega_+$  is independent of  $g$ . More

precisely, we can see that the value of  $\Omega_+$  given in Eq. (9.148) agrees with the free-top precession frequency, by the following reasoning.  $I_3\omega_3$  is the component of  $\mathbf{L}$  along the symmetry axis, which makes an angle  $\theta$  with the vertical (which is essentially the direction of  $\mathbf{L}$ ). Therefore,  $\mathbf{L}$  has magnitude  $L \approx I_3\omega_3/\cos\theta$ , which means we can write  $\Omega_+ \approx L/I$ . This is the precession frequency of a free top, given in Eq. (9.55), as viewed from a fixed frame.

- 3. We can plot the  $\Omega_{\pm}$  in Eq. (9.82) as functions of  $\omega_3$ . With the definitions of  $\tilde{\omega}_3$  and  $\Omega_0$  in Eqs. (9.145) and (9.146), we can rewrite Eq. (9.82) as

$$\Omega_{\pm} = \frac{\omega_3\Omega_0}{\tilde{\omega}_3} \left( 1 \pm \sqrt{1 - \frac{\tilde{\omega}_3^2}{\omega_3^2}} \right). \quad (9.150)$$

Since it is easier to work with dimensionless quantities, let's rewrite this as

$$y_{\pm} = x \pm \sqrt{x^2 - 1}, \quad \text{where } y_{\pm} \equiv \frac{\Omega_{\pm}}{\Omega_0}, \quad \text{and } x \equiv \frac{\omega_3}{\tilde{\omega}_3}. \quad (9.151)$$

A rough plot of  $y_{\pm}$  vs.  $x$  is shown in Fig. 9.93. The behavior of this graph for large  $x$  is found from Eq. (9.151) to be  $y_+ \approx 2x$ , and  $y_- \approx 1/(2x)$ . You can show that these are equivalent to the results in Eq. (9.148). ♣

![Figure 9.93: A graph showing the dimensionless precession frequencies y_+ and y_- as functions of the dimensionless spin frequency x. The vertical axis is labeled y_± and has a mark at y_± = 1. The horizontal axis is labeled x and has a mark at x = 1. The curve for y_+ starts at (1, 1) and increases monotonically, passing through (1, 1) and curving upwards. The curve for y_- starts at (1, 1) and decreases monotonically, passing through (1, 1) and curving downwards towards the x-axis.](2c520da662754886c1a2db91bbac1dfc_img.jpg)

Figure 9.93: A graph showing the dimensionless precession frequencies y\_+ and y\_- as functions of the dimensionless spin frequency x. The vertical axis is labeled y\_± and has a mark at y\_± = 1. The horizontal axis is labeled x and has a mark at x = 1. The curve for y\_+ starts at (1, 1) and increases monotonically, passing through (1, 1) and curving upwards. The curve for y\_- starts at (1, 1) and decreases monotonically, passing through (1, 1) and curving downwards towards the x-axis.

Fig. 9.93

### 9.18. Many tops

The system is made up of  $N$  rigid bodies, each consisting of a disk and a massless stick glued to it on its left (see Fig. 9.94). Label these subsystems as  $S_i$ , with  $S_1$  being the one closest to the pole. Let each disk have mass  $m$  and moment of inertia  $I$ , and let each stick have length  $\ell$ . Let the angular speeds be  $\omega_i$ . The relevant angular momentum of  $S_i$  is then  $L_i = I\omega_i$ , and it points horizontally.<sup>31</sup> Let the desired precession frequency be  $\Omega$ . Then  $d\mathbf{L}_i/dt$  has magnitude  $L_i\Omega = (I\omega_i)\Omega$  and points into the page at the instant shown in Fig. 9.94.

Consider the torque  $\boldsymbol{\tau}_i$  on  $S_i$ , around its CM. Let's first look at  $S_1$ . The pole provides an upward force of  $Nmg$  (this force is what keeps all the tops up), so it provides a torque of  $Nmg\ell$  (into the page) around the CM of  $S_1$ . The downward force from the stick on the right provides no torque around the CM, because it acts at the CM. Likewise, the gravitational force on  $S_1$  provides no torque around the CM. Therefore,  $\boldsymbol{\tau}_1 = d\mathbf{L}_1/dt$  gives  $Nmg\ell = (I\omega_1)\Omega$ , and so

$$\omega_1 = \frac{Nmg\ell}{I\Omega}. \quad (9.152)$$

Now look at  $S_2$ .  $S_1$  provides an upward force of  $(N-1)mg$  (this force is what keeps  $S_2$  through  $S_N$  up), so it provides a torque of  $(N-1)mg\ell$  around the CM of  $S_2$ . As with  $S_1$ , this is the only torque on  $S_2$ . Therefore,  $\boldsymbol{\tau}_2 = d\mathbf{L}_2/dt$  gives  $(N-1)mg\ell = (I\omega_2)\Omega$ , and so

$$\omega_2 = \frac{(N-1)mg\ell}{I\Omega}. \quad (9.153)$$

Similar reasoning applies to the other  $S_i$ , so we arrive at

$$\omega_i = \frac{(N+1-i)mg\ell}{I\Omega}. \quad (9.154)$$

The  $\omega_i$  are therefore in the ratio

$$\omega_1 : \omega_2 : \dots : \omega_{N-1} : \omega_N = N : (N-1) : \dots : 2 : 1. \quad (9.155)$$

![Figure 9.94: A diagram of a single top subsystem S_i. It consists of a vertical stick on the left and a disk on the right. The disk is tilted at an angle, and its angular momentum vector L_i is shown as a horizontal arrow pointing to the right. The torque vector tau_i is shown as a horizontal arrow pointing into the page (indicated by a cross in a circle) at the center of mass of the disk.](5251da0cde5cbe653df9d03e9ebf1e19_img.jpg)

Figure 9.94: A diagram of a single top subsystem S\_i. It consists of a vertical stick on the left and a disk on the right. The disk is tilted at an angle, and its angular momentum vector L\_i is shown as a horizontal arrow pointing to the right. The torque vector tau\_i is shown as a horizontal arrow pointing into the page (indicated by a cross in a circle) at the center of mass of the disk.

Fig. 9.94

<sup>31</sup> We're ignoring the angular momentum arising from the precession. This part of  $\mathbf{L}$  points vertically (because the tops all point horizontally) and therefore doesn't change. Hence, it doesn't enter into  $\boldsymbol{\tau} = d\mathbf{L}/dt$ .

Note that we needed to apply  $\boldsymbol{\tau} = d\mathbf{L}/dt$  many times, using each CM as the origin. Using only the pivot point on the pole as the origin would have given us only one piece of information, whereas we needed  $N$  pieces.

REMARKS: As a double-check, we can verify that the above  $\omega$ 's make  $\boldsymbol{\tau} = d\mathbf{L}/dt$  true, where  $\boldsymbol{\tau}$  and  $\mathbf{L}$  are the total torque and angular momentum relative to the pivot on the pole. The CM of the entire system is  $(N+1)\ell/2$  from the pole, so the torque due to gravity is

$$\tau = Nmg \frac{(N+1)\ell}{2}. \quad (9.156)$$

The total angular momentum is, using Eq. (9.154),

$$\begin{aligned} L &= I(\omega_1 + \omega_2 + \cdots + \omega_N) \\ &= \frac{mg\ell}{\Omega} (N + (N-1) + (N-2) + \cdots + 2 + 1) \\ &= \frac{mg\ell}{\Omega} \left( \frac{N(N+1)}{2} \right). \end{aligned} \quad (9.157)$$

Comparing this with Eq. (9.156), we see that  $\tau = L\Omega$ , that is,  $\tau = |d\mathbf{L}/dt|$ .

We can also pose this problem for the setup where all the  $\omega_i$  are equal (call them  $\omega$ ), and the goal is to find the lengths of the sticks that allow circular precession with the sticks always forming a straight horizontal line. We can use the same reasoning as above, and Eq. (9.154) takes the modified form

$$\omega = \frac{(N+1-i)mg\ell_i}{I\Omega}, \quad (9.158)$$

where  $\ell_i$  is the length of the  $i$ th stick. Therefore, the  $\ell_i$  are in the ratio

$$\ell_1 : \ell_2 : \cdots : \ell_{N-1} : \ell_N = \frac{1}{N} : \frac{1}{N-1} : \cdots : \frac{1}{2} : 1. \quad (9.159)$$

Again, we can verify that these  $\ell$ 's make  $\boldsymbol{\tau} = d\mathbf{L}/dt$  true, where  $\boldsymbol{\tau}$  and  $\mathbf{L}$  are the total torque and angular momentum relative to the pivot on the pole. As an exercise, you can show that the CM happens to be a distance  $\ell_N$  from the pole. So the torque due to gravity is, using Eq. (9.158) to obtain  $\ell_N$ ,

$$\tau = Nmg\ell_N = Nmg(\omega I \Omega / mg) = NI\omega\Omega. \quad (9.160)$$

The total angular momentum is simply  $L = NI\omega$ . So indeed,  $\tau = L\Omega = |d\mathbf{L}/dt|$ . Note that since the sum  $\sum 1/n$  diverges, it is possible to make the setup extend arbitrarily far from the pole. ♣

#### 9.19. Heavy top on a slippery table

In Section 9.7.3, we looked at  $\boldsymbol{\tau}$  and  $\mathbf{L}$  relative to the pivot point. Such quantities are of no use now, because the pivot is accelerating, so it isn't a legal choice of origin for applying  $\boldsymbol{\tau} = d\mathbf{L}/dt$ . We will therefore look at  $\boldsymbol{\tau}$  and  $\mathbf{L}$  relative to the CM, which is always a legal origin for applying  $\boldsymbol{\tau} = d\mathbf{L}/dt$ .

With the CM as our origin, there are two modifications we need to make to the derivation in Section 9.7.3. First, the moments of inertia are now measured with respect to the CM, instead of the pivot point.  $I_3$  is unchanged, but the parallel-axis theorem gives the new  $I$  as

$$I' \equiv I - M\ell^2. \quad (9.161)$$

Second, the torque is modified. The only force from the frictionless floor is the normal force  $N$ . But  $N$  is not necessarily equal to  $Mg$ , because the CM may be accelerating in the vertical direction. The vertical  $F = ma$  equation is  $N - Mg = M\ddot{y}$ , where  $y = \ell \cos \theta$ . Taking the second derivative of  $y$ , we obtain  $N = Mg - M\ell(\ddot{\theta} \sin \theta + \dot{\theta}^2 \cos \theta)$ . The torque relative to the CM therefore has magnitude

$$\tau = N\ell \sin \theta = Mg\ell \sin \theta - M\ell^2 \sin \theta (\ddot{\theta} \sin \theta + \dot{\theta}^2 \cos \theta), \quad (9.162)$$

and it points in the same direction as in Section 9.7.3. Putting everything together, we see that Eq. (9.69) is unchanged, Eq. (9.70) has  $I$  replaced with  $I' \equiv I - M\ell^2$ , and the second of Eqs. (9.70) also has an extra term and becomes

$$(Mg\ell - M\ell^2(\ddot{\theta} \sin \theta + \dot{\theta}^2 \cos \theta) + I'\dot{\phi}^2 \cos \theta - I_3\omega_3\dot{\phi}) \sin \theta = I\ddot{\theta}. \quad (9.163)$$

Note that if  $\dot{\theta} \equiv 0$ , the only modification needed is the change in  $I$ .

If you prefer to use the Lagrangian method in Section 9.7.4, then  $I$  needs to be changed to  $I'$  as above, and the other modification comes in the kinetic energy in the Lagrangian. We must add on the kinetic energy of the whole object treated like a point mass at the CM, because so far we have included only the kinetic energy relative to our new origin (the CM). Since the table is frictionless, the CM can move only vertically, so its velocity is  $\dot{y} = -\ell\dot{\theta} \sin \theta$ . Therefore, we have to add the term  $M(\ell\dot{\theta} \sin \theta)^2/2$  to the Lagrangian. You can show that this leads to the extra term in Eq. (9.163).

#### 9.20. Fixed highest point

For the desired motion with  $P$  always the highest point, the important thing to note is that every point in the top moves in a fixed circle around the  $\hat{\mathbf{z}}$  axis. Therefore,  $\boldsymbol{\omega}$  points vertically at all times. Hence, if  $\Omega$  is the frequency of precession, we have  $\boldsymbol{\omega} = \Omega\hat{\mathbf{z}}$ .

Another way to see that  $\boldsymbol{\omega}$  points vertically is to view things in the frame that rotates with angular velocity  $\Omega\hat{\mathbf{z}}$ . In this frame, the top has no motion at all. It isn't even spinning, because the point  $P$  is always the highest point. In the language of Fig. 9.30, we therefore have  $\omega' = 0$ , so  $\boldsymbol{\omega} = \Omega\hat{\mathbf{z}} + \omega'\hat{\mathbf{x}}_3 = \Omega\hat{\mathbf{z}}$ .

The principal moments are (with the pivot as the origin; see Fig. 9.95)

$$I_3 = \frac{MR^2}{2}, \quad \text{and} \quad I \equiv I_1 = I_2 = M\ell^2 + \frac{MR^2}{4}, \quad (9.164)$$

where we have used the parallel-axis theorem in finding  $I$ . The components of  $\boldsymbol{\omega}$  along the principal axes are  $\omega_3 = \Omega \cos \theta$  and  $\omega_2 = \Omega \sin \theta$ . Therefore (keeping things in terms of the general moments,  $I_3$  and  $I$ , for now),

$$\mathbf{L} = I_3\Omega \cos \theta \hat{\mathbf{x}}_3 + I\Omega \sin \theta \hat{\mathbf{x}}_2. \quad (9.165)$$

The horizontal component of  $\mathbf{L}$  is then  $L_{\perp} = (I_3\Omega \cos \theta) \sin \theta - (I\Omega \sin \theta) \cos \theta$ , so  $d\mathbf{L}/dt$  has magnitude

$$\left| \frac{d\mathbf{L}}{dt} \right| = L_{\perp}\Omega = \Omega^2 \sin \theta \cos \theta (I_3 - I), \quad (9.166)$$

and it is directed into the page (or out of the page, if this quantity is negative). This must equal the torque, which has magnitude  $|\boldsymbol{\tau}| = Mg\ell \sin \theta$  and is directed into the page. Therefore,

$$\Omega = \sqrt{\frac{Mg\ell}{(I_3 - I) \cos \theta}}. \quad (9.167)$$

![Diagram of a spinning top. A vertical axis is labeled x2. A horizontal axis is labeled x3. The top's symmetry axis is at an angle theta from the vertical. The center of mass is at distance l from the pivot. The top has radius R. The angular velocity vector omega is shown pointing vertically upwards. The point P is at the top of the top.](180d77b56743c2caf479d731c4b0ae4f_img.jpg)

Diagram of a spinning top. A vertical axis is labeled x2. A horizontal axis is labeled x3. The top's symmetry axis is at an angle theta from the vertical. The center of mass is at distance l from the pivot. The top has radius R. The angular velocity vector omega is shown pointing vertically upwards. The point P is at the top of the top.

Fig. 9.95

We see that for a general symmetric top, the desired precessional motion (where the same “side” always points up) is possible only if the product  $(I_3 - I) \cos \theta$  is greater than zero. That is,

$$\begin{aligned}\theta < \pi/2 &\implies I_3 > I, \\ \theta > \pi/2 &\implies I_3 < I.\end{aligned}\quad (9.168)$$

For the problem at hand,  $I_3$  and  $I$  are given in Eq. (9.164), so we find

$$\Omega = \sqrt{\frac{4g\ell}{(R^2 - 4\ell^2) \cos \theta}}. \quad (9.169)$$

The necessary condition for such motion to exist is therefore  $R > 2\ell$  if  $\theta < \pi/2$ , or  $R < 2\ell$  if  $\theta > \pi/2$ .

##### REMARKS:

1. It is intuitively clear that  $\Omega$  should become very large as  $\theta \rightarrow \pi/2$ , although it is by no means intuitively clear that such motion should exist at all for angles near  $\pi/2$ .
2. If  $\theta > \pi/2$  and  $R = 0$ , we simply have the circular pendulum discussed in Problem 9.12. And indeed, when  $R = 0$ , the result in Eq. (9.169) reduces to  $\Omega = \sqrt{g/\ell \cos \alpha}$ , where  $\alpha \equiv \pi - \theta$ , which agrees with the result in Eq. (9.126).
3.  $\Omega$  approaches a nonzero constant as  $\theta \rightarrow 0$  or  $\theta \rightarrow \pi$  (depending on the sign of  $I_3 - I$ ), which isn't entirely obvious.
4. If both  $R$  and  $\ell$  are scaled up by the same factor, Eq. (9.169) shows that  $\Omega$  decreases. This also follows from dimensional analysis.
5. Assuming that  $\theta < \pi/2$  (the  $\theta > \pi/2$  case can be handled in a similar manner), the condition  $I_3 > I$  can be understood in the following way. If  $I_3 = I$ , then  $\mathbf{L} \propto \boldsymbol{\omega}$ , so  $\mathbf{L}$  points vertically along  $\boldsymbol{\omega}$ . If  $I_3 > I$ , then  $\mathbf{L}$  points somewhere to the right of the  $z$  axis (at the instant shown in Fig. 9.95). This means that the tip of  $\mathbf{L}$  is moving into the page, along with the top. This is what we need, because  $\boldsymbol{\tau}$  points into the page. If, however,  $I_3 < I$ , then  $\mathbf{L}$  points somewhere to the left of the  $z$  axis, so  $d\mathbf{L}/dt$  points out of the page, and hence cannot be equal to  $\boldsymbol{\tau}$ . ♣

#### 9.21. Basketball on a rim

Assume that the precessional motion is counterclockwise when viewed from above, as indicated in Fig. 9.52. Let's look at things in the frame that has the center of the rim as its origin and that rotates with angular velocity  $\Omega \hat{\mathbf{z}}$ . In this frame, the center of the ball is at rest, and the rim spins clockwise with angular speed  $\Omega$ . If the contact points are to form a great circle on the ball, the ball must be spinning around the (negative)  $\hat{\mathbf{x}}_3$  axis shown in Fig. 9.96. Let the frequency of this spinning be  $\omega'$  (in the language of Fig. 9.30). Then the nonslipping condition says that  $\omega' r = \Omega R$ , and so  $\omega' = \Omega R/r$ . Therefore, the total angular velocity of the ball with respect to the lab frame is

$$\boldsymbol{\omega} = \Omega \hat{\mathbf{z}} - \omega' \hat{\mathbf{x}}_3 = \Omega \hat{\mathbf{z}} - (R/r) \Omega \hat{\mathbf{x}}_3. \quad (9.170)$$

Let us choose the center of the ball as the origin around which we calculate  $\boldsymbol{\tau}$  and  $\mathbf{L}$ . Then every axis in the ball is a principal axis with moment of inertia  $I = (2/3)mr^2$ . The angular momentum is therefore

$$\mathbf{L} = I\boldsymbol{\omega} = I\Omega \hat{\mathbf{z}} - I(R/r)\Omega \hat{\mathbf{x}}_3. \quad (9.171)$$

![Diagram of a basketball on a rim. The ball is shown in cross-section, touching the rim at two points labeled 'contact points'. The rim is a horizontal line segment of length R. The ball has radius r. A vertical axis z passes through the center of the ball. A horizontal axis x3 passes through the center of the ball, pointing to the right. The angle between the z-axis and the line connecting the center of the ball to the contact points is labeled theta. The angle between the x3-axis and the line connecting the center of the ball to the contact points is also labeled theta. The ball is spinning around the x3-axis with angular velocity omega'.](eddfdefa81d468c13a50487339cc7069_img.jpg)

Diagram of a basketball on a rim. The ball is shown in cross-section, touching the rim at two points labeled 'contact points'. The rim is a horizontal line segment of length R. The ball has radius r. A vertical axis z passes through the center of the ball. A horizontal axis x3 passes through the center of the ball, pointing to the right. The angle between the z-axis and the line connecting the center of the ball to the contact points is labeled theta. The angle between the x3-axis and the line connecting the center of the ball to the contact points is also labeled theta. The ball is spinning around the x3-axis with angular velocity omega'.

Fig. 9.96

Only the  $\hat{x}_3$  piece has a horizontal component which contributes to  $d\mathbf{L}/dt$ . This component has length  $L_{\perp} = I(R/r)\Omega \sin \theta$ . Therefore,  $d\mathbf{L}/dt$  has magnitude

$$\left| \frac{d\mathbf{L}}{dt} \right| = \Omega L_{\perp} = \frac{2}{3} \Omega^2 m r R \sin \theta, \quad (9.172)$$

and it points out of the page.

The torque (relative to the center of the ball) comes from the force at the contact point. There are two components to this force. The vertical component is  $mg$ , and the horizontal component is  $m(R - r \cos \theta)\Omega^2$  (pointing to the left), because the center of the ball moves in a circle of radius  $(R - r \cos \theta)$ . The torque therefore has magnitude

$$|\tau| = mg(r \cos \theta) - m(R - r \cos \theta)\Omega^2(r \sin \theta), \quad (9.173)$$

with out of the page taken to be positive. Equating this  $|\tau|$  with the  $|d\mathbf{L}/dt|$  in Eq. (9.172) gives

$$\Omega^2 = \frac{g}{\frac{5}{3}R \tan \theta - r \sin \theta}. \quad (9.174)$$

##### REMARKS:

1.  $\Omega \rightarrow \infty$  as  $\theta \rightarrow 0$ , which makes sense. And  $\Omega \rightarrow 0$  as  $\theta \rightarrow \pi/2$ , which also makes sense.
2.  $\Omega \rightarrow \infty$  when  $R = (3/5)r \cos \theta$ . But this isn't physical, because we must have  $R > r \cos \theta$  in order for the other side of the rim to be outside the ball.
3. You can also work out the problem for the case where the contact points trace out a circle other than a great circle (say, one that is inclined at an angle  $\beta$  below the great circle). The expression for the torque in Eq. (9.173) is unchanged, but the value of  $\omega'$  and the angle of the  $\hat{x}_3$  axis both change, so Eq. (9.172) is modified. If you want to play around with this, one thing you can show (with a bit of work) is that if  $R \gg r$  and if you want the ball to travel around the rim infinitely fast, then  $\beta$  must equal  $\tan^{-1}((5/2) \tan \theta)$ . This is larger than  $\theta$ , so the contact-point circle actually lies below the horizontal. ♣

#### 9.22. Rolling lollipop

We must first find the angular velocity vector  $\omega$ . Assume that the precessional motion is clockwise when viewed from above, as indicated in Fig. 9.53. We claim that  $\omega$  points horizontally to the right (at the instant shown in Fig. 9.97), with magnitude  $(R/r)\Omega$ . This can be seen in two ways.

The first way is to recognize that we essentially have the same scenario as in the “Rolling cone” setup of Problem 9.3 (imagine the sphere to be a ball of ice cream in a cone whose tip is located at the left end of the stick). The sphere's contact point with the ground is instantaneously at rest (the nonslipping condition), so  $\omega$  must pass through this point. But  $\omega$  must also pass through the left end of the stick, because that point is also at rest. Therefore,  $\omega$  must be horizontal. To find the magnitude, note that the center of the sphere moves with speed  $\Omega R$ . But since the center may also be considered to be instantaneously moving with frequency  $\omega$  in a circle of radius  $r$  around the horizontal axis, we have  $\omega r = \Omega R$ . Therefore,  $\omega = (R/r)\Omega$ .

The second way is to write  $\omega$  as  $\omega = -\Omega \hat{z} + \omega' \hat{x}_3$  (in the language of Fig. 9.30), where  $\omega'$  is the frequency of the spinning as viewed by someone rotating around the (negative)  $\hat{z}$  axis with frequency  $\Omega$ . The contact points form a circle of radius  $R$  on the ground. But they also form a circle of radius  $r \cos \theta$  on the sphere, where  $\theta$  is the angle between the stick and the ground (this circle is the circle of points where the

![Diagram of a rolling lollipop. A sphere of radius r and mass m is attached to a stick of length R. The stick makes an angle theta with the horizontal ground. The center of the sphere is at height r from the ground. A coordinate system is shown with the z-axis vertical, the x2-axis horizontal to the right, and the x3-axis along the stick. The angular velocity vector omega is shown as a horizontal arrow pointing to the right. The sphere is rotating clockwise when viewed from above, indicated by a curved arrow on its surface.](63e20b4fe9089deeb117fb9fa0b43d5c_img.jpg)

Diagram of a rolling lollipop. A sphere of radius r and mass m is attached to a stick of length R. The stick makes an angle theta with the horizontal ground. The center of the sphere is at height r from the ground. A coordinate system is shown with the z-axis vertical, the x2-axis horizontal to the right, and the x3-axis along the stick. The angular velocity vector omega is shown as a horizontal arrow pointing to the right. The sphere is rotating clockwise when viewed from above, indicated by a curved arrow on its surface.

Fig. 9.97

above-mentioned ice cream cone touches the sphere). The nonslipping condition then implies that  $\Omega R = \omega'(r \cos \theta)$ . Therefore,  $\omega' = \Omega R / (r \cos \theta)$ , and so

$$\boldsymbol{\omega} = -\Omega \hat{\mathbf{z}} + \omega' \hat{\mathbf{x}}_3 = -\Omega \hat{\mathbf{z}} + \left( \frac{\Omega R}{r \cos \theta} \right) (\cos \theta \hat{\mathbf{x}} + \sin \theta \hat{\mathbf{z}}) = (R/r) \Omega \hat{\mathbf{x}}, \quad (9.175)$$

where we have used  $\tan \theta = r/R$ .

Now let's calculate the normal force. Choose the pivot as the origin. The principal axes are then  $\hat{\mathbf{x}}_3$  along the stick, along with any two directions orthogonal to the stick. Choose  $\hat{\mathbf{x}}_2$  to be in the plane of the paper (see Fig. 9.97). Then the components of  $\boldsymbol{\omega}$  along the principal axes are

$$\omega_3 = (R/r) \Omega \cos \theta, \quad \text{and} \quad \omega_2 = -(R/r) \Omega \sin \theta. \quad (9.176)$$

The principal moments are

$$I_3 = (2/5)mr^2, \quad \text{and} \quad I_2 = (2/5)mr^2 + m(r^2 + R^2), \quad (9.177)$$

where we have used the parallel-axis theorem. The angular momentum is  $\mathbf{L} = I_3 \omega_3 \hat{\mathbf{x}}_3 + I_2 \omega_2 \hat{\mathbf{x}}_2$ , so its horizontal component has length  $L_{\perp} = I_3 \omega_3 \cos \theta - I_2 \omega_2 \sin \theta$ . Therefore, the magnitude of  $d\mathbf{L}/dt$  is

$$\begin{aligned} \left| \frac{d\mathbf{L}}{dt} \right| &= \Omega L_{\perp} = \Omega (I_3 \omega_3 \cos \theta - I_2 \omega_2 \sin \theta) \\ &= \Omega \left[ \left( \frac{2}{5}mr^2 \right) \left( \frac{R}{r} \Omega \cos \theta \right) \cos \theta \right. \\ &\quad \left. - \left( \frac{2}{5}mr^2 + m(r^2 + R^2) \right) \left( -\frac{R}{r} \Omega \sin \theta \right) \sin \theta \right] \\ &= \frac{\Omega^2 m R}{r} \left( \frac{2}{5}r^2 + (r^2 + R^2) \sin^2 \theta \right) \\ &= \frac{7}{5}mrR\Omega^2, \end{aligned} \quad (9.178)$$

where we have used  $\sin \theta = r/\sqrt{r^2 + R^2}$ . The direction of  $d\mathbf{L}/dt$  is out of the page.

The torque (relative to the pivot) is due to the gravitational force acting at the CM, along with the normal force  $N$  acting at the contact point. (Any horizontal friction that happens to exist at the contact point produces zero torque relative to the pivot.) Therefore,  $\boldsymbol{\tau}$  points out of the page with magnitude  $|\boldsymbol{\tau}| = (N - mg)R$ . Equating this with the  $|d\mathbf{L}/dt|$  in Eq. (9.178) gives

$$N = mg + \frac{7}{5}mr\Omega^2. \quad (9.179)$$

This has the interesting property of being independent of  $R$ , and hence also  $\theta$ . This independence arises because both  $|\boldsymbol{\tau}|$  and  $|d\mathbf{L}/dt|$  are proportional to  $R$ , a fact which is easier to see via the reasoning in the first remark below.

##### REMARKS:

1. There is actually a quicker way to calculate the  $d\mathbf{L}/dt$  in Eq. (9.178). At a given instant, the sphere is rotating around the horizontal  $x$  axis with frequency  $\omega = (R/r)\Omega$ . The moment of inertia around this axis is  $I_x = (7/5)mr^2$ , from the parallel-axis theorem. Therefore, the horizontal component of  $\mathbf{L}$  has magnitude  $L_x = I_x \omega = (7/5)mrR\Omega$ . Multiplying this by the frequency (namely  $\Omega$ ) at which  $\mathbf{L}$  swings around the  $z$  axis gives the result for  $|d\mathbf{L}/dt|$  in Eq. (9.178). There is also a vertical component of  $\mathbf{L}$  relative to the pivot, but this component doesn't change, so it doesn't come into  $d\mathbf{L}/dt$ . (The vertical component happens to equal  $-mR^2\Omega$ . This can be obtained by realizing that the sphere behaves like a point

- mass for the present purpose, or by using the inertia tensor relative to the pivot, or by calculating  $L_z = I_3\omega_3 \sin \theta + I_2\omega_2 \cos \theta$ .)
- The pivot must provide a downward force of  $N - mg = (7/5)mr\Omega^2$ , to make the net vertical force on the lollipop equal to zero. This result is slightly larger than the  $mr\Omega^2$  result for the “sliding” setup in Exercise 9.53.
- The sum of the horizontal forces at the pivot and the contact point must equal the required centripetal force of  $mR\Omega^2$ . But it is impossible to say how this force is divided up, without being given more information. ♣

### 9.23. Rolling coin

Choose the CM as the origin. The principal axes are then  $\hat{x}_2$  and  $\hat{x}_3$  (as shown in Fig. 9.98), along with  $\hat{x}_1$  pointing into the paper. Assume that the precessional motion is counterclockwise when viewed from above, as indicated in Fig. 9.54. Let’s look at things in the frame that has the center of the contact-point circle on the ground as its origin, and that rotates with angular velocity  $\Omega\hat{z}$ . In this frame, the CM remains fixed, and the coin rotates with frequency  $\omega'$  (in the language of Fig. 9.30) around the negative  $\hat{x}_3$  axis. The nonslipping condition then says that  $\omega'r = \Omega R$ , and so  $\omega' = \Omega R/r$ . Therefore, the total angular velocity of the coin with respect to the lab frame is

![Diagram of a rolling coin. A horizontal line represents the ground. A point on this line is the center of a circle of radius R. A coin of radius r is shown at a distance R from the origin. The coin's center of mass (CM) is at a distance R from the origin. The coin is tilted at an angle theta from the vertical. A vertical dashed line passes through the CM. The principal axes x2 and x3 are shown: x2 is horizontal and perpendicular to the coin's face, and x3 is along the coin's symmetry axis. The angle between the vertical dashed line and the x3 axis is theta. The angle between the horizontal line and the line connecting the origin to the CM is also theta.](70208e421470c421bb8727a78c8e5846_img.jpg)

Diagram of a rolling coin. A horizontal line represents the ground. A point on this line is the center of a circle of radius R. A coin of radius r is shown at a distance R from the origin. The coin's center of mass (CM) is at a distance R from the origin. The coin is tilted at an angle theta from the vertical. A vertical dashed line passes through the CM. The principal axes x2 and x3 are shown: x2 is horizontal and perpendicular to the coin's face, and x3 is along the coin's symmetry axis. The angle between the vertical dashed line and the x3 axis is theta. The angle between the horizontal line and the line connecting the origin to the CM is also theta.

Fig. 9.98

$$\boldsymbol{\omega} = \Omega\hat{z} - \omega'\hat{x}_3 = \Omega\hat{z} - (R/r)\Omega\hat{x}_3. \quad (9.180)$$

But  $\hat{z} = \sin \theta \hat{x}_2 + \cos \theta \hat{x}_3$ , so we can write  $\boldsymbol{\omega}$  in terms of the principal axes as

$$\boldsymbol{\omega} = \Omega \sin \theta \hat{x}_2 - \Omega \left( \frac{R}{r} - \cos \theta \right) \hat{x}_3. \quad (9.181)$$

The principal moments are

$$I_3 = (1/2)mr^2, \quad \text{and} \quad I_2 = (1/4)mr^2. \quad (9.182)$$

The angular momentum is  $\mathbf{L} = I_2\omega_2\hat{x}_2 + I_3\omega_3\hat{x}_3$ , so its horizontal component has length  $L_{\perp} = I_2\omega_2 \cos \theta - I_3\omega_3 \sin \theta$ , with leftward taken to be positive. Therefore, the magnitude of  $d\mathbf{L}/dt$  is

$$\begin{aligned} \left| \frac{d\mathbf{L}}{dt} \right| &= \Omega L_{\perp} \\ &= \Omega (I_2\omega_2 \cos \theta - I_3\omega_3 \sin \theta) \\ &= \Omega \left[ \left( \frac{1}{4}mr^2 \right) (\Omega \sin \theta) \cos \theta - \left( \frac{1}{2}mr^2 \right) \left( -\Omega (R/r - \cos \theta) \right) \sin \theta \right] \\ &= \frac{1}{4}mr\Omega^2 \sin \theta (2R - r \cos \theta), \end{aligned} \quad (9.183)$$

with a positive quantity corresponding to  $d\mathbf{L}/dt$  pointing out of the page (at the instant shown).

The torque (relative to the CM) comes from the force at the contact point. There are two components to this force. The vertical component is  $mg$ , and the horizontal component is  $m(R - r \cos \theta)\Omega^2$  leftward, because the CM moves in a circle of radius  $(R - r \cos \theta)$ . The torque therefore has magnitude

$$|\boldsymbol{\tau}| = mg(r \cos \theta) - m(R - r \cos \theta)\Omega^2(r \sin \theta), \quad (9.184)$$

with out of the page taken to be positive. Equating this  $|\boldsymbol{\tau}|$  with the  $|d\mathbf{L}/dt|$  in Eq. (9.183) gives

$$\Omega^2 = \frac{g}{\frac{3}{2}R \tan \theta - \frac{5}{4}r \sin \theta}. \quad (9.185)$$

The right-hand side must be positive if a solution for  $\Omega$  is to exist. Therefore, the condition for the desired motion to be possible is

$$R > \frac{5}{6}r \cos \theta. \quad (9.186)$$

#### REMARKS:

1. For  $\theta \rightarrow \pi/2$ , Eq. (9.185) gives  $\Omega \rightarrow 0$ , as it should. And for  $\theta \rightarrow 0$ , we obtain  $\Omega \rightarrow \infty$ , which also makes sense.
2. For  $r \cos \theta > R > (5/6)r \cos \theta$ , the CM of the coin lies to the *left* of the center of the contact-point circle (at the instant shown). The centripetal force,  $m(R - r \cos \theta)\Omega^2$ , is therefore negative (which means that it is directed radially outward, to the right), but the motion is still possible. As  $R$  gets close to  $(5/6)r \cos \theta$ , the frequency  $\Omega$  goes to infinity, which means that the radially outward force also goes to infinity. The coefficient of friction between the coin and the ground must therefore be correspondingly large.
3. We can consider a more general coin, whose density depends only on the distance from the center, and whose  $I_3$  equals  $\beta mr^2$ . For example, a uniform coin has  $\beta = 1/2$ , and a coin with all its mass on the edge has  $\beta = 1$ . By the perpendicular-axis theorem,  $I_1 = I_2 = (1/2)\beta mr^2$ , and you can show that the above methods yield

$$\Omega^2 = \frac{g}{(1 + \beta)R \tan \theta - (1 + \beta/2)r \sin \theta} \implies R > \left( \frac{1 + \beta/2}{1 + \beta} \right) r \cos \theta. \quad (9.187)$$

The larger  $\beta$  is, the smaller the lower bound on  $R$  is. But even if  $\beta \rightarrow \infty$  (imagine long radial spokes attached to the coin, and eliminate the ground except for the ring of contact points, so it doesn't get in the way),  $R$  still can't be any smaller than  $(r/2) \cos \theta$ . ♣

![Diagram of a wobbling coin. A coin is shown tilted at an angle theta from the vertical. Its center of mass (CM) is at the origin of a coordinate system with axes x2 (horizontal, pointing left) and x3 (vertical, pointing up). The coin's radius is R. The contact point with the ground is at a distance R cos theta from the CM along the x3 axis. The angle theta is also shown between the vertical axis and the coin's surface.](6703336f9b0fb575aa547e967b21b57a_img.jpg)

Diagram of a wobbling coin. A coin is shown tilted at an angle theta from the vertical. Its center of mass (CM) is at the origin of a coordinate system with axes x2 (horizontal, pointing left) and x3 (vertical, pointing up). The coin's radius is R. The contact point with the ground is at a distance R cos theta from the CM along the x3 axis. The angle theta is also shown between the vertical axis and the coin's surface.

Fig. 9.99

### 9.24. Wobbling coin

- (a) Choose the CM as the origin. The principal axes are then  $\hat{\mathbf{x}}_2$  and  $\hat{\mathbf{x}}_3$  (as shown in Fig. 9.99), along with  $\hat{\mathbf{x}}_1$  pointing into the paper. Assume that the precessional motion is counterclockwise when viewed from above, as indicated in Fig. 9.55. Consider the setup in the frame rotating with angular velocity  $\Omega \hat{\mathbf{z}}$ . In this frame, the location of the contact point remains fixed, and the coin rotates with frequency  $\omega'$  (in the language of Fig. 9.30) around the negative  $\hat{\mathbf{x}}_3$  axis. The radius of the circle of contact points on the table is  $R \cos \theta$ . Therefore, the nonslipping condition says that  $\omega' R = \Omega (R \cos \theta)$ , and so  $\omega' = \Omega \cos \theta$ . Hence, the total angular velocity of the coin with respect to the lab frame is

$$\boldsymbol{\omega} = \Omega \hat{\mathbf{z}} - \omega' \hat{\mathbf{x}}_3 = \Omega (\sin \theta \hat{\mathbf{x}}_2 + \cos \theta \hat{\mathbf{x}}_3) - (\Omega \cos \theta) \hat{\mathbf{x}}_3 = \Omega \sin \theta \hat{\mathbf{x}}_2. \quad (9.188)$$

In retrospect, it makes sense that  $\boldsymbol{\omega}$  must point in the  $\hat{\mathbf{x}}_2$  direction. Both the CM and the instantaneous contact point on the coin are at rest, so  $\boldsymbol{\omega}$  must lie along the line containing these two points, that is, along the  $\hat{\mathbf{x}}_2$  axis.

- (b) The principal moment around the  $\hat{\mathbf{x}}_2$  axis is  $I = mR^2/4$ . The angular momentum is  $\mathbf{L} = I\omega_2 \hat{\mathbf{x}}_2$ , so its horizontal component has length  $L_{\perp} = L \cos \theta = (I\omega_2) \cos \theta$ . Therefore,  $d\mathbf{L}/dt$  has magnitude

$$\left| \frac{d\mathbf{L}}{dt} \right| = \Omega L_{\perp} = \Omega \left( \frac{mR^2}{4} \right) (\Omega \sin \theta) \cos \theta, \quad (9.189)$$

and it points out of the page.

The torque (relative to the CM) is due to the normal force at the contact point. This normal force is essentially equal to  $mg$ , because the CM is assumed to be falling very slowly. Note that there is no sideways friction force at the contact point, because the CM is essentially motionless. The torque therefore has magnitude

$$|\tau| = mgR \cos \theta, \quad (9.190)$$

and it points out of the page. Equating this  $|\tau|$  with the  $|d\mathbf{L}/dt|$  in Eq. (9.189) gives

$$\Omega = 2\sqrt{\frac{g}{R \sin \theta}}. \quad (9.191)$$

##### REMARKS:

1.  $\Omega \rightarrow \infty$  as  $\theta \rightarrow 0$ . This is evident if you do the experiment; the contact point travels very quickly around the circle.
2.  $\Omega \rightarrow 2\sqrt{g/R}$  as  $\theta \rightarrow \pi/2$ , which isn't so obvious. In this case,  $\mathbf{L}$  points nearly vertically, and it traces out a tiny cone due to a tiny torque. In this  $\theta \rightarrow \pi/2$  limit,  $\Omega$  is also the frequency at which the plane of the coin spins around the vertical axis. If you spin a coin very fast about a vertical diameter, it initially undergoes a purely spinning motion with only one contact point. But then it gradually loses energy due to friction, until the spinning frequency slows down to  $2\sqrt{g/R}$ , at which point it begins to wobble (we're assuming that the coin is very thin, so that it can't balance on its edge). In the case where the coin is a US quarter (with  $R \approx 0.012$  m), this critical frequency of  $2\sqrt{g/R}$  turns out to be  $\Omega \approx 57$  rad/s, which corresponds to about 9 Hz.
3. The result in Eq. (9.191) is a special case of the result in Eq. (9.185) of Problem 9.23. The CM of the coin in Problem 9.23 is motionless if  $R = r \cos \theta$ . Plugging this into Eq. (9.185) gives  $\Omega^2 = 4g/(r \sin \theta)$ , which agrees with Eq. (9.191), because  $r$  was the coin's radius in Problem 9.23. ♣
- (c) Consider one revolution of the contact point around the  $z$  axis. Since the radius of the circle on the table is  $R \cos \theta$ , the contact point moves a distance  $2\pi R \cos \theta$  around the coin during this time. Hence, the new contact point on the coin is a distance  $2\pi R - 2\pi R \cos \theta$  away from the original contact point. The coin therefore appears to have rotated by a fraction  $(1 - \cos \theta)$  of a full turn during this time. The frequency with which you see it turn is therefore

$$(1 - \cos \theta)\Omega = 2(1 - \cos \theta)\sqrt{\frac{g}{R \sin \theta}}. \quad (9.192)$$

##### REMARKS:

1. If  $\theta \approx \pi/2$ , then the frequency of Abe's rotation is essentially equal to  $\Omega$ . This makes sense, because the top of Abe's head will be, say, always near the top of the coin, and this point will trace out a small circle around the  $z$  axis, with nearly the same frequency as the contact point.
2. As  $\theta \rightarrow 0$ , Abe appears to rotate with frequency  $\theta^{3/2}\sqrt{g/R}$  (using  $\sin \theta \approx \theta$  and  $\cos \theta \approx 1 - \theta^2/2$ ). Therefore, although the contact point moves infinitely quickly in this limit, we nevertheless see Abe rotating very slowly, as you can experimentally verify.
3. All of the results for frequencies in this problem must be some multiple of  $\sqrt{g/R}$ , by dimensional analysis. But whether the multiplication factor is zero, infinite, or something in between, is not at all obvious.
4. An incorrect answer for the frequency of Abe's turning (when viewed from above) is that it equals the vertical component of  $\omega$ , which is

$\omega_z = \omega \sin \theta = (\Omega \sin \theta) \sin \theta = 2(\sin \theta)^{3/2} \sqrt{g/R}$ . This does not equal the result in Eq. (9.192). (It agrees at  $\theta = \pi/2$  but is off by a factor of 2 for  $\theta \rightarrow 0$ .) This answer is incorrect because there is simply no reason why the vertical component of  $\boldsymbol{\omega}$  should equal the frequency of revolution of, say, Abe's nose, around the vertical axis. For example, at moments when  $\boldsymbol{\omega}$  passes through the nose, then the nose isn't moving at all, so it certainly cannot be described as moving around the vertical axis with frequency  $\omega_z = \omega \sin \theta$ . The result in Eq. (9.192) is a sort of average measure of the frequency of rotation. Even though any given point on the coin is not undergoing uniform circular motion, your eye sees the coin essentially rotating uniformly as a whole. ♣

### 9.25. Nutation cusps

- (a) Because both  $\dot{\phi}$  and  $\dot{\theta}$  are continuous functions of time, we must have  $\dot{\phi} = \dot{\theta} = 0$  at a kink. Otherwise, either  $d\theta/d\phi = \dot{\theta}/\dot{\phi}$  or  $d\phi/d\theta = \dot{\phi}/\dot{\theta}$  would be well defined at the kink. Let the kink occur at  $t = t_0$ . Then the second of Eqs. (9.92) gives  $\sin(\omega_n t_0) = 0$ . Therefore,  $\cos(\omega_n t_0) = \pm 1$ , and the first of Eqs. (9.92) gives

$$\Delta\Omega = \mp\Omega_s, \quad (9.193)$$

as desired. Note that if  $\cos(\omega_n t_0) = 1$ , then  $\Delta\Omega = -\Omega_s$ , so Eq. (9.91) says that the kink occurs at the smallest value of  $\theta$ , that is, at the highest point of the top's motion. And if  $\cos(\omega_n t_0) = -1$ , then  $\Delta\Omega = \Omega_s$ , so Eq. (9.91) again says that the kink occurs at the highest point of the top's motion. These results agree with the  $\Delta\Omega = \pm\Omega_s$  plots in Fig. 9.38.

- (b) To show that these kinks are cusps, we will show that the slope of the  $\theta$  vs.  $\phi$  plot is infinite on either side of the kink. That is, we will show that  $d\theta/d\phi = \dot{\theta}/\dot{\phi} = \pm\infty$ . Consider the case where  $\cos(\omega_n t_0) = 1$  and  $\Delta\Omega = -\Omega_s$  (the  $\cos(\omega_n t_0) = -1$  case proceeds similarly). With  $\Delta\Omega = -\Omega_s$ , Eq. (9.92) gives

$$\frac{\dot{\theta}}{\dot{\phi}} = \frac{\sin \theta_0 \sin \omega_n t}{1 - \cos \omega_n t}. \quad (9.194)$$

Let  $t = t_0 + \epsilon$ . Using  $\cos(\omega_n t_0) = 1$  and  $\sin(\omega_n t_0) = 0$ , and expanding Eq. (9.194) to lowest order in  $\epsilon$ , we find

$$\frac{\dot{\theta}}{\dot{\phi}} = \frac{\sin \theta_0 (\omega_n \epsilon)}{\omega_n^2 \epsilon^2 / 2} = \frac{2 \sin \theta_0}{\omega_n \epsilon}. \quad (9.195)$$

For infinitesimal  $\epsilon$ , this switches from  $-\infty$  to  $+\infty$  as  $\epsilon$  passes through zero. The point here is that although both  $\dot{\theta}$  and  $\dot{\phi}$  go to zero,  $\dot{\phi}$  goes quadratically, whereas  $\dot{\theta}$  goes only linearly.

![Figure 9.100: A 3D diagram showing the change in angular momentum vector L during a nutation cusp. The vertical axis is z, and the horizontal axis is x2. The original angular momentum vector 'old L' has magnitude I3*omega3 and makes an angle theta0 with the z-axis. A new angular momentum vector 'new L' is shown, which is the vector sum of 'old L' and a perpendicular component I*sin(theta0)*Delta*Omega. The new vector 'new L' makes an angle theta'0 with the z-axis. The angle between 'old L' and 'new L' is labeled theta'0 - theta0.](7908d404c28cf10551372ea26b4ec78a_img.jpg)

Figure 9.100: A 3D diagram showing the change in angular momentum vector L during a nutation cusp. The vertical axis is z, and the horizontal axis is x2. The original angular momentum vector 'old L' has magnitude I3\*omega3 and makes an angle theta0 with the z-axis. A new angular momentum vector 'new L' is shown, which is the vector sum of 'old L' and a perpendicular component I\*sin(theta0)\*Delta\*Omega. The new vector 'new L' makes an angle theta'0 with the z-axis. The angle between 'old L' and 'new L' is labeled theta'0 - theta0.

Fig. 9.100

### 9.26. Nutation circles

- (a) In the limit  $\omega_3 \gg \Omega_s$ , the original  $\mathbf{L}$  points essentially along the  $x_3$  direction, with magnitude  $I_3\omega_3$ . So it makes an angle of essentially  $\theta_0$  with the vertical  $z$  axis. Now consider the quick kick. If  $\dot{\phi}$  (which is the angular speed around the vertical  $z$  axis) suddenly increases by  $\Delta\Omega$ , then this corresponds to a sudden increase in angular speed around the  $x_2$  axis of  $\sin \theta_0 \Delta\Omega$  (see Fig. 9.100). The kick therefore produces an angular momentum component (relative to the pivot) of  $I \sin \theta_0 \Delta\Omega$  in the  $x_2$  direction. So from Fig. 9.100, the angle that the new  $\mathbf{L}$  makes with the  $z$  axis is (using  $\Delta\Omega \ll \omega_3$ )

$$\theta'_0 \approx \theta_0 - \frac{I \sin \theta_0 \Delta\Omega}{I_3 \omega_3} = \theta_0 - \frac{\sin \theta_0 \Delta\Omega}{\omega_n}, \quad (9.196)$$

- where we have used the definition of  $\omega_n$  from Eq. (9.86). We see that the effect of the kick is to make  $\mathbf{L}$  quickly change its  $\theta$  value (by only a small amount, because we are assuming  $\omega_3 \gg \Delta\Omega$ ). The  $\phi$  value doesn't immediately change, because immediately after the kick the  $x_3$  axis is still in exactly the same place, because it hasn't had time to move.
- (b) After the kick is finished,  $\mathbf{L}$  will trace out a cone around the  $z$  axis at approximately the same rate as before, namely  $\Omega_s$ . (None of the relevant quantities in  $\boldsymbol{\tau} = d\mathbf{L}/dt$  have changed much from the original circular-precession case, so the precession frequency is basically the same.) So the new  $\mathbf{L}$  has its  $(\phi, \theta)$  coordinates given by

$$(\phi(t), \theta(t))_{\mathbf{L}} = \left( \Omega_s t, \theta_0 - \frac{\sin \theta_0 \Delta\Omega}{\omega_n} \right). \quad (9.197)$$

We're assuming that  $\Omega_s$  is very small, so if you want, you can ignore the  $\Omega_s$  term and just consider  $\mathbf{L}$  to be fixed, at least on the time scale of the nutations (see the remark below). But this term will cancel anyway in producing the following equation. Looking at Eq. (9.91), we see that the coordinates of the CM relative to  $\mathbf{L}$  are

$$(\phi(t), \theta(t))_{\text{CM}-\mathbf{L}} = \left( \left( \frac{\Delta\Omega}{\omega_n} \right) \sin \omega_n t, \left( \frac{\Delta\Omega}{\omega_n} \sin \theta_0 \right) \cos \omega_n t \right). \quad (9.198)$$

The  $\sin \theta_0$  factor in  $\theta(t)$  is exactly what is needed for the CM to trace out a circle around  $\mathbf{L}$ , because a change in  $\phi$  corresponds to a CM spatial change of  $\ell \Delta\phi \sin \theta_0$ , whereas a change in  $\theta$  corresponds to a CM spatial change of  $\ell \Delta\theta$ .

Now let's see how this relates to a free top. For  $\omega_n \gg \Omega_s$ , the time scale on which  $\mathbf{L}$  changes due to the gravitational torque (namely  $1/\Omega_s$ ) is very long compared with the time scale of the nutation (namely  $1/\omega_n$ ). Therefore, since  $\mathbf{L}$  is essentially motionless on the time scale of  $1/\omega_n$ , the effects of gravity are negligible on this time scale. Hence, the system should behave like a free top. So let's verify that the results here do indeed agree with the results from Section 9.6.2.

Equation (9.55) in Section 9.6.2 says that the frequency of the precession of  $\hat{\mathbf{x}}_3$  around  $\mathbf{L}$  for a free top is  $L/I$ . But the frequency of the precession of  $\hat{\mathbf{x}}_3$  around  $\mathbf{L}$  in the present problem is  $\omega_n$ , so this had better be equal to  $L/I$ . And indeed,  $L$  is essentially equal to  $I_3\omega_3$ , so  $\omega_n \equiv I_3\omega_3/I = L/I$ . Therefore, for short enough time scales (short enough so that  $\mathbf{L}$  doesn't move much), a nutating top with  $\omega_3 \gg \Delta\Omega \gg \Omega_s$  looks very much like a free top.

**REMARK:** We need the  $\Delta\Omega \gg \Omega_s$  condition so that the nutation motion looks roughly like circles (that is, like the top plot in Fig. 9.38, and not the others). This requirement can be seen by the following reasoning. The time for one period of the nutation motion is  $2\pi/\omega_n$ . From Eq. (9.91),  $\phi(t)$  increases by  $\Delta\phi = 2\pi\Omega_s/\omega_n$  during this time. And also from Eq. (9.91), the diameter  $d$  of the "circle" along the  $\phi$  axis is roughly  $d = 2\Delta\Omega/\omega_n$ . The motion looks approximately like a circle if  $d \gg \Delta\phi$ , that is, if  $\Delta\Omega \gg \Omega_s$ . ♣

### 9.27. Rolling without slipping

Yes, there are indeed other ways. It isn't necessary for the contact points to form a vertical great circle. They can form a smaller tilted circle, as shown in Fig. 9.101. In this case the angular velocity vector points up to the left. There is indeed no slipping here, and the ball rolls straight. You can convince yourself of this in the following way. Imagine the ball hovering and spinning in place with its center at rest. At all times, the point at the bottom of the ball is moving directly out of the page; the collection of these points is the tilted circle in Fig. 9.101. Let the speed of the instantaneous bottom point be  $v$ , and now imagine taking a horizontal sheet of paper and sliding it out of the page with constant speed  $v$ , just beneath the ball, barely touching it. Since this is the

![Diagram of a ball rolling without slipping. The ball is shown as a circle with radius R. A vector labeled omega points from the center of the ball towards the upper left. A dashed circle is drawn inside the ball, tilted relative to the vertical. An arrow on the dashed circle indicates a counter-clockwise direction of motion. The angle theta is shown between the vertical dashed line and the radius to the point of contact on the dashed circle.](7e84e3f9a68cc985d8f7f65644bf512e_img.jpg)

Diagram of a ball rolling without slipping. The ball is shown as a circle with radius R. A vector labeled omega points from the center of the ball towards the upper left. A dashed circle is drawn inside the ball, tilted relative to the vertical. An arrow on the dashed circle indicates a counter-clockwise direction of motion. The angle theta is shown between the vertical dashed line and the radius to the point of contact on the dashed circle.

Fig. 9.101

![Diagram of a sphere of radius R rolling on a flat surface. The angular velocity vector ω is shown originating from the center of the sphere and pointing upwards and to the right. The angle θ is measured between the horizontal dashed line and the vector ω. The contact point with the surface is at the bottom of the sphere.](103a19c6c6bae202841f7b5ddc351cb1_img.jpg)

Diagram of a sphere of radius R rolling on a flat surface. The angular velocity vector ω is shown originating from the center of the sphere and pointing upwards and to the right. The angle θ is measured between the horizontal dashed line and the vector ω. The contact point with the surface is at the bottom of the sphere.

Fig. 9.102

same speed as the bottom point on the ball (which is the contact point, because it's at the bottom), there is no slipping between the ball and the paper. Finally, if we go to the reference frame of the paper, we have the desired motion of a ball rolling without slipping on a flat surface.

If  $\theta$  is the angle that  $\omega$  makes with the horizontal, then the radius of the contact circle is  $R \cos \theta$ . The linear speed of the ball is therefore  $\omega(R \cos \theta)$ . If you want, you can think of this as  $(\omega \cos \theta)R$ . That is, only the horizontal component of  $\omega$  leads to translational motion of the ball. The vertical component simply yields a spinning motion around the vertical diameter. If  $\theta$  approaches  $90^\circ$ , then the contact circle is very small (see Fig. 9.102), so the speed of the ball is very small (for a given  $\omega$ ).

In the real world, the contact area between the ball and the surface isn't an idealized single point, so if the contact circle isn't a vertical great circle, there is inevitably some slipping at the points near the bottom of the ball. The smaller the contact circle, the more the slipping, because the slipping arises from the twisting motion around the vertical diameter, which comes from the vertical component of  $\omega$ . If you take an actual ball and roll it with a tilted  $\omega$ , you will find that the rolling motion is noisier the more that  $\omega$  is tilted. What you hear is the slipping due to the extended contact region. But in an ideal world (or perhaps in a bowling alley, which is a reasonable approximation thereof), a tilted  $\omega$  wouldn't be any noisier.

### 9.28. Rolling straight?

Intuitively, it is fairly clear that the sphere cannot change direction, but it is a little tricky to prove. Qualitatively, we can reason as follows. Assume that there is a nonzero friction force at the contact point. (The normal force is irrelevant here, because it doesn't provide a torque about the center, because the contact point is always directly below the center. This is what is special about a sphere.) Then the sphere accelerates in the direction of this force. However, you can show with the right-hand rule that this force produces a torque that causes the angular momentum to change in a way that corresponds to the sphere accelerating in the direction *opposite* to the friction force (assuming that the sphere is rolling without slipping). There is thus a contradiction, unless the friction force is equal to zero.

Let's now be rigorous. Let the angular velocity of the sphere be  $\omega$ , which may point diagonally if the contact points don't form a vertical great circle on the sphere. The nonslipping condition says that the sphere's CM velocity equals

$$\mathbf{v} = \omega \times (R\hat{\mathbf{z}}). \quad (9.199)$$

The sphere's angular momentum is

$$\mathbf{L} = I\omega. \quad (9.200)$$

The friction force (if it exists) from the ground at the contact point changes both the momentum and the angular momentum.  $\mathbf{F} = d\mathbf{p}/dt$  gives

$$\mathbf{F} = m \frac{d\mathbf{v}}{dt}. \quad (9.201)$$

And  $\boldsymbol{\tau} = d\mathbf{L}/dt$  (relative to the center) gives

$$(-R\hat{\mathbf{z}}) \times \mathbf{F} = \frac{d\mathbf{L}}{dt}, \quad (9.202)$$

because the force is applied at position  $-R\hat{\mathbf{z}}$  relative to the center. We will now show that the preceding four equations imply that  $\dot{\omega} = \mathbf{0}$ . From Eq. (9.199), this then implies that  $\dot{\mathbf{v}} = \mathbf{0}$ , as desired.

Equations (9.199) and (9.201) give  $\mathbf{F} = m\dot{\mathbf{v}} = m\dot{\omega} \times (R\hat{\mathbf{z}})$ . Plugging this  $\mathbf{F}$ , along with the  $\mathbf{L}$  from Eq. (9.200), into Eq. (9.202) then gives

$$(-R\hat{\mathbf{z}}) \times (m\dot{\omega} \times (R\hat{\mathbf{z}})) = I\dot{\omega}. \quad (9.203)$$

The vector  $\dot{\boldsymbol{\omega}}$  must lie in the horizontal plane, because it equals the cross product of two vectors, one of which is the vertical  $\hat{\mathbf{z}}$ . This implies that (as you can verify)  $\hat{\mathbf{z}} \times (\dot{\boldsymbol{\omega}} \times \hat{\mathbf{z}}) = \dot{\boldsymbol{\omega}}$ . Therefore, Eq. (9.203) gives

$$-mR^2 \dot{\boldsymbol{\omega}} = \frac{2}{5} mR^2 \dot{\boldsymbol{\omega}}, \quad (9.204)$$

and so  $\dot{\boldsymbol{\omega}} = \mathbf{0}$ , as we wanted to show.

### 9.29. Ball on paper

Our strategy will be to produce, and then equate, two different expressions for the total change in the angular momentum of the ball, relative to its center. The first comes from the effects of the friction force on the ball. The second comes from looking at the general form of the initial and final motion.

To produce our first expression for  $\Delta \mathbf{L}$ , note that the normal force provides no torque, so we can ignore it. The friction force,  $\mathbf{F}$ , from the paper changes both  $\mathbf{p}$  and  $\mathbf{L}$  according to

$$\begin{aligned} \Delta \mathbf{p} &= \int \mathbf{F} dt, \\ \Delta \mathbf{L} &= \int \boldsymbol{\tau} dt = \int (-R\hat{\mathbf{z}}) \times \mathbf{F} dt = (-R\hat{\mathbf{z}}) \times \int \mathbf{F} dt. \end{aligned} \quad (9.205)$$

Both of these integrals run over the entire slipping time, which may include time on the table after the ball leaves the paper. In the second line above, we have used the fact that the friction force always acts at the same location, namely  $(-R\hat{\mathbf{z}})$ , relative to the center of the ball. The two above equations yield

$$\Delta \mathbf{L} = (-R\hat{\mathbf{z}}) \times \Delta \mathbf{p}. \quad (9.206)$$

To produce our second equation for  $\Delta \mathbf{L}$ , let's examine how  $\mathbf{L}_\perp$  (the horizontal component of  $\mathbf{L}$ )<sup>32</sup> is related to  $\mathbf{p}$  when the ball is rolling without slipping, which is the case at both the start and finish. When the ball is not slipping, we have the situation shown in Fig. 9.103 (assuming that the ball is rolling to the right). The magnitudes of  $\mathbf{p}$  and  $\mathbf{L}_\perp$  are given by

$$\begin{aligned} p &= mv, \\ L_\perp &= I\omega_\perp = \frac{2}{5} mR^2 \omega_\perp = \frac{2}{5} Rm(R\omega_\perp) = \frac{2}{5} Rmv = \frac{2}{5} Rp, \end{aligned} \quad (9.207)$$

where we have used the nonslipping condition,  $v = R\omega_\perp$ . (The actual  $I = (2/5)mR^2$  value for a solid sphere won't be important for the final result.) We can now combine the directions of  $\mathbf{L}_\perp$  and  $\mathbf{p}$  in Fig. 9.103 with the above  $L_\perp = (2/5)Rp$  scalar relation to write

$$\mathbf{L}_\perp = \frac{2}{5} R\hat{\mathbf{z}} \times \mathbf{p}, \quad (9.208)$$

where  $\hat{\mathbf{z}}$  points out of the page. Since this relation is true at both the start and the finish, it must also be true for the differences in  $\mathbf{L}_\perp$  and  $\mathbf{p}$ . That is,

$$\Delta \mathbf{L}_\perp = \frac{2}{5} R\hat{\mathbf{z}} \times \Delta \mathbf{p}. \quad (9.209)$$

![Diagram showing a top view of a ball rolling to the right. A circle represents the ball. An arrow labeled 'p' points to the right from the center of the ball. An arrow labeled 'L_perp' points upwards from the center of the ball. The text '(top view)' is to the right of the ball.](e0e137b8e31bde924e982062ed16051e_img.jpg)

Diagram showing a top view of a ball rolling to the right. A circle represents the ball. An arrow labeled 'p' points to the right from the center of the ball. An arrow labeled 'L\_perp' points upwards from the center of the ball. The text '(top view)' is to the right of the ball.

Fig. 9.103

<sup>32</sup> The vertical component of  $\mathbf{L}$  (which is nonzero only if  $\boldsymbol{\omega}$  has a vertical component, which is the case if the contact points don't form a vertical great circle on the ball) is constant, because the torque from friction provides only a horizontal torque. We may therefore ignore it, because we are concerned only with  $\Delta \mathbf{L}$ .

But  $\Delta \mathbf{L}_{\perp} = \Delta \mathbf{L}$  because the vertical component of  $\mathbf{L}$  doesn't change, so Eqs. (9.206) and (9.209) give

$$(-R\hat{\mathbf{z}}) \times \Delta \mathbf{p} = \frac{2}{5}R\hat{\mathbf{z}} \times \Delta \mathbf{p} \implies \mathbf{0} = \hat{\mathbf{z}} \times \Delta \mathbf{p}. \quad (9.210)$$

There are three ways this cross product can be zero:

- $\Delta \mathbf{p}$  is parallel to  $\hat{\mathbf{z}}$ . But it isn't, because  $\Delta \mathbf{p}$  lies in the horizontal plane.
- $\hat{\mathbf{z}} = \mathbf{0}$ . Not true.
- $\Delta \mathbf{p} = \mathbf{0}$ . This is the only possibility, so it must be true. Therefore,  $\Delta \mathbf{v} = \mathbf{0}$ , as we wanted to show.

Note that the line of the final motion may very well be shifted sideways from the line of the initial motion. But what we've shown is that the final line is parallel to the initial line, and the speed is the same.

##### REMARKS:

1. As stated in the problem, it's fine if you move the paper in a jerky motion, so that the ball slips around on it. We assumed nothing about the nature of the friction force in the above reasoning. And we used the nonslipping condition only at the initial and final times. The intermediate motion is arbitrary.
2. As a special case, if you start a ball at rest on a piece of paper, then no matter how you choose to (horizontally) slide the paper out from underneath the ball, the ball will be at rest in the end. The final position will most likely be different from the initial position, but the ball will be at rest wherever it ends up.
3. You are encouraged to experimentally verify that these crazy claims are true. Make sure that the paper doesn't wrinkle, because a wrinkle would allow a force to be applied at a point other than the contact point. And balls that don't squish are much better, of course, because the contact region better resembles a single point. ♣

### 9.30. Ball on a turntable

Let the angular velocity of the turntable be  $\Omega\hat{\mathbf{z}}$ , and let the angular velocity of the ball (with respect to the lab frame) be  $\boldsymbol{\omega}$ , which may point diagonally if the contact points don't form a vertical great circle on the ball. If the ball is at position  $\mathbf{r}$  (with respect to the lab frame), then its CM velocity (with respect to the lab frame) may be broken up into the velocity of the turntable (at position  $\mathbf{r}$ ) plus the ball's velocity with respect to the turntable. The nonslipping condition says that the latter is  $\boldsymbol{\omega} \times (a\hat{\mathbf{z}})$ , where  $a$  is the radius of the ball.<sup>33</sup> The ball's velocity with respect to the lab frame is thus

$$\mathbf{v} = (\Omega\hat{\mathbf{z}}) \times \mathbf{r} + \boldsymbol{\omega} \times (a\hat{\mathbf{z}}). \quad (9.211)$$

The important point to realize in this problem is that the friction force from the turntable is responsible for changing both the ball's linear momentum and its angular momentum. In particular,  $\mathbf{F} = d\mathbf{p}/dt$  gives

$$\mathbf{F} = m \frac{d\mathbf{v}}{dt}. \quad (9.212)$$

And the angular momentum of the ball is  $\mathbf{L} = I\boldsymbol{\omega}$ , so  $\boldsymbol{\tau} = d\mathbf{L}/dt$  (relative to the center of the ball) gives

$$(-a\hat{\mathbf{z}}) \times \mathbf{F} = I \frac{d\boldsymbol{\omega}}{dt}, \quad (9.213)$$

because the force is applied at position  $-a\hat{\mathbf{z}}$  relative to the center.

<sup>33</sup> The velocity with respect to the turntable is actually  $\boldsymbol{\omega}_t \times (a\hat{\mathbf{z}})$ , where  $\boldsymbol{\omega}_t$  is the angular velocity in the turntable frame. But  $\boldsymbol{\omega}_t$  differs from  $\boldsymbol{\omega}$  simply by the angular velocity of the turntable, which is  $\Omega\hat{\mathbf{z}}$ . This implies that  $\boldsymbol{\omega}_t \times (a\hat{\mathbf{z}}) = \boldsymbol{\omega} \times (a\hat{\mathbf{z}})$ .

We will now use the previous three equations to demonstrate that the ball undergoes circular motion. Our goal will be to produce an equation of the form,

$$\frac{d\mathbf{v}}{dt} = \Omega' \hat{\mathbf{z}} \times \mathbf{v}, \quad (9.214)$$

because this describes circular motion with frequency  $\Omega'$  (to be determined).<sup>34</sup> We will eliminate  $\mathbf{F}$  first, and then  $\boldsymbol{\omega}$ . Plugging the expression for  $\mathbf{F}$  from Eq. (9.212) into Eq. (9.213) gives

$$(-a\hat{\mathbf{z}}) \times \left( m \frac{d\mathbf{v}}{dt} \right) = I \frac{d\boldsymbol{\omega}}{dt} \implies \frac{d\boldsymbol{\omega}}{dt} = -\left( \frac{am}{I} \right) \hat{\mathbf{z}} \times \frac{d\mathbf{v}}{dt}. \quad (9.215)$$

Taking the derivative of Eq. (9.211) gives

$$\begin{aligned} \frac{d\mathbf{v}}{dt} &= \Omega \hat{\mathbf{z}} \times \frac{d\mathbf{r}}{dt} + \frac{d\boldsymbol{\omega}}{dt} \times (a\hat{\mathbf{z}}) \\ &= \Omega \hat{\mathbf{z}} \times \mathbf{v} - \left( \frac{am}{I} \right) \hat{\mathbf{z}} \times \frac{d\mathbf{v}}{dt} \times (a\hat{\mathbf{z}}). \end{aligned} \quad (9.216)$$

Since we know that the vector  $d\mathbf{v}/dt$  lies in the horizontal plane, it is easy to work out the cross product in the second term here (or just use the identity  $(\mathbf{A} \times \mathbf{B}) \times \mathbf{C} = (\mathbf{A} \cdot \mathbf{C})\mathbf{B} - (\mathbf{B} \cdot \mathbf{C})\mathbf{A}$ ) to obtain

$$\frac{d\mathbf{v}}{dt} = \Omega \hat{\mathbf{z}} \times \mathbf{v} - \left( \frac{ma^2}{I} \right) \frac{d\mathbf{v}}{dt} \implies \frac{d\mathbf{v}}{dt} = \left( \frac{\Omega}{1 + (ma^2/I)} \right) \hat{\mathbf{z}} \times \mathbf{v}. \quad (9.217)$$

For a uniform sphere,  $I = (2/5)ma^2$ , so we obtain

$$\frac{d\mathbf{v}}{dt} = \left( \frac{2}{7}\Omega \right) \hat{\mathbf{z}} \times \mathbf{v}. \quad (9.218)$$

Therefore, in view of Eq. (9.214), we see that the ball undergoes circular motion, with a frequency equal to  $2/7$  times the frequency of the turntable. Note that this result for the frequency doesn't depend on initial conditions. For an extension to this problem, see Weltner (1987) and references therein.

##### REMARKS:

1. Integrating Eq. (9.218) from the initial time to some later time gives

$$\mathbf{v} - \mathbf{v}_0 = \left( \frac{2}{7}\Omega \right) \hat{\mathbf{z}} \times (\mathbf{r} - \mathbf{r}_0). \quad (9.219)$$

This may be written (as you can verify) in the more suggestive (if not more frightening) form,

$$\mathbf{v} = \left( \frac{2}{7}\Omega \right) \hat{\mathbf{z}} \times \left( \mathbf{r} - \left( \mathbf{r}_0 + \frac{7}{2\Omega} (\hat{\mathbf{z}} \times \mathbf{v}_0) \right) \right). \quad (9.220)$$

This equation describes circular motion, with the center located at the point,

$$\mathbf{r}_c = \mathbf{r}_0 + \frac{7}{2\Omega} (\hat{\mathbf{z}} \times \mathbf{v}_0), \quad (9.221)$$

<sup>34</sup> Equation (9.214) describes circular motion because it implies that  $\mathbf{v}$  has constant magnitude (since the change in  $\mathbf{v}$  is perpendicular to  $\mathbf{v}$ ), and so the direction of  $\mathbf{v}$  changes at the constant angular rate  $\Omega'$ . The only curve with these properties is a circle. If you want to be more mathematical, you can integrate Eq. (9.214) to obtain  $\mathbf{v} = \Omega' \hat{\mathbf{z}} \times \mathbf{r} + \mathbf{C}$ , which can be written as  $d\mathbf{r}/dt = \Omega' \hat{\mathbf{z}} \times (\mathbf{r} - \mathbf{r}_c)$ , which implies that  $d(\mathbf{r} - \mathbf{r}_c)/dt = \Omega' \hat{\mathbf{z}} \times (\mathbf{r} - \mathbf{r}_c)$ , which means that the length of  $\mathbf{r} - \mathbf{r}_c$  doesn't change (because its change is perpendicular to itself). And since the changes are also constrained to be perpendicular to  $\hat{\mathbf{z}}$ , we must have a horizontal circle.

and with radius,

$$R = |\mathbf{r}_0 - \mathbf{r}_c| = \frac{7}{2\Omega} |\hat{\mathbf{z}} \times \mathbf{v}_0| = \frac{7v_0}{2\Omega}. \quad (9.222)$$

2. There are a few special cases to consider:

- If  $v_0 = 0$  (that is, if the spinning motion of the ball exactly cancels the rotational motion of the turntable, so that the CM of the ball is at rest in the lab frame), then  $R = 0$  and the ball remains in the same place, as it should.
- If the ball is initially not spinning, and just moving along with the turntable, then  $v_0 = \Omega r_0$ . The radius of the circle is therefore  $R = (7/2)r_0$ , and its center is located at, from Eq. (9.221),

$$\mathbf{r}_c = \mathbf{r}_0 + \frac{7}{2\Omega} (-\Omega \mathbf{r}_0) = -\frac{5\mathbf{r}_0}{2}. \quad (9.223)$$

The point on the circle diametrically opposite to the initial point is therefore a distance  $r_c + R = (5/2)r_0 + (7/2)r_0 = 6r_0$  from the center of the turntable.

- If we want the center of the circle to be the center of the turntable, then Eq. (9.221) says that we need  $(7/2\Omega)\hat{\mathbf{z}} \times \mathbf{v}_0 = -\mathbf{r}_0$ . This implies that  $\mathbf{v}_0$  has magnitude  $v_0 = (2/7)\Omega r_0$  and points tangentially in the same direction as the turntable moves. That is, the ball moves at  $2/7$  times the velocity of the point on the turntable right beneath it.
- 3. The fact that the frequency  $(2/7)\Omega$  is a rational multiple of  $\Omega$  means that the ball will eventually return to the same point on the turntable. In the lab frame, the ball traces out two circles in the time it takes the turntable to undergo seven revolutions. From the point of view of someone on the turntable, the ball “spirals” around five times before returning to the original position.
- 4. If we look at a ball with moment of inertia  $I = \beta ma^2$  (so a uniform sphere has  $\beta = 2/5$ ), then Eq. (9.217) shows that the “ $2/7$ ” in Eq. (9.218) gets replaced by “ $\beta/(1 + \beta)$ .” If a ball has most of its mass concentrated at its center (so that  $\beta \rightarrow 0$ ), then the frequency of the circular motion goes to 0, and the radius goes to  $\infty$  (as long as  $v_0 \neq 0$ ). ♣