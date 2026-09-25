# Chapter 6 The Lagrangian method

In this chapter, we're going to learn about a whole new way of looking at things. Consider the system of a mass on the end of a spring. We can analyze this, of course, by using  $F = ma$  to write down  $m\ddot{x} = -kx$ . The solutions to this equation are sinusoidal functions, as we well know. We can, however, figure things out by using another method which doesn't explicitly use  $F = ma$ . In many (in fact, probably most) physical situations, this new method is far superior to using  $F = ma$ . You will soon discover this for yourself when you tackle the problems and exercises for this chapter. We will present our new method by first stating its rules (without any justification) and showing that they somehow end up magically giving the correct answer. We will then give the method proper justification.

### 6.1 The Euler–Lagrange equations

Here is the procedure. Consider the following seemingly silly combination of the kinetic and potential energies ( $T$  and  $V$ , respectively),

$$L \equiv T - V. \quad (6.1)$$

This is called the *Lagrangian*. Yes, there is a minus sign in the definition (a plus sign would simply give the total energy). In the problem of a mass on the end of a spring,  $T = m\dot{x}^2/2$  and  $V = kx^2/2$ , so we have

$$L = \frac{1}{2}m\dot{x}^2 - \frac{1}{2}kx^2. \quad (6.2)$$

Now write

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}} \right) = \frac{\partial L}{\partial x}. \quad (6.3)$$

Don't worry, we'll show you in Section 6.2 where this comes from. This equation is called the *Euler–Lagrange (E–L) equation*. For the problem at hand, we have  $\partial L / \partial \dot{x} = m\dot{x}$  and  $\partial L / \partial x = -kx$  (see Appendix B for the definition of a partial derivative), so Eq. (6.3) gives

$$m\ddot{x} = -kx, \quad (6.4)$$

which is exactly the result obtained by using  $F = ma$ . An equation such as Eq. (6.4), which is derived from the Euler–Lagrange equation, is called an *equation of motion*.<sup>1</sup> If the problem involves more than one coordinate, as most problems do, we just have to apply Eq. (6.3) to each coordinate. We will obtain as many equations as there are coordinates. Each equation may very well involve many of the coordinates (see the example below, where both equations involve both  $x$  and  $\theta$ ).

At this point, you may be thinking, “That was a nice little trick, but we just got lucky in the spring problem. The procedure won’t work in a more general situation.” Well, let’s see. How about if we consider the more general problem of a particle moving in an arbitrary potential  $V(x)$  (we’ll stick to one dimension for now). The Lagrangian is then

$$L = \frac{1}{2}m\dot{x}^2 - V(x), \quad (6.5)$$

and the Euler–Lagrange equation, Eq. (6.3), gives

$$m\ddot{x} = -\frac{dV}{dx}. \quad (6.6)$$

But  $-dV/dx$  is the force on the particle. So we see that Eqs. (6.1) and (6.3) together say exactly the same thing that  $F = ma$  says, when using a Cartesian coordinate in one dimension (but this result is in fact quite general, as we’ll see in Section 6.4). Note that shifting the potential by a given constant has no effect on the equation of motion, because Eq. (6.3) involves only the derivative of  $V$ . This is equivalent to saying that only differences in energy are relevant, and not the actual values, as we well know.

In a three-dimensional setup written in terms of Cartesian coordinates, the potential takes the form  $V(x, y, z)$ , so the Lagrangian is

$$L = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - V(x, y, z). \quad (6.7)$$

It then immediately follows that the three Euler–Lagrange equations (obtained by applying Eq. (6.3) to  $x$ ,  $y$ , and  $z$ ) may be combined into the vector statement,

$$m\ddot{\mathbf{x}} = -\nabla V. \quad (6.8)$$

But  $-\nabla V = \mathbf{F}$ , so we again arrive at Newton’s second law,  $\mathbf{F} = m\mathbf{a}$ , now in three dimensions.

Let’s do one more example to convince you that there’s really something nontrivial going on here.

<sup>1</sup> The term “equation of motion” is a little ambiguous. It is understood to refer to the second-order differential equation satisfied by  $x$ , and not the actual equation for  $x$  as a function of  $t$ , namely  $x(t) = A \cos(\omega t + \phi)$  in this problem, which is obtained by integrating the equation of motion twice.

![Diagram of a spring pendulum. A spring is suspended from a fixed horizontal ceiling. The spring is at an angle theta from the vertical dashed line. The total length of the spring is l+x. A mass m is attached to the end of the spring.](f7bac54e777c1fa438e9cc353dde7bef_img.jpg)

Diagram of a spring pendulum. A spring is suspended from a fixed horizontal ceiling. The spring is at an angle theta from the vertical dashed line. The total length of the spring is l+x. A mass m is attached to the end of the spring.

Fig. 6.1

**Example (Spring pendulum):** Consider a pendulum made of a spring with a mass  $m$  on the end (see Fig. 6.1). The spring is arranged to lie in a straight line (which we can arrange by, say, wrapping the spring around a rigid massless rod). The equilibrium length of the spring is  $\ell$ . Let the spring have length  $\ell + x(t)$ , and let its angle with the vertical be  $\theta(t)$ . Assuming that the motion takes place in a vertical plane, find the equations of motion for  $x$  and  $\theta$ .

**Solution:** The kinetic energy may be broken up into the radial and tangential parts, so we have

$$T = \frac{1}{2}m(\dot{x}^2 + (\ell + x)^2\dot{\theta}^2). \quad (6.9)$$

The potential energy comes from both gravity and the spring, so we have

$$V(x, \theta) = -mg(\ell + x) \cos \theta + \frac{1}{2}kx^2. \quad (6.10)$$

The Lagrangian is therefore

$$L \equiv T - V = \frac{1}{2}m(\dot{x}^2 + (\ell + x)^2\dot{\theta}^2) + mg(\ell + x) \cos \theta - \frac{1}{2}kx^2. \quad (6.11)$$

There are two variables here,  $x$  and  $\theta$ . As mentioned above, the nice thing about the Lagrangian method is that we can just use Eq. (6.3) twice, once with  $x$  and once with  $\theta$ . So the two Euler–Lagrange equations are

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}}\right) = \frac{\partial L}{\partial x} \implies m\ddot{x} = m(\ell + x)\dot{\theta}^2 + mg \cos \theta - kx, \quad (6.12)$$

and

$$\begin{aligned} \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}}\right) &= \frac{\partial L}{\partial \theta} \implies \frac{d}{dt}(m(\ell + x)^2\dot{\theta}) = -mg(\ell + x) \sin \theta \\ \implies m(\ell + x)^2\ddot{\theta} + 2m(\ell + x)\dot{x}\dot{\theta} &= -mg(\ell + x) \sin \theta \\ \implies m(\ell + x)\ddot{\theta} + 2m\dot{x}\dot{\theta} &= -mg \sin \theta. \end{aligned} \quad (6.13)$$

Equation (6.12) is simply the radial  $F = ma$  equation, complete with the centripetal acceleration,  $-(\ell + x)\dot{\theta}^2$ . And the first line of Eq. (6.13) is the statement that the torque equals the rate of change of the angular momentum (this is one of the subjects of Chapter 8). Alternatively, if you want to work in a rotating reference frame, then Eq. (6.12) is the radial  $F = ma$  equation, complete with the centrifugal force,  $m(\ell + x)\dot{\theta}^2$ . And the third line of Eq. (6.13) is the tangential  $F = ma$  equation, complete with the Coriolis force,  $-2m\dot{x}\dot{\theta}$ . But never mind about this now. We'll deal with rotating frames in Chapter 10.<sup>2</sup>

<sup>2</sup> Throughout this chapter, I'll occasionally point out torques, angular momenta, centrifugal forces, and other such things when they pop up in equations of motion, even though we haven't covered

REMARK: After writing down the E–L equations, it is always best to double-check them by trying to identify them as  $F = ma$  and/or  $\tau = dL/dt$  equations (once we learn about that). Sometimes, however, this identification isn’t obvious. And for the times when everything is clear (that is, when you look at the E–L equations and say, “Oh, of course!”), it is usually clear only *after* you’ve derived the equations. In general, the safest method for solving a problem is to use the Lagrangian method and then double-check things with  $F = ma$  and/or  $\tau = dL/dt$  if you can. ♣

At this point it seems to be personal preference, and all academic, whether you use the Lagrangian method or the  $F = ma$  method. The two methods produce the same equations. However, in problems involving more than one variable, it usually turns out to be *much* easier to write down  $T$  and  $V$ , as opposed to writing down all the forces. This is because  $T$  and  $V$  are nice and simple scalars. The forces, on the other hand, are vectors, and it is easy to get confused if they point in various directions. The Lagrangian method has the advantage that once you’ve written down  $L \equiv T - V$ , you don’t have to think anymore. All you have to do is blindly take some derivatives.<sup>3</sup>

When jumping from high in a tree,  
 Just write down del  $L$  by del  $z$ .  
 Take del  $L$  by  $z$  dot,  
 Then  $t$ -dot what you’ve got,  
 And equate the results (but quickly!)

But ease of computation aside, is there any fundamental difference between the two methods? Is there any deep reasoning behind Eq. (6.3)? Indeed, there is ...

### 6.2 The principle of stationary action

Consider the quantity,

$$S \equiv \int_{t_1}^{t_2} L(x, \dot{x}, t) dt. \quad (6.14)$$

$S$  is called the *action*. It is a quantity with the dimensions of (Energy)  $\times$  (Time).  $S$  depends on  $L$ , and  $L$  in turn depends on the function  $x(t)$  via Eq. (6.1).<sup>4</sup> Given any

them yet. I figure it can’t hurt to bring your attention to them. But rest assured, a familiarity with these topics is by no means necessary for an understanding of what we’ll be doing in this chapter, so just ignore the references if you want. One of the great things about the Lagrangian method is that even if you’ve never heard of the terms “torque,” “centrifugal,” “Coriolis,” or even “ $F = ma$ ” itself, you can still get the correct equations by simply writing down the kinetic and potential energies, and then taking a few derivatives.

<sup>3</sup> Well, you eventually have to *solve* the resulting equations of motion, but you have to do that with the  $F = ma$  method, too.

<sup>4</sup> In some situations, the kinetic and potential energies in  $L \equiv T - V$  may explicitly depend on time, so we have included the “ $t$ ” in Eq. (6.14).

function  $x(t)$ , we can produce the quantity  $S$ . We'll deal with only one coordinate,  $x$ , for now.

Integrals like the one in Eq. (6.14) are called *functionals*, and  $S$  is sometimes denoted by  $S[x(t)]$ . It depends on the entire function  $x(t)$ , and not on just one input number, as a regular function  $f(t)$  does.  $S$  can be thought of as a function of an infinite number of values, namely all the  $x(t)$  for  $t$  ranging from  $t_1$  to  $t_2$ . If you don't like infinities, you can imagine breaking up the time interval into, say, a million pieces, and then replacing the integral by a discrete sum.

Let's now pose the following question: Consider a function  $x(t)$ , for  $t_1 \leq t \leq t_2$ , which has its endpoints fixed (that is,  $x(t_1) = x_1$  and  $x(t_2) = x_2$ , where  $x_1$  and  $x_2$  are given), but is otherwise arbitrary. What function  $x(t)$  yields a stationary value of  $S$ ? A stationary value is a local minimum, maximum, or saddle point.<sup>5</sup>

For example, consider a ball dropped from rest, and consider the function  $y(t)$  for  $0 \leq t \leq 1$ . Assume that we somehow know that  $y(0) = 0$  and  $y(1) = -g/2$ .<sup>6</sup> A number of possibilities for  $y(t)$  are shown in Fig. 6.2, and each of these can (in theory) be plugged into Eqs. (6.1) and (6.14) to generate  $S$ . Which one yields a stationary value of  $S$ ? The following theorem gives us the answer.

![Figure 6.2: A graph showing several possible trajectories y(t) for a ball dropped from rest. The horizontal axis is time t, ranging from 0 to 1. The vertical axis is position y, ranging from 0 down to -g/2. All trajectories start at (0, 0) and end at (1, -g/2). The trajectories are smooth curves that represent different possible paths the ball could take, though only one is the actual physical path.](1fcdf404a9b94a0247dcb98023afec34_img.jpg)

Figure 6.2: A graph showing several possible trajectories y(t) for a ball dropped from rest. The horizontal axis is time t, ranging from 0 to 1. The vertical axis is position y, ranging from 0 down to -g/2. All trajectories start at (0, 0) and end at (1, -g/2). The trajectories are smooth curves that represent different possible paths the ball could take, though only one is the actual physical path.

Fig. 6.2

**Theorem 6.1** *If the function  $x_0(t)$  yields a stationary value (that is, a local minimum, maximum, or saddle point) of  $S$ , then*

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}_0} \right) = \frac{\partial L}{\partial x_0}. \quad (6.15)$$

*It is understood that we are considering the class of functions whose endpoints are fixed. That is,  $x(t_1) = x_1$  and  $x(t_2) = x_2$ .*

**Proof:** We will use the fact that if a certain function  $x_0(t)$  yields a stationary value of  $S$ , then any other function very close to  $x_0(t)$  (with the same endpoint values) yields essentially the same  $S$ , up to first order in any deviations. This is actually the definition of a stationary value. The analogy with regular functions is that if  $f(b)$  is a stationary value of  $f$ , then  $f(b + \epsilon)$  differs from  $f(b)$  only at second order in the small quantity  $\epsilon$ . This is true because  $f'(b) = 0$ , so there is no first-order term in the Taylor series expansion around  $b$ .

Assume that the function  $x_0(t)$  yields a stationary value of  $S$ , and consider the function

$$x_a(t) \equiv x_0(t) + a\beta(t), \quad (6.16)$$

<sup>5</sup> A saddle point is a point where there are no first-order changes in  $S$ , and where some of the second-order changes are positive and some are negative (like the middle of a saddle, of course).

<sup>6</sup> This follows from  $y = -gt^2/2$ , but pretend that we don't know this formula.

where  $a$  is a number, and where  $\beta(t)$  satisfies  $\beta(t_1) = \beta(t_2) = 0$  (to keep the endpoints of the function fixed), but is otherwise arbitrary. When producing the action  $S[x_a(t)]$  in (6.14), the  $t$  is integrated out, so  $S$  is just a number. It depends on  $a$ , in addition to  $t_1$  and  $t_2$ . Our requirement is that there be no change in  $S$  at first order in  $a$ . How does  $S$  depend on  $a$ ? Using the chain rule, we have

$$\begin{aligned}\frac{\partial}{\partial a}S[x_a(t)] &= \frac{\partial}{\partial a} \int_{t_1}^{t_2} L dt = \int_{t_1}^{t_2} \frac{\partial L}{\partial a} dt \\ &= \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial x_a} \frac{\partial x_a}{\partial a} + \frac{\partial L}{\partial \dot{x}_a} \frac{\partial \dot{x}_a}{\partial a} \right) dt.\end{aligned}\quad (6.17)$$

In other words,  $a$  influences  $S$  through its effect on  $x$ , and also through its effect on  $\dot{x}$ . From Eq. (6.16), we have

$$\frac{\partial x_a}{\partial a} = \beta, \quad \text{and} \quad \frac{\partial \dot{x}_a}{\partial a} = \dot{\beta}, \quad (6.18)$$

so Eq. (6.17) becomes<sup>7</sup>

$$\frac{\partial}{\partial a}S[x_a(t)] = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial x_a} \beta + \frac{\partial L}{\partial \dot{x}_a} \dot{\beta} \right) dt. \quad (6.19)$$

Now comes the one sneaky part of the proof. We will integrate the second term by parts (you will see this trick many times in your physics career). Using

$$\int \frac{\partial L}{\partial \dot{x}_a} \dot{\beta} dt = \frac{\partial L}{\partial \dot{x}_a} \beta - \int \left( \frac{d}{dt} \frac{\partial L}{\partial \dot{x}_a} \right) \beta dt, \quad (6.20)$$

Eq. (6.19) becomes

$$\frac{\partial}{\partial a}S[x_a(t)] = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial x_a} - \frac{d}{dt} \frac{\partial L}{\partial \dot{x}_a} \right) \beta dt + \left. \frac{\partial L}{\partial \dot{x}_a} \beta \right|_{t_1}^{t_2}. \quad (6.21)$$

But  $\beta(t_1) = \beta(t_2) = 0$ , so the last term (the “boundary term”) vanishes. We now use the fact that  $(\partial/\partial a)S[x_a(t)]$  must be zero for *any* function  $\beta(t)$ , because we are assuming that  $x_0(t)$  yields a stationary value. The only way this can be true is if the quantity in parentheses above (evaluated at  $a = 0$ ) is identically equal to zero, that is,

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}_0} \right) = \frac{\partial L}{\partial x_0}. \quad \blacksquare \quad (6.22)$$

<sup>7</sup> Note that nowhere do we assume that  $x_a$  and  $\dot{x}_a$  are independent variables. The partial derivatives in Eq. (6.18) are very much related, in that one is the derivative of the other. The use of the chain rule in Eq. (6.17) is still perfectly valid.

The E–L equation, Eq. (6.3), therefore doesn’t just come out of the blue. It is a consequence of requiring that the action be at a stationary value. We may therefore replace  $F = ma$  by the following principle.

#### - **The principle of stationary action:**

*The path of a particle is the one that yields a stationary value of the action.*

This principle (also known as Hamilton’s principle) is equivalent to  $F = ma$  because the above theorem shows that if (and only if, as you can show by working backwards) we have a stationary value of  $S$ , then the E–L equations hold. And the E–L equations are equivalent to  $F = ma$  (as we showed for Cartesian coordinates in Section 6.1, and as we’ll prove for any coordinate system in Section 6.4). Therefore, “stationary action” is equivalent to  $F = ma$ .

If we have a multidimensional setup where the Lagrangian is a function of the variables  $x_1(t), x_2(t), \dots$ , then the above principle of stationary action is still all we need. With more than one variable, we can now vary the path by varying each coordinate (or combinations thereof). The variation of each coordinate produces an E–L equation which, as we saw in the Cartesian case, is equivalent to an  $F = ma$  equation.

Given a classical mechanics problem, we can solve it with  $F = ma$ , or we can solve it with the E–L equations, which are a consequence of the principle of stationary action (often called the principle of “least action” or “minimal action,” but see the fourth remark below). Either method will get the job done. But as mentioned at the end of Section 6.1, it is often easier to use the latter, because it avoids the use of force which can get confusing if you have forces pointing in all sorts of complicated directions.

It just stood there and did nothing, of course,  
A harmless and still wooden horse.  
But the minimal action  
Was just a distraction;  
The plan involved no use of force.

Let’s now return to the example of a ball dropped from rest, mentioned above. The Lagrangian is  $L = T - V = m\dot{y}^2/2 - mgy$ , so Eq. (6.22) gives  $\ddot{y} = -g$ , which is simply the  $F = ma$  equation (divided through by  $m$ ), as expected. The solution is  $y(t) = -gt^2/2 + v_0t + y_0$ , as we well know. But the initial conditions tell us that  $v_0 = y_0 = 0$ , so our solution is  $y(t) = -gt^2/2$ . You are encouraged to verify explicitly that this  $y(t)$  yields an action that is stationary with respect to variations of the form, say,  $y(t) = -gt^2/2 + \epsilon t(t - 1)$ , which also satisfies the endpoint conditions (this is the task of Exercise 6.30). There is, of course, an infinite number of other ways to vary  $y(t)$ , but this specific result should help convince you of the validity of Theorem 6.1.

Note that the stationarity implied by the Euler–Lagrange equation, Eq. (6.22), is a *local* statement. It gives information only about nearby paths. It says nothing

about the *global* nature of how the action depends on all possible paths. If we find that a solution to Eq. (6.22) happens to produce a local minimum (as opposed to a maximum or a saddle), there is no reason to conclude that it is a global minimum, although in many cases it turns out to be (see Exercise 6.32, for the case of a thrown ball).

#### REMARKS:

1. Theorem 6.1 is based on the assumption that the ending time,  $t_2$ , of the motion is given. But how do we know this final time? Well, we don't. In the example of a ball thrown upward, the total time to rise and fall back to your hand can be anything, depending on the ball's initial speed. This initial speed will show up as an integration constant when solving the E–L equations. The motion must end sometime, and the principle of stationary action says that for whatever time this happens to be, the physical path has a stationary action.
2. Theorem 6.1 shows that we can explain the E–L equations by the principle of stationary action. This, however, simply shifts the burden of proof. We are now left with the task of justifying why we should want the action to have a stationary value. The good news is that there is a very solid reason for this. The bad news is that the reason involves quantum mechanics, so we won't be able to discuss it properly here. Suffice it to say that a particle actually takes all possible paths in going from one place to another, and each path is associated with the complex number  $e^{iS/\hbar}$  (where  $\hbar = 1.05 \cdot 10^{-34}$  J s is *Planck's constant*). These complex numbers have absolute value 1 and are called “phases.” It turns out that the phases from all possible paths must be added up to give the “amplitude” of going from one point to another. The absolute value of the amplitude must then be squared to obtain the probability.<sup>8</sup>  
The basic point, then, is that at a nonstationary value of  $S$ , the phases from different paths differ (greatly, because  $\hbar$  is so small compared with the typical size of the action for a macroscopic particle) from one another, which effectively leads to the addition of many random vectors in the complex plane. These end up canceling each other, yielding a sum of essentially zero. There is therefore no contribution to the overall amplitude from non-stationary values of  $S$ . Hence, we do not observe the paths associated with these  $S$ 's. At a stationary value of  $S$ , however, all the phases take on essentially the same value, thereby adding constructively instead of destructively. There is therefore a nonzero probability for the particle to take a path that yields a stationary value of  $S$ . So this is the path we observe.
3. But again, the preceding remark simply shifts the burden of proof one step further. We must now justify why these phases  $e^{iS/\hbar}$  should exist, and why the Lagrangian that appears in  $S$  should equal  $T - V$ . But here's where we're going to stop.
4. The principle of stationary action is sometimes referred to as the principle of “least” action, but this is misleading. True, it is often the case that the stationary value turns out to be a minimum value, but it need not be, as we can see in the following example. Consider a harmonic oscillator which has a Lagrangian equal to

$$L = \frac{1}{2}m\dot{x}^2 - \frac{1}{2}kx^2. \quad (6.23)$$

Let  $x_0(t)$  be a function that yields a stationary value of the action. Then we know that  $x_0(t)$  satisfies the E–L equation,  $m\ddot{x}_0 = -kx_0$ . Consider a slight variation on this path,

<sup>8</sup> This is one of those remarks that is completely useless, because it is incomprehensible to those who haven't seen the topic before, and trivial to those who have. My apologies. But this and the following remarks are definitely not necessary for an understanding of the material in this chapter. If you're interested in reading more about these quantum mechanical issues, you should take a look at Richard Feynman's book (Feynman, 2006). Feynman was, after all, the one who thought of this idea.

$x_0(t) + \xi(t)$ , where  $\xi(t)$  satisfies  $\xi(t_1) = \xi(t_2) = 0$ . With this new function, the action becomes

$$S_\xi = \int_{t_1}^{t_2} \left( \frac{m}{2} (\dot{x}_0^2 + 2\dot{x}_0\dot{\xi} + \dot{\xi}^2) - \frac{k}{2} (x_0^2 + 2x_0\xi + \xi^2) \right) dt. \quad (6.24)$$

The two cross-terms add up to zero, because after integrating the  $\dot{x}_0\dot{\xi}$  term by parts, their sum is

$$m\dot{x}_0\xi \Big|_{t_1}^{t_2} - \int_{t_1}^{t_2} (m\ddot{x}_0 + kx_0)\xi \, dt. \quad (6.25)$$

The first term is zero, due to the boundary conditions on  $\xi(t)$ . The second term is zero, due to the E–L equation. We’ve basically just reproduced the proof of Theorem 6.1 for the special case of the harmonic oscillator here.

The terms in Eq. (6.24) involving only  $x_0$  give the stationary value of the action (call it  $S_0$ ). To determine whether  $S_0$  is a minimum, maximum, or saddle point, we must look at the difference,

$$\Delta S \equiv S_\xi - S_0 = \frac{1}{2} \int_{t_1}^{t_2} (m\dot{\xi}^2 - k\xi^2) \, dt. \quad (6.26)$$

It is always possible to find a function  $\xi$  that makes  $\Delta S$  positive. Simply choose  $\xi$  to be small, but make it wiggle very fast, so that  $\dot{\xi}$  is large. Therefore, it is *never* the case that  $S_0$  is a maximum. Note that this reasoning works for any potential, not just a harmonic oscillator, as long as it is a function of position only (that is, it contains no derivatives, as we always assume).

You might be tempted to use the same line of reasoning to say that it is also always possible to find a function  $\xi$  that makes  $\Delta S$  negative, by making  $\xi$  large and  $\dot{\xi}$  small. If this were true, then we could put everything together and conclude that all stationary points are saddle points, for a harmonic oscillator. However, it is *not* always possible to make  $\xi$  large enough and  $\dot{\xi}$  small enough so that  $\Delta S$  is negative, due to the boundary conditions  $\xi(t_1) = \xi(t_2) = 0$ . If  $\xi$  changes from zero to a large value and then back to zero, then  $\dot{\xi}$  may also have to be large, if the time interval is short enough. Problem 6.6 deals quantitatively with this issue. For now, let’s just recognize that in some cases  $S_0$  is a minimum, in some cases it is a saddle point, and it is never a maximum. “Least action” is therefore a misnomer.

5. It is sometimes said that nature has a “purpose,” in that it seeks to take the path that produces the minimum action. In view of the second remark above, this is incorrect. In fact, nature does exactly the opposite. It takes *every* path, treating them all on equal footing. We end up seeing only the path with a stationary action, due to the way the quantum mechanical phases add. It would be a harsh requirement, indeed, to demand that nature make a “global” decision (that is, compare paths that are separated by large distances) and choose the one with the smallest action. Instead, we see that everything takes place on a “local” scale. Nearby phases simply add, and everything works out automatically.

When an archer shoots an arrow through the air, the aim is made possible by all the other arrows taking all the other nearby paths, each with essentially the same action. Likewise, when you walk down the street with a certain destination in mind, you’re not alone . . .

When walking, I know that my aim  
Is caused by the ghosts with my name.  
And although I can’t see  
Where they walk next to me,  
I know they’re all there, just the same.

6. Consider a function,  $f(x)$ , of one variable (for ease of terminology). Let  $f(b)$  be a local minimum of  $f$ . There are two basic properties of this minimum. The first is that  $f(b)$  is smaller than all nearby values. The second is that the slope of  $f$  is zero at  $b$ . From the above remarks, we see that (as far as the action  $S$  is concerned) the first property is completely irrelevant, and the second one is the whole point. In other words, saddle points (and maxima, although we showed above that these never exist for  $S$ ) are just as good as minima, as far as the constructive addition of the  $e^{iS/\hbar}$  phases is concerned.
7. Given that classical mechanics is an approximate theory, while quantum mechanics is the (more) correct one, it is quite silly to justify the principle of stationary action by demonstrating its equivalence to  $F = ma$ , as we did above. We should be doing it the other way around. However, because our intuition is based on  $F = ma$ , it's easier to start with  $F = ma$  as the given fact, rather than calling upon the latent quantum-mechanical intuition hidden deep within all of us. Maybe someday ...

At any rate, in more advanced theories dealing with fundamental issues concerning the tiny building blocks of matter (where actions are of the same order of magnitude as  $\hbar$ ), the approximate  $F = ma$  theory is invalid, and you *have* to use the Lagrangian method.

8. When dealing with a system in which a nonconservative force such as friction is present, the Lagrangian method loses much of its appeal. The reason for this is that nonconservative forces don't have a potential energy associated with them, so there isn't a specific  $V(x)$  that you can write down in the Lagrangian. Although friction forces can in fact be incorporated in the Lagrangian method, you have to include them in the E–L equations essentially by hand. We won't deal with nonconservative forces in this chapter. ♣

### 6.3 Forces of constraint

A nice thing about the Lagrangian method is that we are free to impose any given constraints at the beginning of the problem, thereby immediately reducing the number of variables. This is always done (perhaps without thinking) whenever a particle is constrained to move on a wire or surface, etc. Often we are concerned not with the exact nature of the forces doing the constraining, but only with the resulting motion, given that the constraints hold. By imposing the constraints at the outset, we can find the motion, but we can't say anything about the constraining forces.

If we want to determine the constraining forces, we must take a different approach. The main idea of the strategy, as we will show below, is that we must not impose the constraints too soon. This leaves us with a larger number of variables to deal with, so the calculations are more cumbersome. But the benefit is that we are able to find the constraining forces.

Consider the setup of a particle sliding off a fixed frictionless hemisphere of radius  $R$  (see Fig. 6.3). Let's say that we are concerned only with finding the equation of motion for  $\theta$ , and not the constraining force. Then we can write everything in terms of  $\theta$ , because we know that the radial distance  $r$  is constrained to be  $R$ . The kinetic energy is  $mR^2\dot{\theta}^2/2$ , and the potential energy (relative to the bottom of the hemisphere) is  $mgR \cos \theta$ , so the Lagrangian is

$$L = \frac{1}{2}mR^2\dot{\theta}^2 - mgR \cos \theta, \quad (6.27)$$

![Diagram of a particle sliding off a fixed frictionless hemisphere of radius R. The hemisphere is on a horizontal surface. A particle is shown at a position on the hemisphere's surface, defined by an angle theta from the vertical dashed line. A curved arrow indicates the particle's motion along the surface.](0eab77f088d4d8bd753fe2de427d35e6_img.jpg)

Diagram of a particle sliding off a fixed frictionless hemisphere of radius R. The hemisphere is on a horizontal surface. A particle is shown at a position on the hemisphere's surface, defined by an angle theta from the vertical dashed line. A curved arrow indicates the particle's motion along the surface.

Fig. 6.3

and the equation of motion, via Eq. (6.3), is

$$\ddot{\theta} = (g/R) \sin \theta, \quad (6.28)$$

which is equivalent to the tangential  $F = ma$  statement.

Now let's say that we want to find the constraining normal force that the hemisphere applies to the particle. To do this, let's solve the problem in a different way and write things in terms of both  $r$  and  $\theta$ . Also (and here's the critical step), let's be really picky and say that  $r$  isn't *exactly* constrained to be  $R$ , because in the real world the particle actually sinks into the hemisphere a little bit. This may seem a bit silly, but it's really the whole point. The particle pushes and sinks inward a tiny distance until the hemisphere gets squashed enough to push back with the appropriate force to keep the particle from sinking in any more (just consider the hemisphere to be made of lots of little springs with very large spring constants). The particle is therefore subject to a (very steep) potential arising from the hemisphere's force. The constraining potential,  $V(r)$ , looks something like the plot in Fig. 6.4. The true Lagrangian for the system is thus

![Figure 6.4: A graph of the constraining potential V(r) versus radial distance r. The vertical axis is labeled V(r) and the horizontal axis is labeled r. The potential is zero for r >= R and rises very steeply to infinity as r approaches R from the right, representing a hard constraint.](a44b2247c723fd33ab800e091a171ca2_img.jpg)

Figure 6.4: A graph of the constraining potential V(r) versus radial distance r. The vertical axis is labeled V(r) and the horizontal axis is labeled r. The potential is zero for r >= R and rises very steeply to infinity as r approaches R from the right, representing a hard constraint.

Fig. 6.4

$$L = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2) - mgr \cos \theta - V(r). \quad (6.29)$$

(The  $\dot{r}^2$  term in the kinetic energy will turn out to be insignificant.) The equations of motion obtained from varying  $\theta$  and  $r$  are therefore

$$\begin{aligned} mr^2\ddot{\theta} + 2mr\dot{r}\dot{\theta} &= mgr \sin \theta, \\ m\ddot{r} &= mr\dot{\theta}^2 - mg \cos \theta - V'(r). \end{aligned} \quad (6.30)$$

Having written down the equations of motion, we will *now* apply the constraint condition that  $r = R$ . This condition implies  $\dot{r} = \ddot{r} = 0$ . (Of course,  $r$  isn't *really* equal to  $R$ , but any differences are inconsequential from this point onward.) The first of Eqs. (6.30) then reproduces Eq. (6.28), while the second yields

$$-\left. \frac{dV}{dr} \right|_{r=R} = mg \cos \theta - mR\dot{\theta}^2. \quad (6.31)$$

But  $F_N \equiv -dV/dr$  is the constraint force applied in the  $r$  direction, which is precisely the force we are looking for. The normal force of constraint is therefore

$$F_N(\theta, \dot{\theta}) = mg \cos \theta - mR\dot{\theta}^2. \quad (6.32)$$

This is equivalent to the radial  $F = ma$  equation,  $mg \cos \theta - F_N = mR\dot{\theta}^2$  (which is certainly a quicker way to find the normal force in the present problem). Note that this result is valid only if  $F_N(\theta, \dot{\theta}) > 0$ . If the normal force becomes zero, then this means that the particle has left the sphere, in which case  $r$  no longer equals  $R$ .

#### REMARKS:

1. What if we instead had (unwisely) chosen Cartesian coordinates,  $x$  and  $y$ , instead of polar coordinates,  $r$  and  $\theta$ ? Since the distance from the particle to the surface of the hemisphere is  $\eta \equiv \sqrt{x^2 + y^2} - R$ , we obtain a true Lagrangian equal to

$$L = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2) - mgy - V(\eta). \quad (6.33)$$

The equations of motion are (using the chain rule)

$$m\ddot{x} = -\frac{dV}{d\eta} \frac{\partial \eta}{\partial x}, \quad \text{and} \quad m\ddot{y} = -mg - \frac{dV}{d\eta} \frac{\partial \eta}{\partial y}. \quad (6.34)$$

We now apply the constraint condition  $\eta = 0$ . Since  $-dV/d\eta$  equals the constraint force  $F$ , you can show that the equations we end up with (namely, the two E–L equations and the constraint equation) are

$$m\ddot{x} = F \frac{x}{R}, \quad m\ddot{y} = -mg + F \frac{y}{R}, \quad \text{and} \quad \sqrt{x^2 + y^2} - R = 0. \quad (6.35)$$

These three equations are sufficient to determine the three unknowns  $\ddot{x}$ ,  $\ddot{y}$ , and  $F$  as functions of the quantities  $x$ ,  $\dot{x}$ ,  $y$ , and  $\dot{y}$ . See Exercise 6.37, which should convince you that polar coordinates are the way to go. In general, the strategy for solving for  $F$  is to take two time derivatives of the constraint equation and then eliminate the second derivatives of the coordinates by using the E–L equations (this process was trivial in the polar-coordinate case).

2. You can see from Eq. (6.35) that the E–L equations end up taking the form,

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) = \frac{\partial L}{\partial q_i} + F \frac{\partial \eta}{\partial q_i}, \quad (6.36)$$

for each coordinate  $q_i$ . The quantity  $\eta$  is what appears in the constraint equation,  $\eta = 0$ . In our hemisphere problem, we had  $\eta = r - R$  in polar coordinates, and  $\eta = \sqrt{x^2 + y^2} - R$  in Cartesian coordinates. The E–L equations, combined with the  $\eta = 0$  condition, give us exactly the number of equations ( $N + 1$  of them, where  $N$  is the number of coordinates) needed to determine all of the  $N + 1$  unknowns (all the  $\ddot{q}_i$ , and  $F$ ) in terms of the  $q_i$  and  $\dot{q}_i$ .

Writing down the equations in Eq. (6.36) is basically the method of Lagrange multipliers, where the Lagrange multiplier turns out to be the force. But if you're not familiar with this method, no need to worry; you can derive everything from scratch using the above technique involving the steep potential. If you do happen to be familiar with it, then there might in fact be a need to worry about how you apply it, as the following remark explains.

3. When trying to determine the forces of constraint, you can just start with Eq. (6.36), without bothering to write down  $V(\eta)$ . But you must be careful to make sure that  $\eta$  does indeed represent the distance the particle is from where it should be. In polar coordinates, if someone gives you the constraint condition for the hemisphere as  $7(r - R) = 0$ , and if you use the left-hand side of this as the  $\eta$  in Eq. (6.36), then you will get the wrong constraint force; it will be too small by a factor of 7. Likewise, in Cartesian coordinates, writing the constraint as  $y - \sqrt{R^2 - x^2} = 0$  will give you the wrong force. The best way to avoid this problem is, of course, to pick one of your variables as the distance the particle is from where it should be (up to an additive constant, as in the case of  $r - R = 0$ ). ♣

### 6.4 Change of coordinates

When  $L$  is written in terms of Cartesian coordinates  $x, y, z$ , we showed in Section 6.1 that the Euler–Lagrange equations are equivalent to Newton's  $\mathbf{F} = m\mathbf{a}$

equations; see Eq. (6.8). But what about the case where we use polar, spherical, or some other coordinates? The equivalence of the E–L equations and  $\mathbf{F} = m\mathbf{a}$  isn't so obvious. As far as trusting the E–L equations for such coordinates goes, you can achieve peace of mind in two ways. You can accept the principle of stationary action as something so beautiful and profound that it simply has to work for any choice of coordinates. Or, you can take the more mundane road and show through a change of coordinates that if the E–L equations hold for one set of coordinates (and we know that they *do* hold for at least one set, namely Cartesian coordinates), then they also hold for any other coordinates (of a certain form, described below). In this section, we will demonstrate the validity of the E–L equations through the explicit change of coordinates.<sup>9</sup>

Consider the set of coordinates,

$$x_i : (x_1, x_2, \dots, x_N). \quad (6.37)$$

For example, if  $N = 6$ , then  $x_1, x_2, x_3$  could be the Cartesian  $x, y, z$  coordinates of one particle, and  $x_4, x_5, x_6$  could be the  $r, \theta, \phi$  polar coordinates of a second particle, and so on. Assume that the E–L equations hold for these variables, that is,

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}_i} \right) = \frac{\partial L}{\partial x_i} \quad (1 \leq i \leq N). \quad (6.38)$$

Consider a new set of variables that are functions of the  $x_i$  and  $t$ ,

$$q_i = q_i(x_1, x_2, \dots, x_N; t). \quad (6.39)$$

We will restrict ourselves to the case where the  $q_i$  do not depend on the  $\dot{x}_i$ . (This is quite reasonable. If the coordinates depended on the velocities, then we wouldn't be able to label points in space with definite coordinates. We'd have to worry about how the particles were behaving when they were at the points. These would be strange coordinates indeed.) We can, in theory, invert Eq. (6.39) and express the  $x_i$  as functions of the  $q_i$  and  $t$ ,

$$x_i = x_i(q_1, q_2, \dots, q_N; t). \quad (6.40)$$

**Claim 6.2** *If Eq. (6.38) is true for the  $x_i$  coordinates, and if the  $x_i$  and  $q_i$  are related by Eq. (6.40), then Eq. (6.38) is also true for the  $q_i$  coordinates. That is,*

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_m} \right) = \frac{\partial L}{\partial q_m} \quad (1 \leq m \leq N). \quad (6.41)$$

<sup>9</sup> This calculation is straightforward but a bit messy, so you may want to skip this section and just settle for the “beautiful and profound” reasoning.

**Proof:** We have

$$\frac{\partial L}{\partial \dot{q}_m} = \sum_{i=1}^N \frac{\partial L}{\partial \dot{x}_i} \frac{\partial \dot{x}_i}{\partial \dot{q}_m}. \quad (6.42)$$

(Note that if the  $x_i$  depended on the  $\dot{q}_i$ , then we would have to include the additional term,  $\sum (\partial L / \partial x_i) (\partial x_i / \partial \dot{q}_m)$ . But we have excluded such dependence.) Let's rewrite the  $\partial \dot{x}_i / \partial \dot{q}_m$  term. From Eq. (6.40), we have

$$\dot{x}_i = \sum_{m=1}^N \frac{\partial x_i}{\partial q_m} \dot{q}_m + \frac{\partial x_i}{\partial t}. \quad (6.43)$$

Therefore,

$$\frac{\partial \dot{x}_i}{\partial \dot{q}_m} = \frac{\partial x_i}{\partial q_m}. \quad (6.44)$$

Substituting this into Eq. (6.42) and taking the time derivative of both sides gives

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_m} \right) = \sum_{i=1}^N \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}_i} \right) \frac{\partial x_i}{\partial q_m} + \sum_{i=1}^N \frac{\partial L}{\partial \dot{x}_i} \frac{d}{dt} \left( \frac{\partial x_i}{\partial q_m} \right). \quad (6.45)$$

In the second term here, it is legal to switch the order of the total derivative,  $d/dt$ , and the partial derivative,  $\partial / \partial q_m$ .

**REMARK:** In case you have your doubts, let's prove that this switching is legal.

$$\begin{aligned} \frac{d}{dt} \left( \frac{\partial x_i}{\partial q_m} \right) &= \sum_{k=1}^N \frac{\partial}{\partial q_k} \left( \frac{\partial x_i}{\partial q_m} \right) \dot{q}_k + \frac{\partial}{\partial t} \left( \frac{\partial x_i}{\partial q_m} \right) \\ &= \frac{\partial}{\partial q_m} \left( \sum_{k=1}^N \frac{\partial x_i}{\partial q_k} \dot{q}_k + \frac{\partial x_i}{\partial t} \right) \\ &= \frac{\partial \dot{x}_i}{\partial q_m}. \quad \clubsuit \end{aligned} \quad (6.46)$$

In the first term on the right-hand side of Eq. (6.45), we can use the given information in Eq. (6.38) and rewrite the  $(d/dt)(\partial L / \partial \dot{x}_i)$  term. We then obtain

$$\begin{aligned} \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_m} \right) &= \sum_{i=1}^N \frac{\partial L}{\partial x_i} \frac{\partial x_i}{\partial q_m} + \sum_{i=1}^N \frac{\partial L}{\partial \dot{x}_i} \frac{\partial \dot{x}_i}{\partial q_m} \\ &= \frac{\partial L}{\partial q_m}, \end{aligned} \quad (6.47)$$

as we wanted to show. ■

We have therefore demonstrated that if the Euler–Lagrange equations are true for one set of coordinates,  $x_i$  (and they *are* true for Cartesian coordinates), then

they are also true for any other set of coordinates,  $q_i$ , satisfying Eq. (6.39). If you're inclined to look at the principle of stationary action with distrust, thinking that it might be a coordinate-dependent statement, this proof should put you at ease. The Euler–Lagrange equations are valid in any coordinates.

Note that the above proof did not in any way use the precise form of the Lagrangian. If  $L$  were equal to  $T + V$ , or  $8T + \pi V^2/T$ , or any other arbitrary function, our result would still be true: If Eq. (6.38) is true for one set of coordinates, then it is also true for any other set of coordinates  $q_i$  satisfying Eq. (6.39). The point is that the only  $L$  for which the hypothesis is true at all (that is, for which Eq. (6.38) holds) is  $L \equiv T - V$  (or any constant multiple of this).

**REMARK:** On one hand, it is quite amazing how little we assumed in proving the above claim. *Any* new coordinates of the very general form in Eq. (6.39) satisfy the E–L equations, as long as the original coordinates do. If the E–L equations had, say, a factor of 5 on the right-hand side of Eq. (6.38), then they would *not* hold in arbitrary coordinates. To see this, just follow the proof through with the factor of 5.

On the other hand, the claim is quite believable, if you make an analogy with a function instead of a functional. Consider the function  $f(z) = z^2$ . This has a minimum at  $z = 0$ , consistent with the fact that  $df/dz = 0$  at  $z = 0$ . But let's now write  $f$  in terms of the variable  $y$  defined by, say,  $z = y^4$ . Then  $f(y) = y^8$ , and  $f$  has a minimum at  $y = 0$ , consistent with the fact that  $df/dy = 0$  at  $y = 0$ . So  $f' = 0$  holds in both coordinates at the corresponding points  $y = z = 0$ . This is the (simplified) analog of the E–L equations holding in both coordinates. In both cases, the derivative equation describes where the stationary value occurs.

This change-of-variables result may be stated in a more geometrical (and friendly) way. If you plot a function and then stretch the horizontal axis in an arbitrary manner (which is what happens when you change coordinates), then a stationary value (that is, one where the slope is zero) will still be a stationary value after the stretching.<sup>10</sup> A picture (or even just the thought of one) is worth a dozen equations, apparently.

As an example of an equation that does *not* hold for all coordinates, consider the preceding example, but with  $f' = 1$  instead of  $f' = 0$ . In terms of  $z$ ,  $f' = 1$  when  $z = 1/2$ . And in terms of  $y$ ,  $f' = 1$  when  $y = (1/8)^{1/7}$ . But the points  $z = 1/2$  and  $y = (1/8)^{1/7}$  are not the same point. In other words,  $f' = 1$  is not a coordinate-independent statement. Most equations are coordinate dependent. The special thing about  $f' = 0$  is that a stationary point is a stationary point no matter how you look at it. ♣

### 6.5 Conservation laws

#### 6.5.1 Cyclic coordinates

Consider the case where the Lagrangian does not depend on a certain coordinate  $q_k$ . Then

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_k} \right) = \frac{\partial L}{\partial q_k} = 0 \implies \frac{\partial L}{\partial \dot{q}_k} = C, \quad (6.48)$$

<sup>10</sup> There is, however, one exception. A stationary point in one coordinate system might be located at a kink in another coordinate system, so that  $f'$  is not defined there. For example, if we had instead defined  $y$  by  $z = y^{1/4}$ , then  $f(y) = y^{1/2}$ , which has an undefined slope at  $y = 0$ . Basically, we've stretched (or shrunk) the horizontal axis by a factor of infinity at the origin, and this is a process that can change a zero slope into an undefined one. But let's not worry about this.

where  $C$  is a constant, that is, independent of time. In this case, we say that  $q_k$  is a *cyclic* coordinate, and that  $\partial L/\partial \dot{q}_k$  is a *conserved* quantity (meaning that it doesn't change with time). If Cartesian coordinates are used, then  $\partial L/\partial \dot{x}_k$  is simply the momentum,  $m\dot{x}_k$ , because  $\dot{x}_k$  appears only in the the kinetic energy's  $m\dot{x}_k^2/2$  term (we exclude cases where the potential depends on  $\dot{x}_k$ ). We therefore call  $\partial L/\partial \dot{q}_k$  the *generalized momentum* corresponding to the coordinate  $q_k$ . And in cases where  $\partial L/\partial \dot{q}_k$  does not change with time, we call it a *conserved momentum*. Note that a generalized momentum need not have the units of linear momentum, as the angular-momentum examples below show.

---

**Example (Linear momentum):** Consider a ball thrown through the air. In the full three dimensions, the Lagrangian is

$$L = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - mgz. \quad (6.49)$$

There is no  $x$  or  $y$  dependence here, so both  $\partial L/\partial \dot{x} = m\dot{x}$  and  $\partial L/\partial \dot{y} = m\dot{y}$  are constant, as we well know. The fancy way of saying this is that conservation of  $p_x \equiv m\dot{x}$  arises from spatial translation invariance in the  $x$  direction. The fact that the Lagrangian doesn't depend on  $x$  means that it doesn't matter if you throw the ball in one spot, or in another spot a mile down the road. The setup is independent of the  $x$  value. This independence leads to conservation of  $p_x$ . Likewise for  $p_y$ .

---

**Example (Angular and linear momentum in cylindrical coordinates):** Consider a potential that depends only on the distance to the  $z$  axis. In cylindrical coordinates, the Lagrangian is

$$L = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2 + \dot{z}^2) - V(r). \quad (6.50)$$

There is no  $z$  dependence here, so  $\partial L/\partial \dot{z} = m\dot{z}$  is constant. Also, there is no  $\theta$  dependence, so  $\partial L/\partial \dot{\theta} = mr^2\dot{\theta}$  is constant. Since  $r\dot{\theta}$  is the velocity in the tangential direction around the  $z$  axis, we see that our conserved quantity,  $mr(r\dot{\theta})$ , is the angular momentum (discussed in Chapters 7–9) around the  $z$  axis. In the same manner as in the preceding example, conservation of angular momentum around the  $z$  axis arises from rotation invariance around the  $z$  axis.

---

**Example (Angular momentum in spherical coordinates):** In spherical coordinates, consider a potential that depends only on  $r$  and  $\theta$ . Our convention for spherical coordinates is that  $\theta$  is the angle down from the north pole, and  $\phi$  is the angle around the equator. The Lagrangian is

$$L = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2 + r^2 \sin^2\theta \dot{\phi}^2) - V(r, \theta). \quad (6.51)$$

There is no  $\phi$  dependence here, so  $\partial L/\partial \dot{\phi} = mr^2 \sin^2 \theta \dot{\phi}$  is constant. Since  $r \sin \theta$  is the distance from the  $z$  axis, and since  $r \sin \theta \dot{\phi}$  is the speed in the tangential direction around the  $z$  axis, we see that our conserved quantity,  $m(r \sin \theta)(r \sin \theta \dot{\phi})$ , is the angular momentum around the  $z$  axis.

#### 6.5.2 Energy conservation

We will now derive another conservation law, namely conservation of energy. The conservation of momentum or angular momentum above arose when the Lagrangian was independent of  $x$ ,  $y$ ,  $z$ ,  $\theta$ , or  $\phi$ . Conservation of energy arises when the Lagrangian is independent of time. This conservation law is different from those in the above momenta examples, because  $t$  is not a coordinate that the stationary-action principle can be applied to. You can imagine varying the coordinates  $x$ ,  $\theta$ , etc., which are functions of  $t$ . But it makes no sense to vary  $t$ . Therefore, we're going to have to prove this conservation law in a different way. Consider the quantity

$$E \equiv \left( \sum_{i=1}^N \frac{\partial L}{\partial \dot{q}_i} \dot{q}_i \right) - L. \quad (6.52)$$

$E$  turns out (usually) to be the energy. We'll show this below. The motivation for this expression for  $E$  comes from the theory of Legendre transforms, but we won't get into that here. We'll just accept the definition in Eq. (6.52) and prove a very useful fact about it.

**Claim 6.3** *If  $L$  has no explicit time dependence (that is, if  $\partial L/\partial t = 0$ ), then  $E$  is conserved (that is,  $dE/dt = 0$ ), assuming that the motion obeys the E–L equations (which it does).*

Note that there is one partial derivative and one total derivative in this statement.

**Proof:**  $L$  is a function of the  $q_i$ , the  $\dot{q}_i$ , and possibly  $t$ . Making copious use of the chain rule, we have

$$\begin{aligned} \frac{dE}{dt} &= \frac{d}{dt} \left( \sum_{i=1}^N \frac{\partial L}{\partial \dot{q}_i} \dot{q}_i \right) - \frac{dL}{dt} \\ &= \sum_{i=1}^N \left( \left( \frac{d}{dt} \frac{\partial L}{\partial \dot{q}_i} \right) \dot{q}_i + \frac{\partial L}{\partial \dot{q}_i} \ddot{q}_i \right) - \left( \sum_{i=1}^N \left( \frac{\partial L}{\partial q_i} \dot{q}_i + \frac{\partial L}{\partial \dot{q}_i} \ddot{q}_i \right) + \frac{\partial L}{\partial t} \right). \end{aligned} \quad (6.53)$$

There are five terms here. The second cancels with the fourth. And the first (after using the E–L equation, Eq. (6.3), to rewrite it) cancels with the third. We

therefore arrive at the simple result,

$$\frac{dE}{dt} = -\frac{\partial L}{\partial t}. \quad (6.54)$$

In the event that  $\partial L/\partial t = 0$  (that is, there are no  $t$ 's sitting on the paper when you write down  $L$ ), which is usually the case in the situations we consider (because we generally won't deal with potentials that depend on time), we have  $dE/dt = 0$ . ■

Not too many things are constant with respect to time, and the quantity  $E$  has units of energy, so it's a good bet that it's the energy. Let's show this in Cartesian coordinates (however, see the remark below). The Lagrangian is

$$L = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - V(x, y, z), \quad (6.55)$$

so Eq. (6.52) gives

$$E = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) + V(x, y, z), \quad (6.56)$$

which is the total energy. The effect of the operations in Eq. (6.52) in most cases is just to switch the sign in front of the potential.

Of course, taking the kinetic energy  $T$  and subtracting the potential energy  $V$  to obtain  $L$ , and then using Eq. (6.52) to produce  $E = T + V$ , seems like a rather convoluted way of arriving at  $T + V$ . But the point of all this is that we used the E–L equations to *prove* that  $E$  is conserved. Although we know very well from the  $F = ma$  methods in Chapter 5 that the sum  $T + V$  is conserved, it's not fair to assume that it is conserved in our new Lagrangian formalism. We have to show that this *follows* from the E–L equations.

As with the translation and rotation invariance we observed in the examples in Section 6.5.1, we see that energy conservation arises from time translation invariance. If the Lagrangian has no explicit  $t$  dependence, then the setup looks the same today as it did yesterday. This fact leads to conservation of energy.

**REMARK:** The quantity  $E$  in Eq. (6.52) gives the energy of the system only if the entire system is represented by the Lagrangian. That is, the Lagrangian must represent a closed system with no external forces. If the system is not closed, then Claim 6.3 (or more generally, Eq. (6.54)) is still perfectly valid for the  $E$  defined in Eq. (6.52), but this  $E$  may simply not be the energy of the system. Problem 6.8 is a good example of such a situation.

Another example is the following. Imagine a long rod in the horizontal  $x$ - $y$  plane. The rod points in the  $x$  direction, and a bead is free to slide frictionlessly along it. At  $t = 0$ , an external machine is arranged to accelerate the rod in the negative  $y$  direction (that is, transverse to itself) with acceleration  $-g$ . So  $\ddot{y} = -gt$ . There is no internal potential energy in this system, so the

Lagrangian is just the kinetic energy,  $L = m\dot{x}^2/2 + m(gt)^2/2$ . Equation (6.52) therefore gives  $E = m\dot{x}^2/2 - m(gt)^2/2$ , which isn't the energy. But Eq. (6.54) is still true, because

$$\frac{dE}{dt} = -\frac{\partial L}{\partial t} \iff m\dot{x}\ddot{x} - mg^2t = -mg^2t \iff \ddot{x} = 0, \quad (6.57)$$

which is correct. However, this setup is exactly the same as projectile motion in the  $x$ - $y$  plane, where  $y$  is now the vertical axis, provided that we eliminate the rod and consider gravity instead of the machine to be causing the acceleration in the  $y$  direction. But if we are thinking in terms of gravity, then the normal thing to do is to say that the particle moves under the influence of the potential  $V(y) = mgy$ . The Lagrangian for this closed system (bead plus earth) is  $L = m(\dot{x}^2 + \dot{y}^2)/2 - mgy$ , and so Eq. (6.52) gives  $E = m(\dot{x}^2 + \dot{y}^2)/2 + mgy$ , which is indeed the energy of the particle. But having said all this, most of the systems we'll deal with are closed, so you can usually ignore this remark and assume that the  $E$  in Eq. (6.52) gives the energy. ♣

### 6.6 Noether's theorem

We now present one of the most beautiful and useful theorems in physics. It deals with two fundamental concepts, namely *symmetries* and *conserved quantities*. The theorem (due to Emmy Noether) may be stated as follows.

**Theorem 6.4 (Noether's theorem)** *For each symmetry of the Lagrangian, there is a conserved quantity.*

By “symmetry,” we mean that if the coordinates are changed by some small quantities, then the Lagrangian has no first-order change in these quantities. By “conserved quantity,” we mean a quantity that does not change with time. The result in Section 6.5.1 for cyclic coordinates is a special case of this theorem.

**Proof:** Let the Lagrangian be invariant, to first order in the small number  $\epsilon$ , under the change of coordinates,

$$q_i \longrightarrow q_i + \epsilon K_i(q). \quad (6.58)$$

Each  $K_i(q)$  may be a function of all the  $q_i$ , which we collectively denote by the shorthand,  $q$ .

**REMARK:** As an example of what these  $K_i$ 's might look like, consider the Lagrangian,  $L = (m/2)(5\dot{x}^2 - 2\dot{x}\dot{y} + 2\dot{y}^2) + C(2x - y)$ . We've just pulled this out of a hat, although it happens to be the type of  $L$  that arises in Atwood's machine problems; see Problem 6.9 and Exercise 6.40. This  $L$  is invariant under the transformation  $x \rightarrow x + \epsilon$  and  $y \rightarrow y + 2\epsilon$ , because the derivative terms are unaffected, and the difference  $2x - y$  is unchanged. (It's actually invariant to all orders in  $\epsilon$ , and not just first order. But this isn't necessary for the theorem to hold.) Therefore,  $K_x = 1$  and  $K_y = 2$ , which happen to be independent of the coordinates. In the problems we'll be doing, the  $K_i$ 's can generally be determined by simply looking at the potential term.

Of course, someone else might come along with  $K_x = 3$  and  $K_y = 6$ , which is also a symmetry. And indeed, any factor can be taken out of  $\epsilon$  and put into the  $K_i$ 's without changing the quantity  $\epsilon K_i(q)$  in Eq. (6.58). Any such modification will just bring an overall constant factor (and hence not change the property of being conserved) into the conserved quantity in Eq. (6.61) below. It is therefore irrelevant. ♣

The fact that the Lagrangian does not change at first order in  $\epsilon$  means that

$$\begin{aligned} 0 &= \frac{dL}{d\epsilon} = \sum_i \left( \frac{\partial L}{\partial q_i} \frac{\partial q_i}{\partial \epsilon} + \frac{\partial L}{\partial \dot{q}_i} \frac{\partial \dot{q}_i}{\partial \epsilon} \right) \\ &= \sum_i \left( \frac{\partial L}{\partial q_i} K_i + \frac{\partial L}{\partial \dot{q}_i} \dot{K}_i \right). \end{aligned} \quad (6.59)$$

Using the E–L equation, Eq. (6.3), we can rewrite this as

$$\begin{aligned} 0 &= \sum_i \left( \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) K_i + \frac{\partial L}{\partial \dot{q}_i} \dot{K}_i \right) \\ &= \frac{d}{dt} \left( \sum_i \frac{\partial L}{\partial \dot{q}_i} K_i \right). \end{aligned} \quad (6.60)$$

Therefore, the quantity

$$P(q, \dot{q}) \equiv \sum_i \frac{\partial L}{\partial \dot{q}_i} K_i(q) \quad (6.61)$$

does not change with time. It is given the generic name of *conserved momentum*. But it need not have the units of linear momentum. ■

As Noether most keenly observed  
(And for which much acclaim is deserved),  
It's easy to see  
That for each symmetry,  
A quantity must be conserved.

---

**Example 1:** Consider the Lagrangian in the above remark,  $L = (m/2)(5\dot{x}^2 - 2\dot{x}\dot{y} + 2\dot{y}^2) + C(2x - y)$ . We saw that  $K_x = 1$  and  $K_y = 2$ . The conserved momentum is therefore

$$\begin{aligned} P(x, y, \dot{x}, \dot{y}) &= \frac{\partial L}{\partial \dot{x}} K_x + \frac{\partial L}{\partial \dot{y}} K_y = m(5\dot{x} - \dot{y})(1) + m(-\dot{x} + 2\dot{y})(2) \\ &= m(3\dot{x} + 3\dot{y}). \end{aligned} \quad (6.62)$$

The overall factor of  $3m$  isn't important.

---

**Example 2:** Consider a thrown ball. We have  $L = (m/2)(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - mgz$ . This is invariant under translations in  $x$ , that is,  $x \rightarrow x + \epsilon$ ; and also under translations in  $y$ , that is,  $y \rightarrow y + \epsilon$ . (Both  $x$  and  $y$  are cyclic coordinates.) We need invariance only to first order in  $\epsilon$  for Noether's theorem to hold, but this  $L$  is invariant to all orders.

We therefore have two symmetries in our Lagrangian. The first has  $K_x = 1$ ,  $K_y = 0$ , and  $K_z = 0$ . The second has  $K_x = 0$ ,  $K_y = 1$ , and  $K_z = 0$ . Of course, the nonzero  $K_i$ 's here can be chosen to be any constants, but we may as well pick them to be 1. The two conserved momenta are

$$\begin{aligned} P_1(x, y, z, \dot{x}, \dot{y}, \dot{z}) &= \frac{\partial L}{\partial \dot{x}} K_x + \frac{\partial L}{\partial \dot{y}} K_y + \frac{\partial L}{\partial \dot{z}} K_z = m\dot{x}, \\ P_2(x, y, z, \dot{x}, \dot{y}, \dot{z}) &= \frac{\partial L}{\partial \dot{x}} K_x + \frac{\partial L}{\partial \dot{y}} K_y + \frac{\partial L}{\partial \dot{z}} K_z = m\dot{y}. \end{aligned} \quad (6.63)$$

These are simply the  $x$  and  $y$  components of the linear momentum, as we saw in the first example in Section 6.5.1. Note that any combination of these momenta, say  $3P_1 + 8P_2$ , is also conserved. (In other words,  $x \rightarrow x + 3\epsilon$ ,  $y \rightarrow y + 8\epsilon$ ,  $z \rightarrow z$  is a symmetry of the Lagrangian.) But the above  $P_1$  and  $P_2$  are the simplest momenta to choose as a “basis” for the infinite number of conserved momenta (which is how many you have, if there are two or more independent continuous symmetries).

---

**Example 3:** Consider a mass on a spring, with relaxed length zero, in the  $x$ - $y$  plane. The Lagrangian,  $L = (m/2)(\dot{x}^2 + \dot{y}^2) - (k/2)(x^2 + y^2)$ , is invariant under the change of coordinates,  $x \rightarrow x + \epsilon y$  and  $y \rightarrow y - \epsilon x$ , to first order in  $\epsilon$  (as you can check). So we have  $K_x = y$  and  $K_y = -x$ . The conserved momentum is therefore

$$P(x, y, \dot{x}, \dot{y}) = \frac{\partial L}{\partial \dot{x}} K_x + \frac{\partial L}{\partial \dot{y}} K_y = m(\dot{x}y - \dot{y}x). \quad (6.64)$$

This is the (negative of the)  $z$  component of the angular momentum. The angular momentum is conserved here because the potential,  $V(x, y) \propto x^2 + y^2 = r^2$ , depends only on the distance from the origin. We'll discuss such potentials in Chapter 7.

In contrast with the first two examples above, the  $x \rightarrow x + \epsilon y$ ,  $y \rightarrow y - \epsilon x$  transformation isn't so obvious here. How did we get this? Well, unfortunately there doesn't seem to be any fail-safe method of determining the  $K_i$ 's in general, so sometimes you just have to guess around. But in many problems, the  $K_i$ 's are simple constants which are easy to see.

#### --- REMARKS:

1. As we saw above, in some cases the  $K_i$ 's are functions of the coordinates, and in some cases they are not.
2. The cyclic-coordinate result in Eq. (6.48) is a special case of Noether's theorem, for the following reason. If  $L$  doesn't depend on a certain coordinate  $q_k$ , then  $q_k \rightarrow q_k + \epsilon$  is certainly a symmetry. Hence  $K_k = 1$  (with all the other  $K_i$ 's equal to zero), and Eq. (6.60) reduces to Eq. (6.48).
3. We use the word “symmetry” to describe the situation where the transformation in Eq. (6.58) produces no first-order change in the Lagrangian. This is an appropriate choice of word, because the Lagrangian describes the system, and if the system essentially doesn't change when the coordinates are changed, then we say that the system is symmetric. For example, if we have a setup that doesn't depend on  $\theta$ , then we say that the setup is symmetric under rotations. Rotate the system however you want, and it looks

the same. The two most common applications of Noether's theorem are the conservation of angular momentum, which arises from symmetry under rotations; and conservation of linear momentum, which arises from symmetry under translations.

4. In simple systems, as in Example 2 above, it is clear why the resulting  $P$  is conserved. But in more complicated systems, as in Example 1 above, the resulting  $P$  might not have an obvious interpretation. But at least you know that it is conserved, and this will invariably help in understanding a setup.
5. Although conserved quantities are extremely useful in studying a physical situation, it should be stressed that there is no more information contained in them than there is in the E–L equations. Conserved quantities are simply the result of integrating the E–L equations. For example, if you write down the E–L equations for Example 1 above, and then add the “ $x$ ” equation (which is  $5m\ddot{x} - m\ddot{y} = 2C$ ) to twice the “ $y$ ” equation (which is  $-m\ddot{x} + 2m\ddot{y} = -C$ ), then you arrive at  $3m(\ddot{x} + \ddot{y}) = 0$ . In other words,  $3m(\dot{x} + \dot{y})$  is constant, as we found from Noether's theorem.

Of course, you might have to do some guesswork to find the proper combination of the E–L equations that gives a zero on the right-hand side. But you'd have to do some guesswork anyway, to find the symmetry for Noether's theorem. At any rate, a conserved quantity is useful because it is an integrated form of the E–L equations. It puts you one step closer to solving the problem, compared with where you would be if you started with the second-order E–L equations.

6. Does every system have a conserved momentum? Certainly not. The one-dimensional problem of a falling ball ( $m\ddot{z} = -mg$ ) doesn't have one. And if you write down an arbitrary potential in 3-D, odds are that there won't be one. In a sense, things have to contrive nicely for there to be a conserved momentum. In some problems, you can just look at the physical system and see what the symmetry is, but in others (for example, in the Atwood's-machine problems for this chapter), the symmetry is not at all obvious.
7. By “conserved quantity,” we mean a quantity that depends on (at most) the coordinates and their first derivatives (that is, not on their second derivatives). If we don't make this restriction, then it is trivial to construct quantities that are independent of time. For example, in Example 1 above, the “ $x$ ” E–L equation (which is  $5m\ddot{x} - m\ddot{y} = 2C$ ) tells us that  $5m\ddot{x} - m\ddot{y}$  has its time derivative equal to zero. Note that an equivalent way of excluding these trivial cases is to say that the value of a conserved quantity depends on the initial conditions (that is, the velocities and positions). The quantity  $5m\ddot{x} - m\ddot{y}$  doesn't satisfy this criterion, because its value is always constrained to be  $2C$ . ♣

### 6.7 Small oscillations

In many physical systems, a particle undergoes small oscillations around an equilibrium point. In Section 5.2, we showed that the frequency of these small oscillations is

$$\omega = \sqrt{\frac{V''(x_0)}{m}}, \quad (6.65)$$

where  $V(x)$  is the potential energy, and  $x_0$  is the equilibrium point. However, this result holds only for *one-dimensional* motion (we'll see below why this is true). In more complicated systems, such as the one described below, it is necessary to use another procedure to obtain the frequency  $\omega$ . This procedure is a fail-safe one, applicable in all situations. It is, however, a bit more involved than simply writing down Eq. (6.65). So in one-dimensional problems, Eq. (6.65) is still what you want to use. We'll demonstrate our fail-safe method through the following problem.

![Diagram of a mass m on a frictionless table connected by a string through a hole to a hanging mass M. The string length is l, and the distance from the hole to m is r. The angle theta is shown relative to a vertical dashed line.](41183f01ec4a2599ce21177e2edcc150_img.jpg)

The diagram shows a rectangular table with a mass  $m$  on its surface. A string passes through a hole in the center of the table, connecting  $m$  to a hanging mass  $M$ . The distance from the hole to  $m$  is labeled  $r$ . The angle between the string on the table and a vertical dashed line is labeled  $\theta$ . The length of the string is  $l$ , and the portion of the string below the table is labeled  $l-r$ .

Diagram of a mass m on a frictionless table connected by a string through a hole to a hanging mass M. The string length is l, and the distance from the hole to m is r. The angle theta is shown relative to a vertical dashed line.

Fig. 6.5

**Problem:** A mass  $m$  is free to slide on a frictionless table and is connected, via a string that passes through a hole in the table, to a mass  $M$  that hangs below (see Fig. 6.5). Assume that  $M$  moves in a vertical line only, and assume that the string always remains taut.

- Find the equations of motion for the variables  $r$  and  $\theta$  shown in the figure.
- Under what condition does  $m$  undergo circular motion?
- What is the frequency of small oscillations (in the variable  $r$ ) about this circular motion?

**Solution:**

- Let the string have length  $\ell$  (this length won't matter). Then the Lagrangian (we'll call it " $\mathcal{L}$ " here, to save " $L$ " for the angular momentum, which arises below) is

$$\mathcal{L} = \frac{1}{2}M\dot{r}^2 + \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2) + Mg(\ell - r). \quad (6.66)$$

For the purposes of the potential energy, we've taken the table to be at height zero, but any other value could be chosen. The E–L equations of motion obtained from varying  $\theta$  and  $r$  are

$$\begin{aligned} \frac{d}{dt}(mr^2\dot{\theta}) &= 0, \\ (M + m)\ddot{r} &= mr\dot{\theta}^2 - Mg. \end{aligned} \quad (6.67)$$

The first equation says that angular momentum is conserved. The second equation says that the  $Mg$  gravitational force accounts for the acceleration of the two masses along the direction of the string, plus the centripetal acceleration of  $m$ .

- The first of Eqs. (6.67) says that  $mr^2\dot{\theta} = L$ , where  $L$  is some constant (the angular momentum) which depends on the initial conditions. Plugging  $\dot{\theta} = L/mr^2$  into the second of Eqs. (6.67) gives

$$(M + m)\ddot{r} = \frac{L^2}{mr^3} - Mg. \quad (6.68)$$

Circular motion occurs when  $\dot{r} = \ddot{r} = 0$ . Therefore, the radius of the circular orbit is given by

$$r_0^3 = \frac{L^2}{Mmg}. \quad (6.69)$$

Since  $L = mr^2\dot{\theta}$ , Eq. (6.69) is equivalent to

$$mr_0\dot{\theta}^2 = Mg, \quad (6.70)$$

which can also be obtained by letting  $\ddot{r} = 0$  in the second of Eqs. (6.67). In other words, the gravitational force on  $M$  exactly accounts for the centripetal acceleration of  $m$  if the motion is circular. Given  $r_0$ , Eq. (6.70) determines what  $\dot{\theta}$  must be in order to have circular motion, and vice versa.

- (c) To find the frequency of small oscillations about the circular motion, we need to look at what happens to  $r$  if we perturb it slightly from its equilibrium value of  $r_0$ . Our fail-safe procedure is the following.

Let  $r(t) \equiv r_0 + \delta(t)$ , where  $\delta(t)$  is very small (more precisely,  $\delta(t) \ll r_0$ ), and expand Eq. (6.68) to first order in  $\delta(t)$ . Using

$$\frac{1}{r^3} \equiv \frac{1}{(r_0 + \delta)^3} \approx \frac{1}{r_0^3 + 3r_0^2\delta} = \frac{1}{r_0^3(1 + 3\delta/r_0)} \approx \frac{1}{r_0^3} \left(1 - \frac{3\delta}{r_0}\right), \quad (6.71)$$

we obtain

$$(M + m)\ddot{\delta} \approx \frac{L^2}{mr_0^3} \left(1 - \frac{3\delta}{r_0}\right) - Mg. \quad (6.72)$$

The terms not involving  $\delta$  on the right-hand side cancel, by the definition of  $r_0$  given in Eq. (6.69). This cancellation always occurs in such a problem at this stage, due to the definition of the equilibrium point. We are therefore left with

$$\ddot{\delta} + \left(\frac{3L^2}{(M + m)mr_0^4}\right) \delta \approx 0. \quad (6.73)$$

This is a good old simple-harmonic-oscillator equation in the variable  $\delta$ . Therefore, the frequency of small oscillations about a circle of radius  $r_0$  is

$$\omega \approx \sqrt{\frac{3L^2}{(M + m)mr_0^4}} = \sqrt{\frac{3M}{M + m}} \sqrt{\frac{g}{r_0}}, \quad (6.74)$$

where we have used Eq. (6.69) to eliminate  $L$  in the second expression.

To sum up, the above frequency is the frequency of small oscillations in the variable  $r$ . In other words, if you have nearly circular motion, and if you plot  $r$  as a function of time (and ignore what  $\theta$  is doing), then you will get a nice sinusoidal graph whose frequency is given by Eq. (6.74). Note that this frequency need not have anything to do with the other relevant frequency in this problem, namely the frequency of the circular motion, which is  $\sqrt{M/m}\sqrt{g/r_0}$ , from Eq. (6.70).

**REMARKS:** Let's look at some limits. For a given  $r_0$ , if  $m \gg M$ , then  $\omega \approx \sqrt{3Mg/mr_0} \approx 0$ . This makes sense, because everything is moving very slowly. This frequency equals  $\sqrt{3}$  times the frequency of circular motion, namely  $\sqrt{Mg/mr_0}$ , which isn't at all obvious. For a given  $r_0$ , if  $m \ll M$ , then  $\omega \approx \sqrt{3g/r_0}$ , which isn't so obvious, either.

The frequency of small oscillations is equal to the frequency of circular motion if  $M = 2m$ , which, once again, isn't obvious. This condition is independent of  $r_0$ . ♣

The above procedure for finding the frequency of small oscillations can be summed up in three steps: (1) find the equations of motion; (2) find the equilibrium point; and (3) let  $x(t) \equiv x_0 + \delta(t)$ , where  $x_0$  is the equilibrium point of the relevant variable, and expand one of the equations of motion (or a combination of them) to first order in  $\delta$ , to obtain a simple-harmonic-oscillator equation for  $\delta$ . If the equilibrium point happens to be at  $x = 0$  (which is often the case), then everything is greatly simplified. There is no need to introduce  $\delta$ , and the expansion in the third step above simply entails ignoring powers of  $x$  that are higher than first order.

**REMARK:** If you just use the potential energy for the above problem (which is  $Mgr$ , up to an additive constant) in Eq. (6.65), then you will obtain a frequency of zero, which is incorrect. You *can* use Eq. (6.65) to find the frequency, if you instead use the “effective potential” for this problem, namely  $L^2/(2mr^2) + Mgr$ , and if you use the total mass,  $M + m$ , as the mass in Eq. (6.65), as you can check. The reason why this works will become clear in Chapter 7 when we introduce the effective potential. In many problems, however, it isn’t obvious what the appropriate modified potential is that should be used, or what mass goes in Eq. (6.65). So it’s generally much safer to take a deep breath and go through an expansion similar to the one in part (c) of the example above. ♣

The one-dimensional result in Eq. (6.65) is, of course, a special case of our above expansion procedure. We can repeat the derivation of Section 5.2 in the present language. In one dimension, the E–L equation of motion is  $m\ddot{x} = -V'(x)$ . Let  $x_0$  be the equilibrium point, so  $V'(x_0) = 0$ . And let  $x(t) \equiv x_0 + \delta(t)$ . Expanding  $m\ddot{x} = -V'(x)$  to first order in  $\delta$ , we have  $m\ddot{\delta} = -V'(x_0) - V''(x_0)\delta$ , plus higher-order terms. Since  $V'(x_0) = 0$ , we have  $m\ddot{\delta} \approx -V''(x_0)\delta$ , as desired.

![Figure 6.6: A diagram showing a surface of revolution. It is a 3D representation of a surface generated by rotating a curve around a central horizontal axis. The surface is wider at the right end and tapers towards the left. A dashed line represents the central axis of rotation.](a1699031d8fa07e0da305f2c4acdd587_img.jpg)

Figure 6.6: A diagram showing a surface of revolution. It is a 3D representation of a surface generated by rotating a curve around a central horizontal axis. The surface is wider at the right end and tapers towards the left. A dashed line represents the central axis of rotation.

Fig. 6.6

![Figure 6.7: A diagram showing a surface of revolution with specific boundary conditions. The surface is generated by rotating a curve y = y(x) around the x-axis. The left boundary is at x = a_1 with radius c_1, and the right boundary is at x = a_2 with radius c_2. The curve is labeled y(x).](ac46373947b338a8658ae56c8cc9168a_img.jpg)

Figure 6.7: A diagram showing a surface of revolution with specific boundary conditions. The surface is generated by rotating a curve y = y(x) around the x-axis. The left boundary is at x = a\_1 with radius c\_1, and the right boundary is at x = a\_2 with radius c\_2. The curve is labeled y(x).

Fig. 6.7

### 6.8 Other applications

The formalism developed in Section 6.2 works for *any* function  $L(x, \dot{x}, t)$ . If our goal is to find the stationary points of  $S \equiv \int L$ , then Eq. (6.15) holds, no matter what  $L$  is. There is no need for  $L$  to be equal to  $T - V$ , or indeed, to have anything to do with physics. And  $t$  need not have anything to do with time. All that is required is that the quantity  $x$  depend on the parameter  $t$ , and that  $L$  depend only on  $x$ ,  $\dot{x}$ , and  $t$  (and not, for example, on  $\ddot{x}$ ; see Exercise 6.34). The formalism is very general and powerful, as the following example demonstrates.

---

**Example (Minimal surface of revolution):** A surface of revolution has two given parallel rings as its boundary; see Fig. 6.6. What should the shape of the surface be so that it has the minimum possible area? We will present three solutions. A fourth is left for Problem 6.22.

**First solution:** Let the surface be generated by rotating the curve  $y = y(x)$  around the  $x$  axis. The boundary conditions are  $y(a_1) = c_1$  and  $y(a_2) = c_2$ ; see Fig. 6.7.

Slicing the surface up into vertical rings, we see that the area is given by

$$A = \int_{a_1}^{a_2} 2\pi y \sqrt{1 + y'^2} dx. \quad (6.75)$$

Our goal is to find the function  $y(x)$  that minimizes this integral. We therefore have exactly the same situation as in Section 6.2, except that  $x$  is now the parameter (instead of  $t$ ), and  $y$  is now the function (instead of  $x$ ). Our “Lagrangian” is thus  $L \propto y\sqrt{1 + y'^2}$ . To minimize the integral  $A$ , we “simply” have to write down the E–L equation,

$$\frac{d}{dx} \left( \frac{\partial L}{\partial y'} \right) = \frac{\partial L}{\partial y}, \quad (6.76)$$

and calculate the derivatives. This calculation however, gets a bit tedious, so I’ve relegated it to Lemma 6.5 at the end of this section. For now we’ll just use the result in Eq. (6.86) which gives (with  $f(y) = y$  here)

$$1 + y'^2 = By^2. \quad (6.77)$$

At this point we can cleverly guess (motivated by the fact that  $1 + \sinh^2 z = \cosh^2 z$ ) that the solution is

$$y(x) = \frac{1}{b} \cosh b(x + d), \quad (6.78)$$

where  $b = \sqrt{B}$ , and  $d$  is a constant of integration. Or we can separate variables to obtain (again with  $b = \sqrt{B}$ )

$$dx = \frac{dy}{\sqrt{(by)^2 - 1}}, \quad (6.79)$$

and then use the fact that the integral of  $1/\sqrt{z^2 - 1}$  is  $\cosh^{-1} z$ , to obtain the same result. The answer to our problem, therefore, is that  $y(x)$  takes the form of Eq. (6.78), with  $b$  and  $d$  determined by the boundary conditions,

$$c_1 = \frac{1}{b} \cosh b(a_1 + d), \quad \text{and} \quad c_2 = \frac{1}{b} \cosh b(a_2 + d). \quad (6.80)$$

In the symmetrical case where  $c_1 = c_2$ , we know that the minimum occurs in the middle, so we may choose  $d = 0$  and  $a_1 = -a_2$ .

Solutions for  $b$  and  $d$  exist only for certain ranges of the  $a$ ’s and  $c$ ’s. Basically, if  $a_2 - a_1$  is too large, then there is no solution. In this case, the minimal “surface” turns out to be the two given circles, attached by a line (which isn’t a nice two-dimensional surface). If you perform an experiment with soap bubbles (which want to minimize their area), and if you pull the rings too far apart, then the surface will break and disappear as it tries to form the two circles. Problem 6.23 deals with this issue.

**Second solution:** Consider the curve that we rotate around the  $x$  axis to be described now by the function  $x(y)$ . That is, let  $x$  be a function of  $y$ . The area is then given by

$$A = \int_{c_1}^{c_2} 2\pi y \sqrt{1 + x'^2} dy, \quad (6.81)$$

where  $x' \equiv dx/dy$ . Note that the function  $x(y)$  may be double-valued, so it may not really be a function. But it looks like a function locally, and all of our formalism deals with local variations.

Our “Lagrangian” is now  $L \propto y\sqrt{1+x'^2}$ , and the E–L equation is

$$\frac{d}{dy}\left(\frac{\partial L}{\partial x'}\right) = \frac{\partial L}{\partial x} \implies \frac{d}{dy}\left(\frac{yx'}{\sqrt{1+x'^2}}\right) = 0. \quad (6.82)$$

The nice thing about this solution is the “0” on the right-hand side, which arises from the fact that  $L$  doesn’t depend on  $x$  (that is,  $x$  is a cyclic coordinate). Therefore,  $yx'/\sqrt{1+x'^2}$  is constant. If we define this constant to be  $1/b$ , then we can solve for  $x'$  and then separate variables to obtain

$$dx = \frac{dy}{\sqrt{(by)^2 - 1}}, \quad (6.83)$$

in agreement with Eq. (6.79). The solution proceeds as above.

**Third solution:** The “Lagrangian” in the first solution above,  $L \propto y\sqrt{1+y'^2}$ , is independent of  $x$ . Therefore, in analogy with conservation of energy (which arises from a Lagrangian that is independent of  $t$ ), the quantity

$$E \equiv y' \frac{\partial L}{\partial y'} - L = \frac{y'^2 y}{\sqrt{1+y'^2}} - y\sqrt{1+y'^2} = \frac{-y}{\sqrt{1+y'^2}} \quad (6.84)$$

is constant (that is, independent of  $x$ ). This statement is equivalent to Eq. (6.77), and the solution proceeds as above. As demonstrated by the brevity of the second and third solutions here, it is highly advantageous to make use of conserved quantities whenever you can.

---

Let us now prove the following lemma, which we invoked in the first solution above. This lemma is very useful, because it is common to encounter problems where the quantity to be extremized depends on the arclength,  $\sqrt{1+y'^2}$ , and takes the form of  $\int f(y)\sqrt{1+y'^2} dx$ . We will give two proofs. The first proof uses the Euler–Lagrange equation. The calculation gets a bit messy, so it’s a good idea to work through it once and for all and then just invoke the result whenever needed. This derivation isn’t something you’d want to repeat too often. The second proof makes use of a conserved quantity. And in contrast with the first proof, this method is exceedingly clean and simple. It actually *is* something you’d want to repeat quite often. But we’ll still do it once and for all.

**Lemma 6.5** *Let  $f(y)$  be a given function of  $y$ . Then the function  $y(x)$  that extremizes the integral,*

$$\int_{x_1}^{x_2} f(y)\sqrt{1+y'^2} dx, \quad (6.85)$$

satisfies the differential equation,

$$1 + y'^2 = Bf(y)^2, \quad (6.86)$$

where  $B$  is a constant of integration.<sup>11</sup>

**First proof:** Our goal is to find the function  $y(x)$  that extremizes the integral in Eq. (6.85). We therefore have exactly the same situation as in Section 6.2, except with  $x$  in place of  $t$ , and  $y$  in place of  $x$ . Our “Lagrangian” is thus  $L = f(y)\sqrt{1 + y'^2}$ , and the Euler–Lagrange equation is

$$\frac{d}{dx} \left( \frac{\partial L}{\partial y'} \right) = \frac{\partial L}{\partial y} \implies \frac{d}{dx} \left( f \cdot y' \cdot \frac{1}{\sqrt{1 + y'^2}} \right) = f' \sqrt{1 + y'^2}, \quad (6.87)$$

where  $f' \equiv df/dy$ . We must now perform some straightforward (albeit tedious) differentiations. Using the product rule on the three factors on the left-hand side, and making copious use of the chain rule, we obtain

$$\frac{f'y'^2}{\sqrt{1 + y'^2}} + \frac{fy''}{\sqrt{1 + y'^2}} - \frac{fy'^2y''}{(1 + y'^2)^{3/2}} = f' \sqrt{1 + y'^2}. \quad (6.88)$$

Multiplying through by  $(1 + y'^2)^{3/2}$  and simplifying gives

$$fy'' = f'(1 + y'^2). \quad (6.89)$$

We have completed the first step of the proof, namely producing the Euler–Lagrange differential equation. We must now integrate it. Equation (6.89) happens to be integrable for arbitrary functions  $f(y)$ . If we multiply through by  $y'$  and rearrange, we obtain

$$\frac{y'y''}{1 + y'^2} = \frac{f'y'}{f}. \quad (6.90)$$

Taking the  $dx$  integral of both sides gives  $(1/2) \ln(1 + y'^2) = \ln(f) + C$ , where  $C$  is a constant of integration. Exponentiation then gives (with  $B \equiv e^{2C}$ )

$$1 + y'^2 = Bf(y)^2, \quad (6.91)$$

as we wanted to show. In an actual problem, we would solve this equation for  $y'$ , and then separate variables and integrate. But we would need to be given a specific function  $f(y)$  to be able to do this.

<sup>11</sup> The constant  $B$  and also one other constant of integration (arising when Eq. (6.86) is integrated to obtain  $y$ ) are determined by the boundary conditions on  $y(x)$ ; see, for example, Eq. (6.80). This situation, where the two constants are determined by the values of the function at two points, is slightly different from the situation in the physics problems we’ve done where the two constants are determined by the value (that is, the initial position) and the slope (that is, the speed) at just one point. But either way, two given facts must be used.

**Second proof:** Our “Lagrangian,”  $L = f(y)\sqrt{1 + y'^2}$ , is independent of  $x$ . Therefore, in analogy with the conserved energy given in Eq. (6.52), the quantity

$$E \equiv y' \frac{\partial L}{\partial y'} - L = \frac{-f(y)}{\sqrt{1 + y'^2}} \quad (6.92)$$

is independent of  $x$ . Call it  $1/\sqrt{B}$ . Then we have easily reproduced Eq. (6.91). For practice, you can also prove this lemma by considering  $x$  to be a function of  $y$ , as we did in the second solution in the minimal-surface example above. ■

![Diagram of a block of mass m on an inclined plane of mass M and angle theta. The plane is on a horizontal surface and has a horizontal arrow pointing left, indicating it can move.](4d12d97f0b15c331e237d43daa8cb585_img.jpg)

Diagram of a block of mass m on an inclined plane of mass M and angle theta. The plane is on a horizontal surface and has a horizontal arrow pointing left, indicating it can move.

Fig. 6.8

![Diagram of two falling sticks. The bottom stick is vertical, hinged at the ground, with a mass m at its center. The top stick is also hinged at the bottom of the bottom stick, with a mass m at its center. The top stick is tilted at a small angle epsilon from the vertical. Both sticks have length r.](725b7b3fc268306ee12619ce78ce9b28_img.jpg)

Diagram of two falling sticks. The bottom stick is vertical, hinged at the ground, with a mass m at its center. The top stick is also hinged at the bottom of the bottom stick, with a mass m at its center. The top stick is tilted at a small angle epsilon from the vertical. Both sticks have length r.

Fig. 6.9

![Diagram of a pendulum with an oscillating support. A mass m is at the end of a massless stick of length l. The support at the top is a block that can move horizontally, indicated by a double-headed arrow.](2ee9e7e891d32bf23d2aa88357a06eb3_img.jpg)

Diagram of a pendulum with an oscillating support. A mass m is at the end of a massless stick of length l. The support at the top is a block that can move horizontally, indicated by a double-headed arrow.

Fig. 6.10

![Diagram of two masses, one swinging. Two equal masses m are connected by a massless string over two pulleys. The left mass hangs vertically. The right mass hangs at an angle theta from the vertical, with the string segment having length r.](5e29799065c14f6fff2aa203ff29c4b6_img.jpg)

Diagram of two masses, one swinging. Two equal masses m are connected by a massless string over two pulleys. The left mass hangs vertically. The right mass hangs at an angle theta from the vertical, with the string segment having length r.

Fig. 6.11

### 6.9 Problems

## Section 6.1: The Euler–Lagrange equations

#### 6.1. Moving plane \*\*

A block of mass  $m$  is held motionless on a frictionless plane of mass  $M$  and angle of inclination  $\theta$  (see Fig. 6.8). The plane rests on a frictionless horizontal surface. The block is released. What is the horizontal acceleration of the plane? (This problem already showed up as Problem 3.8. If you haven’t already done so, try solving it using  $F = ma$ . You will then have a greater appreciation for the Lagrangian method.)

### 6.2. Two falling sticks \*\*

Two massless sticks of length  $2r$ , each with a mass  $m$  fixed at its middle, are hinged at an end. One stands on top of the other, as shown in Fig. 6.9. The bottom end of the lower stick is hinged at the ground. They are held such that the lower stick is vertical, and the upper one is tilted at a small angle  $\epsilon$  with respect to the vertical. They are then released. At this instant, what are the angular accelerations of the two sticks? Work in the approximation where  $\epsilon$  is very small.

### 6.3. Pendulum with an oscillating support \*\*

A pendulum consists of a mass  $m$  and a massless stick of length  $\ell$ . The pendulum support oscillates horizontally with a position given by  $x(t) = A \cos(\omega t)$ ; see Fig. 6.10. What is the general solution for the angle of the pendulum as a function of time?

### 6.4. Two masses, one swinging \*\*\*

Two equal masses  $m$ , connected by a massless string, hang over two pulleys (of negligible size), as shown in Fig. 6.11. The left one moves in a vertical line, but the right one is free to swing back and forth in the plane of the masses and pulleys. Find the equations of motion for  $r$  and  $\theta$ , as shown.

Assume that the left mass starts at rest, and the right mass undergoes small oscillations with angular amplitude  $\epsilon$  (with  $\epsilon \ll 1$ ). What is the

initial average acceleration (averaged over a few periods) of the left mass? In which direction does it move?

#### 6.5. Inverted pendulum \*\*\*\*

A pendulum consists of a mass  $m$  at the end of a massless stick of length  $\ell$ . The other end of the stick is made to oscillate vertically with a position given by  $y(t) = A \cos(\omega t)$ , where  $A \ll \ell$ . See Fig. 6.12. It turns out that if  $\omega$  is large enough, and if the pendulum is initially nearly upside-down, then surprisingly it will *not* fall over as time goes by. Instead, it will (sort of) oscillate back and forth around the vertical position. If you want to do the experiment yourself, see the 28th demonstration of the entertaining collection in Ehrlich (1994).

Find the equation of motion for the angle of the pendulum (measured relative to its upside-down position). Explain why the pendulum doesn't fall over, and find the frequency of the back and forth motion.

![Diagram of an inverted pendulum. A mass m is at the end of a massless stick of length l. The other end of the stick is attached to a base that is oscillating vertically, indicated by a double-headed arrow. The stick is shown at an angle to the vertical.](f5a022147c6e963ecdb57ee17ace49d8_img.jpg)

Diagram of an inverted pendulum. A mass m is at the end of a massless stick of length l. The other end of the stick is attached to a base that is oscillating vertically, indicated by a double-headed arrow. The stick is shown at an angle to the vertical.

Fig. 6.12

### Section 6.2: The principle of stationary action

### 6.6. Minimum or saddle \*\*

- (a) In Eq. (6.26), let  $t_1 = 0$  and  $t_2 = T$ , for convenience. And let  $\xi(t)$  be an easy-to-deal-with “triangular” function, of the form

$$\xi(t) = \begin{cases} \epsilon t/T, & 0 \leq t \leq T/2, \\ \epsilon(1 - t/T), & T/2 \leq t \leq T. \end{cases} \quad (6.93)$$

Under what condition is the harmonic-oscillator  $\Delta S$  in Eq. (6.26) negative?

- (b) Answer the same question, but now with  $\xi(t) = \epsilon \sin(\pi t/T)$ .

### Section 6.3: Forces of constraint

### 6.7. Normal force from a plane \*\*

A mass  $m$  slides down a frictionless plane that is inclined at an angle  $\theta$ . Show, using the method in Section 6.3, that the normal force from the plane is the familiar  $mg \cos \theta$ .

### Section 6.5: Conservation laws

#### 6.8. Bead on a stick \*

A stick is pivoted at the origin and is arranged to swing around in a horizontal plane at constant angular speed  $\omega$ . A bead of mass  $m$  slides frictionlessly along the stick. Let  $r$  be the radial position of the bead. Find the conserved quantity  $E$  given in Eq. (6.52). Explain why this quantity is *not* the energy of the bead.

![Diagram of an Atwood's machine with three pulleys and three masses. The left mass is 4m at height x, the middle mass is 3m, and the right mass is m at height y. The pulleys are arranged in a series, with the left and right pulleys fixed to a ceiling and the middle pulley movable.](444d6fc1e540b0300839c7dce7b4c517_img.jpg)

Diagram of an Atwood's machine with three pulleys and three masses. The left mass is 4m at height x, the middle mass is 3m, and the right mass is m at height y. The pulleys are arranged in a series, with the left and right pulleys fixed to a ceiling and the middle pulley movable.

Fig. 6.13

### Section 6.6: Noether's theorem

### 6.9. Atwood's machine \*\*

Consider the Atwood's machine shown in Fig. 6.13. The masses are  $4m$ ,  $3m$ , and  $m$ . Let  $x$  and  $y$  be the heights of the left and right masses, relative to their initial positions. Find the conserved momentum.

![Diagram of a hoop and pulley system. A mass M is attached to a massless hoop of radius R that lies in a vertical plane. The hoop is free to rotate about its fixed center. M is tied to a string which winds part way around the hoop, then rises vertically up and over a massless pulley. A mass m hangs on the other end of the string.](33e7d594235ea4babd7d265d9feb911a_img.jpg)

Diagram of a hoop and pulley system. A mass M is attached to a massless hoop of radius R that lies in a vertical plane. The hoop is free to rotate about its fixed center. M is tied to a string which winds part way around the hoop, then rises vertically up and over a massless pulley. A mass m hangs on the other end of the string.

Fig. 6.14

### Section 6.7: Small oscillations

#### 6.10. Hoop and pulley \*\*

A mass  $M$  is attached to a massless hoop of radius  $R$  that lies in a vertical plane. The hoop is free to rotate about its fixed center.  $M$  is tied to a string which winds part way around the hoop, then rises vertically up and over a massless pulley. A mass  $m$  hangs on the other end of the string (see Fig. 6.14). Find the equation of motion for the angle of rotation of the hoop. What is the frequency of small oscillations? Assume that  $m$  moves only vertically, and assume  $M > m$ .

![Diagram of a bead on a rotating hoop. A bead is free to slide along a frictionless hoop of radius R. The hoop rotates with constant angular speed omega around a vertical diameter. The angle theta is shown between the vertical diameter and the radius to the bead.](958b6abad112641aff6e44e6235a2ea1_img.jpg)

Diagram of a bead on a rotating hoop. A bead is free to slide along a frictionless hoop of radius R. The hoop rotates with constant angular speed omega around a vertical diameter. The angle theta is shown between the vertical diameter and the radius to the bead.

Fig. 6.15

#### 6.11. Bead on a rotating hoop \*\*

A bead is free to slide along a frictionless hoop of radius  $R$ . The hoop rotates with constant angular speed  $\omega$  around a vertical diameter (see Fig. 6.15). Find the equation of motion for the angle  $\theta$  shown. What are the equilibrium positions? What is the frequency of small oscillations about the stable equilibrium? There is one value of  $\omega$  that is rather special; what is it, and why is it special?

![Diagram of another bead on a rotating hoop (top view). A bead is free to slide along a frictionless hoop of radius r. The plane of the hoop is horizontal, and the center of the hoop travels in a horizontal circle of radius R, with constant angular speed omega, about a given point. The angle theta is shown between the radius to the center of the hoop and the radius to the bead.](b4808acdd3ce082e54dd5cbec213e997_img.jpg)

Diagram of another bead on a rotating hoop (top view). A bead is free to slide along a frictionless hoop of radius r. The plane of the hoop is horizontal, and the center of the hoop travels in a horizontal circle of radius R, with constant angular speed omega, about a given point. The angle theta is shown between the radius to the center of the hoop and the radius to the bead.

Fig. 6.16

#### 6.12. Another bead on a rotating hoop \*\*

A bead is free to slide along a frictionless hoop of radius  $r$ . The plane of the hoop is horizontal, and the center of the hoop travels in a horizontal circle of radius  $R$ , with constant angular speed  $\omega$ , about a given point (see Fig. 6.16). Find the equation of motion for the angle  $\theta$  shown. Also, find the frequency of small oscillations about the equilibrium point.

#### 6.13. Mass on a wheel \*\*

A mass  $m$  is fixed to a given point on the rim of a wheel of radius  $R$  that rolls without slipping on the ground. The wheel is massless, except for a mass  $M$  located at its center. Find the equation of motion for the angle through which the wheel rolls. For the case where the wheel undergoes small oscillations, find the frequency.

![Diagram of a pendulum with a free support. A mass M is free to slide along a frictionless rail. A pendulum of length l and mass m hangs from M.](bd8bca5edf4c79825d3f2be721ed94b3_img.jpg)

Diagram of a pendulum with a free support. A mass M is free to slide along a frictionless rail. A pendulum of length l and mass m hangs from M.

Fig. 6.17

#### 6.14. Pendulum with a free support \*\*

A mass  $M$  is free to slide along a frictionless rail. A pendulum of length  $l$  and mass  $m$  hangs from  $M$  (see Fig. 6.17). Find the equations of motion. For small oscillations, find the normal modes and their frequencies.

#### **6.15. Pendulum support on an inclined plane \*\***

A mass  $M$  is free to slide down a frictionless plane inclined at an angle  $\beta$ . A pendulum of length  $l$  and mass  $m$  hangs from  $M$ ; see Fig. 6.18 (assume that  $M$  extends a short distance beyond the side of the plane, so the pendulum can hang down). Find the equations of motion. For small oscillations, find the normal modes and their frequencies.

![Diagram for problem 6.15: A block of mass M on an inclined plane at angle beta. A pendulum of length l and mass m is suspended from the block.](a43193244fcc992530f5886b41338ffe_img.jpg)

Diagram for problem 6.15: A block of mass M on an inclined plane at angle beta. A pendulum of length l and mass m is suspended from the block.

Fig. 6.18

#### **6.16. Tilting plane \*\*\***

A mass  $M$  is fixed at the right-angled vertex where a massless rod of length  $l$  is attached to a very long massless rod (see Fig. 6.19). A mass  $m$  is free to move frictionlessly along the long rod (assume that it can pass through  $M$ ). The rod of length  $l$  is hinged at a support, and the whole system is free to rotate, in the plane of the rods, about the hinge. Let  $\theta$  be the angle of rotation of the system, and let  $x$  be the distance between  $m$  and  $M$ . Find the equations of motion. Find the normal modes when  $\theta$  and  $x$  are both very small.

![Diagram for problem 6.16: A mass M is at the vertex of two rods. One rod of length l is hinged at a support and makes an angle theta with the vertical. The other rod is long and massless, and mass m is at a distance x from M.](640465c4ecaa54d2d7d83bb967f4e20a_img.jpg)

Diagram for problem 6.16: A mass M is at the vertex of two rods. One rod of length l is hinged at a support and makes an angle theta with the vertical. The other rod is long and massless, and mass m is at a distance x from M.

Fig. 6.19

#### **6.17. Rotating curve \*\*\***

The curve  $y(x) = b(x/a)^\lambda$  is rotated around the  $y$  axis with constant frequency  $\omega$  (see Fig. 6.20). A bead moves frictionlessly along the curve. Find the frequency of small oscillations about the equilibrium point. Under what conditions do oscillations exist? (This problem gets a little messy.)

![Diagram for problem 6.17: A curve y(x) = b(x/a)^lambda in the xy-plane. The curve is rotated around the y-axis with angular frequency omega. A bead is shown on the curve.](9656aea17abaef10ba86544a33aea01d_img.jpg)

Diagram for problem 6.17: A curve y(x) = b(x/a)^lambda in the xy-plane. The curve is rotated around the y-axis with angular frequency omega. A bead is shown on the curve.

Fig. 6.20

#### **6.18. Motion in a cone \*\*\***

A particle slides on the inside surface of a frictionless cone. The cone is fixed with its tip on the ground and its axis vertical. The half-angle at the tip is  $\alpha$  (see Fig. 6.21). Let  $r$  be the distance from the particle to the axis, and let  $\theta$  be the angle around the cone. Find the equations of motion.

If the particle moves in a circle of radius  $r_0$ , what is the frequency,  $\omega$ , of this motion? If the particle is then perturbed slightly from this circular motion, what is the frequency,  $\Omega$ , of the oscillations about the radius  $r_0$ ? Under what conditions does  $\Omega = \omega$ ?

![Diagram for problem 6.18: A cone with half-angle alpha at its tip. A particle is shown moving in a horizontal circle of radius r_0 on the inner surface of the cone.](d724e9697826af65e659841928838211_img.jpg)

Diagram for problem 6.18: A cone with half-angle alpha at its tip. A particle is shown moving in a horizontal circle of radius r\_0 on the inner surface of the cone.

Fig. 6.21

#### **6.19. Double pendulum \*\*\*\***

Consider a double pendulum made of two masses,  $m_1$  and  $m_2$ , and two rods of lengths  $l_1$  and  $l_2$  (see Fig. 6.22). Find the equations of motion.

For small oscillations, find the normal modes and their frequencies for the special case  $l_1 = l_2$  (and consider the cases  $m_1 = m_2$ ,  $m_1 \gg m_2$ , and  $m_1 \ll m_2$ ). Do the same for the special case  $m_1 = m_2$  (and consider the cases  $l_1 = l_2$ ,  $l_1 \gg l_2$ , and  $l_1 \ll l_2$ ).

![Diagram for problem 6.19: A double pendulum with two masses m1 and m2 and two rods of lengths l1 and l2 suspended from a fixed support.](aecc43683c0c570cb4819db16f3e2b0d_img.jpg)

Diagram for problem 6.19: A double pendulum with two masses m1 and m2 and two rods of lengths l1 and l2 suspended from a fixed support.

Fig. 6.22

### Section 6.8: Other applications

#### 6.20. Shortest distance in a plane \*

In the spirit of Section 6.8, show that the shortest path between two points in a plane is a straight line.

![Diagram for Fig. 6.23: A rectangle representing a plane with two points inside. A curved arrow indicates a path from the first point to the second.](1ef219415059e42ac0d3a662d321c030_img.jpg)

Diagram for Fig. 6.23: A rectangle representing a plane with two points inside. A curved arrow indicates a path from the first point to the second.

Fig. 6.23

### 6.21. Index of refraction \*\*

Assume that the speed of light in a given slab of material is proportional to the height above the base of the slab.<sup>12</sup> Show that light moves in circular arcs in this material; see Fig. 6.23. You may assume that light takes the path of least time between two points (Fermat's principle of least time).

![Diagram for Fig. 6.24: A minimal surface of revolution between two vertical planes at x1 and x2. The surface is shown as a dashed curve rotated around a central axis.](25b51f10a41f04441586f7090dcdd4f1_img.jpg)

Diagram for Fig. 6.24: A minimal surface of revolution between two vertical planes at x1 and x2. The surface is shown as a dashed curve rotated around a central axis.

Fig. 6.24

### 6.22. Minimal surface \*\*

Derive the shape of the minimal surface discussed in Section 6.8, by demanding that a cross-sectional “ring” (that is, the region between the planes  $x = x_1$  and  $x = x_2$ ) is in equilibrium; see Fig. 6.24. *Hint:* The tension must be constant throughout the surface (assuming that we're ignoring gravity, which we are).

![Diagram for Fig. 6.25: A minimal surface of revolution between two vertical planes. The distance between the planes is labeled 2l, and the radius of the rings at the planes is labeled r.](eaa61dcb7ce4a9dc8cf50e137b571c63_img.jpg)

Diagram for Fig. 6.25: A minimal surface of revolution between two vertical planes. The distance between the planes is labeled 2l, and the radius of the rings at the planes is labeled r.

Fig. 6.25

#### 6.23. Existence of a minimal surface \*\*

Consider the minimal surface from Section 6.8, and look at the special case where the two rings have the same radius  $r$  (see Fig. 6.25). Let  $2\ell$  be the distance between the rings. What is the largest value of  $\ell/r$  for which a minimal surface exists? You will need to solve something numerically here.

#### 6.24. The brachistochrone \*\*\*

A bead is released from rest at the origin and slides down a frictionless wire that connects the origin to a given point, as shown in Fig. 6.26. You wish to shape the wire so that the bead reaches the endpoint in the shortest possible time. Let the desired curve be described by the function  $y(x)$ , with downward taken to be positive. Show that  $y(x)$  satisfies

![Diagram for Fig. 6.26: A coordinate system with x horizontal and y vertical (downward). A curve starts at the origin (0,0) and ends at a point (x,y). An arrow on the curve indicates the direction of motion.](86c862b9ee2c40d0cc2d8484ae6fe3e7_img.jpg)

Diagram for Fig. 6.26: A coordinate system with x horizontal and y vertical (downward). A curve starts at the origin (0,0) and ends at a point (x,y). An arrow on the curve indicates the direction of motion.

Fig. 6.26

$$1 + y'^2 = \frac{B}{y}, \quad (6.94)$$

where  $B$  is a constant. Then show that  $x$  and  $y$  may be written as

$$x = a(\theta - \sin \theta), \quad y = a(1 - \cos \theta). \quad (6.95)$$

<sup>12</sup> If you want to make the equivalent statement in terms of the material's “index of refraction,” commonly denoted by  $n$ , then you can say: As a function of the height  $y$ , the index  $n$  is given by  $n(y) = y_0/y$ , where  $y_0$  is some length that is larger than the height of the slab. This is equivalent to the original statement because the speed of light in a material equals  $c/n$ .

This is the parametrization of a *cycloid*, which is the path taken by a point on the rim of a rolling wheel.

### 6.10 Exercises

### Section 6.1: The Euler–Lagrange equations

### 6.25. Spring on a T \*\*

A rigid T consists of a long rod glued perpendicular to another rod of length  $\ell$  that is pivoted at the origin. The T rotates around in a horizontal plane with constant frequency  $\omega$ . A mass  $m$  is free to slide along the long rod and is connected to the intersection of the rods by a spring with spring constant  $k$  and relaxed length zero (see Fig. 6.27). Find  $r(t)$ , where  $r$  is the position of the mass along the long rod. There is a special value of  $\omega$ ; what is it, and why is it special?

![Diagram of a mass m on a rotating T-shaped rod. The T is pivoted at the origin and rotates with angular frequency omega in a horizontal plane. The mass m is on the long rod at a distance r from the pivot. A spring with constant k connects the mass to the pivot. The diagram is labeled '(top view)'.](b0ef965bd8727ea993fad049549046d5_img.jpg)

Diagram of a mass m on a rotating T-shaped rod. The T is pivoted at the origin and rotates with angular frequency omega in a horizontal plane. The mass m is on the long rod at a distance r from the pivot. A spring with constant k connects the mass to the pivot. The diagram is labeled '(top view)'.

Fig. 6.27

### 6.26. Spring on a T, with gravity \*\*\*

Consider the setup in the previous exercise, but now let the T swing around in a vertical plane with constant frequency  $\omega$ . Find  $r(t)$ . There is a special value of  $\omega$ ; what is it, and why is it special? (You may assume  $\omega < \sqrt{k/m}$ .)

![Diagram of a mass m on a rotating T-shaped rod in a vertical plane. The T is pivoted at the origin and rotates with angular frequency omega. The mass m is on the long rod at a distance r from the pivot. A spring with constant k connects the mass to the pivot. The diagram is labeled '(top view)'.](c2ba1bdd5e12870c7bbe7c0080ba3ed8_img.jpg)

Diagram of a mass m on a rotating T-shaped rod in a vertical plane. The T is pivoted at the origin and rotates with angular frequency omega. The mass m is on the long rod at a distance r from the pivot. A spring with constant k connects the mass to the pivot. The diagram is labeled '(top view)'.

### 6.27. Coffee cup and mass \*\*

A coffee cup of mass  $M$  is connected to a mass  $m$  by a string. The coffee cup hangs over a frictionless pulley of negligible size, and the mass  $m$  is initially held with the string horizontal, as shown in Fig. 6.28. The mass  $m$  is then released. Find the equations of motion for  $r$  (the length of string between  $m$  and the pulley) and  $\theta$  (the angle that the string to  $m$  makes with the horizontal). Assume that  $m$  somehow doesn't run into the string holding the cup up.

Fig. 6.28

The coffee cup will initially fall, but it turns out that it will reach a lowest point and then rise back up. Write a program (see Section 1.4) that numerically determines the ratio of the  $r$  at this lowest point to the  $r$  at the start, for a given value of  $m/M$ . (To check your program, a value of  $m/M = 1/10$  yields a ratio of about 0.208.)

![Diagram of a mass m on a rotating T-shaped rod in a vertical plane. The T is pivoted at the origin and rotates with angular frequency omega. The mass m is on the long rod at a distance r from the pivot. A spring with constant k connects the mass to the pivot. The diagram is labeled '(top view)'.](794689ce0551f777555db0c997afe924_img.jpg)

Diagram of a mass m on a rotating T-shaped rod in a vertical plane. The T is pivoted at the origin and rotates with angular frequency omega. The mass m is on the long rod at a distance r from the pivot. A spring with constant k connects the mass to the pivot. The diagram is labeled '(top view)'.

### 6.28. Three falling sticks \*\*\*

Three massless sticks of length  $2r$ , each with a mass  $m$  fixed at its middle, are hinged at their ends, as shown in Fig. 6.29. The bottom end of the lower stick is hinged at the ground. They are held such that the lower two sticks are vertical, and the upper one is tilted at a small angle  $\epsilon$  with respect to the vertical. They are then released. At this instant, what are the angular accelerations of the three sticks? Work

Fig. 6.29

in the approximation where  $\epsilon$  is very small. (You may want to look at Problem 6.2 first.)

### 6.29. Cycloidal pendulum \*\*\*\*

The standard pendulum frequency of  $\sqrt{g/\ell}$  holds only for small oscillations. The frequency becomes smaller as the amplitude grows. It turns out that if you want to build a pendulum whose frequency is independent of the amplitude, you should hang it from the cusp of a cycloid of a certain size, as shown in Fig. 6.30. As the string wraps partially around the cycloid, the effect is to decrease the length of string in the air, which in turn increases the frequency back up to a constant value. In more detail:

A cycloid is the path taken by a point on the rim of a rolling wheel. The upside-down cycloid in Fig. 6.30 can be parametrized by  $(x, y) = R(\theta - \sin \theta, -1 + \cos \theta)$ , where  $\theta = 0$  corresponds to the cusp. Consider a pendulum of length  $4R$  hanging from the cusp, and let  $\alpha$  be the angle the string makes with the vertical, as shown.

![Diagram of a cycloidal pendulum. A shaded region represents an inverted cycloid curve. A string is suspended from the cusp (the top point) of the cycloid. The string wraps around the curve and ends in a bob. A dashed vertical line passes through the cusp. The angle alpha is shown between this vertical line and the straight portion of the string.](889c1787a4ae8030bd9d7956976117d2_img.jpg)

Diagram of a cycloidal pendulum. A shaded region represents an inverted cycloid curve. A string is suspended from the cusp (the top point) of the cycloid. The string wraps around the curve and ends in a bob. A dashed vertical line passes through the cusp. The angle alpha is shown between this vertical line and the straight portion of the string.

Fig. 6.30

- In terms of  $\alpha$ , find the value of the parameter  $\theta$  associated with the point where the string leaves the cycloid.
- In terms of  $\alpha$ , find the length of string touching the cycloid.
- In terms of  $\alpha$ , find the Lagrangian.
- Show that the quantity  $\sin \alpha$  undergoes simple harmonic motion with frequency  $\sqrt{g/4R}$ , independent of the amplitude.
- In place of parts (c) and (d), solve the problem again by using  $F = ma$ . This actually gives a much quicker solution.

## Section 6.2: The principle of stationary action

### 6.30. Dropped ball \*

Consider the action, from  $t = 0$  to  $t = 1$ , of a ball dropped from rest. From the E–L equation (or from  $F = ma$ ), we know that  $y(t) = -gt^2/2$  yields a stationary value of the action. Show explicitly that the particular function  $y(t) = -gt^2/2 + \epsilon t(t-1)$  yields an action that has no first-order dependence on  $\epsilon$ .

### 6.31. Explicit minimization \*

For a ball thrown upward, guess a solution for  $y$  of the form  $y(t) = a_2 t^2 + a_1 t + a_0$ . Assuming that  $y(0) = y(T) = 0$ , this quickly becomes  $y(t) = a_2(t^2 - Tt)$ . Calculate the action between  $t = 0$  and  $t = T$ , and show that it is minimized when  $a_2 = -g/2$ .

### 6.32. Always a minimum \*

For a ball thrown up in the air, show that the stationary value of the action is always a global minimum.

### **6.33. Second-order change \***

Let  $x_a(t) \equiv x_0(t) + a\beta(t)$ . Equation (6.19) gives the first derivative of the action with respect to  $a$ . Show that the second derivative is

$$\frac{d^2}{da^2}S[x_a(t)] = \int_{t_1}^{t_2} \left( \frac{\partial^2 L}{\partial x^2} \beta^2 + 2 \frac{\partial^2 L}{\partial x \partial \dot{x}} \beta \dot{\beta} + \frac{\partial^2 L}{\partial \dot{x}^2} \dot{\beta}^2 \right) dt. \quad (6.96)$$

### **6.34. $\ddot{x}$ dependence \***

Assume that there is  $\ddot{x}$  dependence (in addition to  $x, \dot{x}, t$  dependence) in the Lagrangian in Theorem 6.1. There will then be the additional term  $(\partial L / \partial \ddot{x}_a) \ddot{\beta}$  in Eq. (6.19). It is tempting to integrate this term by parts twice, and then arrive at a modified form of Eq. (6.22):

$$\frac{\partial L}{\partial x_0} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}_0} \right) + \frac{d^2}{dt^2} \left( \frac{\partial L}{\partial \ddot{x}_0} \right) = 0. \quad (6.97)$$

Is this a valid result? If not, where is the error in the reasoning?

## *Section 6.3: Forces of constraint*

### **6.35. Constraint on a circle \***

A bead of mass  $m$  slides with speed  $v$  around a horizontal hoop of radius  $R$ . What force does the hoop apply to the bead? (Ignore gravity.)

### **6.36. Atwood's machine \***

Consider the standard Atwood's machine in Fig. 6.31, with masses  $m_1$  and  $m_2$ . Find the tension in the string.

![Diagram of an Atwood's machine. A pulley is suspended from a horizontal ceiling. A string passes over the pulley, with a mass m1 hanging on the left side and a mass m2 hanging on the right side.](470af8d47fdf2fb2656725aaf59cd740_img.jpg)

Diagram of an Atwood's machine. A pulley is suspended from a horizontal ceiling. A string passes over the pulley, with a mass m1 hanging on the left side and a mass m2 hanging on the right side.

**Fig. 6.31**

### **6.37. Cartesian coordinates \*\***

In Eq. (6.35), take two time derivatives of the  $\sqrt{x^2 + y^2} - R = 0$  equation to obtain

$$R^2(x\ddot{x} + y\ddot{y}) + (x\dot{y} - y\dot{x})^2 = 0, \quad (6.98)$$

and then combine this with the other two equations to solve for  $F$  in terms of  $x, y, \dot{x}, \dot{y}$ . Convert the result to polar coordinates (with  $\theta$  measured from the vertical) and show that it agrees with Eq. (6.32).

### **6.38. Constraint on a curve \*\*\***

Let the horizontal plane be the  $x$ - $y$  plane. A bead of mass  $m$  slides with speed  $v$  along a curve described by the function  $y = f(x)$ . What force does the curve apply to the bead? (Ignore gravity.)

### Section 6.5: Conservation laws

#### 6.39. Bead on stick, using $F = ma$ \*

After doing Problem 6.8, show again that the quantity  $E$  is conserved, but now use  $F = ma$ . Do this in two ways:

- Use the first of Eqs. (3.51). *Hint:* multiply through by  $\dot{r}$ .
- Use the second of Eqs. (3.51) to calculate the work done on the bead, and use the work–energy theorem.

![Diagram of an Atwood's machine. A fixed pulley is attached to a ceiling. A rope passes over it, with a 4m mass on the left. The right end of the rope is attached to a movable pulley. A 5m mass hangs from the left side of the movable pulley at height x, and a 3m mass hangs from the right side at height y.](c728819b43076c4b4da830407da37686_img.jpg)

Diagram of an Atwood's machine. A fixed pulley is attached to a ceiling. A rope passes over it, with a 4m mass on the left. The right end of the rope is attached to a movable pulley. A 5m mass hangs from the left side of the movable pulley at height x, and a 3m mass hangs from the right side at height y.

Fig. 6.32

### Section 6.6: Noether's theorem

### 6.40. Atwood's machine \*\*

Consider the Atwood's machine shown in Fig. 6.32. The masses are  $4m$ ,  $5m$ , and  $3m$ . Let  $x$  and  $y$  be the heights of the right two masses, relative to their initial positions. Use Noether's theorem to find the conserved momentum. (The solution to Problem 6.9 gives some other methods, too.)

### Section 6.7: Small oscillations

### 6.41. Spring and a wheel \*

The top of a wheel of mass  $M$  and radius  $R$  is connected to a spring (at its equilibrium length) with spring constant  $k$ , as shown in Fig. 6.33. Assume that all the mass of the wheel is at its center. If the wheel rolls without slipping, what is the frequency of (small) oscillations?

![Diagram of a wheel of mass M and radius R on a horizontal surface. A spring with constant k is attached to a vertical wall on the left and to the top of the wheel.](f0d4d78be51fec610647e311faf950cc_img.jpg)

Diagram of a wheel of mass M and radius R on a horizontal surface. A spring with constant k is attached to a vertical wall on the left and to the top of the wheel.

Fig. 6.33

### 6.42. Spring on a spoke \*\*

A spring with spring constant  $k$  and relaxed length zero lies along a spoke of a massless wheel of radius  $R$ . One end of the spring is attached to the center, and the other end is attached to a mass  $m$  that is free to slide along the spoke. When the system is in its equilibrium position with the spring hanging vertically, how far (in terms of  $R$ ) should the mass hang down (you are free to adjust  $k$ ) so that for small oscillations, the frequency of the spring oscillations equals the frequency of the rocking motion of the wheel? Assume that the wheel rolls without slipping.

![Diagram of a massless hoop of radius R. Two equal masses are attached to the hoop at angles theta from the vertical dashed line. The angle between the two masses is 2*theta.](5d8c299ab0b9add88b585b9efa877b22_img.jpg)

Diagram of a massless hoop of radius R. Two equal masses are attached to the hoop at angles theta from the vertical dashed line. The angle between the two masses is 2\*theta.

Fig. 6.34

#### 6.43. Oscillating hoop \*\*

Two equal masses are glued to a massless hoop of radius  $R$  that is free to rotate about its center in a vertical plane. The angle between the masses is  $2\theta$ , as shown in Fig. 6.34. Find the frequency of small oscillations.

#### 6.44. Oscillating hoop with a pendulum \*\*\*

A massless hoop of radius  $R$  is free to rotate about its center in a vertical plane. A mass  $m$  is attached at one point, and a pendulum of length  $\sqrt{2}R$

(and also of mass  $m$ ) is attached at another point  $90^\circ$  away, as shown in Fig. 6.35. Let  $\theta$  be the angle of the hoop relative to the position shown, and let  $\alpha$  be the angle of the pendulum with respect to the vertical. Find the normal modes for small oscillations.

#### **6.45. Mass sliding on a rim \*\***

A mass  $m$  is free to slide frictionlessly along the rim of a wheel of radius  $R$  that rolls without slipping on the ground. The wheel is massless, except for a mass  $M$  located at its center. Find the normal modes for small oscillations.

#### **6.46. Mass sliding on a rim, with a spring \*\*\***

Consider the setup in the previous exercise, but now let the mass  $m$  be attached to a spring with spring constant  $k$  and relaxed length zero, the other end of which is attached to a point on the rim. Assume that the spring is constrained to run along the rim, and assume that the mass can pass freely over the point where the spring is attached to the rim. To keep things from getting too messy here, you can set  $M = m$ .

- Find the frequencies of the normal modes for small oscillations. Check the  $g = 0$  limit, and (if you've done the previous exercise) the  $k = 0$  limit.
- For the special case where  $g/R = k/m$ , show that the frequencies can be written as  $\sqrt{k/m}(\sqrt{5} \pm 1)/2$ . This numerical factor is the golden ratio (and its inverse). Describe what the normal modes look like.

#### **6.47. Vertically rotating hoop \*\*\***

A bead is free to slide along a frictionless hoop of radius  $r$ . The plane of the hoop is vertical, and the center of the hoop travels in a vertical circle of radius  $R$  with constant angular speed  $\omega$  about a given point (see Fig. 6.36). Find the equation of motion for the angle  $\theta$  shown. For large  $\omega$  (which implies small  $\theta$ ), find the amplitude of the “particular” solution with frequency  $\omega$ . What happens if  $r = R$ ?

![Diagram for Fig. 6.35: A wheel of radius R rolls on a horizontal surface. A mass m is attached to the rim at a point 45 degrees from the vertical. A pendulum of length sqrt(2)R is suspended from the same point, with a mass m at its end. The angle theta is measured from the vertical to the line connecting the center to the mass on the rim, and alpha is the angle of the pendulum from the vertical.](e9acb7bc2bb278dd2a22e64e1e2d8abb_img.jpg)

Diagram for Fig. 6.35: A wheel of radius R rolls on a horizontal surface. A mass m is attached to the rim at a point 45 degrees from the vertical. A pendulum of length sqrt(2)R is suspended from the same point, with a mass m at its end. The angle theta is measured from the vertical to the line connecting the center to the mass on the rim, and alpha is the angle of the pendulum from the vertical.

Fig. 6.35

![Diagram for Fig. 6.36: A side view of a hoop of radius r. The center of the hoop is moving in a vertical circle of radius R with constant angular speed omega. A bead is on the hoop at an angle theta from the vertical. The center of the hoop is at a distance R from the pivot point.](b624c76153dd34832626e5ca7f59dd78_img.jpg)

Diagram for Fig. 6.36: A side view of a hoop of radius r. The center of the hoop is moving in a vertical circle of radius R with constant angular speed omega. A bead is on the hoop at an angle theta from the vertical. The center of the hoop is at a distance R from the pivot point.

Fig. 6.36

### 6.11 Solutions

#### 6.1. Moving plane

Let  $x_1$  be the horizontal coordinate of the plane (with positive  $x_1$  to the left), and let  $x_2$  be the horizontal coordinate of the block (with positive  $x_2$  to the right); see Fig. 6.37. The relative horizontal distance between the plane and the block is  $x_1 + x_2$ , so the height fallen by the block is  $(x_1 + x_2) \tan \theta$ . The Lagrangian is therefore

$$L = \frac{1}{2}M\dot{x}_1^2 + \frac{1}{2}m(\dot{x}_2^2 + (\dot{x}_1 + \dot{x}_2)^2 \tan^2 \theta) + mg(x_1 + x_2) \tan \theta. \quad (6.99)$$

![Diagram for Fig. 6.37: A block of mass m on a wedge of mass M. The wedge is on a horizontal surface and has an angle theta. The horizontal coordinate of the wedge is x1 (positive to the left) and the horizontal coordinate of the block is x2 (positive to the right).](f08008d762d2aba1df73a18ead9c57dc_img.jpg)

Diagram for Fig. 6.37: A block of mass m on a wedge of mass M. The wedge is on a horizontal surface and has an angle theta. The horizontal coordinate of the wedge is x1 (positive to the left) and the horizontal coordinate of the block is x2 (positive to the right).

Fig. 6.37

![Diagram of two falling sticks. A bottom stick of length r and mass m is pivoted at its base on a horizontal surface, making an angle theta_1 with the vertical. A top stick of length r and mass m is pivoted at its base to the top of the bottom stick, making an angle theta_2 with the vertical. Dashed lines indicate the vertical positions.](042b341b9ea96d1923e04e5f93b48846_img.jpg)

Diagram of two falling sticks. A bottom stick of length r and mass m is pivoted at its base on a horizontal surface, making an angle theta\_1 with the vertical. A top stick of length r and mass m is pivoted at its base to the top of the bottom stick, making an angle theta\_2 with the vertical. Dashed lines indicate the vertical positions.

Fig. 6.38

The equations of motion obtained from varying  $x_1$  and  $x_2$  are

$$\begin{aligned} M\ddot{x}_1 + m(\ddot{x}_1 + \ddot{x}_2) \tan^2 \theta &= mg \tan \theta, \\ m\ddot{x}_2 + m(\ddot{x}_1 + \ddot{x}_2) \tan^2 \theta &= mg \tan \theta. \end{aligned} \quad (6.100)$$

Note that the difference of these two equations immediately yields conservation of momentum,  $M\ddot{x}_1 - m\ddot{x}_2 = 0 \implies (d/dt)(M\dot{x}_1 - m\dot{x}_2) = 0$ . Equations (6.100) are two linear equations in the two unknowns,  $\ddot{x}_1$  and  $\ddot{x}_2$ , so we can solve for  $\ddot{x}_1$ . After a little simplification, we arrive at

$$\ddot{x}_1 = \frac{mg \sin \theta \cos \theta}{M + m \sin^2 \theta}. \quad (6.101)$$

For some limiting cases, see the remarks in the solution to Problem 3.8.

#### 6.2. Two falling sticks

Let  $\theta_1(t)$  and  $\theta_2(t)$  be defined as in Fig. 6.38. Then the position of the bottom mass in Cartesian coordinates is  $(r \sin \theta_1, r \cos \theta_1)$ , and the position of the top mass is  $(2r \sin \theta_1 - r \sin \theta_2, 2r \cos \theta_1 + r \cos \theta_2)$ . So the potential energy of the system is

$$V(\theta_1, \theta_2) = mgr(3 \cos \theta_1 + \cos \theta_2). \quad (6.102)$$

The kinetic energy is somewhat more complicated. The kinetic energy of the bottom mass is simply  $mr^2 \dot{\theta}_1^2 / 2$ . Taking the derivative of the top mass's position given above, we find that the kinetic energy of the top mass is

$$\frac{1}{2}mr^2 \left( (2 \cos \theta_1 \dot{\theta}_1 - \cos \theta_2 \dot{\theta}_2)^2 + (-2 \sin \theta_1 \dot{\theta}_1 - \sin \theta_2 \dot{\theta}_2)^2 \right). \quad (6.103)$$

We can simplify this, using the small-angle approximations. The terms involving  $\sin \theta$  are fourth order in the small  $\theta$ 's, so we can neglect them. Also, we can approximate  $\cos \theta$  by 1, because this entails dropping only terms of at least fourth order. So the top mass's kinetic energy becomes  $(1/2)mr^2(2\dot{\theta}_1 - \dot{\theta}_2)^2$ . In retrospect, it would have been easier to obtain the kinetic energies of the masses by first applying the small-angle approximations to the positions, and then taking the derivatives to obtain the velocities. This strategy shows that both masses move essentially horizontally (initially). You will probably want to use this strategy when solving Exercise 6.28.

Using the small-angle approximation  $\cos \theta \approx 1 - \theta^2/2$  to rewrite the potential energy in Eq. (6.102), we have

$$L \approx \frac{1}{2}mr^2 \left( 5\dot{\theta}_1^2 - 4\dot{\theta}_1\dot{\theta}_2 + \dot{\theta}_2^2 \right) - mgr \left( 4 - \frac{3}{2}\theta_1^2 - \frac{1}{2}\theta_2^2 \right). \quad (6.104)$$

The equations of motion obtained from varying  $\theta_1$  and  $\theta_2$  are, respectively,

$$\begin{aligned} 5\ddot{\theta}_1 - 2\ddot{\theta}_2 &= \frac{3g}{r}\theta_1 \\ -2\ddot{\theta}_1 + \ddot{\theta}_2 &= \frac{g}{r}\theta_2. \end{aligned} \quad (6.105)$$

At the instant the sticks are released, we have  $\theta_1 = 0$  and  $\theta_2 = \epsilon$ . Solving Eq. (6.105) for  $\ddot{\theta}_1$  and  $\ddot{\theta}_2$  gives

$$\ddot{\theta}_1 = \frac{2g\epsilon}{r}, \quad \text{and} \quad \ddot{\theta}_2 = \frac{5g\epsilon}{r}. \quad (6.106)$$

### 6.3. Pendulum with an oscillating support

Let  $\theta$  be defined as in Fig. 6.39. With  $x(t) = A \cos(\omega t)$ , the position of the mass  $m$  is given by

$$(X, Y)_m = (x + \ell \sin \theta, -\ell \cos \theta). \quad (6.107)$$

![Diagram of a pendulum with an oscillating support. A mass m is suspended by a rod of length l from a support that moves horizontally with displacement x(t). The angle theta is measured from the vertical dashed line.](1a2d2ccc937208acaf2f1df390a17023_img.jpg)

Diagram of a pendulum with an oscillating support. A mass m is suspended by a rod of length l from a support that moves horizontally with displacement x(t). The angle theta is measured from the vertical dashed line.

Fig. 6.39

Taking the derivative to obtain the velocity, we find that the square of the speed is

$$V_m^2 = \dot{X}^2 + \dot{Y}^2 = \ell^2 \dot{\theta}^2 + \dot{x}^2 + 2\ell\dot{x}\dot{\theta} \cos \theta, \quad (6.108)$$

which also follows from applying the law of cosines to the horizontal  $\dot{x}$  and tangential  $\ell\dot{\theta}$  parts of the velocity vector. The Lagrangian is therefore

$$L = \frac{1}{2}m(\ell^2 \dot{\theta}^2 + \dot{x}^2 + 2\ell\dot{x}\dot{\theta} \cos \theta) + mg\ell \cos \theta. \quad (6.109)$$

The equation of motion for  $\theta$  is

$$\begin{aligned} \frac{d}{dt}(m\ell^2 \dot{\theta} + m\ell\dot{x} \cos \theta) &= -m\ell\dot{x}\dot{\theta} \sin \theta - mg\ell \sin \theta \\ \implies \ell\ddot{\theta} + \ddot{x} \cos \theta &= -g \sin \theta. \end{aligned} \quad (6.110)$$

Plugging in the explicit form of  $x(t)$ , we have

$$\ell\ddot{\theta} - A\omega^2 \cos(\omega t) \cos \theta + g \sin \theta = 0. \quad (6.111)$$

In retrospect, this makes sense. Someone in the reference frame of the support, which has horizontal acceleration  $\ddot{x} = -A\omega^2 \cos(\omega t)$ , may as well be living in a world where the acceleration from gravity has a component  $g$  downward and a component  $A\omega^2 \cos(\omega t)$  to the right. Equation (6.111) is just the  $F = ma$  equation in the tangential direction in this accelerating world.

A small-angle approximation in Eq. (6.111) gives

$$\ddot{\theta} + \omega_0^2 \theta = a\omega^2 \cos(\omega t), \quad (6.112)$$

where  $\omega_0 \equiv \sqrt{g/\ell}$  and  $a \equiv A/\ell$ . This equation is simply the equation for a driven oscillator, which we solved in Chapter 4. The solution is

$$\theta(t) = \frac{a\omega^2}{\omega_0^2 - \omega^2} \cos(\omega t) + C \cos(\omega_0 t + \phi), \quad (6.113)$$

where  $C$  and  $\phi$  are determined by the initial conditions.

If  $\omega$  happens to equal  $\omega_0$ , then it appears that the amplitude goes to infinity. However, as soon as the amplitude becomes large, our small-angle approximation breaks down, and Eqs. (6.112) and (6.113) are no longer valid.

### 6.4. Two masses, one swinging

The Lagrangian is

$$L = \frac{1}{2}m\dot{r}^2 + \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2) - mgr + mgr \cos \theta. \quad (6.114)$$

The last two terms are the (negatives of the) potentials of each mass, relative to where they would be if the right mass were located at the right pulley. The equations of motion obtained from varying  $r$  and  $\theta$  are

$$\begin{aligned} 2\ddot{r} &= r\dot{\theta}^2 - g(1 - \cos \theta), \\ \frac{d}{dt}(r^2\dot{\theta}) &= -gr \sin \theta. \end{aligned} \quad (6.115)$$

The first equation deals with the forces and accelerations along the direction of the string. The second equation equates the torque from gravity with the change in angular momentum of the right mass. If we do a (coarse) small-angle approximation and keep only terms up to first order in  $\theta$ , we find that at  $t = 0$  (using the initial condition,  $\dot{r} = 0$ ), Eqs. (6.115) become

$$\begin{aligned} \ddot{r} &= 0, \\ \ddot{\theta} + \frac{g}{r}\theta &= 0. \end{aligned} \quad (6.116)$$

These equations say that the left mass stays still, and the right mass behaves just like a pendulum.

If we want to find the leading term in the initial acceleration of the left mass (that is, the leading term in  $\ddot{r}$ ), we need to be a little less coarse in our approximation. So let's keep terms in Eq. (6.115) up to second order in  $\theta$ . We then have at  $t = 0$  (using the initial condition,  $\dot{r} = 0$ )

$$\begin{aligned} 2\ddot{r} &= r\dot{\theta}^2 - \frac{1}{2}g\theta^2, \\ \ddot{\theta} + \frac{g}{r}\theta &= 0. \end{aligned} \quad (6.117)$$

The second equation still says that the right mass undergoes harmonic motion. We are told that the amplitude is  $\epsilon$ , so we have

$$\theta(t) = \epsilon \cos(\omega t + \phi), \quad (6.118)$$

where  $\omega = \sqrt{g/r}$ . Plugging this into the first equation gives

$$2\ddot{r} = \epsilon^2 g \left( \sin^2(\omega t + \phi) - \frac{1}{2} \cos^2(\omega t + \phi) \right). \quad (6.119)$$

If we average this over a few periods, both  $\sin^2\alpha$  and  $\cos^2\alpha$  average to 1/2, so we find

$$\ddot{r}_{\text{avg}} = \frac{\epsilon^2 g}{8}. \quad (6.120)$$

This is a small second-order effect. It is positive, so the left mass slowly begins to climb.

### 6.5. Inverted pendulum

Let  $\theta$  be defined as in Fig. 6.40. With  $y(t) = A \cos(\omega t)$ , the position of the mass  $m$  is given by

$$(X, Y) = (\ell \sin \theta, y + \ell \cos \theta). \quad (6.121)$$

Taking the derivative to obtain the velocity, we find that the square of the speed is

$$V^2 = \dot{X}^2 + \dot{Y}^2 = \ell^2 \dot{\theta}^2 + \dot{y}^2 - 2\ell\dot{y}\dot{\theta} \sin \theta, \quad (6.122)$$

which also follows from applying the law of cosines to the vertical  $\dot{y}$  and tangential  $\ell\dot{\theta}$  parts of the velocity vector. The Lagrangian is therefore

$$L = \frac{1}{2}m(\ell^2 \dot{\theta}^2 + \dot{y}^2 - 2\ell\dot{y}\dot{\theta} \sin \theta) - mg(y + \ell \cos \theta). \quad (6.123)$$

The equation of motion for  $\theta$  is

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\theta}} \right) = \frac{\partial L}{\partial \theta} \implies \ell \ddot{\theta} - \ddot{y} \sin \theta = g \sin \theta. \quad (6.124)$$

Plugging in the explicit form of  $y(t)$ , we have

$$\ell \ddot{\theta} + \sin \theta (A\omega^2 \cos(\omega t) - g) = 0. \quad (6.125)$$

In retrospect, this makes sense. Someone in the reference frame of the support, which has vertical acceleration  $\ddot{y} = -A\omega^2 \cos(\omega t)$ , may as well be living in a world where the acceleration from gravity is  $g - A\omega^2 \cos(\omega t)$  downward. Equation (6.125) is just the  $F = ma$  equation in the tangential direction in this accelerating world.

Assuming  $\theta$  is small, we may set  $\sin \theta \approx \theta$ , which gives

$$\ddot{\theta} + \theta (a\omega^2 \cos(\omega t) - \omega_0^2) = 0, \quad (6.126)$$

![Diagram of an inverted pendulum. A mass m is attached to a pivot point by a rod of length l. The pivot point is on a support that is accelerating vertically with acceleration y(t). The angle theta is measured from the vertical dashed line to the rod.](eb35b9fe7320ab32449a4c8e99846850_img.jpg)

Diagram of an inverted pendulum. A mass m is attached to a pivot point by a rod of length l. The pivot point is on a support that is accelerating vertically with acceleration y(t). The angle theta is measured from the vertical dashed line to the rod.

Fig. 6.40

![Figure 6.41: Two plots of theta versus time t. The left plot shows theta increasing from 0.1 to 1.75 over t from 0 to 1.4. The right plot shows theta oscillating between approximately -0.1 and 0.1 over t from 0 to 1.4.](520ef5703bf11fe98816e1a70ec3b647_img.jpg)

Figure 6.41 consists of two side-by-side plots of  $\theta$  versus  $t$ . The left plot shows  $\theta$  on the vertical axis (ranging from 0.25 to 1.75) and  $t$  on the horizontal axis (ranging from 0.2 to 1.4). The curve starts at  $\theta \approx 0.1$  and increases monotonically, becoming steeper as  $t$  increases. The right plot shows  $\theta$  on the vertical axis (ranging from -0.1 to 0.1) and  $t$  on the horizontal axis (ranging from 0.2 to 1.4). The curve oscillates around  $\theta = 0$ , starting at  $\theta \approx 0.1$ , reaching a minimum of  $\theta \approx -0.1$  at  $t \approx 0.5$ , and returning to  $\theta \approx 0.1$  at  $t \approx 1.0$ .

Figure 6.41: Two plots of theta versus time t. The left plot shows theta increasing from 0.1 to 1.75 over t from 0 to 1.4. The right plot shows theta oscillating between approximately -0.1 and 0.1 over t from 0 to 1.4.

Fig. 6.41

![Figure 6.42: Two plots of theta versus time t. The left plot shows theta oscillating between -0.1 and 0.1 over t from 0 to 8. The right plot is a zoomed-in view of the first 0.1 seconds, showing high-frequency oscillations between 0.098 and 0.0995.](b880fd5022731a5c27945df98faa4184_img.jpg)

Figure 6.42 consists of two side-by-side plots of  $\theta$  versus  $t$ . The left plot shows  $\theta$  on the vertical axis (ranging from -0.1 to 0.1) and  $t$  on the horizontal axis (ranging from 0 to 8). The curve oscillates sinusoidally between  $\theta \approx 0.1$  and  $\theta \approx -0.1$ . The right plot is a zoomed-in view of the first 0.1 seconds, showing  $\theta$  on the vertical axis (ranging from 0.098 to 0.0995) and  $t$  on the horizontal axis (ranging from 0 to 0.1). The curve shows high-frequency oscillations between approximately 0.098 and 0.0995.

Figure 6.42: Two plots of theta versus time t. The left plot shows theta oscillating between -0.1 and 0.1 over t from 0 to 8. The right plot is a zoomed-in view of the first 0.1 seconds, showing high-frequency oscillations between 0.098 and 0.0995.

Fig. 6.42

where  $\omega_0 \equiv \sqrt{g/\ell}$  and  $a \equiv A/\ell$ . Equation (6.126) cannot be solved exactly, but we can still get a good idea of how  $\theta$  depends on time. We can do this both numerically and (approximately) analytically.

Figure 6.41 shows how  $\theta$  depends on time for parameters with values  $\ell = 1$  m,  $A = 0.1$  m, and  $g = 10$  m/s<sup>2</sup>. So  $a = 0.1$ , and  $\omega_0^2 = 10$  s<sup>-2</sup>. We produced these plots numerically using Eq. (6.126), with the initial conditions of  $\theta(0) = 0.1$  and  $\dot{\theta}(0) = 0$ . In the first plot,  $\omega = 10$  s<sup>-1</sup>. And in the second plot,  $\omega = 100$  s<sup>-1</sup>. The stick falls over in first case, but it undergoes oscillatory motion in the second case. Apparently, if  $\omega$  is large enough the stick won't fall over.

Let's now explain this phenomenon analytically. At first glance, it's rather surprising that the stick stays up. It seems like the average (over a few periods of the  $\omega$  oscillations) of the tangential acceleration in Eq. (6.126), namely  $-\theta(a\omega^2 \cos(\omega t) - \omega_0^2)$ , equals the positive quantity  $\theta\omega_0^2$ , because the  $\cos(\omega t)$  term averages to zero (or so it appears). So you might think that there is a net force making  $\theta$  increase, causing the stick to fall over.

The error in this reasoning is that the average of the  $-a\omega^2\theta \cos(\omega t)$  term is *not* zero, because  $\theta$  undergoes tiny oscillations with frequency  $\omega$ , as seen in the second plot in Fig. 6.42. Both of these plots have  $a = 0.005$ ,  $\omega_0^2 = 10$  s<sup>-2</sup>, and  $\omega = 1000$  s<sup>-1</sup> (we'll work with small  $a$  and large  $\omega$  from now on; more on this below). The second plot is a zoomed-in version of the first one near  $t = 0$ . The important point here is that the tiny oscillations in  $\theta$  shown in the second plot are correlated with  $\cos(\omega t)$ . It turns out that the  $\theta$  value at the  $t$  where  $\cos(\omega t) = 1$  is larger than the  $\theta$  value at the  $t$  where  $\cos(\omega t) = -1$ . So there is a net negative contribution to the  $-a\omega^2\theta \cos(\omega t)$  part of the acceleration. And it may indeed be large enough to keep the pendulum up, as we will now show.

To get a handle on the  $-a\omega^2\theta \cos(\omega t)$  term, let's work in the approximation where  $\omega$  is large and  $a \equiv A/\ell$  is small. More precisely, we will assume  $a \ll 1$  and  $a\omega^2 \gg \omega_0^2$ , for reasons we will explain below. Look at one of the little oscillations in the second plot in Fig. 6.42. These oscillations have frequency  $\omega$ , because they are due to the

support moving up and down. When the support moves up,  $\theta$  increases; and when the support moves down,  $\theta$  decreases. Since the average position of the pendulum doesn't change much over one of these small periods, we can look for an approximate solution to Eq. (6.126) of the form

$$\theta(t) \approx C + b \cos(\omega t), \quad (6.127)$$

where  $b \ll C$ .  $C$  will change over time, but on the scale of  $1/\omega$  it is essentially constant, if  $a \equiv A/\ell$  is small enough. Plugging this guess for  $\theta$  into Eq. (6.126), and using  $a \ll 1$  and  $a\omega^2 \gg \omega_0^2$ , we find  $-b\omega^2 \cos(\omega t) + Ca\omega^2 \cos(\omega t) = 0$ , to leading order.<sup>13</sup> So we must have  $b = aC$ . Our approximate solution for  $\theta$  is therefore

$$\theta \approx C(1 + a \cos(\omega t)). \quad (6.128)$$

Let's now determine how  $C$  gradually changes with time. From Eq. (6.126), the average acceleration of  $\theta$ , over a period  $T = 2\pi/\omega$ , is

$$\begin{aligned} \bar{\ddot{\theta}} &= \overline{-\theta(a\omega^2 \cos(\omega t) - \omega_0^2)} \\ &\approx \overline{-C(1 + a \cos(\omega t))(a\omega^2 \cos(\omega t) - \omega_0^2)} \\ &= -C(a^2\omega^2 \overline{\cos^2(\omega t)} - \omega_0^2) \\ &= -C\left(\frac{a^2\omega^2}{2} - \omega_0^2\right) \\ &\equiv -C\Omega^2, \end{aligned} \quad (6.129)$$

where

$$\Omega = \sqrt{\frac{a^2\omega^2}{2} - \frac{g}{\ell}}. \quad (6.130)$$

But if we take two derivatives of Eq. (6.127), we see that  $\bar{\ddot{\theta}}$  simply equals  $\ddot{C}$ . Equating this value of  $\bar{\ddot{\theta}}$  with the one in Eq. (6.129) gives

$$\ddot{C}(t) + \Omega^2 C(t) \approx 0. \quad (6.131)$$

This equation describes nice simple-harmonic motion. Therefore,  $C$  oscillates sinusoidally with the frequency  $\Omega$  given in Eq. (6.130). This is the overall back and forth motion seen in the first plot in Fig. 6.42. Note that we must have  $a\omega > \sqrt{2}\omega_0$  if this frequency is to be real so that the pendulum stays up. Since we have assumed  $a \ll 1$ , we see that  $a^2\omega^2 > 2\omega_0^2$  implies  $a\omega^2 \gg \omega_0^2$ , which is consistent with our initial assumption above.

If  $a\omega \gg \omega_0$ , then Eq. (6.130) gives  $\Omega \approx a\omega/\sqrt{2}$ . This is the case if we change the setup and just have the pendulum lie flat on a horizontal table where the acceleration from gravity is zero. In this limit where  $g$  is irrelevant, dimensional analysis implies that the frequency of the  $C$  oscillations must be a multiple of  $\omega$ , because  $\omega$  is the only

<sup>13</sup> The reasons for the  $a \ll 1$  and  $a\omega^2 \gg \omega_0^2$  qualifications are the following. If  $a\omega^2 \gg \omega_0^2$ , then the  $a\omega^2 \cos(\omega t)$  term dominates the  $\omega_0^2$  term in Eq. (6.126). The one exception to this is when  $\cos(\omega t) \approx 0$ , but this occurs for a negligibly small amount of time if  $a\omega^2 \gg \omega_0^2$ . If  $a \ll 1$ , then we can legally ignore the  $\ddot{C}$  term when Eq. (6.127) is substituted into Eq. (6.126). This is true because we will find below in Eq. (6.129) that our assumptions lead to  $\ddot{C}$  being roughly proportional to  $C a^2 \omega^2$ . Since the other terms in Eq. (6.126) are proportional to  $Ca\omega^2$ , we need  $a \ll 1$  in order for the  $\ddot{C}$  term to be negligible. In short,  $a \ll 1$  is the condition under which  $C$  varies slowly on the time scale of  $1/\omega$ .

quantity in the problem with units of frequency. It just so happens that the multiple is  $a/\sqrt{2}$ .

As a double check that we haven't messed up somewhere, the  $\Omega$  value resulting from the parameters in Fig. 6.42 (namely  $a = 0.005$ ,  $\omega_0^2 = 10 \text{ s}^{-2}$ , and  $\omega = 1000 \text{ s}^{-1}$ ) is  $\Omega = \sqrt{25/2 - 10} = 1.58 \text{ s}^{-1}$ . This corresponds to a period of  $2\pi/\Omega \approx 3.97 \text{ s}$ . And indeed, from the first plot in the figure, the period looks to be about 4 s (or maybe a hair less). For more on the inverted pendulum, see Butikov (2001).

### **6.6. Minimum or saddle**

- (a) For the given  $\xi(t)$ , the integrand in Eq. (6.26) is symmetric around the midpoint, so we obtain

$$\Delta S = \int_0^{T/2} \left( m \left( \frac{\epsilon}{T} \right)^2 - k \left( \frac{\epsilon t}{T} \right)^2 \right) dt = \frac{m\epsilon^2}{2T} - \frac{k\epsilon^2 T}{24}. \quad (6.132)$$

This is negative if  $T > \sqrt{12m/k} \equiv 2\sqrt{3}/\omega$ . Since the period of the oscillation is  $\tau \equiv 2\pi/\omega$ , we see that  $T$  must be greater than  $(\sqrt{3}/\pi)\tau$  in order for  $\Delta S$  to be negative, assuming that we are using the given triangular function for  $\xi$ .

- (b) With  $\xi(t) = \epsilon \sin(\pi t/T)$ , the integrand in Eq. (6.26) becomes

$$\begin{aligned} \Delta S &= \frac{1}{2} \int_0^T \left( m \left( \frac{\epsilon\pi}{T} \cos(\pi t/T) \right)^2 - k \left( \epsilon \sin(\pi t/T) \right)^2 \right) dt. \\ &= \frac{m\epsilon^2\pi^2}{4T} - \frac{k\epsilon^2 T}{4}, \end{aligned} \quad (6.133)$$

where we have used the fact that the average value of  $\sin^2\theta$  and  $\cos^2\theta$  over half of a period is 1/2 (or you can just do the integrals). This result for  $\Delta S$  is negative if  $T > \pi\sqrt{m/k} \equiv \pi/\omega = \tau/2$ , where  $\tau$  is the period.

**REMARK:** It turns out that the  $\xi(t) \propto \sin(\pi t/T)$  function gives the best chance of making  $\Delta S$  negative. You can show this by invoking a theorem from Fourier analysis that says that any function satisfying  $\xi(0) = \xi(T) = 0$  can be written as the sum  $\xi(t) = \sum_1^\infty c_n \sin(n\pi t/T)$ , where the  $c_n$  are numerical coefficients. When this sum is plugged into Eq. (6.26), you can show that all the cross terms (terms involving two different values of  $n$ ) integrate to zero. Using the fact that the average value of  $\sin^2\theta$  and  $\cos^2\theta$  is 1/2, the rest of the integral yields

$$\Delta S = \frac{1}{4} \sum_1^\infty c_n^2 \left( \frac{m\pi^2 n^2}{T} - kT \right). \quad (6.134)$$

In order to obtain the smallest value of  $T$  that can make this sum negative, we want only the  $n = 1$  term to exist. We then have  $\xi(t) = c_1 \sin(\pi t/T)$ , and Eq. (6.134) reduces to Eq. (6.133), as it should.

As mentioned in Remark 4 in Section 6.2, it is always possible to make  $\Delta S$  positive by picking a  $\xi(t)$  function that is small but wiggles very fast. Therefore, we see that for a harmonic oscillator, if  $T > \tau/2$ , then the stationary value of  $S$  is a saddle point (some  $\xi$ 's make  $\Delta S$  positive, and some make it negative), but if  $T < \tau/2$ , then the stationary value of  $S$  is a minimum (all  $\xi$ 's make  $\Delta S$  positive). In the latter case, the point is that  $T$  is small enough so that there is no way for  $\xi$  to get large, without making  $\dot{\xi}$  large also. ♣

### **6.7. Normal force from a plane**

**FIRST SOLUTION:** The most convenient coordinates in this problem are  $w$  and  $z$ , where  $w$  is the distance upward along the plane, and  $z$  is the distance perpendicularly away from it. The Lagrangian is then

$$\frac{1}{2}m(\dot{w}^2 + \dot{z}^2) - mg(w \sin \theta + z \cos \theta) - V(z), \quad (6.135)$$

![Diagram of a mass m on an inclined plane at angle theta. A coordinate system (x, y) is shown with the origin at the top of the incline. The x-axis is horizontal and the y-axis is vertical. The incline is a line starting from the origin and going down to the right at an angle theta from the horizontal. The mass m is on the incline.](e1b95dda9d5b3ecc408b4dfc2e8fabef_img.jpg)

Diagram of a mass m on an inclined plane at angle theta. A coordinate system (x, y) is shown with the origin at the top of the incline. The x-axis is horizontal and the y-axis is vertical. The incline is a line starting from the origin and going down to the right at an angle theta from the horizontal. The mass m is on the incline.

Fig. 6.43

where  $V(z)$  is the (very steep) constraining potential. The two equations of motion are

$$m\ddot{w} = -mg \sin \theta,$$

$$m\ddot{z} = -mg \cos \theta - \frac{dV}{dz}. \quad (6.136)$$

At this point we invoke the constraint  $z = 0$ . So  $\ddot{z} = 0$ , and the second equation gives

$$F_c \equiv -V'(0) = mg \cos \theta, \quad (6.137)$$

as desired. We also obtain the usual result,  $\ddot{w} = -g \sin \theta$ .

**SECOND SOLUTION:** We can also solve this problem by using the horizontal and vertical coordinates,  $x$  and  $y$ . We'll choose  $(x, y) = (0, 0)$  to be at the top of the plane; see Fig. 6.43. The (very steep) constraining potential is  $V(z)$ , where  $z \equiv x \sin \theta + y \cos \theta$  is the distance from the mass to the plane (as you can verify). The Lagrangian is then

$$L = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2) - mgy - V(z). \quad (6.138)$$

Keeping in mind that  $z \equiv x \sin \theta + y \cos \theta$ , the two equations of motion are (using the chain rule)

$$m\ddot{x} = -\frac{dV}{dz} \frac{\partial z}{\partial x} = -V'(z) \sin \theta, \quad (6.139)$$

$$m\ddot{y} = -mg - \frac{dV}{dz} \frac{\partial z}{\partial y} = -mg - V'(z) \cos \theta.$$

At this point we invoke the constraint condition  $z = 0 \implies x = -y \cot \theta$ . This condition, along with the two E-L equations, allows us to solve for the three unknowns,  $\ddot{x}$ ,  $\ddot{y}$ , and  $V'(0)$ . Using  $\ddot{x} = -\ddot{y} \cot \theta$  in Eq. (6.139), we find

$$\ddot{x} = g \cos \theta \sin \theta, \quad \ddot{y} = -g \sin^2 \theta, \quad F_c \equiv -V'(0) = mg \cos \theta. \quad (6.140)$$

The first two results here are simply the horizontal and vertical components of the acceleration along the plane, which is  $g \sin \theta$ .

### 6.8. Bead on a stick

There is no potential energy here, so the Lagrangian consists of just the kinetic energy,  $T$ , which comes from the radial and tangential motions:

$$L = T = \frac{1}{2}m\dot{r}^2 + \frac{1}{2}mr^2\omega^2. \quad (6.141)$$

Equation (6.52) therefore gives

$$E = \frac{1}{2}m\dot{r}^2 - \frac{1}{2}mr^2\omega^2. \quad (6.142)$$

Claim 6.3 says that this quantity is conserved, because  $\partial L / \partial t = 0$ . But it is *not* the energy of the bead, due to the minus sign in the second term.

The point here is that in order to keep the stick rotating at a constant angular speed, there must be an external force acting on it. This force in turn causes work to be done on the bead, thereby increasing its kinetic energy. The kinetic energy  $T$  is therefore *not* conserved. From Eqs. (6.141) and (6.142), we see that  $E = T - mr^2\omega^2$  is the quantity that is constant in time. See Exercise 6.39 for some  $F = ma$  ways to show that the quantity  $E$  in Eq. (6.142) is conserved.

### 6.9. Atwood's machine

**FIRST SOLUTION:** If the left mass goes up by  $x$  and the right mass goes up by  $y$ , then conservation of string says that the middle mass must go down by  $x + y$ . Therefore, the Lagrangian of the system is

$$L = \frac{1}{2}(4m)\dot{x}^2 + \frac{1}{2}(3m)(-\dot{x} - \dot{y})^2 + \frac{1}{2}m\dot{y}^2 - \left( (4m)gx + (3m)g(-x - y) + mgy \right)$$

$$= \frac{7}{2}m\dot{x}^2 + 3m\dot{x}\dot{y} + 2m\dot{y}^2 - mg(x - 2y). \quad (6.143)$$

This is invariant under the transformation  $x \rightarrow x + 2\epsilon$  and  $y \rightarrow y + \epsilon$ . Hence, we can use Noether's theorem, with  $K_x = 2$  and  $K_y = 1$ . The conserved momentum is then

$$P = \frac{\partial L}{\partial \dot{x}} K_x + \frac{\partial L}{\partial \dot{y}} K_y = m(7\dot{x} + 3\dot{y})(2) + m(3\dot{x} + 4\dot{y})(1) = m(17\dot{x} + 10\dot{y}). \quad (6.144)$$

This  $P$  is constant. In particular, if the system starts at rest, then  $\dot{x}$  always equals  $-(10/17)\dot{y}$ .

SECOND SOLUTION: The Euler–Lagrange equations are, from Eq. (6.143),

$$\begin{aligned} 7m\ddot{x} + 3m\ddot{y} &= -mg, \\ 3m\ddot{x} + 4m\ddot{y} &= 2mg. \end{aligned} \quad (6.145)$$

Adding the second equation to twice the first gives

$$17m\ddot{x} + 10m\ddot{y} = 0 \implies \frac{d}{dt}(17m\dot{x} + 10m\dot{y}) = 0. \quad (6.146)$$

THIRD SOLUTION: We can also solve this problem using  $F = ma$ . Since the tension  $T$  is the same throughout the rope, we see that the three  $F = dP/dt$  equations are

$$2T - 4mg = \frac{dP_{4m}}{dt}, \quad 2T - 3mg = \frac{dP_{3m}}{dt}, \quad 2T - mg = \frac{dP_m}{dt}. \quad (6.147)$$

The three forces depend on only two quantities ( $T$  and  $mg$ ), so there must be some combination of them that adds up to zero. If we set  $a(2T - 4mg) + b(2T - 3mg) + c(2T - mg) = 0$ , then we have  $a + b + c = 0$  and  $4a + 3b + c = 0$ , which is satisfied by  $a = 2$ ,  $b = -3$ , and  $c = 1$ . Therefore,

$$\begin{aligned} 0 &= \frac{d}{dt}(2P_{4m} - 3P_{3m} + P_m) \\ &= \frac{d}{dt}(2(4m)\dot{x} - 3(3m)(-\dot{x} - \dot{y}) + m\dot{y}) \\ &= \frac{d}{dt}(17m\dot{x} + 10m\dot{y}). \end{aligned} \quad (6.148)$$

### 6.10. Hoop and pulley

Let the radius to  $M$  make an angle  $\theta$  with the vertical (see Fig. 6.44). Then the coordinates of  $M$  relative to the center of the hoop are  $R(\sin\theta, -\cos\theta)$ . The height of  $m$ , relative to its position when  $M$  is at the bottom of the hoop, is  $y = -R\theta$ . The Lagrangian is therefore (and yes, we've chosen a different  $y = 0$  reference point for each mass, but such a definition changes the potential only by a constant amount, which is irrelevant)

$$L = \frac{1}{2}(M + m)R^2\dot{\theta}^2 + MgR\cos\theta + mgR\theta. \quad (6.149)$$

The equation of motion is then

$$(M + m)R\ddot{\theta} = g(m - M\sin\theta). \quad (6.150)$$

This is just  $F = ma$  along the direction of the string (because  $Mg\sin\theta$  is the tangential component of the gravitational force on  $M$ ).

Equilibrium occurs when  $\dot{\theta} = \ddot{\theta} = 0$ . From Eq. (6.150), we see that this happens at  $\sin\theta_0 = m/M$ . Letting  $\theta \equiv \theta_0 + \delta$ , and expanding Eq. (6.150) to first order in  $\delta$ , gives

$$\ddot{\delta} + \left( \frac{Mg\cos\theta_0}{(M + m)R} \right) \delta = 0. \quad (6.151)$$

![Diagram of a hoop and pulley system. A large hoop of radius R is pivoted at its top point on a horizontal surface. A mass M is attached to the inner right side of the hoop. A string is attached to the top of the hoop, passes over a small pulley fixed to the ceiling, and then hangs vertically with a mass m attached to its end. The angle theta is measured from the vertical to the radius connecting the center of the hoop to mass M.](20cce98e06b356e38d3766269285b127_img.jpg)

Diagram of a hoop and pulley system. A large hoop of radius R is pivoted at its top point on a horizontal surface. A mass M is attached to the inner right side of the hoop. A string is attached to the top of the hoop, passes over a small pulley fixed to the ceiling, and then hangs vertically with a mass m attached to its end. The angle theta is measured from the vertical to the radius connecting the center of the hoop to mass M.

Fig. 6.44

The frequency of small oscillations is therefore

$$\omega = \sqrt{\frac{M \cos \theta_0}{M+m}} \sqrt{\frac{g}{R}} = \left( \frac{M-m}{M+m} \right)^{1/4} \sqrt{\frac{g}{R}}, \quad (6.152)$$

where we have used  $\cos \theta_0 = \sqrt{1 - \sin^2 \theta_0}$ .

**REMARKS:** If  $M \gg m$ , then  $\theta_0 \approx 0$ , and  $\omega \approx \sqrt{g/R}$ . This makes sense, because  $m$  can be ignored, so  $M$  essentially oscillates around the bottom of the hoop, just like a pendulum of length  $R$ .

If  $M$  is only slightly greater than  $m$ , then  $\theta_0 \approx \pi/2$ , and  $\omega \approx 0$ . This also makes sense, because if  $\theta \approx \pi/2$ , then the restoring force  $g(m - M \sin \theta)$  doesn't change much as  $\theta$  changes (the derivative of  $\sin \theta$  is zero at  $\theta = \pi/2$ ), so it's as if we have a pendulum in a very weak gravitational field.

We can actually derive the frequency in Eq. (6.152) without doing any calculations. Look at  $M$  at the equilibrium position. The tangential forces on it cancel, and the radially inward force from the hoop must be  $Mg \cos \theta_0$  to balance the radial outward component of the gravitational force. Therefore, for all the mass  $M$  knows, it is sitting at the bottom of a hoop of radius  $R$  in a world where gravity has strength  $g' = g \cos \theta_0$ . The general formula for the frequency of a pendulum (as you can quickly show) is  $\omega = \sqrt{F'/M'R}$ , where  $F'$  is the gravitational force (which is  $Mg'$  here), and  $M'$  is the total mass being accelerated (which is  $M+m$  here). This gives the  $\omega$  in Eq. (6.152). (This reasoning is a little subtle; food for thought.) ♣

### 6.11. Bead on a rotating hoop

Breaking the velocity up into the component along the hoop plus the component perpendicular to the hoop, we find

$$L = \frac{1}{2}m(\omega^2 R^2 \sin^2 \theta + R^2 \dot{\theta}^2) + mgR \cos \theta. \quad (6.153)$$

The equation of motion is then

$$R\ddot{\theta} = \sin \theta (\omega^2 R \cos \theta - g). \quad (6.154)$$

The  $F = ma$  interpretation of this is that the component of gravity pulling downward along the hoop accounts for the acceleration along the hoop plus the component of the centripetal acceleration along the hoop.

Equilibrium occurs when  $\dot{\theta} = \ddot{\theta} = 0$ . The right-hand side of Eq. (6.154) equals zero when either  $\sin \theta = 0$  (that is,  $\theta = 0$  or  $\theta = \pi$ ) or  $\cos \theta = g/(\omega^2 R)$ . Since  $\cos \theta$  must be less than or equal to 1, this second condition is possible only if  $\omega^2 \geq g/R$ . So we have two cases:

- If  $\omega^2 < g/R$ , then  $\theta = 0$  and  $\theta = \pi$  are the only equilibrium points.

The  $\theta = \pi$  case is unstable. This is fairly intuitive, but it can also be seen mathematically by letting  $\theta \equiv \pi + \delta$ , where  $\delta$  is small. Equation (6.154) then becomes

$$\ddot{\delta} - \delta(\omega^2 + g/R) = 0. \quad (6.155)$$

The coefficient of  $\delta$  is negative, so  $\delta$  undergoes exponential instead of oscillatory motion.

The  $\theta = 0$  case turns out to be stable. For small  $\theta$ , Eq. (6.154) becomes

$$\ddot{\theta} + \theta(g/R - \omega^2) = 0. \quad (6.156)$$

The coefficient of  $\theta$  is positive, so we have sinusoidal solutions. The frequency of small oscillations is  $\sqrt{g/R - \omega^2}$ . This goes to zero as  $\omega \rightarrow \sqrt{g/R}$ .

- If  $\omega^2 \geq g/R$ , then  $\theta = 0$ ,  $\theta = \pi$ , and  $\cos \theta_0 \equiv g/(\omega^2 R)$  are all equilibrium points. The  $\theta = \pi$  case is again unstable, by looking at Eq. (6.155). And the

$\theta = 0$  case is also unstable, because the coefficient of  $\theta$  in Eq. (6.156) is now negative (or zero, if  $\omega^2 = g/R$ ).

Therefore,  $\cos \theta_0 \equiv g/(\omega^2 R)$  is the only stable equilibrium. To find the frequency of small oscillations, let  $\theta \equiv \theta_0 + \delta$  in Eq. (6.154), and expand to first order in  $\delta$ . Using  $\cos \theta_0 \equiv g/(\omega^2 R)$ , we find

$$\ddot{\delta} + (\omega^2 \sin^2 \theta_0) \delta = 0. \quad (6.157)$$

The frequency of small oscillations is therefore  $\omega \sin \theta_0 = \sqrt{\omega^2 - g^2/\omega^2 R^2}$ .

The frequency  $\omega = \sqrt{g/R}$  is the critical frequency above which there is a stable equilibrium at  $\theta \neq 0$ , that is, above which the mass wants to move away from the bottom of the hoop.

REMARK: This frequency of small oscillations goes to zero as  $\omega \rightarrow \sqrt{g/R}$ . And it approximately equals  $\omega$  as  $\omega \rightarrow \infty$ . This second limit can be viewed in the following way. For very large  $\omega$ , gravity isn't important, and the bead feels a centripetal force (the normal force from the hoop) essentially equal to  $m\omega^2 R$  as it moves near  $\theta = \pi/2$ . So for all the bead knows, it is a pendulum of length  $R$  in a world where “gravity” pulls sideways with a force  $m\omega^2 R \equiv mg'$  (outward, so that it is approximately canceled by the inward-pointing normal force, just as the downward gravitational force is approximately canceled by the upward tension in a regular pendulum). The frequency of such a pendulum is  $\sqrt{g'/R} = \sqrt{\omega^2 R/R} = \omega$ . ♣

### 6.12. Another bead on a rotating hoop

With the angles  $\omega t$  and  $\theta$  defined as in Fig. 6.45, the Cartesian coordinates for the bead are

$$(x, y) = (R \cos \omega t + r \cos(\omega t + \theta), R \sin \omega t + r \sin(\omega t + \theta)). \quad (6.158)$$

The velocity is then

$$\begin{aligned} (x, y) &= (-\omega R \sin \omega t - r(\omega + \dot{\theta}) \sin(\omega t + \theta), \\ &\quad \omega R \cos \omega t + r(\omega + \dot{\theta}) \cos(\omega t + \theta)). \end{aligned} \quad (6.159)$$

The square of the speed is therefore

$$\begin{aligned} v^2 &= R^2 \omega^2 + r^2 (\omega + \dot{\theta})^2 \\ &\quad + 2Rr\omega(\omega + \dot{\theta})(\sin \omega t \sin(\omega t + \theta) + \cos \omega t \cos(\omega t + \theta)) \\ &= R^2 \omega^2 + r^2 (\omega + \dot{\theta})^2 + 2Rr\omega(\omega + \dot{\theta}) \cos \theta. \end{aligned} \quad (6.160)$$

This speed can also be obtained by using the law of cosines to add the velocity of the center of the hoop to the velocity of the bead with respect to the center (as you can show).

There is no potential energy, so the Lagrangian is simply  $L = mv^2/2$ . The equation of motion is then, as you can show,

$$r\ddot{\theta} + R\omega^2 \sin \theta = 0. \quad (6.161)$$

Equilibrium occurs when  $\dot{\theta} = \ddot{\theta} = 0$ , so Eq. (6.161) tells us that the equilibrium is located at  $\theta = 0$ , which makes intuitive sense. (Another solution is  $\theta = \pi$ , but that's an unstable equilibrium.) A small-angle approximation in Eq. (6.161) gives  $\ddot{\theta} + (R/r)\omega^2 \theta = 0$ , so the frequency of small oscillations is  $\Omega = \omega \sqrt{R/r}$ .

REMARKS: If  $R \ll r$ , then  $\Omega \approx 0$ . This makes sense, because the frictionless hoop is essentially not moving. If  $R = r$ , then  $\Omega = \omega$ . If  $R \gg r$ , then  $\Omega$  is very large. In this case, we can double-check the  $\Omega = \omega \sqrt{R/r}$  result in the following way. In

![Diagram of a bead on a rotating hoop (top view). A circular hoop of radius R is centered at the origin. A bead of mass m is located on the hoop at a distance r from the center. The angle between the horizontal dashed line and the line from the origin to the center of the hoop is labeled ωt. The angle between the line from the origin to the center of the hoop and the line from the center to the bead is labeled θ. A curved arrow indicates the rotation of the hoop with angular velocity ω.](12a6746dd149052b3ba5d45ac76c0cef_img.jpg)

Diagram of a bead on a rotating hoop (top view). A circular hoop of radius R is centered at the origin. A bead of mass m is located on the hoop at a distance r from the center. The angle between the horizontal dashed line and the line from the origin to the center of the hoop is labeled ωt. The angle between the line from the origin to the center of the hoop and the line from the center to the bead is labeled θ. A curved arrow indicates the rotation of the hoop with angular velocity ω.

Fig. 6.45

the accelerating frame of the hoop, the bead feels a centrifugal force (discussed in Chapter 10) of  $m(R+r)\omega^2$ . For all the bead knows, it is in a gravitational field with strength  $g' \equiv (R+r)\omega^2$ . So the bead (which acts like a pendulum of length  $r$ ), oscillates with a frequency equal to

$$\sqrt{\frac{g'}{r}} = \sqrt{\frac{(R+r)\omega^2}{r}} \approx \omega\sqrt{\frac{R}{r}} \quad (\text{for } R \gg r). \quad (6.162)$$

Note that if we try to use this “effective gravity” argument as a double check for smaller values of  $R$ , we get the wrong answer. For example, if  $R = r$ , we obtain an oscillation frequency of  $\omega\sqrt{2R/r}$ , instead of the correct value  $\omega\sqrt{R/r}$ . This is because in reality the centrifugal force fans out near the equilibrium point, while our “effective gravity” argument assumes that the field lines are parallel (and so it gives a frequency that is too large). ♣

![Diagram of a wheel of radius R on a horizontal surface. A bead of mass m is on the wheel at an angle theta from the vertical. The center of the wheel is labeled M. A dashed line connects the center M to the bead m, and another dashed line connects the center M to the point of contact with the ground. The angle theta is measured from the vertical dashed line to the line connecting M and m.](54828fa2c5632d22dcce4ccfd9fb4192_img.jpg)

Diagram of a wheel of radius R on a horizontal surface. A bead of mass m is on the wheel at an angle theta from the vertical. The center of the wheel is labeled M. A dashed line connects the center M to the bead m, and another dashed line connects the center M to the point of contact with the ground. The angle theta is measured from the vertical dashed line to the line connecting M and m.

Fig. 6.46

### 6.13. Mass on a wheel

Let the angle  $\theta$  be defined as in Fig. 6.46, with the convention that  $\theta$  is positive if  $M$  is to the right of  $m$ . Then the position of  $m$  in Cartesian coordinates, relative to the point where  $m$  would be in contact with the ground, is

$$(x, y)_m = R(\theta - \sin \theta, 1 - \cos \theta). \quad (6.163)$$

We have used the nonslipping condition to say that the present contact point is a distance  $R\theta$  to the right of where  $m$  would be in contact with the ground. Differentiating Eq. (6.163), we find that the square of  $m$ 's speed is  $v_m^2 = 2R^2\dot{\theta}^2(1 - \cos \theta)$ .

The position of  $M$  is  $(x, y)_M = R(\theta, 1)$ , so the square of its speed is  $v_M^2 = R^2\dot{\theta}^2$ . The Lagrangian is therefore

$$L = \frac{1}{2}MR^2\dot{\theta}^2 + mR^2\dot{\theta}^2(1 - \cos \theta) + mgR \cos \theta, \quad (6.164)$$

where we have measured both potential energies relative to the height of  $M$ . The equation of motion is

$$MR\ddot{\theta} + 2mR\ddot{\theta}(1 - \cos \theta) + mR\dot{\theta}^2 \sin \theta + mg \sin \theta = 0. \quad (6.165)$$

In the case of small oscillations, we can use  $\cos \theta \approx 1 - \theta^2/2$  and  $\sin \theta \approx \theta$ . The second and third terms in Eq. (6.165) are then third order in  $\theta$  and can be neglected (basically, the middle term in Eq. (6.164), which is the kinetic energy of  $m$ , is negligible), so we find

$$\ddot{\theta} + \left(\frac{mg}{MR}\right)\theta = 0. \quad (6.166)$$

The frequency of small oscillations is therefore

$$\omega = \sqrt{\frac{m}{M}}\sqrt{\frac{g}{R}}. \quad (6.167)$$

REMARKS: If  $M \gg m$ , then  $\omega \rightarrow 0$ . This makes sense. If  $m \gg M$ , then  $\omega \rightarrow \infty$ . This also makes sense, because the huge  $mg$  force makes the situation similar to one where the wheel is bolted to the ground, in which case the wheel vibrates with a high frequency.

Equation (6.167) can actually be derived in a much quicker way, using torque. For small oscillations, the gravitational force on  $m$  produces a torque of  $-mgR\theta$  around the contact point on the ground. For small  $\theta$ ,  $m$  has essentially no moment of inertia around the contact point, so the total moment of inertia is simply  $MR^2$ . Therefore,  $\tau = I\alpha$  gives  $-mgR\theta = MR^2\ddot{\theta}$ , from which the result follows. ♣

### 6.14. Pendulum with a free support

Let  $x$  be the coordinate of  $M$ , and let  $\theta$  be the angle of the pendulum (see Fig. 6.47). Then the position of the mass  $m$  in Cartesian coordinates is  $(x + \ell \sin \theta, -\ell \cos \theta)$ . Taking the derivative to find the velocity, and then squaring to find the speed, gives  $v_m^2 = \dot{x}^2 + \ell^2 \dot{\theta}^2 + 2\ell \dot{x} \dot{\theta} \cos \theta$ . The Lagrangian is therefore

$$L = \frac{1}{2} M \dot{x}^2 + \frac{1}{2} m (\dot{x}^2 + \ell^2 \dot{\theta}^2 + 2\ell \dot{x} \dot{\theta} \cos \theta) + mg\ell \cos \theta. \quad (6.168)$$

The equations of motion obtained from varying  $x$  and  $\theta$  are

$$\begin{aligned} (M+m)\ddot{x} + m\ell\ddot{\theta} \cos \theta - m\ell\dot{\theta}^2 \sin \theta &= 0, \\ \ell\ddot{\theta} + \ddot{x} \cos \theta + g \sin \theta &= 0. \end{aligned} \quad (6.169)$$

If  $\theta$  is small, we can use the small-angle approximations,  $\cos \theta \approx 1 - \theta^2/2$  and  $\sin \theta \approx \theta$ . Keeping only the terms that are first-order in  $\theta$ , we obtain

$$\begin{aligned} (M+m)\ddot{x} + m\ell\ddot{\theta} &= 0, \\ \ddot{x} + \ell\ddot{\theta} + g\theta &= 0. \end{aligned} \quad (6.170)$$

The first equation expresses momentum conservation. Integrating it twice gives

$$x = -\left(\frac{m\ell}{M+m}\right)\theta + At + B. \quad (6.171)$$

The second equation is  $F = ma$  in the tangential direction. Eliminating  $\ddot{x}$  from Eq. (6.170) gives

$$\ddot{\theta} + \left(\frac{M+m}{M}\right)\frac{g}{\ell}\theta = 0. \quad (6.172)$$

Therefore,  $\theta(t) = C \cos(\omega t + \phi)$ , where

$$\omega = \sqrt{1 + \frac{m}{M}} \sqrt{\frac{g}{\ell}}. \quad (6.173)$$

The general solutions for  $\theta$  and  $x$  are therefore

$$\theta(t) = C \cos(\omega t + \phi), \quad x(t) = -\frac{Cm\ell}{M+m} \cos(\omega t + \phi) + At + B. \quad (6.174)$$

The constant  $B$  is irrelevant, so we'll ignore it. The two normal modes are:

- $A = 0$ : In this case,  $x = -\theta m\ell/(M+m)$ . Both masses oscillate with the frequency  $\omega$  given in Eq. (6.173), always moving in opposite directions. The center of mass does not move (as you can verify).
- $C = 0$ : In this case,  $\theta = 0$  and  $x = At$ . The pendulum hangs vertically, with both masses moving horizontally at the same speed. The frequency of oscillations is zero in this mode.

REMARKS: If  $M \gg m$ , then  $\omega = \sqrt{g/\ell}$ , as expected, because the support essentially stays still.

If  $m \gg M$ , then  $\omega \rightarrow \sqrt{m/M} \sqrt{g/\ell} \rightarrow \infty$ . This makes sense, because the tension in the rod is very large. We can actually be quantitative about this limit. For small oscillations and for  $m \gg M$ , the tension of  $mg$  in the rod produces a sideways force of  $mg\theta$  on  $M$ . So the horizontal  $F = Ma$  equation for  $M$  is  $mg\theta = M\ddot{x}$ . But  $x \approx -\ell\theta$  in this limit, so we have  $mg\theta = -M\ell\ddot{\theta}$ , which gives the desired frequency. ♣

![Diagram of a pendulum with a free support. A block of mass M is on a horizontal surface, constrained to move horizontally by a spring or guide. A pendulum of length l and mass m is suspended from the block. The horizontal displacement of the block is x, and the angle of the pendulum from the vertical is theta.](0f75bd9a711223433b71ac5ae1a24a56_img.jpg)

Diagram of a pendulum with a free support. A block of mass M is on a horizontal surface, constrained to move horizontally by a spring or guide. A pendulum of length l and mass m is suspended from the block. The horizontal displacement of the block is x, and the angle of the pendulum from the vertical is theta.

Fig. 6.47

![Diagram of a pendulum support on an inclined plane. A block of mass M is on a plane inclined at angle beta. A pendulum of length l and mass m is suspended from M. The coordinate z is measured along the plane. The angle theta is measured from the vertical dashed line.](403e465e83656b58f6e922cbeab17817_img.jpg)

Diagram of a pendulum support on an inclined plane. A block of mass M is on a plane inclined at angle beta. A pendulum of length l and mass m is suspended from M. The coordinate z is measured along the plane. The angle theta is measured from the vertical dashed line.

Fig. 6.48

### 6.15. Pendulum support on an inclined plane

Let  $z$  be the coordinate of  $M$  along the plane, and let  $\theta$  be the angle of the pendulum (see Fig. 6.48). In Cartesian coordinates, the positions of  $M$  and  $m$  are

$$(x, y)_M = (z \cos \beta, -z \sin \beta), \quad (6.175)$$

$$(x, y)_m = (z \cos \beta + \ell \sin \theta, -z \sin \beta - \ell \cos \theta).$$

Differentiating these positions, we find that the squares of the speeds are

$$\begin{aligned} v_M^2 &= \dot{z}^2, \\ v_m^2 &= \dot{z}^2 + \ell^2 \dot{\theta}^2 + 2\ell \dot{z} \dot{\theta} (\cos \beta \cos \theta - \sin \beta \sin \theta). \end{aligned} \quad (6.176)$$

The Lagrangian is therefore

$$\frac{1}{2} M \dot{z}^2 + \frac{1}{2} m (\dot{z}^2 + \ell^2 \dot{\theta}^2 + 2\ell \dot{z} \dot{\theta} \cos(\theta + \beta)) + Mgz \sin \beta + mg(z \sin \beta + \ell \cos \theta). \quad (6.177)$$

The equations of motion obtained from varying  $z$  and  $\theta$  are

$$\begin{aligned} (M + m)\ddot{z} + m\ell(\ddot{\theta} \cos(\theta + \beta) - \dot{\theta}^2 \sin(\theta + \beta)) &= (M + m)g \sin \beta, \\ \ell \ddot{\theta} + \ddot{z} \cos(\theta + \beta) &= -g \sin \theta. \end{aligned} \quad (6.178)$$

Let us now consider small oscillations about the equilibrium point (where  $\ddot{\theta} = \dot{\theta} = 0$ ). We must first determine where this point is. The first equation above gives  $\ddot{z} = g \sin \beta$ . The second equation then gives  $g \sin \beta \cos(\theta + \beta) = -g \sin \theta$ . By expanding the cosine term, we find  $\tan \theta = -\tan \beta$ , so  $\theta = -\beta$ . ( $\theta = \pi - \beta$  is also a solution, but this is an unstable equilibrium.) The equilibrium position of the pendulum is therefore where the string is perpendicular to the plane.<sup>14</sup>

To find the normal modes and frequencies for small oscillations, let  $\theta \equiv -\beta + \delta$ , and expand Eq. (6.178) to first order in  $\delta$ . Letting  $\ddot{\eta} \equiv \ddot{z} - g \sin \beta$  for convenience, we obtain

$$\begin{aligned} (M + m)\ddot{\eta} + m\ell \ddot{\delta} &= 0, \\ \ddot{\eta} + \ell \ddot{\delta} + (g \cos \beta)\delta &= 0. \end{aligned} \quad (6.179)$$

Using the determinant method (or using the method in Problem 6.14; either way works), we find the frequencies of the normal modes to be

$$\omega_1 = 0, \quad \text{and} \quad \omega_2 = \sqrt{1 + \frac{m}{M}} \sqrt{\frac{g \cos \beta}{\ell}}. \quad (6.180)$$

These are the same as the frequencies in the previous problem (where  $M$  moves horizontally), but with  $g \cos \beta$  in place of  $g$ ; compare Eq. (6.179) with Eq. (6.170).<sup>15</sup> Looking at Eq. (6.174), and recalling the definition of  $\eta$ , we see that the general solutions for  $\theta$  and  $z$  are

$$\theta(t) = -\beta + C \cos(\omega t + \phi), \quad z(t) = -\frac{Cm\ell}{M+m} \cos(\omega t + \phi) + \frac{g \sin \beta}{2} t^2 + At + B. \quad (6.181)$$

<sup>14</sup> This makes sense. The tension in the string is perpendicular to the plane, so for all the pendulum bob knows, it may as well be sliding down a plane parallel to the given one, a distance  $\ell$  away. Given the same initial speed, the two masses slide down their two “planes” with equal speeds at all times.

<sup>15</sup> This makes sense, because in a frame that accelerates down the plane at  $g \sin \beta$ , the only external force on the masses is a gravitational force of  $g \cos \beta$  perpendicular to the plane. As far as  $M$  and  $m$  are concerned, they live in a world where gravity pulls “downward” (perpendicular to the plane) with strength  $g' = g \cos \beta$ .

The constant  $B$  is irrelevant, so we'll ignore it. The basic difference between these normal modes and the ones in the previous problem is the acceleration down the plane. If you go to a frame that accelerates down the plane at  $g \sin \beta$ , and if you tilt your head at an angle  $\beta$  and accept the fact that  $g' = g \cos \beta$  in your world, then the setup is identical to the one in the previous problem.

### 6.16. Tilting plane

Relative to the support, the positions of the masses are

$$\begin{aligned}(x, y)_M &= (\ell \sin \theta, -\ell \cos \theta), \\ (x, y)_m &= (\ell \sin \theta + x \cos \theta, -\ell \cos \theta + x \sin \theta).\end{aligned}\quad (6.182)$$

Differentiating these positions, we find that the squares of the speeds are

$$v_M^2 = \ell^2 \dot{\theta}^2, \quad v_m^2 = (\ell \dot{\theta} + \dot{x})^2 + x^2 \dot{\theta}^2. \quad (6.183)$$

You can also obtain  $v_m^2$  by noting that  $(\ell \dot{\theta} + \dot{x})$  is the speed along the long rod, and  $x \dot{\theta}$  is the speed perpendicular to it. The Lagrangian is

$$L = \frac{1}{2} M \ell^2 \dot{\theta}^2 + \frac{1}{2} m ((\ell \dot{\theta} + \dot{x})^2 + x^2 \dot{\theta}^2) + Mg\ell \cos \theta + mg(\ell \cos \theta - x \sin \theta). \quad (6.184)$$

The equations of motion obtained from varying  $x$  and  $\theta$  are

$$\begin{aligned}\ell \ddot{\theta} + \ddot{x} &= x \dot{\theta}^2 - g \sin \theta, \\ M \ell^2 \ddot{\theta} + m \ell (\ell \ddot{\theta} + \ddot{x}) + m x^2 \ddot{\theta} + 2 m x \dot{x} \dot{\theta} &= -(M + m) g \ell \sin \theta - m g x \cos \theta.\end{aligned}\quad (6.185)$$

Let us now consider the case where both  $x$  and  $\theta$  are small (or more precisely,  $\theta \ll 1$  and  $x/\ell \ll 1$ ). Expanding Eq. (6.185) to first order in  $\theta$  and  $x/\ell$  gives

$$\begin{aligned}(\ell \ddot{\theta} + \ddot{x}) + g \theta &= 0, \\ M \ell (\ell \ddot{\theta} + g \theta) + m \ell (\ell \ddot{\theta} + \ddot{x}) + m g \ell \theta + m g x &= 0.\end{aligned}\quad (6.186)$$

We can simplify these a bit. Using the first equation to substitute  $-g\theta$  for  $(\ell \ddot{\theta} + \ddot{x})$ , and also  $-\ddot{x}$  for  $(\ell \ddot{\theta} + g\theta)$ , in the second equation gives

$$\begin{aligned}\ell \ddot{\theta} + \ddot{x} + g \theta &= 0, \\ -M \ell \ddot{x} + m g x &= 0.\end{aligned}\quad (6.187)$$

The normal modes can be found using the determinant method, or we can find them just by inspection. The second equation says that either  $x(t) \equiv 0$ , or  $x(t) = A \cosh(\alpha t + \beta)$ , where  $\alpha = \sqrt{mg/M\ell}$ . So we have two cases:

- If  $x(t) = 0$ , then the first equation in (6.187) says that the normal mode is

$$\begin{pmatrix} \theta \\ x \end{pmatrix} = B \begin{pmatrix} 1 \\ 0 \end{pmatrix} \cos(\omega t + \phi), \quad (6.188)$$

where  $\omega \equiv \sqrt{g/\ell}$ . This mode is fairly clear. With the proper initial conditions,  $m$  will stay right where  $M$  is. The normal force from the long rod will be exactly what is needed in order for  $m$  to undergo the same oscillatory motion as  $M$ . The two masses may as well be two pendulums of length  $\ell$  swinging side by side.

- If  $x(t) = A \cosh(\alpha t + \beta)$ , then the first equation in (6.187) can be solved (by guessing a particular solution for  $\theta$  of the same form) to give the normal mode,

$$\begin{pmatrix} \theta \\ x \end{pmatrix} = C \begin{pmatrix} -m \\ \ell(M + m) \end{pmatrix} \cosh(\alpha t + \beta), \quad (6.189)$$

where  $\alpha = \sqrt{mg/M\ell}$ . This mode is not as clear. And indeed, its range of validity is rather limited. The exponential behavior will quickly make  $x$  and  $\theta$  large, and

thus outside the validity of our small-variable approximations. You can show that in this mode the center of mass remains directly below the pivot. This can occur, for example, by having  $m$  move down to the right as the rods rotate and swing  $M$  up to the left. There is no oscillation in this mode; the positions keep growing. The CM falls, to provide for the increasing kinetic energy.

### 6.17. Rotating curve

The speed along the curve is  $\dot{x}\sqrt{1+y'^2}$ , and the speed perpendicular to the curve is  $\omega x$ . So the Lagrangian is

$$L = \frac{1}{2}m\left(\omega^2 x^2 + \dot{x}^2(1+y'^2)\right) - mgy, \quad (6.190)$$

where  $y(x) = b(x/a)^\lambda$ . The equation of motion is then

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}}\right) = \frac{\partial L}{\partial x} \implies \ddot{x}(1+y'^2) + \dot{x}^2 y' y'' = \omega^2 x - gy'. \quad (6.191)$$

Equilibrium occurs when  $\dot{x} = \ddot{x} = 0$ , so Eq. (6.191) says that the equilibrium value of  $x$  satisfies

$$x_0 = \frac{gy'(x_0)}{\omega^2}. \quad (6.192)$$

The  $F = ma$  explanation for this (writing  $y'(x_0)$  as  $\tan \theta$ , where  $\theta$  is the angle of the curve, and then multiplying through by  $\omega^2 \cos \theta$ ) is that the component of gravity along the curve accounts for the component of the centripetal acceleration along the curve. Using  $y(x) = b(x/a)^\lambda$ , Eq. (6.192) yields

$$x_0 = a \left( \frac{a^2 \omega^2}{\lambda g b} \right)^{1/(\lambda-2)}. \quad (6.193)$$

As  $\lambda \rightarrow \infty$ , we see that  $x_0$  goes to  $a$ . This makes sense, because the curve essentially equals zero up to  $a$ , and then it rises very steeply. You can check numerous other limits. Letting  $x \equiv x_0 + \delta$  in Eq. (6.191), and expanding to first order in  $\delta$ , gives

$$\ddot{\delta} \left(1 + y'(x_0)^2\right) = \delta \left(\omega^2 - gy''(x_0)\right). \quad (6.194)$$

The frequency of small oscillations is therefore given by

$$\Omega^2 = \frac{gy''(x_0) - \omega^2}{1 + y'(x_0)^2}. \quad (6.195)$$

Using the explicit form of  $y$ , along with Eq. (6.193), we find

$$\Omega^2 = \frac{(\lambda - 2)\omega^2}{1 + \frac{a^2 \omega^4}{g^2} \left( \frac{a^2 \omega^2}{\lambda g b} \right)^{2/(\lambda-2)}}. \quad (6.196)$$

We see that  $\lambda$  must be greater than 2 in order for there to be oscillatory motion around the equilibrium point. For  $\lambda < 2$ , the equilibrium point is unstable, that is, to the left the force is inward, and to the right the force is outward.

For the case  $\lambda = 2$ , we have  $y(x) = b(x/a)^2$ , so the equilibrium condition, Eq. (6.192), gives  $x_0 = (2gb/a^2\omega^2)x_0$ . For this to be true for some  $x_0$ , we must have  $\omega^2 = 2gb/a^2$ . But if this holds, then Eq. (6.192) is true for all  $x$ . So in the special case of  $\lambda = 2$ , the bead happily sits anywhere on the curve if  $\omega^2 = 2gb/a^2$ . (In the rotating frame of the curve, the tangential components of the centrifugal and gravitational forces exactly cancel at all points.) If  $\lambda = 2$  and  $\omega^2 \neq 2gb/a^2$ , then the particle feels a force either always inward or always outward.

**REMARKS:** For  $\omega \rightarrow 0$ , Eqs. (6.193) and (6.196) give  $x_0 \rightarrow 0$  and  $\Omega \rightarrow 0$ . And for  $\omega \rightarrow \infty$ , they give  $x_0 \rightarrow \infty$  and  $\Omega \rightarrow 0$ . In both cases  $\Omega \rightarrow 0$ , because in both

cases the equilibrium position is at a place where the curve is very flat (horizontally or vertically, respectively), and the restoring force ends up being small.

For  $\lambda \rightarrow \infty$ , we have  $x_0 \rightarrow a$  and  $\Omega \rightarrow \infty$ . The frequency is large here because the equilibrium position at  $a$  is where the curve has a sharp corner, so the restoring force changes quickly with position. Or, you can think of it as a pendulum with a very small length, if you approximate the “corner” by a tiny circle. ♣

### 6.18. Motion in a cone

If the particle’s distance from the axis is  $r$ , then its height is  $r/\tan\alpha$ , and its distance up along the cone is  $r/\sin\alpha$ . Breaking the velocity into components up along the cone and around the cone, we see that the square of the speed is  $v^2 = \dot{r}^2/\sin^2\alpha + r^2\dot{\theta}^2$ . The Lagrangian is therefore

$$L = \frac{1}{2}m\left(\frac{\dot{r}^2}{\sin^2\alpha} + r^2\dot{\theta}^2\right) - \frac{mgr}{\tan\alpha}. \quad (6.197)$$

The equations of motion obtained from varying  $\theta$  and  $r$  are

$$\begin{aligned} \frac{d}{dt}(mr^2\dot{\theta}) &= 0 \\ \ddot{r} &= r\dot{\theta}^2\sin^2\alpha - g\cos\alpha\sin\alpha. \end{aligned} \quad (6.198)$$

The first of these equations expresses conservation of angular momentum. The second equation is more transparent if we divide through by  $\sin\alpha$ . With  $x \equiv r/\sin\alpha$  being the distance up along the cone, we have  $\ddot{x} = (r\dot{\theta}^2)\sin\alpha - g\cos\alpha$ . This is the  $F = ma$  statement for the diagonal  $x$  direction.

Letting  $mr^2\dot{\theta} \equiv L$ , we can eliminate  $\dot{\theta}$  from the second equation to obtain

$$\ddot{r} = \frac{L^2\sin^2\alpha}{m^2r^3} - g\cos\alpha\sin\alpha. \quad (6.199)$$

We will now calculate the two desired frequencies.

- Frequency of circular oscillations,  $\omega$ : For circular motion with  $r = r_0$ , we have  $\dot{r} = \ddot{r} = 0$ , so the second of Eqs. (6.198) gives

$$\omega \equiv \dot{\theta} = \sqrt{\frac{g}{r_0\tan\alpha}}. \quad (6.200)$$

- Frequency of oscillations about a circle,  $\Omega$ : If the orbit were actually the circle  $r = r_0$ , then Eq. (6.199) would give (with  $\ddot{r} = 0$ )

$$\frac{L^2\sin^2\alpha}{m^2r_0^3} = g\cos\alpha\sin\alpha. \quad (6.201)$$

This is equivalent to Eq. (6.200), which can be seen by writing  $L$  as  $mr_0^2\dot{\theta}$ .

We will now use our standard procedure of letting  $r(t) = r_0 + \delta(t)$ , where  $\delta(t)$  is very small, and then plugging this into Eq. (6.199) and expanding to first order in  $\delta$ . Using

$$\frac{1}{(r_0 + \delta)^3} \approx \frac{1}{r_0^3 + 3r_0^2\delta} = \frac{1}{r_0^3(1 + 3\delta/r_0)} \approx \frac{1}{r_0^3}\left(1 - \frac{3\delta}{r_0}\right), \quad (6.202)$$

we have

$$\ddot{\delta} = \frac{L^2\sin^2\alpha}{m^2r_0^3}\left(1 - \frac{3\delta}{r_0}\right) - g\cos\alpha\sin\alpha. \quad (6.203)$$

Recalling Eq. (6.201), the terms not involving  $\delta$  cancel, and we are left with

$$\ddot{\delta} = -\left(\frac{3L^2\sin^2\alpha}{m^2r_0^4}\right)\delta. \quad (6.204)$$

Using Eq. (6.201) again to eliminate  $L$  we have

$$\ddot{\delta} + \left( \frac{3g}{r_0} \sin \alpha \cos \alpha \right) \delta = 0. \quad (6.205)$$

Therefore,

$$\Omega = \sqrt{\frac{3g}{r_0} \sin \alpha \cos \alpha}. \quad (6.206)$$

Having found the two desired frequencies in Eqs. (6.200) and (6.206), we see that their ratio is

$$\frac{\Omega}{\omega} = \sqrt{3} \sin \alpha. \quad (6.207)$$

This ratio  $\Omega/\omega$  is independent of  $r_0$ . The two frequencies are equal if  $\sin \alpha = 1/\sqrt{3}$ , that is, if  $\alpha \approx 35.3^\circ \equiv \tilde{\alpha}$ . If  $\alpha = \tilde{\alpha}$ , then after one revolution around the cone,  $r$  returns to the value it had at the beginning of the revolution. So the particle undergoes periodic motion.

**REMARKS:** In the limit  $\alpha \rightarrow 0$  (that is, the cone is very thin), Eq. (6.207) says that  $\Omega/\omega \rightarrow 0$ . In fact, Eqs. (6.200) and (6.206) say that  $\omega \rightarrow \infty$  and  $\Omega \rightarrow 0$ . So the particle spirals around many times during one complete  $r$  cycle. This seems intuitive.

In the limit  $\alpha \rightarrow \pi/2$  (that is, the cone is almost a flat plane), both  $\omega$  and  $\Omega$  go to zero, and Eq. (6.207) says that  $\Omega/\omega \rightarrow \sqrt{3}$ . This result is not at all obvious.

If  $\Omega/\omega = \sqrt{3} \sin \alpha$  is a rational number, then the particle undergoes periodic motion. For example, if  $\alpha = 60^\circ$ , then  $\Omega/\omega = 3/2$ , so it takes two complete circles for  $r$  to go through three cycles. Or, if  $\alpha = \arcsin(1/2\sqrt{3}) \approx 16.8^\circ$ , then  $\Omega/\omega = 1/2$ , so it takes two complete circles for  $r$  to go through one cycle. ♣

![Diagram of a double pendulum. A pivot point is at the top. A first rod of length l1 is suspended from the pivot, making an angle theta1 with the vertical. A second rod of length l2 is suspended from the end of the first rod, making an angle theta2 with the vertical. The masses are m1 and m2.](288f1b558decac194e9c6c95257d10bb_img.jpg)

Diagram of a double pendulum. A pivot point is at the top. A first rod of length l1 is suspended from the pivot, making an angle theta1 with the vertical. A second rod of length l2 is suspended from the end of the first rod, making an angle theta2 with the vertical. The masses are m1 and m2.

**Fig. 6.49**

### 6.19. Double pendulum

Relative to the pivot point, the Cartesian coordinates of  $m_1$  and  $m_2$  are, respectively (see Fig. 6.49),

$$\begin{aligned} (x, y)_1 &= (\ell_1 \sin \theta_1, -\ell_1 \cos \theta_1), \\ (x, y)_2 &= (\ell_1 \sin \theta_1 + \ell_2 \sin \theta_2, -\ell_1 \cos \theta_1 - \ell_2 \cos \theta_2). \end{aligned} \quad (6.208)$$

Taking the derivative to find the velocities, and then squaring, gives

$$\begin{aligned} v_1^2 &= \ell_1^2 \dot{\theta}_1^2, \\ v_2^2 &= \ell_1^2 \dot{\theta}_1^2 + \ell_2^2 \dot{\theta}_2^2 + 2\ell_1 \ell_2 \dot{\theta}_1 \dot{\theta}_2 (\cos \theta_1 \cos \theta_2 + \sin \theta_1 \sin \theta_2). \end{aligned} \quad (6.209)$$

The Lagrangian is therefore

$$\begin{aligned} L &= \frac{1}{2} m_1 \ell_1^2 \dot{\theta}_1^2 + \frac{1}{2} m_2 (\ell_1^2 \dot{\theta}_1^2 + \ell_2^2 \dot{\theta}_2^2 + 2\ell_1 \ell_2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2)) \\ &\quad + m_1 g \ell_1 \cos \theta_1 + m_2 g (\ell_1 \cos \theta_1 + \ell_2 \cos \theta_2). \end{aligned} \quad (6.210)$$

The equations of motion obtained from varying  $\theta_1$  and  $\theta_2$  are

$$\begin{aligned} 0 &= (m_1 + m_2) \ell_1^2 \ddot{\theta}_1 + m_2 \ell_1 \ell_2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 \ell_1 \ell_2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) \\ &\quad + (m_1 + m_2) g \ell_1 \sin \theta_1, \\ 0 &= m_2 \ell_2^2 \ddot{\theta}_2 + m_2 \ell_1 \ell_2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 \ell_1 \ell_2 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) \\ &\quad + m_2 g \ell_2 \sin \theta_2. \end{aligned} \quad (6.211)$$

This is a bit of a mess, but it simplifies greatly if we consider small oscillations. Using the small-angle approximations and keeping only the leading-order terms, we obtain

$$\begin{aligned} 0 &= (m_1 + m_2)\ell_1\ddot{\theta}_1 + m_2\ell_2\ddot{\theta}_2 + (m_1 + m_2)g\theta_1, \\ 0 &= \ell_2\ddot{\theta}_2 + \ell_1\ddot{\theta}_1 + g\theta_2. \end{aligned} \quad (6.212)$$

Consider now the special case,  $\ell_1 = \ell_2 \equiv \ell$ . We can find the frequencies of the normal modes by using the determinant method, discussed in Section 4.5. You can show that the result is

$$\omega_{\pm} = \sqrt{\frac{m_1 + m_2 \pm \sqrt{m_1 m_2 + m_2^2}}{m_1}} \sqrt{\frac{g}{\ell}}. \quad (6.213)$$

The normal modes turn out to be, after some simplification,

$$\begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_{\pm} \propto \begin{pmatrix} \mp\sqrt{m_2} \\ \sqrt{m_1 + m_2} \end{pmatrix} \cos(\omega_{\pm}t + \phi_{\pm}). \quad (6.214)$$

Some special cases are:

- $m_1 = m_2$ : The frequencies are

$$\omega_{\pm} = \sqrt{2 \pm \sqrt{2}} \sqrt{\frac{g}{\ell}}. \quad (6.215)$$

The normal modes are

$$\begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_{\pm} \propto \begin{pmatrix} \mp 1 \\ \sqrt{2} \end{pmatrix} \cos(\omega_{\pm}t + \phi_{\pm}). \quad (6.216)$$

- $m_1 \gg m_2$ : With  $m_2/m_1 \equiv \epsilon$ , the frequencies are (to leading nontrivial order in  $\epsilon$ )

$$\omega_{\pm} = (1 \pm \sqrt{\epsilon}/2) \sqrt{\frac{g}{\ell}}. \quad (6.217)$$

The normal modes are

$$\begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_{\pm} \propto \begin{pmatrix} \mp\sqrt{\epsilon} \\ 1 \end{pmatrix} \cos(\omega_{\pm}t + \phi_{\pm}). \quad (6.218)$$

In both modes, the upper (heavy) mass essentially stands still, and the lower (light) mass oscillates like a pendulum of length  $\ell$ .

- $m_1 \ll m_2$ : With  $m_1/m_2 \equiv \epsilon$ , the frequencies are (to leading order in  $\epsilon$ )

$$\omega_+ = \sqrt{\frac{2g}{\epsilon\ell}}, \quad \omega_- = \sqrt{\frac{g}{2\ell}}. \quad (6.219)$$

The normal modes are

$$\begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_{\pm} \propto \begin{pmatrix} \mp 1 \\ 1 \end{pmatrix} \cos(\omega_{\pm}t + \phi_{\pm}). \quad (6.220)$$

In the first mode, the lower (heavy) mass essentially stands still (from the  $x_2$  in Eq. (6.208)), and the upper (light) mass vibrates back and forth at a high frequency (because there is a very large tension in the rods). In the second mode, the rods form a straight line, and the system is essentially a pendulum of length  $2\ell$ .

Consider now the special case,  $m_1 = m_2$ . Using the determinant method, you can show that the frequencies of the normal modes are

$$\omega_{\pm} = \sqrt{g} \sqrt{\frac{\ell_1 + \ell_2 \pm \sqrt{\ell_1^2 + \ell_2^2}}{\ell_1 \ell_2}}. \quad (6.221)$$

The normal modes turn out to be, after some simplification,

$$\begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_{\pm} \propto \begin{pmatrix} \ell_2 \\ \ell_2 - \ell_1 \mp \sqrt{\ell_1^2 + \ell_2^2} \end{pmatrix} \cos(\omega_{\pm} t + \phi_{\pm}). \quad (6.222)$$

Some special cases are:

- $\ell_1 = \ell_2$ : We already considered this case above. You can show that Eqs. (6.221) and (6.222) agree with Eqs. (6.215) and (6.216), respectively.
- $\ell_1 \gg \ell_2$ : With  $\ell_2/\ell_1 \equiv \epsilon$ , the frequencies are (to leading order in  $\epsilon$ )

$$\omega_+ = \sqrt{\frac{2g}{\ell_2}}, \quad \omega_- = \sqrt{\frac{g}{\ell_1}}. \quad (6.223)$$

The normal modes are

$$\begin{aligned} \begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_+ &\propto \begin{pmatrix} -\epsilon \\ 2 \end{pmatrix} \cos(\omega_+ t + \phi_+), \\ \begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_- &\propto \begin{pmatrix} 1 \\ 1 \end{pmatrix} \cos(\omega_- t + \phi_-). \end{aligned} \quad (6.224)$$

In the first mode, the masses essentially move equal distances in opposite directions, at a high frequency (assuming  $\ell_2$  is small). The factor of 2 in the frequency arises because the angle of  $\ell_2$  is twice what it would be if  $m_1$  were bolted in place; so  $m_2$  feels double the tangential force. In the second mode, the rods form a straight line, and the masses move just like a mass of  $2m$ . The system is essentially a pendulum of length  $\ell_1$ .

- $\ell_1 \ll \ell_2$ : With  $\ell_1/\ell_2 \equiv \epsilon$ , the frequencies are (to leading order in  $\epsilon$ )

$$\omega_+ = \sqrt{\frac{2g}{\ell_1}}, \quad \omega_- = \sqrt{\frac{g}{\ell_2}}. \quad (6.225)$$

The normal modes are

$$\begin{aligned} \begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_+ &\propto \begin{pmatrix} 1 \\ -\epsilon \end{pmatrix} \cos(\omega_+ t + \phi_+), \\ \begin{pmatrix} \theta_1(t) \\ \theta_2(t) \end{pmatrix}_- &\propto \begin{pmatrix} 1 \\ 2 \end{pmatrix} \cos(\omega_- t + \phi_-). \end{aligned} \quad (6.226)$$

In the first mode, the bottom mass essentially stands still, and the top mass oscillates at a high frequency (assuming  $\ell_1$  is small). The factor of 2 in the frequency arises because the top mass essentially lives in a world where the acceleration from gravity is  $g' = 2g$  (because of the extra  $mg$  force downward from the lower mass). In the second mode, the system is essentially a pendulum of length  $\ell_2$ . The factor of 2 in the angles is what is needed to make the tangential force on the top mass roughly equal to zero (because otherwise it would oscillate at a high frequency, since  $\ell_1$  is small).

### **6.20. Shortest distance in a plane**

Let the two given points be  $(x_1, y_1)$  and  $(x_2, y_2)$ , and let the path be described by the function  $y(x)$ . (Yes, we'll assume it can be written as a function. Locally, we don't have to worry about any double-valued issues.) Then the length of the path is

$$\ell = \int_{x_1}^{x_2} \sqrt{1 + y'^2} dx. \quad (6.227)$$

The “Lagrangian” is  $L = \sqrt{1 + y'^2}$ , so the Euler–Lagrange equation is

$$\frac{d}{dx} \left( \frac{\partial L}{\partial y'} \right) = \frac{\partial L}{\partial y} \implies \frac{d}{dx} \left( \frac{y'}{\sqrt{1 + y'^2}} \right) = 0. \quad (6.228)$$

We see that  $y'/\sqrt{1 + y'^2}$  is constant. Therefore,  $y'$  is also constant, so we have a straight line,  $y(x) = Ax + B$ , where  $A$  and  $B$  are determined by the endpoint conditions.

### **6.21. Index of refraction**

Let the path be described by  $y(x)$ . The speed at height  $y$  is  $v \propto y$ . Therefore, the time to go from  $(x_1, y_1)$  to  $(x_2, y_2)$  is

$$T = \int_{x_1}^{x_2} \frac{ds}{v} \propto \int_{x_1}^{x_2} \frac{\sqrt{1 + y'^2}}{y} dx. \quad (6.229)$$

The “Lagrangian” is therefore

$$L \propto \frac{\sqrt{1 + y'^2}}{y}. \quad (6.230)$$

At this point, we could apply the E–L equation to this  $L$ , but let's just use Lemma 6.5, with  $f(y) = 1/y$ . Equation (6.86) gives

$$1 + y'^2 = Bf(y)^2 \implies 1 + y'^2 = \frac{B}{y^2}. \quad (6.231)$$

We must now integrate this. Solving for  $y'$ , and then separating variables and integrating, gives

$$\int dx = \pm \int \frac{y dy}{\sqrt{B - y^2}} \implies x + A = \mp \sqrt{B - y^2}. \quad (6.232)$$

Therefore,  $(x + A)^2 + y^2 = B$ , which is the equation for a circle. Note that the circle is centered at a point with  $y = 0$ , that is, at a point on the bottom of the slab. This is the point where the perpendicular bisector of the line joining the two given points intersects the bottom of the slab.

### **6.22. Minimal surface**

By “tension” in a surface, we mean the force per unit length in the surface. The tension throughout the surface must be constant, because it is in equilibrium. If the tension at one point were larger than at another, then some patch of the surface between these points would move.

The ratio of the circumferences of the circular boundaries of the ring is  $y_2/y_1$ . Therefore, the condition that the horizontal forces on the ring cancel is

![Figure 6.50: A 3D diagram of a minimal surface of revolution, resembling a soap bubble. It is bounded by two vertical circles of radii y1 and y2. The surface is shown with dashed lines indicating its curvature. At the top and bottom edges, the surface makes angles theta1 and theta2 with the horizontal dashed lines.](55bfad37987748bcc6ceb2609ee7f446_img.jpg)

Figure 6.50: A 3D diagram of a minimal surface of revolution, resembling a soap bubble. It is bounded by two vertical circles of radii y1 and y2. The surface is shown with dashed lines indicating its curvature. At the top and bottom edges, the surface makes angles theta1 and theta2 with the horizontal dashed lines.

Fig. 6.50

$y_1 \cos \theta_1 = y_2 \cos \theta_2$ , where the  $\theta$ 's are the angles of the surface, as shown in Fig. 6.50. In other words,  $y \cos \theta$  is constant throughout the surface. But  $\cos \theta = 1/\sqrt{1 + y'^2}$ , so we have

$$\frac{y}{\sqrt{1 + y'^2}} = C. \quad (6.233)$$

This is equivalent to Eq. (6.77), and the solution proceeds as in Section 6.8.

### 6.23. Existence of a minimal surface

The general solution for  $y(x)$  is given in Eq. (6.78) as  $y(x) = (1/b) \cosh b(x + d)$ . If we choose the origin to be midway between the rings, then  $d = 0$ . Both boundary condition are thus

$$r = \frac{1}{b} \cosh b\ell. \quad (6.234)$$

We will now determine the maximum value of  $\ell/r$  for which the minimal surface exists. If  $\ell/r$  is too large, then we will see that there is no solution for  $b$  in Eq. (6.234). If you perform an experiment with soap bubbles (which want to minimize their area), and if you pull the rings too far apart, then the surface will break and disappear as it tries to form the two boundary circles.

Define the dimensionless quantities,

$$\eta \equiv \frac{\ell}{r}, \quad \text{and} \quad z \equiv br. \quad (6.235)$$

Then Eq. (6.234) becomes

$$z = \cosh \eta z. \quad (6.236)$$

If we make a rough plot of the graphs of  $w = z$  and  $w = \cosh \eta z$  for a few values of  $\eta$  (see Fig. 6.51), we see that there is no solution to Eq. (6.236) if  $\eta$  is too large. The limiting value of  $\eta$  for which there exists a solution occurs when the curves  $w = z$  and  $w = \cosh \eta z$  are tangent; that is, when the slopes are equal in addition to the functions being equal. Let  $\eta_0$  be the limiting value of  $\eta$ , and let  $z_0$  be the place where the tangency occurs. Then equality of the values and the slopes gives

$$z_0 = \cosh(\eta_0 z_0), \quad \text{and} \quad 1 = \eta_0 \sinh(\eta_0 z_0). \quad (6.237)$$

Dividing the second of these equations by the first gives

$$1 = (\eta_0 z_0) \tanh(\eta_0 z_0). \quad (6.238)$$

This must be solved numerically. The solution is

$$\eta_0 z_0 \approx 1.200. \quad (6.239)$$

Plugging this into the second of Eqs. (6.237) gives

$$\left(\frac{\ell}{r}\right)_{\max} \equiv \eta_0 \approx 0.663. \quad (6.240)$$

(Note also that  $z_0 = 1.200/\eta_0 = 1.810$ .) We see that if  $\ell/r$  is larger than 0.663, then there is no solution for  $y(x)$  that is consistent with the boundary

![Figure 6.51: A graph showing the relationship between w and z. The vertical axis is w and the horizontal axis is z. A straight line w = z is shown. Several curves representing w = cosh(eta*z) are plotted for different values of eta. As eta increases, the curves shift upwards. The limiting case is shown where the curve w = cosh(eta_0*z) is tangent to the line w = z at the point (z_0, z_0).](c5ca6e0bad2cec50108e3374c9efb947_img.jpg)

Figure 6.51: A graph showing the relationship between w and z. The vertical axis is w and the horizontal axis is z. A straight line w = z is shown. Several curves representing w = cosh(eta\*z) are plotted for different values of eta. As eta increases, the curves shift upwards. The limiting case is shown where the curve w = cosh(eta\_0\*z) is tangent to the line w = z at the point (z\_0, z\_0).

Fig. 6.51

![Figure 6.52: A sequence of five diagrams showing the deformation of a soap bubble. The first diagram is a cylinder of length 2l and radius r. The subsequent diagrams show the cylinder pinching in the middle, forming a neck that eventually closes, leaving two separate disks. Arrows indicate the progression of the shape change.](dc1cb9edf11be33622e1046538bb23f1_img.jpg)

Figure 6.52: A sequence of five diagrams showing the deformation of a soap bubble. The first diagram is a cylinder of length 2l and radius r. The subsequent diagrams show the cylinder pinching in the middle, forming a neck that eventually closes, leaving two separate disks. Arrows indicate the progression of the shape change.

Fig. 6.52

conditions. Above this value of  $\ell/r$ , the soap bubble minimizes its area by heading toward the shape of just two disks, but it will pop well before it reaches that configuration.

To get a sense of the rough shape of the limiting minimal surface, note that the ratio of the radius of the “middle” circle to the radius of the boundary rings is

$$\frac{y(0)}{y(\ell)} = \frac{\cosh(0)}{\cosh(b\ell)} = \frac{1}{\cosh(\eta_0 z_0)} = \frac{1}{z_0} \approx 0.55. \quad (6.241)$$

#### REMARKS:

1. We glossed over one issue above, namely that there may be more than one solution for the constant  $b$  in Eq. (6.234). In fact, Fig. 6.51 shows that for any  $\eta < 0.663$ , there are two solutions for  $z$  in Eq. (6.236), and hence two solutions for  $b$  in Eq. (6.234). This means that there are two possible surfaces that might solve our problem. Which one do we want? It turns out that the surface corresponding to the smaller value of  $b$  is the one that minimizes the area, while the surface corresponding to the larger value of  $b$  is the one that (in some sense) maximizes the area.

We say “in some sense” because the surface with the larger  $b$  is actually a saddle point for the area. It can’t be a maximum, after all, because we can always make the area larger by adding little wiggles to it. It’s a saddle point because there does exist a class of variations for which it has the maximum area, namely ones where the “dip” in the curve is continuously made larger (just imagine lowering the midpoint in a smooth manner). Such a set of variations is shown in Fig. 6.52. If we start with a cylinder for a surface and then gradually pinch in the center, the area decreases at first (the decrease in the cross-sectional area is the dominant effect at the start). But then as the dip becomes very deep, the area increases because the surface starts to look like the two disks, and these two disks have a larger area than the original narrow cylinder. The surface eventually resembles two nearly flat cones connected by a line. As these cones finally flatten out to the two disks, the area decreases. Therefore, the area must have achieved a local maximum (at least with respect to this class of variations) somewhere in between. This local maximum (or rather, saddle point) arises because the Euler–Lagrange technique simply sets the “derivative” equal to zero and doesn’t differentiate between maxima, minima, and saddle points.

If  $\eta \equiv \ell/r > 0.663$  (so that the initial cylinder is now wide instead of narrow), there exists at least one class of variations for which the area decreases monotonically from the area of the cylinder down to the area of the two disks. If you draw a series of pictures (for a wide cylinder) analogous to those in Fig. 6.52, it is quite believable that this is the case.

2. How does the area of the limiting surface (with  $\eta_0 = 0.663$ ) compare with the area of the two disks? The area of the two disks is  $A_d = 2\pi r^2$ . And the area of

the limiting surface is

$$A_s = \int_{-\ell}^{\ell} 2\pi y \sqrt{1 + y'^2} dx. \quad (6.242)$$

Using Eq. (6.234), this becomes

$$\begin{aligned} A_s &= \int_{-\ell}^{\ell} \frac{2\pi}{b} \cosh^2 bx \, dx = \int_{-\ell}^{\ell} \frac{\pi}{b} (1 + \cosh 2bx) \, dx \\ &= \frac{2\pi\ell}{b} + \frac{\pi \sinh 2b\ell}{b^2}. \end{aligned} \quad (6.243)$$

But from the definitions of  $\eta$  and  $z$ , we have  $\ell = \eta_0 r$  and  $b = z_0/r$  for the limiting surface. Therefore,  $A_s$  can be written as

$$A_s = \pi r^2 \left( \frac{2\eta_0}{z_0} + \frac{\sinh 2\eta_0 z_0}{z_0^2} \right). \quad (6.244)$$

Plugging in the numerical values ( $\eta_0 \approx 0.663$  and  $z_0 \approx 1.810$ ) gives

$$A_d \approx (6.28)r^2, \quad \text{and} \quad A_s \approx (7.54)r^2. \quad (6.245)$$

The ratio of  $A_s$  to  $A_d$  is approximately 1.2 (it's actually  $\eta_0 z_0$ , as you can show). The limiting surface therefore has a larger area. This is expected, because for  $\ell/r > \eta_0$  the surface tries to run off to one with a smaller area, and there are no other stable configurations besides the  $\cosh$  solution we found. ♣

![Figure 6.53: A diagram showing a curve in the xy-plane. The x-axis is horizontal and the y-axis is vertical, pointing downwards. The curve starts at the origin (0,0) and ends at a point (x_0, y_0). An arrow on the curve indicates the direction of motion from the origin towards (x_0, y_0).](4eccdb3b560a656d9a0c44d49e83650f_img.jpg)

Figure 6.53: A diagram showing a curve in the xy-plane. The x-axis is horizontal and the y-axis is vertical, pointing downwards. The curve starts at the origin (0,0) and ends at a point (x\_0, y\_0). An arrow on the curve indicates the direction of motion from the origin towards (x\_0, y\_0).

Fig. 6.53

### 6.24. The brachistochrone

FIRST SOLUTION: In Fig. 6.53, the boundary conditions are  $y(0) = 0$  and  $y(x_0) = y_0$ , with downward taken to be the positive  $y$  direction. From conservation of energy, the speed as a function of  $y$  is  $v = \sqrt{2gy}$ . The total time is therefore

$$T = \int_0^{x_0} \frac{ds}{v} = \int_0^{x_0} \frac{\sqrt{1 + y'^2}}{\sqrt{2gy}} dx. \quad (6.246)$$

Our goal is to find the function  $y(x)$  that minimizes this integral, subject to the boundary conditions above. We can therefore apply the results of the variational technique, with a “Lagrangian” equal to

$$L \propto \frac{\sqrt{1 + y'^2}}{\sqrt{y}}. \quad (6.247)$$

At this point, we could apply the E–L equation to this  $L$ , but let's just use Lemma 6.5, with  $f(y) = 1/\sqrt{y}$ . Equation (6.86) gives

$$1 + y'^2 = Bf(y)^2 \implies 1 + y'^2 = \frac{B}{y}, \quad (6.248)$$

as desired. We must now integrate this. Solving for  $y'$  and separating variables gives

$$\frac{\sqrt{y} dy}{\sqrt{B-y}} = \pm dx. \quad (6.249)$$

A helpful change of variables to get rid of the square root in the denominator is  $y \equiv B \sin^2 \phi$ . Then  $dy = 2B \sin \phi \cos \phi d\phi$ , and Eq. (6.249) simplifies to

$$2B \sin^2 \phi d\phi = \pm dx. \quad (6.250)$$

We can now use  $\sin^2 \phi = (1 - \cos 2\phi)/2$  to integrate this. After multiplying through by 2, the result is  $B(2\phi - \sin 2\phi) = \pm 2x - C$ , where  $C$  is a constant of integration. Now note that we can rewrite our definition of  $\phi$  (which was  $y \equiv B \sin^2 \phi$ ) as  $2y = B(1 - \cos 2\phi)$ . If we then define  $\theta \equiv 2\phi$ , we have

$$x = \pm a(\theta - \sin \theta) \pm d, \quad y = a(1 - \cos \theta). \quad (6.251)$$

where  $a \equiv B/2$ , and  $d \equiv C/2$ . The particle starts at  $(x, y) = (0, 0)$ . Therefore,  $\theta$  starts at  $\theta = 0$ , since this corresponds to  $y = 0$ . The starting condition  $x = 0$  then implies that  $d = 0$ . Also, we are assuming that the wire heads down to the right, so we choose the positive sign in the expression for  $x$ . Therefore, we finally have

$$x = a(\theta - \sin \theta), \quad y = a(1 - \cos \theta), \quad (6.252)$$

as desired. This is the parametrization of a *cycloid*, which is the path taken by a point on the rim of a rolling wheel. The initial slope of the  $y(x)$  curve is infinite, as you can check.

REMARK: The above method derived the parametric form in (6.252) from scratch. But since Eq. (6.252) was given in the statement of the problem, another route is to simply verify that this parametrization satisfies Eq. (6.248). To this end, assume that  $x = a(\theta - \sin \theta)$  and  $y = a(1 - \cos \theta)$ , which gives

$$y' \equiv \frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta} = \frac{\sin \theta}{1 - \cos \theta}. \quad (6.253)$$

Therefore,

$$1 + y'^2 = 1 + \frac{\sin^2 \theta}{(1 - \cos \theta)^2} = \frac{2}{1 - \cos \theta} = \frac{2a}{y}, \quad (6.254)$$

which agrees with Eq. (6.248), with  $B \equiv 2a$ . ♣

SECOND SOLUTION: Let's use a variational argument again, but now with  $y$  as the independent variable. That is, let the chain be described by the function  $x(y)$ . The arclength is now given by  $ds = \sqrt{1 + x'^2} dy$ . Therefore, instead of the Lagrangian in Eq. (6.247), we have

$$L \propto \frac{\sqrt{1 + x'^2}}{\sqrt{y}}. \quad (6.255)$$

The Euler–Lagrange equation is

$$\frac{d}{dy} \left( \frac{\partial L}{\partial x'} \right) = \frac{\partial L}{\partial x} \implies \frac{d}{dy} \left( \frac{1}{\sqrt{y}} \frac{x'}{\sqrt{1 + x'^2}} \right) = 0. \quad (6.256)$$

The zero on the right-hand side makes things nice and easy because it means that the quantity in parentheses is a constant. If we define this constant to be  $1/\sqrt{B}$ , then we can solve for  $x'$  and then separate variables to obtain

$$\frac{\sqrt{y} dy}{\sqrt{B-y}} = \pm dx. \quad (6.257)$$

in agreement with Eq. (6.249). The solution proceeds as above.

THIRD SOLUTION: The “Lagrangian” in the first solution above, which is given in Eq. (6.247) as

$$L \propto \frac{\sqrt{1+y'^2}}{\sqrt{y}}, \quad (6.258)$$

is independent of  $x$ . Therefore, in analogy with conservation of energy (which arises from a Lagrangian that is independent of  $t$ ), the quantity

$$E \equiv y' \frac{\partial L}{\partial y'} - L = \frac{y'^2}{\sqrt{y}\sqrt{1+y'^2}} - \frac{\sqrt{1+y'^2}}{\sqrt{y}} = \frac{-1}{\sqrt{y}\sqrt{1+y'^2}} \quad (6.259)$$

is constant (that is, independent of  $x$ ). This statement is equivalent to Eq. (6.248), and the solution proceeds as above.