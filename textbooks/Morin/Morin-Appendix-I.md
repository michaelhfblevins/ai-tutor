# Appendix I Lorentz transformations

![Diagram showing two coordinate systems, S and S', in a 3D perspective. System S has axes x, y, and z. System S' has axes x', y', and z'. The origin of S' is moving to the right along the x-axis of S with a constant velocity v, as indicated by an arrow above the x' axis.](2aac34cbf63e76087296a83ec51857ca_img.jpg)

Diagram showing two coordinate systems, S and S', in a 3D perspective. System S has axes x, y, and z. System S' has axes x', y', and z'. The origin of S' is moving to the right along the x-axis of S with a constant velocity v, as indicated by an arrow above the x' axis.

**Fig. I.1**

In this appendix, we will give an alternate derivation of the Lorentz transformations in Eq. (11.17). The goal here is to derive them from scratch, using only the two postulates of relativity. We will *not* use any of the results derived in Section 11.3. Our strategy will be to use the relativity postulate (“all inertial frames are equivalent”) to figure out as much as we can, and to then invoke the speed-of-light postulate at the end. The main reason for doing things in this order is that it will allow us to derive a very interesting result in Section 11.10.

As in Section 11.4, consider a coordinate system  $S'$  moving relative to another system  $S$  (see Fig. I.1). Let the constant relative speed between the frames be  $v$ . Let the corresponding axes of  $S$  and  $S'$  point in the same direction, and let the origin of  $S'$  move along the  $x$  axis of  $S$ , in the positive direction. As in Section 11.4, we want to find the constants,  $A$ ,  $B$ ,  $C$ , and  $D$ , in the relations,

$$\begin{aligned}\Delta x &= A \Delta x' + B \Delta t', \\ \Delta t &= C \Delta t' + D \Delta x'.\end{aligned}\tag{I.1}$$

The four constants will end up depending on  $v$  (which is constant, given the two inertial frames). Since we have four unknowns, we need four facts. The facts we have at our disposal (using only the two postulates of relativity) are the following.

1. The physical setup:  $S'$  travels with velocity  $v$  with respect to  $S$ .
2. The principle of relativity:  $S$  should see things in  $S'$  in exactly the same way as  $S'$  sees things in  $S$  (except perhaps for a minus sign in some relative positions, but this just depends on our arbitrary choice of directional signs for the axes).
3. The speed-of-light postulate: A light pulse with speed  $c$  in  $S'$  also has speed  $c$  in  $S$ .

The second statement here contains two independent bits of information. (It contains at least two, because we will indeed be able to solve for our four unknowns. And it contains no more than two, because then our four unknowns would be over-constrained.) The two bits that are used depend on personal preference. Three that are commonly used are: (a) the relative speed looks the same from either frame, (b) time dilation (if any) looks the same from either frame, and

(c) length contraction (if any) looks the same from either frame. It is also common to recast the second statement in the form: The Lorentz transformations are the same as their inverse transformations (up to a possible minus sign). We'll choose to work with (a) and (b). Our four independent facts are then:

1.  $S'$  travels with velocity  $v$  with respect to  $S$ .
2.  $S$  travels with velocity  $-v$  with respect to  $S'$ . The minus sign here is due to the convention that we picked the positive  $x$  axes of the two frames to point in the same direction.
3. Time dilation (if any) looks the same from either frame.
4. A light pulse with speed  $c$  in  $S'$  also has speed  $c$  in  $S$ .

Let's see what these imply, in the above order.<sup>1</sup>

- (1) says that a given point in  $S'$  moves with velocity  $v$  with respect to  $S$ . Letting  $x' = 0$  (which is understood to be  $\Delta x' = 0$ , but we'll drop the  $\Delta$ 's from here on) in Eqs. (I.1) and dividing them gives  $x/t = B/C$ . This must equal  $v$ . Therefore,  $B = vC$ , and the transformations become

$$\begin{aligned} x &= Ax' + vCt', \\ t &= Ct' + Dx'. \end{aligned} \quad (\text{I.2})$$

- (2) says that a given point in  $S$  moves with velocity  $-v$  with respect to  $S'$ . Letting  $x = 0$  in the first of Eqs. (I.2) gives  $x'/t' = -vC/A$ . This must equal  $-v$ . Therefore,  $C = A$ , and the transformations become

$$\begin{aligned} x &= Ax' + vAt', \\ t &= At' + Dx'. \end{aligned} \quad (\text{I.3})$$

Note that these are consistent with the Galilean transformations, which have  $A = 1$  and  $D = 0$ .

- (3) can be used in the following way. How fast does a person in  $S$  see a clock in  $S'$  tick? (The clock is assumed to be at rest with respect to  $S'$ .) Let our two events be two successive ticks of the clock. Then  $x' = 0$ , and the second of Eqs. (I.3) gives

$$t = At'. \quad (\text{I.4})$$

In other words, one second on  $S'$ 's clock takes a time of  $A$  seconds in  $S$ 's frame.

Consider the analogous situation from  $S'$ 's point of view. How fast does a person in  $S'$  see a clock in  $S$  tick? (The clock is now assumed to be at rest with respect to  $S$ , in order to create the analogous setup. This is important.) If we invert Eqs. (I.3) to solve

<sup>1</sup> In what follows, we could obtain the final result a little quicker if we invoked the speed-of-light fact prior to the time-dilation one. But we'll do things in the above order so that we can easily carry over the results of this appendix to the discussion in Section 11.10.

for  $x'$  and  $t'$  in terms of  $x$  and  $t$ , we find

$$\begin{aligned} x' &= \frac{x - vt}{A - Dv}, \\ t' &= \frac{At - Dx}{A(A - Dv)}. \end{aligned} \quad (\text{I.5})$$

Two successive ticks of the clock in  $S$  satisfy  $x = 0$ , so the second of Eqs. (I.5) gives

$$t' = \frac{t}{A - Dv}. \quad (\text{I.6})$$

In other words, one second on  $S$ 's clock takes a time of  $1/(A - Dv)$  seconds in  $S'$ 's frame.

Both Eqs. (I.4) and (I.6) apply to the same situation (someone looking at a clock flying by). Therefore, the factors on the right-hand sides must be equal, that is,

$$A = \frac{1}{A - Dv} \implies D = \frac{1}{v} \left( A - \frac{1}{A} \right). \quad (\text{I.7})$$

Our transformations in Eq. (I.3) therefore take the form

$$\begin{aligned} x &= A(x' + vt'), \\ t &= A \left( t' + \frac{1}{v} \left( 1 - \frac{1}{A^2} \right) x' \right). \end{aligned} \quad (\text{I.8})$$

These are consistent with the Galilean transformations, which have  $A = 1$ .

- (4) may now be used to say that if  $x' = ct'$ , then  $x = ct$ . In other words, if  $x' = ct'$ , then

$$c = \frac{x}{t} = \frac{A((ct') + vt')}{A \left( t' + \frac{1}{v} \left( 1 - \frac{1}{A^2} \right) (ct') \right)} = \frac{c + v}{1 + \frac{c}{v} \left( 1 - \frac{1}{A^2} \right)}. \quad (\text{I.9})$$

Solving for  $A$  gives

$$A = \frac{1}{\sqrt{1 - v^2/c^2}}. \quad (\text{I.10})$$

We have chosen the positive square root so that the positive  $x$  and  $x'$  axes point in the same direction. The transformations are now no longer consistent with the Galilean transformations, because  $c$  is not infinite, which means that  $A$  is not 1.

The constant  $A$  is commonly denoted by  $\gamma$ , so we may finally write our Lorentz transformations, Eqs. (I.8), in the form,

$$\begin{aligned} x &= \gamma(x' + vt'), \\ t &= \gamma(t' + vx'/c^2), \end{aligned} \quad (\text{I.11})$$

where

$$\gamma \equiv \frac{1}{\sqrt{1 - v^2/c^2}}, \quad (\text{I.12})$$

in agreement with Eq. (11.17).