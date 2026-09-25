# Chapter 1 Strategies for solving problems

Physics involves a great deal of problem solving. Whether you are doing cutting-edge research or reading a book on a well-known subject, you are going to need to solve some problems. In the latter case (the presently relevant one, given what is in your hand right now), it is fairly safe to say that the true test of understanding something is the ability to solve problems on it. Reading about a topic is often a necessary step in the learning process, but it is by no means a sufficient one. The more important step is spending as much time as possible solving problems (which is inevitably an active task) beyond the time you spend reading (which is generally a more passive task). I have therefore included a very large number of problems/exercises in this book.

However, if I'm going to throw all these problems at you, I should at least give you some general strategies for solving them. These strategies are the subject of the present chapter. They are things you should always keep in the back of your mind when tackling a problem. Of course, they are generally not sufficient by themselves; you won't get too far without understanding the physical concepts behind the subject at hand. But when you add these strategies to your physical understanding, they can make your life a lot easier.

## 1.1 General strategies

There are a number of general strategies you should invoke without hesitation when solving a problem. They are:

#### 1. **Draw a diagram, if appropriate.**

In the diagram, be sure to label clearly all the relevant quantities (forces, lengths, masses, etc.). Diagrams are absolutely critical in certain types of problems. For example, in problems involving “free-body” diagrams (discussed in Chapter 3) or relativistic kinematics (discussed in Chapter 11), drawing a diagram can change a hopelessly complicated problem into a near-trivial one. And even in cases where diagrams aren't this crucial, they're invariably very helpful. A picture is definitely worth a thousand words (and even a few more, if you label things!).

#### 2. Write down what you know, and what you are trying to find.

In a simple problem, you may just do this in your head without realizing it. But in more difficult problems, it is very useful to explicitly write things out. For example, if there are three unknowns that you're trying to find, but you've written down only two facts, then you know there must be another fact you're missing (assuming that the problem is in fact solvable), so you can go searching for it. It might be a conservation law, or an  $F = ma$  equation, etc.

#### 3. Solve things symbolically.

If you are solving a problem where the given quantities are specified numerically, you should immediately change the numbers to letters and solve the problem in terms of the letters. After you obtain an answer in terms of the letters, you can plug in the actual numerical values to obtain a numerical answer. There are many advantages to using letters:

- IT'S QUICKER. It's much easier to multiply a  $g$  by an  $\ell$  by writing them down on a piece of paper next to each other, than it is to multiply them together on a calculator. And with the latter strategy, you'd undoubtedly have to pick up your calculator at least a few times during the course of a problem.
- YOU'RE LESS LIKELY TO MAKE A MISTAKE. It's very easy to mistype an 8 for a 9 in a calculator, but you're probably not going to miswrite a  $q$  for a  $g$  on a piece of paper. But if you do, you'll quickly realize that it should be a  $g$ . You certainly won't just give up on the problem and deem it unsolvable because no one gave you the value of  $q$ !
- YOU CAN DO THE PROBLEM ONCE AND FOR ALL. If someone comes along and says, oops, the value of  $\ell$  is actually 2.4 m instead of 2.3 m, then you won't have to do the whole problem again. You can simply plug the new value of  $\ell$  into your final symbolic answer.
- YOU CAN SEE THE GENERAL DEPENDENCE OF YOUR ANSWER ON THE VARIOUS GIVEN QUANTITIES. For example, you can see that it grows with quantities  $a$  and  $b$ , decreases with  $c$ , and doesn't depend on  $d$ . There is much, much more information contained in a symbolic answer than in a numerical one. And besides, symbolic answers nearly always look nice and pretty.
- YOU CAN CHECK UNITS AND SPECIAL CASES. These checks go hand-in-hand with the previous "general dependence" advantage. But since they're so important, we'll postpone their discussion and devote Sections 1.2 and 1.3 to them.

Having said all this, it should be noted that there are occasionally times when things get a bit messy when working with letters. For example, solving a system of three equations in three unknowns might be rather cumbersome unless you plug in the actual numbers. But in the vast majority of problems, it is highly advantageous to work entirely with letters.

#### 4. Consider units/dimensions.

This is extremely important. See Section 1.2 for a detailed discussion.

#### 5. Check limiting/special cases.

This is also extremely important. See Section 1.3 for a detailed discussion.

#### 6. Check order of magnitude if you end up getting a numerical answer.

If you end up with an actual numerical answer to a problem, be sure to do a sanity check to see if the number is reasonable. If you've calculated the distance along the ground that a car skids before it comes to rest, and if you've gotten an answer of a kilometer or a millimeter, then you know you've probably done something wrong. Errors of this sort often come from forgetting some powers of 10 (say, when converting kilometers to meters) or from multiplying something instead of dividing (although you should be able to catch this by checking your units, too).

You will inevitably encounter problems, physics ones or otherwise, where you don't end up obtaining a rigorous answer, either because the calculation is intractable, or because you just don't feel like doing it. But in these cases it's usually still possible to make an educated guess, to the nearest power of 10. For example, if you walk past a building and happen to wonder how many bricks are in it, or what the labor cost was in constructing it, then you can probably give a reasonable answer without doing any severe computations. The physicist Enrico Fermi was known for his ability to estimate things quickly and produce order-of-magnitude guesses with only minimal calculation. Hence, a problem where the goal is to simply obtain the nearest power-of-10 estimate is known as a "Fermi problem." Of course, sometimes in life you need to know things to better accuracy than the nearest power of 10 . . .

> How Fermi could estimate things!  
> Like the well-known Olympic ten rings,  
> And the one hundred states,  
> And weeks with ten dates,  
> And birds that all fly with one . . . wings.

In the following two sections, we'll discuss the very important strategies of checking units and special cases. Then in Section 1.4 we'll discuss the technique of solving problems numerically, which is what you need to do when you end up with a set of equations you can't figure out how to solve. Section 1.4 isn't quite analogous to Sections 1.2 and 1.3, in that these first two are relevant to basically any problem you'll ever do, whereas solving equations numerically is something you'll do only for occasional problems. But it's nevertheless something that every physics student should know.

In all three of these sections, we'll invoke various results derived later in the book. For the present purposes, the derivations of these results are completely irrelevant, so don't worry at all about the physics behind them – there will be

plenty of opportunity for that later on! The main point here is to learn what to do with the result of a problem once you've obtained it.

## 1.2 Units, dimensional analysis

The units, or dimensions, of a quantity are the powers of mass, length, and time associated with it. For example, the units of a speed are length per time. The consideration of units offers two main benefits. First, looking at units before you start a problem can tell you roughly what the answer has to look like, up to numerical factors. Second, checking units at the end of a calculation (which is something you should *always* do) can tell you if your answer has a chance at being correct. It won't tell you that your answer is definitely correct, but it might tell you that your answer is definitely incorrect. For example, if your goal in a problem is to find a length, and if you end up with a mass, then you know it's time to look back over your work.

"Your units are wrong!" cried the teacher.  
 "Your church weighs six joules – what a feature!  
 And the people inside  
 Are four hours wide,  
 And eight gauss away from the preacher!"

In practice, the second of the above two benefits is what you will generally make use of. But let's do a few examples relating to the first benefit, because these can be a little more exciting. To solve the three examples below exactly, we would need to invoke results derived in later chapters. But let's just see how far we can get by using only dimensional analysis. We'll use the "[ ]" notation for units, and we'll let  $M$  stand for mass,  $L$  for length, and  $T$  for time. For example, we'll write a speed as  $[v] = L/T$  and the gravitational constant as  $[G] = L^3/(MT^2)$  (you can figure this out by noting that  $Gm_1m_2/r^2$  has the dimensions of force, which in turn has dimensions  $ML/T^2$ , from  $F = ma$ ). Alternatively, you can just use the mks units, kg, m, s, instead of  $M, L, T$ , respectively.<sup>1</sup>

![Diagram of a simple pendulum. A mass m is suspended by a massless string of length l from a fixed horizontal support. The string makes an angle theta with the vertical dashed line. A downward arrow labeled g indicates the direction of gravity.](5756508641ee599941f6d1e85de7e84b_img.jpg)

Diagram of a simple pendulum. A mass m is suspended by a massless string of length l from a fixed horizontal support. The string makes an angle theta with the vertical dashed line. A downward arrow labeled g indicates the direction of gravity.

Fig. 1.1

**Example (Pendulum):** A mass  $m$  hangs from a massless string of length  $\ell$  (see Fig. 1.1) and swings back and forth in the plane of the paper. The acceleration due to gravity is  $g$ . What can we say about the frequency of oscillations?

**Solution:** The only dimensionful quantities given in the problem are  $[m] = M$ ,  $[\ell] = L$ , and  $[g] = L/T^2$ . But there is one more quantity, the maximum angle  $\theta_0$ , which is dimensionless (and easy to forget). Our goal is to find the frequency, which

<sup>1</sup> When you check units at the end of a calculation, you will invariably be working with the kg,m,s notation. So that notation will inevitably get used more. But I'll use the  $M, L, T$  notation here, because I think it's a little more instructive. At any rate, just remember that the letter m (or  $M$ ) stands for "meter" in one case, and "mass" in the other.

has units of  $1/T$ . The only combination of our given dimensionful quantities that has units of  $1/T$  is  $\sqrt{g/\ell}$ . But we can't rule out any  $\theta_0$  dependence, so the most general possible form of the frequency is<sup>2</sup>

$$\omega = f(\theta_0) \sqrt{\frac{g}{\ell}}, \quad (1.1)$$

where  $f$  is a dimensionless function of the dimensionless variable  $\theta_0$ .

REMARKS:

1. It just so happens that for small oscillations,  $f(\theta_0)$  is essentially equal to 1, so the frequency is essentially equal to  $\sqrt{g/\ell}$ . But there is no way to show this by using only dimensional analysis; you actually have to solve the problem for real. For larger values of  $\theta_0$ , the higher-order terms in the expansion of  $f$  become important. Exercise 4.23 deals with the leading correction, and the answer turns out to be  $f(\theta_0) = 1 - \theta_0^2/16 + \dots$ .
2. Since there is only one mass in the problem, there is no way that the frequency (with units of  $1/T$ ) can depend on  $[m] = M$ . If it did, there would be nothing to cancel the units of mass and produce a pure inverse-time.
3. We claimed above that the only combination of our given dimensionful quantities that has units of  $1/T$  is  $\sqrt{g/\ell}$ . This is easy to see here, but in more complicated problems where the correct combination isn't so obvious, the following method will always work. Write down a general product of the given dimensionful quantities raised to arbitrary powers ( $m^a \ell^b g^c$  in this problem), and then write out the units of this product in terms of  $a$ ,  $b$ , and  $c$ . If we want to obtain units of  $1/T$  here, then we need

$$M^a L^b \left( \frac{L}{T^2} \right)^c = \frac{1}{T}. \quad (1.2)$$

Matching up the powers of the three kinds of units on each side of this equation gives

$$M : a = 0, \quad L : b + c = 0, \quad T : -2c = -1. \quad (1.3)$$

The solution to this system of equations is  $a = 0$ ,  $b = -1/2$ , and  $c = 1/2$ , so we have reproduced the  $\sqrt{g/\ell}$  result. ♣

What can we say about the total energy of the pendulum (with the potential energy measured relative to the lowest point)? We'll talk about energy in Chapter 5, but the only thing we need to know here is that energy has units of  $ML^2/T^2$ . The only combination of the given dimensionful constants of this form is  $mg\ell$ . But again, we can't rule out any  $\theta_0$  dependence, so the energy must take the form  $f(\theta_0)mg\ell$ , where  $f$  is some function. That's as far as we can go with dimensional analysis. However, if we actually invoke a little physics, we can say that the total energy equals the potential energy at the highest point, which is  $mg\ell(1 - \cos\theta_0)$ . Using the Taylor expansion for  $\cos\theta$  (see Appendix A for a discussion of Taylor series), we see that  $f(\theta_0) = \theta_0^2/2 - \theta_0^4/24 + \dots$ . So in contrast with the frequency result above, the maximum angle  $\theta_0$  plays a critical role in the energy.

<sup>2</sup> We'll measure frequency here in radians per second, denoted by  $\omega$ . So we're actually talking about the "angular frequency." Just divide by  $2\pi$  (which doesn't affect the units) to obtain the "regular" frequency in cycles per second (hertz), usually denoted by  $\nu$ . We'll talk at great length about oscillations in Chapter 4.

![Diagram of a mass-spring system. A spring with spring constant k is attached to a vertical wall on the left and a mass m on the right. The mass is resting on a horizontal surface.](05c9994c1f5daf53d0d9b107657d7a17_img.jpg)

Diagram of a mass-spring system. A spring with spring constant k is attached to a vertical wall on the left and a mass m on the right. The mass is resting on a horizontal surface.

Fig. 1.2

**Example (Spring):** A spring with spring constant  $k$  has a mass  $m$  on its end (see Fig. 1.2). The spring force is  $F(x) = -kx$ , where  $x$  is the displacement from the equilibrium position. What can we say about the frequency of oscillations?

**Solution:** The only dimensionful quantities in this problem are  $[m] = M$ ,  $[k] = M/T^2$  (obtained by noting that  $kx$  has the dimensions of force), and the maximum displacement from the equilibrium,  $[x_0] = L$ . (There is also the equilibrium length, but the force doesn't depend on this, so there is no way it can come into the answer.) Our goal is to find the frequency, which has units of  $1/T$ . The only combination of our given dimensionful quantities with these units is

$$\omega = C\sqrt{\frac{k}{m}}, \quad (1.4)$$

where  $C$  is a dimensionless number. It just so happens that  $C$  is equal to 1 (assuming that we're measuring  $\omega$  in radians per second), but there is no way to show this by using only dimensional analysis. Note that, in contrast with the pendulum above, the frequency cannot have any dependence on the maximum displacement.

What can we say about the total energy of the spring? Energy has units of  $ML^2/T^2$ , and the only combination of the given dimensionful constants of this form is  $Bkx_0^2$ , where  $B$  is a dimensionless number. It turns out that  $B = 1/2$ , so the total energy equals  $kx_0^2/2$ .

**REMARK:** A real spring doesn't have a perfectly parabolic potential (that is, a perfectly linear force), so the force actually looks something like  $F(x) = -kx + bx^2 + \dots$ . If we truncate the series at the second term, then we have one more dimensionful quantity to work with,  $[b] = M/LT^2$ . To form a quantity with the dimensions of frequency,  $1/T$ , we need  $x_0$  and  $b$  to appear in the combination  $x_0b$ , because this is the only way to get rid of the  $L$ . You can then see (by using the strategy of writing out a general product of the variables, discussed in the third remark in the pendulum example above) that the frequency must be of the form  $f(x_0b/k)\sqrt{k/m}$ , where  $f$  is some function. We can therefore have  $x_0$  dependence in this case. This answer must reduce to  $C\sqrt{k/m}$  for  $b = 0$ . Hence,  $f$  must be of the form  $f(y) = C + c_1y + c_2y^2 + \dots$  ♣

**Example (Low-orbit satellite):** A satellite of mass  $m$  travels in a circular orbit just above the earth's surface. What can we say about its speed?

**Solution:** The only dimensionful quantities in the problem are  $[m] = M$ ,  $[g] = L/T^2$ , and the radius of the earth  $[R] = L$ .<sup>3</sup> Our goal is to find the speed, which has units of  $L/T$ . The only combination of our dimensionful quantities with these units is

$$v = C\sqrt{gR}. \quad (1.5)$$

It turns out that  $C = 1$ .

<sup>3</sup> You might argue that the mass of the earth,  $M_E$ , and Newton's gravitational constant,  $G$ , should be also included here, because Newton's gravitational force law for a particle on the surface of the earth is  $F = GM_E m/R^2$ . But since this force can be written as  $m(GM_E/R^2) \equiv mg$ , we can absorb the effects of  $M_E$  and  $G$  into  $g$ .

## 1.3 Approximations, limiting cases

As with units, the consideration of limiting cases (or perhaps we should say special cases) offers two main benefits. First, it can help you get started on a problem. If you're having trouble figuring out how a given system behaves, then you can imagine making, for example, a certain length become very large or very small, and then you can see what happens to the behavior. Having convinced yourself that the length actually affects the system in extreme cases (or perhaps you will discover that the length doesn't affect things at all), it will then be easier to understand how it affects the system in general, which will then make it easier to write down the relevant quantitative equations (conservation laws,  $F = ma$  equations, etc.), which will allow you to fully solve the problem. In short, modifying the various parameters and observing the effects on the system can lead to an enormous amount of information.

Second, as with checking units, checking limiting cases (or special cases) is something you should *always* do at the end of a calculation. But as with checking units, it won't tell you that your answer is definitely correct, but it might tell you that your answer is definitely incorrect. It is generally true that your intuition about limiting cases is much better than your intuition about generic values of the parameters. You should use this fact to your advantage.

Let's do a few examples relating to the second benefit. The initial expressions given in each example below are taken from various examples throughout the book, so just accept them for now. For the most part, I'll repeat here what I'll say later on when we work through the problems for real. A tool that comes up often in checking limiting cases is the Taylor series approximations; the series for many functions are given in Appendix A.

---

**Example (Dropped ball):** A beach ball is dropped from rest at height  $h$ . Assume that the drag force from the air takes the form  $F_d = -m\alpha v$ . We'll find in Section 3.3 that the ball's velocity and position are given by

$$v(t) = -\frac{g}{\alpha} (1 - e^{-\alpha t}), \quad \text{and} \quad y(t) = h - \frac{g}{\alpha} \left( t - \frac{1}{\alpha} (1 - e^{-\alpha t}) \right). \quad (1.6)$$

These expressions are a bit complicated, so for all you know, I could have made a typo in writing them down. Or worse, I could have completely botched the solution. So let's look at some limiting cases. If these limiting cases yield expected results, then we can feel a little more confident that the answers are actually correct.

If  $t$  is very small (more precisely, if  $\alpha t \ll 1$ ; see the discussion following this example), then we can use the Taylor series,  $e^{-x} \approx 1 - x + x^2/2$ , to make approximations

to leading order in  $\alpha t$ . The  $v(t)$  in Eq. (1.6) becomes

$$\begin{aligned} v(t) &= -\frac{g}{\alpha} \left( 1 - \left( 1 - \alpha t + \frac{(\alpha t)^2}{2} - \dots \right) \right) \\ &\approx -gt, \end{aligned} \quad (1.7)$$

plus terms of higher order in  $\alpha t$ . This answer is expected, because the drag force is negligible at the start, so we essentially have a freely falling body with acceleration  $g$  downward. For small  $t$ , Eq. (1.6) also gives

$$\begin{aligned} y(t) &= h - \frac{g}{\alpha} \left[ t - \frac{1}{\alpha} \left( 1 - \left( 1 - \alpha t + \frac{(\alpha t)^2}{2} - \dots \right) \right) \right] \\ &\approx h - \frac{gt^2}{2}, \end{aligned} \quad (1.8)$$

plus terms of higher order in  $\alpha t$ . Again, this answer is expected, because we essentially have a freely falling body at the start, so the distance fallen is the standard  $gt^2/2$ .

We can also look at large  $t$  (or rather, large  $\alpha t$ ). In this case,  $e^{-\alpha t}$  is essentially zero, so the  $v(t)$  in Eq. (1.6) becomes (there's no need for a Taylor series in this case)

$$v(t) \approx -\frac{g}{\alpha}. \quad (1.9)$$

This is the “terminal velocity.” Its value makes sense, because it is the velocity for which the total force,  $-mg - m\alpha v$ , vanishes. For large  $t$ , Eq. (1.6) also gives

$$y(t) \approx h - \frac{gt}{\alpha} + \frac{g}{\alpha^2}. \quad (1.10)$$

Apparently for large  $t$ ,  $g/\alpha^2$  is the distance (and this does indeed have units of length, because  $\alpha$  has units of  $T^{-1}$ , because  $m\alpha v$  has units of force) that our ball lags behind another ball that started out already at the terminal velocity,  $-g/\alpha$ .

---

Whenever you derive approximate answers as we just did, you gain something and you lose something. You lose some truth, of course, because your new answer is technically not correct. But you gain some aesthetics. Your new answer is invariably much cleaner (sometimes involving only one term), and this makes it a lot easier to see what's going on.

In the above example, it actually makes no sense to look at the limit where  $t$  is small or large, because  $t$  has dimensions. Is a year a large or small time? How about a hundredth of a second? There is no way to answer this without knowing what problem you're dealing with. A year is short on the time scale of galactic evolution, but a hundredth of a second is long on the time scale of a nuclear process. It makes sense only to look at the limit of a small (or large) *dimensionless* quantity. In the above example, this quantity is  $\alpha t$ . The given constant  $\alpha$  has units of  $T^{-1}$ , so  $1/\alpha$  sets a typical time scale for the system. It

therefore makes sense to look at the limit where  $t \ll 1/\alpha$  (that is,  $\alpha t \ll 1$ ), or where  $t \gg 1/\alpha$  (that is,  $\alpha t \gg 1$ ). In the limit of a small dimensionless quantity, a Taylor series can be used to expand an answer in powers of the small quantity, as we did above. We sometimes get sloppy and say things like, “In the limit of small  $t$ .” But you know that we really mean, “In the limit of some small dimensionless quantity that has a  $t$  in the numerator,” or, “In the limit where  $t$  is much smaller than a certain quantity that has the dimensions of time.”

**REMARK:** As mentioned above, checking special cases tells you that either (1) your answer is consistent with your intuition, or (2) it’s wrong. It never tells you that it’s definitely correct. This is the same as what happens with the scientific method. In the real world, everything comes down to experiment. If you have a theory that you think is correct, then you need to check that its predictions are consistent with experiments. The specific experiments you do are the analog of the special cases you check after solving a problem; these two things represent what you know is true. If the results of the experiments are inconsistent with your theory, then you need to go back and fix your theory, just as you would need to go back and fix your answer. If, on the other hand, the results are consistent, then although this is good, the only thing it really tells you is that your theory *might* be correct. And considering the way things usually turn out, the odds are that it’s not actually correct, but rather the limiting case of a more correct theory (just as Newtonian physics is a limiting case of relativistic physics, which is a limiting case of quantum field theory, etc.). That’s how physics works. You can’t prove anything, so you learn to settle for the things you can’t disprove.

Consider, when seeking gestalts,  
 The theories that physics exalts.  
 It’s not that they’re known  
 To be written in stone.  
 It’s just that we can’t say they’re false. ♣

When making approximations, how do you know how many terms in the Taylor series to keep? In the example above, we used  $e^{-x} \approx 1 - x + x^2/2$ . But why did we stop at the  $x^2$  term? The honest (but slightly facetious) answer is, “Because I had already done this problem before writing it up, so I knew how many terms to keep.” But the more informative (although perhaps no more helpful) answer is that before you do the calculation, there’s really no way of knowing how many terms to keep. So you should just keep a few and see what happens. If everything ends up canceling out, then this tells you that you need to repeat the calculation with another term in the series. For example, in Eq. (1.8), if we had stopped the Taylor series at  $e^{-x} \approx 1 - x$ , then we would have obtained  $y(t) = h - 0$ , which isn’t very useful, since the general goal is to get the leading-order behavior in the parameter we’re looking at (which is  $t$  here). So in this case we’d know we’d have to go back and include the  $x^2/2$  term in the series. If we were doing a problem in which there was still no  $t$  (or whatever variable) dependence at that order, then we’d have to go back and include the  $-x^3/6$  term in the series. Of course, you could just play it safe and keep terms up to, say, fifth order. But that’s invariably a poor strategy, because you’ll probably never in your life have to go out that far in a series. So just start with one or two terms and see what it gives you. Note that in Eq. (1.7), we actually didn’t need the

second-order term, so we in fact could have gotten by with only  $e^{-x} \approx 1 - x$ . But having the extra term here didn't end up causing much heartache.

After you make an approximation, how do you know if it's a "good" one? Well, just as it makes no sense to ask if a dimensionful quantity is large or small without comparing it to another quantity, it makes no sense to ask if an approximation is "good" or "bad" without stating the accuracy you want. In the above example, if you're looking at a  $t$  value for which  $\alpha t \approx 1/100$ , then the term we ignored in Eq. (1.7) is smaller than  $gt$  by a factor  $\alpha t/2 \approx 1/200$ . So the error is on the order of 1%. If this is enough accuracy for whatever purpose you have in mind, then the approximation is a good one. If not, it's a bad one, and you should add more terms in the series until you get your desired accuracy.

The results of checking limits generally fall into two categories. Most of the time you know what the result should be, so this provides a double-check on your answer. But sometimes an interesting limit pops up that you might not expect. Such is the case in the following examples.

![Diagram for Fig. 1.3 showing two masses, m and M, on a horizontal line. Mass m is on the left with a velocity vector v pointing to the right. Mass M is on the right and is stationary.](50a9c7181c18688b552a026ea24bc095_img.jpg)

Diagram for Fig. 1.3 showing two masses, m and M, on a horizontal line. Mass m is on the left with a velocity vector v pointing to the right. Mass M is on the right and is stationary.

Fig. 1.3

**Example (Two masses in 1-D):** A mass  $m$  with speed  $v$  approaches a stationary mass  $M$  (see Fig. 1.3). The masses bounce off each other elastically. Assume that all motion takes place in one dimension. We'll find in Section 5.6.1 that the final velocities of the particles are

$$v_m = \frac{(m - M)v}{m + M}, \quad \text{and} \quad v_M = \frac{2mv}{m + M}. \quad (1.11)$$

There are three special cases that beg to be checked:

- If  $m = M$ , then Eq. (1.11) tells us that  $m$  stops, and  $M$  picks up a speed  $v$ . This is fairly believable (and even more so for pool players). And it becomes quite clear once you realize that these final speeds certainly satisfy conservation of energy and momentum with the initial conditions.
- If  $M \gg m$ , then  $m$  bounces backward with speed  $\approx v$ , and  $M$  hardly moves. This makes sense, because  $M$  is basically a brick wall.
- If  $m \gg M$ , then  $m$  keeps plowing along at speed  $\approx v$ , and  $M$  picks up a speed of  $\approx 2v$ . This  $2v$  is an unexpected and interesting result (it's easier to see if you consider what's happening in the reference frame of the heavy mass  $m$ ), and it leads to some neat effects, as in Problem 5.23.

![Diagram for Fig. 1.4 showing a circular pendulum. A mass m is suspended by a string of length l from a fixed point. The string makes a constant angle theta with the vertical. The mass swings in a horizontal circle, indicated by a dashed ellipse and a curved arrow. Gravity g is shown acting downwards.](0b12afcd375d5f967112ceb045230b96_img.jpg)

Diagram for Fig. 1.4 showing a circular pendulum. A mass m is suspended by a string of length l from a fixed point. The string makes a constant angle theta with the vertical. The mass swings in a horizontal circle, indicated by a dashed ellipse and a curved arrow. Gravity g is shown acting downwards.

Fig. 1.4

**Example (Circular pendulum):** A mass hangs from a massless string of length  $\ell$ . Conditions have been set up so that the mass swings around in a horizontal circle, with the string making a constant angle  $\theta$  with the vertical (see Fig. 1.4). We'll find in Section 3.5 that the angular frequency,  $\omega$ , of this motion is

$$\omega = \sqrt{\frac{g}{\ell \cos \theta}}. \quad (1.12)$$

As far as  $\theta$  is concerned, there are two limits we should definitely check:

- If  $\theta \rightarrow 90^\circ$ , then  $\omega \rightarrow \infty$ . This makes sense; the mass has to spin very quickly to avoid flopping down.
- If  $\theta \rightarrow 0$ , then  $\omega \rightarrow \sqrt{g/\ell}$ , which is the same as the frequency of a standard “plane” pendulum of length  $\ell$  (for small oscillations). This is a cool result and not at all obvious. (But once we get to  $F = ma$  in Chapter 3, you can convince yourself why this is true by looking at the projection of the force on a given horizontal line.)

---

In the above examples, we checked limiting and special cases of answers that were correct (I hope!). This whole process is more useful (and a bit more fun, actually) when you check the limits of an answer that is *incorrect*. In this case, you gain the unequivocal information that your answer is wrong. But rather than leading you into despair, this information is in fact something you should be quite happy about, considering that the alternative is to carry on in a state of blissful ignorance. Once you know that your answer is wrong, you can go back through your work and figure out where the error is (perhaps by checking limits at various stages to narrow down where the error could be). Personally, if there’s any way I’d like to discover that my answer is garbage, this is it. At any rate, checking limiting cases can often save you a lot of trouble in the long run...

The lemmings get set for their race.  
 With one step and two steps they pace.  
 They take three and four,  
 And then head on for more,  
 Without checking the limiting case.

## 1.4 Solving differential equations numerically

Solving a physics problem often involves solving a differential equation. A differential equation is one that involves derivatives (usually with respect to time, in our physics problems) of the variable you’re trying to solve for. The differential equation invariably comes about from using  $F = ma$ , and/or  $\tau = I\alpha$ , or the Lagrangian technique we’ll discuss in Chapter 6. For example, consider a falling body.  $F = ma$  gives  $-mg = ma$ , which can be written as  $-g = \ddot{y}$ , where a dot denotes a time derivative. This is a rather simple differential equation, and you can quickly guess that  $y(t) = -gt^2/2$  is a solution. Or, more generally with the constants of integration thrown in,  $y(t) = y_0 + v_0t - gt^2/2$ .

However, the differential equations produced in some problems can get rather complicated, so sooner or later you will encounter one that you can’t solve exactly (either because it’s in fact impossible to solve, or because you can’t think of the

appropriate clever trick). Having resigned yourself to not getting the exact answer, you should ponder how to obtain a decent approximation to it. Fortunately, it's easy to write a short program that will give you a very good numerical answer to your problem. Given enough computer time, you can obtain any desired accuracy (assuming that the system isn't chaotic, but we won't have to worry about this for the systems we'll be dealing with).

We'll demonstrate the procedure by considering a standard problem, one that we'll solve exactly and in great depth in Chapter 4. Consider the equation,

$$\ddot{x} = -\omega^2 x. \quad (1.13)$$

This is the equation for a mass on a spring, with  $\omega = \sqrt{k/m}$ . We'll find in Chapter 4 that the solution can be written, among other ways, as

$$x(t) = A \cos(\omega t + \phi). \quad (1.14)$$

But let's pretend we don't know this. If someone comes along and gives us the values of  $x(0)$  and  $\dot{x}(0)$ , then it seems that somehow we should be able to find  $x(t)$  and  $\dot{x}(t)$  for any later  $t$ , just by using Eq. (1.13). Basically, if we're told how the system starts, and if we know how it evolves, via Eq. (1.13), then we should know everything about it. So here's how we find  $x(t)$  and  $\dot{x}(t)$ .

The plan is to discretize time into intervals of some small unit (call it  $\epsilon$ ), and to then determine what happens at each successive point in time. If we know  $x(t)$  and  $\dot{x}(t)$ , then we can easily find (approximately) the value of  $x$  at a slightly later time, by using the definition of  $\dot{x}$ . Similarly, if we know  $\dot{x}(t)$  and  $\ddot{x}(t)$ , then we can easily find (approximately) the value of  $\dot{x}$  at a slightly later time, by using the definition of  $\ddot{x}$ . Using the definitions of the derivatives, the relations are simply

$$\begin{aligned} x(t + \epsilon) &\approx x(t) + \epsilon \dot{x}(t), \\ \dot{x}(t + \epsilon) &\approx \dot{x}(t) + \epsilon \ddot{x}(t). \end{aligned} \quad (1.15)$$

These two equations, combined with (1.13), which gives us  $\ddot{x}$  in terms of  $x$ , allow us to march along in time, obtaining successive values for  $x$ ,  $\dot{x}$ , and  $\ddot{x}$ .<sup>4</sup>

Here's what a typical program might look like.<sup>5</sup> (This is a Maple program, but even if you aren't familiar with this, the general idea should be clear.) Let's say

<sup>4</sup> Of course, another expression for  $\ddot{x}$  is the definitional one, analogous to Eqs. (1.15), involving the third derivative. But this would then require knowledge of the third derivative, and so on with higher derivatives, and we would end up with an infinite chain of relations. An *equation of motion* such as Eq. (1.13) (which in general could be an  $F = ma$ ,  $\tau = I\alpha$ , or Euler–Lagrange equation) relates  $\ddot{x}$  back to  $x$  (and possibly  $\dot{x}$ ), thereby creating an intertwined relation among  $x$ ,  $\dot{x}$ , and  $\ddot{x}$ , and eliminating the need for an infinite and useless chain.

<sup>5</sup> We've written the program in the most straightforward way, without any concern for efficiency, because computing time isn't an issue in this simple system. But in more complex systems that require programs for which computing time is an issue, a major part of the problem-solving process is developing a program that is as efficient as possible.

that the particle starts from rest at position  $x = 2$ , and let's pick  $\omega^2 = 5$ . We'll use the notation where  $x1$  stands for  $\dot{x}$ , and  $x2$  stands for  $\ddot{x}$ . And  $\epsilon$  stands for  $\epsilon$ . Let's calculate  $x$  at, say,  $t = 3$ .

```
x:=2:           # initial position
x1:=0:          # initial velocity
e:=.01:         # small time interval
for i to 300 do  # do 300 steps (ie, up to 3 seconds)
x2:=-5*x:       # the given equation
x:=x+e*x1:      # how x changes, by definition of x1
x1:=x1+e*x2:    # how x1 changes, by definition of x2
end do:         # the Maple command to stop the do loop
x;              # print the value of x
```

This procedure won't give the exact value for  $x$ , because  $x$  and  $\dot{x}$  don't really change according to Eqs. (1.15). These equations are just first-order approximations to the full Taylor series with higher-order terms. Said differently, there is no way the above procedure can be exactly correct, because there are ambiguities in how the program can be written. Should line 5 come before or after line 7? That is, in determining  $\dot{x}$  at time  $t + \epsilon$ , should we use the  $\ddot{x}$  at time  $t$  or  $t + \epsilon$ ? And should line 7 come before or after line 6? The point is that for very small  $\epsilon$ , the order doesn't matter much. And in the limit  $\epsilon \rightarrow 0$ , the order doesn't matter at all.

If we want to obtain a better approximation, we can just shorten  $\epsilon$  down to 0.001 and increase the number of steps to 3000. If the result looks basically the same as with  $\epsilon = 0.01$ , then we know we pretty much have the right answer. In the present example,  $\epsilon = 0.01$  yields  $x \approx 1.965$  after 3 seconds. If we set  $\epsilon = 0.001$ , then we obtain  $x \approx 1.836$ . And if we set  $\epsilon = 0.0001$ , then we get  $x \approx 1.823$ . The correct answer must therefore be somewhere around  $x = 1.82$ . And indeed, if we solve the problem exactly, we obtain  $x(t) = 2 \cos(\sqrt{5} t)$ . Plugging in  $t = 3$  gives  $x \approx 1.822$ .

This is a wonderful procedure, but it shouldn't be abused. It's nice to know that we can always obtain a decent numerical approximation if all else fails. But we should set our initial goal on obtaining the correct algebraic expression, because this allows us to see the overall behavior of the system. And besides, nothing beats the truth. People tend to rely a bit too much on computers and calculators nowadays, without pausing to think about what is actually going on in a problem.

The skill to do math on a page  
 Has declined to the point of outrage.  
 Equations quadratica  
 Are solved on Math'matica,  
 And on birthdays we don't know our age.

## 1.5 Problems

## Section 1.2: Units, dimensional analysis

### 1.1. Escape velocity \*

As given below in Exercise 1.9, show that the escape velocity from the earth is  $v = \sqrt{2GM_E/R}$ , up to numerical factors. You can use the fact that the form of Newton's gravitation force law implies that the acceleration (and hence overall motion) of the particle doesn't depend on its mass.

### 1.2. Mass in a tube \*

![Diagram of a tube of mass M and length l pivoted at one end. A mass m is at the pivot. The tube is initially horizontal and then swings down to a vertical position.](aa7a4ea43951479b7e7b4c530ea5bc2d_img.jpg)

The diagram shows a horizontal tube of length  $l$  and mass  $M$  pivoted at its left end. A small mass  $m$  is located at the pivot point. An arrow indicates the tube swinging downwards from its horizontal position.

Diagram of a tube of mass M and length l pivoted at one end. A mass m is at the pivot. The tube is initially horizontal and then swings down to a vertical position.

Fig. 1.5

A tube of mass  $M$  and length  $l$  is free to swing around a pivot at one end. A mass  $m$  is positioned inside the (frictionless) tube at this end. The tube is held horizontal and then released (see Fig. 1.5). Let  $\eta$  be the fraction of the tube that the mass has traversed by the time the tube becomes vertical. Does  $\eta$  depend on  $l$ ?

### 1.3. Waves in a fluid \*

How does the speed of waves in a fluid depend on its density,  $\rho$ , and “bulk modulus,”  $B$  (which has units of pressure, which is force per area)?

### 1.4. Vibrating star \*

Consider a vibrating star, whose frequency  $\nu$  depends (at most) on its radius  $R$ , mass density  $\rho$ , and Newton's gravitational constant  $G$ . How does  $\nu$  depend on  $R$ ,  $\rho$ , and  $G$ ?

### 1.5. Damping \*\*

A particle with mass  $m$  and initial speed  $V$  is subject to a velocity-dependent damping force of the form  $bv^n$ .

- For  $n = 0, 1, 2, \dots$ , determine how the stopping time depends on  $m$ ,  $V$ , and  $b$ .
- For  $n = 0, 1, 2, \dots$ , determine how the stopping distance depends on  $m$ ,  $V$ , and  $b$ .

Be careful! See if your answers make sense. Dimensional analysis gives the answer only up to a numerical factor. This is a tricky problem, so don't let it discourage you from using dimensional analysis. Most applications of dimensional analysis are quite straightforward.

## Section 1.3: Approximations, limiting cases

### 1.6. Projectile distance \*

A person throws a ball (at an angle of her choosing, to achieve the maximum distance) with speed  $v$  from the edge of a cliff of height  $h$ . Assuming

that one of the following quantities is the maximum horizontal distance the ball can travel, which one is it? (Don't solve the problem from scratch, just check special cases.)

$$\frac{gh^2}{v^2}, \quad \frac{v^2}{g}, \quad \sqrt{\frac{v^2 h}{g}}, \quad \frac{v^2}{g} \sqrt{1 + \frac{2gh}{v^2}}, \quad \frac{v^2}{g} \left(1 + \frac{2gh}{v^2}\right), \quad \frac{v^2/g}{1 - \frac{2gh}{v^2}}.$$

## Section 1.4: Solving differential equations numerically

### 1.7. Two masses, one swinging \*\*

Two equal masses are connected by a string that hangs over two pulleys (of negligible size), as shown in Fig. 1.6. The left mass moves in a vertical line, but the right mass is free to swing back and forth in the plane of the masses and pulleys. It can be shown (see Problem 6.4) that the equations of motion for  $r$  and  $\theta$  (labeled in the figure) are

$$\begin{aligned} 2\ddot{r} &= r\dot{\theta}^2 - g(1 - \cos\theta), \\ \ddot{\theta} &= -\frac{2\dot{r}\dot{\theta}}{r} - \frac{g \sin\theta}{r}. \end{aligned} \quad (1.16)$$

Assume that both masses start out at rest, with the right mass making an initial angle of  $10^\circ = \pi/18$  with the vertical. If the initial value of  $r$  is 1 m, how much time does it take for it to reach a length of 2 m? Write a program to solve this numerically. Use  $g = 9.8 \text{ m/s}^2$ .

![Diagram of a mechanical system with two masses and two pulleys. A string passes over two pulleys fixed to a ceiling. The left side of the string hangs vertically with a mass 'm' at the end. The right side of the string hangs from the second pulley and is at an angle 'theta' from the vertical. The length of this right segment is 'r', and it also has a mass 'm' at its end. A dashed vertical line indicates the vertical direction for measuring the angle 'theta'.](e5410c8a59de981df993d51b9bddc9b3_img.jpg)

Diagram of a mechanical system with two masses and two pulleys. A string passes over two pulleys fixed to a ceiling. The left side of the string hangs vertically with a mass 'm' at the end. The right side of the string hangs from the second pulley and is at an angle 'theta' from the vertical. The length of this right segment is 'r', and it also has a mass 'm' at its end. A dashed vertical line indicates the vertical direction for measuring the angle 'theta'.

Fig. 1.6

## 1.6 Exercises

## Section 1.2: Units, dimensional analysis

### 1.8. Pendulum on the moon

If a pendulum has a period of 3 s on the earth, what would its period be if it were placed on the moon? Use  $g_M/g_E \approx 1/6$ .

### 1.9. Escape velocity \*

The *escape velocity* on the surface of a planet is given by

$$v = \sqrt{\frac{2GM}{R}}, \quad (1.17)$$

where  $M$  and  $R$  are the mass and radius of the planet, respectively, and  $G$  is Newton's gravitational constant. (The escape velocity is the velocity

needed to refute the “What goes up must come down” maxim, neglecting air resistance.)

- Write  $v$  in terms of the average mass density  $\rho$ , instead of  $M$ .
- Assuming that the average density of the earth is four times that of Jupiter, and that the radius of Jupiter is 11 times that of the earth, what is  $v_J/v_E$ ?

### 1.10. Downhill projectile \*

A hill is sloped downward at an angle  $\theta$  with respect to the horizontal. A projectile of mass  $m$  is fired with speed  $v_0$  perpendicular to the hill. When it eventually lands on the hill, let its velocity make an angle  $\beta$  with respect to the horizontal. Which of the quantities  $\theta$ ,  $m$ ,  $v_0$ , and  $g$  does the angle  $\beta$  depend on?

### 1.11. Waves on a string \*

How does the speed of waves on a string depend on its mass  $M$ , length  $L$ , and tension (that is, force)  $T$ ?

### 1.12. Vibrating water drop \*

Consider a vibrating water drop, whose frequency  $\nu$  depends on its radius  $R$ , mass density  $\rho$ , and surface tension  $S$ . The units of surface tension are (force)/(length). How does  $\nu$  depend on  $R$ ,  $\rho$ , and  $S$ ?

![Diagram of an Atwood's machine with three masses and three pulleys. A central pulley is suspended from a ceiling by a string. A string is looped over this central pulley, with mass m2 hanging from its bottom. Two other strings are looped over the central pulley and extend upwards to two separate fixed pulleys on the ceiling. From the left fixed pulley, a string hangs down with mass m1. From the right fixed pulley, a string hangs down with mass m3.](f732d3320afe06d979aabbd366184254_img.jpg)

Diagram of an Atwood's machine with three masses and three pulleys. A central pulley is suspended from a ceiling by a string. A string is looped over this central pulley, with mass m2 hanging from its bottom. Two other strings are looped over the central pulley and extend upwards to two separate fixed pulleys on the ceiling. From the left fixed pulley, a string hangs down with mass m1. From the right fixed pulley, a string hangs down with mass m3.

Fig. 1.7

## Section 1.3: Approximations, limiting cases

### 1.13. Atwood's machine \*

Consider the “Atwood’s” machine shown in Fig. 1.7, consisting of three masses and three frictionless pulleys. It can be shown that the acceleration of  $m_1$  is given by (just accept this):

$$a_1 = g \frac{3m_2m_3 - m_1(4m_3 + m_2)}{m_2m_3 + m_1(4m_3 + m_2)}, \quad (1.18)$$

with upward taken to be positive. Find  $a_1$  in the following special cases:

- $m_2 = 2m_1 = 2m_3$ .
- $m_1$  much larger than both  $m_2$  and  $m_3$ .
- $m_1$  much smaller than both  $m_2$  and  $m_3$ .
- $m_2 \gg m_1 = m_3$ .
- $m_1 = m_2 = m_3$ .

### 1.14. Cone frustum \*

A cone frustum has base radius  $b$ , top radius  $a$ , and height  $h$ , as shown in Fig. 1.8. Assuming that one of the following quantities is the volume

of the frustum, which one is it? (Don't solve the problem from scratch, just check special cases.)

$$\frac{\pi h}{3}(a^2 + b^2), \quad \frac{\pi h}{2}(a^2 + b^2), \quad \frac{\pi h}{3}(a^2 + ab + b^2),$$

$$\frac{\pi h}{3} \cdot \frac{a^4 + b^4}{a^2 + b^2}, \quad \pi hab.$$

![Diagram of a frustum of a cone. The top circular base has radius a, the bottom circular base has radius b, and the vertical height is h.](fd0bd97f68ab12fb22f937db56c801a5_img.jpg)

Diagram of a frustum of a cone. The top circular base has radius a, the bottom circular base has radius b, and the vertical height is h.

Fig. 1.8

### 1.15. Landing at the corner \*

A ball is thrown at an angle  $\theta$  up to the top of a cliff of height  $L$ , from a point a distance  $L$  from the base, as shown in Fig. 1.9. Assuming that one of the following quantities is the initial speed required to make the ball hit right at the edge of the cliff, which one is it? (Don't solve the problem from scratch, just check special cases.)

$$\sqrt{\frac{gL}{2(\tan \theta - 1)}}, \quad \frac{1}{\cos \theta} \sqrt{\frac{gL}{2(\tan \theta - 1)}}, \quad \frac{1}{\cos \theta} \sqrt{\frac{gL}{2(\tan \theta + 1)}},$$

$$\sqrt{\frac{gL \tan \theta}{2(\tan \theta + 1)}}.$$

![Diagram of a projectile motion problem. A ball is thrown from the ground at an angle theta with initial speed v0. The trajectory is a dashed parabolic curve that ends at the top edge of a cliff of height L. The horizontal distance from the launch point to the base of the cliff is also L.](b52180f7a841ba1408d66e2bac469720_img.jpg)

Diagram of a projectile motion problem. A ball is thrown from the ground at an angle theta with initial speed v0. The trajectory is a dashed parabolic curve that ends at the top edge of a cliff of height L. The horizontal distance from the launch point to the base of the cliff is also L.

Fig. 1.9

### 1.16. Projectile with drag \*\*

Consider a projectile subject to a drag force  $\mathbf{F} = -m\alpha\mathbf{v}$ . If it is fired with speed  $v_0$  at an angle  $\theta$ , it can be shown that the height as a function of time is given by (just accept this here; it's one of the tasks of Exercise 3.53)

$$y(t) = \frac{1}{\alpha} \left( v_0 \sin \theta + \frac{g}{\alpha} \right) \left( 1 - e^{-\alpha t} \right) - \frac{gt}{\alpha}. \quad (1.19)$$

Show that this reduces to the usual projectile expression,  $y(t) = (v_0 \sin \theta)t - gt^2/2$ , in the limit of small  $\alpha$ . What exactly is meant by “small  $\alpha$ ”?

## Section 1.4: Solving differential equations numerically

### 1.17. Pendulum \*\*

A pendulum of length  $\ell$  is released from the horizontal position. It can be shown that the tangential  $F = ma$  equation is (where  $\theta$  is measured with respect to the vertical)

$$\ddot{\theta} = -\frac{g \sin \theta}{\ell}. \quad (1.20)$$

If  $\ell = 1$  m, and  $g = 9.8$  m/s<sup>2</sup>, write a program to show that the time it takes the pendulum to swing down through the vertical position is

$t \approx 0.592$  s. This happens to be about 1.18 times the  $(\pi/2)\sqrt{\ell/g} \approx 0.502$  s it would take the pendulum to swing down if it were released from very close to the vertical (this is 1/4 of the standard period of  $2\pi\sqrt{\ell/g}$  for a pendulum). It also happens to be about 1.31 times the  $\sqrt{2\ell/g} \approx 0.452$  s it would take a mass to simply freefall a height  $\ell$ .

### 1.18. Distance with damping \*\*

A mass is subject to a damping force proportional to its velocity, which means that the equation of motion takes the form  $\ddot{x} = -A\dot{x}$ , where  $A$  is some constant. If the initial speed is 2 m/s, and if  $A = 1 \text{ s}^{-1}$ , how far has the mass traveled at 1 s? 10 s? 100 s? You should find that the distance approaches a limiting value.

Now assume that the mass is subject to a damping force proportional to the square of its velocity, which means that the equation of motion now takes the form  $\ddot{x} = -A\dot{x}^2$ , where  $A$  is some constant. If the initial speed is 2 m/s, and if  $A = 1 \text{ m}^{-1}$ , how far has the mass traveled at 1 s? 10 s? 100 s? How about some larger powers of 10? You should find that the distance keeps growing, but slowly like the log of  $t$ . (The results for these two forms of the damping are consistent with the results of Problem 1.5.)

## 1.7 Solutions

### 1.1. Escape velocity

It is tempting to use the same reasoning as in the low-orbit satellite example in Section 1.2. This reasoning gives the same result,  $v = C\sqrt{gR} = C\sqrt{GM_E/R}$ , where  $C$  is some number (it turns out that  $C = \sqrt{2}$ ). Although this solution yields the correct answer, it isn't quite rigorous, in view of the footnote in the low-orbit satellite example. Because the particle isn't always at the same radius, the force changes, so it isn't obvious that we can absorb the  $M_E$  and  $G$  dependence into one quantity,  $g$ , as we did with the orbiting satellite. Let us therefore be more rigorous with the following reasoning.

The dimensionful quantities in the problem are  $[m] = M$ , the radius of the earth  $[R] = L$ , the mass of the earth  $[M_E] = M$ , and Newton's gravitational constant  $[G] = L^3/MT^2$ . These units for  $G$  follow from the gravitational force law,  $F = Gm_1m_2/r^2$ . If we use no information other than these given quantities, then there is no way to arrive at the speed of  $C\sqrt{GM_E/R}$ , because for all we know, there could be a factor of  $(m/M_E)^7$  in the answer. This number is dimensionless, so it wouldn't mess up the units.

If we want to make any progress in this problem, we have to use the fact that the gravitational force takes the form of  $GM_Em/r^2$ . This then implies (as was stated in the problem) that the acceleration is independent of  $m$ . And since the path of the particle is determined by its acceleration, we see that the answer can't depend on  $m$ . We are therefore left with the quantities  $G$ ,  $R$ , and  $M_E$ , and you can show that the only combination of these quantities that gives the units of speed is  $v = C\sqrt{GM_E/R}$ .

### 1.2. Mass in a tube

The dimensionful quantities are  $[g] = L/T^2$ ,  $[\ell] = L$ ,  $[m] = M$ , and  $[M] = M$ . We want to produce a dimensionless number  $\eta$ . Since  $g$  is the only constant involving time,  $\eta$  cannot depend on  $g$ . This then implies that  $\eta$  cannot depend on  $\ell$ , which is the only

length remaining. Therefore,  $\eta$  depends only on  $m$  and  $M$  (and furthermore only on the ratio  $m/M$ , since we want a dimensionless number). So the answer to the stated problem is, “No.”

It turns out that you have to solve the problem numerically if you actually want to find  $\eta$  (see Problem 8.5). Some results are: If  $m \ll M$ , then  $\eta \approx 0.349$ . If  $m = M$ , then  $\eta \approx 0.378$ . And if  $m = 2M$ , then  $\eta \approx 0.410$ .

### 1.3. Waves in a fluid

We want to make a speed,  $[v] = L/T$ , out of the quantities  $[\rho] = M/L^3$ , and  $[B] = [F/A] = (ML/T^2)/(L^2) = M/(LT^2)$ . We can play around with these quantities to find the combination that has the correct units, but let's do it the no-fail way. If  $v \propto \rho^a B^b$ , then we have

$$\frac{L}{T} = \left(\frac{M}{L^3}\right)^a \left(\frac{M}{LT^2}\right)^b. \quad (1.21)$$

Matching up the powers of the three kinds of units on each side of this equation gives

$$M : 0 = a + b, \quad L : 1 = -3a - b, \quad T : -1 = -2b. \quad (1.22)$$

The solution to this system of equations is  $a = -1/2$  and  $b = 1/2$ . Therefore, our answer is  $v \propto \sqrt{B/\rho}$ . Fortunately, there was a solution to this system of three equations in two unknowns.

### 1.4. Vibrating star

We want to make a frequency,  $[\nu] = 1/T$ , out of the quantities  $[R] = L$ ,  $[\rho] = M/L^3$ , and  $[G] = L^3/(MT^2)$ . These units for  $G$  follow from the gravitational force law,  $F = Gm_1m_2/r^2$ . As in the previous problem, we can play around with these quantities to find the combination that has the correct units, but let's do it the no-fail way. If  $\nu \propto R^a \rho^b G^c$ , then we have

$$\frac{1}{T} = L^a \left(\frac{M}{L^3}\right)^b \left(\frac{L^3}{MT^2}\right)^c. \quad (1.23)$$

Matching up the powers of the three kinds of units on each side of this equation gives

$$M : 0 = b - c, \quad L : 0 = a - 3b + 3c, \quad T : -1 = -2c. \quad (1.24)$$

The solution to this system of equations is  $a = 0$ , and  $b = c = 1/2$ . Therefore, our answer is  $\nu \propto \sqrt{\rho G}$ . So it turns out that there is no  $R$  dependence.

REMARK: Note the difference in the given quantities in this problem ( $R$ ,  $\rho$ , and  $G$ ) and the ones in Exercise 1.12 ( $R$ ,  $\rho$ , and  $S$ ). In this problem with the star, the mass is large enough so that we can ignore the surface tension,  $S$ . And in Exercise 1.12 with the drop, the mass is small enough so that we can ignore the gravitational force, and hence  $G$ . ♣

### 1.5. Damping

- (a) The constant  $b$  has units  $[b] = [\text{Force}][v^{-n}] = (ML/T^2)(T^n/L^n)$ . The other quantities are  $[m] = M$  and  $[V] = L/T$ . There is also  $n$ , which is dimensionless. You can show that the only combination of these quantities that has units of  $T$  is

$$t = f(n) \frac{m}{bV^{n-1}}, \quad (1.25)$$

where  $f(n)$  is a dimensionless function of  $n$ .

For  $n = 0$ , we have  $t = f(0) mV/b$ . This increases with  $m$  and  $V$ , and decreases with  $b$ , as it should.

For  $n = 1$ , we have  $t = f(1) m/b$ . So we seem to have  $t \sim m/b$ . This, however, cannot be correct, because  $t$  should definitely grow with  $V$ . A large initial speed  $V_1$  requires some nonzero time to slow down to a smaller speed  $V_2$ , after which time we simply have the same scenario with initial speed  $V_2$ . So where did we go wrong? After all, dimensional analysis tells us that the answer *does* have to look like  $t = f(1) m/b$ , where  $f(1)$  is a numerical factor. The resolution to this puzzle

is that  $f(1)$  is infinite. If we worked out the problem using  $F = ma$ , we would encounter an integral that diverges. So for any  $V$ , we would find an infinite  $t$ .<sup>6</sup>

Similarly, for  $n \geq 2$ , there is at least one power of  $V$  in the denominator of  $t$ . This certainly cannot be correct, because  $t$  should not decrease with  $V$ . So  $f(n)$  must likewise be infinite for all of these cases.

The moral of this exercise is that sometimes you have to be careful when using dimensional analysis. The numerical factor in front of your answer nearly always turns out to be of order 1, but in some strange cases it turns out to be 0 or  $\infty$ .

REMARK: For  $n \geq 1$ , the expression in Eq. (1.25) still has relevance. For example, for  $n = 2$ , the  $m/(Vb)$  expression is relevant if you want to know how long it takes to go from  $V$  to some final speed  $V_f$ . The answer involves  $m/(V_f b)$ , which diverges as  $V_f \rightarrow 0$ . ♣

- (b) You can show that the only combination of the quantities that has units of  $L$  is

$$\ell = g(n) \frac{m}{bV^{n-2}}, \quad (1.26)$$

where  $g(n)$  is a dimensionless function of  $n$ .

For  $n = 0$ , we have  $\ell = g(0) mV^2/b$ . This increases with  $V$ , as it should.

For  $n = 1$ , we have  $\ell = g(1) mV/b$ . This increases with  $V$ , as it should.

For  $n = 2$  we have  $\ell = g(2) m/b$ . So we *seem* to have  $\ell \sim m/b$ . But as in part (a), this cannot be correct, because  $\ell$  should definitely depend on  $V$ . A large initial speed  $V_1$  requires some nonzero distance to slow down to a smaller speed  $V_2$ , after which point we simply have the same scenario with initial speed  $V_2$ . So, from the reasoning in part (a), the total distance is infinite for  $n \geq 2$ , because the function  $g$  is infinite.

REMARK: Note that for integral  $n \neq 1$ ,  $t$  and  $\ell$  are either both finite or both infinite. For  $n = 1$ , however, the total time is infinite, whereas the total distance is finite. This situation actually holds for  $1 \leq n < 2$ , if we want to consider fractional  $n$ . ♣

### 1.6. Projectile distance

All of the possible answers have the correct units, so we'll have to figure things out by looking at special cases. Let's look at each choice in turn:

$\frac{gh^2}{v^2}$  : Incorrect, because the answer shouldn't be zero for  $h = 0$ . Also, it shouldn't grow with  $g$ . And even worse, it shouldn't be infinite for  $v \rightarrow 0$ .

$\frac{v^2}{g}$  : Incorrect, because the answer should depend on  $h$ .

$\sqrt{\frac{v^2 h}{g}}$  : Incorrect, because the answer shouldn't be zero for  $h = 0$ .

$\frac{v^2}{g} \sqrt{1 + \frac{2gh}{v^2}}$  : Can't rule this out, and it happens to be the correct answer.

$\frac{v^2}{g} \left(1 + \frac{2gh}{v^2}\right)$  : Incorrect, because the answer should be zero for  $v \rightarrow 0$ . But this expression goes to  $2h$  for  $v \rightarrow 0$ .

$\frac{v^2/g}{1 - \frac{2gh}{v^2}}$  : Incorrect, because the answer shouldn't be infinite for  $v^2 = 2gh$ .

<sup>6</sup> The total time  $t$  is actually undefined, because the particle never comes to rest. But  $t$  does grow with  $V$ , in the sense that if  $t$  is defined to be the time to slow down to some certain small speed, then  $t$  grows with  $V$ .

### 1.7. Two masses, one swinging

As in Section 1.4, we'll write a Maple program. We'll let  $q$  stand for  $\theta$ , and we'll use the notation where  $q1$  stands for  $\dot{\theta}$ , and  $q2$  stands for  $\ddot{\theta}$ . Likewise for  $r$ . We'll run the program for as long as  $r < 2$ . As soon as  $r$  exceeds 2, the program will stop and print the value of the time.

```

r:=1:                # initial r value
r1:=0:               # initial r velocity
q:=3.14/18:          # initial angle
q1:=0:               # initial angular velocity
e:=.001:              # small time interval
i:=0:                # i counts the number of time steps
while r<2 do          # run the program until r=2
i:=i+1:              # increase the counter by 1
r2:=(r*q1^2-9.8*(1-cos(q)))/2: # the first of the given eqs
r:=r+e*r1:           # how r changes, by definition of r1
r1:=r1+e*r2:         # how r1 changes, by definition of r2
q2:=-2*r1*q1/r-9.8*sin(q)/r: # the second of the given eqs
q:=q+e*q1:           # how q changes, by definition of q1
q1:=q1+e*q2:         # how q1 changes, by definition of q2
end do:              # the Maple command to stop the do loop
i*e;                 # print the value of the time

```

This yields a time of  $t = 8.057$  s. If we instead use a time interval of 0.0001 s, we obtain  $t = 8.1377$  s. And a time interval of 0.00001 s gives  $t = 8.14591$  s. So the correct time must be somewhere around 8.15 s.