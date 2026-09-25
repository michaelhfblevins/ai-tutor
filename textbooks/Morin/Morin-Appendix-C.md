# Appendix C $F = ma$ vs. $F = dp/dt$

In nonrelativistic mechanics,<sup>1</sup> the equations  $F = ma$  and  $F = dp/dt$  say exactly the same thing if  $m$  is constant. But if  $m$  is not constant, then  $dp/dt = d(mv)/dt = ma + (dm/dt)v$ , which doesn't equal  $ma$ . So if a system has a changing mass, should we use  $F = ma$  or  $F = dp/dt$ ? Which equation correctly describes the physics? The answer to this depends on what you label as the system to which you associate the quantities  $m$ ,  $p$ , and  $a$ . You can generally do a problem using either  $F = ma$  or  $F = dp/dt$ , but you must be very careful about how you label things and how you treat them. The subtleties are best understood through two examples.

---

**Example 1 (Sand dropping into a cart):** Consider a cart into which sand is dropped vertically at a rate  $dm/dt = \sigma$ . With what force must you push on the cart to keep it moving horizontally at a constant speed  $v$ ? (This was the setup in the first example in Section 5.8.)

**First solution:** Let  $m(t)$  be the mass of the cart-plus-sand-inside system (which we'll just call the "cart"). If we use  $F = ma$  (where  $a$  is the acceleration of the cart, which is zero), then we obtain  $F = 0$ , which is incorrect. The correct expression to use is  $F = dp/dt$ . This gives

$$F = \frac{dp}{dt} = ma + \frac{dm}{dt}v = 0 + \sigma v. \quad (\text{C.1})$$

This makes sense, because your force is what increases the momentum of the cart, and this momentum increases simply because the mass of the cart increases.

**Second solution:** It is possible to solve this problem by using  $F = ma$  if we let our system be a small piece of mass that is being added to the cart. Your force is what accelerates this mass from rest to speed  $v$ . Consider a mass  $\Delta m$  that falls into the cart during a time  $\Delta t$ . Imagine that it falls into the cart in one lump at the start of the  $\Delta t$ , and then accelerates up to speed  $v$  during the time  $\Delta t$ . (It accelerates due to friction. But if you want, you can eliminate the cart as the intermediate object and just push directly on the mass.) This process repeats during each successive  $\Delta t$  interval. We

<sup>1</sup> We won't bother with relativity in this appendix, because nonrelativistic mechanics contains all the critical aspects we want to address.

can use  $F = ma$  here because the mass of the small piece is constant. So we have  $F = ma = \Delta m(v/\Delta t)$ . Writing this as  $(\Delta m/\Delta t)v$  gives the  $\sigma v$  result we found above.

**Third solution:** As in the second solution, let's imagine the process occurring in discrete steps, but now with the cart as the system. Assume that a mass  $\Delta m$  falls into the cart and instantaneously decreases its speed (by conservation of momentum) to  $v' = mv/(m + \Delta m)$ , which is  $\Delta v = v - v' = v\Delta m/(m + \Delta m)$  less than the original  $v$ . Assume that you then push on the cart for a time  $\Delta t$  (during which the mass remains constant at  $m + \Delta m$ , so  $F = ma$  is the relevant expression) and bring it back up to speed  $v$ . The acceleration is  $a = \Delta v/\Delta t = v(\Delta m/\Delta t)/(m + \Delta m) = \sigma v/(m + \Delta m)$ , so your force is

$$F = (m + \Delta m)a = (m + \Delta m) \left( \frac{\sigma v}{m + \Delta m} \right) = \sigma v. \quad (C.2)$$

**Example 2 (Sand leaking from a cart):** Consider a cart that leaks sand out of the bottom at a rate  $dm/dt = \sigma$ . If you apply a force  $F$  to the cart, what is its acceleration?

**Solution:** Let  $m(t)$  be the mass of the cart-plus-sand-inside system (the “cart”). In this example, the correct expression to use is  $F = ma$ , so the acceleration is

$$a = \frac{F}{m}. \quad (C.3)$$

Note that since  $m$  decreases with time,  $a$  increases with time. We used  $F = ma$  here because at any instant, the mass  $m$  is what is being accelerated by the force  $F$ . As above, you can imagine the process occurring in discrete steps: You push on the mass for a short period of time, then a little piece instantaneously leaks out; then you push again on the new (smaller) mass, then another little piece leaks out; and so on. In this discretized scenario, it is clear that  $F = ma$  is the appropriate formula, because it holds for each step in the process. The only ambiguity is whether to use  $m$  or  $m + dm$  at a certain time, but this yields a negligible error.

**REMARKS:** It is still true that  $F = dp/dt$  in this second example, provided that you let  $F$  be *total* force, and let  $p$  be the *total* momentum. In this example,  $F$  is the only force. However, the total momentum consists of both the sand in the cart and the sand that has leaked out and is falling through the air.<sup>2</sup> A common mistake is to use  $F = dp/dt$ , with  $p$  being only the cart's momentum. The leaked sand still has momentum.

There is a simple example that demonstrates why  $F = dp/dt$  doesn't work when  $p$  refers only to the cart. Choose  $F = 0$ , so that the cart moves with constant speed  $v$ . Cut the cart in half, and label the back part as the “leaked sand” and the front part as the “cart.” If you want the cart's  $p$  to have  $dp/dt = F = 0$ , then the cart's speed must double if its mass gets cut in half. But this is nonsense. Both halves simply continue to move at the same rate. ♣

<sup>2</sup> If there were air resistance, we would have to worry about its effect on the falling sand if we wanted to use  $F = dp/dt$  to solve the problem, where  $p$  is the total momentum. This is clearly not the best way to do the problem. If complicated things happen with the sand in the air, it would be foolish to consider this part of the sand when we don't have to.

---

To sum up,  $F = dp/dt$  is always valid, provided that you use the *total* force and *total* momentum of a given system of particles. This approach, however, can get messy in certain situations. So in some cases it is easier to use an  $F = ma$  argument, but you must be careful to correctly identify the system that is being accelerated by the force. The asymmetry in the above two examples is that in the first example, the force does indeed accelerate the incoming sand. But in the second example, the force does *not* accelerate (or decelerate) the outgoing sand.  $F$  has nothing to do with the leaked sand.