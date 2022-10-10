#!/usr/bin/env python
# coding: utf-8

# # Systems of Linear Equations
# 
# 
# <span style="font-size:20pt;">Examples</span>
# 
# ``````{div} full-width
# 
# - **Systems of linear equations**: $A \mathbf{x} = \mathbf{b}$
# 
# ````{admonition} Example 2.1
# :class: seealso
# :name: system-of-linear-equations-matrix-form-example
# 
# Write the following linear system of equations as a matrix equation
# \begin{align*}
#     2x_1 + x_2 &= 4, \\
#     4x_1 + 3x_2 &= 10.
# \end{align*}
# ````
# 
# - **Solution using inverse matrix:** $\mathbf{x} = A^{-1} \mathbf{b}$
# 
# ````{admonition} Example 2.2
# :class: seealso
# :name: solution-by-inverse-example
# 
# Solve the following systems of linear equations using the inverse of the coefficient matrix:
# 
# &emsp; (i) &emsp; $\begin{array}{rl}
#         x_1 - 2x_2 &= 11, \\
#         2x_1 + 4x_2 &= -18.
#     \end{array}$
# &emsp; &emsp; (ii) &emsp; $\begin{array}{rl}
#         x_1 - 2x_2 + 3x_3 &= -7, \\
#         2x_2 - 4x_3 &= 8, \\
#         3x_1 + x_2 - 4x_3 &= 7.
#     \end{array}$
# ````
# 
# - **Cramer's rule:** $x_i = \dfrac{\det(A_i)}{\det(A)}$ where $A_i$ is a matrix obtained by replacing column $i$ of $A$ with $\mathbf{b}$
# 
# 
# ````{admonition} Example 2.3
# :class: seealso
# :name: cramers-rule-example
# 
# Solve the following systems of linear equations using Cramer's rule
# 
# &emsp; (i) &emsp; $\begin{array}{rl}
#     3x_1 - 2x_2 &= -4, \\
#     x_1 - 3x_2 &= 1.
# \end{array}$
# &emsp; &emsp; (ii) &emsp; $\begin{array}{rl}
#     -2x_1 - 3x_2 - x_3 &= -5, \\
#     -4x_1 + 4x_2 + 3x_3 &= -20, \\
#     -3x_1 &= -12.
# \end{array}$
# ````
# 
# - **Gaussian elimination:** use elementary row operations to reduce to row echelon form
# 
# ````{admonition} Example 2.4
# :class: seealso
# :name: ge-example
# 
# Use Gaussian-elimination to solve the following systems of linear equations:
# 
# &emsp; (i) &emsp; $\begin{array}{rl}
#     x_1 + 2x_2 &= 7, \\ 
#     3x_1 - 4x_2 &= 1.
#     \end{array}$
# &emsp; &emsp; (ii) &emsp; $\begin{array}{rl}
#     x_1 + x_3 &= 3, \\ 
#     -2x_1 + x_2 + 3x_3 &= 3, \\
#     -x_1 + 2x_2 + 4x_3 &= 5.
#     \end{array}$
# 
# ````
# 
# - **Partial pivoting:** swap the pivot row to ensure the pivot element has the largest absolute value of the elements in the column beneath it 
# 
# ````{admonition} Example 2.5
# :class: seealso
# :name: partial-pivoting-example
# 
# Solve the system of linear equations using Gaussian elimination with partial pivoting. 
# 
# \begin{align*}
#     \begin{array}{rcl}
#         x_1 - x_2 + 3x_3 &=& 13, \\
#         4x_1 - 2x_2 + x_3 &=& 15, \\
#         -3x_1 - x_2 + 4x_3 &=& 8.
#     \end{array}
# \end{align*}
# ````
# 
# - **Gauss-Jordan elimination:** use elementary row operations to row reduce to reduced row echelon form
# 
# ````{admonition} Example 2.6
# :class: seealso
# :name: gje-example
# 
# Use Gauss-Jordan elimination to solve the following system of linear equations
# 
# \begin{align*}
#     3x_1 + x_2 - 2 x_3 &= 1, \\
#     x_1 - x_2 + 2x_3 &= 3, \\
#     2x_1 - 3x_2 + 7x_3 &= 4.
# \end{align*}
# ````
# 
# - **Calculating an inverse matrix using Gauss-Jordan elimination:** row reduce $[A\mid I]$ to reduced row echelon form and extract the right-hand matrix
# 
# ````{admonition} Example 2.7
# :class: seealso
# :name: gje-inverse-example
# 
# Use Gauss-Jordan elimination to calculate the inverse of 
# \begin{align*}
#     A = \begin{pmatrix}1 & 0 & 2 \\ 2 & -1 & 3 \\ 1 & 4 & 4 \end{pmatrix}.
# \end{align*}
# ````
# - **Consistent, inconsistent and indeterminate sytems:** a system of consistent if $\operatorname{rank}(A) = \operatorname{rank}([A \mid \mathbf{b}])$, inconsistent if $\operatorname{rank}(A) < \operatorname{rank}(A \mid \mathbf{b})$ and indeterminate if $\operatorname{rank}(A) < \text{the number of unknowns}$
# 
# ````{admonition} Example 2.8
# :class: seealso
# :name: rank-example
# 
# Determine the rank of the coefficient matrix and the augmented matrix for the following systems of linear equations and classify them as either consistent, inconsistent or indeterminate systems.
#     
# &emsp; (i) &emsp; $\begin{array}{rcl}
#     3x_1 + x_2 - 2x_3 &=& 1, \\
#     x_1 - x_2 + 2x_3 &=& 3, \\
#     2x_1 - 3x_2 + 7x_3 &=& 4.
# \end{array}$
# &emsp; &emsp; (ii) &emsp; $\begin{array}{rcl}
#     x_1 - x_2 + 2x_3 &=& 3, \\
#     2x_1 - 3x_2 + 7x_3 &=& 4, \\
#     -x_1 + 3x_2 - 8x_3 &=& 1.
# \end{array}$
# &emsp; &emsp; (iii) &emsp;  $\begin{array}{rcl}
#     x_1 + x_2 - 2x_3 &=& 1, \\
#     2x_1 - x_2 + x_3 &=& 9, \\
#     x_1 + 4x_2 - 7x_3 &=& 2.
# \end{array}$
# 
# ````
# 
# - **Homogeneous systems:** $A \mathbf{x} = \mathbf{0}$
# 
# `````{admonition} Example 2.9
# :class: seealso
# :name: homogeneous-systems-example
# 
# Solve the following homogeneous system of linear equations using Gauss-Jordan elimination
# 
# \begin{align*}
#     x_1 + 2x_3 - x_5 &= 0, \\
#     2x_1 + 4x_3 - 2x_4 + 4x_5 &= 0, \\
#     x_2 + x_3 +2x_4 &= 0.
# \end{align*}
# `````
# 
# 
# <span style="font-size:20pt;">Exercises</span>
# 
# `````{admonition} Exercise 2.1
# :class: note
# :name: ex2.1
# 
# Solve the following linear system of equations using the inverse of the coefficient matrix.
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 4
# (a) 
# \begin{align*}
#      - 4 x_{1} + 2 x_{2} &= -22, \\
#      3 x_{1} + 4 x_{2} &= 11.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# (b)
# \begin{align*}
#      - 4 x_{1} + 2 x_{2} &= 6, \\
#      - x_{1} - 3 x_{2} &= -2.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# (c) 
# \begin{align*}
#      - 4 x_{1} - 4 x_{2} - 2 x_{3} &= 16, \\
#      3 x_{1} + 4 x_{3} &= -8, \\
#      x_{1} &= 0.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# (d)
# \begin{align*}
#      4 x_{1} - 4 x_{3} &= 8, \\
#      4 x_{1} -  x_{2} +  x_{3} &= -4, \\
#      3 x_{1} +  x_{2} + 2 x_{3} &= -12.
# \end{align*}
# ```
# ````
# `````
# 
# `````{admonition} Exercise 2.2
# :class: note
# :name: ex2.2
# 
# Solve the following linear system of equations using Cramer's rule.
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 4
# (a) &emsp; 
# \begin{align*}
#      x_{1} + 4 x_{2} &= -20, \\
#      - 4 x_{1} +  x_{2} &= -5.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# (b) &emsp; 
# \begin{align*}
#      x_{1} +  x_{2} &= 4, \\
#      4 x_{2} &= 12.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# (c) &emsp; 
# \begin{align*}
#      3 x_{1} - 4 x_{2} - 4 x_{3} &= 21, \\
#      - 2 x_{1} -  x_{2} -  x_{3} &= 8, \\
#      4 x_{1} -  x_{2} + 3 x_{3} &= -14.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# (d) &emsp;
# \begin{align*}
#      4 x_{1} + 4 x_{2} +  x_{3} &= 5, \\
#      - 2 x_{1} +  x_{2} +  x_{3} &= -1, \\
#      - 5 x_{1} - 4 x_{2} + 2 x_{3} &= -14.
# \end{align*}
# ```
# `````
# 
# `````{admonition} Exercise 2.3
# :class: note
# :name: ex2.3
# 
# Solve the following linear system of equations using Gaussian elimination.
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 4
# 
# (a) &emsp; 
# \begin{align*}
#      - x_{1} + 3 x_{2} &= -2, \\
#      - 2 x_{1} +  x_{2} &= 1.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (b) &emsp; 
# \begin{align*}
#      3 x_{1} +  x_{2} + 2 x_{3} &= 11, \\
#      4 x_{1} - 4 x_{3} &= -4, \\
#      4 x_{1} - 2 x_{2} +  x_{3} &= 13.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (c) &emsp; 
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -17, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -14, \\
#      3 x_{1} -  x_{2} + 4 x_{3} &= -13.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (d) &emsp; 
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -26, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -19, \\
#      3 x_{1} -  x_{2} - 4 x_{3} &= -20.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (e) &emsp; 
# \begin{align*}
#      3 x_{1} - 5 x_{2} - 4 x_{3} -  x_{4} &= 28, \\
#      - 4 x_{2} + 3 x_{3} - 4 x_{4} &= 41, \\
#      2 x_{1} + 3 x_{2} + 3 x_{3} - 3 x_{4} &= 11, \\
#      - 2 x_{1} + 2 x_{2} - 5 x_{3} - 4 x_{4} &= -21.
# \end{align*}
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (f) &emsp; 
# \begin{align*}
#      2 x_{1} - 3 x_{2} - 3 x_{3} + 4 x_{4} &= -1, \\
#      4 x_{1} - 5 x_{2} +  x_{3} - 5 x_{4} &= 42, \\
#      3 x_{1} + 3 x_{2} -  x_{3} - 5 x_{4} &= 20, \\
#      x_{1} +  x_{3} + 3 x_{4} &= -4.
# \end{align*}
# ```
# `````
# 
# `````{admonition} Exercise 2.4
# :class: note
# :name: ex2.4
# 
# Solve the linear system of equations from [exercise 2.3](ex2.3) using Gaussian elimination with partial pivoting.
# `````
# 
# `````{admonition} Exercise 2.5
# :class: note
# :name: ex2.5
# 
# Solve the linear system of equations from [exercise 2.3](ex2.3) using Gauss-Jordan elimination.
# `````
# 
# `````{admonition} Exercise 2.6
# :class: note
# :name: ex2.6
# 
# Use Gauss-Jordan elimination to calculate the inverse of the coefficient matrices from [exercise 2.1](ex2.1).
# `````
# 
# `````{admonition} Exercise 2.7
# :class: note
# :name: ex2.7
# 
# For the following linear systems of equations, determine the rank of the coefficient matrix and the augmented matrix and classify the system is consistent, inconsistent or indeterminate and calculate the solution (if possible).
# 
# ````{grid}
# 
# ```{grid-item}
# (a)
# \begin{align*}
#      x_{1} -  x_{2} + 2 x_{3} &= 2, \\
#      2 x_{1} +  x_{2} + 4 x_{3} &= 7, \\
#      4 x_{1} +  x_{2} +  x_{3} &= 4.
# \end{align*}
# ```
# 
# ```{grid-item}
# (b)
# \begin{align*}
#      x_{1} -  x_{2} + 2 x_{3} &= 3, \\
#      2 x_{1} - 3 x_{2} + 7 x_{3} &= 4, \\
#      - x_{1} + 3 x_{2} - 8 x_{3} &= 1.
# \end{align*}
# ```
# 
# ```{grid-item}
# 
# (c)
# \begin{align*}
#      x_{1} +  x_{2} - 2 x_{3} &= 1, \\
#      2 x_{1} -  x_{2} +  x_{3} &= 9, \\
#      x_{1} + 4 x_{2} - 7 x_{3} &= 2.
# \end{align*}
# ```
# `````
# 
# `````{admonition} Exercise 2.8
# :class: note
# :name: ex2.8
# 
# Solve the following systems of homogeneous linear equations.
# 
# ````{grid}
# 
# ```{grid-item}
# (a)
# \begin{align*}
#      3 x_{1} + 2 x_{2} + 7 x_{3} &= 0, \\
#      4 x_{1} - 3 x_{2} - 2 x_{3} &= 0, \\
#      5 x_{1} + 9 x_{2} + 23 x_{3} &= 0.
# \end{align*}
# ```
# 
# ```{grid-item}
# (b)
# \begin{align*}
#      2 x_{1} + 3 x_{2} -  x_{3} &= 0, \\
#      x_{1} -  x_{2} - 2 x_{3} &= 0, \\
#      3 x_{1} +  x_{2} + 3 x_{3} &= 0.
# \end{align*}
# ```
# `````
# 
# 
# `````{admonition} Exercise 2.9
# :class: note
# :name: ex2.9 
#     
# Determine the values of $k$ for which the following system of linear equations
# 
# \begin{align*}
#     x_1 + x_2 + 3x_3 &= 1, \\
#     4x_1 + 3x_2 + kx_3 &= 2, \\
#     2x_1 + x_2 + 2x_3 &= 3,
# \end{align*}
# 
# has:
# 
# (a) a unique solution;
# &emsp; (b) a non-trivial solution
# `````
# 
# ``````
