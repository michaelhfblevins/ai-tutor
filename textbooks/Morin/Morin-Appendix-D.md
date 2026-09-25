# Appendix D Existence of principal axes

In this appendix, we will prove Theorem 9.4. That is, we will show that an orthonormal set of principal axes does indeed exist for any object, and for any choice of origin. It isn't crucial that you study this proof. If you want to just accept the fact that principal axes exist, that's perfectly fine. But the method we will use in this proof is one you will see again and again in your physics studies, in particular when you study quantum mechanics (see the remark following the proof).

**Theorem D.1** *Given a real symmetric  $3 \times 3$  matrix,  $\mathbf{I}$ , there exist three orthonormal real vectors,  $\hat{\mathbf{\omega}}_k$ , and three real numbers,  $I_k$ , with the property that*

$$\mathbf{I}\hat{\mathbf{\omega}}_k = I_k\hat{\mathbf{\omega}}_k. \quad (\text{D.1})$$

**Proof:** This theorem holds more generally with 3 replaced by  $N$  (all the steps below easily generalize), but we'll work with  $N = 3$ , to be concrete. Consider a general  $3 \times 3$  matrix,  $\mathbf{I}$  (we don't need to assume yet that it's real or symmetric). Assume that  $\mathbf{I}\mathbf{u} = I\mathbf{u}$  for some vector  $\mathbf{u}$  and some number  $I$ .<sup>1</sup> This may be rewritten as

$$\begin{pmatrix} (I_{xx} - I) & I_{xy} & I_{xz} \\ I_{yx} & (I_{yy} - I) & I_{yz} \\ I_{zx} & I_{zy} & (I_{zz} - I) \end{pmatrix} \begin{pmatrix} u_x \\ u_y \\ u_z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}. \quad (\text{D.2})$$

In order for there to be a nontrivial solution for the vector  $\mathbf{u}$  (that is, one where  $\mathbf{u} \neq (0, 0, 0)$ ), the determinant of this matrix must be zero.<sup>2</sup> Taking the determinant, we see that we get an equation for  $I$  of the form

$$aI^3 + bI^2 + cI + d = 0. \quad (\text{D.3})$$

<sup>1</sup> Such a vector  $\mathbf{u}$  is called an *eigenvector* of  $\mathbf{I}$ , and the associated  $I$  is called an *eigenvalue*. But don't let these names scare you. They're just definitions.

<sup>2</sup> If the determinant were not zero, then we could explicitly construct the inverse of the matrix, which involves cofactors divided by the determinant. Multiplying both sides by this inverse would yield  $\mathbf{u} = \mathbf{0}$ .

The constants  $a$ ,  $b$ ,  $c$ , and  $d$  are functions of the matrix entries  $I_{ij}$ , but we won't need their precise form to prove this existence theorem. The only thing we need this equation for is to say that there do exist three (generally complex) solutions for  $I$ , because the equation is a cubic.

We will now show that the solutions for  $I$  are real. This will imply that there exist three real vectors  $\mathbf{u}$  satisfying  $\mathbf{I}\mathbf{u} = I\mathbf{u}$ , because we can plug the real  $I$ 's back into Eq. (D.2) and solve for the real components  $u_x$ ,  $u_y$ , and  $u_z$ , up to an overall constant. We will then show that these vectors are orthogonal.

- *Proof that the  $I$ 's are real:* This follows from the real and symmetric conditions on  $\mathbf{I}$ . Start with the equation  $\mathbf{I}\mathbf{u} = I\mathbf{u}$ , and take the dot product with  $\mathbf{u}^*$  to obtain

$$\begin{aligned}\mathbf{u}^* \cdot \mathbf{I}\mathbf{u} &= \mathbf{u}^* \cdot I\mathbf{u} \\ &= I\mathbf{u}^* \cdot \mathbf{u}.\end{aligned}\quad (\text{D.4})$$

The vector  $\mathbf{u}^*$  is the vector obtained by complex conjugating each component of  $\mathbf{u}$  (we don't know yet that  $\mathbf{u}$  can be chosen to be real). On the right side,  $I$  is a scalar, so we can take it out from between the  $\mathbf{u}^*$  and  $\mathbf{u}$ . The fact that  $\mathbf{I}$  is real implies that if we complex conjugate the equation  $\mathbf{I}\mathbf{u} = I\mathbf{u}$ , we obtain  $\mathbf{I}\mathbf{u}^* = I^*\mathbf{u}^*$  (we know that  $\mathbf{I}$  is real, but we don't know yet that  $I$  is real). If we then take the dot product of this equation with  $\mathbf{u}$ , we obtain

$$\mathbf{u} \cdot \mathbf{I}\mathbf{u}^* = I^*\mathbf{u} \cdot \mathbf{u}^*.\quad (\text{D.5})$$

We now claim that if  $\mathbf{I}$  is symmetric, then  $\mathbf{a} \cdot \mathbf{I}\mathbf{b} = \mathbf{b} \cdot \mathbf{I}\mathbf{a}$ , for any vectors  $\mathbf{a}$  and  $\mathbf{b}$ . (We'll leave this for you to show by simply multiplying each side out.) In particular,  $\mathbf{u}^* \cdot \mathbf{I}\mathbf{u} = \mathbf{u} \cdot \mathbf{I}\mathbf{u}^*$ , so Eqs. (D.4) and (D.5) give

$$(I - I^*)\mathbf{u} \cdot \mathbf{u}^* = 0.\quad (\text{D.6})$$

And since  $\mathbf{u} \cdot \mathbf{u}^* = |u_1|^2 + |u_2|^2 + |u_3|^2 \neq 0$ , we must have  $I = I^*$ . Therefore,  $I$  is real.

- *Proof that the  $\mathbf{u}$  are orthogonal:* This follows from the symmetric condition on  $\mathbf{I}$ . Let  $\mathbf{I}\mathbf{u}_1 = I_1\mathbf{u}_1$ , and  $\mathbf{I}\mathbf{u}_2 = I_2\mathbf{u}_2$ . Take the dot product of the former equation with  $\mathbf{u}_2$  to obtain

$$\mathbf{u}_2 \cdot \mathbf{I}\mathbf{u}_1 = I_1\mathbf{u}_2 \cdot \mathbf{u}_1,\quad (\text{D.7})$$

and take the dot product of the latter equation with  $\mathbf{u}_1$  to obtain

$$\mathbf{u}_1 \cdot \mathbf{I}\mathbf{u}_2 = I_2\mathbf{u}_1 \cdot \mathbf{u}_2.\quad (\text{D.8})$$

As above, the symmetric condition on  $\mathbf{I}$  implies that the left-hand sides of Eqs. (D.7) and (D.8) are equal. Therefore,

$$(I_1 - I_2)\mathbf{u}_1 \cdot \mathbf{u}_2 = 0.\quad (\text{D.9})$$

There are two possibilities here: (1) If  $I_1 \neq I_2$ , then we are done, because  $\mathbf{u}_1 \cdot \mathbf{u}_2 = 0$ , which says that  $\mathbf{u}_1$  and  $\mathbf{u}_2$  are orthogonal. (2) If  $I_1 = I_2 \equiv I$ , then we have  $\mathbf{I}(a\mathbf{u}_1 + b\mathbf{u}_2) = I(a\mathbf{u}_1 + b\mathbf{u}_2)$ , for any  $a$  and  $b$ . So any linear combination of  $\mathbf{u}_1$  and  $\mathbf{u}_2$  has the same property that  $\mathbf{u}_1$  and  $\mathbf{u}_2$  have (namely, that applying  $\mathbf{I}$  is the same as just multiplying by  $I$ ). We therefore have a whole plane of such vectors, so we can pick any two orthogonal vectors in this plane to be called  $\mathbf{u}_1$  and  $\mathbf{u}_2$ . ■

This theorem proves the existence of principal axes, because the inertia tensor in Eq. (9.8) is indeed a real and symmetric matrix.

REMARK: (Warning: This remark has nothing to do with classical mechanics. It's simply an ill-disguised excuse to get a limerick on quantum mechanics into the book.) In quantum mechanics, it turns out that any observable quantity, such as position, energy, momentum, angular momentum, etc., can be represented by a *Hermitian* matrix, with the observed value being an eigenvalue of the matrix. A Hermitian matrix is a (generally complex) matrix with the property that the transpose of the matrix equals the complex conjugate of itself. For example, a  $2 \times 2$  Hermitian matrix must be of the form,

$$\begin{pmatrix} a & b + ic \\ b - ic & d \end{pmatrix}, \quad (\text{D.10})$$

for real numbers  $a$ ,  $b$ ,  $c$ , and  $d$ . Now, if observed values are to be given by the eigenvalues of such a matrix, then the eigenvalues had better be real, because no one (in this world, at least) is about to go for a jog of  $4 + 3i$  miles, or pay an electric bill for  $17 - 43i$  kilowatt-hours. And indeed, you can show, via a slightly modified version of the above “Proof that the  $I$ 's are real” procedure, that the eigenvalues of any Hermitian matrix are in fact real. (And likewise, the eigenvectors are orthogonal.) This is, to say the least, very fortunate.

God's first tries were hardly ideal,  
 For complex worlds have no appeal.  
 So in the present edition,  
 He made things Hermitian,  
 And *this* world, it seems, is quite real. ♣