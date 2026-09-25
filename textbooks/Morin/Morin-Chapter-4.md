# Chapter 4 Oscillations

In this chapter we will discuss oscillatory motion. The simplest examples of such motion are a swinging pendulum and a mass on a spring, but it is possible to make a system more complicated by introducing a damping force and/or an external driving force. We will study all of these cases.

We are interested in oscillatory motion for two reasons. First, we study it because we *can* study it. This is one of the few systems in physics where we can solve the motion exactly. There's nothing wrong with looking under the lamppost every now and then. Second, oscillatory motion is ubiquitous in nature, for reasons that will become clear in Section 5.2. If there was ever a type of physical system worthy of study, this is it. We'll start off by doing some necessary math in Section 4.1. And then in Section 4.2 we'll show how the math is applied to the physics.

## 4.1 Linear differential equations

A *linear differential equation* is one in which  $x$  and its time derivatives enter only through their first powers. An example is  $3\ddot{x} + 7\dot{x} + x = 0$ . An example of a nonlinear differential equation is  $3\ddot{x} + 7\dot{x}^2 + x = 0$ . If the right-hand side of the equation is zero, then we use the term *homogeneous* differential equation. If the right-hand side is some function of  $t$ , as in the case of  $3\ddot{x} - 4\dot{x} = 9t^2 - 5$ , then we use the term *inhomogeneous* differential equation. The goal of this chapter is to learn how to solve linear differential equations, both homogeneous and inhomogeneous. These come up again and again in physics, so we had better find a systematic method of solving them.

The techniques that we will use are best learned through examples, so let's solve a few differential equations, starting with some simple ones. Throughout this chapter,  $x$  is understood to be a function of  $t$ . Hence, a dot denotes time differentiation.

---

**Example 1** ( $\dot{x} = ax$ ): This is a very simple differential equation. There are two ways (at least) to solve it.

**First method:** Separate variables to obtain  $dx/x = a dt$ , and then integrate to obtain  $\ln x = at + c$ , where  $c$  is a constant of integration. Then exponentiate to obtain

$$x = Ae^{at}, \quad (4.1)$$

where  $A \equiv e^c$ .  $A$  is determined by the value of  $x$  at, say,  $t = 0$ .

**Second method:** Guess an exponential solution, that is, one of the form  $x = Ae^{\alpha t}$ . Substitution into  $\dot{x} = ax$  immediately gives  $\alpha = a$ . Therefore, the solution is  $x = Ae^{at}$ . Note that we can't solve for  $A$ , due to the fact that our differential equation is homogeneous and linear in  $x$  (translation:  $A$  cancels out).  $A$  is determined by the initial condition.

This method may seem a bit silly, and somewhat cheap. But as we will see below, guessing these exponential functions (or sums of them) is actually the most general thing we can try, so the method is indeed quite general.

**REMARK:** Using this method, you might be concerned that although we have found one solution, we might have missed another one. But the general theory of differential equations says that a first-order linear equation has only one independent solution (we'll just accept this fact here). So if we find one solution, then we know that we've found the whole thing. ♣

---

**Example 2 ( $\ddot{x} = ax$ ):** If  $a$  is negative, then we'll see that this equation describes the oscillatory motion of, say, a spring. If  $a$  is positive, then it describes exponentially growing or decaying motion. There are two ways (at least) to solve this equation.

**First method:** We can use the separation-of-variables method from Section 3.3 here, because our system is one in which the force depends only on the position  $x$ . But this method is rather cumbersome, as you found if you did Problem 3.10 or Exercise 3.38. It will certainly work, but in the case where our equation is *linear* in  $x$ , there is a much simpler method:

**Second method:** As in the first example above, we can guess a solution of the form  $x(t) = Ae^{\alpha t}$  and then find out what  $\alpha$  must be. Again, we can't solve for  $A$ , because it cancels out. Plugging  $Ae^{\alpha t}$  into  $\ddot{x} = ax$  gives  $\alpha = \pm\sqrt{a}$ . We have therefore found *two* solutions. The most general solution is an arbitrary linear combination of these,

$$x(t) = Ae^{\sqrt{a}t} + Be^{-\sqrt{a}t}, \quad (4.2)$$

which you can quickly check does indeed work.  $A$  and  $B$  are determined by the initial conditions. As in the first example above, you might be concerned that although we have found two solutions to the equation, we might have missed others. But the general theory of differential equations says that our second-order linear equation has only two independent solutions. Therefore, having found two independent solutions, we know that we've found them all.

**VERY IMPORTANT REMARK:** The fact that the sum of two different solutions is again a solution to our equation is a monumentally important property of *linear* differential equations.

This property does *not* hold for nonlinear differential equations, for example  $\ddot{x}^2 = bx$ , because the act of squaring after adding the two solutions produces a cross term which destroys the equality, as you should check (see Problem 4.1). This property is called the *principle of superposition*. That is, superposing two solutions yields another solution. In other words, *linearity* leads to superposition. This fact makes theories that are governed by linear equations *much* easier to deal with than those that are governed by nonlinear ones. General Relativity, for example, is based on nonlinear equations, and solutions to most General Relativity systems are extremely difficult to come by.

For equations with one main condition  
 (Those linear), you have permission  
 To take your solutions,  
 With firm resolutions,  
 And add them in superposition. ♣

Let's say a little more about the solution in Eq. (4.2). If  $a$  is negative, then it is helpful to define  $a \equiv -\omega^2$ , where  $\omega$  is a real number. The solution then becomes  $x(t) = Ae^{i\omega t} + Be^{-i\omega t}$ . Using  $e^{i\theta} = \cos \theta + i \sin \theta$ , this can be written in terms of trig functions, if desired. Various ways of writing the solution are:

$$\begin{aligned} x(t) &= Ae^{i\omega t} + Be^{-i\omega t}, \\ x(t) &= C \cos \omega t + D \sin \omega t, \\ x(t) &= E \cos(\omega t + \phi_1), \\ x(t) &= F \sin(\omega t + \phi_2). \end{aligned} \tag{4.3}$$

Depending on the specifics of a given system, one of the above forms will work better than the others. The various constants in these expressions are related to each other. For example,  $C = E \cos \phi_1$  and  $D = -E \sin \phi_1$ , which follow from the cosine sum formula. Note that there are two free parameters in each of the above expressions for  $x(t)$ . These parameters are determined by the initial conditions (say, the position and velocity at  $t = 0$ ). In contrast with these free parameters, the quantity  $\omega$  is determined by the particular physical system we're dealing with. For example, we'll see that for a spring,  $\omega = \sqrt{k/m}$ , where  $k$  is the spring constant.  $\omega$  is independent of the initial conditions.

If  $a$  is positive, then let's define  $a \equiv \alpha^2$ , where  $\alpha$  is a real number. The solution in Eq. (4.2) then becomes  $x(t) = Ae^{\alpha t} + Be^{-\alpha t}$ . Using  $e^\theta = \cosh \theta + \sinh \theta$ , this can be written in terms of hyperbolic trig functions, if desired. Various ways of writing the solution are:

$$\begin{aligned} x(t) &= Ae^{\alpha t} + Be^{-\alpha t}, \\ x(t) &= C \cosh \alpha t + D \sinh \alpha t, \\ x(t) &= E \cosh(\alpha t + \phi_1), \\ x(t) &= F \sinh(\alpha t + \phi_2). \end{aligned} \tag{4.4}$$

Again, the various constants are related to each other. If you are unfamiliar with the hyperbolic trig functions, a few facts are listed in Appendix A.

Although the solution in Eq. (4.2) is completely correct for both signs of  $a$ , it's generally more illuminating to write the negative- $a$  solutions in either the trig forms or the  $e^{\pm i\omega t}$  exponential form where the  $i$ 's are explicit.

The usefulness of our method of guessing exponential solutions cannot be overemphasized. It may seem somewhat restrictive, but it works. The examples in the remainder of this chapter should convince you of this.

This is our method, essential,  
 For equations we solve, differential.  
 It gets the job done,  
 And it's even quite fun.  
 We just try a routine exponential.

---

**Example 3 ( $\ddot{x} + 2\gamma\dot{x} + ax = 0$ ):** This will be our last mathematical example, and then we'll start doing some physics. As we'll see later, this example pertains to a damped harmonic oscillator. We've put a factor of 2 in the coefficient of  $\dot{x}$  here to make some later formulas look nicer. The force in this example (if we switch from math to physics for a moment) is  $-2\gamma\dot{x} - ax$  (times  $m$ ), which depends on both  $v$  and  $x$ . Our methods of Section 3.3 therefore don't apply; we're not going to be able to use separation of variables here. This leaves us with only our method of guessing an exponential solution,  $Ae^{\alpha t}$ . So let's see what it gives us. Plugging  $x(t) = Ae^{\alpha t}$  into the given equation, and canceling the nonzero factor of  $Ae^{\alpha t}$ , gives

$$\alpha^2 + 2\gamma\alpha + a = 0. \quad (4.5)$$

The solutions for  $\alpha$  are  $-\gamma \pm \sqrt{\gamma^2 - a}$ . Call these  $\alpha_1$  and  $\alpha_2$ . Then the general solution to our equation is

$$\begin{aligned} x(t) &= Ae^{\alpha_1 t} + Be^{\alpha_2 t} \\ &= e^{-\gamma t} \left( Ae^{t\sqrt{\gamma^2 - a}} + Be^{-t\sqrt{\gamma^2 - a}} \right). \end{aligned} \quad (4.6)$$

If  $\gamma^2 - a < 0$ , then we can write this in terms of sines and cosines, so we have oscillatory motion that decreases in time due to the  $e^{-\gamma t}$  factor (or it increases, if  $\gamma < 0$ , but this is rarely physical). If  $\gamma^2 - a > 0$ , then we have exponential motion. We'll talk more about these different possibilities in Section 4.3.

In the first two examples above, the solutions were fairly clear. But in the present case, you're not apt to look at the above solution and say, "Oh, of course. It's obvious!" So our method of trying solutions of the form  $Ae^{\alpha t}$  isn't looking so silly anymore.

---

In general, if we have an  $n$ th order homogeneous linear differential equation,

$$\frac{d^n x}{dt^n} + c_{n-1} \frac{d^{n-1}x}{dt^{n-1}} + \cdots + c_1 \frac{dx}{dt} + c_0 x = 0, \quad (4.7)$$

then our strategy is to guess an exponential solution,  $x(t) = Ae^{\alpha t}$ , and to then (in theory) solve the resulting  $n$ th order equation,  $\alpha^n + c_{n-1}\alpha^{n-1} + \cdots + c_1\alpha + c_0 = 0$ , for  $\alpha$ , to obtain the solutions  $\alpha_1, \dots, \alpha_n$ . The general solution for  $x(t)$  is then the superposition,

$$x(t) = A_1e^{\alpha_1 t} + A_2e^{\alpha_2 t} + \cdots + A_ne^{\alpha_n t}, \quad (4.8)$$

where the  $A_i$  are determined by the initial conditions. In practice, however, we will rarely encounter differential equations of degree higher than 2. (Note: if some of the  $\alpha_i$  happen to be equal, then Eq. (4.8) is not valid, so a modification is needed. We will encounter such a situation in Section 4.3.)

## 4.2 Simple harmonic motion

Let's now do some real live physical problems. We'll start with simple harmonic motion. This is the motion undergone by a particle subject to a force  $F(x) = -kx$ . The classic system that undergoes simple harmonic motion is a mass attached to a massless spring, on a frictionless table (see Fig. 4.1). A typical spring has a force of the form  $F(x) = -kx$ , where  $x$  is the displacement from equilibrium (see Section 5.2 for the reason behind this). This is "Hooke's law," and it holds as long as the spring isn't stretched or compressed too far. Eventually this expression breaks down for any real spring. But if we assume a  $-kx$  force, then  $F = ma$  gives  $-kx = m\ddot{x}$ , or

$$\ddot{x} + \omega^2 x = 0, \quad \text{where } \omega \equiv \sqrt{\frac{k}{m}}. \quad (4.9)$$

This is simply the equation we studied in Example 2 in the previous section. From Eq. (4.3), the solution may be written as

$$x(t) = A \cos(\omega t + \phi). \quad (4.10)$$

This trig solution shows that the system oscillates back and forth forever in time.  $\omega$  is the *angular frequency*. If  $t$  increases by  $2\pi/\omega$ , then the argument of the cosine increases by  $2\pi$ , so the position and velocity are back to what they were. The *period* (the time for one complete cycle) is therefore  $T = 2\pi/\omega = 2\pi\sqrt{m/k}$ . The frequency in cycles per second (hertz) is  $\nu = 1/T = \omega/2\pi$ . The constant  $A$  (or rather the absolute value of  $A$ , if  $A$  is negative) is the *amplitude*, that is, the maximum distance the mass gets from the origin. Note that the velocity as a function of time is  $v(t) \equiv \dot{x}(t) = -A\omega \sin(\omega t + \phi)$ .

The constants  $A$  and  $\phi$  are determined by the initial conditions. If, for example,  $x(0) = 0$  and  $\dot{x}(0) = v$ , then we must have  $A \cos \phi = 0$  and  $-A\omega \sin \phi = v$ . Hence,  $\phi = \pi/2$ , and so  $A = -v/\omega$  (or  $\phi = -\pi/2$  and  $A = v/\omega$ , but this leads to the same solution). Therefore, we have  $x(t) = -(v/\omega) \cos(\omega t + \pi/2)$ . This looks a little nicer if we write it as  $x(t) = (v/\omega) \sin(\omega t)$ . It turns out that

![Diagram of a mass-spring system on a horizontal surface. A mass labeled 'm' is attached to a spring with spring constant 'k'. The spring is connected to a vertical wall on the left. The mass is resting on a horizontal surface.](fbebc18263a4dade04a54c89169d0f86_img.jpg)

Diagram of a mass-spring system on a horizontal surface. A mass labeled 'm' is attached to a spring with spring constant 'k'. The spring is connected to a vertical wall on the left. The mass is resting on a horizontal surface.

Fig. 4.1

if the facts you're given are the initial position and velocity,  $x_0$  and  $v_0$ , then the  $x(t) = C \cos \omega t + D \sin \omega t$  expression in Eq. (4.3) usually works best, because (as you can verify) it yields the nice clean results,  $C = x_0$  and  $D = v_0/\omega$ . Problem 4.3 gives another setup that involves initial conditions.

![Diagram of a simple pendulum. A mass m is suspended by a string of length l from a fixed horizontal support. The string makes an angle theta with the vertical dashed line.](052458c8cbd36d1b3ec33f8e5c01aa1d_img.jpg)

Diagram of a simple pendulum. A mass m is suspended by a string of length l from a fixed horizontal support. The string makes an angle theta with the vertical dashed line.

Fig. 4.2

**Example (Simple pendulum):** Another classic system that undergoes (approximately) simple harmonic motion is the simple pendulum, that is, a mass that hangs on a massless string and swings in a vertical plane. Let  $\ell$  be the length of the string, and let  $\theta(t)$  be the angle the string makes with the vertical (see Fig. 4.2). Then the gravitational force on the mass in the tangential direction is  $-mg \sin \theta$ . So  $F = ma$  in the tangential direction gives

$$-mg \sin \theta = m(\ell \ddot{\theta}). \quad (4.11)$$

The tension in the string combines with the radial component of gravity to produce the radial acceleration, so the radial  $F = ma$  equation serves only to tell us the tension, which we won't need here.

We will now enter the realm of approximations and assume that the amplitude of the oscillations is small. Without this approximation, the problem cannot be solved in closed form. Assuming  $\theta$  is small, we can use  $\sin \theta \approx \theta$  in Eq. (4.11) to obtain

$$\ddot{\theta} + \omega^2 \theta = 0, \quad \text{where } \omega \equiv \sqrt{\frac{g}{\ell}}. \quad (4.12)$$

Therefore,

$$\theta(t) = A \cos(\omega t + \phi), \quad (4.13)$$

where  $A$  and  $\phi$  are determined by the initial conditions. So the pendulum undergoes simple harmonic motion with a frequency of  $\sqrt{g/\ell}$ . The period is therefore  $T = 2\pi/\omega = 2\pi\sqrt{\ell/g}$ . The true motion is arbitrarily close to this, for sufficiently small amplitudes. Exercise 4.23 deals with the higher-order corrections to the motion in the case where the amplitude is not small.

There will be many occasions throughout your physics education where you will plow through a calculation and then end up with a simple equation of the form  $\ddot{z} + \omega^2 z = 0$ , where  $\omega^2$  is a positive quantity that depends on various parameters in the problem. When you encounter such an equation, you should jump for joy, because without any more effort you can simply write down the answer: the solution for  $z$  must be of the form  $z(t) = A \cos(\omega t + \phi)$ . No matter how complicated the system looks at first glance, if you end up with an equation that looks like  $\ddot{z} + \omega^2 z = 0$ , then you know that the system undergoes simple harmonic motion with a frequency equal to the square root of the coefficient of  $z$ , no matter what that coefficient is. If you end up with  $\ddot{z} + (\text{zucchini})z = 0$ , then the frequency is  $\omega = \sqrt{\text{zucchini}}$  (well, as long as the zucchini is positive and has the dimensions of inverse time squared).

## 4.3 Damped harmonic motion

Consider a mass  $m$  attached to the end of a spring with spring constant  $k$ . Let the mass be subject to a drag force proportional to its velocity,  $F_f = -bv$  (the subscript  $f$  here stands for “friction”; we’ll save the letter  $d$  for “driving” in the next section); see Fig. 4.3. Why do we study this  $F_f = -bv$  damping force? Two reasons: First, it is linear in  $x$ , which will allow us to solve for the motion. And second, it is a perfectly realistic force; an object moving at a slow speed through a fluid generally experiences a drag force proportional to its velocity. Note that this  $F_f = -bv$  force is *not* the force that a mass would feel if it were placed on a table with friction. In that case the drag force would be (roughly) constant.

Our goal in this section is to solve for the position as a function of time. The total force on the mass is  $F = -b\dot{x} - kx$ . So  $F = m\ddot{x}$  gives

$$\ddot{x} + 2\gamma\dot{x} + \omega^2x = 0, \quad (4.14)$$

where  $2\gamma \equiv b/m$ , and  $\omega^2 \equiv k/m$ . This is conveniently the same equation we already solved in Example 3 in Section 4.1 (with  $a \rightarrow \omega^2$ ). Now, however, we have the physical restrictions that  $\gamma > 0$  and  $\omega^2 > 0$ . Letting  $\Omega^2 \equiv \gamma^2 - \omega^2$  for simplicity, we may write the solution in Eq. (4.6) as

$$x(t) = e^{-\gamma t} (Ae^{\Omega t} + Be^{-\Omega t}), \quad \text{where } \Omega \equiv \sqrt{\gamma^2 - \omega^2}. \quad (4.15)$$

There are three cases to consider.

### Case 1: Underdamping ( $\Omega^2 < 0$ )

If  $\Omega^2 < 0$ , then  $\gamma < \omega$ . Since  $\Omega$  is imaginary, let us define the real number  $\tilde{\omega} \equiv \sqrt{\omega^2 - \gamma^2}$ , so that  $\Omega = i\tilde{\omega}$ . Equation (4.15) then gives

$$\begin{aligned} x(t) &= e^{-\gamma t} (Ae^{i\tilde{\omega}t} + Be^{-i\tilde{\omega}t}) \\ &\equiv e^{-\gamma t} C \cos(\tilde{\omega}t + \phi). \end{aligned} \quad (4.16)$$

These two forms are equivalent. Using  $e^{i\theta} = \cos\theta + i\sin\theta$ , the constants in Eq. (4.16) are related by  $A + B = C \cos\phi$  and  $A - B = iC \sin\phi$ . Note that in a physical problem,  $x(t)$  is real, so we must have  $A^* = B$ , where the star denotes complex conjugation. The two constants  $A$  and  $B$ , or the two constants  $C$  and  $\phi$ , are determined by the initial conditions.

Depending on the given problem, one of the expressions in Eq. (4.16) will inevitably work better than the other. Or perhaps one of the other forms in Eq. (4.3) (times  $e^{-\gamma t}$ ) will be the most useful one. The cosine form makes it apparent that the motion is harmonic motion whose amplitude decreases in time, due to the  $e^{-\gamma t}$  factor. A plot of such motion is shown in Fig. 4.4.<sup>1</sup> The frequency of the

![Diagram of a mass-spring system with damping. A mass m is attached to a spring with spring constant k. A force F_f is shown acting to the right, and a velocity v is shown acting to the left.](b6a1a6741471e0028eb218c36601b059_img.jpg)

The diagram shows a mass  $m$  attached to a spring with spring constant  $k$ . The spring is fixed to a vertical wall on the left. A force  $F_f$  is shown acting to the right, and a velocity  $v$  is shown acting to the left.

Diagram of a mass-spring system with damping. A mass m is attached to a spring with spring constant k. A force F\_f is shown acting to the right, and a velocity v is shown acting to the left.

Fig. 4.3

![Graph of position x versus time t for underdamped harmonic motion. The plot shows a damped oscillation x(t) with an exponential envelope e^{-\gamma t}.](84e0cc2296ce1d76046af25acfb965d3_img.jpg)

The graph shows the position  $x$  versus time  $t$  for underdamped harmonic motion. The plot shows a damped oscillation  $x(t)$  with an exponential envelope  $e^{-\gamma t}$ . The oscillation starts at a positive value and decreases in amplitude over time, crossing the  $t$ -axis at regular intervals.

Graph of position x versus time t for underdamped harmonic motion. The plot shows a damped oscillation x(t) with an exponential envelope e^{-\gamma t}.

Fig. 4.4

<sup>1</sup> To be precise, the amplitude doesn't decrease exactly like  $Ce^{-\gamma t}$ , as Eq. (4.16) suggests, because  $Ce^{-\gamma t}$  describes the envelope of the motion, and not the curve that passes through the extremes of

motion,  $\tilde{\omega} = \sqrt{\omega^2 - \gamma^2}$ , is smaller than the natural frequency  $\omega$  of the undamped oscillator.

REMARKS: If  $\gamma$  is very small (more precisely, if  $\gamma \ll \omega$ ), then  $\tilde{\omega} \approx \omega$ , which makes sense because we almost have an undamped oscillator. If  $\gamma$  is very close to  $\omega$ , then  $\tilde{\omega} \approx 0$ . So the oscillations are very slow (more precisely,  $\tilde{\omega} \ll \omega$ ). Of course, for very small  $\tilde{\omega}$  it's hard to even tell that the oscillations exist, because they will damp out on a time scale of order  $1/\gamma \approx 1/\omega$ , which is short compared with the long time scale of the oscillations,  $1/\tilde{\omega}$ . ♣

### Case 2: Overdamping ( $\Omega^2 > 0$ )

If  $\Omega^2 > 0$ , then  $\gamma > \omega$ .  $\Omega$  is real (and taken to be positive), so Eq. (4.15) gives

$$x(t) = Ae^{-(\gamma-\Omega)t} + Be^{-(\gamma+\Omega)t}. \quad (4.17)$$

There is no oscillatory motion in this case; see Fig. 4.5. Since  $\gamma > \Omega \equiv \sqrt{\gamma^2 - \omega^2}$ , both of the exponents are negative, so the motion goes to zero for large  $t$ . This had better be the case, because a real spring is certainly not going to have the motion fly off to infinity. If we had obtained a positive exponent somehow, we'd know we had made a mistake.

REMARKS: If  $\gamma$  is just slightly larger than  $\omega$ , then  $\Omega \approx 0$ , so the two terms in (4.17) are roughly equal, and we essentially have exponential decay, according to  $e^{-\gamma t}$ . If  $\gamma \gg \omega$  (that is, strong damping), then  $\Omega \approx \gamma$ , so the first term in (4.17) dominates (it has the less negative exponent), and we essentially have exponential decay according to  $e^{-(\gamma-\Omega)t}$ . We can be somewhat quantitative about this by approximating  $\Omega$  as

$$\Omega \equiv \sqrt{\gamma^2 - \omega^2} = \gamma\sqrt{1 - \omega^2/\gamma^2} \approx \gamma(1 - \omega^2/2\gamma^2). \quad (4.18)$$

Hence, the exponential behavior goes like  $e^{-\omega^2 t/2\gamma}$ . Because  $\gamma \gg \omega$ , this is slow decay (that is, slow compared with  $t \sim 1/\omega$ ), which makes sense if the damping is very strong. The mass slowly creeps back to the origin, as in the case of a weak spring immersed in molasses. ♣

### Case 3: Critical damping ( $\Omega^2 = 0$ )

If  $\Omega^2 = 0$ , then  $\gamma = \omega$ . Equation (4.14) therefore becomes  $\ddot{x} + 2\gamma\dot{x} + \gamma^2x = 0$ . In this special case, we have to be careful in solving our differential equation. The solution in Eq. (4.15) is not valid, because in the procedure leading to Eq. (4.6), the roots  $\alpha_1$  and  $\alpha_2$  are equal (to  $-\gamma$ ), so we have really found only one solution,  $e^{-\gamma t}$ . We'll just invoke here the result from the theory of differential equations that says that in this special case, the other solution is of the form  $te^{-\gamma t}$ .

REMARK: You should check explicitly that  $te^{-\gamma t}$  solves the equation  $\ddot{x} + 2\gamma\dot{x} + \gamma^2x = 0$ . Or if you want to, you can derive it in the spirit of Problem 4.2. In the more general case where there are  $n$  identical roots in the procedure leading to Eq. (4.8) (call them all  $\alpha$ ), the  $n$  independent solutions to the differential equation are  $t^k e^{\alpha t}$ , for  $0 \leq k \leq (n-1)$ . But more often than not, there are no repeated roots, so you don't have to worry about this. ♣

the motion. You can show that the amplitude in fact decreases like  $Ce^{-\gamma t} \cos(\tan^{-1}(\gamma/\tilde{\omega}))$ . This is the expression for the curve that passes through the extremes; see Castro (1986). But for small damping ( $\gamma \ll \omega$ ), this is essentially equal to  $Ce^{-\gamma t}$ . And in any event, it is proportional to  $e^{-\gamma t}$ .

![Figure 4.5: A graph showing the displacement x(t) versus time t for an overdamped oscillator. The curve starts at a positive value on the x-axis and decays exponentially towards the origin, never crossing the t-axis.](9f82bee1ad5917c67a7e5c1a7ce4fa0e_img.jpg)

Figure 4.5: A graph showing the displacement x(t) versus time t for an overdamped oscillator. The curve starts at a positive value on the x-axis and decays exponentially towards the origin, never crossing the t-axis.

Fig. 4.5

Our solution is therefore of the form,

$$x(t) = e^{-\gamma t}(A + Bt). \quad (4.19)$$

The exponential factor eventually wins out over the  $Bt$  term, so the motion goes to zero for large  $t$  (see Fig. 4.6).

If we are given a spring with a fixed  $\omega$ , and if we look at the system for different values of  $\gamma$ , then critical damping (when  $\gamma = \omega$ ) is the case where the motion converges to zero in the quickest way (which is like  $e^{-\omega t}$ ). This is true because in the underdamped case ( $\gamma < \omega$ ), the envelope of the oscillatory motion goes like  $e^{-\gamma t}$ , which goes to zero slower than  $e^{-\omega t}$ , because  $\gamma < \omega$ . And in the overdamped case ( $\gamma > \omega$ ), the dominant piece is the  $e^{-(\gamma-\Omega)t}$  term. And as you can verify, if  $\gamma > \omega$  then  $\gamma - \Omega \equiv \gamma - \sqrt{\gamma^2 - \omega^2} < \omega$ , so this motion also goes to zero slower than  $e^{-\omega t}$ . Critical damping is very important in many real systems, such as screen doors and shock absorbers, where the goal is to have the system head to zero (without overshooting and bouncing around) as fast as possible.

![Figure 4.6: A graph showing the displacement x(t) versus time t for a critically damped harmonic oscillator. The curve starts at a positive value on the x-axis and decays exponentially towards the t-axis, representing the function x(t) = e^{-\gamma t}(A + Bt).](2e8dd34433bac31ce3d0d503abd0210e_img.jpg)

Figure 4.6: A graph showing the displacement x(t) versus time t for a critically damped harmonic oscillator. The curve starts at a positive value on the x-axis and decays exponentially towards the t-axis, representing the function x(t) = e^{-\gamma t}(A + Bt).

Fig. 4.6

## 4.4 Driven (and damped) harmonic motion

Before we examine driven harmonic motion, we must learn how to solve a new type of differential equation. How can we solve something of the form

$$\ddot{x} + 2\gamma\dot{x} + ax = C_0e^{i\omega_0 t}, \quad (4.20)$$

where  $\gamma$ ,  $a$ ,  $\omega_0$ , and  $C_0$  are given quantities? This is an inhomogeneous differential equation, due to the term on the right-hand side. It's not very physical, because the right-hand side is complex, but let's not worry about that for now. Equations of this sort come up again and again, and fortunately there's a straightforward (although sometimes messy) method for solving them. As usual, the method involves making a reasonable guess, plugging it in, and seeing what condition comes out. Since we have the  $e^{i\omega_0 t}$  sitting on the right-hand side of Eq. (4.20), let's guess a solution of the form  $x(t) = Ae^{i\omega_0 t}$ .  $A$  will depend on  $\omega_0$ , among other things, as we will see. Plugging this guess into Eq. (4.20) and canceling the nonzero factor of  $e^{i\omega_0 t}$ , we obtain

$$(-\omega_0^2)A + 2\gamma(i\omega_0)A + aA = C_0. \quad (4.21)$$

Solving for  $A$ , we find that our solution for  $x$  is

$$x(t) = \left( \frac{C_0}{-\omega_0^2 + 2i\gamma\omega_0 + a} \right) e^{i\omega_0 t}. \quad (4.22)$$

Note the differences between this technique and the one in Example 3 in Section 4.1. In that example, the goal was to determine the  $\alpha$  in  $x(t) = Ae^{\alpha t}$ .

And there was no way to solve for  $A$ ; the initial conditions determined  $A$ . But in the present technique, the  $\omega_0$  in  $x(t) = Ae^{i\omega_0 t}$  is a given quantity, and the goal is to solve for  $A$  in terms of the given constants. Therefore, in the solution in Eq. (4.22), there are *no free constants* to be determined by the initial conditions. We've found one particular solution, and we're stuck with it. The term *particular solution* is used for Eq. (4.22).

With no freedom to adjust the solution in Eq. (4.22), how can we satisfy an arbitrary set of initial conditions? Fortunately, Eq. (4.22) does not represent the most general solution to Eq. (4.20). The most general solution is the sum of our particular solution in Eq. (4.22), *plus* the "homogeneous" solution we found in Eq. (4.6). This sum is certainly a solution, because the solution in Eq. (4.6) was explicitly constructed to yield zero when plugged into the left-hand side of Eq. (4.20). Therefore, tacking it on to our particular solution doesn't change the equality in Eq. (4.20), because the left side is linear. The principle of superposition has saved the day. The complete solution to Eq. (4.20) is therefore

$$x(t) = e^{-\gamma t} \left( Ae^{t\sqrt{\gamma^2 - a}} + Be^{-t\sqrt{\gamma^2 - a}} \right) + \left( \frac{C_0}{-\omega_0^2 + 2i\gamma\omega_0 + a} \right) e^{i\omega_0 t}, \quad (4.23)$$

where  $A$  and  $B$  are determined by the initial conditions.

With superposition in mind, it's clear what the strategy should be if we have a slightly more general equation to solve, for example,

$$\ddot{x} + 2\gamma\dot{x} + ax = C_1 e^{i\omega_1 t} + C_2 e^{i\omega_2 t}. \quad (4.24)$$

Simply solve the equation with only the first term on the right. Then solve the equation with only the second term on the right. Then add the two solutions. And then add on the homogeneous solution from Eq. (4.6). We are able to apply the principle of superposition because the left-hand side of Eq. (4.24) is linear.

Finally, let's look at the case where we have many such terms on the right-hand side, for example,

$$\ddot{x} + 2\gamma\dot{x} + ax = \sum_{n=1}^N C_n e^{i\omega_n t}. \quad (4.25)$$

We need to solve  $N$  different equations, each with only one of the  $N$  terms on the right-hand side. Then we add up all the solutions, and then we add on the homogeneous solution from Eq. (4.6). If  $N$  is infinite, that's fine; we just have to add up an infinite number of solutions. This is the principle of superposition at its best.

**REMARK:** The previous paragraph, combined with a basic result from Fourier analysis, allows us to solve (in principle) any equation of the form

$$\ddot{x} + 2\gamma\dot{x} + ax = f(t). \quad (4.26)$$

Fourier analysis says that any (nice enough) function  $f(t)$  can be decomposed into its Fourier components,

$$f(t) = \int_{-\infty}^{\infty} g(\omega) e^{i\omega t} d\omega. \quad (4.27)$$

In this continuous sum, the functions  $g(\omega)$  (times  $d\omega$ ) take the place of the coefficients  $C_n$  in Eq. (4.25). So if  $S_\omega(t)$  is the solution for  $x(t)$  when there is only the term  $e^{i\omega t}$  on the right-hand side of Eq. (4.26) (that is,  $S_\omega(t)$  is the solution given in Eq. (4.22), without the  $C_0$  factor), then the principle of superposition tells us that the complete particular solution to Eq. (4.26) is

$$x(t) = \int_{-\infty}^{\infty} g(\omega) S_\omega(t) d\omega. \quad (4.28)$$

Finding the coefficients  $g(\omega)$  is the hard part (or rather, the messy part), but we won't get into that here. We won't do anything with Fourier analysis in this book, but it's nevertheless good to know that it *is* possible to solve (4.26) for any function  $f(t)$ . Most of the functions we'll consider will be nice functions like  $\cos \omega_0 t$ , which has a very simple Fourier decomposition, namely  $\cos \omega_0 t = \frac{1}{2}(e^{i\omega_0 t} + e^{-i\omega_0 t})$ . ♣

Let's now do a physical example.

**Example (Damped and driven spring):** Consider a spring with spring constant  $k$ . A mass  $m$  at the end of the spring is subject to a drag force proportional to its velocity,  $F_f = -bv$ . The mass is also subject to a driving force,  $F_d(t) = F_d \cos \omega_d t$  (see Fig. 4.7). What is its position as a function of time?

**Solution:** The force on the mass is  $F(x, \dot{x}, t) = -b\dot{x} - kx + F_d \cos \omega_d t$ . So  $F = ma$  gives

$$\begin{aligned} \ddot{x} + 2\gamma\dot{x} + \omega^2 x &= F \cos \omega_d t \\ &= \frac{F}{2} (e^{i\omega_d t} + e^{-i\omega_d t}). \end{aligned} \quad (4.29)$$

where  $2\gamma \equiv b/m$ ,  $\omega^2 \equiv k/m$ , and  $F \equiv F_d/m$ . Note that there are two different frequencies here,  $\omega$  and  $\omega_d$ , which need not have anything to do with each other. Equation (4.22), along with the principle of superposition, tells us that our particular solution is

$$x_p(t) = \left( \frac{F/2}{-\omega_d^2 + 2i\gamma\omega_d + \omega^2} \right) e^{i\omega_d t} + \left( \frac{F/2}{-\omega_d^2 - 2i\gamma\omega_d + \omega^2} \right) e^{-i\omega_d t}. \quad (4.30)$$

The complete solution is the sum of this particular solution and the homogeneous solution from Eq. (4.15).

Let's now eliminate the  $i$ 's in Eq. (4.30) (which we had better be able to do, because  $x$  must be real), and write  $x$  in terms of sines and cosines. Getting the  $i$ 's out of the denominators (by multiplying both the numerator and the denominator by the complex conjugate of the denominator), and using  $e^{i\theta} = \cos \theta + i \sin \theta$ , we find,

![Diagram of a mass-spring system. A spring with constant k is attached to a wall on the left. A mass m is attached to the right end of the spring. A driving force F_d(t) is shown as a horizontal arrow pointing to the right. A drag force F_f is shown as a horizontal arrow pointing to the left. The velocity v is also shown as a horizontal arrow pointing to the right.](86cbb19347ca5edf9fd19782a6451c1c_img.jpg)

Diagram of a mass-spring system. A spring with constant k is attached to a wall on the left. A mass m is attached to the right end of the spring. A driving force F\_d(t) is shown as a horizontal arrow pointing to the right. A drag force F\_f is shown as a horizontal arrow pointing to the left. The velocity v is also shown as a horizontal arrow pointing to the right.

Fig. 4.7

after a little work,

$$x_p(t) = \left( \frac{F(\omega^2 - \omega_d^2)}{(\omega^2 - \omega_d^2)^2 + 4\gamma^2\omega_d^2} \right) \cos \omega_d t + \left( \frac{2F\gamma\omega_d}{(\omega^2 - \omega_d^2)^2 + 4\gamma^2\omega_d^2} \right) \sin \omega_d t. \quad (4.31)$$

REMARKS: If you want, you can solve Eq. (4.29) by taking the real part of the solution to Eq. (4.20) (with  $C_0 \rightarrow F$ ), that is, the  $x(t)$  in Eq. (4.22). This is true because if we take the real part of Eq. (4.20), we obtain

$$\begin{aligned} \frac{d^2}{dt^2}(\text{Re}(x)) + 2\gamma \frac{d}{dt}(\text{Re}(x)) + a(\text{Re}(x)) &= \text{Re}(C_0 e^{i\omega_0 t}) \\ &= C_0 \cos(\omega_0 t). \end{aligned} \quad (4.32)$$

In other words, if  $x$  satisfies Eq. (4.20) with a  $C_0 e^{i\omega_0 t}$  on the right-hand side, then  $\text{Re}(x)$  satisfies it with a  $C_0 \cos(\omega_0 t)$  on the right. At any rate, it's clear that the real part of the solution in Eq. (4.22) (with  $C_0 \rightarrow F$ ) does indeed give the result in Eq. (4.31), because in Eq. (4.30) we simply took half of a quantity plus its complex conjugate, which is the real part.

If you don't like using complex numbers, another way of solving Eq. (4.29) is to keep it in the form with the  $\cos \omega_d t$  on the right, and guess a solution of the form  $A \cos \omega_d t + B \sin \omega_d t$ , and then solve for  $A$  and  $B$  (this is the task of Problem 4.8). The result is Eq. (4.31). ♣

We can now write Eq. (4.31) in a very simple form. If we define

$$R \equiv \sqrt{(\omega^2 - \omega_d^2)^2 + (2\gamma\omega_d)^2}, \quad (4.33)$$

then we can rewrite Eq. (4.31) as

$$\begin{aligned} x_p(t) &= \frac{F}{R} \left( \frac{\omega^2 - \omega_d^2}{R} \cos \omega_d t + \frac{2\gamma\omega_d}{R} \sin \omega_d t \right) \\ &\equiv \frac{F}{R} \cos(\omega_d t - \phi), \end{aligned} \quad (4.34)$$

where  $\phi$  (the *phase*) is defined by

$$\cos \phi = \frac{\omega^2 - \omega_d^2}{R}, \quad \sin \phi = \frac{2\gamma\omega_d}{R} \implies \tan \phi = \frac{2\gamma\omega_d}{\omega^2 - \omega_d^2}. \quad (4.35)$$

The triangle describing the angle  $\phi$  is shown in Fig. 4.8. Note that  $0 \leq \phi \leq \pi$ , because the  $\sin \phi$  in Eq. (4.35) is greater than or equal to zero. See the end of this section for more discussion of  $\phi$ .

Recalling the homogeneous solution in Eq. (4.15), we can write the complete solution to Eq. (4.29) as

$$x(t) = \frac{F}{R} \cos(\omega_d t - \phi) + e^{-\gamma t} (Ae^{\Omega t} + Be^{-\Omega t}). \quad (4.36)$$

![Figure 4.8: A right-angled triangle illustrating the phase angle phi. The horizontal base is labeled omega^2 - omega_d^2. The vertical side is labeled 2*gamma*omega_d. The hypotenuse is labeled R = sqrt((omega^2 - omega_d^2)^2 + (2*gamma*omega_d)^2). The angle phi is shown at the bottom-left vertex between the base and the hypotenuse.](1aa2aef3257fd562b0625da623f45801_img.jpg)

Figure 4.8: A right-angled triangle illustrating the phase angle phi. The horizontal base is labeled omega^2 - omega\_d^2. The vertical side is labeled 2\*gamma\*omega\_d. The hypotenuse is labeled R = sqrt((omega^2 - omega\_d^2)^2 + (2\*gamma\*omega\_d)^2). The angle phi is shown at the bottom-left vertex between the base and the hypotenuse.

Fig. 4.8

The constants  $A$  and  $B$  are determined by the initial conditions. If there is any damping at all in the system (that is, if  $\gamma > 0$ ), then the homogeneous part of the solution goes to zero for large  $t$ , and we are left with only the particular solution. In other words, the system approaches a definite  $x(t)$ , namely  $x_p(t)$ , independent of the initial conditions.

### Resonance

The amplitude of the motion given in Eq. (4.34) is proportional to

$$\frac{1}{R} = \frac{1}{\sqrt{(\omega^2 - \omega_d^2)^2 + (2\gamma\omega_d)^2}}. \quad (4.37)$$

Given  $\omega_d$  and  $\gamma$ , this is maximum when  $\omega = \omega_d$ . Given  $\omega$  and  $\gamma$ , it is maximum when  $\omega_d = \sqrt{\omega^2 - 2\gamma^2}$ , as you can show in Exercise 4.29. But for weak damping (that is,  $\gamma \ll \omega$ , which is usually the case we are concerned with), this reduces to  $\omega_d \approx \omega$  also. The term *resonance* is used to describe the situation where the amplitude of the oscillations is as large as possible. It is quite reasonable that this is achieved when the driving frequency equals the frequency of the spring. But what is the value of the phase  $\phi$  at resonance? Using Eq. (4.35), we see that  $\phi$  satisfies  $\tan \phi \approx \pm\infty$  when  $\omega_d \approx \omega$ . Therefore,  $\phi = \pi/2$  (it is indeed  $\pi/2$ , and not  $-\pi/2$ , because the  $\sin \phi$  in Eq. (4.35) is positive), and the motion of the particle lags the driving force by a quarter of a cycle at resonance. For example, when the particle moves rightward past the origin (which means it has a quarter of a cycle to go before it hits the maximum value of  $x$ ), the force is already at its maximum. And when the particle makes it out to the maximum value of  $x$ , the force is already back to zero.

The fact that the force is maximum when the particle is moving fastest makes sense from an energy point of view.<sup>2</sup> If you want the amplitude to become large, then you need to give the system as much energy as you can. That is, you must do as much work as possible on the system. And in order to do as much work as possible, you should have your force act over as large a distance as possible, which means that you should apply your force when the particle is moving fastest, that is, as it speeds past the origin. And similarly, you don't want to waste your force when the particle is barely moving near the endpoints of its motion. In short,  $v$  is the derivative of  $x$  and therefore a quarter cycle ahead of  $x$  (which is a general property of a sinusoidal function, as you can show). Since we want the force to be in phase with  $v$  at resonance (by the above energy argument), we see that the force is also a quarter cycle ahead of  $x$ .

Resonance has a large number of extremely important applications (both wanted and unwanted) in the real world. On the desirable side, resonance makes

<sup>2</sup> Energy is one of the topics of the next chapter, so you may want to come back and read this paragraph after reading that.

it possible to have a relaxing day at the beach at the Bay of Fundy, talking to a friend over your cell phone while pushing a child on a swing at low tide. On the undesirable side, your ride home on that newly discovered “washboard” dirt road will be annoyingly bumpy at a certain speed, and any attempt to take your mind off the discomfort by turning up the radio will result only in certain parts of your car rattling in perfect sync (well, actually  $90^\circ$  out of phase) with the bass line of your formerly favorite song.<sup>3</sup>

### *The phase $\phi$*

Equation (4.35) gives the phase of the motion as

$$\tan \phi = \frac{2\gamma\omega_d}{\omega^2 - \omega_d^2}, \quad (4.38)$$

where  $0 \leq \phi \leq \pi$ . Let’s look at a few cases for  $\omega_d$  (not necessarily at resonance) and see what the resulting phase  $\phi$  is. Using Eq. (4.38), we have:

- If  $\omega_d \approx 0$  (or more precisely, if  $\gamma\omega_d \ll \omega^2 - \omega_d^2$ ), then  $\phi \approx 0$ . This means that the motion is in phase with the force. The mathematical reason for this is that if  $\omega_d \approx 0$ , then both  $\ddot{x}$  and  $\dot{x}$  are small, because they are proportional to  $\omega_d^2$  and  $\omega_d$ , respectively. Therefore, the first two terms in Eq. (4.29) are negligible, so we end up with  $x \propto \cos \omega_d t$ . In other words, the phase is zero.

The physical reason is that since there is essentially no acceleration, the net force is always essentially zero. This means that the driving force always essentially balances the spring force (that is, the two forces are  $180^\circ$  out of phase), because the damping force is negligible (since  $\dot{x} \propto \omega_d \approx 0$ ). But the spring force is  $180^\circ$  out of phase with the motion (because of the minus sign in  $F = -kx$ ). Therefore, the driving force is in phase with the motion.

- If  $\omega_d \approx \omega$ , then  $\phi \approx \pi/2$ . This is the case of resonance, discussed above.
- If  $\omega_d \approx \infty$  (or more precisely, if  $\gamma\omega_d \ll \omega_d^2 - \omega^2$ ), then  $\phi \approx \pi$ . The mathematical reason for this is that if  $\omega_d \approx \infty$ , then the  $\ddot{x}$  term in Eq. (4.29) dominates, so we have  $\ddot{x} \propto \cos \omega_d t$ . Therefore,  $\ddot{x}$  is in phase with the force. But  $x$  is  $180^\circ$  out of phase with  $\ddot{x}$  (this is a general property of a sinusoidal function), so  $x$  is  $180^\circ$  out of phase with the force.

The physical reason is that if  $\omega_d \approx \infty$ , then the mass hardly moves, because from Eq. (4.37) we see that the amplitude is proportional to  $1/\omega_d^2$ . This amplitude then implies that the velocity is proportional to  $1/\omega_d$ . Therefore, both  $x$  and  $v$  are always small. But if  $x$  and  $v$  are always small, then the spring and damping forces can be ignored. So we basically have a mass that feels only one force, the driving force. But we already understand very well a situation where a mass is subject to only one oscillating force: a mass on a spring. The mass in our setup can’t tell if it’s being driven by an oscillating

<sup>3</sup> Some other examples of resonance that are often cited are in fact not actually examples of resonance, but rather of “negative damping” (also known as positive feedback). Musical instruments fall into this category, as does the well-known Tacoma Narrows bridge failure. For a detailed discussion of this issue, see Billah and Scanlan (1991) and also Green and Unruh (2006).

driving force, or being pushed and pulled by an oscillating spring force. They both feel the same. Therefore, both phases must be the same. But in the spring case, the minus sign in  $F = -kx$  tells us that the force is  $180^\circ$  out of phase with the motion. Hence, the same result holds in the  $\omega_d \approx \infty$  case.

Another special case for the phase occurs when  $\gamma = 0$  (no damping), for which we have  $\tan \phi = \pm 0$ , depending on the sign of  $\omega^2 - \omega_d^2$ . So  $\phi$  is either  $0$  or  $\pi$ . The motion is therefore either exactly in phase or out of phase with the driving force, depending on which of  $\omega$  or  $\omega_d$  is larger.

## 4.5 Coupled oscillators

In the previous sections, we dealt with only one function of time,  $x(t)$ . What if we have two functions of time, say  $x(t)$  and  $y(t)$ , that are related by a pair of “coupled” differential equations? For example, we might have

$$\begin{aligned} 2\ddot{x} + \omega^2(5x - 3y) &= 0, \\ 2\ddot{y} + \omega^2(5y - 3x) &= 0. \end{aligned} \quad (4.39)$$

For now, let’s not worry about how these equations might arise. Let’s just try to solve them (we’ll do a physical example later in this section). We’ll assume  $\omega^2 > 0$  here, although this isn’t necessary. We’ll also assume there aren’t any damping or driving forces, although a few of the problems and exercises for this chapter deal with these additions. We call the above equations “coupled” because there are  $x$ ’s and  $y$ ’s in both of them, and it isn’t immediately obvious how to separate them to solve for  $x$  and  $y$ . There are two methods (at least) for solving these equations.

**First method:** Sometimes it is easy, as in this case, to find certain linear combinations of the given equations for which nice things happen. If we take the sum, we find

$$(\ddot{x} + \ddot{y}) + \omega^2(x + y) = 0. \quad (4.40)$$

This equation involves  $x$  and  $y$  only in the combination of their sum,  $x + y$ . With  $z \equiv x + y$ , Eq. (4.40) is just our old friend,  $\ddot{z} + \omega^2 z = 0$ . The solution is

$$x + y = A_1 \cos(\omega t + \phi_1), \quad (4.41)$$

where  $A_1$  and  $\phi_1$  are determined by the initial conditions. We may also take the difference of Eqs. (4.39), which results in

$$(\ddot{x} - \ddot{y}) + 4\omega^2(x - y) = 0. \quad (4.42)$$

This equation involves  $x$  and  $y$  only in the combination of their difference,  $x - y$ . The solution is

$$x - y = A_2 \cos(2\omega t + \phi_2). \quad (4.43)$$

Taking the sum and difference of Eqs. (4.41) and (4.43), we find that  $x(t)$  and  $y(t)$  are given by

$$\begin{aligned} x(t) &= B_1 \cos(\omega t + \phi_1) + B_2 \cos(2\omega t + \phi_2), \\ y(t) &= B_1 \cos(\omega t + \phi_1) - B_2 \cos(2\omega t + \phi_2), \end{aligned} \quad (4.44)$$

where the  $B_i$ 's are half of the  $A_i$ 's. The strategy of this solution was simply to fiddle around and try to form differential equations that involved only one combination of the variables. This allowed us to write down the familiar solution for these combinations, as we did in Eqs. (4.41) and (4.43).

We've managed to solve our equations for  $x$  and  $y$ . However, it turns out that the more interesting thing we've done is produce the equations (4.41) and (4.43). The combinations  $(x + y)$  and  $(x - y)$  are called the *normal coordinates* of the system. These are the combinations that oscillate with one pure frequency. The motion of  $x$  and  $y$  will in general look complicated, and it may be difficult to tell that the motion is really made up of just the two frequencies in Eq. (4.44). But if you plot the values of  $(x + y)$  and  $(x - y)$  as time goes by, for *any* motion of the system, then you will find nice sinusoidal graphs, even if  $x$  and  $y$  are each behaving in a rather unpleasant manner.

**Second method:** In the above method, it was fairly easy to guess which combinations of Eqs. (4.39) would produce equations involving only one combination of  $x$  and  $y$ . But surely there are problems in physics where the guessing isn't so easy. What do we do then? Fortunately, there is a fail-safe method for solving for  $x$  and  $y$ . It proceeds as follows.

In the spirit of Section 4.1, let's try a solution of the form  $x = Ae^{i\alpha t}$  and  $y = Be^{i\alpha t}$ , which we will write, for convenience, as

$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} A \\ B \end{pmatrix} e^{i\alpha t}. \quad (4.45)$$

It isn't obvious that there should exist solutions for  $x$  and  $y$  that have the same  $t$  dependence, but let's try it and see what happens. We've explicitly put the  $i$  in the exponent, but there's no loss of generality here. If  $\alpha$  happens to be imaginary, then the exponent is real. It's personal preference whether or not you put the  $i$  in. Plugging our guess into Eqs. (4.39), and dividing through by  $e^{i\alpha t}$ , we find

$$\begin{aligned} 2A(-\alpha^2) + 5A\omega^2 - 3B\omega^2 &= 0, \\ 2B(-\alpha^2) + 5B\omega^2 - 3A\omega^2 &= 0, \end{aligned} \quad (4.46)$$

or equivalently, in matrix form,

$$\begin{pmatrix} -2\alpha^2 + 5\omega^2 & -3\omega^2 \\ -3\omega^2 & -2\alpha^2 + 5\omega^2 \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}. \quad (4.47)$$

This homogeneous equation for  $A$  and  $B$  has a nontrivial solution (that is, one where  $A$  and  $B$  aren't both 0) only if the matrix is *not* invertible. This is true because if it were invertible, then we could multiply through by the inverse to obtain  $(A, B) = (0, 0)$ . When is a matrix invertible? There is a straightforward (although tedious) method for finding the inverse. It involves taking cofactors, taking a transpose, and dividing by the determinant. The step that concerns us here is the division by the determinant, since this implies that the inverse exists if and only if the determinant is not zero. So we see that Eq. (4.47) has a nontrivial solution only if the determinant equals zero. Because we seek a nontrivial solution, we must therefore have

$$0 = \begin{vmatrix} -2\alpha^2 + 5\omega^2 & -3\omega^2 \\ -3\omega^2 & -2\alpha^2 + 5\omega^2 \end{vmatrix} \\ = 4\alpha^4 - 20\alpha^2\omega^2 + 16\omega^4. \quad (4.48)$$

This is a quadratic equation in  $\alpha^2$ , and the roots are  $\alpha = \pm\omega$  and  $\alpha = \pm 2\omega$ . We have therefore found four types of solutions. If  $\alpha = \pm\omega$ , then we can plug this back into Eq. (4.47) to obtain  $A = B$ . (Both equations give this same result. This was essentially the point of setting the determinant equal to zero.) And if  $\alpha = \pm 2\omega$ , then Eq. (4.47) gives  $A = -B$ . (Again, the equations are redundant.) Note that we cannot solve specifically for  $A$  and  $B$ , but only for their ratio. Adding up our four solutions according to the principle of superposition, we see that  $x$  and  $y$  take the general form (written in vector form for the sake of simplicity and bookkeeping),

$$\begin{pmatrix} x \\ y \end{pmatrix} = A_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} e^{i\omega t} + A_2 \begin{pmatrix} 1 \\ 1 \end{pmatrix} e^{-i\omega t} \\ + A_3 \begin{pmatrix} 1 \\ -1 \end{pmatrix} e^{2i\omega t} + A_4 \begin{pmatrix} 1 \\ -1 \end{pmatrix} e^{-2i\omega t}. \quad (4.49)$$

The four  $A_i$  are determined by the initial conditions. We can rewrite Eq. (4.49) in a somewhat cleaner form. If the coordinates  $x$  and  $y$  describe the positions of particles, they must be real. Therefore,  $A_1$  and  $A_2$  must be complex conjugates, and likewise for  $A_3$  and  $A_4$ . If we then define some  $\phi$ 's and  $B$ 's via  $A_2^* = A_1 \equiv (B_1/2)e^{i\phi_1}$  and  $A_4^* = A_3 \equiv (B_2/2)e^{i\phi_2}$ , we may rewrite our solution in the form, as you can verify,

$$\begin{pmatrix} x \\ y \end{pmatrix} = B_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} \cos(\omega t + \phi_1) + B_2 \begin{pmatrix} 1 \\ -1 \end{pmatrix} \cos(2\omega t + \phi_2), \quad (4.50)$$

where the  $B_i$  and  $\phi_i$  are real (and are determined by the initial conditions). We have therefore reproduced the result in Eq. (4.44).

It is clear from Eq. (4.50) that the combinations  $x + y$  and  $x - y$  (the normal coordinates) oscillate with the pure frequencies,  $\omega$  and  $2\omega$ , respectively, because

the combination  $x + y$  makes the  $B_2$  terms disappear, and the combination  $x - y$  makes the  $B_1$  terms disappear.

It is also clear that if  $B_2 = 0$ , then  $x = y$  at all times, and they both oscillate with frequency  $\omega$ . And if  $B_1 = 0$ , then  $x = -y$  at all times, and they both oscillate with frequency  $2\omega$ . These two pure-frequency motions are called the *normal modes*. They are labeled by the vectors  $(1, 1)$  and  $(1, -1)$ , respectively. In describing a normal mode, both the vector and the frequency should be stated. The significance of normal modes will become clear in the following example.

![Diagram of two masses connected by three springs between two walls.](8eb31edda0a3f30a53d69fc98f9b9493_img.jpg)

The diagram shows two identical masses, each labeled 'm', connected in a line by three identical springs, each labeled 'k'. The entire system is held between two vertical walls. The left mass is connected to the left wall by a spring, the two masses are connected to each other by a middle spring, and the right mass is connected to the right wall by a spring.

Diagram of two masses connected by three springs between two walls.

**Fig. 4.9**

**Example (Two masses, three springs):** Consider two masses  $m$ , connected to each other and to two walls by three springs, as shown in Fig. 4.9. The three springs have the same spring constant  $k$ . Find the most general solution for the positions of the masses as functions of time. What are the normal coordinates? What are the normal modes?

**Solution:** Let  $x_1(t)$  and  $x_2(t)$  be the positions of the left and right masses, respectively, relative to their equilibrium positions. Then the middle spring is stretched a distance  $x_2 - x_1$  compared with the stretch at equilibrium. Therefore, the net force on the left mass is  $-kx_1 + k(x_2 - x_1)$ , and the net force on the right mass is  $-kx_2 - k(x_2 - x_1)$ . It's easy to make a mistake in the sign of the second term in these expressions, but you can check it by, say, looking at the force when  $x_2$  is very big. At any rate, the second term must have the opposite sign in the two expressions, by Newton's third law. With these forces,  $F = ma$  on each mass gives, with  $\omega^2 = k/m$ ,

$$\begin{aligned}\ddot{x}_1 + 2\omega^2 x_1 - \omega^2 x_2 &= 0, \\ \ddot{x}_2 + 2\omega^2 x_2 - \omega^2 x_1 &= 0.\end{aligned}\tag{4.51}$$

These are rather friendly looking coupled equations, and we can see that the sum and difference are the useful combinations to take. The sum gives

$$(\ddot{x}_1 + \ddot{x}_2) + \omega^2(x_1 + x_2) = 0,\tag{4.52}$$

and the difference gives

$$(\ddot{x}_1 - \ddot{x}_2) + 3\omega^2(x_1 - x_2) = 0.\tag{4.53}$$

The solutions to these equations are the normal coordinates,

$$\begin{aligned}x_1 + x_2 &= A_+ \cos(\omega t + \phi_+), \\ x_1 - x_2 &= A_- \cos(\sqrt{3}\omega t + \phi_-).\end{aligned}\tag{4.54}$$

Taking the sum and difference of these normal coordinates, we have

$$\begin{aligned}x_1(t) &= B_+ \cos(\omega t + \phi_+) + B_- \cos(\sqrt{3}\omega t + \phi_-), \\ x_2(t) &= B_+ \cos(\omega t + \phi_+) - B_- \cos(\sqrt{3}\omega t + \phi_-),\end{aligned}\tag{4.55}$$

where the  $B$ 's are half of the  $A$ 's. Along with the  $\phi$ 's, they are determined by the initial conditions.

REMARK: For practice, let's also derive Eq. (4.55) by using the determinant method. Letting  $x_1 = Ae^{i\alpha t}$  and  $x_2 = Be^{i\alpha t}$  in Eq. (4.51), we see that for there to be a nontrivial solution for  $A$  and  $B$ , we must have

$$0 = \begin{vmatrix} -\alpha^2 + 2\omega^2 & -\omega^2 \\ -\omega^2 & -\alpha^2 + 2\omega^2 \end{vmatrix} \\ = \alpha^4 - 4\alpha^2\omega^2 + 3\omega^4. \quad (4.56)$$

This is a quadratic equation in  $\alpha^2$ , and the roots are  $\alpha = \pm\omega$  and  $\alpha = \pm\sqrt{3}\omega$ . If  $\alpha = \pm\omega$ , then Eq. (4.51) gives  $A = B$ . If  $\alpha = \pm\sqrt{3}\omega$ , then Eq. (4.51) gives  $A = -B$ . The solutions for  $x_1$  and  $x_2$  therefore take the general form

$$\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = A_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} e^{i\omega t} + A_2 \begin{pmatrix} 1 \\ 1 \end{pmatrix} e^{-i\omega t} \\ + A_3 \begin{pmatrix} 1 \\ -1 \end{pmatrix} e^{i\sqrt{3}\omega t} + A_4 \begin{pmatrix} 1 \\ -1 \end{pmatrix} e^{-i\sqrt{3}\omega t} \\ \equiv B_+ \begin{pmatrix} 1 \\ 1 \end{pmatrix} \cos(\omega t + \phi_+) + B_- \begin{pmatrix} 1 \\ -1 \end{pmatrix} \cos(\sqrt{3}\omega t + \phi_-), \quad (4.57)$$

where the last line follows from the same substitutions that led to Eq. (4.50). This expression is equivalent to Eq. (4.55). ♣

The normal modes are obtained by setting either  $B_-$  or  $B_+$  equal to zero in Eq. (4.55) or Eq. (4.57). Therefore, the normal modes are  $(1, 1)$  and  $(1, -1)$ . How do we visualize these? The mode  $(1, 1)$  oscillates with frequency  $\omega$ . In this case (where  $B_- = 0$ ), we have  $x_1(t) = x_2(t) = B_+ \cos(\omega t + \phi_+)$  at all times. So the masses simply oscillate back and forth in the same manner, as shown in Fig. 4.10. It is clear that such motion has frequency  $\omega$ , because as far as the masses are concerned, the middle spring is effectively not there, so each mass moves under the influence of only one spring, and therefore has frequency  $\omega$ .

The mode  $(1, -1)$  oscillates with frequency  $\sqrt{3}\omega$ . In this case (where  $B_+ = 0$ ), we have  $x_1(t) = -x_2(t) = B_- \cos(\sqrt{3}\omega t + \phi_-)$  at all times. So the masses oscillate back and forth with opposite displacements, as shown in Fig. 4.11. It is clear that this mode should have a frequency larger than that for the other mode, because the middle spring is stretched (or compressed), so the masses feel a larger force. But it takes a little thought to show that the frequency is  $\sqrt{3}\omega$ .<sup>4</sup>

---

The normal mode  $(1, 1)$  above is associated with the normal coordinate  $x_1 + x_2$ . They both involve the frequency  $\omega$ . However, this association is *not* due to the fact that the coefficients of both  $x_1$  and  $x_2$  in this normal coordinate are equal to 1.

<sup>4</sup> If you want to obtain this  $\sqrt{3}\omega$  result without going through all of the above work, just note that the center of the middle spring doesn't move. Therefore, it acts like two "half springs," each with spring constant  $2k$  (as you can verify). Hence, each mass is effectively attached to a " $k$ " spring and a " $2k$ " spring, yielding a total effective spring constant of  $3k$ . Thus the  $\sqrt{3}$ .

![Figure 4.10: Two diagrams of a coupled oscillator system in the (1, 1) normal mode. The top diagram shows two masses at their equilibrium positions. The bottom diagram shows both masses displaced to the right by the same amount, with the middle spring remaining at its natural length, effectively inactive.](9e39bd3706c7fc6d019f7f55b2296e40_img.jpg)

Figure 4.10: Two diagrams of a coupled oscillator system in the (1, 1) normal mode. The top diagram shows two masses at their equilibrium positions. The bottom diagram shows both masses displaced to the right by the same amount, with the middle spring remaining at its natural length, effectively inactive.

Fig. 4.10

![Figure 4.11: Two diagrams of a coupled oscillator system in the (1, -1) normal mode. The top diagram shows the left mass displaced to the right and the right mass displaced to the left by equal amounts, stretching the middle spring. The bottom diagram shows the left mass displaced to the left and the right mass displaced to the right by equal amounts, compressing the middle spring.](ef27996fa639d1138b5b4111945220c5_img.jpg)

Figure 4.11: Two diagrams of a coupled oscillator system in the (1, -1) normal mode. The top diagram shows the left mass displaced to the right and the right mass displaced to the left by equal amounts, stretching the middle spring. The bottom diagram shows the left mass displaced to the left and the right mass displaced to the right by equal amounts, compressing the middle spring.

Fig. 4.11

Rather, it is due to the fact that the *other* normal mode, namely  $(x_1, x_2) \propto (1, -1)$ , gives no contribution to the sum  $x_1 + x_2$ . There are a few too many 1's floating around in the above example, so it's hard to see which results are meaningful and which results are coincidence. But the following example should clear things up. Let's say we solved a problem using the determinant method, and we found the solution to be

$$\begin{pmatrix} x \\ y \end{pmatrix} = B_1 \begin{pmatrix} 3 \\ 2 \end{pmatrix} \cos(\omega_1 t + \phi_1) + B_2 \begin{pmatrix} 1 \\ -5 \end{pmatrix} \cos(\omega_2 t + \phi_2). \quad (4.58)$$

Then  $5x + y$  is the normal coordinate associated with the normal mode  $(3, 2)$ , which has frequency  $\omega_1$ . (This is true because there is no  $\cos(\omega_2 t + \phi_2)$  dependence in the combination  $5x + y$ .) And similarly,  $2x - 3y$  is the normal coordinate associated with the normal mode  $(1, -5)$ , which has frequency  $\omega_2$  (because there is no  $\cos(\omega_1 t + \phi_1)$  dependence in the combination  $2x - 3y$ ).

Note the difference between the types of differential equations we solved in the previous chapter in Section 3.3, and the types we solved throughout this chapter. The former dealt with forces that did not have to be linear in  $x$  or  $\dot{x}$ , but that had to depend on only  $x$ , or only  $\dot{x}$ , or only  $t$ . The latter dealt with forces that could depend on all three of these quantities, but that had to be linear in  $x$  and  $\dot{x}$ .

## 4.6 Problems

## Section 4.1: Linear differential equations

### 4.1. Superposition

Let  $x_1(t)$  and  $x_2(t)$  be solutions to  $\ddot{x}^2 = bx$ . Show that  $x_1(t) + x_2(t)$  is *not* a solution to this equation.

### 4.2. A limiting case \*

Consider the equation  $\ddot{x} = ax$ . If  $a = 0$ , then the solution to  $\ddot{x} = 0$  is simply  $x(t) = C + Dt$ . Show that in the limit  $a \rightarrow 0$ , Eq. (4.2) reduces to this form. *Note:*  $a \rightarrow 0$  is a sloppy way of saying what we mean. What is the proper way to write this limit?

### Section 4.2: Simple harmonic motion

### 4.3. Increasing the mass \*\*

A mass  $m$  oscillates on a spring with spring constant  $k$ . The amplitude is  $d$ . At the moment (let this be  $t = 0$ ) when the mass is at position  $x = d/2$  (and moving to the right), it collides and sticks to another mass  $m$ . The speed of the resulting mass  $2m$  right after the collision is half the speed of the moving mass  $m$  right before the collision

(from momentum conservation, discussed in Chapter 5). What is the resulting  $x(t)$ ? What is the amplitude of the new oscillation?

### 4.4. Average tension \*\*

Is the average (over time) tension in the string of a pendulum larger or smaller than  $mg$ ? By how much? As usual, assume that the angular amplitude  $A$  is small.

### 4.5. Walking east on a turntable \*\*

A person walks at constant speed  $v$  eastward with respect to a turntable that rotates counterclockwise at constant frequency  $\omega$ . Find the general expression for the person's coordinates with respect to the ground (with the  $x$  direction taken to be eastward).

### Section 4.3: Damped harmonic motion

### 4.6. Maximum speed \*\*

A mass on the end of a spring (with natural frequency  $\omega$ ) is released from rest at position  $x_0$ . The experiment is repeated, but now with the system immersed in a fluid that causes the motion to be overdamped (with damping coefficient  $\gamma$ ). Find the ratio of the maximum speed in the former case to that in the latter. What is the ratio in the limit of strong damping ( $\gamma \gg \omega$ )? In the limit of critical damping?

### Section 4.4: Driven (and damped) harmonic motion

### 4.7. Exponential force \*

A particle of mass  $m$  is subject to a force  $F(t) = ma_0 e^{-bt}$ . The initial position and speed are both zero. Find  $x(t)$ . (This problem was already given as Problem 3.9, but solve it here by guessing an exponential function, in the spirit of Section 4.4.)

### 4.8. Driven oscillator \*

Derive Eq. (4.31) by guessing a solution of the form  $x(t) = A \cos \omega_d t + B \sin \omega_d t$  in Eq. (4.29).

### Section 4.5: Coupled oscillators

### 4.9. Unequal masses \*\*

Three identical springs and two masses,  $m$  and  $2m$ , lie between two walls as shown in Fig. 4.12. Find the normal modes.

![Diagram of a coupled oscillator system with unequal masses. Two vertical walls are connected by three identical springs with spring constant k. A mass m is attached to the left wall, a mass 2m is attached to the middle spring, and the right wall is attached to the rightmost spring.](8ab60220e3fa21b79b96c5380f553223_img.jpg)

Diagram of a coupled oscillator system with unequal masses. Two vertical walls are connected by three identical springs with spring constant k. A mass m is attached to the left wall, a mass 2m is attached to the middle spring, and the right wall is attached to the rightmost spring.

Fig. 4.12

### 4.10. Weakly coupled \*\*

Three springs and two equal masses lie between two walls, as shown in Fig. 4.13. The spring constant,  $k$ , of the two outside springs is much

![Diagram of a coupled oscillator system with equal masses. Two vertical walls are connected by three springs. The two outer springs have spring constant k, and the middle spring has spring constant κ. Two equal masses m are placed between the springs.](c5ba1a163e239ad2ea20851217c40c3b_img.jpg)

Diagram of a coupled oscillator system with equal masses. Two vertical walls are connected by three springs. The two outer springs have spring constant k, and the middle spring has spring constant κ. Two equal masses m are placed between the springs.

Fig. 4.13

![Diagram of a circular chain with two masses. One mass is at the top, and the other is at the bottom. A driving force F_d(t) is applied to the top mass, indicated by a double-headed arrow pointing left.](e67bd1eef75ab1b489af59c1a5fe9215_img.jpg)

Diagram of a circular chain with two masses. One mass is at the top, and the other is at the bottom. A driving force F\_d(t) is applied to the top mass, indicated by a double-headed arrow pointing left.

Fig. 4.14

![Diagram of a circular chain with two masses. One mass is at the top, and the other is at the bottom. No external force is shown.](87e5adbfccf31dbbe105638f43a04302_img.jpg)

Diagram of a circular chain with two masses. One mass is at the top, and the other is at the bottom. No external force is shown.

Fig. 4.15

![Diagram of a circular chain with three masses. One mass is at the top, and two are at the bottom, forming an equilateral triangle.](951327e0d4c60bc8d7ce7af25e0801cc_img.jpg)

Diagram of a circular chain with three masses. One mass is at the top, and two are at the bottom, forming an equilateral triangle.

Fig. 4.16

larger than the spring constant,  $\kappa$ , of the middle spring. Let  $x_1$  and  $x_2$  be the positions of the left and right masses, respectively, relative to their equilibrium positions. If the initial positions are given by  $x_1(0) = a$  and  $x_2(0) = 0$ , and if both masses are released from rest, show that  $x_1$  and  $x_2$  can be written as (assuming  $\kappa \ll k$ )

$$\begin{aligned} x_1(t) &\approx a \cos((\omega + \epsilon)t) \cos(\epsilon t), \\ x_2(t) &\approx a \sin((\omega + \epsilon)t) \sin(\epsilon t), \end{aligned} \quad (4.59)$$

where  $\omega \equiv \sqrt{k/m}$  and  $\epsilon \equiv (\kappa/2k)\omega$ . Explain qualitatively what the motion looks like.

### 4.11. Driven mass on a circle \*\*

Two identical masses  $m$  are constrained to move on a horizontal hoop. Two identical springs with spring constant  $k$  connect the masses and wrap around the hoop (see Fig. 4.14). One mass is subject to a driving force  $F_d \cos \omega_d t$ . Find the particular solution for the motion of the masses.

### 4.12. Springs on a circle \*\*\*\*

- Two identical masses  $m$  are constrained to move on a horizontal hoop. Two identical springs with spring constant  $k$  connect the masses and wrap around the hoop (see Fig. 4.15). Find the normal modes.
- Three identical masses are constrained to move on a hoop. Three identical springs connect the masses and wrap around the hoop (see Fig. 4.16). Find the normal modes.
- Now do the general case with  $N$  identical masses and  $N$  identical springs.

### 4.7 Exercises

### Section 4.1: Linear differential equations

### 4.13. $kx$ force \*

A particle of mass  $m$  is subject to a force  $F(x) = kx$ , with  $k > 0$ . What is the most general form of  $x(t)$ ? If the particle starts out at  $x_0$ , what is the one special value of the initial velocity for which the particle doesn't eventually get far away from the origin?

### 4.14. Rope on a pulley \*\*

A rope with length  $L$  and mass density  $\sigma$  kg/m hangs over a massless pulley. Initially, the ends of the rope are a distance  $x_0$  above and below their average position. The rope is given an initial speed. If you want

the rope to not eventually fall off the pulley, what should this initial speed be? (Don't worry about the issue discussed in Calkin (1989).)

### Section 4.2: Simple harmonic motion

### 4.15. Amplitude \*

Find the amplitude of the motion given by  $x(t) = C \cos \omega t + D \sin \omega t$ .

### 4.16. Angled rails \*

Two particles of mass  $m$  are constrained to move along two horizontal frictionless rails that make an angle  $2\theta$  with respect to each other. They are connected by a spring with spring constant  $k$ , whose relaxed length is at the position shown in Fig. 4.17. What is the frequency of oscillations for the motion where the spring remains parallel to the position shown?

![Diagram for Fig. 4.17: Two particles of mass m are on rails that meet at a vertex with an angle 2θ. A spring with constant k connects the two particles.](ff2a9e2d096b7106da4a2aaaee50266b_img.jpg)

Diagram for Fig. 4.17: Two particles of mass m are on rails that meet at a vertex with an angle 2θ. A spring with constant k connects the two particles.

Fig. 4.17

### 4.17. Effective spring constant \*

- Two springs with spring constants  $k_1$  and  $k_2$  are connected in parallel, as shown in Fig. 4.18. What is the effective spring constant,  $k_{\text{eff}}$ ? In other words, if the mass is displaced by  $x$ , find the  $k_{\text{eff}}$  for which the force equals  $F = -k_{\text{eff}}x$ .
- Two springs with spring constants  $k_1$  and  $k_2$  are connected in series, as shown in Fig. 4.19. What is the effective spring constant,  $k_{\text{eff}}$ ?

![Diagram for Fig. 4.18: Two springs with constants k1 and k2 are connected in parallel between a wall and a mass.](94a42e39f7a5c70ed0d2a92b928db8cd_img.jpg)

Diagram for Fig. 4.18: Two springs with constants k1 and k2 are connected in parallel between a wall and a mass.

Fig. 4.18

![Diagram for Fig. 4.19: Two springs with constants k1 and k2 are connected in series between a wall and a mass.](96b9f0390c5dc3a0839cacec2021fdd4_img.jpg)

Diagram for Fig. 4.19: Two springs with constants k1 and k2 are connected in series between a wall and a mass.

Fig. 4.19

### 4.18. Changing $k$ \*\*

Two springs each have spring constant  $k$  and equilibrium length  $\ell$ . They are both stretched a distance  $\ell$  and attached to a mass  $m$  and two walls, as shown in Fig. 4.20. At a given instant, the right spring constant is somehow magically changed to  $3k$  (the relaxed length remains  $\ell$ ). What is the resulting  $x(t)$ ? Take the initial position to be  $x = 0$ .

![Diagram for Fig. 4.20: A mass m is between two walls. The left spring has constant k and length 2l. The right spring has constant k (initially) and length 2l. An arrow indicates the right spring constant changes to 3k.](0b0a64422efb42aa8fc431ab081ad945_img.jpg)

Diagram for Fig. 4.20: A mass m is between two walls. The left spring has constant k and length 2l. The right spring has constant k (initially) and length 2l. An arrow indicates the right spring constant changes to 3k.

Fig. 4.20

### 4.19. Removing a spring \*\*

The springs in Fig. 4.21 are at their equilibrium length. The mass oscillates along the line of the springs with amplitude  $d$ . At the moment (let this be  $t = 0$ ) when the mass is at position  $x = d/2$  (and moving to the right), the right spring is removed. What is the resulting  $x(t)$ ? What is the amplitude of the new oscillation?

![Diagram for Fig. 4.21: A mass m is between two walls, connected by two springs, each with constant k.](eb9c8d229f1abe4571bdf3f5c8d3e7a4_img.jpg)

Diagram for Fig. 4.21: A mass m is between two walls, connected by two springs, each with constant k.

Fig. 4.21

### 4.20. Springs all over \*\*

- A mass  $m$  is attached to two springs that have relaxed lengths of zero. The other ends of the springs are fixed at two points (see Fig. 4.22). The two spring constants are equal. The mass sits at its equilibrium position and is then given a kick in an arbitrary

![Diagram for Fig. 4.22: A mass m is between two fixed points, connected by two springs, each with constant k.](46ded23c8fa31aabb0c45af6d7fb9e53_img.jpg)

Diagram for Fig. 4.22: A mass m is between two fixed points, connected by two springs, each with constant k.

Fig. 4.22

![Diagram for Fig. 4.23: A central point is connected to five springs, each ending in a star. The springs are arranged in a star-like pattern, radiating outwards from the central point.](219009f5013fbd979c7b7bcc7786a193_img.jpg)

Diagram for Fig. 4.23: A central point is connected to five springs, each ending in a star. The springs are arranged in a star-like pattern, radiating outwards from the central point.

Fig. 4.23

direction. Describe the resulting motion. (Ignore gravity, although you actually don't need to.)

- (b) A mass  $m$  is attached to  $n$  springs that have relaxed lengths of zero. The other ends of the springs are fixed at various points in space (see Fig. 4.23). The spring constants are  $k_1, k_2, \dots, k_n$ . The mass sits at its equilibrium position and is then given a kick in an arbitrary direction. Describe the resulting motion. (Again, ignore gravity, although you actually don't need to.)

![Diagram for Fig. 4.24: A mass hangs from a ceiling. A dashed box with a question mark is placed around the mass, obscuring three strings and two springs. Two other strings protrude from behind the paper. A solid line connects the ceiling to the top of the dashed box, and another solid line connects the bottom of the dashed box to a solid square mass.](cfd3c090804f99cfa7d80cba273e112b_img.jpg)

Diagram for Fig. 4.24: A mass hangs from a ceiling. A dashed box with a question mark is placed around the mass, obscuring three strings and two springs. Two other strings protrude from behind the paper. A solid line connects the ceiling to the top of the dashed box, and another solid line connects the bottom of the dashed box to a solid square mass.

Fig. 4.24

### 4.21. Rising up \*\*\*

In Fig. 4.24, a mass hangs from a ceiling. A piece of paper is held up to obscure three strings and two springs; all you see is two other strings protruding from behind the paper, as shown. How should the three strings and two springs be attached to each other and to the two visible strings (different items can be attached only at their endpoints) so that if you start with the system at its equilibrium position and then cut a certain one of the hidden strings, the mass will rise up?<sup>5</sup>

### 4.22. Projectile on a spring \*\*\*

A projectile of mass  $m$  is fired from the origin at speed  $v_0$  and angle  $\theta$ . It is attached to the origin by a spring with spring constant  $k$  and relaxed length zero.

- Find  $x(t)$  and  $y(t)$ .
- Show that for small  $\omega \equiv \sqrt{k/m}$ , the trajectory reduces to normal projectile motion. And show that for large  $\omega$ , the trajectory reduces to simple harmonic motion, that is, oscillatory motion along a line (at least before the projectile smashes back into the ground). What are the more meaningful statements that should replace “small  $\omega$ ” and “large  $\omega$ ”?
- What value should  $\omega$  take so that the projectile hits the ground when it is moving straight downward?

### 4.23. Corrections to the pendulum \*\*\*

- For small oscillations, the period of a pendulum is approximately  $T \approx 2\pi\sqrt{\ell/g}$ , independent of the amplitude,  $\theta_0$ . For finite oscillations, use  $dt = dx/v$  to show that the exact expression for  $T$  is

$$T = \sqrt{\frac{8\ell}{g}} \int_0^{\theta_0} \frac{d\theta}{\sqrt{\cos\theta - \cos\theta_0}}. \quad (4.60)$$

<sup>5</sup> Thanks to Paul Horowitz for this extremely cool problem. For more applications of the idea behind it, see Cohen and Horowitz (1991).

- (b) Find an approximation to this  $T$ , up to second order in  $\theta_0^2$ , in the following way. Make use of the identity  $\cos \phi = 1 - 2 \sin^2(\phi/2)$  to write  $T$  in terms of sines (because it's more convenient to work with quantities that go to zero as  $\theta \rightarrow 0$ ). Then make the change of variables,  $\sin x \equiv \sin(\theta/2) / \sin(\theta_0/2)$  (you'll see why). Finally, expand your integrand in powers of  $\theta_0$ , and perform the integrals to show that<sup>6</sup>

$$T \approx 2\pi \sqrt{\frac{\ell}{g}} \left( 1 + \frac{\theta_0^2}{16} + \dots \right). \quad (4.61)$$

## Section 4.3: Damped harmonic motion

### 4.24. Crossing the origin

Show that an overdamped or critically damped oscillator can cross the origin at most once.

### 4.25. Strong damping \*

In the strong damping ( $\gamma \gg \omega$ ) case discussed in the remark in the overdamping subsection, we saw that  $x(t) \propto e^{-\omega^2 t / 2\gamma}$ . Using the definitions of  $\omega$  and  $\gamma$ , this can be written as  $x(t) \propto e^{-kt/b}$ , where  $b$  is the coefficient of the damping force. By looking at the forces on the mass, explain why this makes sense.

### 4.26. Maximum speed \*

A critically damped oscillator with natural frequency  $\omega$  starts out at position  $x_0 > 0$ . What is the maximum initial speed (directed toward the origin) it can have and not cross the origin?

### 4.27. Another maximum speed \*\*

An overdamped oscillator with natural frequency  $\omega$  and damping coefficient  $\gamma$  starts out at position  $x_0 > 0$ . What is the maximum initial speed (directed toward the origin) it can have and not cross the origin?

### 4.28. Ratio of maxima \*\*

A mass on the end of a spring is released from rest at position  $x_0$ . The experiment is repeated, but now with the system immersed in a fluid that causes the motion to be critically damped. Show that the maximum speed of the mass in the first case is  $e$  times the maximum speed in the second case.<sup>7</sup>

<sup>6</sup> If you like this sort of thing, you can show that the next term in the parentheses is  $(11/3072)\theta_0^4$ . But be careful, this fourth-order correction comes from two terms.

<sup>7</sup> The fact that the maximum speeds differ by a fixed numerical factor follows from dimensional analysis, which tells us that the maximum speed in the first case must be proportional to  $\omega x_0$ . And

### Section 4.4: Driven (and damped) harmonic motion

### 4.29. Resonance

Given  $\omega$  and  $\gamma$ , show that the  $R$  in Eq. (4.33) is minimum when  $\omega_d = \sqrt{\omega^2 - 2\gamma^2}$  (unless this is imaginary, in which case the minimum occurs at  $\omega_d = 0$ ).

### 4.30. No damping force \*

A particle of mass  $m$  is subject to a spring force,  $-kx$ , and also a driving force,  $F_d \cos \omega_d t$ . But there is no damping force. Find the particular solution for  $x(t)$  by guessing  $x(t) = A \cos \omega_d t + B \sin \omega_d t$ . If you write this in the form  $C \cos(\omega_d t - \phi)$ , where  $C > 0$ , what are  $C$  and  $\phi$ ? Be careful about the phase (there are two cases to consider).

![Diagram of two masses m connected by two springs k to a wall.](119c104614ae02ce4c43bb8866c2ecbe_img.jpg)

A diagram showing a vertical wall on the left. Two springs, each labeled 'k', are connected in series to the wall. Two masses, each labeled 'm', are attached to the ends of the springs. The first mass is between the two springs, and the second mass is at the free end.

Diagram of two masses m connected by two springs k to a wall.

## Section 4.5: Coupled oscillators

### 4.31. Springs and one wall \*\*

Two identical springs and two identical masses are attached to a wall as shown in Fig. 4.25. Find the normal modes, and show that the frequencies can be written as  $\sqrt{k/m}(\sqrt{5} \pm 1)/2$ . This numerical factor is the golden ratio (and its inverse).

![Diagram of two masses m connected by three springs k to a wall.](a7831f13f35802b185dfa3f52740b4c1_img.jpg)

A diagram showing a vertical wall on the left. Three springs, each labeled 'k', are connected in series to the wall. Three masses, each labeled 'm', are attached to the ends of the springs. The first mass is between the first and second springs, the second mass is between the second and third springs, and the third mass is at the free end.

Diagram of two masses m connected by three springs k to a wall.

### 4.32. Springs between walls \*\*

Four identical springs and three identical masses lie between two walls (see Fig. 4.26). Find the normal modes.

Fig. 4.26

![Diagram of two beads on angled rails connected by a spring.](2e0e56ec50486c0a146d85ade11bf3fa_img.jpg)

A diagram showing two rails that meet at a point and diverge at an angle  $\theta$ . Two beads, each labeled 'm', are placed on the rails. A spring with spring constant 'k' connects the two beads. The rails are frictionless.

Diagram of two beads on angled rails connected by a spring.

### 4.33. Beads on angled rails \*\*

Two horizontal frictionless rails make an angle  $\theta$  with each other, as shown in Fig. 4.27. Each rail has a bead of mass  $m$  on it, and the beads are connected by a spring with spring constant  $k$  and relaxed length zero. Assume that one of the rails is positioned a tiny distance above the other, so that the beads can pass freely through the crossing. Find the normal modes.

Fig. 4.27

### 4.34. Coupled and damped \*\*

The system in the example in Section 4.5 is modified by immersing it in a fluid so that both masses feel a damping force,  $F_f = -bv$ . Solve for  $x_1(t)$  and  $x_2(t)$ . Assume underdamping.

### 4.35. Coupled and driven \*\*

The system in the example in Section 4.5 is modified by subjecting the left mass to a driving force  $F_d \cos(2\omega t)$ , and the right mass to a driving

since  $\gamma = \omega$  in the critical-damping case, the damping doesn't introduce a new parameter, so the maximum speed has no choice but to again be proportional to  $\omega x_0$ . But showing that the maximum speeds differ by the nice factor of  $e$  requires a calculation.

force  $2F_d \cos(2\omega t)$ , where  $\omega = \sqrt{k/m}$ . Find the particular solution for  $x_1(t)$  and  $x_2(t)$ , and explain why your answer makes sense.

## 4.8 Solutions

### 4.1. Superposition

The sum  $x_1 + x_2$  is a solution to  $\ddot{x}^2 = bx$  if

$$\begin{aligned} \left( \frac{d^2(x_1 + x_2)}{dt^2} \right)^2 &= b(x_1 + x_2) \\ \iff (\ddot{x}_1 + \ddot{x}_2)^2 &= b(x_1 + x_2) \\ \iff \ddot{x}_1^2 + 2\ddot{x}_1\ddot{x}_2 + \ddot{x}_2^2 &= b(x_1 + x_2). \end{aligned} \quad (4.62)$$

But  $\ddot{x}_1^2 = bx_1$  and  $\ddot{x}_2^2 = bx_2$ , by assumption. So we are left with the  $2\ddot{x}_1\ddot{x}_2$  term on the left-hand side, which destroys the equality. (Note that  $2\ddot{x}_1\ddot{x}_2$  can't be zero, because if either  $\ddot{x}_1$  or  $\ddot{x}_2$  is identically zero, then either  $x_1$  or  $x_2$  is also, so we didn't really have a solution to begin with.)

### 4.2. A limiting case

The expression " $a \rightarrow 0$ " is sloppy because  $a$  has units of inverse time squared, and the number 0 has no units. The proper statement is that Eq. (4.2) reduces to  $x(t) = C + Dt$  when  $\sqrt{a}t \ll 1$ , or equivalently when  $t \ll 1/\sqrt{a}$ , which is now a comparison of quantities with the same units. The smaller  $a$  is, the larger  $t$  can be. Therefore, if " $a \rightarrow 0$ ," then  $t$  can basically be anything. Assuming  $\sqrt{a}t \ll 1$ , we can write  $e^{\pm\sqrt{a}t} \approx 1 \pm \sqrt{a}t$ , and Eq. (4.2) becomes

$$\begin{aligned} x(t) &\approx A(1 + \sqrt{a}t) + B(1 - \sqrt{a}t) \\ &= (A + B) + \sqrt{a}(A - B)t \\ &\equiv C + Dt. \end{aligned} \quad (4.63)$$

$C$  is the initial position, and  $D$  is the speed of the particle. If these quantities are of order 1 in the units chosen, then if we solve for  $A$  and  $B$ , we see that they must be roughly negatives of each other, and both of order  $1/\sqrt{a}$ . So if the speed and initial position are of order 1, then  $A$  and  $B$  actually diverge in the " $a \rightarrow 0$ " limit. If  $a$  is small but nonzero, then  $t$  will eventually become large enough so that  $\sqrt{a}t \ll 1$  won't hold, in which case the linear form in Eq. (4.63) won't be valid.

### 4.3. Increasing the mass

The first thing we must do is find the velocity of the mass right before the collision. The motion before the collision looks like  $x(t) = d \cos(\omega t + \phi)$ , where  $\omega = \sqrt{k/m}$ . The collision happens at  $t = 0$  (although it actually doesn't matter what time we plug in here), so we have  $d/2 = x(0) = d \cos \phi$ , which gives  $\phi = \pm\pi/3$ . The velocity right before the collision is therefore

$$v(0) \equiv \dot{x}(0) = -\omega d \sin \phi = -\omega d \sin(\pm\pi/3) = \mp(\sqrt{3}/2)\omega d. \quad (4.64)$$

We want the plus sign, because we are told that the mass is moving to the right. Finding the motion after the collision is now reduced to an initial conditions problem. We have a mass  $2m$  on a spring with spring constant  $k$ , with initial position  $d/2$  and initial velocity  $(\sqrt{3}/4)\omega d$  (half of the result above). In situations where we know the initial position and velocity, it turns out that the best form to use for  $x(t)$  from the expressions in Eq. (4.3) is

$$x(t) = C \cos \omega' t + D \sin \omega' t, \quad (4.65)$$

because the initial position at  $t = 0$  is simply  $C$ , and the initial velocity at  $t = 0$  is  $\omega'D$ . The initial conditions are therefore easy to apply. We have put a prime on the frequency in Eq. (4.65) to remind us that it is different from the initial frequency, because the mass is now  $2m$ . So we have  $\omega' = \sqrt{k/2m} = \omega/\sqrt{2}$ . The initial conditions therefore give

$$\begin{aligned} x(0) = d/2 &\implies C = d/2, \\ v(0) = (\sqrt{3}/4)\omega d &\implies \omega'D = (\sqrt{3}/4)\omega d \implies D = (\sqrt{6}/4)d. \end{aligned} \quad (4.66)$$

Our solution for  $x(t)$  is therefore

$$x(t) = \frac{d}{2} \cos \omega't + \frac{\sqrt{6}d}{4} \sin \omega't, \quad \text{where } \omega' = \sqrt{\frac{k}{2m}}. \quad (4.67)$$

To find the amplitude, we must calculate the maximum value of  $x(t)$ . This is the task of Exercise 4.15, and the result is that the amplitude of the  $x(t) = C \cos \omega't + D \sin \omega't$  motion is  $A = \sqrt{C^2 + D^2}$ . So we have

$$A = \sqrt{\frac{d^2}{4} + \frac{6d^2}{16}} = \sqrt{\frac{5}{8}} d. \quad (4.68)$$

This is smaller than the original amplitude  $d$ , because energy is lost to heat during the collision (but energy is one of the topics of the next chapter).

### 4.4. Average tension

Let the length of the pendulum be  $\ell$ . We know that the angle  $\theta$  depends on time according to

$$\theta(t) = A \cos(\omega t), \quad (4.69)$$

where  $\omega = \sqrt{g/\ell}$ . If  $T$  is the tension in the string, then the radial  $F = ma$  equation is  $T - mg \cos \theta = m\ell\dot{\theta}^2$ . Using Eq. (4.69), this becomes

$$T = mg \cos(A \cos(\omega t)) + m\ell(-\omega A \sin(\omega t))^2. \quad (4.70)$$

Since  $A$  is small, we can use the small-angle approximation  $\cos \alpha \approx 1 - \alpha^2/2$ , which gives

$$\begin{aligned} T &\approx mg \left( 1 - \frac{1}{2} A^2 \cos^2(\omega t) \right) + m\ell\omega^2 A^2 \sin^2(\omega t) \\ &= mg + mgA^2 \left( \sin^2(\omega t) - \frac{1}{2} \cos^2(\omega t) \right), \end{aligned} \quad (4.71)$$

where we have made use of  $\omega^2 = g/\ell$ . The average value of both  $\sin^2 \theta$  and  $\cos^2 \theta$  over one period is 1/2 (you can show this by doing the integrals, or you can just note that the averages are equal and they add up to 1), so the average value of  $T$  is

$$T_{\text{avg}} = mg + \frac{mgA^2}{4}, \quad (4.72)$$

which is larger than  $mg$ , by  $mgA^2/4$ . It makes sense that  $T_{\text{avg}} > mg$ , because the average value of the vertical component of  $T$  equals  $mg$  (because the pendulum has no net rise or fall over a long period of time), and there is some nonzero contribution to the magnitude of  $T$  from the horizontal component.

### 4.5. Walking east on a turntable

The velocity of the person with respect to the ground is the sum of  $v\hat{x}$  and  $\mathbf{u}$ , where  $\mathbf{u}$  is the velocity (at the person's position) of the turntable with respect to the ground.

In terms of the angle  $\theta$  in Fig. 4.28, the velocity components with respect to the ground are

$$\dot{x} = v - u \sin \theta, \quad \text{and} \quad \dot{y} = u \cos \theta. \quad (4.73)$$

But  $u = r\omega$ . So we have, using  $r \sin \theta = y$  and  $r \cos \theta = x$ ,

$$\dot{x} = v - \omega y, \quad \text{and} \quad \dot{y} = \omega x. \quad (4.74)$$

Taking the derivative of the first equation, and then plugging in  $\dot{y}$  from the second, gives  $\ddot{x} = -\omega^2 x$ . Therefore,  $x(t) = A \cos(\omega t + \phi)$ . The first equation then quickly gives  $y(t)$ , and the result is that the general expression for the person's position is

$$(x, y) = (A \cos(\omega t + \phi), A \sin(\omega t + \phi) + v/\omega). \quad (4.75)$$

This describes a circle centered at the point  $(0, v/\omega)$ . The constants  $A$  and  $\phi$  are determined by the initial  $x$  and  $y$  values. You can show that

$$A = \sqrt{x_0^2 + (y_0 - v/\omega)^2}, \quad \text{and} \quad \tan \phi = \frac{y_0 - v/\omega}{x_0}. \quad (4.76)$$

**REMARKS:** It turns out that in the frame of the turntable, the person's path is also a circle. This can be seen in the following way. Imagine a distant object (say, a star) located in the eastward direction. In the frame of the turntable, this star rotates clockwise with frequency  $\omega$ . And in the frame of the turntable, the person's velocity always points toward the star. Therefore, the person's velocity rotates clockwise with frequency  $\omega$ . And since the magnitude of the velocity is constant, this means that the person travels clockwise in a circle in the frame of the turntable. From the usual expression  $v = r\omega$ , we see that this circle has a radius  $v/\omega$ .

This result leads to another way of showing that the person's path is a circle as viewed in the ground frame. In short, when the person's clockwise circular motion at speed  $v$  with respect to the turntable is combined with the counterclockwise motion of the turntable with respect to the ground (with the same frequency  $\omega$ , but in the opposite direction), the resulting motion of the person with respect to the ground is a circle with its center at the point  $(0, v/\omega)$ .

The situation is summarized in Fig. 4.29. From the above result (that the path is a circle in the turntable frame), we may characterize the person's motion in the turntable frame by imagining her riding on a merry-go-round that rotates clockwise with frequency  $\omega$  with respect to the turntable. This merry-go-round is shown at five different times in the figure. The effect of the merry-go-round's clockwise rotational motion is to cancel the counterclockwise rotation of the turntable, so that the merry-go-round ends up not rotating at all with respect to the ground. Therefore, if the person (the dot in the figure) starts at the top of the merry-go-round (which she in fact does, because this corresponds to walking eastward with respect to the turntable), then she always remains at the top. She therefore travels in a circle that is simply shifted upward by the vertical radius of the merry-go-round (the dotted lines shown, which have length  $v/\omega$ ), relative to the center of the turntable. This agrees with the original result. You can also see from the figure how the values of  $A$  and  $\phi$  in Eq. (4.76) arise. For example,  $A$  is the length of the solid lines shown. ♣

### 4.6. Maximum speed

For the undamped case, the general form of  $x$  is  $x(t) = C \cos(\omega t + \phi)$ . The initial condition  $v(0) = 0$  tells us that  $\phi = 0$ , and then the initial condition  $x(0) = x_0$  tells us that  $C = x_0$ . Therefore,  $x(t) = x_0 \cos(\omega t)$ , and so  $v(t) = -\omega x_0 \sin(\omega t)$ . This has a maximum magnitude of  $\omega x_0$ .

Now consider the overdamped case. Equation (4.17) gives the position as

$$x(t) = Ae^{-(\gamma-\Omega)t} + Be^{-(\gamma+\Omega)t}. \quad (4.77)$$

![Figure 4.28: A diagram showing a circle centered at the origin. A point on the circle is at a distance r from the origin, making an angle theta with the positive x-axis. A velocity vector v is shown tangent to the circle at this point, pointing in the counter-clockwise direction. A velocity vector u is shown pointing from the point towards the center of the circle. An arrow labeled 'east' points to the right, and a curved arrow labeled omega indicates counter-clockwise rotation.](aaa04a620f8665549055d31f84bdd94e_img.jpg)

Figure 4.28: A diagram showing a circle centered at the origin. A point on the circle is at a distance r from the origin, making an angle theta with the positive x-axis. A velocity vector v is shown tangent to the circle at this point, pointing in the counter-clockwise direction. A velocity vector u is shown pointing from the point towards the center of the circle. An arrow labeled 'east' points to the right, and a curved arrow labeled omega indicates counter-clockwise rotation.

Fig. 4.28

![Figure 4.29: A diagram showing a large circle representing the turntable. Inside it, five smaller circles represent a merry-go-round at different times. A dot representing a person is always at the top of each small circle. Dotted lines connect the centers of the small circles to the center of the large circle, and they are all vertical. Solid lines connect the centers of the small circles to the dot, and they are all horizontal. Arrows labeled 'east' and omega indicate the directions of motion.](d5baf0a024b6c0ea9f99a83b6432eaa3_img.jpg)

Figure 4.29: A diagram showing a large circle representing the turntable. Inside it, five smaller circles represent a merry-go-round at different times. A dot representing a person is always at the top of each small circle. Dotted lines connect the centers of the small circles to the center of the large circle, and they are all vertical. Solid lines connect the centers of the small circles to the dot, and they are all horizontal. Arrows labeled 'east' and omega indicate the directions of motion.

Fig. 4.29

The initial conditions are

$$\begin{aligned} x(0) = x_0 &\implies A + B = x_0, \\ v(0) = 0 &\implies -(\gamma - \Omega)A - (\gamma + \Omega)B = 0. \end{aligned} \quad (4.78)$$

Solving these equations for  $A$  and  $B$ , and then plugging the results into Eq. (4.77), gives

$$x(t) = \frac{x_0}{2\Omega} \left( (\gamma + \Omega)e^{-(\gamma - \Omega)t} - (\gamma - \Omega)e^{-(\gamma + \Omega)t} \right). \quad (4.79)$$

Taking the derivative to find  $v(t)$ , and using  $\gamma^2 - \Omega^2 = \omega^2$ , gives

$$v(t) = \frac{-\omega^2 x_0}{2\Omega} \left( e^{-(\gamma - \Omega)t} - e^{-(\gamma + \Omega)t} \right). \quad (4.80)$$

Taking the derivative again, we find that the maximum speed occurs at

$$t_{\max} = \frac{1}{2\Omega} \ln \left( \frac{\gamma + \Omega}{\gamma - \Omega} \right). \quad (4.81)$$

Plugging this into Eq. (4.80), and taking advantage of the logs in the exponentials, gives

$$\begin{aligned} v(t_{\max}) &= \frac{-\omega^2 x_0}{2\Omega} \exp \left( -\frac{\gamma}{2\Omega} \ln \left( \frac{\gamma + \Omega}{\gamma - \Omega} \right) \right) \left( \sqrt{\frac{\gamma + \Omega}{\gamma - \Omega}} - \sqrt{\frac{\gamma - \Omega}{\gamma + \Omega}} \right) \\ &= -\omega x_0 \left( \frac{\gamma - \Omega}{\gamma + \Omega} \right)^{\gamma/2\Omega}. \end{aligned} \quad (4.82)$$

The desired ratio,  $R$ , of the maximum speeds in the two scenarios is therefore

$$R = \left( \frac{\gamma + \Omega}{\gamma - \Omega} \right)^{\gamma/2\Omega}. \quad (4.83)$$

In the limit of strong damping ( $\gamma \gg \omega$ ), we have  $\Omega \equiv \sqrt{\gamma^2 - \omega^2} \approx \gamma - \omega^2/2\gamma$ . So the ratio becomes

$$R \approx \left( \frac{2\gamma}{\omega^2/2\gamma} \right)^{1/2} = \frac{2\gamma}{\omega}. \quad (4.84)$$

In the limit of critical damping ( $\gamma \approx \omega$ ,  $\Omega \approx 0$ ), we have, with  $\Omega/\gamma \equiv \epsilon$ ,

$$R \approx \left( \frac{1 + \epsilon}{1 - \epsilon} \right)^{1/2\epsilon} \approx (1 + 2\epsilon)^{1/2\epsilon} \approx e, \quad (4.85)$$

in agreement with the result of Exercise 4.28 (the solution to which is much quicker than the one above, since you don't need to deal with all the  $\Omega$ 's). You can also show that in these two limits,  $t_{\max}$  equals  $\ln(2\gamma/\omega)/\gamma$  and  $1/\gamma \approx 1/\omega$ , respectively.

### 4.7. Exponential force

$F = ma$  gives  $\ddot{x} = a_0 e^{-bt}$ . Let's guess a particular solution of the form  $x(t) = Ce^{-bt}$ . Plugging this in gives  $C = a_0/b^2$ . And since the solution to the homogeneous equation  $\ddot{x} = 0$  is  $x(t) = At + B$ , the complete solution for  $x$  is

$$x(t) = \frac{a_0 e^{-bt}}{b^2} + At + B. \quad (4.86)$$

The initial condition  $x(0) = 0$  gives  $B = -a_0/b^2$ . And the initial condition  $v(0) = 0$  applied to  $v(t) = -a_0 e^{-bt}/b + A$  gives  $A = a_0/b$ . Therefore,

$$x(t) = a_0 \left( \frac{e^{-bt}}{b^2} + \frac{t}{b} - \frac{1}{b^2} \right), \quad (4.87)$$

in agreement with Problem 3.9.

### 4.8. Driven oscillator

Plugging  $x(t) = A \cos \omega_d t + B \sin \omega_d t$  into Eq. (4.29) gives

$$\begin{aligned} & -\omega_d^2 A \cos \omega_d t - \omega_d^2 B \sin \omega_d t \\ & - 2\gamma \omega_d A \sin \omega_d t + 2\gamma \omega_d B \cos \omega_d t \\ & + \omega^2 A \cos \omega_d t + \omega^2 B \sin \omega_d t = F \cos \omega_d t. \end{aligned} \quad (4.88)$$

If this is true for all  $t$ , the coefficients of  $\cos \omega_d t$  on both sides must be equal. And likewise for  $\sin \omega_d t$ . Therefore,

$$\begin{aligned} -\omega_d^2 A + 2\gamma \omega_d B + \omega^2 A &= F, \\ -\omega_d^2 B - 2\gamma \omega_d A + \omega^2 B &= 0. \end{aligned} \quad (4.89)$$

Solving this system of equations for  $A$  and  $B$  gives

$$A = \frac{F(\omega^2 - \omega_d^2)}{(\omega^2 - \omega_d^2)^2 + 4\gamma^2 \omega_d^2}, \quad B = \frac{2F\gamma \omega_d}{(\omega^2 - \omega_d^2)^2 + 4\gamma^2 \omega_d^2}, \quad (4.90)$$

in agreement with Eq. (4.31).

### 4.9. Unequal masses

Let  $x_1$  and  $x_2$  be the positions of the left and right masses, respectively, relative to their equilibrium positions. The forces on the two masses are  $-kx_1 + k(x_2 - x_1)$  and  $-kx_2 - k(x_2 - x_1)$ , respectively, so the  $F = ma$  equations are

$$\begin{aligned} \ddot{x}_1 + 2\omega^2 x_1 - \omega^2 x_2 &= 0, \\ 2\ddot{x}_2 + 2\omega^2 x_2 - \omega^2 x_1 &= 0. \end{aligned} \quad (4.91)$$

The appropriate linear combinations of these equations aren't obvious, so we'll use the determinant method. Letting  $x_1 = A_1 e^{i\alpha t}$  and  $x_2 = A_2 e^{i\alpha t}$ , we see that for there to be a nontrivial solution for  $A$  and  $B$ , we must have

$$\begin{aligned} 0 &= \begin{vmatrix} -\alpha^2 + 2\omega^2 & -\omega^2 \\ -\omega^2 & -2\alpha^2 + 2\omega^2 \end{vmatrix} \\ &= 2\alpha^4 - 6\alpha^2 \omega^2 + 3\omega^4. \end{aligned} \quad (4.92)$$

The roots of this quadratic equation in  $\alpha^2$  are

$$\alpha = \pm \omega \sqrt{\frac{3 + \sqrt{3}}{2}} \equiv \pm \alpha_1, \quad \text{and} \quad \alpha = \pm \omega \sqrt{\frac{3 - \sqrt{3}}{2}} \equiv \pm \alpha_2. \quad (4.93)$$

If  $\alpha^2 = \alpha_1^2$ , then the normal mode is proportional to  $(\sqrt{3} + 1, -1)$ . And if  $\alpha^2 = \alpha_2^2$ , then the normal mode is proportional to  $(\sqrt{3} - 1, 1)$ . So the normal modes are

$$\begin{aligned} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} &= \begin{pmatrix} \sqrt{3} + 1 \\ -1 \end{pmatrix} \cos(\alpha_1 t + \phi_1), \quad \text{and} \\ \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} &= \begin{pmatrix} \sqrt{3} - 1 \\ 1 \end{pmatrix} \cos(\alpha_2 t + \phi_2). \end{aligned} \quad (4.94)$$

Note that these two vectors are not orthogonal (there is no need for them to be). The normal coordinates associated with these normal modes are  $x_1 - (\sqrt{3} - 1)x_2$  and  $x_1 + (\sqrt{3} + 1)x_2$ , respectively, because these are the combinations that make the  $\alpha_2$  and  $\alpha_1$  frequencies disappear, respectively.

### 4.10. Weakly coupled

The magnitude of the force in the middle spring is  $\kappa(x_2 - x_1)$ , so the  $F = ma$  equations are

$$\begin{aligned} m\ddot{x}_1 &= -kx_1 + \kappa(x_2 - x_1), \\ m\ddot{x}_2 &= -kx_2 - \kappa(x_2 - x_1). \end{aligned} \quad (4.95)$$

Adding and subtracting these equations gives

$$\begin{aligned} m(\ddot{x}_1 + \ddot{x}_2) &= -k(x_1 + x_2) \implies x_1 + x_2 = A \cos(\omega t + \phi), \\ m(\ddot{x}_1 - \ddot{x}_2) &= -(k + 2\kappa)(x_1 - x_2) \implies x_1 - x_2 = B \cos(\tilde{\omega} t + \tilde{\phi}), \end{aligned} \quad (4.96)$$

where

$$\omega \equiv \sqrt{\frac{k}{m}}, \quad \text{and} \quad \tilde{\omega} \equiv \sqrt{\frac{k + 2\kappa}{m}}. \quad (4.97)$$

The initial conditions are  $x_1(0) = a$ ,  $\dot{x}_1(0) = 0$ ,  $x_2(0) = 0$ , and  $\dot{x}_2(0) = 0$ . The easiest way to apply these is to plug them into the normal coordinates in Eq. (4.96), before solving for  $x_1(t)$  and  $x_2(t)$ . The velocity conditions quickly give  $\phi = \tilde{\phi} = 0$ , and then the position conditions give  $A = B = a$ . Solving for  $x_1(t)$  and  $x_2(t)$  yields

$$\begin{aligned} x_1(t) &= \frac{a}{2} \cos(\omega t) + \frac{a}{2} \cos(\tilde{\omega} t), \\ x_2(t) &= \frac{a}{2} \cos(\omega t) - \frac{a}{2} \cos(\tilde{\omega} t). \end{aligned} \quad (4.98)$$

Writing  $\omega$  and  $\tilde{\omega}$  as

$$\omega = \frac{\tilde{\omega} + \omega}{2} - \frac{\tilde{\omega} - \omega}{2}, \quad \text{and} \quad \tilde{\omega} = \frac{\tilde{\omega} + \omega}{2} + \frac{\tilde{\omega} - \omega}{2}, \quad (4.99)$$

and using the identity  $\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$ , gives

$$\begin{aligned} x_1(t) &= a \cos\left(\frac{\tilde{\omega} + \omega}{2} t\right) \cos\left(\frac{\tilde{\omega} - \omega}{2} t\right), \\ x_2(t) &= a \sin\left(\frac{\tilde{\omega} + \omega}{2} t\right) \sin\left(\frac{\tilde{\omega} - \omega}{2} t\right). \end{aligned} \quad (4.100)$$

If we now approximate  $\tilde{\omega}$  as

$$\tilde{\omega} \equiv \sqrt{\frac{k + 2\kappa}{m}} = \sqrt{\frac{k}{m}} \sqrt{1 + \frac{2\kappa}{k}} \approx \omega \left(1 + \frac{\kappa}{k}\right) \equiv \omega + 2\epsilon, \quad (4.101)$$

where  $\epsilon \equiv (\kappa/2k)\omega = (\kappa/2m)\sqrt{m/k}$ , we can write  $x_1$  and  $x_2$  as

$$\begin{aligned} x_1(t) &\approx a \cos((\omega + \epsilon)t) \cos(\epsilon t), \\ x_2(t) &\approx a \sin((\omega + \epsilon)t) \sin(\epsilon t), \end{aligned} \quad (4.102)$$

as desired. To get an idea of what this motion looks like, let's examine  $x_1$ . Since  $\epsilon \ll \omega$ , the  $\cos(\epsilon t)$  oscillation is much slower than the  $\cos((\omega + \epsilon)t)$  oscillation. Therefore,  $\cos(\epsilon t)$  is essentially constant on the time scale of the  $\cos((\omega + \epsilon)t)$  oscillations. This means that for the time span of a few of these oscillations,  $x_1$  essentially oscillates with frequency  $\omega + \epsilon \approx \omega$  and amplitude  $a \cos(\epsilon t)$ . This  $a \cos(\epsilon t)$  term is the “envelope” of the oscillation, as shown in Fig. 4.30, for  $\epsilon/\omega = 1/10$ . Initially, the amplitude of  $x_1$  is  $a$ , but it decreases to zero when  $\epsilon t = \pi/2$ . By this time, the amplitude of the  $x_2$

![Figure 4.30: Two plots showing the time evolution of the displacement x1(t) and x2(t) for a weakly coupled oscillator system. The top plot shows x1(t) as a high-frequency oscillation (cos((omega + epsilon)t)) whose amplitude is modulated by a slower envelope function a cos(epsilon t). The amplitude starts at a and goes to zero at epsilon t = pi/2. The bottom plot shows x2(t) as a high-frequency oscillation (sin((omega + epsilon)t)) whose amplitude is modulated by a slower envelope function a sin(epsilon t). The amplitude starts at zero and reaches a at epsilon t = pi/2.](f3a30a3ddcf782cfcc565500c73110eb_img.jpg)

Figure 4.30: Two plots showing the time evolution of the displacement x1(t) and x2(t) for a weakly coupled oscillator system. The top plot shows x1(t) as a high-frequency oscillation (cos((omega + epsilon)t)) whose amplitude is modulated by a slower envelope function a cos(epsilon t). The amplitude starts at a and goes to zero at epsilon t = pi/2. The bottom plot shows x2(t) as a high-frequency oscillation (sin((omega + epsilon)t)) whose amplitude is modulated by a slower envelope function a sin(epsilon t). The amplitude starts at zero and reaches a at epsilon t = pi/2.

Fig. 4.30

oscillation, which is  $a \sin(\epsilon t)$ , has grown to  $a$ . So at  $t = \pi/2\epsilon$ , the right mass has all the motion, and the left mass is at rest. This process keeps repeating. After each time period of  $\pi/2\epsilon$ , the motion of one mass gets transferred to the other. The weaker the coupling (that is, the spring constant  $\kappa$ ) between the masses, the smaller the  $\epsilon$ , and so the longer the time period.

REMARKS: The above reasoning also holds for two pendulums connected by a weak spring. All the above steps carry through, with the only change being that  $k$  is replaced by  $mg/\ell$ , because the spring force,  $-kx$ , is replaced by the tangential gravitational force,  $-mg \sin \theta \approx -mg(x/\ell)$ . So after a time

$$t = \frac{\pi}{2\epsilon} = \frac{\pi}{2} \left( \frac{2m}{\kappa} \sqrt{\frac{k}{m}} \right) \rightarrow \frac{\pi m}{\kappa} \sqrt{\frac{g}{\ell}}, \quad (4.103)$$

the pendulum that was initially oscillating is now momentarily at rest, and the other pendulum has all the motion. Since the time scale,  $T_s$ , of a single mass on the end of the weak spring is proportional to  $\sqrt{m/\kappa}$ , and since the time scale,  $T_p$ , of a simple pendulum is proportional to  $\sqrt{\ell/g}$ , we see that the above  $t$  is proportional to  $T_s^2/T_p$ .

The existence of the “beats” in Fig. 4.30 can be traced to the fact that the expressions in Eq. (4.98) are linear combinations of sinusoidal functions with two very close frequencies. The physics here is the same as the physics that produces the beats you hear when listening to two musical notes of nearly the same pitch, as when tuning a guitar.<sup>8</sup> The time between the zeros of, say,  $x_1$  in Fig. 4.30 is  $\pi/\epsilon$ , so the angular frequency of the beats is  $2\pi/(\pi/\epsilon) = 2\epsilon$ . ♣

### 4.11. Driven mass on a circle

Label two diametrically opposite points as the equilibrium positions. Let the positions of the masses relative to these points be  $x_1$  and  $x_2$ , measured counterclockwise. If the driving force acts on mass “1,” then the  $F = ma$  equations are

$$\begin{aligned} m\ddot{x}_1 + 2k(x_1 - x_2) &= F_d \cos \omega_d t, \\ m\ddot{x}_2 + 2k(x_2 - x_1) &= 0. \end{aligned} \quad (4.104)$$

To solve these equations, we can treat the driving force as the real part of  $F_d e^{i\omega_d t}$  and try solutions of the form  $x_1(t) = A_1 e^{i\omega_d t}$  and  $x_2(t) = A_2 e^{i\omega_d t}$ , and then solve for  $A_1$  and  $A_2$ . Or we can try some trig functions. If we take the latter route, we quickly find that the solutions can’t involve any sine terms (this is due to the fact that there are no first derivatives of the  $x$ ’s in Eq. (4.104)). Therefore, the trig functions must look like  $x_1(t) = A_1 \cos \omega_d t$  and  $x_2(t) = A_2 \cos \omega_d t$ . Using either of the two methods, Eq. (4.104) becomes

$$\begin{aligned} -\omega_d^2 A_1 + 2\omega^2(A_1 - A_2) &= F, \\ -\omega_d^2 A_2 + 2\omega^2(A_2 - A_1) &= 0, \end{aligned} \quad (4.105)$$

where  $\omega \equiv \sqrt{k/m}$  and  $F \equiv F_d/m$ . Solving for  $A_1$  and  $A_2$ , we find that the desired particular solution is

$$x_1(t) = \frac{-F(2\omega^2 - \omega_d^2)}{\omega_d^2(4\omega^2 - \omega_d^2)} \cos \omega_d t, \quad x_2(t) = \frac{-2F\omega^2}{\omega_d^2(4\omega^2 - \omega_d^2)} \cos \omega_d t. \quad (4.106)$$

<sup>8</sup> If the two frequencies involved aren’t too close to each other, then you can actually hear a faint note with a frequency equal to the difference of the original frequencies (and possibly some other notes too, involving various combinations of the frequencies). But this is a different phenomenon from the above beats; it is due to the nonlinear way in which the ear works. See Hall (1981) for more details.

The most general solution is the sum of this particular solution and the homogeneous solution found in Eq. (4.111) in the solution to Problem 4.12 below.

#### REMARKS:

1. If  $\omega_d = 2\omega$ , the amplitudes of the motions go to infinity. This makes sense, considering that there is no damping, and that the natural frequency of the system (calculated in Problem 4.12) is  $2\omega$ .
2. If  $\omega_d = \sqrt{2}\omega$ , then the mass that is being driven doesn't move. The reason for this is that the driving force balances the force that the mass feels from the two springs due to the other mass's motion. And indeed, you can show that  $\sqrt{2}\omega$  is the frequency that one mass moves at if the other mass is at rest (and thereby acts essentially like a brick wall). Note that  $\omega_d = \sqrt{2}\omega$  is the cutoff between the masses moving in the same direction or in opposite directions.
3. If  $\omega_d \rightarrow \infty$ , then both motions go to zero. But  $x_2$  is fourth-order small, whereas  $x_1$  is only second-order small.
4. If  $\omega_d \rightarrow 0$ , then  $A_1 \approx A_2 \approx -F/2\omega_d^2$ , which is very large. The slowly changing driving force basically spins the masses around in one direction for a while, and then reverses and spins them around in the other direction. We essentially have the driving force acting on a mass  $2m$ , and two integrations of  $F_d \cos \omega_d t = (2m)\ddot{x}$  show that the amplitude of the motion is  $F/2\omega_d^2$ , as above. Equivalently, you can calculate the  $A_1 - A_2$  difference in the  $\omega_d \rightarrow 0$  limit to show that the springs stretch just the right amount to cause there to be a net force of  $(F_d/2) \cos \omega_d t$  on each mass. This leads to the same  $F/2\omega_d^2$  amplitude. ♣

### 4.12. Springs on a circle

- (a) Label two diametrically opposite points as the equilibrium positions. Let the positions of the masses relative to these points be  $x_1$  and  $x_2$ , measured counterclockwise. Then the  $F = ma$  equations are

$$\begin{aligned} m\ddot{x}_1 + 2k(x_1 - x_2) &= 0, \\ m\ddot{x}_2 + 2k(x_2 - x_1) &= 0. \end{aligned} \quad (4.107)$$

The determinant method works here, but let's just do it the easy way. Adding the equations gives

$$\ddot{x}_1 + \ddot{x}_2 = 0, \quad (4.108)$$

and subtracting them gives

$$(\ddot{x}_1 - \ddot{x}_2) + 4\omega^2(x_1 - x_2) = 0. \quad (4.109)$$

The normal coordinates are therefore

$$\begin{aligned} x_1 + x_2 &= At + B, \\ x_1 - x_2 &= C \cos(2\omega t + \phi). \end{aligned} \quad (4.110)$$

Solving these two equations for  $x_1$  and  $x_2$ , and writing the results in vector form, gives

$$\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} (At + B) + C \begin{pmatrix} 1 \\ -1 \end{pmatrix} \cos(2\omega t + \phi), \quad (4.111)$$

where the constants  $A$ ,  $B$ , and  $C$  are defined to be half of what they were in Eq. (4.110). The normal modes are therefore

$$\begin{aligned} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} &= \begin{pmatrix} 1 \\ 1 \end{pmatrix} (At + B), \quad \text{and} \\ \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} &= C \begin{pmatrix} 1 \\ -1 \end{pmatrix} \cos(2\omega t + \phi). \end{aligned} \quad (4.112)$$

The first mode has frequency zero. It corresponds to the masses sliding around the circle, equally spaced, at constant speed. The second mode has both masses moving to the left, then both to the right, back and forth. Each mass feels a force of  $4kx$  (because there are two springs, and each one stretches by  $2x$ ), hence the  $\sqrt{4} = 2$  in the frequency.

- (b) Label three equally spaced points as the equilibrium positions. Let the positions of the masses relative to these points be  $x_1$ ,  $x_2$ , and  $x_3$ , measured counterclockwise. Then the  $F = ma$  equations are, as you can show,

$$\begin{aligned} m\ddot{x}_1 + k(x_1 - x_2) + k(x_1 - x_3) &= 0, \\ m\ddot{x}_2 + k(x_2 - x_3) + k(x_2 - x_1) &= 0, \\ m\ddot{x}_3 + k(x_3 - x_1) + k(x_3 - x_2) &= 0. \end{aligned} \quad (4.113)$$

The sum of all three of these equations definitely gives something nice. Also, differences between any two of the equations give something useful. But let's use the determinant method to get some practice. Trying solutions of the form  $x_1 = A_1 e^{i\alpha t}$ ,  $x_2 = A_2 e^{i\alpha t}$ , and  $x_3 = A_3 e^{i\alpha t}$ , we obtain the matrix equation,

$$\begin{pmatrix} -\alpha^2 + 2\omega^2 & -\omega^2 & -\omega^2 \\ -\omega^2 & -\alpha^2 + 2\omega^2 & -\omega^2 \\ -\omega^2 & -\omega^2 & -\alpha^2 + 2\omega^2 \end{pmatrix} \begin{pmatrix} A_1 \\ A_2 \\ A_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}. \quad (4.114)$$

Setting the determinant equal to zero yields a cubic equation in  $\alpha^2$ . But it's a nice cubic equation, with  $\alpha^2 = 0$  as a solution. The other solution is the double root  $\alpha^2 = 3\omega^2$ .

The  $\alpha = 0$  root corresponds to  $A_1 = A_2 = A_3$ . That is, it corresponds to the vector  $(1, 1, 1)$ . This  $\alpha = 0$  case is the one case where our exponential solution isn't really an exponential. But  $\alpha^2$  equalling zero in Eq. (4.114) basically tells us that we're dealing with a function whose second derivative is zero, that is, a linear function  $At + B$ . Therefore, the normal mode is

$$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} (At + B). \quad (4.115)$$

This mode has frequency zero. It corresponds to the masses sliding around the circle, equally spaced, at constant speed.

The two  $\alpha^2 = 3\omega^2$  roots correspond to a two-dimensional subspace of normal modes. You can show that any vector of the form  $(a, b, c)$  with  $a + b + c = 0$  is a normal mode with frequency  $\sqrt{3}\omega$ . We will arbitrarily pick the vectors  $(0, 1, -1)$  and  $(1, 0, -1)$  as basis vectors for this space. We can then write the normal modes as linear combinations of the vectors

$$\begin{aligned} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} &= C_1 \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \cos(\sqrt{3}\omega t + \phi_1), \\ \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} &= C_2 \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \cos(\sqrt{3}\omega t + \phi_2). \end{aligned} \quad (4.116)$$

**REMARKS:** The  $\alpha^2 = 3\omega^2$  case is very similar to the example in Section 4.5 with two masses and three springs oscillating between two walls. The way we've written the two modes in Eq. (4.116), the first one has the first mass stationary (so there could be a wall there, for all the other two masses know). Similarly for the second mode. Hence the  $\sqrt{3}\omega$  result here, as in the example.

The normal coordinates in this problem are  $x_1 + x_2 + x_3$  (obtained by adding the three equations in (4.113)), and also any combination of the form  $ax_1 + bx_2 + cx_3$ , where  $a + b + c = 0$  (obtained by taking  $a$  times the first equation in Eq. (4.113), plus  $b$  times the second, plus  $c$  times the third). The three normal coordinates that correspond to the mode in Eq. (4.115) and the two modes we chose in Eq. (4.116) are, respectively,  $x_1 + x_2 + x_3$ ,  $x_1 - 2x_2 + x_3$ , and  $-2x_1 + x_2 + x_3$ , because each of these combinations gets no contribution from the other two modes (demanding this is how you can derive the coefficients of the  $x_i$ 's, up to an overall constant). ♣

- (c) In part (b), when we set the determinant of the matrix in Eq. (4.114) equal to zero, we were essentially finding the eigenvectors and eigenvalues<sup>9</sup> of the matrix,

$$\begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix} = 3I - \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}, \quad (4.117)$$

where  $I$  is the identity matrix. We haven't bothered writing the common factor  $\omega^2$  here, because it doesn't affect the eigenvectors. As an exercise, you can show that for the general case of  $N$  springs and  $N$  masses on a circle, the above matrix becomes the  $N \times N$  matrix,

$$3I - \begin{pmatrix} 1 & 1 & 0 & 0 & \dots & 1 \\ 1 & 1 & 1 & 0 & \dots & 0 \\ 0 & 1 & 1 & 1 & \dots & 0 \\ 0 & 0 & 1 & 1 & \dots & 0 \\ \vdots & & & & \ddots & \vdots \\ 1 & 0 & 0 & 0 & \dots & 1 \end{pmatrix} \equiv 3I - M. \quad (4.118)$$

In the matrix  $M$ , the three consecutive 1's keep shifting to the right, and they wrap around cyclicly. We must now find the eigenvectors of  $M$ , which will require being a little clever.

We can guess the eigenvectors and eigenvalues of  $M$  if we take a hint from its cyclic nature. A particular set of things that are rather cyclic are the  $N$ th roots of 1. If  $\beta$  is an  $N$ th root of 1, you can verify that  $(1, \beta, \beta^2, \dots, \beta^{N-1})$  is an eigenvector of  $M$  with eigenvalue  $\beta^{-1} + 1 + \beta$ . (This general method works for any matrix where the entries keep shifting to the right. The entries don't have to be equal.) The eigenvalues of the entire matrix in Eq. (4.118) are therefore  $3 - (\beta^{-1} + 1 + \beta) = 2 - \beta^{-1} - \beta$ . There are  $N$  different  $N$ th roots of 1, namely  $\beta_n = e^{2\pi i n/N}$ , for  $0 \leq n \leq N - 1$ . So the  $N$  eigenvalues are

$$\begin{aligned} \lambda_n &= 2 - \left( e^{-2\pi i n/N} + e^{2\pi i n/N} \right) = 2 - 2 \cos(2\pi n/N) \\ &= 4 \sin^2(\pi n/N). \end{aligned} \quad (4.119)$$

The corresponding eigenvectors are

$$V_n = \left( 1, \beta_n, \beta_n^2, \dots, \beta_n^{N-1} \right). \quad (4.120)$$

Since the numbers  $n$  and  $N - n$  yield the same value for  $\lambda_n$  in Eq. (4.119), the eigenvalues come in pairs (except for  $n = 0$ , and  $n = N/2$  if  $N$  is even). This is fortunate, because we can then form real linear combinations of the

<sup>9</sup> An eigenvector  $v$  of a matrix  $M$  is a vector that gets taken into a multiple of itself when acted upon by  $M$ . That is,  $Mv = \lambda v$ , where  $\lambda$  is some number (the eigenvalue). This can be rewritten as  $(M - \lambda I)v = 0$ , where  $I$  is the identity matrix. By our usual reasoning about invertible matrices, a nonzero vector  $v$  exists only if  $\lambda$  satisfies  $\det |M - \lambda I| = 0$ .

two corresponding complex eigenvectors given in Eq. (4.120). We see that the vectors

$$V_n^+ \equiv \frac{1}{2}(V_n + V_{N-n}) = \begin{pmatrix} 1 \\ \cos(2\pi n/N) \\ \cos(4\pi n/N) \\ \vdots \\ \cos(2(N-1)\pi n/N) \end{pmatrix} \quad (4.121)$$

and

$$V_n^- \equiv \frac{1}{2i}(V_n - V_{N-n}) = \begin{pmatrix} 0 \\ \sin(2\pi n/N) \\ \sin(4\pi n/N) \\ \vdots \\ \sin(2(N-1)\pi n/N) \end{pmatrix} \quad (4.122)$$

both have eigenvalue  $\lambda_n = \lambda_{N-n}$  (as does any linear combination of these vectors). For the special case of  $n = 0$ , the eigenvector is  $V_0 = (1, 1, 1, \dots, 1)$  with eigenvalue  $\lambda_0 = 0$ . And for the special case of  $n = N/2$  if  $N$  is even, the eigenvector is  $V_{N/2} = (1, -1, 1, \dots, -1)$  with eigenvalue  $\lambda_{N/2} = 4$ .

Referring back to the  $N = 3$  case in Eq. (4.114), we see that we must take the square root of the eigenvalues and then multiply by  $\omega$  to obtain the frequencies (because it was an  $\alpha^2$  that appeared in the matrix, and because we dropped the factor of  $\omega^2$ ). The frequency corresponding to the above two normal modes is therefore, using Eq. (4.119),

$$\omega_n = \omega\sqrt{\lambda_n} = 2\omega \sin(\pi n/N). \quad (4.123)$$

For even  $N$ , the largest value of the frequency is  $2\omega$ , with the masses moving in alternating equal positive and negative displacements. But for odd  $N$ , it is slightly less than  $2\omega$ .

To sum everything up, the  $N$  normal modes are the vectors in Eqs. (4.121) and (4.122), where  $n$  runs from 1 up to the greatest integer less than  $N/2$ . And then we have to add on the  $V_0$  vector, and also the  $V_{N/2}$  vector if  $N$  is even.<sup>10</sup> The frequencies are given in Eq. (4.123). Each frequency is associated with two modes, except the  $V_0$  mode and the  $V_{N/2}$  mode if  $N$  is even.

**REMARK:** Let's check our results for  $N = 2$  and  $N = 3$ . For  $N = 2$ : The values of  $n$  are the two “special” cases of  $n = 0$  and  $n = N/2 = 1$ . If  $n = 0$ , we have  $\omega_0 = 0$  and  $V_0 = (1, 1)$ . If  $n = 1$ , we have  $\omega_1 = 2\omega$  and  $V_1 = (1, -1)$ . These results agree with the two modes in Eq. (4.112).

For  $N = 3$ : If  $n = 0$ , we have  $\omega_0 = 0$  and  $V_0 = (1, 1, 1)$ , in agreement with Eq. (4.115). If  $n = 1$ , we have  $\omega_1 = \sqrt{3}\omega$ , and  $V_1^+ = (1, -1/2, -1/2)$  and  $V_1^- = (0, 1/2, -1/2)$ . These two vectors span the same space we found in Eq. (4.116). And they have the same frequency as in Eq. (4.116). You can also find the vectors for  $N = 4$ . These are fairly intuitive, so try to write them down first without using the above results. ♣

<sup>10</sup> If you want, you can treat the  $n = 0$  and  $n = N/2$  cases the same as all the others. But in both of these cases, the  $V^-$  vector is the zero vector, so you can ignore it. So no matter what route you take, you will end up with exactly  $N$  nontrivial eigenvectors.