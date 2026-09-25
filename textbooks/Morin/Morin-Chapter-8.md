# Chapter 8 Angular momentum, Part I(Constant $\hat{\mathbf{L}}$ )

The angular momentum of a point mass, relative to a given origin, is defined by

$$\mathbf{L} = \mathbf{r} \times \mathbf{p}. \quad (8.1)$$

For a collection of particles, the total  $\mathbf{L}$  is simply the sum of the  $\mathbf{L}$ 's of all the particles. The vector  $\mathbf{r} \times \mathbf{p}$  is a useful thing to study because it has many nice properties. One of these is the conservation law presented in Theorem 7.1, which allowed us to introduce the “effective potential” in Section 7.2. And later in this chapter we will introduce the concept of *torque*,  $\boldsymbol{\tau}$ , which appears in the bread-and-butter statement,  $\boldsymbol{\tau} = d\mathbf{L}/dt$  (analogous to Newton's  $\mathbf{F} = d\mathbf{p}/dt$  law).

There are two basic types of angular momentum problems in the world. Since the solution to any rotational problem invariably comes down to using  $\boldsymbol{\tau} = d\mathbf{L}/dt$ , as we will see, we must determine how  $\mathbf{L}$  changes in time. And since  $\mathbf{L}$  is a vector, it can change because (1) its length changes, or (2) its direction changes (or through some combination of these effects). In other words, if we write  $\mathbf{L} = L\hat{\mathbf{L}}$ , where  $\hat{\mathbf{L}}$  is the unit vector in the  $\mathbf{L}$  direction, then  $\mathbf{L}$  can change because  $L$  changes, or because  $\hat{\mathbf{L}}$  changes, or both.

The first of these cases, that of constant  $\hat{\mathbf{L}}$ , is the easily understood one. Consider a spinning record, with the center chosen as the origin. The vector  $\mathbf{L} = \sum \mathbf{r} \times \mathbf{p}$  is perpendicular to the record, because every term in the sum has this property. If we give the record a tangential force in the proper direction, then it will speed up (in a precise way which we will soon determine). There is nothing mysterious going on here. If we push on the record, it goes faster.  $\mathbf{L}$  points in the same direction as before, but now simply with a larger magnitude. In fact, in this type of problem, we can completely forget that  $\mathbf{L}$  is a vector. We can deal just with its magnitude  $L$ , and everything will be fine. This first case is the subject of the present chapter.

The second case, however, where  $\mathbf{L}$  changes direction, can get rather confusing. This is the subject of the following chapter, where we will talk about twirling tops and other kinds of spinning objects that have a tendency to make one's head spin too. In these situations, the entire point is that  $\mathbf{L}$  is actually a

vector. And unlike in the constant- $\hat{\mathbf{L}}$  case, we really have to visualize things in three dimensions to see what's going on.<sup>1</sup>

The angular momentum of a point mass is given by the simple expression in Eq. (8.1). But in order to deal with setups in the real world, which invariably consist of many particles, we must learn how to calculate the angular momentum of an extended object. This is the task of the Section 8.1. In this chapter, we'll deal only with rotations around the  $z$  axis, or an axis parallel to the  $z$  axis. We'll save the general 3-D motion for Chapter 9.

![Diagram of a flat rigid body (pancake object) in the x-y plane. The body is shaded gray and has a center of mass (CM) marked with a dot. A velocity vector V points downwards and to the right from the CM. An angular velocity vector ω is shown as a curved arrow indicating rotation. The x and y axes are shown as solid lines with arrows at their ends.](944b92fdd50061cbe98b42a006cbb763_img.jpg)

Diagram of a flat rigid body (pancake object) in the x-y plane. The body is shaded gray and has a center of mass (CM) marked with a dot. A velocity vector V points downwards and to the right from the CM. An angular velocity vector ω is shown as a curved arrow indicating rotation. The x and y axes are shown as solid lines with arrows at their ends.

Fig. 8.1

### 8.1 Pancake object in $x$ - $y$ plane

Consider a flat rigid body undergoing arbitrary motion (both translating and spinning) in the  $x$ - $y$  plane; see Fig. 8.1. What is the angular momentum of this body, relative to the origin of the coordinate system?<sup>2</sup> If we imagine the body to consist of particles of mass  $m_i$ , then the angular momentum of the entire body is the sum of the angular momenta of each  $m_i$ , which is  $\mathbf{L}_i = \mathbf{r}_i \times \mathbf{p}_i$ . So the total angular momentum is

$$\mathbf{L} = \sum_i \mathbf{r}_i \times \mathbf{p}_i. \quad (8.2)$$

For a continuous distribution of mass, we would have an integral instead of a sum.  $\mathbf{L}$  depends on the locations and momenta of the masses. The momenta in turn depend on how fast the body is translating and spinning. Our goal here is to find the dependence of  $\mathbf{L}$  on the distribution and motion of the constituent masses. The result will involve the geometry of the body in a specific way, as we will show.

In this section, we will deal only with pancake-like objects that move in the  $x$ - $y$  plane. We will calculate  $\mathbf{L}$  relative to the origin, and we will also derive an expression for the kinetic energy. We will deal with non-pancake objects in Section 8.2. Note that since both the  $\mathbf{r}$  and  $\mathbf{p}$  of all the masses in our pancake-like objects always lie in the  $x$ - $y$  plane, the vector  $\mathbf{L} = \sum \mathbf{r} \times \mathbf{p}$  always points in the  $\hat{\mathbf{z}}$  direction. As mentioned above, this fact is what makes these pancake cases easy to deal with.  $\mathbf{L}$  changes only because its length changes, not its direction. So when we eventually get to the  $\boldsymbol{\tau} = d\mathbf{L}/dt$  equation, it will take on a simple form. Let's first look at a special case, and then we'll look at general motion in the  $x$ - $y$  plane.

<sup>1</sup> The difference between these two cases is essentially the same as the difference between the two basic  $\mathbf{F} = d\mathbf{p}/dt$  cases. The vector  $\mathbf{p}$  can change because its magnitude changes, in which case we have  $F = ma$  (assuming that  $m$  is constant). Or,  $\mathbf{p}$  can change because its direction changes, in which case we have the centripetal-acceleration statement,  $F = mv^2/r$ . (Or there could be a combination of these effects.) The former case seems a bit more intuitive than the latter.

<sup>2</sup> Remember,  $\mathbf{L}$  is defined relative to a chosen origin, because it has the vector  $\mathbf{r}$  in it. So it makes no sense to ask what  $\mathbf{L}$  is, without specifying what origin we've chosen.

#### 8.1.1 Rotation about the $z$ axis

The pancake in Fig. 8.2 is pivoted at the origin and rotates with angular speed  $\omega$  around the  $z$  axis, in the counterclockwise direction (as viewed from above). Consider a little piece of the body, with mass  $dm$  and position  $(x, y)$ . This little piece travels in a circle around the origin with speed  $v = \omega r$ , where  $r = \sqrt{x^2 + y^2}$ . Therefore, the angular momentum of this piece (relative to the origin) equals  $\mathbf{L} = \mathbf{r} \times \mathbf{p} = r(v \, dm)\hat{\mathbf{z}} = dm \, r^2 \omega \hat{\mathbf{z}}$ . The  $\hat{\mathbf{z}}$  direction arises from the cross product of the (orthogonal) vectors  $\mathbf{r}$  and  $\mathbf{p}$ . The angular momentum of the entire body is therefore

![Figure 8.2: A diagram showing a shaded, irregularly shaped object (the 'pancake') in the x-y plane. The object is centered at the origin (0,0) of a Cartesian coordinate system. A curved arrow labeled with the Greek letter omega (ω) indicates a counterclockwise rotation around the z-axis, which is perpendicular to the x-y plane.](c4f8533d1335080882da67e741f5c102_img.jpg)

Figure 8.2: A diagram showing a shaded, irregularly shaped object (the 'pancake') in the x-y plane. The object is centered at the origin (0,0) of a Cartesian coordinate system. A curved arrow labeled with the Greek letter omega (ω) indicates a counterclockwise rotation around the z-axis, which is perpendicular to the x-y plane.

Fig. 8.2

$$\mathbf{L} = \int r^2 \omega \hat{\mathbf{z}} \, dm = \int (x^2 + y^2) \omega \hat{\mathbf{z}} \, dm, \quad (8.3)$$

where the integration runs over the area of the body. If the density of the object is constant, as is usually the case, then we have  $dm = \rho \, dx \, dy$ . If we define the *moment of inertia* around the  $z$  axis to be

$$I_z \equiv \int r^2 \, dm = \int (x^2 + y^2) \, dm, \quad (8.4)$$

then the  $z$  component of  $\mathbf{L}$  is

$$L_z = I_z \omega, \quad (8.5)$$

and both  $L_x$  and  $L_y$  are zero. In the case where the rigid body is made up of a collection of point masses  $m_i$  in the  $x$ - $y$  plane, the moment of inertia in Eq. (8.4) takes the discretized form,

$$I_z \equiv \sum_i m_i r_i^2. \quad (8.6)$$

Given any rigid body in the  $x$ - $y$  plane, we can calculate  $I_z$ . And given  $\omega$ , we can then multiply it by  $I_z$  to find  $L_z$ . In Section 8.3.1, we'll get some practice calculating various moments of inertia.

What is the kinetic energy of our object? We need to add up the energies of all the little pieces. A little piece has energy  $dm \, v^2/2 = dm(r\omega)^2/2$ . So the total kinetic energy is

$$T = \int \frac{r^2 \omega^2}{2} \, dm. \quad (8.7)$$

With our definition of  $I_z$  in Eq. (8.4), this becomes

$$T = \frac{I_z \omega^2}{2}. \quad (8.8)$$

This is easy to remember, because it looks a lot like the kinetic energy of a point mass,  $mv^2/2$ .

![Figure 8.3: A diagram showing a rigid body (a gray irregular shape) in the x-y plane. The center of mass (CM) is marked with a dot. A velocity vector V points downwards and to the right from the CM. A curved arrow labeled ω indicates rotation counter-clockwise around the CM. The x and y axes are shown as coordinate axes.](67c35f5029912e1073657fcfe8482b83_img.jpg)

Figure 8.3: A diagram showing a rigid body (a gray irregular shape) in the x-y plane. The center of mass (CM) is marked with a dot. A velocity vector V points downwards and to the right from the CM. A curved arrow labeled ω indicates rotation counter-clockwise around the CM. The x and y axes are shown as coordinate axes.

Fig. 8.3

![Figure 8.4: A diagram showing the vector relationships for a rigid body in the x-y plane. The center of mass (CM) is at position vector R from the origin. A point on the body is at position vector r from the origin. The vector from the CM to this point is r'. The vectors R, r', and r form a triangle. The x and y axes are shown.](2fad86817518ec25dc5518f31d5dffbf_img.jpg)

Figure 8.4: A diagram showing the vector relationships for a rigid body in the x-y plane. The center of mass (CM) is at position vector R from the origin. A point on the body is at position vector r from the origin. The vector from the CM to this point is r'. The vectors R, r', and r form a triangle. The x and y axes are shown.

Fig. 8.4

#### 8.1.2 General motion in $x$ - $y$ plane

How do we deal with general motion in the  $x$ - $y$  plane? For the motion in Fig. 8.3, where the object is both translating and spinning, the various pieces of mass don't travel in circles around the origin, so we can't write  $v = \omega r$  as we did above. It turns out to be highly advantageous to write the angular momentum,  $\mathbf{L}$ , and the kinetic energy,  $T$ , in terms of the center-of-mass (CM) coordinates and the coordinates relative to the CM. The expressions for  $\mathbf{L}$  and  $T$  take on very nice forms when written this way, as we now show.

Let the position of the CM relative to a fixed origin be  $\mathbf{R} = (X, Y)$ . And let the position of a given point relative to the CM be  $\mathbf{r}' = (x', y')$ . Then the position of the given point relative to the fixed origin is  $\mathbf{r} = \mathbf{R} + \mathbf{r}'$  (see Fig. 8.4). Let the velocity of the CM be  $\mathbf{V}$ , and let the velocity relative to the CM be  $\mathbf{v}'$ . Then  $\mathbf{v} = \mathbf{V} + \mathbf{v}'$ . Let the body rotate with angular speed  $\omega'$  around the CM (around an instantaneous axis parallel to the  $z$  axis, so that the pancake remains in the  $x$ - $y$  plane at all times).<sup>3</sup> Then  $v' = \omega' r'$ .

Let's look at  $\mathbf{L}$  first. Let  $M$  be the total mass of the pancake. The angular momentum relative to the origin is

$$\begin{aligned}
 \mathbf{L} &= \int \mathbf{r} \times \mathbf{v} \, dm \\
 &= \int (\mathbf{R} + \mathbf{r}') \times (\mathbf{V} + \mathbf{v}') \, dm \\
 &= \int \mathbf{R} \times \mathbf{V} \, dm + \int \mathbf{r}' \times \mathbf{v}' \, dm \quad (\text{cross terms vanish; see below}) \\
 &= M\mathbf{R} \times \mathbf{V} + \left( \int r'^2 \omega' \, dm \right) \hat{\mathbf{z}} \\
 &\equiv \mathbf{R} \times \mathbf{P} + \left( I_z^{\text{CM}} \omega' \right) \hat{\mathbf{z}}. \tag{8.9}
 \end{aligned}$$

In going from the second to third line above, the cross terms,  $\int \mathbf{r}' \times \mathbf{V} \, dm$  and  $\int \mathbf{R} \times \mathbf{v}' \, dm$ , vanish by definition of the CM, which says that  $\int \mathbf{r}' \, dm = 0$ . (See Eq. (5.58); basically, the position of the CM in the CM frame is zero.) This implies that  $\int \mathbf{v}' \, dm = d(\int \mathbf{r}' \, dm)/dt$  also equals zero. And since we can pull the constant vectors  $\mathbf{V}$  and  $\mathbf{R}$  out of the above integrals, we are therefore left with zero. The quantity  $I_z^{\text{CM}}$  in the final result is the moment of inertia around an axis through the CM, parallel to the  $z$  axis. Equation (8.9) is a very nice result, and it is important enough to be called a theorem. In words, it says:

**Theorem 8.1** *The angular momentum (relative to the origin) of a body can be found by treating the body like a point mass located at the CM and finding the*

<sup>3</sup> What we mean here is the following. Consider a coordinate system whose origin is the CM and whose axes are parallel to the fixed  $x$  and  $y$  axes. Then the pancake rotates with angular speed  $\omega'$  with respect to this system.

*angular momentum of this point mass relative to the origin, and by then adding on the angular momentum of the body relative to the CM.*<sup>4</sup>

Note that if we have the special case where the CM travels around the origin in a circle with angular speed  $\Omega$  (so that  $V = \Omega R$ ), then Eq. (8.9) becomes  $\mathbf{L} = (MR^2\Omega + I_z^{\text{CM}}\omega')\hat{\mathbf{z}}$ .

Now let's look at  $T$ . The kinetic energy is

$$\begin{aligned}
 T &= \int \frac{1}{2} v^2 dm \\
 &= \int \frac{1}{2} |\mathbf{V} + \mathbf{v}'|^2 dm \\
 &= \frac{1}{2} \int V^2 dm + \frac{1}{2} \int v'^2 dm \quad (\text{cross term vanishes; see below}) \\
 &= \frac{1}{2} MV^2 + \frac{1}{2} \int r'^2 \omega'^2 dm \\
 &\equiv \frac{1}{2} MV^2 + \frac{1}{2} I_z^{\text{CM}} \omega'^2.
 \end{aligned} \tag{8.10}$$

In going from the second to third line above, the cross term  $\int \mathbf{V} \cdot \mathbf{v}' dm = \mathbf{V} \cdot \int \mathbf{v}' dm$  vanishes by definition of the CM, as in the above calculation of  $\mathbf{L}$ . Again, Eq. (8.10) is a very nice result. In words, it says:

**Theorem 8.2** *The kinetic energy of a body can be found by treating the body like a point mass located at the CM, and by then adding on the kinetic energy of the body due to the motion relative to the CM.*<sup>5</sup>

To calculate  $E$ , my dear class,  
 Just add up two things, and you'll pass.  
 Take the CM point's  $E$ ,  
 And then add on with glee,  
 The  $E$  'round the center of mass.

---

**Example (Cylinder on a ramp):** A cylinder of mass  $m$ , radius  $r$ , and moment of inertia  $I = (1/2)mr^2$  (this is the  $I$  for a solid cylinder around its center, as we'll see in Section 8.3.1) rolls without slipping down a plane inclined at an angle  $\theta$ . What is the acceleration of the center of the cylinder?

<sup>4</sup> This theorem works only if we use the CM as the location of the imagined point mass. True, in the above analysis we could have chosen a point  $P$  other than the CM, and then written things in terms of the coordinates of  $P$  and the coordinates relative to  $P$  (which could also be described by a rotation). But then the cross terms in Eq. (8.9) wouldn't vanish, and we'd end up with an unenlightening mess.

<sup>5</sup> We already knew this from Section 5.6.2. It's just that now we know that the kinetic energy in the CM frame takes the form of  $I_z^{\text{CM}}\omega'^2/2$ .

**Solution:** We'll use conservation of energy to determine the speed  $v$  of the center of the cylinder after it has moved a distance  $d$  down the plane, and then we'll read off  $a$  from the standard constant-acceleration kinematic relation,  $v = \sqrt{2ad}$ .

The loss in potential energy of the cylinder is  $mgd \sin \theta$ . This shows up as kinetic energy, which equals  $mv^2/2 + I\omega^2/2$  from Theorem 8.2. But the nonslipping condition is  $v = \omega r$ . Therefore,  $\omega = v/r$ , and conservation of energy gives

$$\begin{aligned} mgd \sin \theta &= \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2 \\ &= \frac{1}{2}mv^2 + \frac{1}{2}\left(\frac{1}{2}mr^2\right)\left(\frac{v}{r}\right)^2 \\ &= \frac{3}{4}mv^2. \end{aligned} \quad (8.11)$$

So the speed as a function of distance is  $v = \sqrt{(4/3)gd \sin \theta}$ . Hence,  $v = \sqrt{2ad}$  gives  $a = (2/3)g \sin \theta$ , which is independent of  $r$ .

**REMARKS:** Our answer is  $2/3$  of the  $g \sin \theta$  result for a block sliding down a frictionless plane. It is smaller because there is kinetic energy “wasted” in the rotational motion. Alternatively, it is smaller because there is a friction force pointing up the plane (to provide the torque necessary to get the cylinder rotating, but we'll talk about torque in Section 8.4), so this decreases the net force down the plane.

If we let  $I$  take the general form  $I = \beta mr^2$ , where  $\beta$  is a numerical factor, then you can show that the acceleration becomes  $a = \sqrt{g \sin \theta / (1 + \beta)}$ . So if  $\beta = 0$  (all the mass is at the center), then we simply have  $a = g \sin \theta$ , so the cylinder behaves just like a sliding block. If  $\beta = 1$  (all the mass is on the rim), then  $a = (1/2)g \sin \theta$ . If  $\beta \rightarrow \infty$ ,<sup>6</sup> then  $a \rightarrow 0$ . After reading Section 8.4, you can think about these special cases alternatively in terms of the forces and torques involved.

Although this problem can also be solved by using force and torque (the task of Exercise 8.37), the conservation-of-energy method is generally quicker in more complicated problems of this type, as you can see by doing, for example, Exercises 8.28 and 8.46. ♣

![Diagram illustrating the parallel-axis theorem. A rigid body (shaded gray) is shown with its center of mass (CM) at a distance R from the origin of a Cartesian coordinate system (x, y). A stick is attached to the origin, and the body is pivoted at the origin. The body is rotating with an angular velocity ω. The distance from the origin to the CM is labeled R.](3084bac1a59dbb10a7fccd0f2003ecab_img.jpg)

Diagram illustrating the parallel-axis theorem. A rigid body (shaded gray) is shown with its center of mass (CM) at a distance R from the origin of a Cartesian coordinate system (x, y). A stick is attached to the origin, and the body is pivoted at the origin. The body is rotating with an angular velocity ω. The distance from the origin to the CM is labeled R.

**Fig. 8.5**

#### 8.1.3 The parallel-axis theorem

Consider the special case where the CM rotates around the origin at the same rate as the body rotates around the CM. This can be achieved, for example, by gluing a stick across the pancake and pivoting one end of the stick at the origin; see Fig. 8.5. In this special case, we have the simplified situation where all points in the pancake travel in circles around the origin. Let their angular speed be  $\omega$ . Then the speed of the CM is  $V = \omega R$ , so Eq. (8.9) gives the angular momentum around the origin as

$$L_z = (MR^2 + I_z^{\text{CM}})\omega. \quad (8.12)$$

<sup>6</sup> This can be obtained by adding on long spokes protruding from the cylinder and having them pass through a deep groove in the plane, or by having a spool with a very small inner radius roll down a thin plane with only its inner “axle” rolling on the plane.

In other words, the moment of inertia around the origin is

$$I_z = MR^2 + I_z^{\text{CM}}. \quad (8.13)$$

This is the *parallel-axis theorem*. It says that once you've calculated the moment of inertia of an object around the axis passing through the CM (namely  $I_z^{\text{CM}}$ ), then if you want to calculate the moment of inertia around a parallel axis, you simply have to add on  $MR^2$ , where  $R$  is the distance between the two axes, and  $M$  is the mass of the object. Note that since the parallel-axis theorem is a special case of the result in Eq. (8.9), it is valid *only* with the CM, and not with any other point. The parallel-axis theorem actually holds for arbitrary nonplanar objects too, as we'll see in Section 8.2. And we'll also derive a more general form of the theorem in Chapter 9.

We can also look at the kinetic energy in this special case where the CM rotates around the origin at the same rate as the body rotates around the CM. Using  $V = \omega R$  in Eq. (8.10), we find

$$T = \frac{1}{2} (MR^2 + I_z^{\text{CM}}) \omega^2 = \frac{1}{2} I_z \omega^2. \quad (8.14)$$

**Example (A stick):** Let's verify the parallel-axis theorem for a stick of mass  $m$  and length  $\ell$ , in the case where we want to compare the moment of inertia around an axis through an end (perpendicular to the stick) with the moment of inertia around an axis through the CM (perpendicular to the stick).

For convenience, let  $\rho = m/\ell$  be the density. The moment of inertia around an axis through an end is

$$I^{\text{end}} = \int_0^\ell x^2 dm = \int_0^\ell x^2 \rho dx = \frac{1}{3} \rho \ell^3 = \frac{1}{3} (\rho \ell) \ell^2 = \frac{1}{3} m \ell^2. \quad (8.15)$$

The moment of inertia around an axis through the CM is

$$I^{\text{CM}} = \int_{-\ell/2}^{\ell/2} x^2 dm = \int_{-\ell/2}^{\ell/2} x^2 \rho dx = \frac{1}{12} \rho \ell^3 = \frac{1}{12} (\rho \ell) \ell^2 = \frac{1}{12} m \ell^2. \quad (8.16)$$

This is consistent with the parallel-axis theorem, Eq. (8.13), because

$$I^{\text{end}} = m \left( \frac{\ell}{2} \right)^2 + I^{\text{CM}}. \quad (8.17)$$

Remember that this works only with the CM. If we instead want to compare  $I^{\text{end}}$  with the  $I$  around a point, say,  $\ell/6$  from that end, then we cannot say that they differ by  $m(\ell/6)^2$ . But we *can* compare each of them to  $I^{\text{CM}}$  and say that they differ by  $(\ell/2)^2 - (\ell/3)^2 = 5\ell^2/36$ .

![Figure 8.6: A diagram showing a shaded, irregularly shaped object labeled 'pancake' in the first quadrant of a Cartesian coordinate system. The horizontal axis is labeled 'x' and the vertical axis is labeled 'y'. The object is entirely within the x-y plane.](f43fa967e0647809e19e661c285f1103_img.jpg)

Figure 8.6: A diagram showing a shaded, irregularly shaped object labeled 'pancake' in the first quadrant of a Cartesian coordinate system. The horizontal axis is labeled 'x' and the vertical axis is labeled 'y'. The object is entirely within the x-y plane.

Fig. 8.6

#### 8.1.4 The perpendicular-axis theorem

This theorem is valid *only* for pancake objects. Consider a pancake object in the  $x$ - $y$  plane (see Fig. 8.6). Then the *perpendicular-axis theorem* says that

$$I_z = I_x + I_y, \quad (8.18)$$

where  $I_x$  and  $I_y$  are defined analogously to the  $I_z$  in Eq. (8.4). That is, to find  $I_x$ , imagine spinning the object around the  $x$  axis at angular speed  $\omega$ , and then define  $I_x \equiv L_x/\omega$ . (Only the distance from the  $x$  axis matters in calculating the speed of a given point. So the fact that the object has extent along the  $x$  direction and is therefore not a pancake in the  $y$ - $z$  plane is irrelevant. The following section has further discussion of this.) Likewise for  $I_y$ . In other words,

$$I_x \equiv \int (y^2 + z^2) dm, \quad I_y \equiv \int (z^2 + x^2) dm, \quad I_z \equiv \int (x^2 + y^2) dm. \quad (8.19)$$

To prove the perpendicular-axis theorem, we simply use the fact that  $z = 0$  for our pancake object. Equation (8.19) then gives  $I_z = I_x + I_y$ . In the limited number of situations where this theorem is applicable, it can save you some trouble. A few examples are given in Section 8.3.1.

### 8.2 Nonplanar objects

In Section 8.1, we restricted the discussion to pancake objects in the  $x$ - $y$  plane. However, nearly all the results we derived carry over to nonplanar objects, provided that the axis of rotation is parallel to the  $z$  axis, and provided that we are concerned only with  $L_z$ , and not  $L_x$  or  $L_y$ . So let's drop the pancake assumption and run through the results we obtained above.

First, consider an object rotating around the  $z$  axis. Let the object have extension in the  $z$  direction. If we imagine slicing the object into pancakes parallel to the  $x$ - $y$  plane, then Eqs. (8.4) and (8.5) correctly give the  $L_z$  for each pancake. And since the  $L_z$  of the whole object is the sum of the  $L_z$ 's of all the pancakes, we see that the  $I_z$  of the whole object is the sum of the  $I_z$ 's of all the pancakes. The difference in the  $z$  values of the pancakes is irrelevant. Therefore, for *any* object rotating around the  $z$  axis, we have

$$I_z = \int (x^2 + y^2) dm, \quad \text{and} \quad L_z = I_z \omega, \quad (8.20)$$

where the integration runs over the entire volume of the body. We'll calculate the  $I_z$  for many nonplanar objects in Section 8.3.1. Note that even though Eq. (8.20) gives the  $L_z$  for an arbitrary object, the analysis in this chapter is still not completely general because (1) we are restricting the axis of rotation to be the (fixed)  $z$  axis, and (2) even with this restriction, an object outside the  $x$ - $y$  plane might

have nonzero  $x$  and  $y$  components of  $\mathbf{L}$ , but we found only the  $z$  component in Eq. (8.20). This second fact is strange but true. We'll deal with it in great detail in Section 9.2.

As far as the kinetic energy goes, the  $T$  for a nonplanar object rotating around the  $z$  axis is still given by Eq. (8.8), because we can obtain the total  $T$  by adding up the  $T$ 's of all the pancake slices.

Also, Eqs. (8.9) and (8.10) continue to hold for a nonplanar object in the case where the CM is translating while the object is spinning around it (or more precisely, spinning around an axis parallel to the  $z$  axis and passing through the CM). The velocity  $\mathbf{V}$  of the CM can actually point in any direction, and these two equations are still valid. But we'll assume in this chapter that all velocities are in the  $x$ - $y$  plane.

Lastly, the parallel-axis theorem still holds for a nonplanar object (the derivation using Eq. (8.9) is the same). But as mentioned in Section 8.1.4, the perpendicular-axis theorem does *not* hold. This is the one instance where we need the planar assumption.

### Finding the CM

The center of mass has come up repeatedly in this chapter. For example, when we used the parallel-axis theorem, we needed to know where the CM was. In some cases, such as with a stick or a disk, the location is obvious. But in other cases, it isn't so clear. So let's get a little practice calculating the location of the CM. Depending on whether the mass distribution is discrete or continuous, the position of the CM is defined by (see Eq. (5.58))

$$\mathbf{R}_{\text{CM}} = \frac{\sum \mathbf{r}_i m_i}{M}, \quad \text{or} \quad \mathbf{R}_{\text{CM}} = \frac{\int \mathbf{r} dm}{M}, \quad (8.21)$$

where  $M$  is the total mass. We'll do an example with a continuous mass distribution here. As is often the case with problems involving an integral, the main step in the solution is deciding how you want to slice the object to do the integral.

---

**Example (Hemispherical shell):** Find the location of the CM of a hollow hemispherical shell, with uniform mass density and radius  $R$ .

**Solution:** By symmetry, the CM is located on the line above the center of the base. So our task reduces to finding the height,  $y_{\text{CM}}$ . Let the mass density be  $\sigma$ . We'll slice the hemisphere up into horizontal rings, described by the angle  $\theta$  above the horizontal, as shown in Fig. 8.7. If the angular thickness of a ring is  $d\theta$ , then its mass is

$$dm = \sigma dA = \sigma (\text{length})(\text{width}) = \sigma (2\pi R \cos \theta)(R d\theta). \quad (8.22)$$

![Diagram of a hemispherical shell of radius R. A horizontal ring is shown at an angle theta above the base. The radius of the ring is R cos theta, and its height from the base is R sin theta. The angle theta is measured from the horizontal base to the radius of the shell.](bea0482d6dddfd01b8379f6707b6ec53_img.jpg)

Diagram of a hemispherical shell of radius R. A horizontal ring is shown at an angle theta above the base. The radius of the ring is R cos theta, and its height from the base is R sin theta. The angle theta is measured from the horizontal base to the radius of the shell.

Fig. 8.7

All points on the ring have a  $y$  value of  $R \sin \theta$ . Therefore,

$$\begin{aligned}
 y_{\text{CM}} &= \frac{1}{M} \int y \, dm = \frac{1}{(2\pi R^2)\sigma} \int_0^{\pi/2} (R \sin \theta)(2\pi R^2 \sigma \cos \theta \, d\theta) \\
 &= R \int_0^{\pi/2} \sin \theta \cos \theta \, d\theta \\
 &= \frac{R \sin^2 \theta}{2} \Big|_0^{\pi/2} \\
 &= \frac{R}{2}.
 \end{aligned} \tag{8.23}$$

The simple factor of  $1/2$  here is nice, but it's not all that obvious. It comes from the fact that each value of  $y$  is represented equally. If you solved the problem by doing a  $dy$  integral instead of a  $d\theta$  one, you would find that there is the same area (and hence the same mass) in each ring of vertical height  $dy$ . In short, as  $y$  increases, the larger tilt of the surface cancels out the smaller radius of the rings, yielding the same area. You are encouraged to work this out.

The calculation of a CM is very similar to the calculation of a moment of inertia. Both involve an integration over the mass of an object, but the former has one power of a length in the integrand, whereas the latter has two powers.

### 8.3 Calculating moments of inertia

#### 8.3.1 Lots of examples

Let's now calculate the moments of inertia of various objects, around specified axes. We'll use  $\rho$  to denote the mass density (per unit length, area, or volume, as appropriate), and we'll assume that this density is uniform throughout the object. For the more complicated objects in the list below, it is generally a good idea to slice them up into pieces for which  $I$  is already known. The problem then reduces to integrating over these known  $I$ 's. There is usually more than one way to do this slicing. For example, a sphere can be looked at as a series of concentric shells or a collection of disks stacked on top of each other. In the examples below, you may want to play around with slicings other than the ones given. Consider at least a few of these examples to be problems and try to work them out for yourself.

![Figure 8.8: Two diagrams of a ring. The top diagram shows a ring in a horizontal plane with a vertical dashed axis passing through its center. A dashed line from the center to the edge is labeled R. The bottom diagram shows the same ring from a side view, appearing as a horizontal ellipse. A horizontal dashed axis passes through the center of the ellipse, and a dashed line from the center to the edge is labeled R.](7dff0de33b9f2d3ad4e76d49bd0d9ba1_img.jpg)

Figure 8.8: Two diagrams of a ring. The top diagram shows a ring in a horizontal plane with a vertical dashed axis passing through its center. A dashed line from the center to the edge is labeled R. The bottom diagram shows the same ring from a side view, appearing as a horizontal ellipse. A horizontal dashed axis passes through the center of the ellipse, and a dashed line from the center to the edge is labeled R.

1. A ring of mass  $M$  and radius  $R$  (axis through center, perpendicular to plane; Fig. 8.8):

$$I = \int r^2 \, dm = \int_0^{2\pi} R^2 \rho R \, d\theta = (2\pi R \rho) R^2 = \boxed{MR^2}, \tag{8.24}$$

as expected, because all of the mass is a distance  $R$  from the axis.

Fig. 8.8

- 2. A ring of mass  $M$  and radius  $R$  (axis through center, in plane; Fig. 8.8): The distance from the axis is (the absolute value of)  $R \sin \theta$ . Therefore,

$$I = \int r^2 dm = \int_0^{2\pi} (R \sin \theta)^2 \rho R d\theta = \frac{1}{2}(2\pi R \rho)R^2 = \boxed{\frac{1}{2}MR^2}, \quad (8.25)$$

where we have used  $\sin^2 \theta = (1 - \cos 2\theta)/2$ . You can also find  $I$  by using the perpendicular-axis theorem. In the notation of Section 8.1.4, we have  $I_x = I_y$ , by symmetry. Therefore,  $I_z = 2I_x$ . Using  $I_z = MR^2$  from Example 1 then gives  $I_x = MR^2/2$ .

- 3. A disk of mass  $M$  and radius  $R$  (axis through center, perpendicular to plane; Fig. 8.9):

$$I = \int r^2 dm = \int_0^{2\pi} \int_0^R r^2 \rho r dr d\theta = (R^4/4)2\pi\rho = \frac{1}{2}(\rho\pi R^2)R^2 = \boxed{\frac{1}{2}MR^2}. \quad (8.26)$$

You can save the (trivial) step of integrating over  $\theta$  by considering the disk to be made up of many concentric rings, and invoking Example 1. The mass of each ring is  $\rho 2\pi r dr$ . Integrating over the rings gives  $I = \int_0^R (\rho 2\pi r dr)r^2 = \pi R^4 \rho/2 = MR^2/2$ , as above. Slicing up the disk is fairly inconsequential in this example, but it will save you some trouble in others.

- 4. A disk of mass  $M$  and radius  $R$  (axis through center, in plane; Fig. 8.9): Slice the disk up into rings, and use Example 2.

$$I = \int_0^R (1/2)(\rho 2\pi r dr)r^2 = (R^2/4)\rho\pi = \frac{1}{4}(\rho\pi R^2)R^2 = \boxed{\frac{1}{4}MR^2}. \quad (8.27)$$

Or just use Example 3 and the perpendicular-axis theorem.

- 5. A thin uniform rod of mass  $M$  and length  $L$  (axis through center, perpendicular to rod; Fig. 8.10): We already found this  $I$  and the next one in Section 8.1.3, but we'll include them here for completeness.

$$I = \int x^2 dm = \int_{-L/2}^{L/2} x^2 \rho dx = \frac{1}{12}(\rho L)L^2 = \boxed{\frac{1}{12}ML^2}. \quad (8.28)$$

- 6. A thin uniform rod of mass  $M$  and length  $L$  (axis through end, perpendicular to rod; Fig. 8.10):

$$I = \int x^2 dm = \int_0^L x^2 \rho dx = \frac{1}{3}(\rho L)L^2 = \boxed{\frac{1}{3}ML^2}. \quad (8.29)$$

- 7. A spherical shell of mass  $M$  and radius  $R$  (any axis through center; Fig. 8.11): Let's slice the sphere into horizontal ring-like strips. In spherical coordinates, the radius of a ring is given by  $r = R \sin \theta$ , where  $\theta$  is the angle down from the north pole.

![Figure 8.9: Two diagrams of a disk. The top diagram shows a disk with a vertical dashed line through its center representing the axis of rotation, and a horizontal dashed line indicating the radius R. The bottom diagram shows a disk with a horizontal dashed line through its center representing the axis of rotation, and a vertical dashed line indicating the radius R.](d1634419d2a0fa0df85c4ec2c1432029_img.jpg)

Figure 8.9: Two diagrams of a disk. The top diagram shows a disk with a vertical dashed line through its center representing the axis of rotation, and a horizontal dashed line indicating the radius R. The bottom diagram shows a disk with a horizontal dashed line through its center representing the axis of rotation, and a vertical dashed line indicating the radius R.

Fig. 8.9

![Figure 8.10: Two diagrams of a thin uniform rod. The top diagram shows a horizontal rod of length L with a vertical dashed line through its center representing the axis of rotation. The bottom diagram shows a horizontal rod of length L with a vertical dashed line at its left end representing the axis of rotation.](4085a02da000201e4dfacb067924e942_img.jpg)

Figure 8.10: Two diagrams of a thin uniform rod. The top diagram shows a horizontal rod of length L with a vertical dashed line through its center representing the axis of rotation. The bottom diagram shows a horizontal rod of length L with a vertical dashed line at its left end representing the axis of rotation.

Fig. 8.10

![Figure 8.11: Two diagrams of a sphere. The top diagram shows a sphere with radius R and a vertical dashed line through its center. The bottom diagram shows a sphere with radius R and a horizontal dashed line through its center.](c4b7fb30b18b64b6a73a27a0522cec1c_img.jpg)

Figure 8.11: Two diagrams of a sphere. The top diagram shows a sphere with radius R and a vertical dashed line through its center. The bottom diagram shows a sphere with radius R and a horizontal dashed line through its center.

Fig. 8.11

![Figure 8.12: Two diagrams of a triangle. The top diagram shows a very thin triangle with length L and a small angle 2\beta. The bottom diagram shows a triangle with length L, vertex angle 2\beta, and altitude h.](a6eb6d319d9ac5c08036f1e1fd224204_img.jpg)

Figure 8.12: Two diagrams of a triangle. The top diagram shows a very thin triangle with length L and a small angle 2\beta. The bottom diagram shows a triangle with length L, vertex angle 2\beta, and altitude h.

Fig. 8.12

The area of a strip is then  $2\pi(R \sin \theta)R d\theta$ . Using  $\int \sin^3 \theta = \int \sin \theta (1 - \cos^2 \theta) = -\cos \theta + \cos^3 \theta / 3$ , we have

$$\begin{aligned} I &= \int r^2 dm = \int_0^\pi (R \sin \theta)^2 2\pi \rho (R \sin \theta) R d\theta = 2\pi \rho R^4 \int_0^\pi \sin^3 \theta \\ &= 2\pi \rho R^4 (4/3) = \frac{2}{3} (4\pi R^2 \rho) R^2 = \boxed{\frac{2}{3} MR^2}. \end{aligned} \quad (8.30)$$

An alternate and slick way of deriving this is to use the following result, similar in spirit to the perpendicular-axis theorem: Adding up the three moments of inertia in Eq. (8.19) gives

$$I_x + I_y + I_z = 2 \int (x^2 + y^2 + z^2) dm = 2 \int r^2 dm. \quad (8.31)$$

If we apply this to a spherical shell, where  $r$  always equals the radius  $R$ , then the right-hand side is  $2MR^2$ . And since the  $I$ 's are all equal by symmetry, they must all be  $2MR^2/3$ .

- 8. A solid sphere of mass  $M$  and radius  $R$  (any axis through center; Fig. 8.11): A sphere is made up of concentric spherical shells. The volume of a shell is  $4\pi r^2 dr$ . Using Example 7, we have

$$I = \int_0^R (2/3)(4\pi \rho r^2 dr) r^2 = (R^5/5)(8\pi \rho/3) = \frac{2}{5} (4\pi R^3 \rho/3) R^2 = \boxed{\frac{2}{5} MR^2}. \quad (8.32)$$

The task of Exercise 8.33 is to derive this result by slicing the sphere into horizontal disks.

- 9. An infinitesimally thin triangle of mass  $M$  and length  $L$  (axis through tip, perpendicular to plane; Fig. 8.12): Let the base have length  $a$ , where  $a$  is infinitesimally small. Then a tiny vertical slice a distance  $x$  from the tip has length  $a(x/L)$ . If the slice has thickness  $dx$ , then it is essentially a point mass of mass  $dm = \rho ax dx/L$ . Therefore,

$$I = \int x^2 dm = \int_0^L x^2 \rho ax/L dx = \frac{1}{2} (\rho a L / 2) L^2 = \boxed{\frac{1}{2} ML^2}, \quad (8.33)$$

because  $aL/2$  is the area of the triangle. This has the same form as the disk in Example 3, because a disk is made up of many of these triangles.

- 10. An isosceles triangle of mass  $M$ , vertex angle  $2\beta$ , and common-side length  $L$  (axis through tip, perpendicular to plane; Fig. 8.12): Let  $h$  be the altitude of the triangle (so  $h = L \cos \beta$ ). Slice the triangle into thin strips parallel to the base. Let  $x$  be the distance from a strip to the vertex. Then the length of a strip is  $\ell = 2x \tan \beta$ , and its mass is  $dm = \rho (2x \tan \beta) dx$ . Using Example 5 above, along with the parallel-axis theorem, we have

$$\begin{aligned} I &= \int dm \left( \frac{\ell^2}{12} + x^2 \right) = \int_0^h (\rho 2x \tan \beta dx) \left( \frac{(2x \tan \beta)^2}{12} + x^2 \right) \\ &= 2\rho \tan \beta \int_0^h \left( 1 + \frac{\tan^2 \beta}{3} \right) x^3 dx = 2\rho \tan \beta \left( 1 + \frac{\tan^2 \beta}{3} \right) \frac{h^4}{4}. \end{aligned} \quad (8.34)$$

But the area of the entire triangle is  $h^2 \tan \beta$ , so we have  $I = (Mh^2/2)(1 + (1/3) \tan^2 \beta)$ . In terms of  $L = h/\cos \beta$ , this is

$$I = (ML^2/2)(\cos^2 \beta + \sin^2 \beta/3) = \boxed{\frac{1}{2}ML^2\left(1 - \frac{2}{3}\sin^2 \beta\right)}. \quad (8.35)$$

- 11. A regular  $N$ -gon of mass  $M$  and “radius”  $R$  (axis through center, perpendicular to plane; Fig. 8.13): The  $N$ -gon is made up of  $N$  isosceles triangles, so we can use Example 10, with  $\beta = \pi/N$ . The masses of the triangles simply add, so if  $M$  is the mass of the whole  $N$ -gon, we have

$$I = \boxed{\frac{1}{2}MR^2\left(1 - \frac{2}{3}\sin^2 \frac{\pi}{N}\right)}. \quad (8.36)$$

We can list the values of  $I$  for a few  $N$ . With the shorthand notation  $(N, I/MR^2)$ , Eq. (8.36) gives  $(3, \frac{1}{4})$ ,  $(4, \frac{1}{3})$ ,  $(6, \frac{5}{12})$ ,  $(\infty, \frac{1}{2})$ . These values of  $I$  form a nice arithmetic progression.

- 12. A rectangle of mass  $M$  and sides of length  $a$  and  $b$  (axis through center, perpendicular to plane; Fig. 8.13): Let the  $z$  axis be perpendicular to the plane. We know that  $I_x = Mb^2/12$  and  $I_y = Ma^2/12$  (because the extent of an object along an axis doesn’t affect the moment around that axis, when written in terms of the total  $M$ ). So the perpendicular-axis theorem gives

$$I_z = I_x + I_y = \boxed{\frac{1}{12}M(a^2 + b^2)}. \quad (8.37)$$

![Figure 8.13: Two diagrams illustrating objects for moment of inertia calculations. The top diagram shows a regular hexagon (N=6) with a central dot representing the axis and a dashed line from the center to a vertex labeled R. The bottom diagram shows a rectangle with side lengths a and b, and a central dot representing the axis.](b141fcbdd480fd6ef9d1d5145eb6b762_img.jpg)

Figure 8.13: Two diagrams illustrating objects for moment of inertia calculations. The top diagram shows a regular hexagon (N=6) with a central dot representing the axis and a dashed line from the center to a vertex labeled R. The bottom diagram shows a rectangle with side lengths a and b, and a central dot representing the axis.

Fig. 8.13

#### 8.3.2 A neat trick

For some objects with certain symmetries, it’s possible to calculate the moment of inertia without doing any integrals. The only things we need are a scaling argument and the parallel-axis theorem. We’ll illustrate this technique by finding the  $I$  for a stick around its center (Example 5 above). You’ll find other applications in the problems for this chapter.

In the present example, the basic trick is to compare the  $I$  for a stick of length  $L$  with the  $I$  for a stick of length  $2L$  (and same density  $\rho$ ). A quick scaling argument shows that the latter is eight times the former. This is true because the integral  $\int x^2 dm = \int x^2 \rho dx$  has three powers of  $x$  in it (yes, the  $dx$  counts). So a change of variables,  $x = 2y$ , brings in a factor of  $2^3 = 8$ . Equivalently, if we imagine expanding the smaller stick into the larger one, then a corresponding piece in the larger stick will be twice as far from the axis, and also twice as massive. The integral  $\int x^2 dm$  therefore increases by a factor of  $2^2 \cdot 2 = 8$ .

The technique is most easily illustrated with pictures. If we denote the moment of inertia of an object by a picture of the object, with a dot signifying the axis,

then we have:

$$\begin{aligned} \text{---} \bullet \text{---} &= 8 \text{---} \bullet \text{---} \\ \text{---} \bullet \text{---} &= 2 \bullet \text{---} \\ \bullet \text{---} &= \text{---} \bullet \text{---} + M \left( \frac{L}{2} \right)^2 \end{aligned}$$

The first line comes from the scaling argument, the second line comes from the fact that moments of inertia simply add (the left-hand side is two copies of the right-hand side, attached at the pivot), and the third line comes from the parallel-axis theorem. Equating the right-hand sides of the first two equations gives

$$\text{---} \bullet \text{---} = 4 \bullet \text{---}$$

Plugging this expression for  $\text{---} \bullet \text{---}$  into the third equation gives the desired result,

$$\bullet \text{---} = \frac{1}{12} ML^2$$

Note that sooner or later we must use real live numbers, which enter here through the parallel-axis theorem. Using only scaling arguments isn't sufficient, because they provide only linear equations homogeneous in the  $I$ 's, and therefore give no means of picking up the proper dimensions. (For an interesting account of Galileo's discovery of scaling laws, see Peterson (2002).)

Once you've mastered this trick and applied it to the fractal objects in Problem 8.8, you can impress your friends by saying that you know how to "use scaling arguments, along with the parallel-axis theorem, to calculate moments of inertia of objects with fractal dimension." And you never know when that might come in handy!

### 8.4 Torque

We will now show that under certain conditions (stated below), the rate of change of angular momentum is equal to a certain quantity,  $\boldsymbol{\tau}$ , which we call the *torque*. That is,  $\boldsymbol{\tau} = d\mathbf{L}/dt$ . This is the rotational analog of our old friend  $\mathbf{F} = d\mathbf{p}/dt$  involving linear momentum. The basic idea here is straightforward, but there are two subtle issues. One deals with internal forces within a collection of particles. The other deals with the possible acceleration of the origin (the point relative to which the torque and angular momentum are calculated). To keep things straight, we'll prove the general result by dealing with three increasingly complicated situations.

Our derivation of  $\boldsymbol{\tau} = d\mathbf{L}/dt$  here holds for completely general motion, so we can take the result and use it in the following chapter, too. If you wish, you can construct a more specific proof of  $\boldsymbol{\tau} = d\mathbf{L}/dt$  for the special case where the axis of rotation is parallel to the  $z$  axis. But since the general proof is no more difficult, we'll present it here in this chapter and do it once and for all.

#### 8.4.1 Point mass, fixed origin

Consider a point mass at position  $\mathbf{r}$  relative to a fixed origin (see Fig. 8.14). The time derivative of the angular momentum,  $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ , is

$$\begin{aligned}\frac{d\mathbf{L}}{dt} &= \frac{d}{dt}(\mathbf{r} \times \mathbf{p}) \\ &= \frac{d\mathbf{r}}{dt} \times \mathbf{p} + \mathbf{r} \times \frac{d\mathbf{p}}{dt} \\ &= \mathbf{v} \times (m\mathbf{v}) + \mathbf{r} \times \mathbf{F} \\ &= 0 + \mathbf{r} \times \mathbf{F},\end{aligned}\quad (8.38)$$

![Figure 8.14: A diagram showing a point mass at position r relative to a fixed origin in a 2D Cartesian coordinate system with x and y axes. The vector r points from the origin to the point mass.](c7276a912524ce4d427a56b86aef0506_img.jpg)

Figure 8.14: A diagram showing a point mass at position r relative to a fixed origin in a 2D Cartesian coordinate system with x and y axes. The vector r points from the origin to the point mass.

Fig. 8.14

where  $\mathbf{F}$  is the force acting on the particle. This is the same calculation as in Theorem 7.1, except that here we are considering an arbitrary force instead of a central one. If we define the *torque* on the particle as

$$\boldsymbol{\tau} \equiv \mathbf{r} \times \mathbf{F}, \quad (8.39)$$

then Eq. (8.38) becomes

$$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}. \quad (8.40)$$

It is understood that the  $\mathbf{r}$  in the torque is measured with respect to the same origin as the  $\mathbf{r}$  in the angular momentum.

#### 8.4.2 Extended mass, fixed origin

In an extended object, there are internal forces acting on the various pieces of the object, in addition to whatever external forces exist. For example, the external force on a given molecule in a body might come from gravity, while the internal forces come from the adjacent molecules. How do we deal with these different types of forces?

In what follows, we will deal only with internal forces that are central forces, so that the force between two objects is directed along the line between them. This is a valid assumption for the pushing and pulling forces between molecules in a solid. (It isn't valid, for example, when dealing with magnetic forces. But we won't be interested in such things here.) We will invoke Newton's third law,

![Figure 8.15: A 2D Cartesian coordinate system with x and y axes. Four particles are shown as black dots. From the origin (0,0), four position vectors r1, r2, r3, and r4 are drawn to the particles. The label N=4 is placed near the top of the y-axis.](037f66bef5b58256aa88c221448f00e9_img.jpg)

Figure 8.15: A 2D Cartesian coordinate system with x and y axes. Four particles are shown as black dots. From the origin (0,0), four position vectors r1, r2, r3, and r4 are drawn to the particles. The label N=4 is placed near the top of the y-axis.

Fig. 8.15

which says that the force that particle 1 applies to particle 2 is equal and opposite to the force that particle 2 applies to particle 1.

For concreteness, let's assume that we have a collection of  $N$  discrete particles labeled by the index  $i$  (see Fig. 8.15). In the continuous case, we would need to replace the following sums with integrals. The total angular momentum of the system is

$$\mathbf{L} = \sum_{i=1}^N \mathbf{r}_i \times \mathbf{p}_i. \quad (8.41)$$

The force acting on each particle is  $\mathbf{F}_i^{\text{ext}} + \mathbf{F}_i^{\text{int}} = d\mathbf{p}_i/dt$ . Therefore,

$$\begin{aligned} \frac{d\mathbf{L}}{dt} &= \frac{d}{dt} \sum_i \mathbf{r}_i \times \mathbf{p}_i \\ &= \sum_i \frac{d\mathbf{r}_i}{dt} \times \mathbf{p}_i + \sum_i \mathbf{r}_i \times \frac{d\mathbf{p}_i}{dt} \\ &= \sum_i \mathbf{v}_i \times (m\mathbf{v}_i) + \sum_i \mathbf{r}_i \times (\mathbf{F}_i^{\text{ext}} + \mathbf{F}_i^{\text{int}}) \\ &= 0 + \sum_i \mathbf{r}_i \times \mathbf{F}_i^{\text{ext}} \\ &\equiv \sum_i \boldsymbol{\tau}_i^{\text{ext}}. \end{aligned} \quad (8.42)$$

The second-to-last line follows because  $\mathbf{v}_i \times \mathbf{v}_i = 0$ , and also because  $\sum_i \mathbf{r}_i \times \mathbf{F}_i^{\text{int}} = 0$ , as you can show in Problem 8.9. In other words, the internal forces provide no net torque. This is quite reasonable. It basically says that a rigid object with no external forces won't spontaneously start rotating.

Note that the right-hand side involves the *total* external torque acting on the body, which may come from forces acting at many different points. Note also that nowhere did we assume that the particles are rigidly connected to each other. Equation (8.42) still holds even if there is relative motion among the particles. But in that case, it's usually hard to get a handle on  $\mathbf{L}$ , because it doesn't take the nice  $I\omega$  form.

![Figure 8.16: A 2D Cartesian coordinate system with x and y axes. Two particles are shown as black dots. From the origin (0,0), two position vectors r1 and r2 are drawn to the particles. A third vector r0 is drawn from the origin to a point between the particles. Two relative position vectors, r1 - r0 and r2 - r0, are drawn from the tip of r0 to the tips of r1 and r2 respectively.](1a5ae56da4eb79c2fe9631fc5be14358_img.jpg)

Figure 8.16: A 2D Cartesian coordinate system with x and y axes. Two particles are shown as black dots. From the origin (0,0), two position vectors r1 and r2 are drawn to the particles. A third vector r0 is drawn from the origin to a point between the particles. Two relative position vectors, r1 - r0 and r2 - r0, are drawn from the tip of r0 to the tips of r1 and r2 respectively.

Fig. 8.16

#### 8.4.3 Extended mass, nonfixed origin

Let the position of the origin be  $\mathbf{r}_0$  (see Fig. 8.16), and let the positions of the particles be  $\mathbf{r}_i$ . The vectors  $\mathbf{r}_0$  and  $\mathbf{r}_i$  are measured with respect to a given fixed coordinate system. The total angular momentum of the system, relative to the

(possibly accelerating) origin  $\mathbf{r}_0$ , is<sup>7</sup>

$$\mathbf{L} = \sum_i (\mathbf{r}_i - \mathbf{r}_0) \times m_i (\dot{\mathbf{r}}_i - \dot{\mathbf{r}}_0). \quad (8.43)$$

Therefore,

$$\begin{aligned} \frac{d\mathbf{L}}{dt} &= \frac{d}{dt} \left( \sum_i (\mathbf{r}_i - \mathbf{r}_0) \times m_i (\dot{\mathbf{r}}_i - \dot{\mathbf{r}}_0) \right) \\ &= \sum_i (\dot{\mathbf{r}}_i - \dot{\mathbf{r}}_0) \times m_i (\dot{\mathbf{r}}_i - \dot{\mathbf{r}}_0) + \sum_i (\mathbf{r}_i - \mathbf{r}_0) \times m_i (\ddot{\mathbf{r}}_i - \ddot{\mathbf{r}}_0) \\ &= 0 + \sum_i (\mathbf{r}_i - \mathbf{r}_0) \times (\mathbf{F}_i^{\text{ext}} + \mathbf{F}_i^{\text{int}} - m_i \ddot{\mathbf{r}}_0), \end{aligned} \quad (8.44)$$

because  $m_i \ddot{\mathbf{r}}_i$  is the net force (namely  $\mathbf{F}_i^{\text{ext}} + \mathbf{F}_i^{\text{int}}$ ) acting on the  $i$ th particle. But a quick corollary to Problem 8.9 is that the term involving  $\mathbf{F}_i^{\text{int}}$  vanishes (as you should check). And since  $\sum m_i \mathbf{r}_i = M\mathbf{R}$  (where  $M = \sum m_i$  is the total mass, and  $\mathbf{R}$  is the position of the center of mass), we have

$$\frac{d\mathbf{L}}{dt} = \left( \sum_i (\mathbf{r}_i - \mathbf{r}_0) \times \mathbf{F}_i^{\text{ext}} \right) - M(\mathbf{R} - \mathbf{r}_0) \times \ddot{\mathbf{r}}_0. \quad (8.45)$$

The first term here is the external torque, measured relative to the origin  $\mathbf{r}_0$ . The second term is something we wish would go away. And indeed, it usually does. It vanishes if any of the following three conditions is satisfied.

1.  $\mathbf{R} = \mathbf{r}_0$ , that is, the origin is the CM.
2.  $\ddot{\mathbf{r}}_0 = \mathbf{0}$ , that is, the origin is not accelerating.
3.  $(\mathbf{R} - \mathbf{r}_0)$  is parallel to  $\ddot{\mathbf{r}}_0$ . This condition is rarely invoked.

If any of these conditions is satisfied, then we are free to write

$$\frac{d\mathbf{L}}{dt} = \sum_i (\mathbf{r}_i - \mathbf{r}_0) \times \mathbf{F}_i^{\text{ext}} \equiv \sum_i \boldsymbol{\tau}_i^{\text{ext}}. \quad (8.46)$$

In other words, we can equate the total external torque with the rate of change of the total angular momentum. An immediate corollary of this result is:

**Corollary 8.3** *If the total external torque on a system is zero, then its angular momentum is conserved. In particular, the angular momentum of an isolated system (one that is subject to no external forces) is conserved.*

<sup>7</sup> More precisely, we are calculating the angular momentum relative to a coordinate system whose origin is  $\mathbf{r}_0$  and whose axes remain parallel to the fixed axes. If we allowed for a rotation of the axes, then we would have to deal with all the fictitious-force issues that are the subject of Chapter 10. As it is, we will still end up dealing with one fictitious force (see the remark below).

Everything up to this point is valid for arbitrary motion. The particles can be moving relative to each other, and the various  $\mathbf{L}_i$ 's can point in different directions, etc. But let's now restrict the motion. In the present chapter, we are dealing only with cases where  $\hat{\mathbf{L}}$  is constant (taken to point in the  $z$  direction). Therefore,  $d\mathbf{L}/dt = d(L\hat{\mathbf{L}})/dt = (dL/dt)\hat{\mathbf{L}}$ . If in addition we consider only rigid objects (where the relative distances among the particles are fixed) that undergo pure rotation around a given point, then  $L = I\omega$ , which gives  $dL/dt = I\dot{\omega} \equiv I\alpha$ . Taking the magnitude of both sides of Eq. (8.46) then gives

$$\tau_{\text{ext}} = I\alpha. \quad (8.47)$$

Invariably, we will calculate angular momentum and torque around either the CM or a fixed point (or a point that moves with constant velocity, but this doesn't come up often). These are the "safe" origins, in the sense that Eq. (8.46) holds. As long as you always use one of these safe origins, you can simply apply Eq. (8.46) and not worry much about its derivation.

**REMARK:** You'll probably never end up invoking the third condition above, but it's interesting to note that there's a simple way of understanding it in terms of accelerating reference frames. This is the topic of Chapter 10, so we're getting a little ahead of ourselves here, but the reasoning is as follows. Let  $\mathbf{r}_0$  be the origin of a reference frame that is accelerating with acceleration  $\ddot{\mathbf{r}}_0$ . Then all objects in this accelerating frame feel a mysterious fictitious force of  $-m\ddot{\mathbf{r}}_0$ . For example, on a train accelerating to the right with acceleration  $a$ , you feel a strange force of  $ma$  pointing to the left. If you don't counter this with another force (by grabbing a handle, for example), then you will fall over. This fictitious force acts just like a gravitational force, because it is proportional to the mass. Therefore, it effectively acts at the CM, producing a torque of  $(\mathbf{R} - \mathbf{r}_0) \times (-M\ddot{\mathbf{r}}_0)$ . This is the second term in Eq. (8.45). This term vanishes if the CM is directly "above" or "below" (as far as the fictitious gravitational force is concerned) the origin, in other words, if  $(\mathbf{R} - \mathbf{r}_0)$  is parallel to  $\ddot{\mathbf{r}}_0$ . See Problem 10.8 for further discussion of this in terms of fictitious forces.

There is one common situation where the third condition can be invoked. Consider a wheel rolling without slipping on the ground. Mark a dot on the rim. At the instant this dot is in contact with the ground, it is a valid choice for the origin. This is true because  $(\mathbf{R} - \mathbf{r}_0)$  points vertically. And  $\ddot{\mathbf{r}}_0$  also points vertically, because a dot on a rolling wheel traces out a cycloid. Right before the dot hits the ground, it is moving straight downward. And right after it hits the ground, it is moving straight upward. But having said this, there's usually nothing to be gained by picking such an origin. So the safe thing to do is to always pick your origin to be either the CM or a fixed point, even if the third condition holds.

For conditions that number but three,

We say, "Torque is  $dL$  by  $dt$ ."

But though they're all true,

I'll stick to just two;

It's CM's and fixed points for me! ♣

![Diagram of a cylinder of mass M on an inclined plane at angle theta, connected by a string over a pulley to a hanging mass m.](970ecd80a7730fb0e867e7408ec29008_img.jpg)

The diagram shows a uniform cylinder of mass  $M$  resting on an inclined plane that makes an angle  $\theta$  with the horizontal. A string is wrapped around the cylinder and passes over a massless pulley at the top of the incline. The other end of the string is connected to a hanging mass  $m$ . The string is parallel to the inclined plane.

Diagram of a cylinder of mass M on an inclined plane at angle theta, connected by a string over a pulley to a hanging mass m.

Fig. 8.17

**Example:** A string wraps around a uniform cylinder of mass  $M$ , which rests on a fixed plane. The string passes up over a massless pulley and is connected to a mass  $m$ , as shown in Fig. 8.17. Assume that the cylinder rolls without slipping on the plane, and that the string is parallel to the plane. What is the acceleration of the mass  $m$ ?

What is the condition on the ratio  $M/m$  for which the cylinder accelerates down the plane?

**First solution:** The friction, tension, and gravitational forces are shown in Fig. 8.18. Define positive  $a_1$ ,  $a_2$ , and  $\alpha$  as shown. These three accelerations, along with  $T$  and  $F$ , are five unknowns. We therefore need to produce five equations. They are:

1.  $F = ma$  on  $m \implies T - mg = ma_2$ .
2.  $F = ma$  on  $M \implies Mg \sin \theta - T - F = Ma_1$ .
3.  $\tau = I\alpha$  on  $M$  (around the CM)  $\implies FR - TR = (MR^2/2)\alpha$ .
4. Nonslipping condition  $\implies \alpha = a_1/R$ .
5. Conservation of string  $\implies a_2 = 2a_1$ .

A few comments on these equations: The normal force and the gravitational force perpendicular to the plane cancel, so we can ignore them. We have picked positive  $F$  to point up the plane, but if it happens to point down the plane and thereby turn out to be negative, that's fine (but it won't); we don't need to worry about which way it really points. In (3), we are using the CM of the cylinder as our origin, but we can also use a fixed point; see the second solution below. In (5), we have used the fact that the top of a rolling wheel moves twice as fast as the center. This is true because the top has the same speed relative to the center as the center has relative to the ground.

We can go about solving these five equations in various ways. Three of the equations involve only two variables, so it's not so bad. (3) and (4) give  $F - T = Ma_1/2$ . Adding this to (2) gives  $Mg \sin \theta - 2T = 3Ma_1/2$ . Using (1) to eliminate  $T$ , and using (5) to write  $a_1$  in terms of  $a_2$ , then gives

$$Mg \sin \theta - 2(mg + ma_2) = \frac{3Ma_2}{4} \implies a_2 = \frac{(M \sin \theta - 2m)g}{(3/4)M + 2m}. \quad (8.48)$$

And  $a_1 = a_2/2$ . We see that  $a_1$  is positive (that is, the cylinder rolls down the plane) if  $M/m > 2/\sin \theta$ . If  $\theta \rightarrow 0$ , then this gives  $M/m \rightarrow \infty$ , which makes sense. If  $\theta \rightarrow \pi/2$ , then  $M/m \rightarrow 2$ . The basic reason for this is that the friction force  $F$ , in addition to the tension  $T$ , is holding the cylinder up (the coefficient of friction must be very large in this case if no slipping is to occur).

**Second solution:** In using  $\tau = dL/dt$ , we can also pick a fixed point as our origin, instead of the CM. The most sensible point is one that is located somewhere along the plane. The  $Mg \sin \theta$  force now provides a torque, but the friction does not. And the lever arm for the tension is now  $2R$ . The angular momentum of the cylinder with respect to a point on the plane is  $L = I\omega + Mv_1 R$ , where the second term comes from the angular momentum due to the object being treated like a point mass at the CM. So  $dL/dt = I\alpha + Ma_1 R$ , and  $\tau = dL/dt$  gives

$$(Mg \sin \theta)R - T(2R) = (MR^2/2)\alpha + Ma_1 R. \quad (8.49)$$

This turns out to be the sum of the third equation plus  $R$  times the second equation in the first solution. We therefore obtain the same result.

![Diagram of a cylinder on an inclined plane connected by a string over a pulley to a hanging mass.](8b5ae6dfe4bd6b5c6574f722cde5e426_img.jpg)

The diagram shows a cylinder of mass  $M$  on an inclined plane at angle  $\theta$ . A string is wrapped around the cylinder and passes over a pulley at the top of the incline, connecting to a hanging mass  $m$ . The forces on the cylinder are: tension  $T$  acting up the incline, friction  $F$  acting up the incline, and the component of gravity  $Mg \sin \theta$  acting down the incline. The acceleration of the cylinder's center of mass is  $a_1$  down the incline, and its angular acceleration is  $\alpha$  clockwise. The forces on the hanging mass are: tension  $T$  acting up and gravity  $mg$  acting down. The acceleration of the hanging mass is  $a_2$  upwards.

Diagram of a cylinder on an inclined plane connected by a string over a pulley to a hanging mass.

Fig. 8.18

### 8.5 Collisions

In Section 5.7, we looked at collisions involving point particles or otherwise nonrotating objects. The fundamental ingredients there that enabled us to solve problems were conservation of linear momentum and conservation of energy (if the collision was elastic). With conservation of angular momentum now at our disposal, we can extend our study of collisions to ones with rotating objects. The additional fact of conservation of  $L$  is compensated for by the new degree of freedom of the rotation. Therefore, provided that the problem is set up properly, we will still have the same number of equations as unknowns.

Conservation of energy can be used in a collision only if it is elastic (by definition). But conservation of angular momentum is similar to conservation of linear momentum, in that it can *always* be used (see the remark below), assuming that the system is isolated. However, conservation of  $L$  is a little different from conservation of  $p$ , because we have to pick an origin before we can proceed. In view of the three conditions that are necessary for Corollary 8.3 to hold, we must pick our origin to be either a fixed point or the CM of the system (we'll ignore the third condition, since it's rarely used). If we unwisely choose an accelerating point, then  $\boldsymbol{\tau} = d\mathbf{L}/dt$  does *not* hold, so we have no right to claim that  $d\mathbf{L}/dt$  equals zero just because the torque is zero (as it is for an isolated system). In collision problems, it is easy to fall into the trap of picking an accelerating point as your origin. For example, you might choose the center of a stick as your origin. But if another object collides with the stick, then the center will accelerate, making it an invalid choice for the origin.

**REMARK:** As far as conservation goes, the way that  $E$  differs from  $\mathbf{p}$  and  $\mathbf{L}$  is that energy can be hidden in the microscopic motion of molecules in the body, in the form of heat. This motion consists of little vibrations with small amplitudes but high speeds. The energy of these vibrations can be large enough to be on the same order of magnitude as the overall energy of the system. But because the vibrations are too small to see, it appears that energy is lost. However, note that even though they're too small to see, you can still feel them with your hand, as heat.

Linear momentum, however, can't be hidden. If an object (not necessarily rigid) has nonzero momentum, then it has to be moving as a whole, and there's no way around that. In short, since  $P = MV_{\text{CM}}$ , we see that if  $P$  is nonzero, then  $V_{\text{CM}}$  is also. So the motion must be on a macroscopic scale; there's no way for it to be hidden on a microscopic scale.

With angular momentum, things are a little trickier. If the object is rigid, then it can't have hidden angular momentum, for reasons similar to those in the linear momentum case; since  $L = I\omega$ , we see that if  $L$  is nonzero, then  $\omega$  is also. However, if the object isn't rigid (consider, say, a gas of particles), then it turns out that it *can* theoretically have hidden angular momentum in microscopic motion, although in practice it ends up being too small to notice. This hidden angular momentum can arise from little swirling regions throughout the system. In contrast with linear momentum, it is possible to have angular momentum without any overall motion. So in this respect, this microscopic swirling motion is similar to the microscopic vibrational motion that yields hidden energy. There are, however, three main differences.

First, if we're assuming that the swirling motion takes place on a microscopic scale, then the  $r$  in  $L = mrv$  is very small, and this leads to a negligible  $L$ . This argument doesn't hold for  $E$ , because the energy of the vibrations doesn't involve  $r$ . Instead, it involves only  $v$ , in the form of

$mv^2/2$ , so it can end up being large. Second, there's no easy way to start up the circular motion of many little swirls by means of a collision, in contrast with the easily started random linear motion that makes up the energy of heat; you just smash two things together. And third, in the case where the object is rigid, the molecules can easily vibrate, but they can't rotate indefinitely because this would involve ripping apart the bonds between adjacent molecules. The issue is that in vibrational motion all coordinates remain small, whereas in rotational motion they don't, because  $\theta$  eventually becomes large.

There is, however, one very common phenomenon, namely magnetism, that (in a sense) is an exception to all three of the above points. Although magnetism isn't an angular momentum, it does come (roughly speaking) from the "circular" motion of electrons around the nuclei in atoms. (In general, it actually comes more from the "spin" of the electrons than their orbital motion around the nuclei, but let's not worry about that here. To get everything right, we'd have to think in terms of quantum mechanics, anyway. Let's just work in a rough classical approximation.) Electrons throughout a magnetic material move in tiny little correlated loops. We can escape the above three points of reasoning because first, the magnetic field involves the electric charge  $e$ , and this is large enough (on the scale of things) to cancel out the smallness of the  $r$  factor. (The actual angular momentum of the electrons in a magnetic material is negligible because their mass is so small. There isn't a large quantity like  $e$  to save the day.) Second, it is quite easy to get the electrons moving in correlated circles by means of magnetic forces; there's no need to smash things together. And third, the electrons are free to move around in little circles (in a classical sense) in atoms without ripping things apart. ♣

It is important to remember that you are free to choose your origin from the legal possibilities of fixed points or the CM. Since it is generally the case that one choice is better than others (in that it makes the calculations easier), you should take advantage of this freedom. Let's do two examples. First an elastic collision, and then an inelastic one.

**Example (Elastic collision):** A mass  $m$  travels perpendicular to a stick of mass  $m$  and length  $\ell$ , which is initially at rest. At what location should the mass collide elastically with the stick, so that the mass and the center of the stick move with equal speeds after the collision?

**Solution:** Let the initial speed of the mass be  $v_0$ . We have three unknowns in the problem (see Fig. 8.19), namely the desired distance from the middle of the stick,  $h$ ; the final (equal) speeds of the stick and the mass,  $v$ ; and the final angular speed of the stick,  $\omega$ . We can solve for these three unknowns by using our three available conservation laws:

- Conservation of  $p$ :

$$mv_0 = mv + mv \implies v = \frac{v_0}{2}. \quad (8.50)$$

- Conservation of  $E$ : Remembering that the energy of the stick equals the energy of the rotational motion around the center, plus the energy of the effective point mass at the center, we have

$$\frac{mv_0^2}{2} = \frac{m}{2} \left( \frac{v_0}{2} \right)^2 + \left[ \frac{m}{2} \left( \frac{v_0}{2} \right)^2 + \frac{1}{2} \left( \frac{m\ell^2}{12} \right) \omega^2 \right] \implies \omega = \frac{\sqrt{6}v_0}{\ell}. \quad (8.51)$$

![Diagram illustrating an elastic collision between a mass m and a stick of mass m and length l. The mass m is moving with initial velocity v_0 towards the stick. The stick is initially at rest. The collision occurs at a distance h from the center of the stick. After the collision, the mass m is moving with velocity v, and the stick is rotating with angular velocity omega and translating with velocity v.](03de44af503f29447b85746426f7aa8d_img.jpg)

The diagram shows two stages of a collision. On the left, a mass  $m$  (represented by a black dot) moves with velocity  $v_0$  towards a vertical stick of length  $\ell$  and mass  $m$ . The stick is initially at rest. The collision point is at a distance  $h$  from the center of the stick. On the right, after the collision, the mass  $m$  is moving with velocity  $v$  (indicated by a horizontal arrow), and the stick is rotating with angular velocity  $\omega$  (indicated by a curved arrow) and translating with velocity  $v$  (indicated by a horizontal arrow). The stick is tilted at an angle.

Diagram illustrating an elastic collision between a mass m and a stick of mass m and length l. The mass m is moving with initial velocity v\_0 towards the stick. The stick is initially at rest. The collision occurs at a distance h from the center of the stick. After the collision, the mass m is moving with velocity v, and the stick is rotating with angular velocity omega and translating with velocity v.

Fig. 8.19

- Conservation of  $L$ : Let's pick our origin to be the fixed point in space that coincides with the initial location of the center of the stick. Then conservation of  $L$  gives

$$mv_0h = m\left(\frac{v_0}{2}\right)h + \left[\left(\frac{m\ell^2}{12}\right)\omega + 0\right]. \quad (8.52)$$

The zero here comes from the fact that the CM of the stick moves directly away from the origin, so there is no contribution to  $L$  from the first of the two parts in Theorem 8.1. Plugging the  $\omega$  from Eq. (8.51) into Eq. (8.52) gives

$$\frac{1}{2}mv_0h = \left(\frac{m\ell^2}{12}\right)\left(\frac{\sqrt{6}v_0}{\ell}\right) \implies h = \frac{\ell}{\sqrt{6}}. \quad (8.53)$$

You are encouraged to solve this problem again with a different choice of origin, for example, the fixed point that coincides with the spot where the mass hits the stick, or the CM of the entire system.

**REMARK:** After the stick makes half of a revolution, it will hit the backside of  $m$ . The resulting motion will have the stick sitting at rest (both translationally and rotationally) and the mass moving with its initial speed  $v_0$ . You can show this by working through the second collision, using the quantities we found above. Or you can just use the fact that this scenario certainly satisfies conservation of  $p$ ,  $E$ , and  $L$  with the initial conditions, so it must be what happens (because the quadratic conservation statements have only two solutions, and the other one corresponds to the intermediate motion). Note that the time it takes the stick to make half of a revolution is  $\pi/\omega = \pi\ell/\sqrt{6}v_0$ . So the stick travels a distance of  $(v_0/2)(\pi\ell/\sqrt{6}v_0) = (\pi\ell/2\sqrt{6})$  before it ends up at rest. This distance is independent of  $v_0$  (which follows from dimensional analysis). ♣

Let's now look at an inelastic collision, where one object sticks to another. We won't be able to use conservation of  $E$  now. But conservation of  $p$  and  $L$  will be sufficient since there is one fewer degree of freedom in the final motion, because the objects don't move independently.

![Diagram of an inelastic collision between a mass m and a stick of length l and mass m. The mass m is moving with velocity v_0 towards the left end of the stick, which is initially at rest. After the collision, the system rotates about its center of mass (CM) with angular velocity omega, and the CM moves with a velocity of v_0/2.](7dfb0e4e6fbee609bc35829098aafbfe_img.jpg)

The diagram illustrates an inelastic collision. On the left, a point mass  $m$  is shown moving with velocity  $v_0$  towards a vertical stick of length  $l$  and mass  $m$ . The stick is initially at rest. An arrow points from the initial state to the final state. In the final state, the mass  $m$  is attached to the left end of the stick. The center of mass (CM) of the combined system is marked with an 'x'. The stick is shown at an angle, rotating with angular velocity  $\omega$  (indicated by a curved arrow). The CM is moving to the right with a velocity of  $v_0/2$  (indicated by a straight arrow).

Diagram of an inelastic collision between a mass m and a stick of length l and mass m. The mass m is moving with velocity v\_0 towards the left end of the stick, which is initially at rest. After the collision, the system rotates about its center of mass (CM) with angular velocity omega, and the CM moves with a velocity of v\_0/2.

Fig. 8.20

**Example (Inelastic collision):** A mass  $m$  travels at speed  $v_0$  perpendicular to a stick of mass  $m$  and length  $\ell$ , which is initially at rest. The mass collides completely inelastically with the stick at one of its ends and sticks to it. What is the resulting angular velocity of the system?

**Solution:** The first thing to note is that the CM of the system is  $\ell/4$  from the end, as shown in Fig. 8.20. After the collision, the system rotates about the CM as the CM moves in a straight line. Conservation of momentum quickly tells us that the speed of the CM is  $v_0/2$ . Also, using the parallel-axis theorem, the moment of inertia of the system around the CM is

$$I_{\text{CM}} = I_{\text{CM}}^{\text{stick}} + I_{\text{CM}}^{\text{mass}} = \left[ \frac{m\ell^2}{12} + m\left(\frac{\ell}{4}\right)^2 \right] + m\left(\frac{\ell}{4}\right)^2 = \frac{5}{24}m\ell^2. \quad (8.54)$$

There are now many ways to proceed, depending on what point we choose as our origin.

FIRST METHOD: Choose the origin to be the fixed point that coincides with the location of the CM right when the collision happens (that is, the point  $\ell/4$  from the end of the stick). Conservation of  $L$  says that the initial  $L$  of the ball must equal the final  $L$  of the system. This gives

$$mv_0\left(\frac{\ell}{4}\right) = \left(\frac{5}{24}m\ell^2\right)\omega + 0 \implies \omega = \frac{6v_0}{5\ell}. \quad (8.55)$$

The zero here comes from the fact that the CM of the stick moves directly away from the origin, so there is no contribution to  $L$  from the first of the two parts in Theorem 8.1. Note that we didn't need to use conservation of  $p$  in this method.

SECOND METHOD: Choose the origin to be the fixed point that coincides with the initial center of the stick. Then conservation of  $L$  gives

$$mv_0\left(\frac{\ell}{2}\right) = \left(\frac{5}{24}m\ell^2\right)\omega + (2m)\left(\frac{v_0}{2}\right)\left(\frac{\ell}{4}\right) \implies \omega = \frac{6v_0}{5\ell}. \quad (8.56)$$

The right-hand side is the angular momentum of the system relative to the CM, plus the angular momentum (relative to the origin) of a point mass of mass  $2m$  located at the CM.

THIRD METHOD: Choose the origin to be the CM of the system. This point moves to the right with speed  $v_0/2$ , along the line a distance  $\ell/4$  below the top of the stick. Relative to the CM, the mass  $m$  moves to the right, and the stick moves to the left, both with speed  $v_0/2$ . Conservation of  $L$  gives

$$m\left(\frac{v_0}{2}\right)\left(\frac{\ell}{4}\right) + \left[0 + m\left(\frac{v_0}{2}\right)\left(\frac{\ell}{4}\right)\right] = \left(\frac{5}{24}m\ell^2\right)\omega \implies \omega = \frac{6v_0}{5\ell}. \quad (8.57)$$

The zero here comes from the fact that the stick initially has no  $L$  around its center. A fourth reasonable choice for the origin is the fixed point that coincides with the initial location of the top of the stick. You can work this one out for practice.

### 8.6 Angular impulse

In Section 5.5.1, we defined the *impulse*, which we'll label as  $\mathcal{I}$ , to be the time integral of the force applied to an object. From Newton's second law,  $\mathbf{F} = d\mathbf{p}/dt$ , the impulse is therefore the net change in linear momentum. That is,

$$\mathcal{I} \equiv \int_{t_1}^{t_2} \mathbf{F}(t) dt = \Delta\mathbf{p}. \quad (8.58)$$

We now define the *angular impulse*,  $\mathcal{I}_\theta$ , to be the time integral of the torque applied to an object. From  $\boldsymbol{\tau} = d\mathbf{L}/dt$ , the angular impulse is therefore the net

change in angular momentum. That is,

$$\mathcal{I}_\theta \equiv \int_{t_1}^{t_2} \boldsymbol{\tau}(t) dt = \Delta \mathbf{L}. \quad (8.59)$$

These are just definitions, devoid of any content. The place where the physics comes in is the following. Consider a situation where  $\mathbf{F}(t)$  is always applied at the same position relative to the origin around which  $\boldsymbol{\tau}(t)$  is calculated (this origin must be a legal one, of course). Let this position be  $\mathbf{R}$ . Then we have  $\boldsymbol{\tau}(t) = \mathbf{R} \times \mathbf{F}(t)$ . Plugging this into Eq. (8.59), and taking the constant  $\mathbf{R}$  outside the integral, gives  $\mathcal{I}_\theta = \mathbf{R} \times \mathcal{I}$ . In other words,

$$\Delta \mathbf{L} = \mathbf{R} \times (\Delta \mathbf{p}) \quad (\text{for } \mathbf{F}(t) \text{ applied at one position}). \quad (8.60)$$

This is a very useful result. It gives the relation between the net changes in  $\mathbf{L}$  and  $\mathbf{p}$ , as opposed to the individual values of each. Even if  $\mathbf{F}(t)$  is changing in some arbitrary manner as time goes by, so that we have no idea what  $\Delta \mathbf{L}$  and  $\Delta \mathbf{p}$  themselves are, we still know that they are related by Eq. (8.60). In many cases, we don't have to worry about the cross product in Eq. (8.60), because the lever arm  $\mathbf{R}$  is perpendicular to the change in momentum  $\Delta \mathbf{p}$ . In such cases, we have

$$|\Delta L| = R|\Delta p|. \quad (8.61)$$

Also, in many cases the object starts at rest, so we don't have to bother with the  $\Delta$ 's. The following example is a classic application of angular impulse and Eq. (8.61).

---

**Example (Striking a stick):** A stick of mass  $m$  and length  $\ell$ , initially at rest, is struck with a hammer. The blow is made perpendicular to the stick at one end. Let the blow occur quickly, so that the stick doesn't have time to move much while the hammer is in contact. If the CM of the stick ends up moving at speed  $v$ , what are the velocities of the ends right after the blow?

**Solution:** Although we have no hope of knowing exactly what  $F(t)$  looks like, or the length of time it is applied, we still know from Eq. (8.61) that  $\Delta L = (\ell/2)\Delta p$ , where we have chosen our origin to be the CM, which gives a lever arm of  $\ell/2$ . Therefore,  $(m\ell^2/12)\omega = (\ell/2)mv$ , so the final  $v$  and  $\omega$  are related by  $\omega = 6v/\ell$ .

The velocities of the ends right after the blow are obtained by adding (or subtracting) the rotational motion to the CM's translational motion. The rotational velocities of the ends relative to the CM are  $\pm\omega(\ell/2) = \pm(6v/\ell)(\ell/2) = \pm 3v$ . Therefore, the end that is hit moves with velocity  $v + 3v = 4v$ , and the other end moves with velocity  $v - 3v = -2v$  (that is, backward).

---

What  $L$  was, he just couldn't tell.  
 And  $p$ ? He was clueless as well.  
 But despite his distress,  
 He wrote down the right guess  
 For their quotient: the lever arm's  $\ell$ .

Impulse is also useful for “collisions” that occur over extended times. See, for example, Problem 8.24.

### 8.7 Problems

### Section 8.1: Pancake object in $x$ - $y$ plane

#### 8.1. Massive pulley \*

Consider the Atwood's machine shown in Fig. 8.21. The masses are  $m$  and  $2m$ , and the pulley is a uniform disk of mass  $m$  and radius  $r$ . The string is massless and does not slip with respect to the pulley. Find the acceleration of the masses. Use conservation of energy.

![Diagram of an Atwood's machine. A pulley of mass m is suspended from a ceiling. A string passes over the pulley, with a mass m hanging on the left and a mass 2m hanging on the right.](6d25ede1879a16a491a433bc24f6a03e_img.jpg)

Diagram of an Atwood's machine. A pulley of mass m is suspended from a ceiling. A string passes over the pulley, with a mass m hanging on the left and a mass 2m hanging on the right.

Fig. 8.21

#### 8.2. Leaving the sphere \*\*

A ball with moment of inertia  $\beta mr^2$  rests on top of a fixed sphere. There is friction between the ball and the sphere. The ball is given an infinitesimal kick, and it rolls down without slipping. Assuming that  $r$  is much smaller than the radius of the sphere, at what point does the ball lose contact with the sphere? How does your answer change if the size of the ball is comparable to, or larger than, the size of the sphere? You may want to solve Problem 5.3 first, if you haven't already done so.

![Diagram of a ball of radius r rolling down a sphere of radius R. The ball is at an angle theta from the vertical. The length of the arc from the top is labeled l.](e1e6625c127ed42b5d996a55e42dcaf1_img.jpg)

Diagram of a ball of radius r rolling down a sphere of radius R. The ball is at an angle theta from the vertical. The length of the arc from the top is labeled l.

Fig. 8.22

#### 8.3. Sliding ladder \*\*\*

A ladder of length  $\ell$  and uniform mass density stands on a frictionless floor and leans against a frictionless wall. It is initially held motionless, with its bottom end an infinitesimal distance from the wall. It is then released, whereupon the bottom end slides away from the wall, and the top end slides down the wall (see Fig. 8.22). When it loses contact with the wall, what is the horizontal component of the velocity of the center of mass?

![Diagram of a ladder of length l leaning against a wall. The bottom end is at a distance b from the wall, and the top end is at a height 2a from the floor.](52cb64635442d017a595dde184126e48_img.jpg)

Diagram of a ladder of length l leaning against a wall. The bottom end is at a distance b from the wall, and the top end is at a height 2a from the floor.

#### 8.4. Leaning rectangle \*\*\*

A rectangle of height  $2a$  and width  $2b$  rests on top of a fixed cylinder of radius  $R$  (see Fig. 8.23). The moment of inertia of the rectangle around its center is  $I$ . The rectangle is given an infinitesimal kick and then “rolls” on the cylinder without slipping. Find the equation of motion for the tilt angle of the rectangle. Under what conditions will the rectangle

Fig. 8.23

![Diagram of a mass m inside a tube of mass M and length l, pivoted at one end.](b823f49bb0cc7132db721014495274ec_img.jpg)

A diagram showing a horizontal tube of mass

 $M$ 

and length

 $l$ 

pivoted at its left end. A small mass

 $m$ 

is located at the pivot point. An arrow indicates the tube can rotate downwards from the horizontal position.

Diagram of a mass m inside a tube of mass M and length l, pivoted at one end.

Fig. 8.24

fall off the cylinder, and under what conditions will it oscillate back and forth? Find the frequency of these small oscillations.

#### 8.5. **Mass in a tube \*\*\***

A tube of mass  $M$  and length  $\ell$  is free to swing around a pivot at one end. A mass  $m$  is positioned inside the (frictionless) tube at this end. The tube is held horizontal and then released (see Fig. 8.24). Let  $\theta$  be the angle of the tube with respect to the horizontal, and let  $x$  be the distance the mass has traveled along the tube. Find the Euler–Lagrange equations for  $\theta$  and  $x$ , and then write them in terms of  $\theta$  and  $\eta \equiv x/\ell$  (the fraction of the distance along the tube).

These equations can only be solved numerically, and you must pick a numerical value for the ratio  $r \equiv m/M$  in order to do this. Write a program (see Section 1.4) that produces the value of  $\eta$  when the tube is vertical ( $\theta = \pi/2$ ). Give this value of  $\eta$  for a few values of  $r$ .

![Diagram of a blob of matter between two horizontal planes z=0 and z=1.](d9bb9105052f5332b6be1a017af0106a_img.jpg)

A diagram showing a blob of matter situated between two horizontal planes labeled

 $z=0$ 

and

 $z=1$ 

. A vertical axis passes through the center of the blob.

Diagram of a blob of matter between two horizontal planes z=0 and z=1.

Fig. 8.25

### Section 8.3: Calculating moments of inertia

#### 8.6. **Minimum $I$ \***

A moldable blob of matter of mass  $M$  is to be situated between the planes  $z = 0$  and  $z = 1$  (see Fig. 8.25) so that the moment of inertia around the  $z$  axis is as small as possible. What shape should the blob take?

#### 8.7. **Slick calculations of $I$ \*\***

In the spirit of Section 8.3.2, find the moments of inertia of the following objects (see Fig. 8.26).

- (a) A uniform square of mass  $m$  and side  $\ell$  (axis through center, perpendicular to plane).
- (b) A uniform equilateral triangle of mass  $m$  and side  $\ell$  (axis through center, perpendicular to plane).

![Diagram of a square with side length l and a central axis.](93ebd4b5633042f663b8115764d5b539_img.jpg)

A diagram of a square with side length

 $l$ 

. A central dot represents the axis of rotation, which is perpendicular to the plane of the square.

Diagram of a square with side length l and a central axis.

![Diagram of an equilateral triangle with side length l and a central axis.](a0ff119ce0de3db389c33cec2611d3ed_img.jpg)

A diagram of an equilateral triangle with side length

 $l$ 

. A central dot represents the axis of rotation, which is perpendicular to the plane of the triangle.

Diagram of an equilateral triangle with side length l and a central axis.

Fig. 8.26

#### 8.8. **Slick calculations of $I$ for fractal objects \*\*\***

In the spirit of Section 8.3.2, find the moments of inertia of the following fractal objects. Be careful how the mass scales.

- (a) Take a stick of length  $\ell$ , and remove the middle third. Then remove the middle third from each of the remaining two pieces. Then remove the middle third from each of the remaining four pieces, and so on, forever. Let the final object have mass  $m$ , and let the axis be through the center, perpendicular to the stick; see Fig. 8.27.<sup>8</sup>

![Diagram of a stick of length l with a central axis and dashed lines indicating the removed middle third.](e11baf89a4273e182ee39342c6f03d82_img.jpg)

A diagram of a stick of length

 $l$ 

. A central dot represents the axis of rotation. Dashed lines indicate the removal of the middle third of the stick.

Diagram of a stick of length l with a central axis and dashed lines indicating the removed middle third.

Fig. 8.27

<sup>8</sup> This object is the Cantor set, for those who like such things. It has no length, so the density of the remaining mass is infinite. If you suddenly develop an aversion to point masses with infinite density, simply imagine the above iteration being carried out only, say, a million times.

- (b) Take an equilateral triangle of side  $\ell$ , and remove the “middle” triangle ( $1/4$  of the area). Then remove the “middle” triangle from each of the remaining three triangles, and so on, forever. Let the final object have mass  $m$ , and let the axis be through the center, perpendicular to the plane; Fig. 8.28.
- (c) Take a square of side  $\ell$ , and remove the “middle” square ( $1/9$  of the area). Then remove the “middle” square from each of the remaining eight squares, and so on, forever. Let the final object have mass  $m$ , and let the axis be through the center, perpendicular to the plane; see Fig. 8.29.

![Figure 8.28: A Sierpinski triangle fractal. It is an equilateral triangle of side length l, with a central triangular hole. This process is repeated recursively for the remaining three triangles. A central dot represents the axis of rotation.](9b14925c5df2866d060e6b722dc3b54c_img.jpg)

Figure 8.28: A Sierpinski triangle fractal. It is an equilateral triangle of side length l, with a central triangular hole. This process is repeated recursively for the remaining three triangles. A central dot represents the axis of rotation.

Fig. 8.28

![Figure 8.29: A fractal square. It is a square of side length l, with a central square hole. This process is repeated recursively for the remaining eight squares. A central dot represents the axis of rotation.](9f8660332330364d58f969b8a6b00ac6_img.jpg)

Figure 8.29: A fractal square. It is a square of side length l, with a central square hole. This process is repeated recursively for the remaining eight squares. A central dot represents the axis of rotation.

Fig. 8.29

### Section 8.4: Torque

#### 8.9. Zero torque from internal forces \*\*

Given a collection of particles with positions  $\mathbf{r}_i$ , let the force on the  $i$ th particle due to all the others be  $\mathbf{F}_i^{\text{int}}$ . Assuming that the force between any two particles is directed along the line between them, use Newton’s third law to show that  $\sum_i \mathbf{r}_i \times \mathbf{F}_i^{\text{int}} = 0$ .

#### 8.10. Removing a support \*

- (a) A uniform rod of length  $\ell$  and mass  $m$  rests on supports at its ends. The right support is quickly removed (see Fig. 8.30). What is the force from the left support immediately thereafter?
- (b) A rod of length  $2r$  and moment of inertia  $\beta mr^2$  rests on top of two supports, each of which is a distance  $d$  away from the center. The right support is quickly removed (see Fig. 8.30). What is the force from the left support immediately thereafter?

![Figure 8.30: Two diagrams of rods on supports. The top diagram shows a uniform rod of length l resting on two triangular supports at its ends. The bottom diagram shows a rod of length 2r resting on two triangular supports, each at a distance d from the center. A central dot indicates the center of mass.](79c769e293287e6116f6006c5553d87f_img.jpg)

Figure 8.30: Two diagrams of rods on supports. The top diagram shows a uniform rod of length l resting on two triangular supports at its ends. The bottom diagram shows a rod of length 2r resting on two triangular supports, each at a distance d from the center. A central dot indicates the center of mass.

Fig. 8.30

#### 8.11. Falling stick \*

A massless stick of length  $b$  has one end pivoted on a support and the other end glued perpendicular to the middle of a stick of mass  $m$  and length  $\ell$ .

- (a) If the two sticks are held in a horizontal plane (see Fig. 8.31) and then released, what is the initial acceleration of the CM?
- (b) If the two sticks are held in a vertical plane (see Fig. 8.31) and then released, what is the initial acceleration of the CM?

![Figure 8.31: Two diagrams of two sticks joined at a right angle. The top diagram shows the sticks in a horizontal plane, with a massless stick of length b pivoted at one end to the middle of a stick of mass m and length l. The bottom diagram shows the sticks in a vertical plane, with the massless stick of length b pivoted at one end to the middle of the stick of mass m and length l. Gravity g is shown acting downwards.](13f4378f1ff3d5b9fbaca0c8607b9afb_img.jpg)

Figure 8.31: Two diagrams of two sticks joined at a right angle. The top diagram shows the sticks in a horizontal plane, with a massless stick of length b pivoted at one end to the middle of a stick of mass m and length l. The bottom diagram shows the sticks in a vertical plane, with the massless stick of length b pivoted at one end to the middle of the stick of mass m and length l. Gravity g is shown acting downwards.

Fig. 8.31

#### 8.12. Pulling a cylinder \*\*

In Exercise 8.50 below, the cylinder moves directly to the right. The fact that it doesn’t have any transverse motion follows from the fact that the two segments of the string pull only to the right and therefore cannot supply a transverse force. Demonstrate this result again by explicitly

![Diagram for Fig. 8.32: A ball of radius r rolling inside a larger cylinder of radius R. The ball is at a small angle from the bottom, and a dashed line indicates the radius R of the large cylinder.](900dc97b1b46413aa0cb9f1e74b76be0_img.jpg)

Diagram for Fig. 8.32: A ball of radius r rolling inside a larger cylinder of radius R. The ball is at a small angle from the bottom, and a dashed line indicates the radius R of the large cylinder.

Fig. 8.32

integrating the string's force on the cylinder over the semicircle of contact. (The  $N = T d\theta$  result from the “Rope wrapped around a pole” example in Section 2.1 will come in handy.)

#### 8.13. Oscillating ball \*\*

A small ball with radius  $r$  and uniform density rolls without slipping near the bottom of a fixed cylinder of radius  $R$  (see Fig. 8.32). What is the frequency of small oscillations? Assume  $r \ll R$ .

![Diagram for Fig. 8.33: A mass hanging from a string of length l, swinging in a horizontal circle. The string makes an angle theta with the vertical. The height from the pivot to the plane of the circle is h, and the radius of the circle is r.](a30a0f5bc00fe96eb86992f6c81b4515_img.jpg)

Diagram for Fig. 8.33: A mass hanging from a string of length l, swinging in a horizontal circle. The string makes an angle theta with the vertical. The height from the pivot to the plane of the circle is h, and the radius of the circle is r.

Fig. 8.33

#### 8.14. Oscillating cylinders \*\*

A hollow cylinder of mass  $M_1$  and radius  $R_1$  rolls without slipping on the inside surface of another hollow cylinder of mass  $M_2$  and radius  $R_2$ . Assume  $R_1 \ll R_2$ . Both axes are horizontal, and the larger cylinder is free to rotate about its axis. What is the frequency of small oscillations?

#### 8.15. Lengthening the string \*\*

A mass hangs from a massless string and swings around in a horizontal circle, as shown in Fig. 8.33. The length of the string is then very slowly increased (or decreased). Let  $\theta$ ,  $\ell$ ,  $r$ , and  $h$  be defined as shown.

- Assuming that  $\theta$  is very small, how does  $r$  depend on  $\ell$ ?
- Assuming that  $\theta$  is very close to  $\pi/2$ , how does  $h$  depend on  $\ell$ ?

![Diagram for Fig. 8.34: Three identical cylinders of radius R arranged in a triangle. Two are on the bottom, touching each other and the ground. The third is on top, touching both bottom cylinders.](a8a7a1562d60c220d53a527c2e6ae6ec_img.jpg)

Diagram for Fig. 8.34: Three identical cylinders of radius R arranged in a triangle. Two are on the bottom, touching each other and the ground. The third is on top, touching both bottom cylinders.

Fig. 8.34

#### 8.16. A triangle of cylinders \*\*\*

Three identical cylinders with moments of inertia  $I = \beta mR^2$  are situated in a triangle as shown in Fig. 8.34. Find the initial downward acceleration of the top cylinder for the following two cases. Which case has a larger acceleration?

- There is friction between the bottom two cylinders and the ground (so they roll without slipping), but there is no friction between any of the cylinders.
- There is no friction between the bottom two cylinders and the ground, but there is friction between the cylinders (so they don't slip with respect to each other).

![Diagram for Fig. 8.35: A chimney modeled as a stack of boards, tilted at an angle from its vertical position. An arrow indicates the direction of toppling.](39c2b009aa0e84afc874770a5a9d611a_img.jpg)

Diagram for Fig. 8.35: A chimney modeled as a stack of boards, tilted at an angle from its vertical position. An arrow indicates the direction of toppling.

Fig. 8.35

#### 8.17. Falling chimney \*\*\*\*

A chimney initially stands upright. It is given a tiny kick, and it topples over. At what point along its length is it most likely to break? In doing this problem, work with the following two-dimensional simplified model of a chimney. Assume that the chimney consists of boards stacked on top of each other, and that each board is attached to the two adjacent ones with tiny rods at each end (see Fig. 8.35). The goal is to determine which rod in the chimney achieves the maximum tension. Work in the

approximation where the width of the chimney is very small compared with the height.

### Section 8.5: Collisions

#### 8.18. Ball hitting stick \*\*

A ball of mass  $M$  collides with a stick with moment of inertia  $I = \beta ml^2$  (relative to its center, which is its CM). The ball is initially traveling at speed  $V_0$  perpendicular to the stick. The ball strikes the stick at a distance  $d$  from the center (see Fig. 8.36). The collision is elastic. Find the resulting translational and rotational speeds of the stick, and also the resulting speed of the ball.

![Diagram for Problem 8.18 showing a ball of mass M moving with velocity V_0 towards a vertical stick of mass m and length l. The stick has a moment of inertia I = beta ml^2 about its center. The ball strikes the stick at a distance d from the center.](a4fd006c28506c27bb566b0e07c503a6_img.jpg)

The diagram shows a ball of mass  $M$  moving with velocity  $V_0$  towards a vertical stick. The stick has mass  $m$ , length  $l$ , and moment of inertia  $I = \beta ml^2$  about its center. The ball strikes the stick at a distance  $d$  from the center. The stick is oriented vertically, and the ball is moving horizontally towards it.

Diagram for Problem 8.18 showing a ball of mass M moving with velocity V\_0 towards a vertical stick of mass m and length l. The stick has a moment of inertia I = beta ml^2 about its center. The ball strikes the stick at a distance d from the center.

Fig. 8.36

#### 8.19. A ball and stick theorem \*\*

Consider the setup in Problem 8.18. Show that the relative speed of the ball and the point of contact on the stick is the same before and immediately after the collision. (This result is analogous to the “relative speed” result for a 1-D collision, Theorem 5.3 in Section 5.7.1.)

### Section 8.6: Angular impulse

#### 8.20. The superball \*\*

A ball with radius  $R$  and  $I = (2/5)mR^2$  is thrown through the air. It spins around the axis perpendicular to the (vertical) plane of the motion. Call this the  $x$ - $y$  plane. The ball bounces off a floor without slipping during the time of contact. Assume that the collision is elastic, and that the magnitude of the vertical  $v_y$  is the same before and after the bounce. Show that  $v'_x$  and  $\omega'$  after the bounce are related to  $v_x$  and  $\omega$  before the bounce by

$$\begin{pmatrix} v'_x \\ R\omega' \end{pmatrix} = \frac{1}{7} \begin{pmatrix} 3 & -4 \\ -10 & -3 \end{pmatrix} \begin{pmatrix} v_x \\ R\omega \end{pmatrix}, \quad (8.62)$$

where positive  $v_x$  is to the right, and positive  $\omega$  is counterclockwise.

#### 8.21. Many bounces \*

Using the result of Problem 8.20, describe what happens over the course of many superball bounces.

#### 8.22. Rolling over a bump \*\*

A ball with radius  $R$  and moment of inertia  $I = (2/5)mR^2$  rolls with speed  $V_0$  without slipping on the ground. It encounters a step of height  $h$  and rolls up over it. Assume that the ball sticks to the corner of

the step briefly (until the center of the ball is directly above the corner). Show that if the ball is to climb over the step, then  $V_0$  must satisfy

$$V_0 \geq \sqrt{\frac{10gh}{7}} \left(1 - \frac{5h}{7R}\right)^{-1}. \quad (8.63)$$

#### 8.23. Falling toast \*\*

After buttering your toast (assumed to be a uniform rigid square of side length  $\ell$ , for the sake of having a doable problem) one morning and holding it in a horizontal position with buttered side up, you accidentally drop it from a height  $H$  above a counter, which itself is a height  $h$  above the ground. The toast is oriented “parallel” to the counter, and as it falls, one edge barely clips the counter (elastically), causing the toast to spin. What value of  $H$ , in terms of  $h$  and  $\ell$ , yields the unfortunate scenario where the toast makes half of a revolution, landing buttered side down on the floor? There is a special value of  $\ell$  in terms of  $h$ . What is it, and why is it special?

![Diagram of a ball of radius R moving with initial velocity V_0 to the right on a horizontal surface.](d0e39224bc29107943e14d2fe2fe141e_img.jpg)

A diagram showing a sphere of radius  $R$  on a horizontal surface. An arrow labeled  $V_0$  points to the right from the center of the sphere, indicating its initial velocity.

Diagram of a ball of radius R moving with initial velocity V\_0 to the right on a horizontal surface.

Fig. 8.37

#### 8.24. Sliding to rolling \*\*

A ball initially slides without rotating on a horizontal surface with friction (see Fig. 8.37). The initial speed is  $V_0$ , and the moment of inertia around the center is  $I = \beta mR^2$ .

- Without knowing anything about the nature of the friction force, find the speed of the ball when it begins to roll without slipping. Also, find the kinetic energy lost while sliding.
- Now consider the special case where the coefficient of kinetic friction is  $\mu$ , independent of position. At what time, and at what distance, does the ball begin to roll without slipping? Verify that the work done by friction equals the energy loss calculated in part (a). (Be careful on this.)

#### 8.25. Lots of sticks \*\*\*

Consider a collection of rigid sticks of length  $2r$ , masses  $m_i$ , and moments of inertia  $\beta m_i r^2$ , with  $m_1 \gg m_2 \gg m_3 \gg \dots$ . The CM of each stick is located at its center. The sticks are placed on a horizontal frictionless surface, as shown in Fig. 8.38. The ends overlap a tiny distance in the  $y$  direction and are a tiny distance apart in the  $x$  direction. The first (heaviest) stick is given an instantaneous blow (as shown) which causes it to translate and rotate. The first stick will strike the second stick, which will then strike the third stick, and so on. Assume that all the collisions are elastic. Depending on the size of  $\beta$ , the speed of the  $n$ th stick will either (1) approach zero, (2) approach infinity, or

![Diagram showing a vertical stack of sticks labeled m1, m2, m3, m4, ... with length 2r. An arrow points to the right from the top of the first stick.](3cf2777c43d38f29958d43516a87273f_img.jpg)

A diagram showing a vertical stack of sticks. The sticks are labeled  $m_1, m_2, m_3, m_4, \dots$  from top to bottom. Each stick has a length of  $2r$ . An arrow points to the right from the top of the first stick ( $m_1$ ), indicating an initial impulse.

Diagram showing a vertical stack of sticks labeled m1, m2, m3, m4, ... with length 2r. An arrow points to the right from the top of the first stick.

Fig. 8.38

(3) be independent of  $n$ , as  $n \rightarrow \infty$ . Show that the special value of  $\beta$  corresponding to the third of these three scenarios is  $\beta = 1/3$ , which happens to correspond to a uniform stick.

### 8.8 Exercises

### Section 8.1: Pancake object in $x$ - $y$ plane

#### 8.26. Swinging stick \*\*

A uniform stick of length  $L$  is pivoted at its bottom end and is initially held vertical. It is given an infinitesimal kick, and it swings down around the pivot. After three-quarters of a turn (in the horizontal position shown in Fig. 8.39), the pivot is somehow vaporized, and the stick flies freely up in the air. What is the maximum height of the center of the stick in the resulting motion? At what angle is the stick tilted when the center reaches this maximum height?

![Diagram for Fig. 8.39: A uniform stick of length L is pivoted at its bottom end. It is shown in a horizontal position, indicated by a dashed line. An arrow points to the right from the top of the stick, indicating its initial motion.](6b9f2506a9309f03372daee35da3f7f1_img.jpg)

Diagram for Fig. 8.39: A uniform stick of length L is pivoted at its bottom end. It is shown in a horizontal position, indicated by a dashed line. An arrow points to the right from the top of the stick, indicating its initial motion.

Fig. 8.39

#### 8.27. Atwood's with a cylinder \*\*

A massless string of negligible thickness is wrapped around a uniform cylinder of mass  $m$  and radius  $r$ . The string passes up over a massless pulley and is tied to a block of mass  $m$  at its other end, as shown in Fig. 8.40. The system is released from rest. What are the accelerations of the block and the cylinder? Assume that the string does not slip with respect to the cylinder. Use conservation of energy (after applying a quick  $F = ma$  argument to show that the two objects move downward with the same acceleration).

![Diagram for Fig. 8.40: A massless string is wrapped around a uniform cylinder of mass m and radius r. The string passes over a massless pulley and is tied to a block of mass m. The cylinder is on the left, and the block is on the right.](6ce5a0f9acd9dfbbbea6f1f743bbc006_img.jpg)

Diagram for Fig. 8.40: A massless string is wrapped around a uniform cylinder of mass m and radius r. The string passes over a massless pulley and is tied to a block of mass m. The cylinder is on the left, and the block is on the right.

Fig. 8.40

#### 8.28. Board and cylinders \*\*

A board lies on top of two uniform cylinders that lie on a fixed plane inclined at an angle  $\theta$ , as shown in Fig. 8.41. The board has mass  $m$ , and each of the cylinders has mass  $m/2$ . The system is released from rest. If there is no slipping between any of the surfaces, what is the acceleration of the board? Use conservation of energy.

![Diagram for Fig. 8.41: A board of mass m lies on top of two uniform cylinders, each of mass m/2. The cylinders are on a fixed plane inclined at an angle theta. The board is shown in a horizontal position relative to the incline.](13de5d06fa60611512fe515a3ea4a721_img.jpg)

Diagram for Fig. 8.41: A board of mass m lies on top of two uniform cylinders, each of mass m/2. The cylinders are on a fixed plane inclined at an angle theta. The board is shown in a horizontal position relative to the incline.

Fig. 8.41

#### 8.29. Moving plane \*\*\*

A ball of mass  $m$  and moment of inertia  $I = \beta mr^2$  is held motionless on a plane of mass  $M$  and angle of inclination  $\theta$  (see Fig. 8.42). The plane rests on a frictionless horizontal surface. The ball is released. Assuming that it rolls without slipping on the plane, what is the horizontal acceleration of the plane? *Hint:* You might want to do Problem 3.8 first. But as with all the exercises in this section, use conservation of energy instead of force and torque; this problem gets extremely messy with the latter strategy.

![Diagram for Fig. 8.42: A ball of mass m is held motionless on a plane of mass M and angle of inclination theta. The plane rests on a frictionless horizontal surface. An arrow points to the left from the bottom of the plane, indicating its motion.](ed17a3bb4d2e40a8ac8fd6c5d0cc8ae8_img.jpg)

Diagram for Fig. 8.42: A ball of mass m is held motionless on a plane of mass M and angle of inclination theta. The plane rests on a frictionless horizontal surface. An arrow points to the left from the bottom of the plane, indicating its motion.

Fig. 8.42

### *Section 8.2: Nonplanar objects*

#### **8.30. Semicircle CM \***

A wire is bent into a semicircle of radius  $R$ . Find the CM.

#### **8.31. Hemisphere CM \***

Find the CM of a solid hemisphere.

### *Section 8.3: Calculating moments of inertia*

#### **8.32. A cone \***

Find the moment of inertia of a solid cone (mass  $M$ , base radius  $R$ ) around its symmetry axis.

#### **8.33. A sphere \***

Find the moment of inertia of a solid sphere (mass  $M$ , radius  $R$ ) around a diameter. Do this by slicing the sphere into disks.

#### **8.34. A triangle, the slick way \*\***

In the spirit of Section 8.3.2, find the moment of inertia of a uniform equilateral triangle of mass  $m$  and side  $\ell$ , around a line joining a vertex and the opposite side; see Fig. 8.43.

![Diagram of an equilateral triangle with side length l. A vertical line passes through the top vertex and the midpoint of the base, representing the axis of rotation. A dot on this line represents the center of mass.](1733b006413ee10b993571e60406ac0d_img.jpg)

Diagram of an equilateral triangle with side length l. A vertical line passes through the top vertex and the midpoint of the base, representing the axis of rotation. A dot on this line represents the center of mass.

Fig. 8.43

#### **8.35. Fractal triangle \*\***

Take an equilateral triangle of side  $\ell$ , and remove the “middle” triangle ( $1/4$  of the area). Then remove the “middle” triangle from each of the remaining three triangles, and so on, forever. Let the final fractal object have mass  $m$ . In the spirit of Section 8.3.2, find the moment of inertia around a line joining a vertex and the opposite side; see Fig. 8.44.

![Diagram of a fractal triangle (Sierpinski triangle) with side length l. A vertical line passes through the top vertex and the midpoint of the base, representing the axis of rotation.](53b7399427528182ae5953889d8d6502_img.jpg)

Diagram of a fractal triangle (Sierpinski triangle) with side length l. A vertical line passes through the top vertex and the midpoint of the base, representing the axis of rotation.

Fig. 8.44

### *Section 8.4: Torque*

#### **8.36. Swinging your arms \***

You are standing on the edge of a step on some stairs, facing up the stairs. You feel yourself starting to fall backward, so you start swinging your arms around in vertical circles, like a windmill. This is what people tend to do in such a situation, but does it actually help you not to fall, or does it simply make you look silly? Explain your reasoning.

#### **8.37. Rolling down the plane \***

A ball with moment of inertia  $\beta mr^2$  rolls without slipping down a plane inclined at an angle  $\theta$ . What is its linear acceleration?

#### **8.38. Coin on a plane \***

A uniform coin rolls down a plane inclined at an angle  $\theta$ . If the coefficient of static friction between the coin and the plane is  $\mu$ , what is the largest angle  $\theta$  for which the coin doesn't slip?

#### **8.39. Accelerating plane \***

A ball with  $I = (2/5)MR^2$  is placed on a plane inclined at an angle  $\theta$ . The plane is accelerated upwards (along its direction) with acceleration  $a$ ; see Fig. 8.45. For what value of  $a$  does the CM of the ball not move? Assume that there is sufficient friction so that the ball doesn't slip with respect to the plane.

![Diagram for Fig. 8.45: A ball on an inclined plane. The plane is tilted at an angle theta to the horizontal. An arrow labeled 'a' points up the incline, indicating the acceleration of the plane.](52c04890615df626ed34e8986525e11a_img.jpg)

Diagram for Fig. 8.45: A ball on an inclined plane. The plane is tilted at an angle theta to the horizontal. An arrow labeled 'a' points up the incline, indicating the acceleration of the plane.

Fig. 8.45

#### **8.40. Bowling ball on paper \***

A bowling ball sits on a piece of paper on the floor. You grab the paper and pull it horizontally along the floor, with acceleration  $a_0$ . What is the acceleration of the center of the ball? Assume that the ball does not slip with respect to the paper.

![Diagram for Fig. 8.46: A ball of mass M is on a horizontal surface. A spring with spring constant k is attached to the left side of the ball. The ball is in contact with a vertical wall on the left.](7802ef76251a5db7970ad0362400e34c_img.jpg)

Diagram for Fig. 8.46: A ball of mass M is on a horizontal surface. A spring with spring constant k is attached to the left side of the ball. The ball is in contact with a vertical wall on the left.

Fig. 8.46

#### **8.41. Spring and cylinder \***

The axle of a solid cylinder of mass  $m$  and radius  $r$  is connected to a spring with spring constant  $k$ , as shown in Fig. 8.46. If the cylinder rolls without slipping, what is the frequency of the oscillations?

#### **8.42. Falling quickly \***

A massless stick of length  $L$  is pivoted at one end and has a mass  $m$  attached to its other end. It is held in a horizontal position, as shown in Fig. 8.47. Where should a second mass  $m$  be attached to the stick, so that the stick falls as fast as possible when dropped?

![Diagram for Fig. 8.47: A horizontal stick of length L is pivoted at its left end. A mass m is attached to the right end. A second mass m is attached at a distance x from the pivot. A curved arrow indicates the stick is about to rotate downwards.](c4fb31cb56e3e57e28022664eecaacd3_img.jpg)

Diagram for Fig. 8.47: A horizontal stick of length L is pivoted at its left end. A mass m is attached to the right end. A second mass m is attached at a distance x from the pivot. A curved arrow indicates the stick is about to rotate downwards.

Fig. 8.47

#### **8.43. Maximum frequency \***

A pendulum is made of a uniform stick of length  $L$ . It is allowed to swing in a vertical plane. Where should the pivot be placed on the stick so that the frequency of (small) oscillations is maximum?

#### **8.44. Massive pulley \***

Solve Problem 8.1 again, but now use force and torque instead of conservation of energy.

#### **8.45. Atwood's with a cylinder \*\***

Solve Exercise 8.27 again, but now use force and torque instead of conservation of energy.

#### **8.46. Board and cylinders \*\***

Solve Exercise 8.28 again, but now use force and torque instead of conservation of energy.

![Diagram of a spool on a horizontal surface. The spool has an inner radius r and an outer radius R. A string is attached to the inner axle and is pulled at an angle theta above the horizontal. The mass of the spool is m. The string tension is T.](754ab7fd6e054072c7bb36692ee70740_img.jpg)

Diagram of a spool on a horizontal surface. The spool has an inner radius r and an outer radius R. A string is attached to the inner axle and is pulled at an angle theta above the horizontal. The mass of the spool is m. The string tension is T.

Fig. 8.48

![Diagram of a coin of radius R on a horizontal surface with coefficient of kinetic friction mu. The coin is moving to the right with speed v and has an angular speed omega (indicated by a curved arrow).](94223c6808d936affb565b61fed7ea93_img.jpg)

Diagram of a coin of radius R on a horizontal surface with coefficient of kinetic friction mu. The coin is moving to the right with speed v and has an angular speed omega (indicated by a curved arrow).

Fig. 8.49

#### **8.47. The spool \*\***

A spool of mass  $m$  and moment of inertia  $I$  is free to roll without slipping on a table. It has an inner radius  $r$ , and an outer radius  $R$ . If you pull on the string with tension  $T$  at an angle  $\theta$  (see Fig. 8.48), what is the acceleration of the spool? Which way does it move?

#### **8.48. Stopping the coin \*\***

A coin stands vertically on a table. It is projected forward (in the plane of itself) with speed  $v$  and angular speed  $\omega$ , as shown in Fig. 8.49. The coefficient of kinetic friction between the coin and the table is  $\mu$ . What should  $v$  and  $\omega$  be so that the coin comes to rest (both translationally and rotationally) a distance  $d$  from where it started?

#### **8.49. Measuring $g$ \*\***

- Consider an extended pendulum whose CM is a distance  $\ell$  from the pivot, and whose moment of inertia around the pivot is  $I$ . Show that the frequency of small oscillations is  $\omega = \sqrt{mg\ell/I}$ , which gives  $T = 2\pi/\omega = 2\pi\sqrt{I/mg\ell}$ , and hence  $g = 4\pi^2 I/(m\ell T^2)$ . Therefore, by measuring  $I$ ,  $m$ ,  $\ell$ , and  $T$ , you can determine  $g$ . However, if the pendulum has an odd shape, it may be difficult to determine  $I$ . Consider, then, the following alternative method of measuring  $g$ .
- For simplicity, assume that the pendulum is planar. Pick an arbitrary point as the pivot and measure the period,  $T$ , of small oscillations. Then with the pendulum at rest, draw a vertical line through this pivot. By trial and error, find another pivot point on this line on the *same* side of the CM<sup>9</sup> (you may need to extend the line with a massless extension) that yields the same period  $T$ . Let  $L$  be the sum of the lengths from these two points to the CM.<sup>10</sup> Show that  $g$  is given by  $g = 4\pi^2 L/T^2$ , which is independent of  $m$  and  $I$ .

#### **8.50. Pulling a cylinder \*\***

A solid cylinder of mass  $m$  and radius  $r$  lies flat on a frictionless horizontal table, with a massless string running halfway around it, as shown in

<sup>9</sup> The CM can be found by hanging the pendulum from a point not on the drawn line, and then drawing a vertical line through this point. The intersection of the two lines is the CM.

<sup>10</sup> There are also two points on the other side of the CM that yield the same period (except in the special case where the two points coincide and produce the minimum period, as in Exercise 8.43, but don't worry about this). These two other points are the same distances from the CM as the original two points, as you can show. So if you happen to find all four points, you can obtain  $L$  by instead measuring the distance from the "inside" point on one side to the "outside" point on the other. This method doesn't require knowing the location of the CM.

Fig. 8.50. A mass also of mass  $m$  is attached to one end of the string, and you pull on the other end with a force  $T$ . The circumference of the cylinder is sufficiently rough so that the string does not slip with respect to it. What is the acceleration of the mass  $m$  attached to the end of the string?

![Diagram for Fig. 8.50: A top view of a cylinder of mass m. A string is wrapped around it, with one end attached to a mass m and the other end being pulled with a force T to the right. A dashed horizontal line passes through the center of the cylinder.](ba3bdb0b1eef8614e28a1b098400e88b_img.jpg)

Diagram for Fig. 8.50: A top view of a cylinder of mass m. A string is wrapped around it, with one end attached to a mass m and the other end being pulled with a force T to the right. A dashed horizontal line passes through the center of the cylinder.

Fig. 8.50

#### 8.51. Coin and plank \*\*

A coin of mass  $M$  and radius  $R$  stands vertically on the right end of a horizontal plank of mass  $M$  and length  $L$ , as shown in Fig. 8.51. The system starts at rest. The plank is then pulled to the right with a constant force  $F$ . Assume that the coin does not slip with respect to the plank. What are the accelerations of the plank and coin? How far to the right does the coin move by the time the left end of the plank reaches it?

![Diagram for Fig. 8.51: A side view of a coin of mass m and radius R standing vertically on the right end of a horizontal plank of mass m and length L. A force F is applied to the right at the right end of the plank.](32c80990de6c8cd52ad40643293b547b_img.jpg)

Diagram for Fig. 8.51: A side view of a coin of mass m and radius R standing vertically on the right end of a horizontal plank of mass m and length L. A force F is applied to the right at the right end of the plank.

Fig. 8.51

#### 8.52. Cylinder, board, and spring \*\*

A board of mass  $m$ , which is free to slide on a frictionless floor, is connected by a spring (with spring constant  $k$ ) to a wall. A cylinder, also of mass  $m$  (and  $I = mR^2/2$ ), rests on top of the board, as shown in Fig. 8.52, and is free to roll without slipping on the board. If the board and the cylinder are pulled some distance to the left and then released from rest, what is the frequency of the resulting oscillatory motion?

![Diagram for Fig. 8.52: A side view of a cylinder of mass m resting on a board of mass m. The board is on a frictionless floor and is connected to a wall on the right by a spring with spring constant k.](3e7adcd0abaade8cf523e6b1231047e8_img.jpg)

Diagram for Fig. 8.52: A side view of a cylinder of mass m resting on a board of mass m. The board is on a frictionless floor and is connected to a wall on the right by a spring with spring constant k.

Fig. 8.52

#### 8.53. Swirling around a cone \*\*

A fixed hollow frictionless cone is positioned with its tip pointing down. A particle is released from rest on the inside surface. After it has slid halfway down to the tip, it bounces elastically off a platform. The platform is positioned at a  $45^\circ$  angle along the surface of the cone, so the particle ends up being deflected horizontally along the surface (in other words, into the page in Fig. 8.53). The particle then swirls up and around the cone before coming down. Measured from the tip of the cone, show that the ratio of the particle's maximum swirling height to the height of the platform is  $(\sqrt{5} + 1)/2$ , which just happens to be the golden ratio.

![Diagram for Fig. 8.53: A side view of a cone with its tip pointing down. A platform is positioned at a 45-degree angle along the surface. A particle is shown at the platform, with an arrow indicating it is deflected horizontally into the page.](9d3fbe11812ec1af8f944e468b62d057_img.jpg)

Diagram for Fig. 8.53: A side view of a cone with its tip pointing down. A platform is positioned at a 45-degree angle along the surface. A particle is shown at the platform, with an arrow indicating it is deflected horizontally into the page.

Fig. 8.53

#### 8.54. Raising a hoop \*\*

A bead of mass  $m$  is positioned at the top of a frictionless hoop of mass  $M$  and radius  $R$ , which stands vertically on the ground. A wall touches the hoop on its left, and a short wall of height  $R$  touches the hoop on its right, as shown in Fig. 8.54. All surfaces are frictionless. The bead is given a tiny kick, and it slides down the hoop, as shown. What is the largest value of  $m/M$  for which the hoop never rises up off the ground? *Note:* It's possible to solve this problem by using only force, but solve it here by using torque.

![Diagram for Fig. 8.54: A side view of a hoop of mass M and radius R standing vertically on the ground. A bead of mass m is at the top of the hoop. A wall is on the left, and a short wall of height R is on the right. An arrow indicates the bead is sliding down the hoop.](c6b97b8864ba04e0f3c8986bfe941aeb_img.jpg)

Diagram for Fig. 8.54: A side view of a hoop of mass M and radius R standing vertically on the ground. A bead of mass m is at the top of the hoop. A wall is on the left, and a short wall of height R is on the right. An arrow indicates the bead is sliding down the hoop.

Fig. 8.54

![Diagram for Fig. 8.55: A block of mass m and a cylinder of mass m on an inclined plane at angle theta. The block is on top of the cylinder. The coefficient of kinetic friction between the block's right face and the cylinder is mu = 1. The block's bottom face is in contact with the plane.](1233143556c2b6abb9fbf37c207cc621_img.jpg)

Diagram for Fig. 8.55: A block of mass m and a cylinder of mass m on an inclined plane at angle theta. The block is on top of the cylinder. The coefficient of kinetic friction between the block's right face and the cylinder is mu = 1. The block's bottom face is in contact with the plane.

Fig. 8.55

#### **8.55. Block and cylinder \*\***

A block and a cylinder (with  $I = \beta mR^2$ ), both of mass  $m$ , lie on a plane (inclined at an angle  $\theta$ ), touching each other as shown in Fig. 8.55. There is sufficient friction between the cylinder and the plane so that it rolls without slipping. But the bottom of the block is coated with grease, so there is no friction between it and the plane. However, there is a coefficient of kinetic friction  $\mu = 1$  between the block's right face and the cylinder. What is the acceleration of the block? How does your answer compare with the result for a lone cylinder rolling down a plane? Assume that  $\theta$  is small enough so that the block's bottom face remains in contact with the plane at all times; what is the condition on  $\theta$  for which this is true?

![Diagram for Fig. 8.56: A uniform stick of length L pivoted at one end on a horizontal rail. The stick is at an angle theta_0 with the vertical dashed line. An arrow indicates it is swinging down.](659635b363330d196e61c77d3b7a2d94_img.jpg)

Diagram for Fig. 8.56: A uniform stick of length L pivoted at one end on a horizontal rail. The stick is at an angle theta\_0 with the vertical dashed line. An arrow indicates it is swinging down.

Fig. 8.56

#### **8.56. Falling and sliding stick \*\*\***

One end of a uniform stick is attached to a pivot, and the pivot is free to slide along a frictionless horizontal rail. The stick is held at an initial angle  $\theta_0$  with respect to the (upward) vertical direction and then released; see Fig. 8.56. Assume that the stick can somehow swing down below the horizontal position without running into the rail (perhaps by having the pivot attached to the side of the rail, so that the stick is shifted horizontally a small distance from the rail).

- Show that when the stick is horizontal, the normal force  $N$  from the rail equals  $mg/4$ , independent of  $\theta_0$ .
- If  $\theta_0 = 0$  (a tiny kick is allowed), show that  $N = 13mg$  when the stick is at the bottom of its motion (at  $\theta = \pi$ ).
- If  $\theta_0 = 0$ , show that the minimum  $N$  occurs at  $\theta \approx 61.5^\circ$  and that the value is  $N_{\min} \approx (0.165)mg$ . You will obtain a cubic; feel free to solve it numerically.

![Diagram for Fig. 8.57: A tower of cylinders on a moving plank. The plank is on a horizontal surface and has an acceleration a to the right. The tower consists of two columns of cylinders, each column having four cylinders shown, with vertical dots indicating the tower continues infinitely upwards. The cylinders are in contact with the plank and with each other.](35e784d6d3ccf128922e5cf56e292481_img.jpg)

Diagram for Fig. 8.57: A tower of cylinders on a moving plank. The plank is on a horizontal surface and has an acceleration a to the right. The tower consists of two columns of cylinders, each column having four cylinders shown, with vertical dots indicating the tower continues infinitely upwards. The cylinders are in contact with the plank and with each other.

Fig. 8.57

#### **8.57. Tower of cylinders \*\*\*\***

Consider the infinitely tall system of massless planks and identical massive cylinders shown in Fig. 8.57. The moment of inertia of the cylinders is  $I = MR^2/2$ . There are two cylinders at each level, and the number of levels is infinite. The cylinders do not slip with respect to the planks, but the bottom plank is free to slide on a table. If you pull on the bottom plank so that it accelerates horizontally with acceleration  $a$ , what is the horizontal acceleration of the bottom row of cylinders?

### *Section 8.5: Collisions*

#### **8.58. Pendulum collision \***

A stick of mass  $m$  and length  $\ell$  is pivoted at an end. It is held horizontal and then released. It swings down, and when it is vertical the free end

elastically collides with a ball, as shown in Fig. 8.58. (Assume that the ball is initially held at rest and then released a split second before the stick strikes it.) If the stick loses half of its angular velocity during the collision, what is the mass of the ball? What is the speed of the ball right after the collision?

![Diagram for Fig. 8.58: A stick of mass m and length l is pivoted at one end. A ball is at the other end. A dashed line labeled 'start' is horizontal. A curved arrow indicates rotation from the start position.](c64175e221581d1a85d5bb6d7f9aeb8a_img.jpg)

Diagram for Fig. 8.58: A stick of mass m and length l is pivoted at one end. A ball is at the other end. A dashed line labeled 'start' is horizontal. A curved arrow indicates rotation from the start position.

Fig. 8.58

#### **8.59. No final rotation \***

A stick of mass  $m$  and length  $\ell$  spins around on a frictionless horizontal table, with its CM at rest (but not fixed by a pivot). A ball of mass  $M$  is placed on the table, and one end of the stick collides elastically with it, as shown in Fig. 8.59. What should  $M$  be so that after the collision the stick has translational motion, but no rotational motion?

![Diagram for Fig. 8.59: A top view of a stick of mass m and length l. A ball of mass M is at the top end. A curved arrow indicates rotation.](6418bd965e6519bb8683c11cd7fe1d21_img.jpg)

Diagram for Fig. 8.59: A top view of a stick of mass m and length l. A ball of mass M is at the top end. A curved arrow indicates rotation.

Fig. 8.59

#### **8.60. Same final speeds \***

A stick slides perpendicular to itself (without rotating) across a frictionless horizontal table and collides elastically at one of its ends with a stationary ball. Both the stick and the ball have mass  $m$ . The mass of the stick is distributed in such a way that the moment of inertia around the CM (which is at the center of the stick) is  $I = Am\ell^2$ , where  $A$  is some number. What should  $A$  be so that the ball moves at the same speed as the center of the stick after the collision?

![Diagram for Fig. 8.60: A top view of a mass M moving with velocity V_0 towards a stationary mass m. A vertical line of length l connects the two masses.](9b8df73ca079ef4e06804ac4145b2e3a_img.jpg)

Diagram for Fig. 8.60: A top view of a mass M moving with velocity V\_0 towards a stationary mass m. A vertical line of length l connects the two masses.

Fig. 8.60

#### **8.61. Perpendicular deflection \*\***

A mass  $M$  moves at speed  $V_0$  perpendicular to a dumbbell at rest on a frictionless horizontal table, as shown in Fig. 8.60. The dumbbell consists of two masses  $m$  at the ends of a massless rod of length  $\ell$ . The mass  $M$  collides elastically with one of the masses (not head-on), and afterwards it is observed that  $M$  moves perpendicular to its original direction, with speed  $u$ . What is  $u$  in terms of  $V_0$ ,  $m$ , and  $M$ ? What is the smallest value of  $m$  (in terms of  $M$ ) for which this scenario is possible?

#### **8.62. Glancing off a stick \*\***

A frictionless stick of mass  $m$  and length  $\ell$  lies at rest on a frictionless horizontal table. A mass  $km$  (where  $k$  is some number) moves with speed  $v_0$  at a  $45^\circ$  angle to the stick and collides elastically with it very close to an end; see Fig. 8.61. What should  $k$  be so that the mass ends up moving in the  $y$ -direction, as shown? *Hint:* Remember that the stick is frictionless.

![Diagram for Fig. 8.61: A top view of a mass km moving with velocity v_0 at a 45-degree angle to a stick of mass m. A dashed line indicates the final velocity of the mass is in the y-direction.](c1522b8d646f2cf79e1728599f4eed89_img.jpg)

Diagram for Fig. 8.61: A top view of a mass km moving with velocity v\_0 at a 45-degree angle to a stick of mass m. A dashed line indicates the final velocity of the mass is in the y-direction.

Fig. 8.61

#### **8.63. Sticking to a dumbbell \***

A mass  $m$  moves at speed  $v$  perpendicular to a dumbbell at rest on a frictionless horizontal table, as shown in Fig. 8.62. The dumbbell consists of two masses also of mass  $m$  at the ends of a massless rod of length  $\ell$ . The moving mass collides and sticks to one of the masses.

![Diagram for Fig. 8.62: A top view of a collision. A point mass m with velocity v moves towards a vertical rod of length l and mass m. The rod has a pivot at its top end.](5be3035ed40d39fd97a0f564a2c46879_img.jpg)

Diagram for Fig. 8.62: A top view of a collision. A point mass m with velocity v moves towards a vertical rod of length l and mass m. The rod has a pivot at its top end.

Fig. 8.62

![Diagram for Fig. 8.63: A top view of a collision. A rod of length l and mass m rotates with angular velocity ω about a pivot at its top end. It is moving towards a vertical rod of length 2R and mass m. The distance between the pivot and the second rod is x. The text 'no pivot' is written above the second rod.](136595a246d5a79278dbb8de4b67bd10_img.jpg)

Diagram for Fig. 8.63: A top view of a collision. A rod of length l and mass m rotates with angular velocity ω about a pivot at its top end. It is moving towards a vertical rod of length 2R and mass m. The distance between the pivot and the second rod is x. The text 'no pivot' is written above the second rod.

Fig. 8.63

![Diagram for Fig. 8.64: A top view of a collision. A circular puck of radius R and mass m moves with velocity v to the right. It is rotating with angular velocity ω clockwise. It is approaching a vertical rod of length 2R and mass m, which is initially at rest.](fb97259128e5e287c802878a23d063b3_img.jpg)

Diagram for Fig. 8.64: A top view of a collision. A circular puck of radius R and mass m moves with velocity v to the right. It is rotating with angular velocity ω clockwise. It is approaching a vertical rod of length 2R and mass m, which is initially at rest.

Fig. 8.64

![Diagram for Fig. 8.65: A side view of a pencil rolling down an inclined plane. The plane is inclined at an angle θ. The pencil is represented as a wheel with six spokes of length r.](0a6544d992194c78cf9612936fd4d73e_img.jpg)

Diagram for Fig. 8.65: A side view of a pencil rolling down an inclined plane. The plane is inclined at an angle θ. The pencil is represented as a wheel with six spokes of length r.

Fig. 8.65

What is the resulting  $\omega$  of the system? What is the velocity of the end of the rod that has the two masses on it, after the rod has made one half of a revolution?

#### 8.64. Colliding sticks \*\*

On a frictionless horizontal table, a stick of mass  $m$  and length  $\ell$  spins around a pivot at one of its ends with angular frequency  $\omega$ . It collides and sticks to an identical stick, with an overlap length equal to  $x$ , as shown in Fig. 8.63. Immediately before the collision, the pivot is removed. What should  $x$  be so that after the collision the double-stick system has translational but no rotational motion?

#### 8.65. Lollipop \*\*

A hockey puck of mass  $m$  and radius  $R$  slides across frictionless ice, as shown in Fig. 8.64 (the view is from above). It has translational speed  $v$  to the right and rotational speed  $\omega$  clockwise. It grazes the “top” end of a rod of mass  $m$  and length  $2R$  which is initially at rest on the ice. It sticks to the rod, forming a rigid object that looks like a lollipop.

- In the special case of  $v = R\omega$ , what is the resulting angular speed of the lollipop?
- How much energy is lost during the collision? How do you explain the fact that energy is lost, given that the  $v = R\omega$  condition implies that the contact point on the puck touches the rod with zero relative speed (and thus doesn't crash into it, as is commonly the case with inelastic collisions)?
- Given  $\omega$ , show that  $v$  should equal  $6R\omega/5$  if you want the minimum amount of energy to be lost.

#### 8.66. Pencil on a plane \*\*\*\*

This exercise deals with the terminal velocity of a “pencil” rolling down a plane. To simplify things, we'll assume that the pencil has all its mass on its axis. And to avoid messy complications, we'll assume that the cross section of the pencil looks like a wheel with six equally spaced massless spokes and no rim (see Fig. 8.65).<sup>11</sup> Let the length of the spokes be  $r$ , and let the plane be inclined at an angle  $\theta$ . Assume that there is sufficient friction to prevent the spokes from slipping on the plane, and assume that the pencil does not bounce when a spoke hits the plane.

- Explain qualitatively why the pencil reaches a terminal (average) velocity, assuming that it remains in contact with the plane at all times.

<sup>11</sup> If the pencil instead looks like a hexagon with flat sides, then it is impossible to say how it behaves, because if the sides bow outward an infinitesimal amount then the system conserves energy, whereas if they bow inward an infinitesimal amount then it does not (for reasons you will figure out).

- (b) Assume that conditions have been set up so that the pencil eventually reaches a nonzero terminal (average) velocity, while remaining in contact with the plane at all times. Describe this terminal velocity. You may do this by stating the maximum speed of the axis in the limiting steady state.
- (c) What is the minimum value of  $\theta$  for which a nonzero terminal velocity exists? An initial kick to the pencil is allowed.
- (d) What is the maximum value of  $\theta$  for which the pencil remains in contact with the plane at all times? As a check on your answer, the difference between the answers in parts (c) and (d) is about  $5.09^\circ$ .

### Section 8.6: Angular impulse

#### 8.67. Striking a pool ball \*

At what height should you horizontally strike a pool ball so that it immediately rolls without slipping?

#### 8.68. Center of percussion \*

You hold one end of a uniform stick of length  $L$ . The stick is struck with a hammer. Where should this blow occur so that the end you are holding doesn't move (immediately after the blow)? In other words, where should the blow occur so that you don't feel a "sting" in your hand? This point is called the *center of percussion*.

#### 8.69. Another center of percussion \*

You hold the top vertex of a solid equilateral triangle of side length  $L$ . The plane of the triangle is vertical. It is struck with a hammer, somewhere along the vertical axis. Where should this blow occur so that the point you are holding doesn't move (immediately after the blow)? Use the fact that the moment of inertia about any axis through the CM of an equilateral triangle is  $mL^2/24$ .

#### 8.70. Not hitting the pole \*\*

A (possibly non-uniform) stick of mass  $m$  and length  $\ell$  lies on frictionless ice. Its midpoint (which is also its CM) touches a thin pole sticking out of the ice. One end of the stick is struck with a quick blow perpendicular to the stick, as shown in Fig. 8.66, so that the CM moves away from the pole. What is the minimum value of the stick's moment of inertia that allows the stick not to hit the pole?

#### 8.71. Pulling the paper \*\*

A ball sits at rest on a piece of paper on a table. You pull the paper in a straight line out from underneath the ball. You are free to pull the

![Diagram for problem 8.70 showing a stick of mass m and length l on frictionless ice. A pole is at the center of mass. A strike is applied to one end perpendicular to the stick.](9fec47648cee9503322c4ca787d76f4a_img.jpg)

(top view)

The diagram shows a vertical stick of length  $\ell$  and mass  $m$ . A dot at the center is labeled "pole". An arrow at the bottom end points to the right, labeled "strike".

Diagram for problem 8.70 showing a stick of mass m and length l on frictionless ice. A pole is at the center of mass. A strike is applied to one end perpendicular to the stick.

Fig. 8.66

paper in an arbitrary (straight line) manner, frontward or backward. You may even give it abrupt, jerky motions, so that the ball slips with respect to it. After the ball comes off the paper, it will eventually roll without slipping on the table. Show (and you are encouraged to experimentally verify this) that the ball in fact ends up at rest. (The generalization of this fact is given in Problem 9.29.) Is it possible to pull the paper in such a way that the ball ends up exactly where it started?

#### 8.72. Up, down, and twisting \*\*

A uniform stick is held horizontally and then released. At the same instant, one end is struck with a quick upwards blow. If the stick ends up horizontal when it returns to its original height, what are the possible values for the maximum height to which the center rises?

#### 8.73. Doing work \*\*

- A pencil of mass  $m$  and length  $\ell$  lies at rest on a frictionless table. You push on it at its midpoint (perpendicular to it), with a constant force  $F$  for a time  $t$ . Find the final speed and the distance traveled. Verify that the work you do equals the final kinetic energy.
- Assume that you apply the same force  $F$  for the same time  $t$  as above, but that you now apply it at one of the pencil's ends (perpendicular to the pencil). Assume that  $t$  is small, so that the pencil doesn't have much time to rotate (this means that you can assume that your force is always essentially perpendicular to the pencil, as far as the torque is concerned). Find the final CM speed, the final angular speed, and the distance your hand moves. Verify that the work you do equals the final kinetic energy.

#### 8.74. Bouncing between bricks \*\*\*

A stick of length  $\ell$  slides on frictionless ice. It bounces elastically between two parallel fixed bricks, a distance  $L$  apart, in such a way that the same end touches both bricks, and the stick hits the bricks at an angle  $\theta$  each time. See Fig. 8.67. What is  $\theta$  in terms of  $L$  and  $\ell$  (an implicit equation is fine)? Draw a reasonably accurate picture of what the situation looks like in the limit  $L \ll \ell$ .

What should  $\theta$  be in terms of  $L$  and  $\ell$  (again, an implicit equation is fine), if the stick makes an additional  $n$  half revolutions between the bricks? What is the minimum value of  $L/\ell$  for which  $n$  half revolutions are possible?

#### 8.75. Repetitive bouncing \*

Using the result of Problem 8.20, what must the relation between  $v_x$  and  $R\omega$  be so that a superball continually bounces back and forth between the same two points of contact on the ground?

![Diagram (top view) showing a stick of length l bouncing between two parallel bricks separated by distance L. The stick makes an angle theta with the normal to the bricks at each contact point.](3b0c70fe88d3da0098a133762c083aee_img.jpg)

The diagram, labeled '(top view)', shows two vertical rectangular bricks separated by a horizontal distance  $L$ , indicated by a dashed line with arrows at both ends. A stick of length  $\ell$  is shown in two positions. In the first position, the left end of the stick is in contact with the left brick, and the stick makes an angle  $\theta$  with the horizontal dashed line. In the second position, the right end of the stick is in contact with the right brick, and the stick also makes an angle  $\theta$  with the horizontal dashed line. The stick's path between these two contacts forms a V-shape.

Diagram (top view) showing a stick of length l bouncing between two parallel bricks separated by distance L. The stick makes an angle theta with the normal to the bricks at each contact point.

Fig. 8.67

#### **8.76. Bouncing under a table \*\***

You throw a superball so that it bounces off the floor, then off the underside of a table, then off the floor again. What must the initial relation between  $v_x$  and  $R\omega$  be so that the ball returns to your hand, with the outward and return paths the same? Use the result of Problem 8.20, and modifications thereof.<sup>12</sup>

#### **8.77. Bouncing under a table again \*\*\*\***

Consider the setup in the previous exercise, where we assumed that the outward and return paths were the same. Is this trajectory (where the path retraces itself) the only possible one for which the ball returns to your hand? Show<sup>13</sup> that the answer is “yes” unless  $t_1 = 7t_2$ , where  $t_1$  is the time the ball spends between your hand and the floor (which is the same out and back, because the magnitude of  $v_y$  isn’t changed by a bounce), and  $t_2$  is the time the ball spends between the floor and the table (again, the same out and back). For the special case where  $t_1 = 7t_2$ , you will find that the ball returns to your hand for *any* initial relation between  $v_x$  and  $R\omega$ .<sup>14</sup>

For a ball with a general moment of inertia  $I = \beta mr^2$ , show that the answer is always “yes,” without exception, if  $\beta \leq 1/3$  (which corresponds to a wheel with massive spokes and a massless rim). Also, show that if  $\beta = 1$  (a hoop), then the  $t_1 = 7t_2$  condition becomes  $t_1 = t_2$ . In other words, if you throw a “super-hoop” from the same height as the table, then no matter how you throw it (as long as the throw is downward and in the plane of the hoop), it will return to your hand. This is a little more believable if you look at the remark in the solution to Problem 8.20.

### **8.9 Solutions**

#### **8.1. Massive pulley**

The two masses have equal speeds at all times. Let  $v$  be their common speed after they have each moved a distance  $d$ . If  $2m$  falls a distance  $d$  (so that  $m$  rises a distance  $d$ ), then the change in potential energy is  $-2mgd + 2mgd = -mgd$ . The total kinetic energy is

$$K = \frac{1}{2}mv^2 + \frac{1}{2}(2m)v^2 + \frac{1}{2}I\omega^2$$

<sup>12</sup> You are strongly encouraged to bounce a ball in such a manner and have it magically come back to your hand. It turns out that the required value of  $\omega$  is small, so a natural throw with  $\omega \approx 0$  essentially gets the job done.

<sup>13</sup> You will want to use Mathematica or some other aid to keep track of the matrix multiplications, especially in the second part of this exercise, which would be completely intractable otherwise.

<sup>14</sup> I learned of this extremely bizarre fact from Howard Georgi.

$$\begin{aligned}
 &= \frac{1}{2}mv^2 + \frac{1}{2}(2m)v^2 + \frac{1}{2}\left(\frac{1}{2}mr^2\right)\left(\frac{v}{r}\right)^2 \\
 &= \frac{7}{4}mv^2,
 \end{aligned} \tag{8.64}$$

where we have used the nonslipping condition,  $v = r\omega$ . Conservation of energy therefore gives

$$0 = \frac{7}{4}mv^2 - mgd \implies v = \sqrt{\frac{4}{7}gd}. \tag{8.65}$$

The usual kinematic result  $v = \sqrt{2ad}$  holds here, so we obtain  $a = 2g/7$ .

#### 8.2. Leaving the sphere

In this setup, as in Problem 5.3, the ball leaves the sphere when the normal force becomes zero, that is, when

$$\frac{mv^2}{R} = mg \cos \theta. \tag{8.66}$$

The only change from the solution to Problem 5.3 comes in the calculation of  $v$ . The ball now has rotational energy, so conservation of energy gives  $mgR(1 - \cos \theta) = mv^2/2 + I\omega^2/2 = mv^2/2 + \beta mr^2\omega^2/2$ . But the nonslipping condition is  $v = r\omega$ , so we have

$$\frac{1}{2}(1 + \beta)mv^2 = mgR(1 - \cos \theta) \implies v = \sqrt{\frac{2gR(1 - \cos \theta)}{1 + \beta}}. \tag{8.67}$$

Plugging this into Eq. (8.66), we see that the ball leaves the sphere when

$$\cos \theta = \frac{2}{3 + \beta}. \tag{8.68}$$

REMARKS: For  $\beta = 0$ , this equals  $2/3$ , as in Problem 5.3. For a uniform ball with  $\beta = 2/5$ , we have  $\cos \theta = 10/17$ , so  $\theta \approx 54^\circ$ . For  $\beta \rightarrow \infty$  (for example, a spool with a very thin axle rolling down the rim of a circle), we have  $\cos \theta \rightarrow 0$ , so  $\theta \approx 90^\circ$ . This makes sense because  $v$  is always very small, since most of the energy takes the form of rotational energy. The coefficient of friction would have to be very large in this case, of course, to keep the spool from slipping near  $\theta \approx 90^\circ$ . ♣

If the size of the ball is comparable to, or larger than, the size of the sphere, then we must take into account the fact that the CM of the ball does not move along a circle of radius  $R$ . Instead, it moves along a circle of radius  $R + r$ , so Eq. (8.66) becomes

$$\frac{mv^2}{R + r} = mg \cos \theta. \tag{8.69}$$

Also, the conservation of energy equation takes the form,  $mg(R + r)(1 - \cos \theta) = mv^2/2 + \beta mr^2\omega^2/2$ . But  $v$  still equals  $r\omega$  (because the ball can be considered to be instantaneously rotating around the contact point with angular speed  $\omega$ ), so the kinetic energy still equals  $(1 + \beta)mv^2/2$ . The conservation of energy statement is thus

$$\frac{1}{2}(1 + \beta)mv^2 = mg(R + r)(1 - \cos \theta). \tag{8.70}$$

We therefore have the same equations as above, except that  $R$  is replaced everywhere by  $R + r$ . But  $R$  didn't appear in the result for  $\theta$  in Eq. (8.68), so the answer is unchanged.

REMARK: The method of the second solution to Problem 5.3 does *not* work in this problem, because there *is* a force available to make  $v_x$  decrease, namely the friction

force. And indeed,  $v_x$  does decrease before the rolling ball leaves the sphere. At a given value of  $\theta$ , the  $v$  in the present problem is simply  $1/\sqrt{1+\beta}$  times the  $v$  in Problem 5.3, so the maximum  $v_x$  is achieved here at  $\cos\theta = 2/3$ , just as in Problem 5.3. But the angle in Eq. (8.68) is larger than this, so  $v_x$  decreases while the ball is between these two angles. (However, see the following problem for a setup involving rotations where the max  $v_x$  is relevant.) ♣

#### 8.3. Sliding ladder

The important point to realize in this problem is that the ladder loses contact with the wall before it hits the ground. So we need to find where this loss of contact occurs. Let  $r = \ell/2$ , for convenience. While the ladder is in contact with the wall, its CM moves in a circle of radius  $r$ . This follows from the fact that the median to the hypotenuse of a right triangle has half the length of the hypotenuse. Let  $\theta$  be the angle between the wall and the radius from the corner to the CM (see Fig. 8.68). This is also the angle between the ladder and the wall.

We'll solve this problem by assuming that the CM always moves in a circle, and then determining the position at which the horizontal CM speed starts to decrease, that is, the point at which the normal force from the wall would have to become negative. Since the normal force of course can't be negative, this is the point where the ladder loses contact with the wall.

By conservation of energy, the kinetic energy of the ladder equals the loss in potential energy, which is  $mgr(1 - \cos\theta)$ . This kinetic energy can be broken up into the CM translational energy plus the rotation energy. The CM translational energy is  $mr^2\dot{\theta}^2/2$ , because the CM travels in a circle of radius  $r$ . The rotational energy is  $I\dot{\theta}^2/2$ . The same  $\dot{\theta}$  applies here as in the CM translational motion, because  $\theta$  is the angle between the ladder and the vertical, and is thus the angle of rotation of the ladder. Letting  $I \equiv \beta mr^2$  to be general ( $\beta = 1/3$  for our ladder), the conservation of energy statement is  $(1+\beta)mr^2\dot{\theta}^2/2 = mgr(1 - \cos\theta)$ . Therefore, the speed of the CM, which is  $v = r\dot{\theta}$ , equals

$$v = \sqrt{\frac{2gr(1 - \cos\theta)}{1 + \beta}}. \quad (8.71)$$

The horizontal component of this is

$$v_x = \sqrt{\frac{2gr}{1 + \beta}} \sqrt{(1 - \cos\theta)} \cos\theta. \quad (8.72)$$

Taking the derivative of  $\sqrt{(1 - \cos\theta)} \cos\theta$ , we see that the horizontal speed is maximum when  $\cos\theta = 2/3$ . Therefore the ladder loses contact with the wall when

$$\cos\theta = \frac{2}{3} \implies \theta \approx 48.2^\circ, \quad (8.73)$$

which is independent of  $\beta$ . This means that, for example, a dumbbell (two masses at the ends of a massless rod, with  $\beta = 1$ ) loses contact with the wall at the same angle. Plugging the value of  $\theta$  from Eq. (8.73) into Eq. (8.72), and using  $\beta = 1/3$ , we obtain a final horizontal speed of

$$v_x = \frac{\sqrt{2gr}}{3} \equiv \frac{\sqrt{g\ell}}{3}. \quad (8.74)$$

Note that this is  $1/3$  of the  $\sqrt{2gr}$  horizontal speed that the ladder would have if it were arranged (perhaps by having the top end slide down a curve) to eventually slide horizontally along the ground. You are encouraged to compare various aspects of this problem with those in Problem 8.2 and Problem 5.3.

**REMARK:** The normal force from the wall is zero at the start and zero at the finish, so it must reach a maximum at some intermediate value of  $\theta$ . Let's find this  $\theta$ . Taking the

![Diagram of a ladder leaning against a wall. The ladder is represented by a solid line of length 2r. The center of mass (CM) is at the midpoint, at a distance r from each end. A dashed line of length r connects the bottom corner to the CM. The angle between the wall and the ladder is labeled theta. The angle between the wall and the dashed line is also labeled theta. The ladder is in contact with a vertical wall on the left and a horizontal floor at the bottom.](ffce6434104c2eeff05cba63d58ec8b4_img.jpg)

Diagram of a ladder leaning against a wall. The ladder is represented by a solid line of length 2r. The center of mass (CM) is at the midpoint, at a distance r from each end. A dashed line of length r connects the bottom corner to the CM. The angle between the wall and the ladder is labeled theta. The angle between the wall and the dashed line is also labeled theta. The ladder is in contact with a vertical wall on the left and a horizontal floor at the bottom.

Fig. 8.68

![Diagram of a rectangle leaning against a cylinder. The rectangle has width 2b and height 2a. The cylinder has radius R. The rectangle is tilted at an angle theta from the vertical. The center of mass (CM) is at a distance a from the contact point. The distance from the center of the cylinder to the CM is R + a. The angle theta is shown between the vertical and the line connecting the cylinder's center to the CM.](50d738bce2627effeff72243f7ab3e79_img.jpg)

Diagram of a rectangle leaning against a cylinder. The rectangle has width 2b and height 2a. The cylinder has radius R. The rectangle is tilted at an angle theta from the vertical. The center of mass (CM) is at a distance a from the contact point. The distance from the center of the cylinder to the CM is R + a. The angle theta is shown between the vertical and the line connecting the cylinder's center to the CM.

Fig. 8.69

derivative of  $v_x$  in Eq. (8.72) to find the CM's horizontal acceleration  $a_x$ , and then using  $\dot{\theta} \propto \sqrt{1 - \cos \theta}$  from Eq. (8.71), we see that the force from the wall is proportional to

$$a_x \propto \frac{\sin \theta (3 \cos \theta - 2) \dot{\theta}}{\sqrt{1 - \cos \theta}} \propto \sin \theta (3 \cos \theta - 2). \quad (8.75)$$

Taking the derivative of this, we find that the force from the wall is maximum when  $\cos \theta = (1 + \sqrt{19})/6 \implies \theta \approx 26.7^\circ$  ♣

#### 8.4. Leaning rectangle

We must first find the position of the rectangle's CM when it has rotated through an angle  $\theta$ . Using Fig. 8.69, we can obtain this position (relative to the center of the cylinder) by adding up the distances along the three shaded triangles. Because there is no slipping, the contact point has moved a distance  $R\theta$  along the rectangle. We find that the position of the CM is

$$(x, y) = R(\sin \theta, \cos \theta) + R\theta(-\cos \theta, \sin \theta) + a(\sin \theta, \cos \theta). \quad (8.76)$$

We'll now use the Lagrangian method to find the equation of motion and the frequency of small oscillations. Using Eq. (8.76), you can show that the square of the speed of the CM is

$$v^2 = \dot{x}^2 + \dot{y}^2 = (a^2 + R^2\theta^2)\dot{\theta}^2. \quad (8.77)$$

The simplicity of this result suggests that there is a quicker way to obtain it. And indeed, the CM instantaneously rotates around the contact point with angular speed  $\dot{\theta}$ , and from Fig. 8.69, the distance to the contact point is  $\sqrt{a^2 + R^2\theta^2}$ . Therefore, the speed of the CM is  $\omega r = \dot{\theta}\sqrt{a^2 + R^2\theta^2}$ .

The Lagrangian is

$$\mathcal{L} = T - V = \frac{1}{2}m(a^2 + R^2\theta^2)\dot{\theta}^2 + \frac{1}{2}I\dot{\theta}^2 - mg((R + a)\cos \theta + R\theta \sin \theta). \quad (8.78)$$

The equation of motion is, as you can check,

$$(ma^2 + mR^2\theta^2 + I)\ddot{\theta} + mR^2\theta\dot{\theta}^2 = mga \sin \theta - mgR\theta \cos \theta. \quad (8.79)$$

Let us now consider small oscillations. Using the small-angle approximations,  $\sin \theta \approx \theta$  and  $\cos \theta \approx 1 - \theta^2/2$ , and keeping terms up to first order in  $\theta$ , we obtain

$$(ma^2 + I)\ddot{\theta} + mg(R - a)\theta = 0. \quad (8.80)$$

The coefficient of  $\theta$  is positive if  $a < R$ . Therefore, oscillatory motion occurs if  $a < R$ . Note that this condition is independent of  $b$ . The frequency of small oscillations is

$$\omega = \sqrt{\frac{mg(R - a)}{ma^2 + I}}. \quad (8.81)$$

If  $a \geq R$ , then the rectangle falls off the cylinder.

**REMARKS:** Let's look at some special cases. If  $I = 0$  (that is, all of the rectangle's mass is located at the CM), we have  $\omega = \sqrt{g(R - a)/a^2}$ . If in addition  $a \ll R$ , then  $\omega \approx \sqrt{gR/a^2}$ . You can also derive these results by considering the CM to be a point mass sliding in a parabolic potential. If the rectangle is instead a uniform horizontal stick, so that  $a \ll R$ ,  $a \ll b$ , and  $I \approx mb^2/3$ , then we have  $\omega \approx \sqrt{3gR/b^2}$ . If the rectangle is a vertical stick (satisfying  $a < R$ ), so that  $b \ll a$  and  $I \approx ma^2/3$ , then we have  $\omega \approx \sqrt{3g(R - a)/4a^2}$ . If in addition  $a \ll R$ , then  $\omega \approx \sqrt{3gR/4a^2}$ .

Without doing much work, there are two other ways we can determine the condition under which there is oscillatory motion. The first is to look at the height of the CM (although this is essentially what we ended up doing in the solution above). Using small-angle approximations in Eq. (8.76), the height of the CM is  $y \approx (R + a) +$

$(R - a)\theta^2/2$ . Therefore, if  $a < R$ , the potential energy increases with  $\theta$ , so the rectangle wants to decrease its  $\theta$  and fall back down to the middle. But if  $a > R$ , the potential energy decreases with  $\theta$ , so the rectangle wants to increase its  $\theta$  and fall off the cylinder.

The second way is to look at the horizontal positions of the CM and the contact point. Small-angle approximations in Eq. (8.76) show that the former equals  $a\theta$  and the latter equals  $R\theta$ . Therefore, if  $a < R$  then the CM is to the left of the contact point, so the torque from gravity (relative to the contact point) makes  $\theta$  decrease, and the motion is stable. But if  $a > R$  then the torque from gravity makes  $\theta$  increase, and the motion is unstable. ♣

#### 8.5. Mass in a tube

The Lagrangian is

$$\mathcal{L} = \frac{1}{2} \left( \frac{1}{3} M \ell^2 \right) \dot{\theta}^2 + \left( \frac{1}{2} m x^2 \dot{\theta}^2 + \frac{1}{2} m \dot{x}^2 \right) + mgx \sin \theta + Mg \left( \frac{\ell}{2} \right) \sin \theta. \quad (8.82)$$

The Euler–Lagrange equations are then

$$\begin{aligned} \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) &= \frac{\partial \mathcal{L}}{\partial x} \implies m\ddot{x} = mx\dot{\theta}^2 + mg \sin \theta, \\ \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{\theta}} \right) &= \frac{\partial \mathcal{L}}{\partial \theta} \implies \frac{d}{dt} \left( \frac{1}{3} M \ell^2 \dot{\theta} + m x^2 \dot{\theta} \right) = \left( mgx + \frac{Mg\ell}{2} \right) \cos \theta \quad (8.83) \\ &\implies \left( \frac{1}{3} M \ell^2 + m x^2 \right) \ddot{\theta} + 2mx\dot{x}\dot{\theta} = \left( mgx + \frac{Mg\ell}{2} \right) \cos \theta. \end{aligned}$$

In terms of  $\eta \equiv x/\ell$ , these equations become

$$\begin{aligned} \ddot{\eta} &= \eta \dot{\theta}^2 + \tilde{g} \sin \theta, \\ (1 + 3r\eta^2) \ddot{\theta} &= \left( 3r\tilde{g}\eta + \frac{3\tilde{g}}{2} \right) \cos \theta - 6r\eta\dot{\eta}\dot{\theta}, \end{aligned} \quad (8.84)$$

where  $r \equiv m/M$  and  $\tilde{g} \equiv g/\ell$ . Below is a Maple program that numerically finds the value of  $\eta$  when  $\theta$  equals  $\pi/2$ , in the case where  $r = 1$ . As mentioned in Problem 1.2, this value of  $\eta$  does not depend on  $g$  or  $\ell$ , and hence not  $\tilde{g}$ . In the program, we'll denote  $\tilde{g}$  by  $g$ , which we'll give the arbitrary value of 10. We'll use  $q$  for  $\theta$ , and  $n$  for  $\eta$ . Also, we'll denote  $\dot{\theta}$  by  $q1$  and  $\ddot{\theta}$  by  $q2$ , etc. Even if you don't know Maple, this program should still be understandable. See Section 1.4 for more discussion of solving differential equations numerically.

```
n:=0:           # initial n value
n1:=0:          # initial n speed
q:=0:           # initial angle
q1:=0:          # initial angular speed
e:=.0001:       # small time interval
g:=10:          # value of g/l
r:=1:           # value of m/M
while q<1.57079 do # do this process until
                  # the angle is pi/2
n2:=n*q1^2+g*sin(q): # the first E-L equation
q2:=((3*r*g*n+3*g/2)*cos(q)
     -6*r*n*n1*q1)/(1+3*r*n^2): # the second E-L equation
n:=n+e*n1:      # how n changes
n1:=n1+e*n2:    # how n1 changes
q:=q+e*q1:      # how q changes
q1:=q1+e*q2:    # how q1 changes
end do:         # stop the process
n;              # print the value of n
```

The resulting value of  $\eta$  is 0.378. If you actually run this program on Maple with different values of  $g$ , you will find that the result for  $\eta$  doesn't depend on  $g$ , as stated above. A few results for  $\eta$  for various values of  $r$  are, in  $(r, \eta)$  notation:  $(0, 0.349)$ ,  $(1, 0.378)$ ,  $(2, 0.410)$ ,  $(10, 0.872)$ ,  $(20, 3.290)$ . It turns out that  $r \approx 11.25$  yields  $\eta \approx 1$ . That is, the mass  $m$  gets to the end of the tube right when the tube becomes vertical.

For  $\eta$  values larger than 1, we could imagine attaching a massless tubular extension on the end of the given tube. It turns out that  $\eta \rightarrow \infty$  as  $r \rightarrow \infty$ . In this case, the mass  $m$  drops nearly straight down, causing the tube to quickly swing down to a nearly vertical position. But  $m$  ends up slightly to one side and then takes a very long time to move over to become directly below the pivot.

![Figure 8.70: A diagram showing a cross-section of a blob in the x-z plane. The z-axis is vertical and the x-axis is horizontal. The blob is symmetric about the z-axis. Two points, P1 and P2, are marked on the right-hand surface of the blob. P1 is at a distance r1 from the z-axis, and P2 is at a distance r2 from the z-axis. A horizontal line at the top of the blob is labeled z = 1.](2a373d121aa35332eeb3f91f65250fe7_img.jpg)

Figure 8.70: A diagram showing a cross-section of a blob in the x-z plane. The z-axis is vertical and the x-axis is horizontal. The blob is symmetric about the z-axis. Two points, P1 and P2, are marked on the right-hand surface of the blob. P1 is at a distance r1 from the z-axis, and P2 is at a distance r2 from the z-axis. A horizontal line at the top of the blob is labeled z = 1.

Fig. 8.70

#### 8.6. Minimum $I$

The shape should be a cylinder with the  $z$  axis as its symmetry axis. A quick proof (by contradiction) is as follows. Assume that the optimal blob is not a cylinder, and consider the surface of the blob. If the blob is not a cylinder, then there exist two points on the surface,  $P_1$  and  $P_2$ , that are located at different distances,  $r_1$  and  $r_2$ , from the  $z$  axis. Assume  $r_1 < r_2$  (see Fig. 8.70). If we move a small piece of the blob from  $P_2$  to  $P_1$ , then we decrease the moment of inertia,  $\int r^2 dm$ . Therefore, the proposed noncylindrical blob cannot be the one with the smallest  $I$ . In order to avoid this contradiction, all points on the surface must be equidistant from the  $z$  axis. The only blob with this property is a cylinder.

#### 8.7. Slick calculations of $I$

- (a) We claim that the  $I$  for a square of side  $2\ell$  is 16 times the  $I$  for a square of side  $\ell$ , assuming that the axes pass through any two corresponding points. This is true because  $dm$  is proportional to the area, which is proportional to length squared, so the corresponding  $dm$ 's differ by a factor of 4. And then there are the two powers of  $r$  in the integrand. Therefore, when changing variables from one square to the other, there are four powers of 2 in the integral  $\int r^2 dm = \int r^2 \rho dx dy$ .

As in Section 8.3.2, we can express the relevant relations in terms of pictures:

$$\begin{aligned} \boxed{\bullet}^{2\ell} &= 16 \boxed{\bullet}^{\ell} \\ \boxed{\bullet} &= 4 \boxed{\bullet} \\ \boxed{\bullet} &= \boxed{\bullet} + m \left( \frac{\ell}{\sqrt{2}} \right)^2 \end{aligned}$$

The first line comes from the scaling argument, the second comes from the fact that moments of inertia simply add, and the third comes from the parallel-axis theorem. Equating the right-hand sides of the first two, and then using the third to eliminate  $\boxed{\bullet}$  gives

$$\boxed{\bullet}^{\ell} = \frac{1}{6} ml^2$$

This agrees with the result of Example 12 in Section 8.3.1, with  $a = b = \ell$ .

- (b) This is again a two-dimensional object, so the  $I$  for a triangle of side  $2\ell$  is 16 times the  $I$  for a triangle of side  $\ell$ , assuming that the axes pass through any two corresponding points. With pictures, we have:

$$\begin{aligned} \text{Triangle of side } 2\ell \text{ with axis through 2 vertices} &= 16 \text{ Triangle of side } \ell \text{ with axis through 2 vertices} \\ \text{Triangle of side } 2\ell \text{ with axis through 2 vertices} &= \text{Triangle of side } \ell \text{ with axis through 2 vertices} + 3(\text{Triangle of side } \ell \text{ with axis through 1 vertex}) \\ \text{Triangle of side } \ell \text{ with axis through 1 vertex} &= \text{Triangle of side } \ell \text{ with axis through 2 vertices} + m\left(\frac{\ell}{\sqrt{3}}\right)^2 \end{aligned}$$

The first line comes from the scaling argument, the second comes from the fact that moments of inertia simply add, and the third comes from the parallel-axis theorem. Equating the right-hand sides of the first two, and then using the third

to eliminate  $\bullet \triangleright$  gives

$$\frac{\bullet \triangle}{\ell} = \frac{1}{12} ml^2$$

This agrees with the result of Example 11 in Section 8.3.1, with  $N = 3$ . The “radius”  $R$  used in that example equals  $\ell/\sqrt{3}$  in the present notation.

#### 8.8. Slick calculations of $I$ for fractal objects

- (a) The scaling argument here is a little trickier than the one in Section 8.3.2. Our object is self-similar to an object 3 times as big, so let’s increase the length by a factor of 3 and see what happens to  $I$ . In the integral  $\int x^2 dm$ , the  $x$ ’s pick up a factor of 3, so this gives a factor of 9. But what happens to the  $dm$ ? Well, tripling the size of our object increases its mass by a factor of 2, because the new object is made up of two of the smaller ones, plus some empty space in the middle. So the  $dm$  picks up a factor of 2. Therefore, the  $I$  for an object of length  $3\ell$  is 18 times the  $I$  for an object of length  $\ell$ , assuming that the axes pass through any two corresponding points. With pictures, we have (the following symbols denote our fractal object):

$$\begin{aligned} \text{---} \bullet \text{---} \text{ of length } 3\ell &= 18 \text{ ---} \bullet \text{---} \text{ of length } \ell \\ \text{---} \bullet \text{---} &= 2 \left( \overset{\ell/2}{\text{---} \bullet \text{---}} \right) \\ \bullet \text{---} &= \text{---} \bullet \text{---} + ml^2 \end{aligned}$$

The first line comes from the scaling argument, the second comes from the fact that moments of inertia simply add, and the third comes from the parallel-axis theorem. Equating the right-hand sides of the first two, and then using the

third to eliminate  $\bullet - -$  gives

$$\bullet - - = \frac{1}{8} ml^2$$

This is larger than the  $I$  for a uniform stick, namely  $m\ell^2/12$ , because the mass here is generally farther away from the center.

REMARK: When we increase the length of our object by a factor of 3, the factor of 2 in the  $dm$  is larger than the factor of 1 relevant to a zero-dimensional object, but smaller than the factor of 3 relevant to a one-dimensional object. So in some sense our object has a dimension between 0 and 1. It is reasonable to define the fractal dimension,  $d$ , of an object as the number for which  $r^d$  is the increase in “volume” when the dimensions are increased by a factor of  $r$ . In this problem, we have  $3^d = 2$ , so  $d = \log_3 2 \approx 0.63$ . ♣

- (b) Again, the mass scales in a strange way. Let’s increase the dimensions of our object by a factor of 2 and see what happens to  $I$ . In the integral  $\int x^2 dm$ , the  $x$ ’s pick up a factor of 2, so this gives a factor of 4. But what happens to the  $dm$ ? Doubling the size of our object increases its mass by a factor of 3, because the new object is made up of three of the smaller ones, plus an empty triangle in the middle. So the  $dm$  picks up a factor of 3. Therefore, the  $I$  for an object of side  $2\ell$  is 12 times the  $I$  for an object of side  $\ell$ , assuming that the axes pass through any two corresponding points. With pictures, we have:

$$\begin{aligned} \text{Large Triangle (side } 2\ell) &= 12 \text{ Small Triangle (side } \ell) \\ \text{Large Triangle (side } 2\ell) &= 3 (\bullet \text{ Triangle}) \\ \bullet \text{ Triangle} &= \text{Small Triangle} + m \left( \frac{\ell}{\sqrt{3}} \right)^2 \end{aligned}$$

The first line comes from the scaling argument, the second comes from the fact that moments of inertia simply add, and the third comes from the parallel-axis theorem. Equating the right-hand sides of the first two, and then using the third

to eliminate  $\bullet \text{ Triangle}$  gives

$$\text{Small Triangle (side } \ell) = \frac{1}{9} ml^2$$

This is larger than the  $I$  for the uniform triangle in Problem 8.7, namely  $m\ell^2/12$ , because the mass here is generally farther away from the center. Increasing the size of our object by a factor of 2 increases the “volume” by a factor of 3, so the fractal dimension is given by  $2^d = 3 \implies d = \log_2 3 \approx 1.58$ .

- (c) Again, the mass scales in a strange way. Let’s increase the dimensions of our object by a factor of 3 and see what happens to  $I$ . In the integral  $\int x^2 dm$ , the  $x$ ’s pick up a factor of 3, so this gives a factor of 9. But what happens to the  $dm$ ?

Tripling the size of our object increases its mass by a factor of 8, because the new object is made up of eight of the smaller ones, plus an empty square in the middle. So the  $dm$  picks up a factor of 8. Therefore, the  $I$  for an object of side  $3\ell$  is 72 times the  $I$  for an object of side  $\ell$ , assuming that the axes pass through any two corresponding points. With pictures, we have:

$$\begin{aligned}
 \begin{array}{c} 3\ell \\ \text{[Diagram: large square with a smaller square in the center]} \end{array} &= 72 \begin{array}{c} \ell \\ \text{[Diagram: small square]} \end{array} \\
 \begin{array}{c} \text{[Diagram: large square with a smaller square in the center]} \end{array} &= 4 \left( \begin{array}{c} \text{[Diagram: small square]} \end{array} \right) + 4 \left( \begin{array}{c} \text{[Diagram: small square]} \end{array} \right) \\
 \bullet \text{ [Diagram: small square]} &= \text{[Diagram: small square]} + ml^2 \\
 \bullet \text{ [Diagram: small square]} &= \text{[Diagram: small square]} + m(\sqrt{2}\ell)^2
 \end{aligned}$$

The first line comes from the scaling argument, the second comes from the fact that moments of inertia simply add, and the third and fourth come from the parallel-axis theorem. Equating the right-hand sides of the first two, and then using the third and fourth to eliminate  $\bullet \text{ [Diagram: small square]}$  and  $\text{[Diagram: small square]}$  gives

$$\begin{array}{c} \ell \\ \text{[Diagram: small square]} \end{array} = \frac{3}{16} ml^2$$

This is larger than the  $I$  for the uniform square in Problem 8.7, namely  $ml^2/6$ , because the mass here is generally farther away from the center. Increasing the size of our object by a factor of 3 increases the “volume” by a factor of 8, so the fractal dimension is given by  $3^d = 8 \implies d = \log_3 8 \approx 1.89$ .

#### 8.9. Zero torque from internal forces

Let  $\mathbf{F}_{ij}^{\text{int}}$  be the force that the  $i$ th particle feels due to the  $j$ th particle (see Fig. 8.71). Then

$$\mathbf{F}_i^{\text{int}} = \sum_j \mathbf{F}_{ij}^{\text{int}}. \quad (8.85)$$

The total internal torque on all the particles, relative to the chosen origin, is therefore

$$\boldsymbol{\tau}^{\text{int}} \equiv \sum_i \mathbf{r}_i \times \mathbf{F}_i^{\text{int}} = \sum_i \sum_j \mathbf{r}_i \times \mathbf{F}_{ij}^{\text{int}}. \quad (8.86)$$

But if we interchange the indices (which were labeled arbitrarily), we have

$$\boldsymbol{\tau}^{\text{int}} = \sum_j \sum_i \mathbf{r}_j \times \mathbf{F}_{ji}^{\text{int}} = - \sum_j \sum_i \mathbf{r}_j \times \mathbf{F}_{ij}^{\text{int}}, \quad (8.87)$$

![Diagram showing two particles, i and j, with position vectors r_i and r_j from an origin. The vector from j to i is labeled r_i - r_j. Force vectors F_ij^int and F_ji^int are shown acting on particles i and j respectively, pointing away from each other along the line connecting them.](c1c07382e0a81f91639774c5692ad302_img.jpg)

Diagram showing two particles, i and j, with position vectors r\_i and r\_j from an origin. The vector from j to i is labeled r\_i - r\_j. Force vectors F\_ij^int and F\_ji^int are shown acting on particles i and j respectively, pointing away from each other along the line connecting them.

Fig. 8.71

where we have used Newton's third law,  $\mathbf{F}_{ij}^{\text{int}} = -\mathbf{F}_{ji}^{\text{int}}$ . Adding the two previous equations gives

$$2\boldsymbol{\tau}^{\text{int}} = \sum_i \sum_j (\mathbf{r}_i - \mathbf{r}_j) \times \mathbf{F}_{ij}^{\text{int}}. \quad (8.88)$$

But  $\mathbf{F}_{ij}^{\text{int}}$  is parallel to  $(\mathbf{r}_i - \mathbf{r}_j)$ , by assumption. Therefore, each cross product in the sum equals zero.

The above sums might make this solution look a bit involved. But the idea is simply that the torques cancel in pairs. This is clear from Fig. 8.71, because the two forces shown are equal and opposite, and they have the same lever arm relative to the origin.

![Diagram of a horizontal stick of length l. A vertical arrow labeled F points upwards from the left end, and a vertical arrow labeled mg points downwards from the center of mass.](bcde5d537e172d0876ea5acd0f9faaed_img.jpg)

Diagram of a horizontal stick of length l. A vertical arrow labeled F points upwards from the left end, and a vertical arrow labeled mg points downwards from the center of mass.

Fig. 8.72

#### 8.10. Removing a support

- (a) **FIRST SOLUTION** Let the desired force from the left support be  $F$ , and let the downward acceleration of the stick's CM be  $a$ . Then the  $F = ma$  and  $\tau = I\alpha$  (relative to the fixed support; see Fig. 8.72) equations, along with the circular-motion relation between  $a$  and  $\alpha$ , are, respectively,

$$mg - F = ma, \quad mg \frac{\ell}{2} = \left(\frac{m\ell^2}{3}\right) \alpha, \quad a = \frac{\ell}{2} \alpha. \quad (8.89)$$

The second equation gives  $\alpha = 3g/2\ell$ . The third equation then gives  $a = 3g/4$ . And the first equation then gives  $F = mg/4$ . Note that the right end of the stick accelerates at  $2a = 3g/2$ , which is larger than  $g$ .

**SECOND SOLUTION** Looking at torques around the CM, and also torques around the fixed support, we have, respectively,

$$F \frac{\ell}{2} = \left(\frac{m\ell^2}{12}\right) \alpha, \quad \text{and} \quad mg \frac{\ell}{2} = \left(\frac{m\ell^2}{3}\right) \alpha. \quad (8.90)$$

Dividing the first of these equations by the second gives  $F = mg/4$ .

- (b) **FIRST SOLUTION** As in the first solution above, we have (using the parallel-axis theorem; see Fig. 8.73)

$$mg - F = ma, \quad mgd = (\beta mr^2 + md^2)\alpha, \quad a = \alpha d. \quad (8.91)$$

Solving for  $F$  gives  $F = mg/(1 + d^2/\beta r^2)$ . For  $d = r$  and  $\beta = 1/3$ , we obtain the answer in part (a).

**SECOND SOLUTION** As in the second solution above, looking at torques around the CM, and also torques around the fixed support, we have, respectively,

$$Fd = (\beta mr^2)\alpha, \quad \text{and} \quad mgd = (\beta mr^2 + md^2)\alpha. \quad (8.92)$$

Dividing the first of these equations by the second gives  $F = mg/(1 + d^2/\beta r^2)$ .

**REMARKS:** For the special case  $d = r$ , we have the following: If  $\beta = 0$  (point mass in the middle) then  $F = 0$ ; if  $\beta = 1$  (dumbbell with masses at the ends) then  $F = mg/2$ ; and if  $\beta = \infty$  (masses at the ends of long massless extensions of the stick) then  $F = mg$ . These all make intuitive sense. In the limit  $d = 0$ , we have  $F = mg$ . And in the limit  $d = \infty$  (using a massless extension), we have  $F = 0$ . Technically, we should be writing  $d \ll \sqrt{\beta} r$  and  $d \gg \sqrt{\beta} r$  here. ♣

#### 8.11. Falling stick

- (a) Let's calculate  $\tau$  and  $L$  relative to the pivot point. The torque is due to gravity, which effectively acts on the CM and has magnitude  $mg b$ . The moment of inertia of the stick around the horizontal axis through the pivot (and perpendicular to the massless stick) is simply  $mb^2$ . So when the stick starts to fall, the  $\tau = dL/dt$

![Diagram of a horizontal stick. A vertical arrow labeled F points upwards from a point at distance d from the left end. A vertical arrow labeled mg points downwards from the center of mass, which is at distance r from the right end.](fb81ba376dbff5faff68f1fa07daff5b_img.jpg)

Diagram of a horizontal stick. A vertical arrow labeled F points upwards from a point at distance d from the left end. A vertical arrow labeled mg points downwards from the center of mass, which is at distance r from the right end.

Fig. 8.73

equation is  $mgb = (mb^2)\alpha$ . Therefore, the initial acceleration of the CM, namely  $b\alpha$ , is

$$b\alpha = g, \quad (8.93)$$

which is independent of  $\ell$  and  $b$ . This answer makes sense. The stick initially falls straight down, and the pivot provides no force because it doesn't know right away that the stick is moving.

- (b) The only change from part (a) is the moment of inertia of the stick around the horizontal axis through the pivot (and perpendicular to the massless stick). From the parallel-axis theorem, this moment is  $mb^2 + m\ell^2/12$ . So when the stick starts to fall, the  $\tau = dL/dt$  equation is  $mgb = (mb^2 + m\ell^2/12)\alpha$ . Therefore, the initial acceleration of the CM is

$$b\alpha = \frac{g}{1 + (\ell^2/12b^2)}. \quad (8.94)$$

For  $\ell \ll b$ , this goes to  $g$ , as it should. And for  $\ell \gg b$ , it goes to zero, as it should. In this case, a tiny movement of the CM corresponds to a very large movement of the points far out along the stick. Therefore, by conservation of energy, the CM must be moving very slowly.

#### 8.12. Pulling a cylinder

Consider the net force in the  $y$  direction (the transverse direction) on an infinitesimal arclength of the cylinder. Measure  $\theta$  clockwise from the bottom, as shown in Fig. 8.74. The tension increases as  $\theta$  increases (assuming  $T_1 > T_2$ ), and the friction force  $F_f$  on the cylinder equals the difference  $dT$  in the tension from one end of the small arc to the other (using Newton's third law, and noting that there can be no net force on the string because it is massless). The friction force on the cylinder therefore produces a force component  $dT \sin \theta$  in the  $y$  direction. From the example in Section 2.1, the normal force on the cylinder is  $N = T d\theta$ , which yields a force component  $T d\theta \cos \theta$  in the  $y$  direction. The net  $y$ -force on the cylinder at the little arc is therefore

$$dF_y = dT \sin \theta + T d\theta \cos \theta = d(T \sin \theta). \quad (8.95)$$

The total  $F_y$  on the cylinder is thus

$$F_y = \int dF_y = \int d(T \sin \theta) = \Delta(T \sin \theta). \quad (8.96)$$

But  $\theta$  runs from 0 to  $\pi$ , which means that  $\sin \theta$  starts and ends at zero. Therefore, the total change in  $T \sin \theta$  equals zero, and so  $F_y = 0$ , as desired. Note that nowhere in this solution did we assume anything about  $T$ . The string might be slipping, and the cylinder might be rough in some places and smooth in others, and it doesn't matter. The total  $F_y$  is still zero (as we know it must be, from the simpler reasoning that  $T_1$  and  $T_2$  pull only in the  $x$  direction). Physically, what happens is that  $N$  is larger in the top half of the semicircle than in the bottom half, and the resulting net downward force cancels the upward force from the friction.

The above  $F_y = \Delta(T \sin \theta)$  result holds in general, and not just when the string wraps around a semicircle. Because of our convention for  $\theta$ , the signs work out so that  $\Delta(T \sin \theta)$  is simply the sum of the  $y$  components of the tensions  $T_1$  and  $T_2$ , which is the answer we expect.

#### 8.13. Oscillating ball

Let the angle from the bottom of the cylinder to the ball be  $\theta$  (see Fig. 8.75), and let  $F_f$  be the friction force. Then the tangential  $F = ma$  equation is

$$F_f - mg \sin \theta = ma, \quad (8.97)$$

where we have chosen rightward to be the positive direction for  $a$  and  $F_f$ . Also, the  $\tau = I\alpha$  equation (relative to the CM) is

$$-rF_f = \frac{2}{5}mr^2\alpha, \quad (8.98)$$

![Diagram of a cylinder with a string wrapped around it. The string is pulled horizontally to the right at both ends with tensions T1 and T2. A small arc of the cylinder is highlighted, showing a normal force N pointing towards the center and a friction force Ff pointing to the left. The angle theta is measured clockwise from the bottom, and dtheta is the angle subtended by the small arc.](75b46136fcdee06615e1ca1c23527a94_img.jpg)

Diagram of a cylinder with a string wrapped around it. The string is pulled horizontally to the right at both ends with tensions T1 and T2. A small arc of the cylinder is highlighted, showing a normal force N pointing towards the center and a friction force Ff pointing to the left. The angle theta is measured clockwise from the bottom, and dtheta is the angle subtended by the small arc.

Fig. 8.74

![Diagram of a ball on a curved surface. The ball is at an angle theta from the bottom of the curve. The radius of the curve is R. A friction force Ff is shown acting to the right along the tangent to the curve at the ball's position.](57e7d7b00070b36fbe98304e2cb770cf_img.jpg)

Diagram of a ball on a curved surface. The ball is at an angle theta from the bottom of the curve. The radius of the curve is R. A friction force Ff is shown acting to the right along the tangent to the curve at the ball's position.

Fig. 8.75

where we have chosen clockwise to be the positive direction for  $\alpha$ . Using the non-slipping condition  $r\alpha = a$ , the torque equation becomes  $F_f = -(2/5)ma$ . Plugging this into Eq. (8.97), and using  $\sin \theta \approx \theta$ , we obtain  $mg\theta + (7/5)ma = 0$ . Under the assumption  $r \ll R$ , the center of the ball moves along a circle with radius essentially equal to  $R$ , so we have  $a \approx R\ddot{\theta}$ . We therefore arrive at

$$\ddot{\theta} + \left(\frac{5g}{7R}\right)\theta = 0. \quad (8.99)$$

This is the equation for simple harmonic motion with frequency

$$\omega = \sqrt{\frac{5g}{7R}}. \quad (8.100)$$

In general, if the ball has a moment of inertia equal to  $\beta mr^2$ , you can show that the frequency of small oscillations is  $\sqrt{g/(1+\beta)R}$ . Note that we needed to use two different expressions for  $a$  in this solution, namely  $r\alpha$  and  $R\ddot{\theta}$ .

**REMARKS:** The answer in Eq. (8.100) is slightly smaller than the  $\sqrt{g/R}$  answer for the case where the ball slides. In terms of forces, the reason for this is that the friction force causes there to be a smaller net tangential force. In terms of energy, the reason is that energy is “lost” in the rotational motion, so the ball ends up moving slower.

If we omit the  $r \ll R$  assumption, then the  $r\alpha = a$  relation still holds, because we can consider the ball to be instantaneously rotating around the contact point. But the  $a = R\ddot{\theta}$  relation is replaced by  $a = (R-r)\ddot{\theta}$ , because the center of the ball moves along a circle of radius  $R-r$ . Therefore, the exact result for the frequency is  $\omega = \sqrt{5g/7(R-r)}$ . This goes to infinity as  $r \rightarrow R$ . ♣

#### 8.14. Oscillating cylinders

The moments of inertia of the cylinders are  $I_1 = M_1 R_1^2$  and  $I_2 = M_2 R_2^2$ . Let  $F$  be the force between the two cylinders, defined with rightward on the small cylinder being positive. Let  $\theta_1$  and  $\theta_2$  be the angles of rotation of the cylinders, with counterclockwise positive, relative to the position where the small cylinder is at the bottom of the big cylinder. Then the torque equations are

$$FR_1 = M_1 R_1^2 \ddot{\theta}_1, \quad \text{and} \quad FR_2 = -M_2 R_2^2 \ddot{\theta}_2. \quad (8.101)$$

We are not so much concerned with  $\theta_1$  and  $\theta_2$  as we are with the angular position that  $M_1$  makes with the vertical. Let this angle be  $\theta$  (see Fig. 8.76). In the approximation  $R_1 \ll R_2$ , the nonslipping condition says that  $R_2\theta \approx R_2\theta_2 - R_1\theta_1$ , since both sides of this equation are expressions for the arclength away from the bottom of the big cylinder. Adding Eqs. (8.101) after dividing through by the masses then gives

$$F \left( \frac{1}{M_1} + \frac{1}{M_2} \right) = -R_2 \ddot{\theta}. \quad (8.102)$$

The tangential force equation on  $M_1$  is

$$F - M_1 g \sin \theta = M_1 (R_2 \ddot{\theta}). \quad (8.103)$$

Substituting the  $F$  from (8.102) into this equation gives, with  $\sin \theta \approx \theta$ ,

$$\left( M_1 + \frac{1}{\frac{1}{M_1} + \frac{1}{M_2}} \right) \ddot{\theta} + \left( \frac{M_1 g}{R_2} \right) \theta = 0. \quad (8.104)$$

After simplifying, the frequency of small oscillations is

$$\omega = \sqrt{\frac{g}{R_2}} \sqrt{\frac{M_1 + M_2}{M_1 + 2M_2}}. \quad (8.105)$$

![Diagram of two cylinders in contact. A large cylinder of radius R_2 is shown as a semi-circle. A smaller cylinder of radius R_1 is in contact with it at the bottom. The center of the small cylinder is at an angle theta from the vertical dashed line. The angle theta_1 is the rotation of the small cylinder, and theta_2 is the rotation of the large cylinder.](71a32a01d8b2b16d8c4dd392e9666f8f_img.jpg)

Diagram of two cylinders in contact. A large cylinder of radius R\_2 is shown as a semi-circle. A smaller cylinder of radius R\_1 is in contact with it at the bottom. The center of the small cylinder is at an angle theta from the vertical dashed line. The angle theta\_1 is the rotation of the small cylinder, and theta\_2 is the rotation of the large cylinder.

Fig. 8.76

REMARKS: In the limit  $M_2 \ll M_1$ , we obtain  $\omega \approx \sqrt{g/R_2}$ . In this case, there is essentially no friction force between the cylinders, because otherwise the “massless”  $M_2$  would have infinite angular acceleration. So there is only a normal force, and the small cylinder essentially acts like a pendulum of length  $R_2$ . In the limit  $M_1 \ll M_2$ , we obtain  $\omega \approx \sqrt{g/2R_2}$ . In this case, the big cylinder is essentially fixed, so we simply have the setup mentioned in the solution to Problem 8.13, with  $\beta = 1$ . ♣

#### 8.15. Lengthening the string

Consider the angular momentum relative to the support point  $P$ . The forces on the mass are the tension in the string and gravity. The former provides no torque around  $P$ , and the latter provides no torque in the  $z$  direction. Therefore,  $L_z$  is constant. The motion is always approximately circular because the length of the string changes very slowly, so if we let  $\omega_\ell$  be the frequency of the circular motion when the string has length  $\ell$ , then we can say that

$$L_z = mr^2\omega_\ell \quad (8.106)$$

is constant. The frequency  $\omega_\ell$  can be obtained by using  $F = ma$  for the circular motion. The tension in the string is essentially  $mg/\cos\theta$  (to make the forces in the  $y$  direction cancel), so the horizontal radial force is  $mg\tan\theta$ . Therefore,

$$mg\tan\theta = mr\omega_\ell^2 = m(\ell\sin\theta)\omega_\ell^2 \implies \omega_\ell = \sqrt{\frac{g}{\ell\cos\theta}} = \sqrt{\frac{g}{h}}. \quad (8.107)$$

Plugging this into Eq. (8.106), we see that the constant value of  $L_z$  is

$$L_z = mr^2\sqrt{\frac{g}{h}}. \quad (8.108)$$

This holds at all times, so the quantity  $r^2/\sqrt{h}$  is constant. Let's look at the two cases.

- (a) For  $\theta \approx 0$ , we have  $h \approx \ell$ , so Eq. (8.108) says that  $r^2/\sqrt{\ell}$  is constant. Therefore,  

$$r \propto \ell^{1/4}, \quad (8.109)$$

which means that  $r$  grows very slowly as you let the string out when  $\theta \approx 0$ .

- (b) For  $\theta \approx \pi/2$ , we have  $r \approx \ell$ , so Eq. (8.108) says that  $\ell^2/\sqrt{h}$  is constant. Therefore,

$$h \propto \ell^4, \quad (8.110)$$

which means that  $h$  grows very quickly as you let the string out when  $\theta \approx \pi/2$ .

Note that Eq. (8.108) says that  $h \propto r^4$  for any value of  $\theta$ . So no matter what  $\theta$  is, if you slowly lengthen the string so that  $r$  doubles, then  $h$  increases by a factor of 16. Equivalently, if you draw the string in, the envelope of the motion of the mass is a surface of revolution generated by a curve of the form  $y \propto -x^4$ .

#### 8.16. A triangle of cylinders

- (a) Let  $N$  be the normal force between the cylinders, and let  $F$  be the friction force from the ground (see Fig. 8.77). Let  $a_x$  be the initial horizontal acceleration of the right bottom cylinder (so  $\alpha = a_x/R$  is its angular acceleration), and let  $a_y$  be the initial vertical acceleration of the top cylinder, with downward taken to be positive.

If we consider the torque around the center of one of the bottom cylinders, then the only relevant force is  $F$ , because  $N$ , gravity, and the normal force from the ground all point through the center. The equations for  $F_x = ma_x$  on the bottom right cylinder,  $F_y = ma_y$  on the top cylinder, and  $\tau = I\alpha$  on the bottom right cylinder are, respectively,

$$\begin{aligned} N \cos 60^\circ - F &= ma_x, \\ mg - 2N \sin 60^\circ &= ma_y, \end{aligned} \quad (8.111)$$

$$FR = (\beta mR^2)(a_x/R).$$

![Diagram of three identical cylinders arranged in a triangle. Two cylinders are at the base, touching each other and the ground. A third cylinder is placed on top of them, touching both. Normal forces N are shown acting between the cylinders and between the bottom cylinders and the ground. Friction forces F are shown acting on the bottom cylinders from the ground, pointing towards the center of the triangle.](b87c6557c55512dd64c8ee2dbe90b9af_img.jpg)

Diagram of three identical cylinders arranged in a triangle. Two cylinders are at the base, touching each other and the ground. A third cylinder is placed on top of them, touching both. Normal forces N are shown acting between the cylinders and between the bottom cylinders and the ground. Friction forces F are shown acting on the bottom cylinders from the ground, pointing towards the center of the triangle.

Fig. 8.77

![Diagram of three cylinders on a horizontal surface. One cylinder is on top, and two are on the bottom. The top cylinder is in contact with both bottom cylinders. The bottom cylinders are in contact with each other and the ground. Normal forces (N) and friction forces (F) are shown acting between the cylinders. For the top cylinder, two N forces point up and two F forces point outwards. For the bottom cylinders, two N forces point down and two F forces point inwards.](a2c50e5f3b43f7b472a8bc91ae86a964_img.jpg)

Diagram of three cylinders on a horizontal surface. One cylinder is on top, and two are on the bottom. The top cylinder is in contact with both bottom cylinders. The bottom cylinders are in contact with each other and the ground. Normal forces (N) and friction forces (F) are shown acting between the cylinders. For the top cylinder, two N forces point up and two F forces point outwards. For the bottom cylinders, two N forces point down and two F forces point inwards.

Fig. 8.78

We have four unknowns,  $N$ ,  $F$ ,  $a_x$ , and  $a_y$ , so we need one more equation. Fortunately,  $a_x$  and  $a_y$  are related. The contact surface between the top and bottom cylinders lies (initially) at an angle of  $30^\circ$  with the horizontal. Therefore, if the bottom cylinders move a distance  $d$  to the side, then the top cylinder moves a distance  $d \tan 30^\circ$  downward. Hence,

$$a_x = \sqrt{3}a_y. \quad (8.112)$$

We now have four equations and four unknowns. Solving for  $a_y$  by your method of choice gives

$$a_y = \frac{g}{7 + 6\beta}. \quad (8.113)$$

- (b) Let  $N$  be the normal force between the cylinders, and let  $F$  be the friction force between the cylinders, with positive directions shown in Fig. 8.78. Let  $a_x$  be the initial horizontal acceleration of the right bottom cylinder, and let  $a_y$  be the initial vertical acceleration of the top cylinder, with downward taken to be positive. Let  $\alpha$  be the angular acceleration of the right bottom cylinder, with counterclockwise taken to be positive. Note that  $\alpha$  is *not* equal to  $a_x/R$ , because the bottom cylinders slip on the ground.

If we consider the torque around the center of one of the bottom cylinders, then the only relevant force is  $F$ . And from the same reasoning as in part (a), we have  $a_x = \sqrt{3}a_y$ . Therefore, the four equations analogous to Eqs. (8.111) and (8.112) are

$$\begin{aligned} N \cos 60^\circ - F \sin 60^\circ &= ma_x, \\ mg - 2N \sin 60^\circ - 2F \cos 60^\circ &= ma_y, \\ FR &= (\beta mR^2)\alpha, \\ a_x &= \sqrt{3}a_y. \end{aligned} \quad (8.114)$$

We have five unknowns,  $N$ ,  $F$ ,  $a_x$ ,  $a_y$ , and  $\alpha$ , so we need one more equation. The tricky part is relating  $\alpha$  to  $a_x$ . One way to do this is to ignore the  $y$  motion of the top cylinder and imagine the bottom right cylinder to be rotating up and around the top cylinder, which is held fixed. In this rotational motion, the center of the bottom cylinder moves at an angle of  $30^\circ$  with respect to the horizontal (at the start). So if it moves an infinitesimal distance  $d$  to the right, then its center moves a distance  $d/\cos 30^\circ$  up and to the right. So the angle through which the bottom cylinder rotates is  $\theta = (d/\cos 30^\circ)/R = (2/\sqrt{3})(d/R)$ . Bringing back in the vertical motion of the top cylinder doesn't change this result. Therefore, taking two derivatives of this relation gives

$$\alpha = \frac{2}{\sqrt{3}} \frac{a_x}{R}. \quad (8.115)$$

We now have five equations and five unknowns. Solving for  $a_y$  by your method of choice gives

$$a_y = \frac{g}{7 + 8\beta}. \quad (8.116)$$

**REMARKS:** If  $\beta = 0$ , that is, if all the mass is at the center of the cylinders, then the results in both parts (a) and (b) reduce to  $g/7$ . This  $\beta = 0$  case is equivalent to the case of frictionless cylinders (of any mass distribution), because then nothing rotates. If  $\beta \neq 0$ , then the result in part (b) is smaller than that in part (a). This isn't so obvious, but the basic reason is that the bottom cylinders in part (b) take up more energy because they have to rotate slightly faster, because  $\alpha = (2/\sqrt{3})(a_x/R)$  instead of  $\alpha = a_x/R$ . ♣

#### 8.17. Falling chimney

Let  $\theta$  be the angle through which the chimney has fallen. Before we start dealing with the forces in the rods, let's first determine  $\ddot{\theta}$  as a function of  $\theta$ . Let  $\ell$  be the height of the chimney. Then the moment of inertia around the pivot point on the ground is  $m\ell^2/3$  (if we ignore the width). And the torque (around the pivot point) due to gravity is  $\tau = mg(\ell/2) \sin \theta$ . Therefore,  $\tau = dL/dt$  gives  $mg(\ell/2) \sin \theta = (1/3)m\ell^2\ddot{\theta}$ , and so

$$\ddot{\theta} = \frac{3g \sin \theta}{2\ell}. \quad (8.117)$$

Let's now determine the forces in the rods. Our strategy will be to imagine that the chimney consists of a chimney of height  $h$ , with another chimney of height  $\ell - h$  placed on top of it. We'll find the forces in the rods connecting these two "sub-chimneys," and then we'll maximize one of these forces ( $T_2$ , defined below) as a function of  $h$ .

The forces on the top piece are gravity and also the forces from the two rods at each end of the bottom board. Let's break these latter forces up into transverse and longitudinal forces along the chimney. Let  $T_1$  and  $T_2$  be the two longitudinal components, and let  $F$  be the sum of the transverse components, as shown in Fig. 8.79. We have picked the positive directions for  $T_1$  and  $T_2$  so that positive  $T_1$  corresponds to compression in the left rod, and positive  $T_2$  corresponds to tension in the right rod (which is what the forces will turn out to be, as we'll see). It turns out that if the width (which we'll call  $2r$ ) is much less than the height, then  $T_2 \gg F$  (as we'll see below), so the tension in the right rod is essentially equal to  $T_2$ . We will therefore be concerned with maximizing  $T_2$ .

In writing down the force and torque equations for the top piece, we have three equations (the radial and tangential  $F = ma$  equations, and  $\tau = dL/dt$  around the CM), and three unknowns ( $F$ ,  $T_1$ , and  $T_2$ ). If we define the fraction  $f \equiv h/\ell$ , then the top piece has length  $(1-f)\ell$  and mass  $(1-f)m$ , and its CM travels in a circle of radius  $(1+f)\ell/2$ . Therefore, our three force and torque equations are, respectively,

$$\begin{aligned} T_2 - T_1 + (1-f)mg \cos \theta &= (1-f)m \left( \frac{(1+f)\ell}{2} \right) \dot{\theta}^2, \\ F + (1-f)mg \sin \theta &= (1-f)m \left( \frac{(1+f)\ell}{2} \right) \ddot{\theta}, \\ (T_1 + T_2)r - F \frac{(1-f)\ell}{2} &= (1-f)m \left( \frac{(1-f)^2\ell^2}{12} \right) \ddot{\theta}. \end{aligned} \quad (8.118)$$

At this point, we could plow forward and solve this system of three equations in three unknowns. But things simplify greatly in the limit  $r \ll \ell$ . The third equation says that  $T_1 + T_2$  is of order  $1/r$ , and the first equation says that  $T_2 - T_1$  is of order 1. These imply that  $T_1 \approx T_2$ , to leading order in  $1/r$ . Therefore, we can set  $T_1 + T_2 \approx 2T_2$  in the third equation. Using this approximation, along with the value of  $\ddot{\theta}$  from Eq. (8.117), the second and third equations become

$$\begin{aligned} F + (1-f)mg \sin \theta &= \frac{3}{4}(1-f^2)mg \sin \theta, \\ 2rT_2 - F \frac{(1-f)\ell}{2} &= \frac{1}{8}(1-f)^3 mg \ell \sin \theta. \end{aligned} \quad (8.119)$$

This first of these equations gives

$$F = \frac{mg \sin \theta}{4}(-1 + 4f - 3f^2), \quad (8.120)$$

and then the second gives

$$T_2 \approx \frac{mg \ell \sin \theta}{8r} f(1-f)^2. \quad (8.121)$$

![Diagram of a falling chimney modeled as two stacked rectangular sections. The bottom section has height h and the top section has height l-h. The total height is l. The chimney is tilted at an angle theta from the vertical. Two rods of length r connect the top and bottom sections. At the left connection point, a force T1 acts along the chimney (compression) and a force F acts perpendicular to it. At the right connection point, a force T2 acts along the chimney (tension) and a force F acts perpendicular to it. The center of mass of the top section is indicated by a dashed line.](ab0b400ec4eac0e40c86bdd2bca85e9e_img.jpg)

Diagram of a falling chimney modeled as two stacked rectangular sections. The bottom section has height h and the top section has height l-h. The total height is l. The chimney is tilted at an angle theta from the vertical. Two rods of length r connect the top and bottom sections. At the left connection point, a force T1 acts along the chimney (compression) and a force F acts perpendicular to it. At the right connection point, a force T2 acts along the chimney (tension) and a force F acts perpendicular to it. The center of mass of the top section is indicated by a dashed line.

Fig. 8.79

As stated above, this is much greater than  $F$  (because  $\ell/r \gg 1$ ), so the tension in the right rod is essentially equal to  $T_2$ . Taking the derivative of  $T_2$  with respect to  $f$ , we see that it is maximum at

$$f \equiv \frac{h}{\ell} = \frac{1}{3}. \quad (8.122)$$

Therefore, the chimney is most likely to break at a point one-third of the way up (assuming that the width is much less than the height). Interestingly,  $f = 1/3$  makes the force  $F$  in Eq. (8.120) exactly equal to zero. For more on the falling chimney, see Madsen (1977) and Varieschi and Kamiya (2003).

#### 8.18. Ball hitting stick

Let  $V$ ,  $v$ , and  $\omega$  be the speed of the ball, the speed of the stick's CM, and the angular speed of the stick, respectively, after the collision. Then conservation of momentum, angular momentum (around the fixed point that coincides with the initial center of the stick), and energy give

$$\begin{aligned} MV_0 &= MV + mv, \\ MV_0 d &= MVd + \beta m \ell^2 \omega, \\ MV_0^2 &= MV^2 + mv^2 + \beta m \ell^2 \omega^2. \end{aligned} \quad (8.123)$$

We must solve these three equations for  $V$ ,  $v$ , and  $\omega$ . The first two equations quickly give  $vd = \beta \ell^2 \omega$ . Solving for  $V$  in the first equation and plugging the result into the third, and then eliminating  $\omega$  through  $vd = \beta \ell^2 \omega$  gives

$$v = \frac{2V_0}{1 + \frac{m}{M} + \frac{d^2}{\beta \ell^2}} \implies \omega = V_0 \frac{2 \frac{d}{\beta \ell^2} V_0}{1 + \frac{m}{M} + \frac{d^2}{\beta \ell^2}}. \quad (8.124)$$

Having found  $v$ , the first equation above gives  $V$  as

$$V = V_0 \frac{1 - \frac{m}{M} + \frac{d^2}{\beta \ell^2}}{1 + \frac{m}{M} + \frac{d^2}{\beta \ell^2}}. \quad (8.125)$$

You are encouraged to check various limits of these answers. Another solution to Eq. (8.123) is of course  $V = V_0$ ,  $v = 0$ , and  $\omega = 0$ . The initial conditions certainly satisfy conservation of  $p$ ,  $L$ , and  $E$  with the initial conditions (a fine tautology, indeed). Nowhere in Eq. (8.123) does it say that the ball actually hits the stick.

#### 8.19. A ball and stick theorem

As in the solution to Problem 8.18, we have

$$\begin{aligned} MV_0 &= MV + mv, \\ MV_0 d &= MVd + I\omega, \\ MV_0^2 &= MV^2 + mv^2 + I\omega^2. \end{aligned} \quad (8.126)$$

The speed of the contact point on the stick right after the collision equals the speed of the CM plus the rotational speed relative to the CM. In other words, it equals  $v + \omega d$ . The desired relative speed is therefore  $(v + \omega d) - V$ . We can determine the value of this relative speed by solving the above three equations for  $V$ ,  $v$ , and  $\omega$ . Equivalently, we can just use the results of Problem 8.18. There is, however, a much more appealing method, which is the following.

The first two equations quickly give  $mv d = I\omega$ . The last equation may then be written as, using  $I\omega^2 = (I\omega)\omega = (mv d)\omega$ ,

$$M(V_0 - V)(V_0 + V) = mv(v + \omega d). \quad (8.127)$$

If we now write the first equation as

$$M(V_0 - V) = mv, \quad (8.128)$$

we can divide Eq. (8.127) by Eq. (8.128) to obtain  $V_0 + V = v + \omega d$ , or

$$V_0 = (v + \omega d) - V, \quad (8.129)$$

as we wanted to show. In terms of velocities, the correct statement is that the final relative velocity is the negative of the initial relative velocity. In other words,  $V_0 - 0 = -(V - (v + \omega d))$ .

#### 8.20. The superball

Since we are told that  $|v_y|$  is unchanged by the bounce, we can ignore it when applying conservation of energy. And since the vertical impulse from the floor provides no torque around the ball's CM, we can completely ignore the  $y$  motion in this problem.

The horizontal impulse from the floor is responsible for changing both  $v_x$  and  $\omega$ . With positive directions defined as in the statement of the problem, Eq. (8.61) gives

$$\begin{aligned} \Delta L &= R\Delta p \\ \implies I(\omega' - \omega) &= Rm(v'_x - v_x). \end{aligned} \quad (8.130)$$

And conservation of energy gives

$$\begin{aligned} \frac{1}{2}mv_x'^2 + \frac{1}{2}I\omega'^2 &= \frac{1}{2}mv_x^2 + \frac{1}{2}I\omega^2 \\ \implies I(\omega'^2 - \omega^2) &= m(v_x^2 - v_x'^2). \end{aligned} \quad (8.131)$$

Dividing this equation by Eq. (8.130) gives<sup>15</sup>

$$R(\omega' + \omega) = -(v'_x + v_x). \quad (8.132)$$

We can now combine this equation with Eq. (8.130) which can be rewritten as, using  $I = (2/5)mR^2$ ,

$$\frac{2}{5}R(\omega' - \omega) = v'_x - v_x. \quad (8.133)$$

Given  $v_x$  and  $\omega$ , the previous two equations are two linear equations in the two unknowns,  $v'_x$  and  $\omega'$ . Solving for  $v'_x$  and  $\omega'$ , and writing the result in matrix notation, gives

$$\begin{pmatrix} v'_x \\ R\omega' \end{pmatrix} = \frac{1}{7} \begin{pmatrix} 3 & -4 \\ -10 & -3 \end{pmatrix} \begin{pmatrix} v_x \\ R\omega \end{pmatrix}, \quad (8.134)$$

as desired. Note that Eq. (8.132), when written in the form of  $v_x + R\omega = -(v'_x + R\omega')$ , says that the relative velocity of the ball's contact point and the ground simply changes sign during the bounce.

REMARK: For a ball with a general moment of inertia  $I = \beta mR^2$ , you can use the above procedure to show that the matrix in Eq. (8.134) takes the general form,

$$\frac{1}{1 + \beta} \begin{pmatrix} 1 - \beta & -2\beta \\ -2 & -(1 - \beta) \end{pmatrix}. \quad (8.135)$$

<sup>15</sup> We have divided out the trivial  $\omega' = \omega$  and  $v'_x = v_x$  solution, which corresponds to slipping motion on a frictionless plane. The nontrivial solution we will find shortly is the nonslipping one. Basically, to conserve energy, there must be no work done by friction. And since work is force times distance, this means that either (1) the plane is frictionless, so that the force is zero, or (2) there is no relative motion between the ball's contact point and the plane, so that the distance is zero. The latter case is the one we are concerned with here.

For  $\beta = 1$  (a hoop), this becomes

$$\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}, \quad (8.136)$$

which means that the bounce simply interchanges and negates the values of  $v_x$  and  $R\omega$ . In particular, if you throw a “super-hoop” sideways with no spin (that is,  $R\omega = 0$ ), then it will bounce straight up in the air (that is,  $v'_x = 0$ ) while spinning. ♣

#### 8.21. Many bounces

Equation (8.62) gives the result after one bounce, so the result after two bounces is

$$\begin{aligned} \begin{pmatrix} v''_x \\ R\omega'' \end{pmatrix} &= \begin{pmatrix} 3/7 & -4/7 \\ -10/7 & -3/7 \end{pmatrix} \begin{pmatrix} v'_x \\ R\omega' \end{pmatrix} \\ &= \begin{pmatrix} 3/7 & -4/7 \\ -10/7 & -3/7 \end{pmatrix}^2 \begin{pmatrix} v_x \\ R\omega \end{pmatrix} \\ &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} v_x \\ R\omega \end{pmatrix} \\ &= \begin{pmatrix} v_x \\ R\omega \end{pmatrix}. \end{aligned} \quad (8.137)$$

The square of the matrix turns out to be the identity. Therefore, after two bounces, both  $v_x$  and  $\omega$  return to their original values. The ball then repeats the motion of the previous two bounces (and so on, after every two bounces). The only difference between successive pairs of bounces is that the ball may shift horizontally. You are strongly encouraged to experimentally verify this interesting periodic behavior.

#### 8.22. Rolling over a bump

We will use the fact that the angular momentum of the ball with respect to the corner of the step (call this point  $P$ ) is unchanged by the collision. This is true because any forces exerted at point  $P$  provide zero torque around  $P$ . (The torque from gravity will be relevant during the subsequent rising-up motion. But during the instantaneous collision,  $L$  does not change.) This fact will allow us to find the energy of the ball right after the collision, which we will then require to be greater than  $mgh$ .

Breaking the initial  $L$  into the contribution relative to the CM, plus the contribution from the ball treated like a point mass located at the CM, we see that the initial angular momentum is  $L = (2/5)mR^2\omega_0 + mV_0(R - h)$ , where  $\omega_0$  is the initial angular speed. But the nonslipping condition tells us that  $\omega_0 = V_0/R$ , so we can write  $L$  as

$$L = \frac{2}{5}mRV_0 + mV_0(R - h) = mV_0 \left( \frac{7R}{5} - h \right). \quad (8.138)$$

Let  $\omega'$  be the angular speed of the ball around point  $P$  immediately after the collision. The parallel-axis theorem says that the moment of inertia around  $P$  is equal to  $(2/5)mR^2 + mR^2 = (7/5)mR^2$ . Conservation of  $L$  around  $P$  during the collision then gives

$$mV_0 \left( \frac{7R}{5} - h \right) = \frac{7}{5}mR^2\omega' \implies \omega' = \frac{V_0}{R} \left( 1 - \frac{5h}{7R} \right). \quad (8.139)$$

The energy of the ball right after the collision is therefore

$$E = \frac{1}{2} \left( \frac{7}{5}mR^2 \right) \omega'^2 = \frac{7}{10}mV_0^2 \left( 1 - \frac{5h}{7R} \right)^2. \quad (8.140)$$

The ball will climb up over the step if  $E \geq mgh$ , which gives

$$V_0 \geq \sqrt{\frac{10gh}{7}} \left( 1 - \frac{5h}{7R} \right)^{-1}. \quad (8.141)$$

REMARKS: It is possible for the ball to rise up over the step even if  $h > R$ , provided that the ball sticks to the corner, without slipping. (If  $h > R$ , the step would have to be “hollowed out” so that the ball doesn’t collide with the side of the step.) But note that  $V_0 \rightarrow \infty$  as  $h \rightarrow 7R/5$ . For  $h \geq 7R/5$ , it is impossible for the ball to make it up over the step, no matter how large  $V_0$  is. The ball will get pushed down into the ground, instead of rising up, if  $h > 7R/5$ .

For an object with a general moment of inertia  $I = \beta mR^2$  (so  $\beta = 2/5$  in our problem), you can show that the minimum initial speed is

$$V_0 \geq \sqrt{\frac{2gh}{1+\beta}} \left(1 - \frac{h}{(1+\beta)R}\right)^{-1}. \quad (8.142)$$

This decreases as  $\beta$  increases. It is smallest when the “ball” is a wheel with all the mass on its rim (so that  $\beta = 1$ ), in which case it is possible for the wheel to climb up over the step even if  $h$  is close to  $2R$ . ♣

#### 8.23. Falling toast

Let  $v_0$  and  $v$  be the speeds of the CM right before and right after the collision (so we know that  $v_0 = \sqrt{2gH}$ ). The  $I$  for a square is the same as the  $I$  for a stick,  $(1/12)m\ell^2$ , so  $\Delta L = (\ell/2)\Delta p$  gives<sup>16</sup>

$$\left(\frac{m\ell^2}{12}\right)\omega = -\frac{\ell}{2}(mv - mv_0) \implies v_0 - v = \frac{\ell\omega}{6}. \quad (8.143)$$

Conservation of energy during the collision gives

$$\frac{1}{2}mv_0^2 = \frac{1}{2}mv^2 + \frac{1}{2}\left(\frac{m\ell^2}{12}\right)\omega^2 \implies (v_0 + v)(v_0 - v) = \frac{\ell^2\omega^2}{12}. \quad (8.144)$$

Dividing this by Eq. (8.143) gives  $v_0 + v = \ell\omega/2$ . We now have two linear equations for  $v$  and  $\omega$ . Solving gives  $v = v_0/2$  and  $\omega = 3v_0/\ell$ .

After the collision, the time to hit the ground is given by  $vt + gt^2/2 = h$ . Solving for  $t$ , setting  $\omega t = \pi$  for half a rotation, and using the  $v$  and  $\omega$  we just found, yields

$$\frac{3v_0}{\ell} \cdot \frac{1}{g} \left( -\frac{v_0}{2} + \sqrt{\frac{v_0^2}{4} + 2gh} \right) = \pi. \quad (8.145)$$

Factoring out a  $v_0^2$  and then using  $v_0^2 = 2gH$  gives

$$\frac{3H}{\ell} \left( \sqrt{1 + \frac{4h}{H}} - 1 \right) = \pi. \quad (8.146)$$

Isolating the square root, and then squaring and solving for  $H$  gives

$$H = \frac{\pi^2\ell^2}{6(6h - \pi\ell)}. \quad (8.147)$$

The special value of  $\ell$  is  $\ell = (6/\pi)h$  (which would be a huge piece of toast), in which case  $H = \infty$ . If  $\ell$  is larger than  $(6/\pi)h$ , then there isn’t enough time to make half a rotation before hitting the floor. The intuitive reason for this is that since  $\omega = 6v/\ell$  (from above), there is no way to increase  $\omega$  without also increasing  $v$ . The toast has the best chance of making half a rotation if  $v$  is very large, because then gravity doesn’t have any time to increase  $v$ . In this limit, the toast makes half a rotation upon hitting the floor if  $\pi/\omega = h/v$ . Plugging in  $\omega = 6v/\ell$  gives  $6h = \pi\ell$ , as desired.

<sup>16</sup> The minus sign on the right-hand side comes from the fact that we were defining the  $v$ ’s to be positive downward. Equivalently, the force from the counter increases the angular speed but decreases the linear speed.

![Diagram of a ball of radius R on a horizontal surface. The ball is moving to the right with velocity V and rotating clockwise with angular velocity omega. A dashed line from the center to the point of contact with the surface is shown.](b40a0e0088ffd4376c6cd0447ea6f004_img.jpg)

Diagram of a ball of radius R on a horizontal surface. The ball is moving to the right with velocity V and rotating clockwise with angular velocity omega. A dashed line from the center to the point of contact with the surface is shown.

Fig. 8.80

For the reasonable values of  $h = 1$  m and  $\ell = 10$  cm, we obtain  $H \approx 3$  mm, which is quite small. You should try this with a pencil to convince yourself that even this small distance can yield the desired (or rather, undesired) half rotation.

#### 8.24. Sliding to rolling

- (a) Define all linear quantities to be positive to the right, and all angular quantities to be positive clockwise, as shown in Fig. 8.80. Then, for example, the friction force  $F_f$  is negative. The friction force slows down the translational motion and speeds up the rotational motion, according to

$$F_f = ma, \quad \text{and} \quad -F_f R = I\alpha. \quad (8.148)$$

Eliminating  $F_f$ , and using  $I = \beta mR^2$ , gives  $a = -\beta R\alpha$ . Integrating this over time, up to the time when the ball stops slipping, gives

$$\Delta V = -\beta R \Delta \omega. \quad (8.149)$$

Note that we could have obtained this by simply using the impulse equation, Eq. (8.61). Using  $\Delta V = V_f - V_0$ , and  $\Delta \omega = \omega_f - \omega_0 = \omega_f$ , and also  $\omega_f = V_f/R$  (the nonslipping condition), Eq. (8.149) gives

$$V_f = \frac{V_0}{1 + \beta}, \quad (8.150)$$

independent of the nature of  $F_f$ .  $F_f$  can depend on position, time, speed, or anything else. The relation  $a = -\beta R\alpha$ , and hence also Eq. (8.149), will still be true at all times.

**REMARK:** We can also calculate  $\tau$  and  $L$  relative to a dot painted on the ground that is the contact point at a given instant. There is zero torque relative to this point. To find  $L$ , we must add the  $L$  of the CM and the  $L$  relative to the CM. Therefore,  $\tau = dL/dt$  gives  $0 = (d/dt)(mvR + \beta mR^2\omega)$ , and so  $a = -\beta R\alpha$ , as above. ♣

Using Eq. (8.150), and also the relation  $\omega_f = V_f/R$ , the loss in kinetic energy is

$$\begin{aligned} \Delta K &= \frac{1}{2}mV_0^2 - \left( \frac{1}{2}mV_f^2 + \frac{1}{2}I\omega_f^2 \right) \\ &= \frac{1}{2}mV_0^2 \left( 1 - \frac{1}{(1 + \beta)^2} - \frac{\beta}{(1 + \beta)^2} \right) \\ &= \frac{1}{2}mV_0^2 \left( \frac{\beta}{1 + \beta} \right). \end{aligned} \quad (8.151)$$

For  $\beta \rightarrow 0$ , no energy is lost, which makes sense. And for  $\beta \rightarrow \infty$  (a spool sliding on its axle), all the energy is lost, which also makes sense, because we essentially have a sliding block which can't rotate.

- (b) Let's first find  $t$ . The friction force is  $F_f = -\mu mg$ , so  $F = ma$  gives  $-\mu g = a$ . Therefore,  $\Delta V = at = -\mu g t$ . But Eq. (8.150) says that  $\Delta V \equiv V_f - V_0 = -V_0\beta/(1 + \beta)$ . Therefore,

$$t = \frac{\beta}{(1 + \beta)} \cdot \frac{V_0}{\mu g}. \quad (8.152)$$

For  $\beta \rightarrow 0$ , we have  $t \rightarrow 0$ , which makes sense. And for  $\beta \rightarrow \infty$ , we have  $t \rightarrow V_0/(\mu g)$ , which equals the time a sliding block would take to stop.

Let's now find  $d$ . We have  $d = V_0 t + (1/2)at^2$ . Using  $a = -\mu g$ , and plugging in the  $t$  from Eq. (8.152), we obtain

$$d = \frac{\beta(2 + \beta)}{(1 + \beta)^2} \cdot \frac{V_0^2}{2\mu g}. \quad (8.153)$$

The two extreme cases for  $\beta$  check here.

To calculate the work done by friction, we might be tempted to write down the product  $F_f d$ , with  $F_f = -\mu mg$  and  $d$  given in Eq. (8.153). But the result doesn't equal the loss in kinetic energy calculated in Eq. (8.151). What's wrong with this reasoning? The error is that the friction force does not act over a distance  $d$ . To find the distance over which  $F_f$  acts, we must find how far the surface of the ball moves relative to the ground. The speed of a dot on the ball that is instantaneously the contact point is  $V_{\text{rel}}(t) = V(t) - R\omega(t) = (V_0 + at) - R\alpha t$ . Using  $\alpha = -a/\beta R$  and  $a = -\mu g$ , this becomes

$$V_{\text{rel}}(t) = V_0 - \frac{1 + \beta}{\beta} \mu g t. \quad (8.154)$$

Integrating this from  $t = 0$  to the  $t$  given in Eq. (8.152) gives

$$d_{\text{rel}} = \int V_{\text{rel}}(t) dt = \frac{\beta}{1 + \beta} \cdot \frac{V_0^2}{2\mu g}. \quad (8.155)$$

The work done by friction is  $F_f d_{\text{rel}} = -\mu mg d_{\text{rel}}$ , which does indeed give the loss in kinetic energy given in Eq. (8.151).

#### 8.25. Lots of sticks

Consider the collision between two sticks. Let  $V$  be the speed of the contact point on the heavy one. Since this stick is essentially infinitely heavy, we may consider it to be an infinitely heavy ball, moving at speed  $V$ . The rotational degree of freedom of the heavy stick is irrelevant, as far as the light stick is concerned. We can therefore invoke the result of Problem 8.19 to say that the relative speed of the contact points is the same before and after the collision. This implies that the contact point on the light stick picks up a speed of  $2V$ , because the heavy stick is essentially unaffected by the collision and keeps moving at speed  $V$ .

Let us now find the speed of the other end of the light stick. This stick receives an impulse from the heavy stick, so we can apply Eq. (8.61) to the light stick to obtain

$$\Delta L = r \Delta p \implies \beta m r^2 \omega = r(m v_{\text{CM}}) \implies r\omega = \frac{v_{\text{CM}}}{\beta}. \quad (8.156)$$

The speed of the struck (top) end is  $v_{\text{top}} = r\omega + v_{\text{CM}}$ , because the CM speed adds to the rotational speed. The speed of the other (bottom) end is  $v_{\text{bot}} = r\omega - v_{\text{CM}}$ , because the CM speed subtracts from the rotational speed.<sup>17</sup> The ratio of these speeds is

$$\frac{v_{\text{bot}}}{v_{\text{top}}} = \frac{\frac{v_{\text{CM}}}{\beta} - v_{\text{CM}}}{\frac{v_{\text{CM}}}{\beta} + v_{\text{CM}}} = \frac{1 - \beta}{1 + \beta}. \quad (8.157)$$

This is a general result whenever you strike the end of a stick with any force. In the present problem, we have  $v_{\text{top}} = 2V$ . Therefore,

$$v_{\text{bot}} = V \left( \frac{2(1 - \beta)}{1 + \beta} \right). \quad (8.158)$$

<sup>17</sup> Since  $\beta \leq 1$  for any real stick, we have  $r\omega = v_{\text{CM}}/\beta \geq v_{\text{CM}}$ . Therefore,  $r\omega - v_{\text{CM}}$  is greater than or equal to zero.

The same analysis holds for all the other collisions. Therefore, the bottom ends of the sticks move with speeds that form a geometric progression with ratio  $2(1 - \beta)/(1 + \beta)$ . If this ratio is less than 1 (that is, if  $\beta > 1/3$ ), then the speeds go to zero as  $n \rightarrow \infty$ . If it is greater than 1 (that is, if  $\beta < 1/3$ ), then the speeds go to infinity as  $n \rightarrow \infty$ . If it equals 1 (that is, if  $\beta = 1/3$ ), then the speeds remain equal to  $V$  and are thus independent of  $n$ , as we wanted to show. A uniform stick has  $\beta = 1/3$  relative to its center (which is usually written in the form  $I = m\ell^2/12$ , where  $\ell = 2r$ ).