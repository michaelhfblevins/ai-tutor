# Appendix B Multivariable, vector calculus

This appendix gives a brief review of multivariable calculus, also known as vector calculus. The first three topics below (dot product, cross product, partial derivatives) are used often in this book, so if you haven't seen them before, you should read these parts carefully. But the last three topics (gradient, divergence, curl) are used only occasionally, so it isn't crucial that you master these (for this book, at least). For all of the topics, it's possible to go much deeper into them, but I'll present just the basics here. If you want further material, any book on multivariable calculus should do the trick.

### B.1 Dot product

The *dot product*, or *scalar product*, between two vectors is defined to be

$$\mathbf{a} \cdot \mathbf{b} \equiv a_x b_x + a_y b_y + a_z b_z. \quad (\text{B.1})$$

The dot product takes two vectors and produces a scalar, which is just a number. You can quickly use Eq. (B.1) to show that the dot product is commutative and distributive. That is,  $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$ , and  $(\mathbf{a} + \mathbf{b}) \cdot \mathbf{c} = \mathbf{a} \cdot \mathbf{c} + \mathbf{b} \cdot \mathbf{c}$ . Note that the dot product of a vector with itself is  $\mathbf{a} \cdot \mathbf{a} = a_x^2 + a_y^2 + a_z^2$ , which is just its length squared,  $|\mathbf{a}|^2 \equiv a^2$ .

Taking the sum of the products of the corresponding components of two vectors, as we did in Eq. (B.1), might seem like a silly and arbitrary thing to do. Why don't we instead look at the sum of the cubes of the products of the corresponding components? The reason is that the dot product as we've defined it has many nice properties, the most useful of which is that it can be written as

$$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}| \cos \theta \equiv ab \cos \theta, \quad (\text{B.2})$$

where  $\theta$  is the angle between the two vectors. We can demonstrate this as follows. Consider the dot product of the vector  $\mathbf{c} \equiv \mathbf{a} + \mathbf{b}$  with itself, which is simply the

![Figure B.1: A triangle formed by vectors a, b, and c. Vector a is horizontal, vector b is at an angle theta to the horizontal dashed line, and vector c is the third side. The interior angle at the vertex between a and b is labeled gamma.](d7a508d59ed339ca6309abff3d85fe94_img.jpg)

Figure B.1: A triangle formed by vectors a, b, and c. Vector a is horizontal, vector b is at an angle theta to the horizontal dashed line, and vector c is the third side. The interior angle at the vertex between a and b is labeled gamma.

Fig. B.1

square of the length of  $\mathbf{c}$ . Using the commutative and distributive properties, we have

$$\begin{aligned} c^2 &= (\mathbf{a} + \mathbf{b}) \cdot (\mathbf{a} + \mathbf{b}) = \mathbf{a} \cdot \mathbf{a} + 2\mathbf{a} \cdot \mathbf{b} + \mathbf{b} \cdot \mathbf{b} \\ &= a^2 + 2\mathbf{a} \cdot \mathbf{b} + b^2. \end{aligned} \quad (\text{B.3})$$

But from the law of cosines applied to the triangle in Fig. B.1, we have

$$c^2 = a^2 + b^2 - 2ab \cos \gamma = a^2 + b^2 + 2ab \cos \theta, \quad (\text{B.4})$$

because  $\gamma = \pi - \theta$ . Comparing this with Eq. (B.3) yields  $\mathbf{a} \cdot \mathbf{b} = ab \cos \theta$ , as desired. The angle between two vectors is therefore given by

$$\cos \theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}. \quad (\text{B.5})$$

A nice corollary of this result is that if the dot product of two vectors is zero, then  $\cos \theta = 0$ , which means that the vectors are perpendicular. If someone gives you the vectors  $(1, -2, 3)$  and  $(4, 5, 2)$ , it's by no means obvious that they're perpendicular. But you know from Eq. (B.5) that they indeed are.

Geometrically, the dot product  $\mathbf{a} \cdot \mathbf{b} = ab \cos \theta$  equals the length of  $\mathbf{a}$  times the component of  $\mathbf{b}$  along  $\mathbf{a}$ . Or vice versa, depending on which length you want to group the  $\cos \theta$  factor with. If we rotate our coordinate system, the dot product of two vectors remains the same, because it depends only on their lengths and the angle between them, and these are unaffected by the rotation. In other words, the dot product is a scalar. This certainly isn't obvious from looking at the original definition in Eq. (B.1), because the coordinates get all messed up during the rotation.

---

**Example (Distance on the earth):** Given the longitude angle  $\phi$  and the polar angle  $\theta$  (measured down from the north pole, so  $\theta$  is  $90^\circ$  minus the latitude angle) for two points on the earth, what is the distance between them, as measured along the earth?

**Solution:** Our goal is to find the angle,  $\beta$ , between the radii vectors to the two points, because the desired distance is then  $R\beta$ . This would be a tricky problem if we didn't have the dot product at our disposal, but things are easy if we make use of Eq. (B.5) to say that  $\cos \beta = \mathbf{r}_1 \cdot \mathbf{r}_2 / R^2$ . The problem then reduces to finding  $\mathbf{r}_1 \cdot \mathbf{r}_2$ . The Cartesian components of these vectors are

$$\begin{aligned} \mathbf{r}_1 &= R(\sin \theta_1 \cos \phi_1, \sin \theta_1 \sin \phi_1, \cos \theta_1), \\ \mathbf{r}_2 &= R(\sin \theta_2 \cos \phi_2, \sin \theta_2 \sin \phi_2, \cos \theta_2). \end{aligned} \quad (\text{B.6})$$

The desired distance is then  $R\beta = R \cos^{-1}(\mathbf{r}_1 \cdot \mathbf{r}_2 / R^2)$ , where

$$\begin{aligned} \mathbf{r}_1 \cdot \mathbf{r}_2 / R^2 &= \sin \theta_1 \sin \theta_2 (\cos \phi_1 \cos \phi_2 + \sin \phi_1 \sin \phi_2) + \cos \theta_1 \cos \theta_2 \\ &= \sin \theta_1 \sin \theta_2 \cos(\phi_2 - \phi_1) + \cos \theta_1 \cos \theta_2. \end{aligned} \quad (\text{B.7})$$

We can check some limits: If  $\phi_1 = \phi_2$ , then this gives  $\beta = \theta_2 - \theta_1$  (or  $\theta_1 - \theta_2$ , depending on which is larger), as expected. And if  $\theta_1 = \theta_2 = 90^\circ$ , then it gives  $\beta = \phi_2 - \phi_1$  (or  $\phi_1 - \phi_2$ ), as expected.

### B.2 Cross product

The *cross product*, or *vector product*, between two vectors is defined via a determinant to be

$$\mathbf{a} \times \mathbf{b} \equiv \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix} = \hat{\mathbf{x}}(a_y b_z - a_z b_y) + \hat{\mathbf{y}}(a_z b_x - a_x b_z) + \hat{\mathbf{z}}(a_x b_y - a_y b_x). \quad (\text{B.8})$$

The cross product takes two vectors and produces another vector. As with the dot product, you can show that the cross product is distributive. However, it is *anti-commutative* (that is,  $\mathbf{a} \times \mathbf{b} = -\mathbf{b} \times \mathbf{a}$ ), which is evident from Eq. (B.8). So the cross product of any vector with itself is zero.

As with the dot product, the reason why we study this particular combination of components is that it has many nice properties, the most useful of which are that its direction is perpendicular to both  $\mathbf{a}$  and  $\mathbf{b}$  (in the orientation determined by the right-hand rule; see below), and its magnitude is

$$|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}| \sin \theta \equiv ab \sin \theta. \quad (\text{B.9})$$

Let's first show that  $\mathbf{a} \times \mathbf{b}$  is indeed perpendicular to both  $\mathbf{a}$  and  $\mathbf{b}$ . We'll do this by making use of the above handy fact that if the dot product of two vectors is zero, then the vectors are perpendicular. We have

$$\mathbf{a} \cdot (\mathbf{a} \times \mathbf{b}) = a_x(a_y b_z - a_z b_y) + a_y(a_z b_x - a_x b_z) + a_z(a_x b_y - a_y b_x) = 0, \quad (\text{B.10})$$

as desired. Likewise for  $\mathbf{b}$ . There is still an ambiguity, however, because although we know that  $\mathbf{a} \times \mathbf{b}$  points along the direction perpendicular to the plane spanned by  $\mathbf{a}$  and  $\mathbf{b}$ , there are two possible directions along this line. Assuming that our coordinate system has been chosen to be “right-handed” (that is, if you point the fingers of your right hand in the direction of  $\hat{\mathbf{x}}$  and then swing them to  $\hat{\mathbf{y}}$ , your thumb points along  $\hat{\mathbf{z}}$ ), then the direction of  $\mathbf{a} \times \mathbf{b}$  is determined by the right-hand rule. That is, if you point the fingers of your right hand in the direction of  $\mathbf{a}$  and then swing them to  $\mathbf{b}$  (through the angle that is less than  $180^\circ$ ), your thumb points along  $\mathbf{a} \times \mathbf{b}$ . This is consistent with the fact that Eq. (B.8) gives  $(1, 0, 0) \times (0, 1, 0) = (0, 0, 1)$ , or  $\hat{\mathbf{x}} \times \hat{\mathbf{y}} = \hat{\mathbf{z}}$ .

Let's now demonstrate the  $|\mathbf{a} \times \mathbf{b}| = ab \sin \theta$  result, which is equivalent to  $|\mathbf{a} \times \mathbf{b}|^2 = a^2 b^2 (1 - \cos^2 \theta)$ , which is equivalent to  $|\mathbf{a} \times \mathbf{b}|^2 = a^2 b^2 - (\mathbf{a} \cdot \mathbf{b})^2$ . Written in terms of the components, this last equation is

$$\begin{aligned} & (a_y b_z - a_z b_y)^2 + (a_z b_x - a_x b_z)^2 + (a_x b_y - a_y b_x)^2 \\ &= (a_x^2 + a_y^2 + a_z^2)(b_x^2 + b_y^2 + b_z^2) - (a_x b_x + a_y b_y + a_z b_z)^2. \end{aligned} \quad (\text{B.11})$$

If you stare at this long enough, you'll see that it's true. The three different types of terms agree on both sides. For example, both sides have an  $a_y^2 b_z^2$  term, a  $-2a_y b_y a_z b_z$  term, and no  $a_x^2 b_x^2$  term.

### B.3 Partial derivatives

When dealing with a function of only one variable, there is no ambiguity when taking a derivative. However, with a function of many variables, we have to specify which one of the variables we're differentiating with respect to. If we have a function of, say, two variables,  $f(x, y)$ , and if we want to take the derivative with respect to  $x$ , then we use the terminology “*partial derivative* with respect to  $x$ ,” with the notation  $\partial f / \partial x$ . To evaluate this partial derivative, we don't have to do anything fancy. We just take a regular derivative with respect to  $x$ , while assuming that  $y$  is constant. For example, if  $f(x, y) = x - 2y + x^2 y^3$ , then  $\partial f / \partial x = 1 + 2xy^3$ , and  $\partial f / \partial y = -2 + 3x^2 y^2$ . If we plot the value of  $f$  as the height above the  $x$ - $y$  plane, then when we take the partial derivative with respect to  $x$ , we're simply finding the slope of the curve formed by the intersection of the function's surface with the vertical plane parallel to the  $x$  axis and passing through the point in question. Similarly for  $y$ .

If we want to maximize or minimize a function of more than one variable, we need to set all the partial derivatives equal to zero. This is true because if the partial derivative with respect to a certain variable isn't zero, then the slope of the function in that direction is nonzero, which means that the point can't be a local maximum or minimum. This argument is the same as in the single-variable case. It's just that now we can make the argument for each of the variables independently.

Demanding that all the partial derivatives equal zero doesn't actually guarantee having a local maximum or minimum. The point in question might be a *saddle point*, which means that the function is a local maximum in some directions and a local minimum in others (so in two dimensions the function looks like a saddle; hence the name). For example, consider the function of two variables,  $f(x, y) = 3x^2 - y^2$ . Then the point  $(0, 0)$  is a local minimum in the  $x$  direction and a local maximum in the  $y$  direction.

For two variables, if the second partial derivatives have opposite signs at a point where the first partial derivatives are zero, then we have a saddle point, because there is an upward parabola in one direction and a downward parabola

in the other. However, we might have a saddle point even if the second partial derivatives have the same sign. For example, if we make the change of variables  $x \equiv w - z$  and  $y \equiv w + z$  in  $f(x, y) = 3x^2 - y^2$ , then it becomes  $f(w, z) = 2w^2 + 2z^2 - 8wz$ . If we didn't already know from the  $f(x, y)$  form that  $(0, 0)$  is a saddle point, we could deduce this in the following way. Imagine that  $z$  is given, and then solve for the  $w$  that makes  $f(w, z) = 0$ . The result of solving this quadratic equation is that  $w$  takes the form of some multiple of  $z$ . That is,  $w = Az$ , where  $A$  happens to be  $2 \pm \sqrt{3}$  in the present case. Since there are two (real) solutions for  $A$  here, there are two lines, namely  $w = (2 \pm \sqrt{3})z$ , emanating from  $(0, 0)$  for which  $f(w, z) = 0$ . So  $(0, 0)$  can't be a local maximum or minimum. It must therefore be a saddle point.<sup>1</sup>

In general, there are two real solutions for  $A$  if and only if the discriminant of the above quadratic equation is positive. For an arbitrary function of two variables, its shape in the vicinity of a point (which we will take to be  $(0, 0)$  after a shift in the coordinates) where both first partial derivatives are zero can be approximated by the Taylor series to second order (which you can verify by taking various derivatives, just as you would do with a function of one variable),

$$f(x, y) = C + \frac{1}{2} \left( \frac{\partial^2 f}{\partial x^2} \right) x^2 + \frac{1}{2} \left( \frac{\partial^2 f}{\partial y^2} \right) y^2 + \left( \frac{\partial^2 f}{\partial x \partial y} \right) xy + \dots, \quad (\text{B.12})$$

where it is understood that the partial derivatives here are evaluated at  $(0, 0)$ . The condition that the discriminant is positive is therefore

$$\left( \frac{\partial^2 f}{\partial x \partial y} \right)^2 - \left( \frac{\partial^2 f}{\partial x^2} \right) \left( \frac{\partial^2 f}{\partial y^2} \right) > 0. \quad (\text{B.13})$$

If this is true, then the point is a saddle point. If the left side is less than zero, then the point is a local maximum or minimum, because there are no nearby points for which  $f(x, y) = C$ ; they are all either greater than  $C$  or less than  $C$ . If the left side equals zero, then the function looks like a trough, at least in the vicinity of the point in question (assuming that there is at least some quadratic dependence in the function).

<sup>1</sup> This is true because along these two lines, the first partial derivatives aren't zero, which means that the plane of the function's surface is tilted there. So the function is positive on one side of each line and negative on the other, which is exactly what happens with a saddle. There is, however, the special case where the discriminant of the quadratic equation is zero (as with, for example,  $f(x, y) = (x - y)^2$ ), in which case there is only one solution for  $A$  and thus only one line for which the function is zero. In this case, the function looks like a (possibly upside down) trough. It is zero (or some given constant) along the line, at least to second order. And it curves up (or down) quadratically as you move away from the line (assuming that there is at least some quadratic dependence in the function).

### B.4 Gradient

Given a function  $f(x, y, z)$  (we'll work mainly with three variables from now on), we can form the vector whose components are the partial derivatives of  $f$ , namely  $(\partial f / \partial x, \partial f / \partial y, \partial f / \partial z)$ . This vector is called the *gradient*. If we define the differential vector operator  $\nabla$  (usually called “del”) to be  $\nabla \equiv (\partial / \partial x, \partial / \partial y, \partial / \partial z)$ , then the gradient is simply

$$\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right). \quad (\text{B.14})$$

The gradient takes a function and produces a vector. For example, if  $f(x, y, z) = xy^2 - yz^3$ , then  $\nabla f = (y^2, 2xy - z^3, -3yz^2)$ . We call  $\nabla$  an “operator” because it needs to operate on a function to produce the gradient vector.

What is the physical meaning of the gradient? The gradient gives the direction you should march in if you want  $f$  to increase at the greatest rate. The reason for this is the following. Consider the value of a function  $f(x, y, z)$  at a certain point, and then look at the value at a nearby point, displaced by the vector  $(dx, dy, dz)$ . What (approximately, to first order) is the change in  $f$  between the two points? Well, as you march a distance  $dx$  in the  $x$  direction, the (first-order) change in  $f$  is  $(\partial f / \partial x) dx$ , by the definition of the partial derivative (just as in the one-variable case). If you then march a distance  $dy$  in the  $y$  direction, the function changes by an additional amount of  $(\partial f / \partial y) dy$ . And likewise the  $z$  direction gives a change of  $(\partial f / \partial z) dz$ . Adding up these three changes in  $f$ , we see that the total first-order change in  $f$  is<sup>2</sup>

$$df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz. \quad (\text{B.15})$$

Using the dot product, this can be written concisely as

$$df = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right) \cdot (dx, dy, dz) \equiv \nabla f \cdot d\mathbf{r}. \quad (\text{B.16})$$

We can now make use of Eq. (B.2) to say that the change in  $f$  is  $df = |\nabla f| |d\mathbf{r}| \cos \theta$ , where  $\theta$  is the angle between  $\nabla f$  and  $d\mathbf{r}$ . The meaning of this is the following. Consider a given point  $(x, y, z)$ . The  $\nabla f$  gradient vector at this point is a particular vector. Imagine marching along little  $d\mathbf{r}$  vectors in various directions and seeing how much  $f$  changes (assume that all the  $d\mathbf{r}$  vectors have the same length, to be consistent). What direction should you march in, in order to have  $f$  change the most? Or not change at all? In the  $df = |\nabla f| |d\mathbf{r}| \cos \theta$

<sup>2</sup> There is technically an ambiguity in where each of these partial derivative is evaluated, because the three little steps you took started at three different points. But these ambiguities involve first-order corrections to the partial derivatives, and since these partial derivatives are already being multiplied by the first-order  $dx$ ,  $dy$ , and  $dz$  terms in Eq. (B.15), any ambiguities will result in second-order effects and can therefore be ignored.

expression,  $|\nabla f|$  has a definite value at the point in question, and we're assuming that we pick  $|d\mathbf{r}|$  to always be the same, so it comes down to the  $\cos \theta$  factor. Therefore, if you march directly along the  $\nabla f$  gradient vector at the point, then  $f$  increases the most. And if you march in any direction in the plane perpendicular to  $\nabla f$ , then  $f$  doesn't change at all (to first order). And if you march in the direction anti-parallel to  $\nabla f$ , then  $f$  decreases the most.

This is more easily visualized in the case of a function of only two variables,  $f(x, y)$ , because then we can picture the value of  $f$  as being the height in the  $z$  direction. The graph of  $f$  is just a surface of mountains and valleys above (or below) the  $x$ - $y$  plane. The gradient  $\nabla f = (\partial f / \partial x, \partial f / \partial y)$  then gives the direction of steepest ascent. That is,  $f$  changes at the greatest rate if you march in the direction of  $\nabla f$  in the  $x$ - $y$  plane; the slope of the surface in this direction in the  $x$ - $y$  plane is larger than in any other direction. And if you march in either direction along the line in the  $x$ - $y$  plane that is perpendicular to  $\nabla f$ , then  $f$  has zero change. By continuing to march along the direction perpendicular to  $\nabla f$  wherever you are, you will form a curve in the  $x$ - $y$  plane for which all the points give the same value of  $f$ . In other words, if you slice the surface of  $f$  with a horizontal plane whose height equals this particular value of  $f$ , and if you look at the intersection of this plane with the surface, then the projection of this intersection onto the  $x$ - $y$  plane is the above curve you formed in the  $x$ - $y$  plane.

### B.5 Divergence

Consider a vector whose components are functions of the coordinates. For example, let  $\mathbf{F} = (F_x, F_y, F_z) = (3xz, 2y^2 + xyz, x^2 + z^3)$ . Then the *divergence* of  $\mathbf{F}$  is defined to be the dot product of the  $\nabla$  operator with  $\mathbf{F}$ , that is,

$$\nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}. \quad (\text{B.17})$$

The divergence takes a vector and produces a number. The above  $\mathbf{F}$  has a divergence of  $(3z) + (4y + xz) + (3z^2)$ .

What is the physical meaning of the divergence? Consider an infinitesimal box with sides of length  $dx$ ,  $dy$ , and  $dz$ . Then the divergence measures the net flux of the vector field out of the box, divided by the volume of the box. (The flux through a surface is defined to be the integral of the area times the component of the vector perpendicular to the surface.) For example, if a certain vector field gives the velocity at each point in a fluid flow, and if the divergence is nonzero, then there must be a source (or sink) that creates (or destroys) fluid, because otherwise whatever fluid goes into the little box would have to come out of it somewhere, yielding zero net flux.

Let's see why the divergence equals the flux per volume. Consider the "left"  $dy \times dz$  face of the little box. The amount of flux from the vector field into the box through this face equals the area  $dy \, dz$  times the  $F_x$  component. (The  $F_y$  and

$F_z$  components are parallel to this face and therefore contribute nothing to the flux through it.) The amount of flux *out* of the “right”  $dy \times dz$  face equals the area  $dy \, dz$  times the value of the  $F_x$  component there. But this value equals (to first order) the original  $F_x$  plus  $(\partial F_x / \partial x) \, dx$ , by the definition of the partial derivative. The  $F_x$  part of this cancels the inward flux from the left face, so the net flux out of the little box through these two faces is  $((\partial F_x / \partial x) \, dx) \, dy \, dz$ . Similar calculations work for the other two pairs of parallel faces, so the total flux out of the box is

$$\text{Net flux} = \left( \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z} \right) dx \, dy \, dz. \quad (\text{B.18})$$

Therefore, as promised, the net flux per volume equals the divergence. The integrated form of this result is the *divergence theorem*, or *Gauss’ theorem*, which takes the form,

$$\int_V \nabla \cdot \mathbf{F} \, dV = \int_S \mathbf{F} \cdot d\mathbf{A}. \quad (\text{B.19})$$

The integral on the left runs over a given volume, and the integral on the right runs over the surface that encloses this volume. The vector  $d\mathbf{A}$  has a magnitude equal to an infinitesimal piece of area of  $S$  and a direction defined to be perpendicular to the plane containing this piece (with the positive direction being outward from the volume). Dotting  $d\mathbf{A}$  with  $\mathbf{F}$  has the effect of picking out only the component of  $\mathbf{F}$  that is perpendicular to the piece (which is what is relevant in calculating the flux).

We’ll skip the fine details here, but the basic idea of the proof of Eq. (B.19) is to divide the volume up into many infinitesimal cubes and to look at the total flux through all the cubes. From Eq. (B.18), the integral of the divergence over one little cube (which is essentially the divergence times the volume, because the divergence is essentially constant over the tiny volume) equals the flux through that cube. The integral of the divergence over the whole volume therefore equals the sum of the fluxes through all the cubes. But all the faces of the cubes that lie in the interior of the volume are shared by two cubes, so the flux through these faces cancels when taking the sum (because the flux through a given face is counted positive for one cube and negative for the other). So we are left with only the flux through the faces on the boundary of the volume (because these faces appear only once in the total integral). We are therefore left with the flux through the surface  $S$ , which is what appears on the right-hand side of Eq. (B.19).

---

**Example (Flux through a sphere):** Verify the divergence theorem in the case where the surface is a sphere of radius  $R$  centered at the origin, and  $\mathbf{F} = (x, y, z)$ .

**Solution:** On the left-hand side of Eq. (B.19), the divergence of  $(x, y, z)$  is  $1+1+1=3$ , so the integral of this over the volume of the sphere is simply  $3(4\pi R^3/3) = 4\pi R^3$ . On the right-hand side, the unit vector perpendicular to the surface is  $(x, y, z)/R$ , so

$d\mathbf{A} = (dA)(x, y, z)/R$ . The dot product of this with  $(x, y, z)$  is  $(dA)(x^2 + y^2 + z^2)/R = (dA)R$ . The integral of this over the surface of the sphere is just  $(4\pi R^2)R = 4\pi R^3$ . The two sides are therefore equal, as we wanted to show.

### B.6 Curl

Consider a vector whose components are functions of the coordinates. For example, let  $\mathbf{F} = (F_x, F_y, F_z) = (3xz, x^2yz, x + z)$ . Then the *curl* of  $\mathbf{F}$  is defined to be the cross product of the  $\nabla$  operator with  $\mathbf{F}$ , that is,

$$\begin{aligned}\nabla \times \mathbf{F} &\equiv \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ \partial/\partial x & \partial/\partial y & \partial/\partial z \\ F_x & F_y & F_z \end{vmatrix} \\ &= \left( \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}, \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}, \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right). \end{aligned} \quad (\text{B.20})$$

The curl takes a vector and produces another vector. The above  $\mathbf{F}$  has a curl of  $(-x^2y, 3x - 1, 2xyz)$ .

What is the physical meaning of the curl? Consider the infinitesimal rectangle shown in Fig. B.2. This rectangle lies in the  $x$ - $y$  plane, so for the moment we will suppress the  $z$  component of all coordinates, for convenience. It turns out that the  $z$  component of the curl equals the counterclockwise integral  $\int \mathbf{F} \cdot d\mathbf{r}$  around the closed loop, divided by the area of the loop (similar statements hold for the  $y$  and  $x$  components and the associated little rectangles in the  $x$ - $z$  and  $y$ - $z$  planes). Let's see why this is true.

The total counterclockwise integral of  $\mathbf{F} \cdot d\mathbf{r}$  around the loop entails moving to the right on segment 1 and to the left on 3, and up on segment 2 and down on 4. On segments 1 and 3, both  $dy$  and  $dz$  are zero, so only the  $F_x dx$  term survives in the dot product  $\mathbf{F} \cdot d\mathbf{r}$ . Likewise,  $F_y dy$  is the only nonzero term on segments 2 and 4. If we pair up the two pairs of parallel sides, the total counterclockwise integral is

$$\begin{aligned}\int \mathbf{F} \cdot d\mathbf{r} &= \int_X^{X+dX} (F_x(x, Y) - F_x(x, Y + dY)) dx \\ &\quad + \int_Y^{Y+dY} (F_y(X + dX, y) - F_y(X, y)) dy. \end{aligned} \quad (\text{B.21})$$

Let's approximate the differences in these parentheses. To first order, we have

$$F_x(x, Y + dY) - F_x(x, Y) \approx dY \frac{\partial F_x(x, y)}{\partial y} \bigg|_{(x, Y)} \approx dY \frac{\partial F_x(x, y)}{\partial y} \bigg|_{(x, Y)}. \quad (\text{B.22})$$

![Diagram of an infinitesimal rectangle in the x-y plane. The rectangle has vertices at (X, Y), (X+dX, Y), (X+dX, Y+dY), and (X, Y+dY). The sides are labeled with circled numbers 1, 2, 3, and 4, indicating a counterclockwise path. Segment 1 is the bottom horizontal side from (X, Y) to (X+dX, Y). Segment 2 is the right vertical side from (X+dX, Y) to (X+dX, Y+dY). Segment 3 is the top horizontal side from (X+dX, Y+dY) to (X, Y+dY). Segment 4 is the left vertical side from (X, Y+dY) to (X, Y). Arrows on the segments indicate the direction of integration. A coordinate system with x and y axes is shown to the left of the rectangle.](e954d77acf25062fd2c651b34fb95d32_img.jpg)

Diagram of an infinitesimal rectangle in the x-y plane. The rectangle has vertices at (X, Y), (X+dX, Y), (X+dX, Y+dY), and (X, Y+dY). The sides are labeled with circled numbers 1, 2, 3, and 4, indicating a counterclockwise path. Segment 1 is the bottom horizontal side from (X, Y) to (X+dX, Y). Segment 2 is the right vertical side from (X+dX, Y) to (X+dX, Y+dY). Segment 3 is the top horizontal side from (X+dX, Y+dY) to (X, Y+dY). Segment 4 is the left vertical side from (X, Y+dY) to (X, Y). Arrows on the segments indicate the direction of integration. A coordinate system with x and y axes is shown to the left of the rectangle.

Fig. B.2

The first approximation here is valid due to the definition of the partial derivative. The second approximation (replacing  $x$  with  $X$ ) is valid because our rectangle is small enough so that  $x$  is essentially equal to  $X$ . Any error in this approximation is second-order small, because we already have a factor of  $dY$  in our term. A similar treatment works for the  $F_y$  terms, so Eq. (B.21) becomes

$$\int \mathbf{F} \cdot d\mathbf{r} = \int_Y^{Y+dY} dX \frac{\partial F_y(x,y)}{\partial x} \bigg|_{(X,Y)} dy - \int_X^{X+dX} dY \frac{\partial F_x(x,y)}{\partial y} \bigg|_{(X,Y)} dx. \quad (\text{B.23})$$

The integrands are constants, so we can quickly perform the integrals to obtain

$$\int \mathbf{F} \cdot d\mathbf{r} = dX dY \left( \frac{\partial F_y(x,y)}{\partial x} - \frac{\partial F_x(x,y)}{\partial y} \right) \bigg|_{(X,Y)}. \quad (\text{B.24})$$

As promised, the  $z$  component of the curl equals the counterclockwise integral  $\int \mathbf{F} \cdot d\mathbf{r}$  around the closed loop, divided by the area of the loop. The preceding analysis also works, of course, for little rectangles in the  $x$ - $z$  and  $y$ - $z$  planes. We therefore obtain the two other components of the curl.

The generalization of the above result to tilted and wavy surfaces is *Stokes' theorem*, which states that

$$\int_S (\nabla \times \mathbf{F}) \cdot d\mathbf{A} = \int_C \mathbf{F} \cdot d\mathbf{r}. \quad (\text{B.25})$$

The integral on the left runs over a given surface, and the integral on the right runs over the curve that is the boundary of this surface. The vector  $d\mathbf{A}$  has a magnitude equal to an infinitesimal piece of area of  $S$  and a direction defined to be perpendicular to the plane containing this piece (with its orientation defined via the orientation along  $C$  and the right-hand rule). We'll skip the details here, but the basic idea of the proof is similar to the idea behind the divergence theorem above, except with certain words replaced by other words ("volume" becomes "surface," and "surface" becomes "curve," etc.). We'll divide the surface up into many infinitesimal rectangles and look at the total integral around all the rectangles. For simplicity, let's just deal with a flat surface in the  $x$ - $y$  plane.

From above, the integral of the  $z$  component of the curl over one little rectangle equals the counterclockwise integral of  $\mathbf{F} \cdot d\mathbf{r}$  around the edges of the rectangle. The integral of the  $z$  component of the curl over the whole surface therefore equals the sum of the integrals around all the rectangles. But all the edges of the rectangles that lie in the interior of the surface are shared by two rectangles, so the integral along these edges cancels when taking the sum (because the integral along a given edge is counted positive for one rectangle and negative for the other). So we are left with only the integral along the edges on the boundary of the surface (because these edges appear only once in the total integral). We are therefore left with the integral along the curve  $C$ , which is what appears on the right-hand side of Eq. (B.25).

Note that if the surface is closed, so that it has no boundary (in other words, there is no curve  $C$ ), then the right-hand side of Eq. (B.25) is zero, and hence the left-hand side is also. Such is the case with, for example, a sphere. Having no boundary means that if you're a little bug walking on the surface, you can't walk off it.

---

**Example (Integral around a circle):** Verify Stokes' theorem in the case where the curve is a circle of radius  $R$  in the  $x$ - $y$  plane, centered at the origin, and  $\mathbf{F} = (-y, x, 0)$ .

**Solution:** On the left-hand side of Eq. (B.25), the curl of  $(-y, x, 0)$  is  $(0, 0, 2)$ . The  $d\mathbf{A}$  vector also points in the  $z$  direction, so the dot product is just  $2(dA)$ . The integral of this over the interior of the circle is simply  $2(\pi R^2)$ . On the right-hand side, the dot product equals  $-y dx + x dy$ . Integrating this along the circumference of the circle is most easily done in polar coordinates. With  $x = R \cos \theta$  and  $y = R \sin \theta$ , we have  $dx = -R \sin \theta d\theta$  and  $dy = R \cos \theta d\theta$ . So  $-y dx + x dy = R^2 d\theta$ . The integral of this as  $\theta$  ranges from 0 to  $2\pi$  is  $R^2(2\pi)$ . The two sides are therefore equal, as desired.

---

There are some handy facts that deal with combinations of the gradient, divergence, and curl. One is that the curl of a gradient is identically zero. That is,  $\nabla \times \nabla f = 0$ . You can verify this explicitly by using the definitions of the curl and the gradient, and also the fact that partial differentiation is commutative (that is,  $\partial^2 f / \partial x \partial y = \partial^2 f / \partial y \partial x$ ). Alternatively, you can let  $\mathbf{F} \equiv \nabla f$  in Stokes' theorem, which gives  $\int_S (\nabla \times \nabla f) \cdot d\mathbf{A} = \int_C \nabla f \cdot d\mathbf{r}$ . The right-hand side of this is simply the net change in the function  $f$  around the closed curve  $C$ , which is always zero. The integrand on the left-hand side must therefore identically be zero.

Also, the divergence of a curl is identically zero. That is,  $\nabla \cdot (\nabla \times \mathbf{F}) = 0$ . Again, you can verify this explicitly by using the definitions of the divergence and the curl, and also the fact that partial differentiation is commutative. Alternatively, you can combine Gauss' theorem and Stokes' theorem to write  $\int_V \nabla \cdot (\nabla \times \mathbf{F}) dV = \int_C \mathbf{F} \cdot d\mathbf{r}$ . The right-hand side is always zero, because the boundary surface  $S$  of any given volume  $V$  is closed, so there is no curve  $C$ . The integrand on the left-hand side must therefore identically be zero.