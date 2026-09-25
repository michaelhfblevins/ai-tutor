# Appendix E Diagonalizing matrices

![Figure E.1: A square of side length a and mass m in the x-y plane. The square is shaded gray and has its bottom-left corner at the origin (0,0). The x and y axes are shown as arrows. The side length 'a' is labeled on the top and right edges, and the mass 'm' is labeled inside the square.](689c593c5eb66a3ec7f63a3db884b864_img.jpg)

Figure E.1: A square of side length a and mass m in the x-y plane. The square is shaded gray and has its bottom-left corner at the origin (0,0). The x and y axes are shown as arrows. The side length 'a' is labeled on the top and right edges, and the mass 'm' is labeled inside the square.

Fig. E.1

This appendix is relevant to Section 9.3, which covers principal axes. The process of diagonalizing matrices (that is, finding the *eigenvectors* and *eigenvalues*, defined below) has countless applications in a wide variety of subjects. We'll describe the process here as it applies to principal axes and moments of inertia.

Let's find the three principal axes and moments of inertia for a square with side length  $a$ , mass  $m$ , and one corner at the origin. The square lies in the  $x$ - $y$  plane, with sides along the  $x$  and  $y$  axes (see Fig. E.1). We'll choose the given  $x$ ,  $y$ , and  $z$  axes as our initial basis axes. Using Eq. (9.8), you can show that the matrix  $\mathbf{I}$  (with respect to this initial basis) is

$$\mathbf{I} = \rho \begin{pmatrix} \int y^2 & -\int xy & 0 \\ -\int xy & \int x^2 & 0 \\ 0 & 0 & \int (x^2 + y^2) \end{pmatrix} = ma^2 \begin{pmatrix} 1/3 & -1/4 & 0 \\ -1/4 & 1/3 & 0 \\ 0 & 0 & 2/3 \end{pmatrix}, \quad (\text{E.1})$$

where  $\rho$  is the mass per unit area, so that  $a^2\rho = m$ . We have used the fact that  $z = 0$ , and we have not bothered to write the  $dx\,dy$  in the integrals.

Our goal is to find the basis in which  $\mathbf{I}$  is diagonal. That is, we want to find three solutions<sup>1</sup> for  $\mathbf{u}$  (and  $I$ ) for the equation  $\mathbf{I}\mathbf{u} = I\mathbf{u}$ . Letting  $I \equiv \lambda ma^2$  to make things look a little cleaner, and using the above explicit form of  $\mathbf{I}$ , the equation  $(\mathbf{I} - I)\mathbf{u} = 0$  becomes

$$ma^2 \begin{pmatrix} 1/3 - \lambda & -1/4 & 0 \\ -1/4 & 1/3 - \lambda & 0 \\ 0 & 0 & 2/3 - \lambda \end{pmatrix} \begin{pmatrix} u_x \\ u_y \\ u_z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}. \quad (\text{E.2})$$

In order for there to be a nonzero solution for the components  $u_x, u_y, u_z$ , the determinant of this matrix must be zero (see Footnote D.2). The resulting cubic

<sup>1</sup> One obvious solution is  $\mathbf{u} = \hat{\mathbf{z}}$ , because  $\mathbf{I}\hat{\mathbf{z}} = (2/3)ma^2\hat{\mathbf{z}}$ . From the orthogonality result of Theorem 9.4, we know that the other two vectors must lie in the  $x$ - $y$  plane. So we could quickly reduce this problem to a two-dimensional one, but let's forge ahead with the general method.

equation for  $\lambda$  is easy to solve, because the determinant is  $[(1/3 - \lambda)^2 - (1/4)^2](2/3 - \lambda) = 0$ . The solutions are  $\lambda = 1/3 \pm 1/4$ , and  $\lambda = 2/3$ . So our three principal moments,  $I \equiv \lambda ma^2$ , are

$$I_1 = \frac{7}{12}ma^2, \quad I_2 = \frac{1}{12}ma^2, \quad I_3 = \frac{2}{3}ma^2. \quad (E.3)$$

These are the *eigenvalues* of  $\mathbf{I}$ .

What are the vectors,  $\mathbf{u}_1$ ,  $\mathbf{u}_2$ , and  $\mathbf{u}_3$ , associated with each of these  $I$ 's? Plugging  $\lambda = 7/12$  into Eq. (E.2) gives the three equations (one for each component),  $-u_x - u_y = 0$ ,  $-u_x - u_y = 0$ , and  $u_z = 0$ . These are redundant equations (that was the point of setting the determinant equal to zero). So  $u_x = -u_y$ , and  $u_z = 0$ . The vector may therefore be written as  $\mathbf{u}_1 = (c, -c, 0)$ , where  $c$  is any constant.<sup>2</sup> If we want a normalized vector, then  $c = 1/\sqrt{2}$ . In a similar manner, plugging  $\lambda = 1/12$  into Eq. (E.2) gives  $\mathbf{u}_2 = (c, c, 0)$ . And finally, plugging  $\lambda = 2/3$  into Eq. (E.2) gives  $\mathbf{u}_3 = (0, 0, c)$ , as claimed in the above footnote. Our three orthonormal principal axes corresponding to the moments in Eq. (E.3) are therefore

$$\hat{\omega}_1 = \left( \frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0 \right), \quad \hat{\omega}_2 = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0 \right), \quad \hat{\omega}_3 = (0, 0, 1). \quad (E.4)$$

These are the *eigenvectors* of  $\mathbf{I}$ . They are shown in Fig. E.2. In the new basis of the principal axes (where  $\hat{\omega}_1 = (1, 0, 0)$ , etc.), the matrix  $\mathbf{I}$  takes the form,

$$\mathbf{I} = ma^2 \begin{pmatrix} 7/12 & 0 & 0 \\ 0 & 1/12 & 0 \\ 0 & 0 & 2/3 \end{pmatrix}. \quad (E.5)$$

![Diagram showing a square in the xy-plane with its center at the origin. Two dashed lines represent the principal axes: one diagonal labeled ω̂₂ and one anti-diagonal labeled ω̂₁. The x and y axes are also shown as solid lines.](b9fd5e6ffc10423405db81b252f939bb_img.jpg)

Diagram showing a square in the xy-plane with its center at the origin. Two dashed lines represent the principal axes: one diagonal labeled ω̂₂ and one anti-diagonal labeled ω̂₁. The x and y axes are also shown as solid lines.

Fig. E.2

In other words, we have “diagonalized” the matrix. The basic idea is that from now on we should use the principal axes as our basis vectors. We can forget that we ever had anything to do with the original  $x$ ,  $y$ , and  $z$  axes.

### REMARKS:

1.  $I_1 + I_2 = I_3$ , as the perpendicular-axis theorem demands.
2.  $I_2$  is the moment around one diagonal through the center of the square, which of course equals the moment around the other diagonal through the center. But the latter is related to  $I_1$  by the parallel-axis theorem. And indeed,  $I_1 = I_2 + m(a/\sqrt{2})^2$ .
3. Any axis through the center of the square, in the plane of the square, has the same moment (by Theorem 9.5 or 9.6). So  $I_2$  equals the moment around an axis through the center, parallel to a side. But this is the same as the moment of a stick of length  $a$  around its center (the extent of the square in the direction of the axis is irrelevant). Hence the factor of  $1/12$  in  $I_2$ . ♣

<sup>2</sup> We can solve for  $\mathbf{u}$  only up to an overall constant, because if  $\mathbf{I}\mathbf{u} = I\mathbf{u}$  is true for a certain  $\mathbf{u}$ , then it is also true that  $\mathbf{I}(c\mathbf{u}) = I(c\mathbf{u})$ , where  $c$  is any constant.