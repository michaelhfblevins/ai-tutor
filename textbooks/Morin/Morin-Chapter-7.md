# Chapter 7 Central forces

A *central force* is by definition a force that points radially and whose magnitude depends only on the distance from the source (that is, not on the angle around the source).<sup>1</sup> Equivalently, we may say that a central force is one whose potential depends only on the distance from the source. That is, if the source is located at the origin, then the potential energy is of the form  $V(\mathbf{r}) = V(r)$ . Such a potential does indeed yield a central force, because

$$\mathbf{F}(\mathbf{r}) = -\nabla V(r) = -\frac{dV}{dr}\hat{\mathbf{r}}, \quad (7.1)$$

which points radially and depends only on  $r$ . Gravitational and electrostatic forces are central forces, with  $V(r) \propto 1/r$ . The spring force is also central, with  $V(r) \propto (r - \ell)^2$ , where  $\ell$  is the equilibrium length.

There are two important facts concerning central forces: (1) they are ubiquitous in nature, so we had better learn how to deal with them, and (2) dealing with them is much easier than you might think, because crucial simplifications occur in the equations of motion when  $V$  is a function of  $r$  only. These simplifications will become evident in the following two sections.

### 7.1 Conservation of angular momentum

Angular momentum plays a key role in dealing with central forces because, as we will show, it is constant over time. For a point mass, we define the *angular momentum*  $\mathbf{L}$  by

$$\mathbf{L} = \mathbf{r} \times \mathbf{p}, \quad (7.2)$$

where the “cross product” is defined in Appendix B.  $\mathbf{L}$  depends on  $\mathbf{r}$ , so it therefore depends on where you pick the origin of your coordinate system. Note that  $\mathbf{L}$  is a vector, and that it is orthogonal to both  $\mathbf{r}$  and  $\mathbf{p}$ , by nature of the cross product. You might wonder why we care enough about  $\mathbf{r} \times \mathbf{p}$  to give it a name. Why not look at  $r^3 p^5 \mathbf{r} \times (\mathbf{r} \times \mathbf{p})$ , or something else? The answer is that  $\mathbf{L}$  has some very nice properties, one of which is the following.

<sup>1</sup> Taken literally, the term “central force” would imply only the radial nature of the force. But a physicist’s definition also includes the dependence solely on the distance from the source.

**Theorem 7.1** *If a particle is subject to a central force only, then its angular momentum is conserved.<sup>2</sup> That is,*

$$\text{If } V(\mathbf{r}) = V(r), \text{ then } \frac{d\mathbf{L}}{dt} = 0. \quad (7.3)$$

**Proof:** We have

$$\begin{aligned} \frac{d\mathbf{L}}{dt} &= \frac{d}{dt}(\mathbf{r} \times \mathbf{p}) \\ &= \frac{d\mathbf{r}}{dt} \times \mathbf{p} + \mathbf{r} \times \frac{d\mathbf{p}}{dt} \\ &= \mathbf{v} \times (m\mathbf{v}) + \mathbf{r} \times \mathbf{F} \\ &= 0, \end{aligned} \quad (7.4)$$

because  $\mathbf{F} \propto \mathbf{r}$ , and the cross product of two parallel vectors is zero. ■

We'll prove this theorem again in the next section, using the Lagrangian method. Let's now prove another theorem which is probably obvious, but good to show anyway.

**Theorem 7.2** *If a particle is subject to a central force only, then its motion takes place in a plane.*

**Proof:** At a given instant  $t_0$ , consider the plane  $P$  containing the position vector  $\mathbf{r}_0$  (with the source of the potential taken to be the origin) and the velocity vector  $\mathbf{v}_0$ . We claim that  $\mathbf{r}$  lies in  $P$  at all times.<sup>3</sup> This is true because  $P$  is defined as the plane orthogonal to the vector  $\mathbf{n}_0 \equiv \mathbf{r}_0 \times \mathbf{v}_0$ . But in the proof of Theorem 7.1, we showed that the vector  $\mathbf{r} \times \mathbf{v} \equiv (\mathbf{r} \times \mathbf{p})/m$  does not change with time. Therefore,  $\mathbf{r} \times \mathbf{v} = \mathbf{n}_0$  for all  $t$ . Since  $\mathbf{r}$  is certainly orthogonal to  $\mathbf{r} \times \mathbf{v}$ , we see that  $\mathbf{r}$  is orthogonal to  $\mathbf{n}_0$  for all  $t$ . Hence,  $\mathbf{r}$  must always lie in  $P$ . ■

An intuitive look at this theorem is the following. Since the position, velocity, and acceleration (which is proportional to  $\mathbf{F}$ , which in turn is proportional to the position vector  $\mathbf{r}$ ) vectors initially all lie in  $P$ , there is a symmetry between the two sides of  $P$ . Therefore, there is no reason for the particle to head out of  $P$  on one side rather than the other. The particle therefore remains in  $P$ . We can then use this same reasoning again a short time later, and so on.

This theorem shows that we need only two coordinates, instead of the usual three, to describe the motion. But since we're on a roll, why stop there? We'll show below that we really need only *one* coordinate. Not bad, three coordinates reduced down to one.

<sup>2</sup> This is a special case of the fact that torque equals the rate of change of angular momentum. We'll talk about this in great detail in Chapter 8.

<sup>3</sup> The plane  $P$  is not well defined if  $\mathbf{v}_0 = \mathbf{0}$ , or if  $\mathbf{r}_0 = \mathbf{0}$ , or if  $\mathbf{v}_0$  is parallel to  $\mathbf{r}_0$ . But in these cases, you can quickly show that the motion is always radial, which is even more restrictive than planar.

### 7.2 The effective potential

The *effective potential* provides a sneaky and useful method for simplifying a three-dimensional central-force problem down to a one-dimensional problem. Here's how it works. Consider a particle of mass  $m$  subject to a central force only, described by the potential  $V(r)$ . Let  $r$  and  $\theta$  be the polar coordinates in the plane of the motion. In these polar coordinates, the Lagrangian (which we'll label as " $\mathcal{L}$ ", to save " $L$ " for the angular momentum) is

$$\mathcal{L} = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2) - V(r). \quad (7.5)$$

The equations of motion obtained from varying  $r$  and  $\theta$  are

$$\begin{aligned} m\ddot{r} &= mr\dot{\theta}^2 - V'(r), \\ \frac{d}{dt}(mr^2\dot{\theta}) &= 0. \end{aligned} \quad (7.6)$$

Since  $-V'(r)$  equals the force  $F(r)$ , the first of these equations is the radial  $F = ma$  equation, complete with the centripetal acceleration, in agreement with the first of Eqs. (3.51). The second equation is the statement of conservation of angular momentum, because  $mr^2\dot{\theta} = r(mr\dot{\theta}) = rp_\theta$  (where  $p_\theta$  is the momentum in the angular direction) is the magnitude of  $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ , from Eq. (B.9). We therefore see that the magnitude of  $\mathbf{L}$  is constant. And since the direction of  $\mathbf{L}$  is always perpendicular to the fixed plane of the motion, the vector  $\mathbf{L}$  is constant in time. We have therefore just given a second proof of Theorem 7.1. In the present Lagrangian language, the conservation of  $\mathbf{L}$  follows from the fact that  $\theta$  is a cyclic coordinate, as we saw in Example 2 in Section 6.5.1. Since  $mr^2\dot{\theta}$  does not change with time, let us denote its constant value by

$$L \equiv mr^2\dot{\theta}. \quad (7.7)$$

$L$  is determined by the initial conditions. It can be specified, for example, by giving the initial values of  $r$  and  $\dot{\theta}$ . Using  $\dot{\theta} = L/(mr^2)$ , we can eliminate  $\dot{\theta}$  from the first of Eqs. (7.6). The result is

$$m\ddot{r} = \frac{L^2}{mr^3} - V'(r). \quad (7.8)$$

Multiplying by  $\dot{r}$  and integrating with respect to time yields

$$\frac{1}{2}m\dot{r}^2 + \left( \frac{L^2}{2mr^2} + V(r) \right) = E, \quad (7.9)$$

where  $E$  is a constant of integration.  $E$  is simply the energy, which can be seen by noting that this equation could also have been obtained by using Eq. (7.7) to eliminate  $\dot{\theta}$  in the energy equation,  $(m/2)(\dot{r}^2 + r^2\dot{\theta}^2) + V(r) = E$ .

Equation (7.9) is rather interesting. It involves only the variable  $r$ . And it looks a lot like the equation for a particle moving in one dimension (labeled by the coordinate  $r$ ) under the influence of the potential,

$$V_{\text{eff}}(r) \equiv \frac{L^2}{2mr^2} + V(r). \quad (7.10)$$

The subscript “eff” here stands for “effective.”  $V_{\text{eff}}(r)$  is called the *effective potential*. The “effective force” is easily read off from Eq. (7.8) to be

$$F_{\text{eff}}(r) = \frac{L^2}{mr^3} - V'(r), \quad (7.11)$$

which agrees with  $F_{\text{eff}} = -V'_{\text{eff}}(r)$ , as it should. This “effective” potential concept is a marvelous result and should be duly appreciated. It says that if we want to solve a two-dimensional problem (which could have come from a three-dimensional problem) involving a central force, then we can recast the problem into a simple one-dimensional problem with a slightly modified potential. We can forget that we ever had the variable  $\theta$ , and we can solve this one-dimensional problem (as we’ll demonstrate below) to obtain  $r(t)$ . Having found  $r(t)$ , we can use  $\dot{\theta}(t) = L/mr^2$  to solve for  $\theta(t)$  (in theory, at least). This whole procedure works only because there is a quantity involving  $r$  and  $\theta$  (or rather,  $\dot{\theta}$ ) that is independent of time. The variables  $r$  and  $\theta$  are therefore *not* independent, so the problem is really one-dimensional instead of two-dimensional.

To get a general idea of how  $r$  behaves with time, all we have to do is draw the graph of  $V_{\text{eff}}(r)$ . Consider the example where  $V(r) = Ar^2$ . This is the potential for a spring with relaxed length zero. Then

$$V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + Ar^2. \quad (7.12)$$

![Graph of the effective potential V_eff(r) versus r for a spring potential V(r) = Ar^2. The curve is a hyperbola-like shape that goes to infinity as r approaches zero and increases as r increases. A horizontal dashed line represents the total energy E. The curve intersects this line at two points, r_1 and r_2, which are the turning points of the motion. The minimum of the curve is at r = 0.](b5e419bd9fcfdefda6c40993ce32a0ee_img.jpg)

The figure shows a graph of the effective potential  $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + Ar^2$  as a function of  $r$ . The vertical axis is labeled  $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + Ar^2$  and the horizontal axis is labeled  $r$ . The curve is U-shaped, approaching infinity as  $r \rightarrow 0$  and increasing as  $r$  increases. A horizontal dashed line labeled  $E$  represents the total energy. The curve intersects this line at two points,  $r_1$  and  $r_2$ , which are marked on the  $r$ -axis. The region between  $r_1$  and  $r_2$  is where the particle's motion is allowed, as  $E \geq V_{\text{eff}}(r)$ .

Graph of the effective potential V\_eff(r) versus r for a spring potential V(r) = Ar^2. The curve is a hyperbola-like shape that goes to infinity as r approaches zero and increases as r increases. A horizontal dashed line represents the total energy E. The curve intersects this line at two points, r\_1 and r\_2, which are the turning points of the motion. The minimum of the curve is at r = 0.

**Fig. 7.1**

To plot  $V_{\text{eff}}(r)$ , we must be given  $L$  (determined by the initial conditions), along with  $A$  and  $m$  (determined by the system we’re dealing with). But the general shape looks like the curve in Fig. 7.1. The energy  $E$  (determined by the initial conditions), which must be given too, is also drawn. The coordinate  $r$  bounces back and forth between the turning points,  $r_1$  and  $r_2$ , which satisfy  $V_{\text{eff}}(r_{1,2}) = E$ .<sup>4</sup> This is true because it is impossible for the particle to be located at an  $r$  for which  $E < V_{\text{eff}}$ , since Eq. (7.9) would then imply an imaginary value for  $\dot{r}$ . If  $E$  equals the minimum of  $V_{\text{eff}}(r)$ , then  $r_1 = r_2$ , so  $r$  is stuck at this one value, which means that the motion is a circle.

**REMARK:** The  $L^2/2mr^2$  term in the effective potential is sometimes called the *angular momentum barrier*. It has the effect of keeping the particle from getting too close to the origin. Basically, the point is that  $L \equiv mr^2\dot{\theta}$  is constant, so as  $r$  gets smaller,  $\dot{\theta}$  gets bigger. But  $\dot{\theta}$  increases at a

<sup>4</sup> It turns out that for our  $Ar^2$  spring potential, the motion in space is an ellipse, with semi-axis lengths  $r_1$  and  $r_2$  (see Problem 7.5). But for a general potential, the motion isn’t so nice.

greater rate than  $r$  decreases, due to the square of the  $r$  in  $L = mr^2\dot{\theta}$ . So eventually we end up with a tangential kinetic energy,  $mr^2\dot{\theta}^2/2$ , that is greater than what is allowed by conservation of energy.<sup>5</sup>

As he walked past the beautiful belle,  
 The attraction was easy to tell.  
 But despite his persistence,  
 He was kept at a distance  
 By that darn conservation of  $L$ ! ♣

Note that it is by no means necessary to introduce the concept of the effective potential. You can simply solve the equations of motion in Eq. (7.6) as they are. But introducing  $V_{\text{eff}}$  makes it much easier to see what's going on in a central-force problem.

When using potentials, effective,  
 Remember the one main objective:  
 The goal is to shun  
 All dimensions but one,  
 And then view things with 1-D perspective.

### 7.3 Solving the equations of motion

If we want to be quantitative, we must solve the equations of motion in Eq. (7.6). Equivalently, we must solve their integrated forms, Eqs. (7.7) and (7.9), which are the conservation of  $L$  and  $E$  statements,

$$\begin{aligned} mr^2\dot{\theta} &= L, \\ \frac{1}{2}mr^2\dot{r}^2 + \frac{L^2}{2mr^2} + V(r) &= E. \end{aligned} \quad (7.13)$$

The word “solve” is a little ambiguous here, because we should specify what quantities we want to solve for in terms of what other quantities. There are essentially two things we can do. We can solve for  $r$  and  $\theta$  in terms of  $t$ . Or we can solve for  $r$  in terms of  $\theta$ . The former has the advantage of immediately yielding velocities and, of course, the information of where the particle is at time  $t$ . The latter has the advantage of explicitly showing what the trajectory looks like in space, even though we don't know how quickly it is being traversed. We'll deal mainly with this latter case, particularly when we discuss the gravitational force and Kepler's laws below. But let's look at both cases now.

<sup>5</sup> This argument doesn't hold if  $V(r)$  goes to  $-\infty$  faster than  $-1/r^2$ . You can see this by drawing the graph of  $V_{\text{eff}}(r)$ , which heads to  $-\infty$  instead of  $+\infty$  as  $r \rightarrow 0$ .  $V(r)$  decreases fast enough to allow for the increase in kinetic energy. But such potentials don't come up that often.

#### 7.3.1 Finding $r(t)$ and $\theta(t)$

The value of  $\dot{r}$  at any point is found from Eq. (7.13) to be

$$\frac{dr}{dt} = \pm \sqrt{\frac{2}{m}} \sqrt{E - \frac{L^2}{2mr^2} - V(r)}. \quad (7.14)$$

To get an actual  $r(t)$  out of this, we must be supplied with  $E$  and  $L$  (determined by the initial values of  $r$ ,  $\dot{r}$ , and  $\dot{\theta}$ ), and also the function  $V(r)$ . To solve this differential equation, we “simply” have to separate variables and then (in theory) integrate:

$$\int \frac{dr}{\sqrt{E - \frac{L^2}{2mr^2} - V(r)}} = \pm \int \sqrt{\frac{2}{m}} dt = \pm \sqrt{\frac{2}{m}} (t - t_0). \quad (7.15)$$

We need to evaluate this (rather unpleasant) integral on the left-hand side, to obtain  $t$  as a function of  $r$ . Having found  $t(r)$ , we can then (in theory) invert the result to obtain  $r(t)$ . Finally, substituting this  $r(t)$  into the relation  $\dot{\theta} = L/mr^2$  from Eq. (7.13) gives  $\dot{\theta}$  as a function of  $t$ , which we can (in theory) integrate to obtain  $\theta(t)$ .

As you might have guessed, this procedure has the potential to yield some stress. For most  $V(r)$ ’s, the integral in Eq. (7.15) is not calculable in closed form. There are only a few “nice” potentials  $V(r)$  for which we can evaluate it. And even in those cases, the remaining tasks are still a pain.<sup>6</sup> But the good news is that these “nice” potentials are precisely the ones we are most interested in. In particular, the gravitational potential, which goes like  $1/r$  and which we will concentrate on during the remainder of this chapter, leads to a calculable integral (the spring potential  $\sim r^2$  does also). However, having said all this, we’re not going to apply this procedure to gravity. It’s nice to know that it exists, but we won’t be doing anything else with it. Instead, we’ll use the following strategy to solve for  $r$  as a function of  $\theta$ .

#### 7.3.2 Finding $r(\theta)$

We can eliminate the  $dt$  from Eqs. (7.13) by getting the  $\dot{r}^2$  term alone on the left side of the second equation, and then dividing by the square of the first equation. The  $dt^2$  factors cancel, and we obtain

$$\left( \frac{1}{r^2} \frac{dr}{d\theta} \right)^2 = \frac{2mE}{L^2} - \frac{1}{r^2} - \frac{2mV(r)}{L^2}. \quad (7.16)$$

We can now (in theory) take a square root, separate variables, and integrate to obtain  $\theta$  as a function of  $r$ . We can then (in theory) invert to obtain  $r$  as a function

<sup>6</sup> Of course, if you run out of patience or hit a brick wall, you always have the option of doing things numerically. See Section 1.4 for a discussion of this.

of  $\theta$ . To do this, we must be given the function  $V(r)$ . So let's now finally give ourselves a  $V(r)$  and do a problem all the way through. We'll study the most important potential of all, or perhaps the second most important one, gravity.<sup>7</sup>

### 7.4 Gravity, Kepler's laws

#### 7.4.1 Calculation of $r(\theta)$

Our goal in this subsection is to obtain  $r$  as a function of  $\theta$ , for a gravitational potential. Let's assume that we're dealing with the earth and the sun, with masses  $M_\odot$  and  $m$ , respectively. The gravitational potential energy of the earth-sun system is

$$V(r) = -\frac{\alpha}{r}, \quad \text{where } \alpha \equiv GM_\odot m. \quad (7.17)$$

In the present treatment, we'll consider the sun to be bolted down at the origin of our coordinate system. Since  $M_\odot \gg m$ , this is approximately true for the earth-sun system. (If we want to do the problem exactly, we must use the *reduced mass*, which is the topic of Section 7.4.5.) Equation (7.16) becomes

$$\left(\frac{1}{r^2} \frac{dr}{d\theta}\right)^2 = \frac{2mE}{L^2} - \frac{1}{r^2} + \frac{2m\alpha}{rL^2}. \quad (7.18)$$

As stated above, we could take a square root, separate variables, integrate to find  $\theta(r)$ , and then invert to find  $r(\theta)$ . This method, although straightforward, is rather messy. So let's solve for  $r(\theta)$  in a slick way.

With all the  $1/r$  terms floating around, it might be easier to solve for  $1/r$  instead of  $r$ . Using  $d(1/r)/d\theta = -(dr/d\theta)/r^2$ , and letting  $y \equiv 1/r$  for convenience, Eq. (7.18) becomes

$$\left(\frac{dy}{d\theta}\right)^2 = -y^2 + \frac{2m\alpha}{L^2}y + \frac{2mE}{L^2}. \quad (7.19)$$

At this point, we could also use the separation-of-variables technique, but let's continue to be slick. Completing the square on the right-hand side gives

$$\left(\frac{dy}{d\theta}\right)^2 = -\left(y - \frac{m\alpha}{L^2}\right)^2 + \frac{2mE}{L^2} + \left(\frac{m\alpha}{L^2}\right)^2. \quad (7.20)$$

Defining  $z \equiv y - m\alpha/L^2$  for convenience yields

$$\left(\frac{dz}{d\theta}\right)^2 = -z^2 + \left(\frac{m\alpha}{L^2}\right)^2 \left(1 + \frac{2EL^2}{m\alpha^2}\right) \equiv -z^2 + B^2, \quad (7.21)$$

<sup>7</sup> The two most important potentials in physics are certainly the gravitational and harmonic-oscillator ones. They both lead to doable integrals, and interestingly both lead to elliptical orbits.

where

$$B \equiv \left( \frac{m\alpha}{L^2} \right) \sqrt{1 + \frac{2EL^2}{m\alpha^2}}. \quad (7.22)$$

At this point, in the spirit of being slick, we can just look at Eq. (7.21) and observe that

$$z = B \cos(\theta - \theta_0) \quad (7.23)$$

is the solution, because  $\cos^2 x + \sin^2 x = 1$ . But lest we feel guilty about not doing separation-of-variables at least once in this problem, let's solve Eq. (7.21) that way, too. The integral is nice and doable, and we have

$$\int \frac{dz}{\sqrt{B^2 - z^2}} = \int d\theta \implies \cos^{-1}\left(\frac{z}{B}\right) = \theta - \theta_0, \quad (7.24)$$

which gives  $z = B \cos(\theta - \theta_0)$ . It is customary to pick the axes so that  $\theta_0 = 0$ , so we'll drop the  $\theta_0$  from here on. Recalling our definition  $z \equiv 1/r - m\alpha/L^2$  and also the definition of  $B$  from Eq. (7.22), Eq. (7.23) becomes

$$\frac{1}{r} = \frac{m\alpha}{L^2} (1 + \epsilon \cos \theta), \quad (7.25)$$

where

$$\epsilon \equiv \sqrt{1 + \frac{2EL^2}{m\alpha^2}} \quad (7.26)$$

is the *eccentricity* of the particle's motion. We will see shortly exactly what  $\epsilon$  signifies.

This completes the derivation of  $r(\theta)$  for the gravitational potential,  $V(r) \propto 1/r$ . It was a little messy, but not unbearably painful. At any rate, we just discovered the basic motion of objects under the influence of gravity, which takes care of virtually all of the gazillion tons of stuff in the universe. Not bad for one page of work.

Newton said as he gazed off afar,  
 "From here to the most distant star,  
 These wond'rous ellipses  
 And solar eclipses  
 All come from a 1 over  $r$ ."

What are the limits on  $r$  in Eq. (7.25)? The minimum value of  $r$  is obtained when the right-hand side reaches its maximum value, which is  $(m\alpha/L^2)(1 + \epsilon)$ . Therefore,

$$r_{\min} = \frac{L^2}{m\alpha(1 + \epsilon)}. \quad (7.27)$$

What is the maximum value of  $r$ ? The answer depends on whether  $\epsilon$  is greater than or less than 1. If  $\epsilon < 1$  (which corresponds to circular or elliptical orbits, as we'll see below), then the minimum value of the right-hand side of Eq. (7.25) is  $(m\alpha/L^2)(1 - \epsilon)$ . Therefore,

$$r_{\max} = \frac{L^2}{m\alpha(1 - \epsilon)} \quad (\text{if } \epsilon < 1). \quad (7.28)$$

If  $\epsilon \geq 1$  (which corresponds to parabolic or hyperbolic orbits, as we'll see below), then the right-hand side of Eq. (7.25) can become zero (when  $\cos \theta = -1/\epsilon$ ). Therefore,

$$r_{\max} = \infty \quad (\text{if } \epsilon \geq 1). \quad (7.29)$$

#### 7.4.2 The orbits

Let's examine in detail the various cases for  $\epsilon$ .

##### • **Circle** ( $\epsilon = 0$ )

If  $\epsilon = 0$ , then Eq. (7.26) says that  $E = -m\alpha^2/2L^2$ . The negative  $E$  means that the potential energy is more negative than the kinetic energy is positive, so the particle is trapped in the potential well. Equations (7.27) and (7.28) give  $r_{\min} = r_{\max} = L^2/m\alpha$ . Therefore, the particle moves in a circular orbit with radius  $L^2/m\alpha$ . Equivalently, Eq. (7.25) says that  $r$  is independent of  $\theta$ .

Note that it isn't necessary to do all the work of Section 7.4.1 if we just want to look at circular motion. For a given  $L$ , the energy  $-m\alpha^2/2L^2$  is the minimum value that the  $E$  given by Eq. (7.13) can take. This is true because to achieve the minimum, we certainly want  $\dot{r} = 0$ . And you can show that minimizing the effective potential,  $L^2/2mr^2 - \alpha/r$ , yields this value for  $E$ . If we plot  $V_{\text{eff}}(r)$ , we have the situation shown in Fig. 7.2. The particle is trapped at the bottom of the potential well, so it has no motion in the  $r$  direction.

![Figure 7.2: A graph of the effective potential V_eff(r) versus r for a circular orbit. The potential curve has a minimum at r_min = r_max. A horizontal dashed line represents the energy E, which is at the minimum of the potential well. The equation V_eff(r) = L^2 / (2mr^2) - alpha / r is shown at the top.](429ee313df70c280505776eb7c7e279a_img.jpg)

Figure 7.2: A graph of the effective potential V\_eff(r) versus r for a circular orbit. The potential curve has a minimum at r\_min = r\_max. A horizontal dashed line represents the energy E, which is at the minimum of the potential well. The equation V\_eff(r) = L^2 / (2mr^2) - alpha / r is shown at the top.

Fig. 7.2

##### • **Ellipse** ( $0 < \epsilon < 1$ )

If  $0 < \epsilon < 1$ , then Eq. (7.26) says that  $-m\alpha^2/2L^2 < E < 0$ . Equations (7.27) and (7.28) give  $r_{\min}$  and  $r_{\max}$ . It isn't obvious that the resulting motion is an ellipse. We'll demonstrate this below.

If we plot  $V_{\text{eff}}(r)$ , we have the situation shown in Fig. 7.3. The particle oscillates between  $r_{\min}$  and  $r_{\max}$ . The energy is negative, so the particle is trapped in the potential well.

![Figure 7.3: A graph of the effective potential V_eff(r) versus r for an elliptical orbit. The potential curve has a minimum. A horizontal dashed line represents the energy E, which is above the minimum of the potential well. The curve intersects the energy line at two points, r_min and r_max, indicating the range of radial motion.](5a4160e24d7daaea831c8f55b9ef087b_img.jpg)

Figure 7.3: A graph of the effective potential V\_eff(r) versus r for an elliptical orbit. The potential curve has a minimum. A horizontal dashed line represents the energy E, which is above the minimum of the potential well. The curve intersects the energy line at two points, r\_min and r\_max, indicating the range of radial motion.

Fig. 7.3

##### • **Parabola** ( $\epsilon = 1$ )

If  $\epsilon = 1$ , then Eq. (7.26) says that  $E = 0$ . This value of  $E$  implies that the particle barely makes it out to infinity (its speed approaches zero as  $r \rightarrow \infty$ ). Equation (7.27) gives  $r_{\min} = L^2/2m\alpha$ , and Eq. (7.29) gives  $r_{\max} = \infty$ . Again, it isn't obvious that the resulting motion is a parabola. We'll demonstrate this below.

![Figure 7.4: A graph of the effective potential V_eff(r) versus r. The curve starts at a high value for small r, decreases to a minimum, and then increases, approaching a horizontal asymptote. A horizontal line representing energy E intersects the curve at a point labeled r_min. An arrow points from the curve to the label r_min.](3e208492ed4b2c819416a39adca02d08_img.jpg)

Figure 7.4: A graph of the effective potential V\_eff(r) versus r. The curve starts at a high value for small r, decreases to a minimum, and then increases, approaching a horizontal asymptote. A horizontal line representing energy E intersects the curve at a point labeled r\_min. An arrow points from the curve to the label r\_min.

Fig. 7.4

![Figure 7.5: A graph of the effective potential V_eff(r) versus r. The curve is similar to Figure 7.4, but the energy E is represented by a dashed horizontal line that is above the minimum of the potential curve. The curve intersects the dashed line at a point labeled r_min. An arrow points from the curve to the label r_min.](7b86cf72a301567fd07e09d32d2472a0_img.jpg)

Figure 7.5: A graph of the effective potential V\_eff(r) versus r. The curve is similar to Figure 7.4, but the energy E is represented by a dashed horizontal line that is above the minimum of the potential curve. The curve intersects the dashed line at a point labeled r\_min. An arrow points from the curve to the label r\_min.

Fig. 7.5

If we plot  $V_{\text{eff}}(r)$ , we have the situation shown in Fig. 7.4. The particle does not oscillate back and forth in the  $r$  direction. It moves inward (or possibly not, if it was initially moving outward), turns around at  $r_{\min} = L^2/2m\alpha$ , and then heads out to infinity forever.

##### • **Hyperbola** ( $\epsilon > 1$ )

If  $\epsilon > 1$ , then Eq. (7.26) says that  $E > 0$ . This value of  $E$  implies that the particle makes it out to infinity with energy to spare. The potential goes to zero as  $r \rightarrow \infty$ , so the particle's speed approaches the nonzero value  $\sqrt{2E/m}$  as  $r \rightarrow \infty$ . Equation (7.27) gives  $r_{\min}$ , and Eq. (7.29) gives  $r_{\max} = \infty$ . Again, it isn't obvious that the resulting motion is a hyperbola. We'll demonstrate this below.

If we plot  $V_{\text{eff}}(r)$ , we have the situation shown in Fig. 7.5. As in the parabola case, the particle does not oscillate back and forth in the  $r$  direction. It moves inward (or possibly not, if it was initially moving outward), turns around at  $r_{\min}$ , and then heads out to infinity forever.

#### 7.4.3 Proof of conic orbits

Let's now prove that Eq. (7.25) does indeed describe the conic sections stated above. We'll also show that the origin (the source of the potential) is a focus of the conic section. These proofs are straightforward, although the ellipse and hyperbola cases get a bit messy. In what follows, we'll find it easier to work with Cartesian coordinates. For convenience, let

$$k \equiv \frac{L^2}{m\alpha}. \quad (7.30)$$

Multiplying Eq. (7.25) through by  $kr$ , and using  $\cos \theta = x/r$ , gives

$$k = r + \epsilon x. \quad (7.31)$$

Solving for  $r$  and squaring yields

$$x^2 + y^2 = k^2 - 2k\epsilon x + \epsilon^2 x^2. \quad (7.32)$$

Let's look at the various cases for  $\epsilon$ . We will invoke without proof various facts about conic sections (focal lengths, etc.).

##### • **Circle** ( $\epsilon = 0$ )

In this case, Eq. (7.32) becomes  $x^2 + y^2 = k^2$ . So we have a circle with radius  $k = L^2/m\alpha$ , with its center at the origin (see Fig. 7.6).

##### • **Ellipse** ( $0 < \epsilon < 1$ )

In this case, Eq. (7.32) can be written (after completing the square for the  $x$  terms, and expending some effort) as

$$\frac{\left(x + \frac{k\epsilon}{1-\epsilon^2}\right)^2}{a^2} + \frac{y^2}{b^2} = 1, \quad \text{where } a = \frac{k}{1-\epsilon^2}, \quad \text{and } b = \frac{k}{\sqrt{1-\epsilon^2}}. \quad (7.33)$$

![Figure 7.6: A diagram of a circle centered at the origin of a Cartesian coordinate system with x and y axes. The radius of the circle is labeled k.](50741be132acb9303d371b409bd8329b_img.jpg)

Figure 7.6: A diagram of a circle centered at the origin of a Cartesian coordinate system with x and y axes. The radius of the circle is labeled k.

Fig. 7.6

This is the equation for an ellipse with its center located at  $(-k\epsilon/(1 - \epsilon^2), 0)$ . The semi-major and semi-minor axes are  $a$  and  $b$ , respectively. And the focal length is  $c = \sqrt{a^2 - b^2} = k\epsilon/(1 - \epsilon^2)$ . Therefore, one focus is located at the origin (see Fig. 7.7). Note that  $c/a$  equals the eccentricity,  $\epsilon$ .

##### • **Parabola** ( $\epsilon = 1$ )

In this case, Eq. (7.32) becomes  $y^2 = k^2 - 2kx$ , which can be written as  $y^2 = -2k(x - \frac{k}{2})$ . This is the equation for a parabola with vertex at  $(k/2, 0)$  and focal length  $k/2$ . (The focal length of a parabola written in the form  $y^2 = 4ax$  is  $a$ .) So we have a parabola with its focus located at the origin (see Fig. 7.8).

##### • **Hyperbola** ( $\epsilon > 1$ )

In this case, Eq. (7.32) can be written (after completing the square for the  $x$  terms)

$$\frac{\left(x - \frac{k\epsilon}{\epsilon^2 - 1}\right)^2}{a^2} - \frac{y^2}{b^2} = 1, \quad \text{where } a = \frac{k}{\epsilon^2 - 1}, \quad \text{and } b = \frac{k}{\sqrt{\epsilon^2 - 1}}. \quad (7.34)$$

This is the equation for a hyperbola with its center (defined to be the intersection of the asymptotes) located at  $(k\epsilon/(\epsilon^2 - 1), 0)$ . The focal length is  $c = \sqrt{a^2 + b^2} = k\epsilon/(\epsilon^2 - 1)$ . Therefore, the focus is located at the origin (see Fig. 7.9). Note that  $c/a$  equals the eccentricity,  $\epsilon$ .

The *impact parameter* (usually denoted by the letter  $b$ ) of a trajectory is defined to be the closest distance to the origin the particle would achieve if it moved in the straight line determined by its initial velocity far from the origin (that is, along the dotted line in the Fig. 7.9). You might think that choosing the letter  $b$  here would cause a problem, because we already defined  $b$  in Eq. (7.34). However, it turns out that these two definitions are identical (see Exercise 7.14), so all is well.

Equation (7.34) actually describes an entire hyperbola, that is, it also describes a branch that opens up to the right with its focus located at  $(2k\epsilon/(\epsilon^2 - 1), 0)$ . However, this right branch was introduced in the squaring operation that produced Eq. (7.32). It isn't a solution to the original equation we wanted to solve, Eq. (7.31). It turns out that the right-opening branch (or its reflection across the  $y$  axis, depending on your sign convention for  $B$  and  $\epsilon$ ) is relevant for a repulsive, instead of attractive,  $1/r$  potential; see Exercise 7.21.

#### 7.4.4 Kepler's laws

We can now, with minimal extra work, write down Kepler's laws. Kepler (1571–1630) lived before Newton (1642–1727), so he didn't have Newton's laws at his disposal. Kepler arrived at his laws via observational data, which was a rather impressive feat. It was known since the time of Copernicus (1473–1543) that the planets move around the sun, but it was Kepler who first gave a quantitative description of the orbits. Kepler's laws assume that the sun is massive enough so that its position is essentially fixed in space. This is a very good approximation,

![Figure 7.7: A diagram of an ellipse centered on the x-axis. The semi-major axis is labeled 'a', the semi-minor axis is labeled 'b', and the distance from the center to a focus is labeled 'c'. One focus is located at the origin (0,0). The ellipse is centered at (-c, 0).](c2c1a4a378869a1b068ae4822d54692f_img.jpg)

Figure 7.7: A diagram of an ellipse centered on the x-axis. The semi-major axis is labeled 'a', the semi-minor axis is labeled 'b', and the distance from the center to a focus is labeled 'c'. One focus is located at the origin (0,0). The ellipse is centered at (-c, 0).

Fig. 7.7

![Figure 7.8: A diagram of a parabola opening to the left. The vertex is at (k/2, 0) on the x-axis. The focus is at the origin (0,0). The focal length is labeled as k/2.](ea580102d991b44855a52cf3f1d047fc_img.jpg)

Figure 7.8: A diagram of a parabola opening to the left. The vertex is at (k/2, 0) on the x-axis. The focus is at the origin (0,0). The focal length is labeled as k/2.

Fig. 7.8

![Figure 7.9: A diagram of a hyperbola opening to the left. The center is on the x-axis. The semi-major axis is labeled 'a', the semi-minor axis is labeled 'b', and the distance from the center to a focus is labeled 'c'. One focus is at the origin (0,0). Dashed lines represent the asymptotes. A dotted line represents the trajectory of a particle, with the impact parameter 'b' shown as the distance from the origin to the dotted line.](7379e3a2a855383e7814f5bd449ff2ea_img.jpg)

Figure 7.9: A diagram of a hyperbola opening to the left. The center is on the x-axis. The semi-major axis is labeled 'a', the semi-minor axis is labeled 'b', and the distance from the center to a focus is labeled 'c'. One focus is at the origin (0,0). Dashed lines represent the asymptotes. A dotted line represents the trajectory of a particle, with the impact parameter 'b' shown as the distance from the origin to the dotted line.

Fig. 7.9

but the following subsection on the *reduced mass* shows how to modify the laws and solve things exactly.

![Diagram illustrating the geometry of a small sector of an orbit. A radius vector of length r sweeps out an angle dθ, forming a thin triangle. The area of this triangle is labeled as r dθ. The arc of the orbit is shown as a dashed line.](563ec888418f26533b534dce245ba828_img.jpg)

Diagram illustrating the geometry of a small sector of an orbit. A radius vector of length r sweeps out an angle dθ, forming a thin triangle. The area of this triangle is labeled as r dθ. The arc of the orbit is shown as a dashed line.

**Fig. 7.10**

- **First law:** *The planets move in elliptical orbits with the sun at one focus.*

We proved this in Eq. (7.33).<sup>8</sup> There are undoubtedly also objects flying past the sun in hyperbolic orbits, but we don't call these things planets, because we never see the same one twice.

- **Second law:** *The radius vector to a planet sweeps out area at a rate that is independent of its position in the orbit.*

This law is nothing other than a fancy way of stating conservation of angular momentum. The area swept out by the radius vector during a short period of time is  $dA = r(r d\theta)/2$ , because  $r d\theta$  is the base of the thin triangle in Fig. 7.10. Therefore, we have (using  $L = mr^2\dot{\theta}$ )

$$\frac{dA}{dt} = \frac{r^2\dot{\theta}}{2} = \frac{L}{2m}, \quad (7.35)$$

which is constant, because  $L$  is constant for a central force. This quick proof is independent of all the work we did in Sections 7.4.1–7.4.3.

- **Third law:** *The square of the period of an orbit,  $T$ , is proportional to the cube of the semi-major-axis length,  $a$ . More precisely,*

$$T^2 = \frac{4\pi^2 a^3}{GM_\odot}, \quad (7.36)$$

where  $M_\odot$  is the mass of the sun. Note that the planet's mass  $m$  doesn't appear in this equation.

**Proof:** Integrating Eq. (7.35) over the time of a whole orbit gives

$$A = \frac{LT}{2m}. \quad (7.37)$$

But the area of an ellipse is  $A = \pi ab$ , where  $a$  and  $b$  are the semi-major and semi-minor axes, respectively. Squaring Eq. (7.37) and using Eq. (7.33) to write  $b = a\sqrt{1 - \epsilon^2}$  gives

$$\pi^2 a^4 = \left( \frac{L^2}{m(1 - \epsilon^2)} \right) \frac{T^2}{4m}. \quad (7.38)$$

We have grouped the right-hand side in this way because we can now use the  $L^2 \equiv m\alpha k$  relation from Eq. (7.30) to transform the term in parentheses into  $\alpha k/(1 - \epsilon^2) \equiv \alpha a$ , where  $a$  is given in Eq. (7.33). But  $\alpha a \equiv (GM_\odot m)a$ , so we obtain

$$\pi^2 a^4 = \frac{(GM_\odot m a) T^2}{4m}, \quad (7.39)$$

which gives Eq. (7.36), as desired. ■

<sup>8</sup> For an alternate geometrical proof due to Feynman (and also Maxwell), see Goodstein and Goodstein (1996).

These three laws describe the motion of all the planets (and asteroids, comets, and such) in the solar system. But our solar system is only the tip of the iceberg. There's a lot of other stuff out there, and it's all governed by gravity (although Newton's inverse square law must be supplanted by Einstein's General Relativity theory of gravitation). There's a whole universe around us, and as time passes on we see and understand more and more of it, both experimentally and theoretically. In recent years, we've even begun to look for friends we might have out there. Why? Because we can. There's nothing wrong with looking under the lamppost now and then. It just happens to be a very big one in this case.

As we grow up, we open an ear,  
 Exploring the cosmic frontier.  
 In this coming of age,  
 We turn in our cage,  
 All alone on a tiny blue sphere.

#### 7.4.5 Reduced mass

We assumed in Section 7.4.1 that the sun is large enough so that it is only negligibly affected by the presence of the planets. That is, it is essentially fixed at the origin. But how do we solve a problem in which the masses of the two interacting bodies are comparable in size? Equivalently, how do we solve the earth–sun problem exactly? It turns out that the only modification required is a replacement of the earth's mass with the *reduced mass*, defined below. The following discussion actually holds for any central force, not just gravity.

The Lagrangian of a general central-force system consisting of the interacting masses  $m_1$  and  $m_2$  is

$$\mathcal{L} = \frac{1}{2}m_1\dot{\mathbf{r}}_1^2 + \frac{1}{2}m_2\dot{\mathbf{r}}_2^2 - V(|\mathbf{r}_1 - \mathbf{r}_2|). \quad (7.40)$$

We have written the potential in this form, dependent only on the distance  $|\mathbf{r}_1 - \mathbf{r}_2|$ , because we are assuming a central force. Let us define

$$\mathbf{R} \equiv \frac{m_1\mathbf{r}_1 + m_2\mathbf{r}_2}{m_1 + m_2}, \quad \text{and} \quad \mathbf{r} \equiv \mathbf{r}_1 - \mathbf{r}_2. \quad (7.41)$$

$\mathbf{R}$  and  $\mathbf{r}$  are the position of the center of mass and the vector between the masses, respectively. Invert these equations to obtain

$$\mathbf{r}_1 = \mathbf{R} + \frac{m_2}{M}\mathbf{r}, \quad \text{and} \quad \mathbf{r}_2 = \mathbf{R} - \frac{m_1}{M}\mathbf{r}, \quad (7.42)$$

where  $M \equiv m_1 + m_2$  is the total mass of the system. In terms of  $\mathbf{R}$  and  $\mathbf{r}$ , the Lagrangian becomes

$$\begin{aligned}\mathcal{L} &= \frac{1}{2}m_1\left(\dot{\mathbf{R}} + \frac{m_2}{M}\dot{\mathbf{r}}\right)^2 + \frac{1}{2}m_2\left(\dot{\mathbf{R}} - \frac{m_1}{M}\dot{\mathbf{r}}\right)^2 - V(|\mathbf{r}|) \\ &= \frac{1}{2}M\dot{\mathbf{R}}^2 + \frac{1}{2}\left(\frac{m_1m_2}{m_1+m_2}\right)\dot{\mathbf{r}}^2 - V(r) \\ &= \frac{1}{2}M\dot{\mathbf{R}}^2 + \frac{1}{2}\mu\dot{\mathbf{r}}^2 - V(r),\end{aligned}\quad (7.43)$$

where the *reduced mass*,  $\mu$ , is defined by

$$\frac{1}{\mu} \equiv \frac{1}{m_1} + \frac{1}{m_2}. \quad (7.44)$$

We now note that the Lagrangian in Eq. (7.43) depends on  $\dot{\mathbf{R}}$ , but not on  $\mathbf{R}$ . Therefore, the Euler–Lagrange equations say that  $\dot{\mathbf{R}}$  is constant. That is, the CM moves at constant velocity (this is just the statement that there are no external forces). The CM motion is therefore trivial, so let's ignore it. Our Lagrangian therefore becomes

$$\mathcal{L} \rightarrow \frac{1}{2}\mu\dot{\mathbf{r}}^2 - V(r). \quad (7.45)$$

But this is simply the Lagrangian for a particle of mass  $\mu$  that moves around a fixed origin under the influence of the potential  $V(r)$ . For gravity, we have

$$\mathcal{L} = \frac{1}{2}\mu\dot{\mathbf{r}}^2 + \frac{\alpha}{r} \quad (\text{where } \alpha \equiv GM_\odot m). \quad (7.46)$$

To solve the earth–sun system exactly, we therefore just need to replace (in the calculation in Section 7.4.1) the earth's mass,  $m$ , with the reduced mass,  $\mu$ , given by

$$\frac{1}{\mu} \equiv \frac{1}{m} + \frac{1}{M_\odot}. \quad (7.47)$$

The resulting value of  $r$  in Eq. (7.25) is the distance between the earth and sun. The earth and sun are therefore distances of  $(M_\odot/M)r$  and  $(m/M)r$ , respectively, away from the CM, from Eq. (7.42). These distances are just scaled-down versions of the distance  $r$ , which represents an ellipse, so we see that the earth and sun move in elliptical orbits (whose sizes are in the ratio  $M_\odot/m$ ) with the CM as a focus. Note that the  $m$ 's that are buried in  $L$  and  $\epsilon$  in Eq. (7.25) must be changed to  $\mu$ 's. But  $\alpha$  is still defined to be  $GM_\odot m$ , so the  $m$  in this definition does *not* get replaced with  $\mu$ .

For the earth–sun system, the  $\mu$  in Eq. (7.47) is essentially equal to  $m$ , because  $M_\odot$  is so large. Using  $m = 5.97 \cdot 10^{24}$  kg, and  $M_\odot = 1.99 \cdot 10^{30}$  kg, we find that

$\mu$  is smaller than  $m$  by only one part in  $3 \cdot 10^5$ . Our fixed-sun approximation is therefore a very good one. You can show that the CM is about  $5 \cdot 10^5$  m from the center of the sun, which is well inside the sun (about a thousandth of the radius).

How are Kepler's laws modified when we solve for the orbits exactly using the reduced mass?

- **First law:** The elliptical statement in the first law is still true, but with the CM (not the sun) located at a focus. The sun also travels in an ellipse with the CM at a focus.<sup>9</sup> Whatever is true for the earth must also be true for the sun, because they come into Eq. (7.43) symmetrically. The only difference is in the size of various quantities.
- **Second law:** In the second law, we need to consider the position vector from the CM (not the sun) to the earth. This vector sweeps out equal areas in equal times, because the angular momentum of the earth (and the sun, too) relative to the CM is constant. This is true because the gravitational force always points through the CM, so the force is a central force with the CM chosen as the origin.
- **Third law:** The period of the earth's orbit (and the sun's, too) is the same as the period of the orbit of our hypothetical particle of mass  $\mu$  orbiting around a fixed origin under the influence of the potential  $-\alpha/r \equiv -GM_\odot m/r$ . This is true because the radius vectors in all three of these systems are always in the same ratio. To find the period of the particle's orbit, we can repeat the derivation leading up to Eq. (7.39). But in that equation, the  $m$  on the bottom is replaced by  $\mu$ , while the  $m$  on the top remains  $m$ , because this is the  $m$  that appears in  $\alpha$ . Therefore, we obtain<sup>10</sup>

$$T^2 = \frac{4\pi^2 a_\mu^3 \mu}{GM_\odot m} = \frac{4\pi^2 a_\mu^3}{GM}, \quad (7.48)$$

where we have used  $\mu \equiv M_\odot m / (M_\odot + m) \equiv M_\odot m / M$ . This result is symmetric in  $M_\odot$  and  $m$ , as it must be because if we interchange the labels of  $M_\odot$  and  $m$ , we still have the same system. And it also correctly reduces to Eq. (7.36) when  $M_\odot \gg m$ .

If you want to write Eq. (7.48) in terms of the semi-major axis of the earth's elliptical orbit, which is  $a_E = (M_\odot/M)a_\mu$ , then just plug in  $a_\mu = (M/M_\odot)a_E$  to obtain

$$T^2 = \frac{4\pi^2 (M/M_\odot)^3 a_E^3}{GM} = \left( \frac{M^2}{M_\odot^2} \right) \frac{4\pi^2 a_E^3}{GM_\odot}. \quad (7.49)$$

Let's perform a check on this formula by considering the special case of equal masses  $m$  orbiting around the same circular path of radius  $r$  (at diametrically opposite points)

<sup>9</sup> Well, this statement is true only if there is just one planet. With many planets, the tiny motion of the sun is very complicated. This is perhaps the best reason to work in the approximation where it is essentially bolted down.

<sup>10</sup> We have put the subscript  $\mu$  on the length  $a$  to remind us that it is the semi-major axis of our hypothetical particle's orbit, and not the semi-major axis of the earth's orbit.

with their CM at the center of the circle. For this simple system, we can solve for the period from scratch using  $F = ma$ :

$$\frac{mv^2}{r} = \frac{Gm^2}{(2r)^2} \implies \frac{m(2\pi r/T)^2}{r} = \frac{Gm^2}{(2r)^2} \implies T^2 = \frac{16\pi^2 r^3}{Gm}, \quad (7.50)$$

which agrees with Eq. (7.49), in different notation, when  $M = 2M_\odot$ .

**REMARK:** There's actually a fairly quick way to see where the  $M^2/M_\odot^2$  factor in Eq. (7.49) comes from. Imagine a new system where the earth's orbit has the same dimensions but where the (slightly) moving sun is replaced by a stationary mass bolted down at the location of the earth–sun CM. This new mass is now a fraction  $M_\odot/M$  as far away from the earth as the sun was. Therefore, since the gravitational force is proportional to  $1/r^2$ , if we make our new mass equal to  $(M_\odot/M)^2 M_\odot$ , then it will exert the same force on the earth that the sun exerted. So if mother earth has her eyes closed, she'll never know the difference. The periods of these two systems must therefore be the same. But from Eq. (7.36), the period of the second system, which has a bolted-down mass, is

$$T^2 = \frac{4\pi^2 a_E^3}{G \cdot (M_\odot/M)^2 M_\odot}, \quad (7.51)$$

in agreement with Eq. (7.49). ♣

### 7.5 Problems

### Section 7.2: The effective potential

### 7.1. Exponential spiral \*

Given  $L$ , find the  $V(r)$  that leads to a spiral path of the form  $r = r_0 e^{a\theta}$ . Choose  $E$  to be zero. *Hint:* Obtain an expression for  $\dot{r}$  that contains no  $\theta$ 's, and then use Eq. (7.9).

#### 7.2. Cross section \*\*

A particle moves in a potential,  $V(r) = -C/(3r^3)$ .

- Given  $L$ , find the maximum value of the effective potential.
- Let the particle come in from infinity with speed  $v_0$  and impact parameter  $b$ . In terms of  $C$ ,  $m$ , and  $v_0$ , what is the largest value of  $b$  (call it  $b_{\max}$ ) for which the particle is captured by the potential? In other words, what is the “cross section” for capture,  $\pi b_{\max}^2$ , for this potential?

### 7.3. Maximum $L$ \*\*\*

A particle moves in a potential,  $V(r) = -V_0 e^{-\lambda^2 r^2}$ .

- Given  $L$ , find the radius of the stable circular orbit. An implicit equation is fine.
- It turns out that if  $L$  is too large, then no circular orbit exists. What is the largest value of  $L$  for which a circular orbit does in fact exist?

If  $r_0$  is the radius of the circle in this cutoff case, what is the value of  $V_{\text{eff}}(r_0)$ ?

### Section 7.4: Gravity, Kepler's laws

#### 7.4. $r^k$ potential \*\*\*

A particle of mass  $m$  moves in a potential given by  $V(r) = \beta r^k$ . Let the angular momentum be  $L$ .

- Find the radius,  $r_0$ , of the circular orbit.
- If the particle is given a tiny kick so that the radius oscillates around  $r_0$ , find the frequency,  $\omega_r$ , of these small oscillations in  $r$ .
- What is the ratio of the frequency  $\omega_r$  to the frequency of the (nearly) circular motion,  $\omega_\theta \equiv \dot{\theta}$ ? Give a few values of  $k$  for which the ratio is rational, that is, for which the path of the nearly circular motion closes back on itself.

### 7.5. Spring ellipse \*\*\*

A particle moves in a  $V(r) = \beta r^2$  potential. Following the general strategy in Sections 7.4.1 and 7.4.3, show that the particle's path is an ellipse.

### 7.6. $\beta/r^2$ potential \*\*\*

A particle is subject to a  $V(r) = \beta/r^2$  potential. Following the general strategy in Section 7.4.1, find the shape of the particle's path. You will need to consider various cases for  $\beta$ .

### 7.7. Rutherford scattering \*\*\*

A particle of mass  $m$  travels in a hyperbolic orbit past a mass  $M$ , whose position is assumed to be fixed. The speed at infinity is  $v_0$ , and the impact parameter is  $b$  (see Exercise 7.14).

- Show that the angle through which the particle is deflected is

$$\phi = \pi - 2 \tan^{-1}(\gamma b) \implies b = \frac{1}{\gamma} \cot\left(\frac{\phi}{2}\right), \quad (7.52)$$

where  $\gamma \equiv v_0^2/GM$ .

- Let  $d\sigma$  be the cross-sectional area (measured when the particle is initially at infinity) that gets deflected into a solid angle of size  $d\Omega$  at angle  $\phi$ .<sup>11</sup> Show that

$$\frac{d\sigma}{d\Omega} = \frac{1}{4\gamma^2 \sin^4(\phi/2)}. \quad (7.53)$$

<sup>11</sup> The *solid angle* of a patch on a sphere is the area of the patch divided by the square of the sphere's radius. So a whole sphere subtends a solid angle of  $4\pi$  *steradians* (the name for one unit of solid angle).

This quantity is called the *differential cross section*. *Note:* the label of this problem, *Rutherford scattering*, actually refers to the scattering of charged particles. But since the electrostatic and gravitational forces are both inverse-square laws, the scattering formulas look the same, except for a few constants.

### 7.6 Exercises

### Section 7.1: Conservation of angular momentum

### 7.8. Wrapping around a pole \*

A puck of mass  $m$  sliding on frictionless ice is attached by a horizontal string of length  $\ell$  to a thin vertical pole of radius  $R$ . The puck initially travels in (essentially) a circle around the pole at speed  $v_0$ . The string wraps around the pole, and the puck gets drawn in and eventually hits the pole. What quantity is conserved during this motion? What is the puck's speed right before it hits the pole?

### 7.9. String through a hole \*

A block of mass  $m$  sliding on a frictionless table is attached to a horizontal string that passes through a tiny hole in the table. The block initially travels in a circle of radius  $\ell$  around the hole at speed  $v_0$ . If you slowly pull the string down through the hole, what quantity is conserved during this motion? What is the block's speed when it is a distance  $r$  from the hole?

### Section 7.2: The effective potential

### 7.10. Power-law spiral \*\*

Given  $L$ , find the  $V(r)$  that leads to a spiral path of the form  $r = r_0\theta^k$ . Choose  $E$  to be zero. *Hint:* Obtain an expression for  $\dot{r}$  that contains no  $\theta$ 's, and then use Eq. (7.9).

### Section 7.4: Gravity, Kepler's laws

### 7.11. Circular orbit \*

For a circular orbit, derive Kepler's third law from scratch, using  $F = ma$ .

### 7.12. Falling into the sun \*

Imagine that the earth is suddenly (and tragically) stopped in its orbit, and then allowed to fall radially into the sun. How long will this take? Use data from Appendix J, and assume that the initial orbit is essentially circular. *Hint:* Consider the radial path to be part of a very thin ellipse.

### **7.13. Intersecting orbits \*\***

Two masses,  $m$  and  $2m$ , orbit around their CM. If the orbits are circular, they don't intersect. But if they are very elliptical, they do. What is the smallest value of the eccentricity for which they intersect?

### **7.14. Impact parameter \*\***

Show that the distance  $b$  defined in Eq. (7.34) and Fig. 7.9 is equal to the impact parameter. Do this:

- Geometrically, by showing that  $b$  is the distance from the origin to the dotted line in Fig. 7.9.
- Analytically, by letting the particle come in from infinity at speed  $v_0$  and impact parameter  $b'$ , and then showing that the  $b$  in Eq. (7.34) equals  $b'$ .

### **7.15. Closest approach \*\***

A particle with speed  $v_0$  and impact parameter  $b$  starts far away from a planet of mass  $M$ .

- Starting from scratch (that is, without using any of the results from Section 7.4), find the distance of closest approach to the planet.
- Use the results of the hyperbola discussion in Section 7.4.3 to show that the distance of closest approach to the planet is  $k/(\epsilon + 1)$ , and then show that this agrees with your answer to part (a).

### **7.16. Skimming a planet \*\***

A particle travels in a parabolic orbit in a planet's gravitational field and skims the surface at its closest approach. The planet has mass density  $\rho$ . Relative to the center of the planet, what is the angular velocity of the particle as it skims the surface?

### **7.17. Parabola $L$ \*\***

A mass  $m$  orbits around a planet of mass  $M$  in a parabolic orbit of the form  $y = x^2/(4\ell)$ , which has focal length  $\ell$ . Find the angular momentum in three different ways:

- Find the speed at closest approach.
- Use Eq. (7.30).
- Consider the point  $(x, x^2/4\ell)$ , where  $x$  is very large. Find approximate expressions for the speed and impact parameter at this point.

### **7.18. Circle to parabola \*\***

A spaceship travels in a circular orbit around a planet. It applies a sudden thrust and increases its speed by a factor  $f$ . If the goal is to change the orbit from a circle to a parabola, what should  $f$  be if the thrust points in

the tangential direction? Is your answer any different if the thrust points in some other direction? What is the distance of closest approach if the thrust points in the radial direction?

### 7.19. Zero potential \*\*

A particle is subject to a constant potential, which we will take to be zero (equivalently, consider the  $\alpha \equiv GMm = 0$  limit). Following the general strategy in Section 7.4, show that the particle's path is a straight line.

### 7.20. Ellipse axes \*\*

Taking it as given that Eq. (7.25) describes an ellipse for  $0 < \epsilon < 1$ , calculate the lengths of the semi-major and semi-minor axes, and show that the results agree with Eq. (7.33).

### 7.21. Repulsive potential \*\*

Consider an “anti-gravitational” potential (or more mundanely, the electrostatic potential between two like charges),  $V(r) = \alpha/r$ , where  $\alpha > 0$ . What is the basic change in the analysis of Section 7.4? Show that circular, elliptical, and parabolic orbits do not exist. Draw the figure analogous to Fig. 7.9 for the hyperbolic orbit.

### 7.7 Solutions

### 7.1. Exponential spiral

The given information  $r = r_0 e^{a\theta}$  yields (using  $\dot{\theta} = L/mr^2$ )

$$\dot{r} = a(r_0 e^{a\theta}) \dot{\theta} = ar \left( \frac{L}{mr^2} \right) = \frac{aL}{mr}. \quad (7.54)$$

Plugging this into Eq. (7.9) gives

$$\frac{m}{2} \left( \frac{aL}{mr} \right)^2 + \frac{L^2}{2mr^2} + V(r) = E = 0. \quad (7.55)$$

Therefore,

$$V(r) = -\frac{(1+a^2)L^2}{2mr^2}. \quad (7.56)$$

### 7.2. Cross section

(a) The effective potential is

$$V_{\text{eff}}(r) = \frac{L^2}{2mr^2} - \frac{C}{3r^3}. \quad (7.57)$$

Setting the derivative equal to zero gives  $r = mC/L^2$ . Plugging this into  $V_{\text{eff}}(r)$  gives

$$V_{\text{eff}}^{\text{max}} = \frac{L^6}{6m^3 C^2}. \quad (7.58)$$

(b) If the energy  $E$  of the particle is less than  $V_{\text{eff}}^{\text{max}}$ , then the particle will reach a minimum value of  $r$ , and then head back out to infinity (see Fig. 7.11). If  $E$  is

![Figure 7.11: A graph of the effective potential V_eff(r) versus r. The curve starts at negative infinity for small r, rises to a local maximum at r_min, and then decreases towards zero. A horizontal dashed line represents the total energy E, which is below the maximum of the potential curve. The intersection of the curve and the energy line determines the minimum distance r_min.](7f3f0081a9a8cd6279be3fd9245912d9_img.jpg)

Figure 7.11: A graph of the effective potential V\_eff(r) versus r. The curve starts at negative infinity for small r, rises to a local maximum at r\_min, and then decreases towards zero. A horizontal dashed line represents the total energy E, which is below the maximum of the potential curve. The intersection of the curve and the energy line determines the minimum distance r\_min.

Fig. 7.11

greater than  $V_{\text{eff}}^{\text{max}}$ , then the particle will head all the way in to  $r = 0$ , never to return. The condition for capture is therefore  $V_{\text{eff}}^{\text{max}} < E$ . Using  $L = mv_0 b$  and  $E = E_\infty = mv_0^2/2$ , this condition becomes

$$\frac{(mv_0 b)^6}{6m^3 C^2} < \frac{mv_0^2}{2} \implies b < \left( \frac{3C^2}{m^2 v_0^4} \right)^{1/6} \equiv b_{\text{max}}. \quad (7.59)$$

The cross section for capture is therefore

$$\sigma = \pi b_{\text{max}}^2 = \pi \left( \frac{3C^2}{m^2 v_0^4} \right)^{1/3}. \quad (7.60)$$

It makes sense that this should increase with  $C$  and decrease with  $m$  and  $v_0$ .

### 7.3. Maximum $L$

(a) The effective potential is

$$V_{\text{eff}}(r) = \frac{L^2}{2mr^2} - V_0 e^{-\lambda^2 r^2}. \quad (7.61)$$

A circular orbit exists at the value(s) of  $r$  for which  $V'_{\text{eff}}(r) = 0$ . Setting the derivative equal to zero and solving for  $L^2$  gives

$$L^2 = (2mV_0\lambda^2)r^4 e^{-\lambda^2 r^2}. \quad (7.62)$$

This implicitly determines  $r$ . As long as  $L$  isn't too large,  $V_{\text{eff}}(r)$  looks something like the graph in Fig. 7.12, although it doesn't necessarily dip down to negative values; see the remark below. You can arrive at this picture by noting that for any  $L$ ,  $V_{\text{eff}}(r)$  behaves like  $1/r^2$  for both  $r \rightarrow 0$  and  $r \rightarrow \infty$ ; and for sufficiently small  $L$ ,  $V_{\text{eff}}(r)$  reaches negative values somewhere in between, due to the  $-V_0$  term. The curve must therefore look like the one shown, which has two locations where  $V'_{\text{eff}}(r) = 0$ . The smaller solution is the one with the stable orbit. However, if  $L$  is too large, then there are no solutions to  $V'_{\text{eff}}(r) = 0$ , because  $V_{\text{eff}}(r)$  decreases monotonically to zero (because  $L^2/2mr^2$  does so). We'll be quantitative about this in part (b).

(b) The function  $r^4 e^{-\lambda^2 r^2}$  on the right-hand side of Eq. (7.62) has a maximum value, because it goes to zero for both  $r \rightarrow 0$  and  $r \rightarrow \infty$ . Therefore, there is a maximum value of  $L$  for which a solution for  $r$  exists. The maximum of  $r^4 e^{-\lambda^2 r^2}$  occurs where

$$0 = \frac{d(r^4 e^{-\lambda^2 r^2})}{dr} = e^{-\lambda^2 r^2} (4r^3 + r^4(-2\lambda^2 r)) \implies r^2 = \frac{2}{\lambda^2} \equiv r_0^2. \quad (7.63)$$

Plugging  $r_0$  into Eq. (7.62) gives

$$L_{\text{max}}^2 = \frac{8mV_0}{\lambda^2 e^2}. \quad (7.64)$$

Plugging  $r_0$  and  $L_{\text{max}}^2$  into Eq. (7.61) gives

$$V_{\text{eff}}(r_0) = \frac{V_0}{e^2} \quad (\text{for } L = L_{\text{max}}). \quad (7.65)$$

Note that this is greater than zero. For the  $L = L_{\text{max}}$  case, the graph of  $V_{\text{eff}}$  is shown in Fig. 7.13. This is the cutoff case between having a dip in the graph, and decreasing monotonically to zero.

REMARK: A common error in this problem is to say that the condition for a circular orbit to exist is that  $V_{\text{eff}}(r) < 0$  at the point where  $V_{\text{eff}}(r)$  is minimum.

![Graph of the effective potential V_eff(r) versus r. The curve starts at a high positive value for small r, decreases to a local minimum, then increases to a local maximum, and finally decreases towards zero as r increases. The curve crosses the r-axis at two points, indicating two circular orbits.](e1244c744e6ec6f051e164cb417d2c75_img.jpg)

Graph of the effective potential V\_eff(r) versus r. The curve starts at a high positive value for small r, decreases to a local minimum, then increases to a local maximum, and finally decreases towards zero as r increases. The curve crosses the r-axis at two points, indicating two circular orbits.

Fig. 7.12

![Graph of the effective potential V_eff(r) versus r for the cutoff case L = L_max. The curve starts at a high positive value for small r, decreases monotonically, and approaches zero from above as r increases. There is no dip or local minimum below zero.](136dcfad49784d6316af1d44ae9a7d09_img.jpg)

Graph of the effective potential V\_eff(r) versus r for the cutoff case L = L\_max. The curve starts at a high positive value for small r, decreases monotonically, and approaches zero from above as r increases. There is no dip or local minimum below zero.

Fig. 7.13

![Graph of the effective potential V_eff(r) versus r. The curve starts at a high value for small r, decreases to a local minimum, and then increases slightly before leveling off. The horizontal axis is labeled r and the vertical axis is labeled V_eff(r).](5ae9490cf914964d7bc2af64168e38cd_img.jpg)

Graph of the effective potential V\_eff(r) versus r. The curve starts at a high value for small r, decreases to a local minimum, and then increases slightly before leveling off. The horizontal axis is labeled r and the vertical axis is labeled V\_eff(r).

Fig. 7.14

The logic here is that since the goal is to have a well in which the particle can be trapped, it seems like we just need  $V_{\text{eff}}$  to achieve a value less than the value at  $r = \infty$ , namely 0. However, this gives the wrong answer ( $L_{\text{max}}^2 = 2mV_0/\lambda^2 e$ , as you can show), because  $V_{\text{eff}}(r)$  can look like the graph in Fig. 7.14. This has a local minimum with  $V_{\text{eff}}(r) > 0$ . ♣

### 7.4. $r^k$ potential

- (a) A circular orbit exists at the value of  $r$  for which the derivative of the effective potential (which is the negative of the effective force) is zero. This is simply the statement that the right-hand side of Eq. (7.8) equals zero, so that  $\ddot{r} = 0$ . Since  $V'(r) = \beta k r^{k-1}$ , Eq. (7.8) gives

$$\frac{L^2}{mr^3} - \beta k r^{k-1} = 0 \implies r_0 = \left( \frac{L^2}{m\beta k} \right)^{1/(k+2)}. \quad (7.66)$$

If  $k$  is negative, then  $\beta$  must also be negative if there is to be a real solution for  $r_0$ .

- (b) The long method of finding the frequency is to set  $r(t) \equiv r_0 + \epsilon(t)$ , where  $\epsilon$  represents the small deviation from the circular orbit, and to then plug this expression for  $r$  into Eq. (7.8). The result (after making some approximations) is a harmonic-oscillator equation of the form  $\ddot{\epsilon} = -\omega_r^2 \epsilon$ . This general procedure, which was described in detail in Section 6.7, will work fine here (as you are encouraged to show), but let's use an easier method.

By introducing the effective potential, we have reduced the problem to a one-dimensional problem in the variable  $r$ . Therefore, we can make use of the result in Section 5.2, where we found in Eq. (5.20) that to find the frequency of small oscillations, we just need to calculate the second derivative of the potential. For the problem at hand, we must use the effective potential, because that is what determines the motion of the variable  $r$ . We therefore have

$$\omega_r = \sqrt{\frac{V''_{\text{eff}}(r_0)}{m}}. \quad (7.67)$$

If you work through the  $r \equiv r_0 + \epsilon$  method described above, you will find that you are basically calculating the second derivative of  $V_{\text{eff}}$ , but in a rather cumbersome way.

Using the form of the effective potential, we have

$$V''_{\text{eff}}(r_0) = \frac{3L^2}{mr_0^4} + \beta k(k-1)r_0^{k-2} = \frac{1}{r_0^4} \left( \frac{3L^2}{m} + \beta k(k-1)r_0^{k+2} \right). \quad (7.68)$$

Using the  $r_0$  from Eq. (7.66), this simplifies to

$$V''_{\text{eff}}(r_0) = \frac{L^2(k+2)}{mr_0^4} \implies \omega_r = \sqrt{\frac{V''_{\text{eff}}(r_0)}{m}} = \frac{L\sqrt{k+2}}{mr_0^2}. \quad (7.69)$$

We could get rid of the  $r_0$  here by using Eq. (7.66), but this form of  $\omega_r$  will be more useful in part (c).

Note that we must have  $k > -2$  for  $\omega_r$  to be real. If  $k < -2$ , then  $V''_{\text{eff}}(r_0) < 0$ , which means that we have a local maximum of  $V_{\text{eff}}$ , instead of a local minimum. In other words, the circular orbit is unstable. Small perturbations grow, instead of oscillating around zero.

- (c) Since  $L = mr_0^2\dot{\theta}$  for the circular orbit, we have  $\omega_\theta \equiv \dot{\theta} = L/(mr_0^2)$ . Combining this with Eq. (7.69), we find

$$\frac{\omega_r}{\omega_\theta} = \sqrt{k+2}. \quad (7.70)$$

![Figure 7.15: Four plots of orbits in the (r, theta) plane for different values of k. The plots show the radial distance r as a function of the angle theta. The orbits are nearly circular for k = -1 and k = -7/4, and elliptical for k = 2 and k = 7. The dashed lines represent the initial circular orbit, and the solid lines represent the perturbed orbit.](72cb9810bdc686501f939b719531b0fd_img.jpg)

$k = -1$ 
 $k = 2$ 
 $k = 7$ 
 $k = -7/4$

Figure 7.15: Four plots of orbits in the (r, theta) plane for different values of k. The plots show the radial distance r as a function of the angle theta. The orbits are nearly circular for k = -1 and k = -7/4, and elliptical for k = 2 and k = 7. The dashed lines represent the initial circular orbit, and the solid lines represent the perturbed orbit.

Fig. 7.15

A few values of  $k$  that yield rational values for this ratio are (the plots of the orbits are shown in Fig. 7.15):

- $k = -1 \implies \omega_r/\omega_\theta = 1$ : This is the gravitational potential. The variable  $r$  makes one oscillation for each complete revolution of the (nearly) circular orbit.
- $k = 2 \implies \omega_r/\omega_\theta = 2$ : This is the spring potential. The variable  $r$  makes two oscillations for each complete revolution.
- $k = 7 \implies \omega_r/\omega_\theta = 3$ : The variable  $r$  makes three oscillations for each complete revolution.
- $k = -7/4 \implies \omega_r/\omega_\theta = 1/2$ : The variable  $r$  makes half of an oscillation for each complete revolution. So we need to have two revolutions to get back to the same value of  $r$ .

There is an infinite number of  $k$  values that yield closed orbits. But note that this statement applies only to orbits that are nearly circular. Also, the “closed” nature of the orbits is only approximate, because it is based on Eq. (7.67) which is an approximate result based on small oscillations. The only  $k$  values that lead to exactly closed orbits for any initial conditions are  $k = -1$  (gravity) and  $k = 2$  (spring), and in both cases the orbits are ellipses. This result is known as Bertrand’s theorem; see Brown (1978).

### 7.5. Spring ellipse

With  $V(r) = \beta r^2$ , Eq. (7.16) becomes

$$\left(\frac{1}{r^2} \frac{dr}{d\theta}\right)^2 = \frac{2mE}{L^2} - \frac{1}{r^2} - \frac{2m\beta r^2}{L^2}. \quad (7.71)$$

As stated in Section 7.4.1, we could take a square root, separate variables, integrate to find  $\theta(r)$ , and then invert to find  $r(\theta)$ . But let’s solve for  $r(\theta)$  in a slick way, as we did for the gravitational case, where we made the change of variables,  $y \equiv 1/r$ . Since there are lots of  $r^2$  terms floating around in Eq. (7.71), it’s reasonable to try the change of variables,  $y \equiv r^2$  or  $y \equiv 1/r^2$ . The latter turns out to be the better choice. So, using  $y \equiv 1/r^2$  and  $dy/d\theta = -2(dr/d\theta)/r^3$ , and multiplying Eq. (7.71) through by  $1/r^2$ , we obtain

$$\begin{aligned} \left(\frac{1}{2} \frac{dy}{d\theta}\right)^2 &= \frac{2mEy}{L^2} - y^2 - \frac{2m\beta}{L^2} \\ &= -\left(y - \frac{mE}{L^2}\right)^2 - \frac{2m\beta}{L^2} + \left(\frac{mE}{L^2}\right)^2. \end{aligned} \quad (7.72)$$

Defining  $z \equiv y - mE/L^2$  for convenience, we have

$$\begin{aligned} \left(\frac{dz}{d\theta}\right)^2 &= -4z^2 + 4\left(\frac{mE}{L^2}\right)^2 \left(1 - \frac{2\beta L^2}{mE^2}\right) \\ &\equiv -4z^2 + 4B^2. \end{aligned} \quad (7.73)$$

As in Section 7.4.1, we can just look at this equation and observe that

$$z = B \cos 2(\theta - \theta_0) \quad (7.74)$$

is the solution. We can rotate the axes so that  $\theta_0 = 0$ , so we'll drop the  $\theta_0$  from here on. Recalling our definition  $z \equiv 1/r^2 - mE/L^2$  and also the definition of  $B$  from Eq. (7.73), Eq. (7.74) becomes

$$\frac{1}{r^2} = \frac{mE}{L^2} (1 + \epsilon \cos 2\theta), \quad (7.75)$$

where

$$\epsilon \equiv \sqrt{1 - \frac{2\beta L^2}{mE^2}}. \quad (7.76)$$

It turns out, as we'll see below, that  $\epsilon$  is *not* the eccentricity of the ellipse, as it was in the gravitational case.

We will now use the procedure in Section 7.4.3 to show that Eq. (7.76) represents an ellipse. For convenience, let

$$k \equiv \frac{L^2}{mE}. \quad (7.77)$$

Multiplying Eq. (7.75) through by  $kr^2$ , and using

$$\cos 2\theta = \cos^2 \theta - \sin^2 \theta = \frac{x^2}{r^2} - \frac{y^2}{r^2}, \quad (7.78)$$

and also  $r^2 = x^2 + y^2$ , we obtain  $k = (x^2 + y^2) + \epsilon(x^2 - y^2)$ . This can be written as

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, \quad \text{where } a = \sqrt{\frac{k}{1 + \epsilon}}, \quad \text{and } b = \sqrt{\frac{k}{1 - \epsilon}}. \quad (7.79)$$

This is the equation for an ellipse with its center located at the origin (as opposed to a focus located at the origin, as in the gravitational case). In Fig. 7.16, the semi-major and semi-minor axes are  $b$  and  $a$ , respectively, and the focal length is  $c = \sqrt{b^2 - a^2} = \sqrt{2k\epsilon/(1 - \epsilon^2)}$ . The eccentricity is  $c/b = \sqrt{2\epsilon/(1 + \epsilon)}$ .

![Figure 7.16: A diagram of an ellipse centered at the origin of a Cartesian coordinate system with x and y axes. The semi-major axis is labeled 'b' along the y-axis, and the semi-minor axis is labeled 'a' along the x-axis. A dashed line segment from the origin to the ellipse represents the focal length 'c'. The eccentricity is indicated as c/b.](5d2ef26f2e414efbbbae7783204095f1_img.jpg)

Figure 7.16: A diagram of an ellipse centered at the origin of a Cartesian coordinate system with x and y axes. The semi-major axis is labeled 'b' along the y-axis, and the semi-minor axis is labeled 'a' along the x-axis. A dashed line segment from the origin to the ellipse represents the focal length 'c'. The eccentricity is indicated as c/b.

Fig. 7.16

**REMARK:** If  $\epsilon = 0$ , then  $a = b$ , which means that the ellipse is actually a circle. Let's see if this makes sense. Looking at Eq. (7.76), we see that we want to show that circular motion implies  $2\beta L^2 = mE^2$ . For circular motion, the radial  $F = ma$  equation is  $mv^2/r = 2\beta r \implies v^2 = 2\beta r^2/m$ . The energy is therefore  $E = mv^2/2 + \beta r^2 = 2\beta r^2$ . Also, the square of the angular momentum is  $L^2 = m^2 v^2 r^2 = 2m\beta r^4$ . Therefore,  $2\beta L^2 = 2\beta(2m\beta r^4) = m(2\beta r^2)^2 = mE^2$ , as we wanted to show. ♣

### 7.6. $\beta/r^2$ potential

With  $V(r) = \beta/r^2$ , Eq. (7.16) becomes

$$\begin{aligned} \left( \frac{1}{r^2} \frac{dr}{d\theta} \right)^2 &= \frac{2mE}{L^2} - \frac{1}{r^2} - \frac{2m\beta}{r^2 L^2} \\ &= \frac{2mE}{L^2} - \frac{1}{r^2} \left( 1 + \frac{2m\beta}{L^2} \right). \end{aligned} \quad (7.80)$$

Letting  $y \equiv 1/r$ , and using  $dy/d\theta = -(1/r^2)(dr/d\theta)$ , this becomes

$$\left( \frac{dy}{d\theta} \right)^2 + a^2 y^2 = \frac{2mE}{L^2}, \quad \text{where } a^2 \equiv 1 + \frac{2m\beta}{L^2}. \quad (7.81)$$

We must now consider various possibilities for  $a^2$ . These possibilities depend on how  $\beta$  compares to  $L^2$ , which depends on the initial conditions of the motion. In what follows, note that the effective potential equals

$$V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + \frac{\beta}{r^2} = \frac{a^2 L^2}{2mr^2}. \quad (7.82)$$

CASE 1:  $a^2 > 0$ , or equivalently  $\beta > -L^2/2m$ . In this case, the effective potential looks like the graph in Fig. 7.17. The solution for  $y$  in Eq. (7.81) is a trig function, which we will take to be a “sin” by appropriately rotating the axes. Using  $y \equiv 1/r$ , we obtain

$$\frac{1}{r} = \frac{1}{a} \sqrt{\frac{2mE}{L^2}} \sin a\theta. \quad (7.83)$$

$\theta = 0$  and  $\theta = \pi/a$  make the right-hand side equal to zero, so they correspond to  $r = \infty$ . And  $\theta = \pi/2a$  makes the right-hand side maximum, so it corresponds to the minimum value of  $r$ , which is  $r_{\min} = a\sqrt{L^2/2mE}$ . This minimum  $r$  can also be obtained in a much quicker manner by finding where  $V_{\text{eff}}(r) = E$ .

If the particle comes in from infinity at  $\theta = 0$ , it eventually heads back out to infinity at  $\theta = \pi/a$ . The angle that the outgoing path makes with the incoming path is therefore  $\pi/a$ . So if  $a$  is large (that is, if  $\beta$  is large and positive, or if  $L$  is small), then the particle bounces nearly straight backward. If  $a$  is small (that is, if  $\beta$  is negative and if  $L^2$  is only slightly larger than  $-2m\beta$ ), then the particle spirals around many times before it pops back out to infinity.

A few special cases are: (1)  $\beta = 0 \implies a = 1$ , which means that the total angle is  $\pi$ , that is, there is no net deflection. In fact, the particle’s path is a straight line, because the potential is zero; see Exercise 7.19. (2)  $L^2 = -8m\beta/3 \implies a = 1/2$ , which means that the total angle is  $2\pi$ , that is, the final line of the particle’s motion is (anti)parallel to the initial line. These lines are shifted sideways from one another, with the separation depending on the initial conditions.

CASE 2:  $a = 0$ , or equivalently  $\beta = -L^2/2m$ . In this case, the effective potential is identically zero, as shown in Fig. 7.18. Equation (7.81) becomes

$$\left(\frac{dy}{d\theta}\right)^2 = \frac{2mE}{L^2}. \quad (7.84)$$

The solution to this is  $y = \theta\sqrt{2mE/L^2} + C$ , which gives

$$r = \frac{1}{\theta} \sqrt{\frac{L^2}{2mE}}, \quad (7.85)$$

where we have set the integration constant  $C$  equal to zero by choosing  $\theta = 0$  to be the angle that corresponds to  $r = \infty$ . Note that we can use  $\beta = -L^2/2m$  to write  $r$  as  $r = (1/\theta)\sqrt{-\beta/E}$ .

Since the effective potential is flat, the rate of change of  $r$  is constant. Therefore, if the particle has  $\dot{r} < 0$ , it will reach the origin in finite time, even though Eq. (7.85) says that it will spiral around the origin an infinite number of times (because  $\theta \rightarrow \infty$  as  $r \rightarrow 0$ ).

CASE 3:  $a^2 < 0$ , or equivalently  $\beta < -L^2/2m$ . In this case, we have the situation shown in either Fig. 7.19 or Fig. 7.20, depending on the sign of  $E$ . For convenience, let  $b$  be the positive real number such that  $b^2 = -a^2$ . Then Eq. (7.81) becomes

$$\left(\frac{dy}{d\theta}\right)^2 - b^2 y^2 = \frac{2mE}{L^2}. \quad (7.86)$$

![Figure 7.17: A graph of the effective potential V_eff(r) versus r. The potential curve is a hyperbola-like shape in the first quadrant, starting from a high value at small r and decreasing towards zero as r increases. A horizontal dashed line represents the total energy E, which intersects the potential curve at a point corresponding to r_min on the r-axis.](92f11ee5b920313b8ee66e9fd1bb1c64_img.jpg)

Figure 7.17: A graph of the effective potential V\_eff(r) versus r. The potential curve is a hyperbola-like shape in the first quadrant, starting from a high value at small r and decreasing towards zero as r increases. A horizontal dashed line represents the total energy E, which intersects the potential curve at a point corresponding to r\_min on the r-axis.

Fig. 7.17

![Figure 7.18: A graph of the effective potential V_eff(r) versus r. The potential is identically zero, represented by a horizontal line along the r-axis. A horizontal dashed line represents the total energy E at a positive value. An arrow points to the r-axis with the label V_eff(r) = 0.](b2b5cc654f851c7564b67ed427191612_img.jpg)

Figure 7.18: A graph of the effective potential V\_eff(r) versus r. The potential is identically zero, represented by a horizontal line along the r-axis. A horizontal dashed line represents the total energy E at a positive value. An arrow points to the r-axis with the label V\_eff(r) = 0.

Fig. 7.18

![Figure 7.19: A graph of the effective potential V_eff(r) versus r. The potential curve is in the fourth quadrant, starting from a negative value at small r and increasing towards zero as r increases. A horizontal dashed line represents the total energy E at a positive value. The potential curve approaches the r-axis asymptotically from below.](d237ba968ff03929313a16484cda0316_img.jpg)

Figure 7.19: A graph of the effective potential V\_eff(r) versus r. The potential curve is in the fourth quadrant, starting from a negative value at small r and increasing towards zero as r increases. A horizontal dashed line represents the total energy E at a positive value. The potential curve approaches the r-axis asymptotically from below.

Fig. 7.19

![Figure 7.20: A graph of the effective potential V_eff(r) versus r. The potential curve is in the fourth quadrant, starting from a negative value at small r and increasing towards zero as r increases. A horizontal dashed line represents the total energy E at a negative value. The potential curve approaches the r-axis asymptotically from below. A point r_max is marked on the r-axis where the potential curve intersects the energy line E.](f693b888cff0fad9eb066e61cf9c0f33_img.jpg)

Figure 7.20: A graph of the effective potential V\_eff(r) versus r. The potential curve is in the fourth quadrant, starting from a negative value at small r and increasing towards zero as r increases. A horizontal dashed line represents the total energy E at a negative value. The potential curve approaches the r-axis asymptotically from below. A point r\_max is marked on the r-axis where the potential curve intersects the energy line E.

Fig. 7.20

The solution to this equation is a hyperbolic trig function. But we must consider two cases:

- $E > 0$ : Using the identity  $\cosh^2 z - \sinh^2 z = 1$ , and recalling  $y \equiv 1/r$ , we see that the solution to Eq. (7.86) is<sup>12</sup>

$$\frac{1}{r} = \frac{1}{b} \sqrt{\frac{2mE}{L^2}} \sinh b\theta. \quad (7.87)$$

Unlike the  $a^2 > 0$  case above, the  $\sinh$  function has no maximum value. Therefore, the right-hand side can head to infinity, which means that  $r$  can head to zero, if the initial  $\dot{r}$  is negative. It does so in a finite time, because  $\dot{r}$  only becomes more negative as time goes by, from Fig. 7.19. For large  $z$ , we have  $\sinh z \approx e^z/2$ , so  $r$  heads to zero like  $e^{-b\theta}$ . The particle will therefore spiral around the origin an infinite number of times (because  $\theta \rightarrow \infty$  as  $r \rightarrow 0$ ).

- $E < 0$ : In this case, Eq. (7.86) can be rewritten as

$$b^2 y^2 - \left( \frac{dy}{d\theta} \right)^2 = \frac{2m|E|}{L^2}. \quad (7.88)$$

The solution to this equation is<sup>13</sup>

$$\frac{1}{r} = \frac{1}{b} \sqrt{\frac{2m|E|}{L^2}} \cosh b\theta. \quad (7.89)$$

As in the  $\sinh$  case, the  $\cosh$  function has no maximum value. Therefore, the right-hand side can head to infinity, which means that  $r$  can head to zero. But in the present  $\cosh$  case, the right-hand side does achieve a nonzero minimum value, when  $\theta = 0$ . So  $r$  achieves a maximum value (if the initial  $\dot{r}$  is positive) equal to  $r_{\max} = b\sqrt{L^2/2m|E|}$ . This is clear from Fig. 7.20. This maximum  $r$  can also be obtained by simply finding where  $V_{\text{eff}}(r) = E$ . After reaching  $r_{\max}$ , the particle heads back down to the origin with behavior similar (for large  $\theta$ ) to the  $\sinh$  case.

![Figure 7.21: A diagram illustrating Rutherford scattering. A particle follows a hyperbolic trajectory in a 2D Cartesian coordinate system (x, y). The trajectory is shown as a solid line with arrows indicating the direction of motion. The impact parameter 'b' is the perpendicular distance from the y-axis to the asymptote of the hyperbola. The distance of closest approach is labeled 'a'. The angle of deflection 'phi' is shown between the initial and final velocity vectors, which are represented by dashed lines parallel to the asymptotes of the hyperbola.](83c99c6d7a60fd0100579a93a89572e0_img.jpg)

Figure 7.21: A diagram illustrating Rutherford scattering. A particle follows a hyperbolic trajectory in a 2D Cartesian coordinate system (x, y). The trajectory is shown as a solid line with arrows indicating the direction of motion. The impact parameter 'b' is the perpendicular distance from the y-axis to the asymptote of the hyperbola. The distance of closest approach is labeled 'a'. The angle of deflection 'phi' is shown between the initial and final velocity vectors, which are represented by dashed lines parallel to the asymptotes of the hyperbola.

Fig. 7.21

### 7.7. Rutherford scattering

- (a) From Exercise 7.14, we know that the impact parameter  $b$  equals the distance  $b$  shown in Fig. 7.9. Therefore, Fig. 7.21 tells us that the angle of deflection (the angle between the initial and final velocity vectors) is

$$\phi = \pi - 2 \tan^{-1} \left( \frac{b}{a} \right). \quad (7.90)$$

But from Eqs. (7.34) and (7.26), we have

$$\frac{b}{a} = \sqrt{\epsilon^2 - 1} = \sqrt{\frac{2EL^2}{m\alpha^2}} = \sqrt{\frac{2(mv_0^2/2)(mv_0b)^2}{m(GMm)^2}} = \frac{v_0^2 b}{GM}. \quad (7.91)$$

Substituting this into Eq. (7.90), with  $\gamma \equiv v_0^2/(GM)$ , gives the first expression in Eq. (7.52). Dividing by 2 and taking the cotangent of both sides then gives the second expression,

$$b = \frac{1}{\gamma} \cot \left( \frac{\phi}{2} \right). \quad (7.92)$$

It actually isn't necessary to go through all the work of Section 7.4.3 to obtain this result via  $a$  and  $b$ . We can just use Eq. (7.25), which says that  $r \rightarrow \infty$  when

<sup>12</sup> More generally, we should write  $\sinh(\theta - \theta_0)$  here. But we can eliminate the need for  $\theta_0$  by picking  $\theta = 0$  to be the angle that corresponds to  $r = \infty$ .

<sup>13</sup> Again, we should write  $\cosh(\theta - \theta_0)$  here. But we can eliminate the need for  $\theta_0$  by picking  $\theta = 0$  to be the angle that corresponds to the maximum value of  $r$ .

$\cos \theta \rightarrow -1/\epsilon$ . This then implies that the dotted lines in Fig. 7.21 have slope  $\tan \theta = \sqrt{\sec^2 \theta - 1} = \sqrt{\epsilon^2 - 1}$ , which reproduces Eq. (7.91).

- (b) Imagine a wide beam of particles moving in the positive  $x$  direction toward the mass  $M$ . Consider a thin cross-sectional ring in this beam, with radius  $b$  and thickness  $db$ . Now consider a very large sphere centered at  $M$ . Any particle that passes through the cross-sectional ring of radius  $b$  will hit this sphere in a ring located at an angle  $\phi$  relative to the  $x$  axis, with an angular spread of  $d\phi$ . The relation between  $db$  and  $d\phi$  is found from Eq. (7.92). Using  $d(\cot \beta)/d\beta = -1/\sin^2 \beta$ , we have

$$\left| \frac{db}{d\phi} \right| = \frac{1}{2\gamma \sin^2(\phi/2)}. \quad (7.93)$$

The area of the incident cross-sectional ring is  $d\sigma = 2\pi b |db|$ . What is the solid angle subtended by a ring at angle  $\phi$  with thickness  $d\phi$ ? Taking the radius of the large sphere to be  $R$  (which will cancel out), the radius of the ring is  $R \sin \phi$ , and the width is  $R |d\phi|$ . The area of the ring is therefore  $2\pi (R \sin \phi) (R |d\phi|)$ , and so the solid angle subtended by the ring is  $d\Omega = 2\pi \sin \phi |d\phi|$  steradians. Therefore, the differential cross section is

$$\begin{aligned} \frac{d\sigma}{d\Omega} &= \frac{2\pi b |db|}{2\pi \sin \phi |d\phi|} = \left( \frac{b}{\sin \phi} \right) \left| \frac{db}{d\phi} \right| \\ &= \left( \frac{(1/\gamma) \cot(\phi/2)}{2 \sin(\phi/2) \cos(\phi/2)} \right) \left( \frac{1}{2\gamma \sin^2(\phi/2)} \right) \\ &= \frac{1}{4\gamma^2 \sin^4(\phi/2)}. \end{aligned} \quad (7.94)$$

**REMARKS:** What does this “differential cross section” result tell us? It tells us that if we want to find out how much cross-sectional area gets mapped into the solid angle  $d\Omega$  at the angle  $\phi$ , then we can use Eq. (7.94) to say (recalling  $\gamma \equiv v_0^2/GM$ ),

$$d\sigma = \frac{G^2 M^2}{4v_0^4 \sin^4(\phi/2)} d\Omega \quad \Rightarrow \quad d\sigma = \frac{G^2 M^2 m^2}{16E^2 \sin^4(\phi/2)} d\Omega, \quad (7.95)$$

where we have used  $E = mv_0^2/2$  to obtain the second expression. Let’s look at some special cases. If  $\phi \approx 180^\circ$  (that is, backward scattering), then the amount of area that gets scattered into a nearly backward solid angle of  $d\Omega$  equals  $d\sigma = (G^2 M^2 / 4v_0^4) d\Omega$ . If  $v_0$  is small, then we see that  $d\sigma$  is large, that is, a large area gets deflected nearly straight backward. This makes sense, because with  $v_0 \approx 0$ , the orbit is essentially parabolic, which means that the initial and final velocities at infinity are (anti)parallel. (If you release a particle from rest far away from a gravitational source, it will come back to you. Assuming it doesn’t bump into the source, of course.) If  $v_0$  is large, then we see that  $d\sigma$  is small, that is, only a small area gets deflected backward. This makes sense, because the particle is more likely to fly past  $M$  without much deflection if it is moving fast, because the force has hardly any time to act. The particle needs to start with a very small  $b$  value (which corresponds to a very small area) in order to get close enough to  $M$  to allow there to be a large enough force to swing it around.

Another special case is  $\phi \approx 0$ , that is, negligible deflection. In this case, Eq. (7.95) tells us that the amount of area that gets scattered into a nearly forward solid angle of  $d\Omega$  is  $d\sigma \approx \infty$ . This makes sense, because if the impact parameter  $b$  is large (and there is an infinite cross-sectional area for which this is true), then

the particle will hardly feel the mass  $M$ , so it will continue to move essentially in a straight line.<sup>14</sup>

What if we consider the electrostatic force, instead of the gravitational force? What is the differential cross section in this case? To answer this, note that we can rewrite  $\gamma$  as

$$\gamma = \frac{v_0^2}{GM} = \frac{2(mv_0^2/2)}{GMm} \equiv \frac{2E}{\alpha}. \quad (7.96)$$

In the case of electrostatics, the force takes the form,  $F_e = kq_1q_2/r^2$ . This looks like the gravitational force,  $F_g = Gm_1m_2/r^2$ , except that the constant  $\alpha$  is now  $kq_1q_2$ , instead of  $Gm_1m_2$ . Therefore, the  $\gamma$  in Eq. (7.96) becomes  $\gamma_e = 2E/(kq_1q_2)$ . Substituting this into Eq. (7.94), or equivalently replacing  $GMm$  by  $kq_1q_2$  in Eq. (7.95), gives the differential cross section for electrostatic scattering,

$$\frac{d\sigma}{d\Omega} = \frac{k^2 q_1^2 q_2^2}{16E^2 \sin^4(\phi/2)}. \quad (7.97)$$

This is the Rutherford-scattering differential-cross-section formula. Around 1910, Rutherford and his students bombarded metal foils with alpha particles. Their results for the distribution of scattering angles were consistent with the above formula. In particular, they observed backward scattering of the alpha particles. Since the above formula is based on the assumption of a point source for the potential, this led Rutherford to his theory that atoms contained a dense positively charged nucleus, as opposed to being made of a spread-out “plum pudding” distribution of charge, which (as a special case of not yielding the correct distribution of scattering angles in general) doesn’t yield backward scattering. ♣

<sup>14</sup> Remember, all we care about is the angle here. So when you’re picturing the large sphere of radius  $R$  centered at  $M$ , don’t say, “If  $b$  is large (for example,  $R/2$ ), then a straight-line trajectory will hit the sphere at a large angle up above the  $x$  axis (for example,  $30^\circ$ ).” This is incorrect. If you want to think in terms of a physical sphere of radius  $R$ , it is understood that  $R$  is infinitely large. Or more precisely,  $R \gg b$ , for any impact parameter  $b$  you might choose. So even if  $b$  is “large,” it is still small compared with  $R$ , so a straight-line trajectory will hit the sphere of radius  $R$  at an angle that is essentially zero. Alternatively, you can just think in terms of angles, and not visualize an actual large sphere centered at  $M$ .