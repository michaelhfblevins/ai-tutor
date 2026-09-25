# Chapter 13 4-vectors

We now come to a very powerful concept in relativity, that of *4-vectors*. Although it's possible to derive everything in Special Relativity without the use of 4-vectors (and indeed, this is the route, give or take, that we've taken in the previous two chapters), they are extremely helpful in making calculations simpler and concepts more transparent.

I have chosen to postpone the full introduction to 4-vectors until now, in order to make it clear that everything in Special Relativity can be derived without them. In encountering relativity for the first time, it's nice to know that no "advanced" techniques are required. But now that you've seen everything once, let's go back and derive various things in an easier way.

Although Special Relativity doesn't require knowledge of 4-vectors, the subject of General Relativity definitely requires a firm understanding of *tensors*, which are the generalization of 4-vectors. We won't have time to go very deeply into GR in Chapter 14, so you'll just have to accept this fact. But suffice it to say that an eventual understanding of GR requires a solid foundation in the 4-vectors of Special Relativity. So let's see what they're all about.

## 13.1 Definition of 4-vectors

**Definition 13.1** *The 4-tuplet,  $A = (A_0, A_1, A_2, A_3)$ , is a "4-vector" if the  $A_i$  transform under a Lorentz transformation in the same way as  $(c dt, dx, dy, dz)$  do. In other words,  $A$  is a 4-vector if it transforms like (assuming the Lorentz transformation is along the  $x$  direction; see Fig. 13.1):*

![Diagram showing two coordinate systems, S and S', illustrating a Lorentz transformation. System S has axes x and y. System S' is moving with velocity v relative to S along the x-axis. The x' axis is tilted relative to the x axis, and the y' axis is parallel to the y axis.](feb84871adbaf20be419c8086e1e1131_img.jpg)

Diagram showing two coordinate systems, S and S', illustrating a Lorentz transformation. System S has axes x and y. System S' is moving with velocity v relative to S along the x-axis. The x' axis is tilted relative to the x axis, and the y' axis is parallel to the y axis.

Fig. 13.1

$$\begin{aligned} A_0 &= \gamma(A'_0 + (v/c)A'_1), \\ A_1 &= \gamma(A'_1 + (v/c)A'_0), \\ A_2 &= A'_2, \\ A_3 &= A'_3. \end{aligned} \tag{13.1}$$

REMARKS:

1. Similar equations must hold, of course, for Lorentz transformations in the  $y$  and  $z$  directions.
2. Additionally, the last three components must be a vector in 3-space. That is, they must transform like a usual vector under rotations in 3-space. So the full definition of a 4-

- vector is that it must transform like  $(c\,dt, dx, dy, dz)$  under Lorentz transformations *and* rotations.
3. We'll use a capital italic letter to denote a 4-vector. A bold-face letter will denote, as usual, a vector in 3-space.
4. Lest we get tired of writing the  $c$ 's over and over, we'll work in units where  $c = 1$  from now on.
5. The first component of a 4-vector is called the "time" component. The other three are the "space" components.
6. The components in  $(dt, dx, dy, dz)$  are sometimes referred to as  $(dx_0, dx_1, dx_2, dx_3)$ . Also, some treatments use the indices "1" through "4," with "4" being the "time" component. But we'll use "0" through "3."
7. The  $A_i$  may be functions of  $v$ , the  $dx_i$ , the  $x_i$  and their derivatives, and any invariants (that is, frame-independent quantities) such as the mass  $m$ .
8. 4-vectors are the obvious generalization of vectors in regular space. A vector in three dimensions, after all, is something that transforms under a rotation just like  $(dx, dy, dz)$  does. We have simply generalized a 3-D rotation to a 4-D Lorentz transformation. ♣

## 13.2 Examples of 4-vectors

So far, we have only one 4-vector at our disposal, namely  $(dt, dx, dy, dz)$ . What are some others? Well,  $(7dt, 7dx, 7dy, 7dz)$  certainly works, as does any other constant multiple of  $(dt, dx, dy, dz)$ . Indeed,  $m(dt, dx, dy, dz)$  is a 4-vector, because  $m$  is an invariant. But how about  $A = (dt, 2dx, dy, dz)$ ? No, this isn't a 4-vector, because on one hand it must transform (assuming it's a 4-vector) like

$$\begin{aligned} dt &\equiv A_0 = \gamma(A'_0 + vA'_1) \equiv \gamma(dt' + v(2dx')), \\ 2dx &\equiv A_1 = \gamma(A'_1 + vA'_0) \equiv \gamma(2dx' + vdt'), \\ dy &\equiv A_2 = A'_2 \equiv dy', \\ dz &\equiv A_3 = A'_3 \equiv dz', \end{aligned} \tag{13.2}$$

from the definition of a 4-vector. But on the other hand, it must transform like

$$\begin{aligned} dt &= \gamma(dt' + v\,dx'), \\ 2dx &= 2\gamma(dx' + v\,dt'), \\ dy &= dy', \\ dz &= dz', \end{aligned} \tag{13.3}$$

because this is how the  $dx_i$  transform. The two preceding sets of equations are inconsistent, so  $A = (dt, 2dx, dy, dz)$  is not a 4-vector. Note that if we had instead considered the 4-tuplet,  $A = (dt, dx, 2dy, dz)$ , then the two preceding equations would have been consistent. But if we had then looked at how  $A$  transforms under a Lorentz transformation in the  $y$  direction, we would have found that it is not a 4-vector.

The moral of this story is that the above definition of a 4-vector is a nontrivial one because there are two possible ways that a 4-tuplet can transform. It can transform according to the 4-vector definition, as in Eq. (13.2). Or it can transform simply by having each of the  $A_i$  separately transform (using how the  $dx_i$ , or whatever else they may be made of, transform), as in Eq. (13.3). Only for certain special 4-tuplets do these two methods give the same result. By definition, we label these special 4-tuplets as 4-vectors.

Let's now construct some less trivial examples of 4-vectors. In constructing these, we'll make abundant use of the fact that the proper-time interval,  $d\tau \equiv \sqrt{dt^2 - d\mathbf{r}^2}$ , is an invariant.

- **Velocity 4-vector:** We can divide  $(dt, dx, dy, dz)$  by  $d\tau$ , where  $d\tau$  is the proper time between two events (the same two events that yielded the  $dt$ , etc.). The result is indeed a 4-vector, because  $d\tau$  is independent of the frame in which it is measured. Using  $d\tau = dt/\gamma$ , we obtain

$$V \equiv \frac{1}{d\tau}(dt, dx, dy, dz) = \gamma \left( 1, \frac{dx}{dt}, \frac{dy}{dt}, \frac{dz}{dt} \right) = (\gamma, \gamma \mathbf{v}). \quad (13.4)$$

This is known as the *velocity 4-vector*. In the rest frame of the object we have  $\mathbf{v} = \mathbf{0}$ , so  $V$  reduces to  $V = (1, 0, 0, 0)$ . With the  $c$ 's, we have  $V = (\gamma c, \gamma \mathbf{v})$ .

- **Energy–momentum 4-vector:** If we multiply the velocity 4-vector by the invariant  $m$ , we obtain another 4-vector,

$$P \equiv mV = (\gamma m, \gamma m \mathbf{v}) = (E, \mathbf{p}), \quad (13.5)$$

which is known as the *energy–momentum 4-vector* (or the *4-momentum* for short), for obvious reasons. In the rest frame of the object,  $P$  reduces to  $P = (m, 0, 0, 0)$ . With the  $c$ 's, we have  $P = (\gamma mc, \gamma m \mathbf{v}) = (E/c, \mathbf{p})$ . Some treatments multiply through by  $c$ , so that the 4-momentum is  $(E, \mathbf{p}c)$ .

- **Acceleration 4-vector:** We can also take the derivative of the velocity 4-vector with respect to  $\tau$ . The result is indeed a 4-vector, because taking the derivative entails taking the (infinitesimal) difference between two 4-vectors (which results in a 4-vector because Eq. (13.1) is linear), and then dividing by the invariant  $d\tau$  (which again results in a 4-vector). Using  $d\tau = dt/\gamma$ , we obtain

$$A \equiv \frac{dV}{d\tau} = \frac{d}{d\tau}(\gamma, \gamma \mathbf{v}) = \gamma \left( \frac{d\gamma}{dt}, \frac{d(\gamma \mathbf{v})}{dt} \right). \quad (13.6)$$

Using  $d\gamma/dt = v\dot{v}/(1 - v^2)^{3/2} = \gamma^3 v\dot{v}$ , we have

$$A = (\gamma^4 v\dot{v}, \gamma^4 v\dot{v} \mathbf{v} + \gamma^2 \mathbf{a}), \quad (13.7)$$

where  $\mathbf{a} \equiv d\mathbf{v}/dt$ .  $A$  is known as the *acceleration 4-vector*. In the rest frame of the object (or, rather, in the instantaneous inertial frame),  $A$  reduces to  $A = (0, \mathbf{a})$ . As we

usually do, we'll pick the velocity  $\mathbf{v}$  to point in the  $x$  direction. That is,  $\mathbf{v} = (v_x, 0, 0)$ . This means that  $v = v_x$ , and also that  $\dot{v} = \dot{v}_x \equiv a_x$ .<sup>1</sup> Equation (13.7) then becomes

$$\begin{aligned} A &= (\gamma^4 v_x a_x, \gamma^4 v_x^2 a_x + \gamma^2 a_x, \gamma^2 a_y, \gamma^2 a_z) \\ &= (\gamma^4 v_x a_x, \gamma^4 a_x, \gamma^2 a_y, \gamma^2 a_z). \end{aligned} \quad (13.8)$$

We can keep taking derivatives with respect to  $\tau$  to create other 4-vectors, but these have little relevance in the real world.

- **Force 4-vector:** We define the *force 4-vector* as

$$F \equiv \frac{dP}{d\tau} = \gamma \left( \frac{dE}{dt}, \frac{d\mathbf{p}}{dt} \right) = \gamma \left( \frac{dE}{dt}, \mathbf{f} \right), \quad (13.9)$$

where  $\mathbf{f} \equiv d(\gamma m \mathbf{v})/dt$  is the usual 3-force. We'll use  $\mathbf{f}$  instead of  $\mathbf{F}$  in this chapter, to avoid confusion with the 4-force,  $F$ . In the case where  $m$  is constant,<sup>2</sup>  $F$  can be written as  $F = d(mV)/d\tau = m dV/d\tau = mA$ . We therefore still have a nice “ $F$  equals  $mA$ ” law of physics, but it's now a 4-vector equation instead of the old 3-vector one. In terms of the acceleration 4-vector, we can use Eqs. (13.7) and (13.8) to write (if  $m$  is constant)

$$\begin{aligned} F &= mA = m(\gamma^4 v \dot{v}, \gamma^4 v \dot{v} \mathbf{v} + \gamma^2 \mathbf{a}) \\ &= m(\gamma^4 v_x a_x, \gamma^4 a_x, \gamma^2 a_y, \gamma^2 a_z). \end{aligned} \quad (13.10)$$

Combining this with Eq. (13.9), we see that the 3-force is

$$\mathbf{f} = m(\gamma^3 a_x, \gamma a_y, \gamma a_z), \quad (13.11)$$

in agreement with Eq. (12.60). In the rest frame of the object (or, rather, the instantaneous inertial frame), the  $F$  in Eq. (13.9) reduces to  $F = (0, \mathbf{f})$ , because  $dE/dt = 0$  when  $v = 0$ , as you can verify. Also, in the rest frame of the object, the  $mA$  in Eq. (13.10) reduces to  $mA = (0, m\mathbf{a})$ . So  $F = mA$  reduces to the familiar  $\mathbf{f} = m\mathbf{a}$ .

## 13.3 Properties of 4-vectors

The appealing thing about 4-vectors is that they have many useful properties. Let's look at some of these.

- **Linear combinations:** If  $A$  and  $B$  are 4-vectors, then  $C \equiv aA + bB$  is also a 4-vector. This is true because the transformations in Eq. (13.1) are linear (as we noted above

<sup>1</sup> The acceleration vector  $\mathbf{a}$  is free to point in any direction, but you can check that the 0's in  $\mathbf{v}$  lead to  $\dot{v} = a_x$ . See Exercise 13.5.

<sup>2</sup> The mass  $m$  wouldn't be constant if the object were being heated, or if extra mass were being added to it. We won't concern ourselves with such cases here.

when deriving the acceleration 4-vector). This linearity implies that the transformation of, say, the time component is

$$\begin{aligned} C_0 &\equiv (aA + bB)_0 = aA_0 + bB_0 = a(A'_0 + vA'_1) + b(B'_0 + vB'_1) \\ &= (aA'_0 + bB'_0) + v(aA'_1 + bB'_1) \\ &\equiv C'_0 + vC'_1, \end{aligned} \quad (13.12)$$

which is the proper transformation for the time component of a 4-vector. Likewise for the other components. This property holds, of course, just as it does for linear combinations of vectors in 3-space.

- **Inner-product invariance:** Consider two arbitrary 4-vectors,  $A$  and  $B$ . Define their inner product to be

$$A \cdot B \equiv A_0B_0 - A_1B_1 - A_2B_2 - A_3B_3 \equiv A_0B_0 - \mathbf{A} \cdot \mathbf{B}. \quad (13.13)$$

Then  $A \cdot B$  is invariant. That is, it is independent of the frame in which it is calculated. This can be shown by direct calculation, using the transformations in Eq. (13.1):

$$\begin{aligned} A \cdot B &\equiv A_0B_0 - A_1B_1 - A_2B_2 - A_3B_3 \\ &= (\gamma(A'_0 + vA'_1))(\gamma(B'_0 + vB'_1)) - (\gamma(A'_1 + vA'_0))(\gamma(B'_1 + vB'_0)) \\ &\quad - A'_2B'_2 - A'_3B'_3 \\ &= \gamma^2(A'_0B'_0 + v(A'_0B'_1 + A'_1B'_0) + v^2A'_1B'_1) \\ &\quad - \gamma^2(A'_1B'_1 + v(A'_1B'_0 + A'_0B'_1) + v^2A'_0B'_0) - A'_2B'_2 - A'_3B'_3 \\ &= A'_0B'_0(\gamma^2 - \gamma^2v^2) - A'_1B'_1(\gamma^2 - \gamma^2v^2) - A'_2B'_2 - A'_3B'_3 \\ &= A'_0B'_0 - A'_1B'_1 - A'_2B'_2 - A'_3B'_3 \\ &\equiv A' \cdot B'. \end{aligned} \quad (13.14)$$

The importance of this result cannot be overstated. This invariance is analogous to the invariance of the inner product,  $\mathbf{A} \cdot \mathbf{B}$ , for rotations in 3-space. The above inner product is also invariant under rotations in 3-space, because it involves the combination  $\mathbf{A} \cdot \mathbf{B}$ . The minus signs in the inner product may seem a little strange. But what we want is a combination of two arbitrary vectors that is invariant under a Lorentz transformation, because such combinations are very useful in seeing what's going on in a system. The nature of the Lorentz transformations demands that there be opposite signs in the inner product, so that's the way it is.

- **Norm:** As a corollary to the invariance of the inner product, we can look at the inner product of a 4-vector with itself, which is by definition the square of the norm. We see that

$$A^2 \equiv A \cdot A \equiv A_0A_0 - A_1A_1 - A_2A_2 - A_3A_3 = A_0^2 - |\mathbf{A}|^2 \quad (13.15)$$

is invariant. This is analogous to the invariance of the norm  $\sqrt{\mathbf{A} \cdot \mathbf{A}}$  for rotations in 3-space. Special cases of the invariance of the 4-vector norm are the invariance of  $c^2 dt^2 - dx^2$  and of  $E^2 - p^2 c^2$ .

- **A theorem:** Here's a nice little theorem:

*If a certain one of the components of a 4-vector is 0 in every frame, then all four components are 0 in every frame.*

**Proof:** If one of the space components (say,  $A_1$ ) is 0 in every frame, then the other space components must also be 0 in every frame, because otherwise a rotation would make  $A_1 \neq 0$ . Also, the time component  $A_0$  must be 0 in every frame, because otherwise a Lorentz transformation in the  $x$  direction would make  $A_1 \neq 0$ .

If the time component,  $A_0$ , is 0 in every frame, then the space components must also be 0 in every frame, because otherwise a Lorentz transformation in the appropriate direction would make  $A_0 \neq 0$ . ■

If someone comes along and says that she has a vector in 3-space that has no  $x$  component, no matter how you rotate the axes, then you would certainly say that the vector must obviously be the zero vector. The situation in Lorentzian 4-space is the same, because all the coordinates get intertwined with each other in the Lorentz (and rotation) transformations.

## 13.4 Energy, momentum

### 13.4.1 Norm

Many useful things arise from the fact that the  $P$  in Eq. (13.5) is a 4-vector. The invariance of the norm implies that  $P \cdot P = E^2 - |\mathbf{p}|^2$  is invariant. If we are dealing with only one particle, we can determine the value of  $P^2$  by conveniently working in the rest frame of the particle (so that  $\mathbf{v} = \mathbf{0}$ ), which gives

$$E^2 - p^2 = m^2, \quad (13.16)$$

or  $E^2 - p^2 c^2 = m^2 c^4$ , with the  $c$ 's. We already knew this, of course, from just writing out  $E^2 - p^2 = \gamma^2 m^2 - \gamma^2 m^2 v^2 = m^2$ .

For a collection of particles, knowledge of the norm is very useful. If a process involves many particles, then we can say that for *any* subset of the particles,

$$\left(\sum E\right)^2 - \left(\sum \mathbf{p}\right)^2 \text{ is invariant,} \quad (13.17)$$

because this is the norm of the sum of the energy–momentum 4-vectors of the chosen particles. The sum is again a 4-vector, due to the linearity of Eq. (13.1). What is the value of the invariant in Eq. (13.17)? The most concise description (which is basically a tautology) is that it is the square of the energy in the CM frame, that is, in the frame in which  $\sum \mathbf{p} = \mathbf{0}$ . For one particle, this reduces to  $m^2$ . Note that the sums are taken before squaring in Eq. (13.17). Squaring before adding would simply give the sum of the squares of the masses.

### 13.4.2 Transformations of $E$ and $\mathbf{p}$

We already know how the energy and momentum transform (see Section 12.2), but let's derive the transformation again here in a very quick and easy manner. We know that  $(E, p_x, p_y, p_z)$  is a 4-vector. So it must transform according to Eq. (13.1). Therefore, for a Lorentz transformation in the  $x$  direction, we have

$$\begin{aligned} E &= \gamma(E' + vp'_x), \\ p_x &= \gamma(p'_x + vE'/c^2), \\ p_y &= p'_y, \\ p_z &= p'_z, \end{aligned} \tag{13.18}$$

in agreement with Eq. (12.27). That's all there is to it. The fact that  $E$  and  $\mathbf{p}$  are part of the same 4-vector provides an easy way to see that if one of them is conserved (in every frame) in a collision, then the other is also. Consider an interaction among a set of particles, and look at the 4-vector,  $\Delta P \equiv P_{\text{after}} - P_{\text{before}}$ . If  $E$  is conserved in every frame, then the time component of  $\Delta P$  is 0 in every frame. But then the theorem in Section 13.3 says that all four components of  $\Delta P$  are 0 in every frame. Therefore,  $\mathbf{p}$  is conserved. Likewise for the case where one of the  $p_i$  is known to be conserved.

## 13.5 Force and acceleration

Throughout this section, we'll deal with objects with constant mass, which we'll call "particles." The treatment here can be generalized to cases where the mass changes (for example, the object is being heated, or extra mass is being dumped on it), but we won't concern ourselves with these.

### 13.5.1 Transformation of forces

Let's first look at the force 4-vector in the instantaneous inertial frame of a given particle (frame  $S'$ ). Equation (13.9) gives

$$F' = \gamma \left( \frac{dE'}{dt}, \mathbf{f}' \right) = (0, \mathbf{f}'). \tag{13.19}$$

The first component is zero because  $dE'/dt = d(m/\sqrt{1 - v'^2})/dt$ , and this contains a factor of  $v'$ , which is zero in this frame. Equivalently, you can just use Eq. (13.10), with a speed of zero.

We can now write down two expressions for the 4-force,  $F$ , in another frame,  $S$ , in which the particle moves with speed  $v$  in the  $x$  direction. First, since  $F$

is a 4-vector, it transforms according to Eq. (13.1). We therefore have, using Eq. (13.19),

$$\begin{aligned} F_0 &= \gamma(F'_0 + vF'_1) = \gamma vf'_x, \\ F_1 &= \gamma(F'_1 + vF'_0) = \gamma f'_x, \\ F_2 &= F'_2 = f'_y, \\ F_3 &= F'_3 = f'_z. \end{aligned} \tag{13.20}$$

But second, from the definition in Eq. (13.9), we also have

$$\begin{aligned} F_0 &= \gamma dE/dt, \\ F_1 &= \gamma f_x, \\ F_2 &= \gamma f_y, \\ F_3 &= \gamma f_z. \end{aligned} \tag{13.21}$$

Combining Eqs. (13.20) and (13.21), we obtain

$$\begin{aligned} dE/dt &= vf'_x, \\ f_x &= f'_x, \\ f_y &= f'_y/\gamma, \\ f_z &= f'_z/\gamma. \end{aligned} \tag{13.22}$$

We therefore recover the results of Section 12.5.3. The longitudinal force is the same in both frames, but the transverse forces are larger by a factor of  $\gamma$  in the particle’s frame. Hence,  $f_y/f_x$  decreases by a factor of  $\gamma$  when going from the particle’s frame to the lab frame (see Fig. 13.2 and Fig. 13.3). And as a bonus, the  $F_0$  component in Eq. (13.22) tells us (after multiplying through by  $dt$ ) that  $dE = f_x dx$ , which is the work–energy result. In other words, using  $f_x \equiv dp_x/dt$ , we have just derived again the result,  $dE/dx = f_x = dp/dt$ , that we derived in Section 12.5.1.

As noted in the first remark in Section 12.5.3, we can’t switch the  $S$  and  $S'$  frames and write  $f'_y = f_y/\gamma$ . When talking about the forces on a particle, there is indeed one preferred reference frame, namely that of the particle. All frames are not equivalent here. When forming all of our 4-vectors in Section 13.2, we explicitly used the  $d\tau$ ,  $dt$ ,  $dx$ , etc., from two events, and it was understood that these two events were located at the particle.

### 13.5.2 Transformation of accelerations

The procedure here is similar to the above treatment of the force. Let’s first look at the acceleration 4-vector in the instantaneous inertial frame of a given particle

![Diagram for Fig. 13.2 showing a right triangle in frame S' with hypotenuse f' and vertical side f'_y. Frame S is moving left relative to S'.](dd4133bf58db59326d809305d98c357c_img.jpg)

A right triangle is shown in a coordinate system labeled '(frame S')'. The hypotenuse is labeled  $\mathbf{f}'$ . The vertical side is labeled  $f'_y$ . The horizontal side is labeled  $f'_x$ . Below the triangle, a stick figure labeled  $S$  is shown with an arrow pointing to the left, indicating that frame  $S$  is moving to the left relative to frame  $S'$ .

Diagram for Fig. 13.2 showing a right triangle in frame S' with hypotenuse f' and vertical side f'\_y. Frame S is moving left relative to S'.

Fig. 13.2

![Diagram for Fig. 13.3 showing a right triangle in frame S with hypotenuse f and vertical side f_y = f'_y / gamma. Frame S is moving right relative to S'.](70da27ab08887c2187ff069604910506_img.jpg)

A right triangle is shown in a coordinate system labeled '(frame S)'. The hypotenuse is labeled  $\mathbf{f}$ . The vertical side is labeled  $f_y = \frac{f'_y}{\gamma}$ . The horizontal side is labeled  $f_x = f'_x$ . Below the triangle, a stick figure labeled  $S$  is shown with an arrow pointing to the right, indicating that frame  $S$  is moving to the right relative to frame  $S'$ .

Diagram for Fig. 13.3 showing a right triangle in frame S with hypotenuse f and vertical side f\_y = f'\_y / gamma. Frame S is moving right relative to S'.

Fig. 13.3

(frame  $S'$ ). Equation (13.7) or Eq. (13.8) gives

$$A' = (0, \mathbf{a}'), \quad (13.23)$$

because  $v' = 0$  in  $S'$ .

We can now write down two expressions for the 4-acceleration,  $A$ , in another frame,  $S$ . First, since  $A$  is a 4-vector, it transforms according to Eq. (13.1). So we have, using Eq. (13.23),

$$\begin{aligned} A_0 &= \gamma(A'_0 + vA'_1) = \gamma v a'_x, \\ A_1 &= \gamma(A'_1 + vA'_0) = \gamma a'_x, \\ A_2 &= A'_2 = a'_y, \\ A_3 &= A'_3 = a'_z. \end{aligned} \quad (13.24)$$

But second, from the expression in Eq. (13.8), we also have

$$\begin{aligned} A_0 &= \gamma^4 v a_x, \\ A_1 &= \gamma^4 a_x, \\ A_2 &= \gamma^2 a_y, \\ A_3 &= \gamma^2 a_z. \end{aligned} \quad (13.25)$$

Combining Eqs. (13.24) and (13.25), we obtain

$$\begin{aligned} a_x &= a'_x / \gamma^3, \\ a_x &= a'_x / \gamma^3, \\ a_y &= a'_y / \gamma^2, \\ a_z &= a'_z / \gamma^2. \end{aligned} \quad (13.26)$$

![Diagram for Fig. 13.4 showing a right triangle in frame S'. The horizontal leg is labeled a'_x, the vertical leg is labeled a'_y, and the hypotenuse is labeled a'. A dashed line extends horizontally from the origin. Below the triangle, a stick figure labeled S is shown with an arrow pointing to the left, indicating the relative velocity v between frames S and S'.](d8541b4f1b47e25669964b24232bd69f_img.jpg)

Diagram for Fig. 13.4 showing a right triangle in frame S'. The horizontal leg is labeled a'\_x, the vertical leg is labeled a'\_y, and the hypotenuse is labeled a'. A dashed line extends horizontally from the origin. Below the triangle, a stick figure labeled S is shown with an arrow pointing to the left, indicating the relative velocity v between frames S and S'.

Fig. 13.4

![Diagram for Fig. 13.5 showing a right triangle in frame S. The horizontal leg is labeled a_x = a'_x / gamma^3, the vertical leg is labeled a_y = a'_y / gamma^2, and the hypotenuse is labeled a. A dashed line extends horizontally from the origin. Below the triangle, a stick figure labeled S is shown with an arrow pointing to the right, indicating the relative velocity v between frames S and S'.](1a22b5158fcf0b0d314d9161e935be53_img.jpg)

Diagram for Fig. 13.5 showing a right triangle in frame S. The horizontal leg is labeled a\_x = a'\_x / gamma^3, the vertical leg is labeled a\_y = a'\_y / gamma^2, and the hypotenuse is labeled a. A dashed line extends horizontally from the origin. Below the triangle, a stick figure labeled S is shown with an arrow pointing to the right, indicating the relative velocity v between frames S and S'.

Fig. 13.5

(The first two equations here are redundant.) We therefore again recover the results of Section 12.5.3. We see that  $a_y/a_x$  increases by a factor of  $\gamma^3/\gamma^2 = \gamma$  when going from the particle's frame to the lab frame (see Fig. 13.4 and Fig. 13.5). This is the opposite of the effect on  $f_y/f_x$ .<sup>3</sup> This difference makes it clear that an  $\mathbf{f} = m\mathbf{a}$  law wouldn't make any sense. If it were true in one frame, then it wouldn't be true in another. Note that the increase in  $a_y/a_x$  in going to the lab frame is consistent with length contraction, as the "Bead on a rod" example in Section 12.5.3 showed.

<sup>3</sup> In a nutshell, this difference is due to the fact that  $\gamma$  changes with time. When talking about the acceleration 4-vector, there are  $\gamma$ 's that we have to differentiate; see Eq. (13.6). This isn't the case with the force 4-vector, because the  $\gamma$  is absorbed into the definition of  $\mathbf{p} \equiv \gamma m \mathbf{v}$ ; see Eq. (13.9). This is what leads to the different powers of  $\gamma$  in Eq. (13.25), in contrast with the identical powers in Eq. (13.21).

**Example (Acceleration for circular motion):** A particle moves with constant speed  $v$  around the circle  $x^2 + y^2 = r^2$ ,  $z = 0$ , in the lab frame. At the instant the particle crosses the negative  $y$  axis (see Fig. 13.6), find the 3-acceleration and 4-acceleration in both the lab frame and the instantaneous inertial frame of the particle (with axes chosen parallel to the lab's axes).

**Solution:** Let the lab frame be  $S$ , and let the particle's instantaneous inertial frame be  $S'$  when it crosses the negative  $y$  axis. Then  $S$  and  $S'$  are related by a Lorentz transformation in the  $x$  direction. The 3-acceleration in  $S$  is simply

$$\mathbf{a} = (0, v^2/r, 0). \quad (13.27)$$

There's nothing fancy going on here; the nonrelativistic proof of  $a = v^2/r$  works just fine again in the relativistic case. Equation (13.7) or (13.8) then gives the 4-acceleration in  $S$  as

$$A = (0, 0, \gamma^2 v^2/r, 0). \quad (13.28)$$

To find the acceleration vectors in  $S'$ , we can use the fact that  $S'$  and  $S$  are related by a Lorentz transformation in the  $x$  direction. This means that the  $A_2$  component of the 4-acceleration is unchanged. So the 4-acceleration in  $S'$  is also

$$A' = A = (0, 0, \gamma^2 v^2/r, 0). \quad (13.29)$$

In the particle's frame,  $\mathbf{a}'$  is the space part of  $A$  (using Eq. (13.7) or (13.8), with  $v = 0$  and  $\gamma = 1$ ). Therefore, the 3-acceleration in  $S'$  is

$$\mathbf{a}' = (0, \gamma^2 v^2/r, 0). \quad (13.30)$$

Note that our results for  $\mathbf{a}$  and  $\mathbf{a}'$  are consistent with Eq. (13.26).

**REMARK:** We can also arrive at the two factors of  $\gamma$  in  $\mathbf{a}'$  by using a simple time-dilation argument. We have

$$a'_y = \frac{d^2 y'}{d\tau^2} = \frac{d^2 y'}{d(t/\gamma)^2} = \gamma^2 \frac{d^2 y}{dt^2} = \gamma^2 \frac{v^2}{r}, \quad (13.31)$$

where we have used the fact that transverse lengths are the same in the two frames. ♣

![Figure 13.6: A diagram showing a circle centered at the origin of a Cartesian coordinate system with x and y axes. A particle is located at the bottom of the circle, on the negative y-axis. A velocity vector labeled 'v' points to the right (positive x direction) from this point.](d425c9f3a5e071fa7ec20d3905298cee_img.jpg)

Figure 13.6: A diagram showing a circle centered at the origin of a Cartesian coordinate system with x and y axes. A particle is located at the bottom of the circle, on the negative y-axis. A velocity vector labeled 'v' points to the right (positive x direction) from this point.

Fig. 13.6

## 13.6 The form of physical laws

One of the postulates of Special Relativity is that all inertial frames are equivalent. Therefore, if a physical law holds in one frame, then it must hold in all frames. Otherwise, it would be possible to differentiate between frames. As noted in

the previous section, the statement “ $\mathbf{f} = m\mathbf{a}$ ” cannot be a physical law. The two sides of the equation transform differently when going from one frame to another, so the statement cannot be true in all frames. If a statement has any chance of being true in all frames, it must involve only 4-vectors. Consider a 4-vector equation (say, “ $A = B$ ”) that is true in frame  $S$ . Then if we apply to this equation a Lorentz transformation (call it  $\mathcal{M}$ ) from  $S$  to another frame  $S'$ , we have

$$\begin{aligned} A &= B \\ \implies \mathcal{M}A &= \mathcal{M}B \\ \implies A' &= B'. \end{aligned} \quad (13.32)$$

The law is therefore also true in frame  $S'$ . Of course, there are many 4-vector equations that are simply not true in any frame (for example,  $F = P$ , or  $2P = 3P$ ). Only a small set of such equations (for example,  $F = mA$ ) are true in at least one frame, and hence in all frames.

Physical laws may also take the form of scalar equations, such as  $P \cdot P = m^2$ . A scalar is by definition a quantity that is frame-independent (as we have shown the inner product to be). So if a scalar statement is true in one inertial frame, then it is true in all inertial frames. Physical laws may also be higher-rank “tensor” equations, such as the ones that arise in electromagnetism and General Relativity. We won’t discuss tensors here, but suffice it to say that they may be thought of as things built up from 4-vectors. Scalars and 4-vectors are special cases of tensors.

All of this is exactly analogous to the situation in 3-D space. In Newtonian mechanics,  $\mathbf{f} = m\mathbf{a}$  is a possible law, because both sides are 3-vectors. But  $\mathbf{f} = m(2a_x, a_y, a_z)$  is not a possible law, because the right-hand side is not a 3-vector; it depends on which axis you label as the  $x$  axis. If a particle has acceleration  $a$  in the eastward direction, and if you happen to pick this as your  $x$  direction, then the force is  $2ma$  eastward. But if you happen to pick eastward as your  $y$  direction, then the force is  $ma$  eastward. It makes no sense for a law to give two different results based on your arbitrary choice of axis labels. An example of a frame-independent statement (under rotations) is the claim that a given stick has a length of 2 meters. This is fine, because it involves the norm, which is a scalar. But if you say that the stick has an  $x$  component of 1.7 meters, then this cannot be true in all frames.

God said to his cosmos directors,  
 “I’ve added some stringent selectors.  
 One is the clause  
 That your physical laws  
 Shall be written in terms of 4-vectors.”

## 13.7 Problems

### 13.1. Velocity addition \*

In  $A$ 's frame,  $B$  moves to the right with speed  $u$ , and  $C$  moves to the left with speed  $v$ . What is the speed of  $B$  with respect to  $C$ ? In other words, use 4-vectors to derive the velocity-addition formula.

### 13.2. Relative speed \*

In the lab frame, two particles move with speed  $v$  along the paths shown in Fig. 13.7. The angle between the trajectories is  $2\theta$ . What is the speed of one particle, as viewed by the other?

![Figure 13.7: A diagram showing two trajectories originating from a common point. One trajectory goes up and to the right at an angle theta above the horizontal dashed line, and the other goes down and to the right at an angle theta below the horizontal dashed line. Both trajectories are labeled with speed v.](59ad081fae425b10b1f309d574519b5c_img.jpg)

Figure 13.7: A diagram showing two trajectories originating from a common point. One trajectory goes up and to the right at an angle theta above the horizontal dashed line, and the other goes down and to the right at an angle theta below the horizontal dashed line. Both trajectories are labeled with speed v.

Fig. 13.7

### 13.3. Another relative speed \*

In the lab frame, particles  $A$  and  $B$  move with speeds  $u$  and  $v$  along the paths shown in Fig. 13.8. The angle between the trajectories is  $\theta$ . What is the speed of one particle, as viewed by the other?

![Figure 13.8: A diagram showing two trajectories originating from a common point. One trajectory, labeled A, goes horizontally to the right with speed u. The other trajectory, labeled B, goes up and to the right with speed v. The angle between the two trajectories is theta.](b131c67d68feeaf7a62f599176ac6a34_img.jpg)

Figure 13.8: A diagram showing two trajectories originating from a common point. One trajectory, labeled A, goes horizontally to the right with speed u. The other trajectory, labeled B, goes up and to the right with speed v. The angle between the two trajectories is theta.

Fig. 13.8

### 13.4. Acceleration for linear motion \*

A spaceship starts at rest with respect to frame  $S$  and accelerates with constant proper acceleration  $a$ . In Section 11.9, we showed that the speed of the spaceship with respect to  $S$  is given by  $v(\tau) = \tanh(a\tau)$ , where  $\tau$  is the spaceship's proper time (we have dropped the  $c$ 's). Let  $V$  be the spaceship's 4-velocity, and let  $A$  be its 4-acceleration. In terms of the proper time  $\tau$ :

- Find  $V$  and  $A$  in frame  $S$ , by explicitly using  $v(\tau) = \tanh(a\tau)$ .
- Write down  $V'$  and  $A'$  in the spaceship's frame,  $S'$ .
- Verify that  $V$  and  $V'$  transform like 4-vectors between the two frames. Likewise for  $A$  and  $A'$ .

## 13.8 Exercises

### 13.5. Acceleration at rest

Show that the derivative of  $v \equiv \sqrt{v_x^2 + v_y^2 + v_z^2}$  equals  $a_x$ , independent of how the various  $v_i$ 's are changing, provided that  $v_y = v_z = 0$  at the moment in question.

## 13.6. Linear acceleration \*

A particle's velocity and acceleration both point in the  $x$  direction, with magnitudes  $v$  and  $\dot{v}$ , respectively (as measured in the lab frame). In the spirit of the example in Section 13.5.2, find the 3-acceleration and 4-acceleration in both the lab frame and the instantaneous inertial frame of the particle. Verify that the 3-accelerations are related according to Eq. (13.26).

## **13.7. Linear force \***

For the setup in the previous exercise, find the 3-force and 4-force in both the lab frame and the instantaneous inertial frame of the particle. Verify that the 3-forces are related according to Eq. (13.22).

## **13.8. Circular motion force \***

For the setup in the example in Section 13.5.2, find the 3-force and 4-force in both the lab frame and the instantaneous inertial frame of the particle. Verify that the 3-forces are related according to Eq. (13.22). (Solve this from scratch; don't just use the results from the example.)

![Diagram Fig. 13.9 showing three particles A, B, and C. Particle A is at the origin with a velocity vector v pointing left. Particle B is at an angle of 120 degrees from the horizontal with velocity v. Particle C is at an angle of -120 degrees from the horizontal with velocity v. The angle between the vectors to B and C is 120 degrees.](2b8a523b94d7cd72f5a36177a571b286_img.jpg)

Diagram Fig. 13.9 showing three particles A, B, and C. Particle A is at the origin with a velocity vector v pointing left. Particle B is at an angle of 120 degrees from the horizontal with velocity v. Particle C is at an angle of -120 degrees from the horizontal with velocity v. The angle between the vectors to B and C is 120 degrees.

**Fig. 13.9**

## **13.9. Same speed \***

Consider the setup in Problem 13.2. Given  $v$ , what should  $\theta$  be so that the speed of one particle, as viewed by the other, is also  $v$ ? (The first form of the speed in Eq. (13.38) will make your calculations the simplest.) Do your answers make sense for  $v \approx 0$  and  $v \approx c$ ?

## **13.10. Doppler effect \***

Consider a photon traveling in the  $x$  direction. Ignoring the  $y$  and  $z$  components, and setting  $c = 1$ , the 4-momentum is  $(p, p)$ . In matrix notation, what are the Lorentz transformations for the frames traveling to the left and to the right at speed  $v$ ? What is the new 4-momentum of the photon in these new frames? Accepting the fact that a photon's energy is proportional to its frequency, verify that your results are consistent with the Doppler results in Section 11.8.1.

![Diagram Fig. 13.10 showing particles A, B, and C. Particle A is at the origin. Particles B and C are at an angle theta from the horizontal dashed line. The angle between the vectors to B and C is 2*theta.](5aabb15877b4318c4bd98299fb1cb650_img.jpg)

Diagram Fig. 13.10 showing particles A, B, and C. Particle A is at the origin. Particles B and C are at an angle theta from the horizontal dashed line. The angle between the vectors to B and C is 2\*theta.

**Fig. 13.10**

## **13.11. Three particles \*\***

Three particles head off with equal speeds  $v$ , at  $120^\circ$  with respect to each other, as shown in Fig. 13.9. What is the inner product of any two of the 4-velocities in any frame? Use your result to find the angle  $\theta$  (see Fig. 13.10) at which two particles travel in the frame of the third.

## **13.9 Solutions**

### **13.1. Velocity addition**

Let the desired speed of  $B$  with respect to  $C$  be  $w$  (see Fig. 13.11). In  $A$ 's frame, the 4-velocity of  $B$  is  $(\gamma_u, \gamma_u u)$ , and the 4-velocity of  $C$  is  $(\gamma_v, -\gamma_v v)$ , where we have suppressed the  $y$  and  $z$  components. In  $C$ 's frame, the 4-velocity of  $B$  is  $(\gamma_w, \gamma_w w)$ , and the 4-velocity of  $C$  is  $(1, 0)$ . The invariance of the inner product implies that

![Diagram Fig. 13.11 showing velocity addition. Top: A's frame with C moving left at v and B moving right at u. Bottom: C's frame with C at rest and B moving right at w.](059907d484600459649c2f732cd71337_img.jpg)

Diagram Fig. 13.11 showing velocity addition. Top: A's frame with C moving left at v and B moving right at u. Bottom: C's frame with C at rest and B moving right at w.

**Fig. 13.11**

$$\begin{aligned}
 (\gamma_u, \gamma_u u) \cdot (\gamma_v, -\gamma_v v) &= (\gamma_w, \gamma_w w) \cdot (1, 0) \\
 \implies \gamma_u \gamma_v (1 + uv) &= \gamma_w \\
 \implies \frac{1 + uv}{\sqrt{1 - u^2} \sqrt{1 - v^2}} &= \frac{1}{\sqrt{1 - w^2}}. \tag{13.33}
 \end{aligned}$$

Squaring and then solving for  $w$  gives

$$w = \frac{u + v}{1 + uv}. \quad (13.34)$$

### 13.2. Relative speed

In the lab frame, the 4-velocities of the particles are (suppressing the  $z$  component)

$$(\gamma_v, \gamma_v v \cos \theta, \gamma_v v \sin \theta) \quad \text{and} \quad (\gamma_v, \gamma_v v \cos \theta, -\gamma_v v \sin \theta). \quad (13.35)$$

Let  $w$  be the desired speed of one particle as viewed by the other. Then in the frame of one particle, the 4-velocities are (suppressing two spatial components)

$$(\gamma_w, \gamma_w w) \quad \text{and} \quad (1, 0), \quad (13.36)$$

where we have rotated the axes so that the relative motion is along the  $x$  axis in this frame. Since the 4-vector inner product is invariant under Lorentz transformations and rotations, we have (using  $\cos 2\theta = \cos^2 \theta - \sin^2 \theta$ )

$$\begin{aligned} (\gamma_v, \gamma_v v \cos \theta, \gamma_v v \sin \theta) \cdot (\gamma_v, \gamma_v v \cos \theta, -\gamma_v v \sin \theta) &= (\gamma_w, \gamma_w w) \cdot (1, 0) \\ \implies \gamma_v^2 (1 - v^2 \cos 2\theta) &= \gamma_w. \end{aligned} \quad (13.37)$$

Using the definitions of the  $\gamma$ 's, squaring, and solving for  $w$  gives

$$w = \sqrt{1 - \frac{(1 - v^2)^2}{(1 - v^2 \cos 2\theta)^2}} = \frac{\sqrt{2v^2(1 - \cos 2\theta) - v^4 \sin^2 2\theta}}{1 - v^2 \cos 2\theta}. \quad (13.38)$$

If desired, this can be rewritten (using some double-angle formulas) in the form,

$$w = \frac{2v \sin \theta \sqrt{1 - v^2 \cos^2 \theta}}{1 - v^2 \cos 2\theta}. \quad (13.39)$$

See the solution to Problem 11.14 for some limiting cases.

### 13.3. Another relative speed

In the lab frame, the 4-velocities of the particles are (suppressing the  $z$  component)

$$V_A = (\gamma_u, \gamma_u u, 0) \quad \text{and} \quad V_B = (\gamma_v, \gamma_v v \cos \theta, \gamma_v v \sin \theta). \quad (13.40)$$

Let  $w$  be the desired speed of one particle as viewed by the other. Then in the frame of one particle, the 4-velocities are (suppressing two spatial components)

$$(\gamma_w, \gamma_w w) \quad \text{and} \quad (1, 0), \quad (13.41)$$

where we have rotated the axes so that the relative motion is along the  $x$  axis in this frame. Since the 4-vector inner product is invariant under Lorentz transformations and rotations, we have

$$\begin{aligned} (\gamma_u, \gamma_u u, 0) \cdot (\gamma_v, \gamma_v v \cos \theta, \gamma_v v \sin \theta) &= (\gamma_w, \gamma_w w) \cdot (1, 0) \\ \implies \gamma_u \gamma_v (1 - uv \cos \theta) &= \gamma_w. \end{aligned} \quad (13.42)$$

Using the definitions of the  $\gamma$ 's, squaring, and solving for  $w$  gives

$$w = \sqrt{1 - \frac{(1 - u^2)(1 - v^2)}{(1 - uv \cos \theta)^2}} = \frac{\sqrt{u^2 + v^2 - 2uv \cos \theta - u^2 v^2 \sin^2 \theta}}{1 - uv \cos \theta}. \quad (13.43)$$

See the solution to Problem 11.15 for some limiting cases.

### 13.4. Acceleration for linear motion

- (a) Using  $v(\tau) = \tanh(a\tau)$ , we have  $\gamma = 1/\sqrt{1-v^2} = \cosh(a\tau)$ . Therefore,

$$V = (\gamma, \gamma v) = (\cosh(a\tau), \sinh(a\tau)), \quad (13.44)$$

where we have suppressed the two transverse components. We then have

$$A = \frac{dV}{d\tau} = a(\sinh(a\tau), \cosh(a\tau)). \quad (13.45)$$

- (b) The spaceship is at rest in its instantaneous inertial frame, so

$$V' = (1, 0) \quad \text{and} \quad A' = (0, a). \quad (13.46)$$

Equivalently, these are obtained by setting  $\tau = 0$  in the results from part (a), because the spaceship hasn't started moving at  $\tau = 0$ , as is always the case in the instantaneous rest frame.

- (c) The Lorentz transformation matrix from  $S'$  to  $S$  is

$$\mathcal{M} = \begin{pmatrix} \gamma & \gamma v \\ \gamma v & \gamma \end{pmatrix} = \begin{pmatrix} \cosh(a\tau) & \sinh(a\tau) \\ \sinh(a\tau) & \cosh(a\tau) \end{pmatrix}. \quad (13.47)$$

We must check that

$$\begin{pmatrix} V_0 \\ V_1 \end{pmatrix} = \mathcal{M} \begin{pmatrix} V'_0 \\ V'_1 \end{pmatrix} \quad \text{and} \quad \begin{pmatrix} A_0 \\ A_1 \end{pmatrix} = \mathcal{M} \begin{pmatrix} A'_0 \\ A'_1 \end{pmatrix}. \quad (13.48)$$

These are easily seen to be true.