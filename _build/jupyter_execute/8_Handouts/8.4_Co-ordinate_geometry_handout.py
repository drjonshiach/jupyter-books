#!/usr/bin/env python
# coding: utf-8

# # Co-ordinate Geometry
# 
# ``````{div} full-width
# 
# <span style="font-size:20pt;">Examples</span>
# 
# - **Vector equation of a line:** $Q = P + t\mathbf{d}$ where $P$ and $Q$ are points on the line, $\mathbf{d}$ is the direction of the line and $t\in \mathbb{R}$ is a parameter
# 
# `````{admonition} Example 4.1
# :class: seealso
# :name: line-vector-equation-example
# 
# Given a point $P=(1,0,2,1,4)$ and a direction vector $\mathbf{d} = (1,-1,0,-1,1)$ in $\mathbb{R}^5,$ find the equation of the line $\ell$ which goes through $P$ in the direction of $\mathbf{d}$.
# 
# `````
# 
# - **Intersection of two lines:** the two lines $\ell_1: P_1 + t_1\mathbf{d}_1$ and $\ell_2: P_2 + t_2\mathbf{d}_2$ intersect  if there exists values of $t_1$ and $t_2$ such that $P_1 + t_1 \mathbf{d}_1 = P_2 + t_2 \mathbf{d}_2$.
# 
# ````{admonition} Example 4.2
# :class: seealso
# :name: line-line-intersection-example
# 
# Three lines in $\mathbb{R}^3$ are defined as $\ell_1: (1 + t, -3 + 2t, t)$, $\ell_2: (6 - t, -5 - 2t, t - 1)$ and $\ell_3: (6 + 2t, -11 + 2t, -2 - t)$. Determine the points of intersection between the three lines (if possible).
# ````
# 
# - **Parallel lines:** the two lines $\ell_1: P_1 + t\mathbf{d}_1$ and $\ell_2: P_2 + t\mathbf{d}_2$ are parallel if there exsists a value $k$ such that $\mathbf{d}_1 = k\mathbf{d}_2$
# 
# `````{admonition} Example 4.3
# :class: seealso
# :name: parallel-lines-example
# 
# Let $\ell_1$ and $\ell_2$ be two lines in $\mathbb{R}^3$ be defined by $\ell_1 = \{(x,y,z) : z = x+1, y=0\}$ and $\ell_2 = \{(x,y,z) : z = -x-1, y=3\}$.
# 
# 
# &emsp; (i) &emsp; Write equations for $\ell_1$ and $\ell_2$ in vector form;
# 
# &emsp; (ii) &emsp; show that these lines are not parallel in $\mathbb{R}^3$.
# 
# `````
# 
# - **Skew lines:** if two lines do not intersect and are not parallel then they are skew.
# 
# ````{admonition} Example 4.4
# :class: seealso
# :name: skew-lines-example
# 
# Show that the lines $\ell_1$ and $\ell_2$ from [example 4.3](parallel-lines-example) are skew lines.
# 
# ````
# 
# - **Perpendicular lines:** two lines $\ell_1: P_1 + t\mathbf{d}_1$ and $\ell_2: P_2 + t\mathbf{d}_2$ are perpendicular if the angle between $\mathbf{d}_1$ and $\mathbf{d}_2$ is a right-angle.
# 
# `````{admonition} Example 4.5
# :class: seealso
# :name: perpendicular-lines-example
# 
# &emsp; (i) &emsp; Determine whether the two lines from [example 4.3](parallel-lines-example) are perpendicular.
# 
# &emsp; (ii) &emsp; Find the equation of a line $\ell_2$ which is perpendicular to $\ell_1 = \{(t,-t,1+t) : t \in \mathbb{R} \}$ at the point $P = (-1,1,0).$
# `````
# 
# - **Normal vector to a plane:** a vector perpendicular to the plane
# - **Point normal equation of a plane:** the equation of a plane which passes through the point $(x_0, y_0, z_0)$ with a normal vector $\mathbf{n}$ is $\mathbf{n} \cdot (x - x_0, y - y_0, z - z_0)$
# 
# `````{admonition} Example 4.6
# :class: seealso
# 
# A plane $p$ in $\mathbb{R}^3$ passes the three points $P_1 = (1, 0, 0)$, $P_2 = (1, 0, -1)$ and $P_3 = (2, 1, 3)$
# 
# &emsp; (i) &emsp; Find the point normal definition of the plane;
# 
# &emsp; (ii) &emsp; Do the points $P_4 = (2, 3, 1)$ and $P_5 = (3, 2, 4)$ lie on $p$?
# 
# `````
# 
# - **Intersection of planes:** Two or more planes in $\mathbb{R}^3$ can intersect at a single point, as an infinite number of points on a line, an infinite number of points on a plane or not intersect at all. 
# 
# ````{admonition} Example 4.7
# :class: seealso
# :name: intersecting-planes-example
# 
# Two non-parallel planes in $\mathbb{R}^3$ are given by $p:3x-4y+z-5 = 0$ and $r:x+ y - z -2 = 0$ respectively. Find the intersection of these two planes
# ````
# 
# - **Shortest distance between a point and a line:** the shortest distance between the point $Q$ and a line that passes through the point $P$ in the direction $\mathbf{d}$ is $|Q - R|$ where $R = P + t\mathbf{d}$ and $t = \frac{(Q - P) \cdot \mathbf{d}}{ \mathbf{d} \cdot \mathbf{d}}$
# 
# ````{admonition} Example 4.8
# :class: seealso
# :name: point-line-distance-example
# 
# Find the shortest distance between the point $Q = (2,2,2)$ and the line $\ell : (t,t-2, t+1)$.
# 
# ````
# 
# - **Shortest distance between two skew lines:** the shortest distance between two skew lines $\ell_1: P_1 + t\mathbf{d}_1$ and $\ell_2: P_2 + t\mathbf{d}_2$ is $d = (P_2 - P_1) \cdot \hat{\mathbf{n}}$ where $\mathbf{n} = \mathbf{d}_1 \times \mathbf{d}_2$.
# 
# ````{admonition} Example 4.9
# :class: seealso
# :name: line-line-distance-example
# 
# Find the shortest distance between the two lines $\ell_1 = \{(t,1+4t,3 + 2t):t\in\mathbb{R}\}$ and $\ell_2 = \{(1,1+2t,3 + 4t):t\in\mathbb{R}\}$.
# ````
# 
# <span style="font-size:20pt;">Exercises</span>
# 
# ````{admonition} Exercise 4.1
# The points $A, B, C, D$ in $\mathbb{R}^3$ have the following position vectors
# 
# \begin{align*}
#     \mathbf{a} &= \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}, &
#     \mathbf{b} &= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, &
#     \mathbf{c} &= \begin{pmatrix} 3 \\ -1 \\ 4 \end{pmatrix}, &
#     \mathbf{d} &= \begin{pmatrix} 5 \\ 2 \\ 6 \end{pmatrix}.
# \end{align*}
# 
# Find:
# 
# &emsp; (a) &emsp; the equation of the line that passes through $A$ and $B$;
# 
# &emsp; (b) &emsp; the equation of the line that passes through $C$ and $D$;
# 
# &emsp; (c) &emsp; the equation of the plane which $A$, $B$ and $C$ lie on;
# 
# &emsp; (d) &emsp; the equation of the plane which $B$, $C$ and $D$ lie on.
# 
# ````
# 
# ````{admonition} Exercise 4.2
# Find the equation of the line that passes through the point $(3, 2, 1)$ which is parallel to $2 \mathbf{i} + \mathbf{j} + 3 \mathbf{k}$.
# 
# ````
# 
# ````{admonition} Exercise 4.3
# Find the equation of the plane that passes through the point $(3, 2, 5)$ which has a normal vector $\mathbf{n} = (2, 1, 3)$.
# ````
# 
# ````{admonition} Exercise 4.4
# Two lines in $\mathbb{R}^3$ are defined by $\ell_1: (1 + 2t, -t, 1 + 3t)$ and $\ell_2: (1 + 2t, 4, 7 - t)$ respectively.
# 
# &emsp; (a) &emsp; find the intersection of the lines or show they are skew;
# 
# &emsp; (b) &emsp; find the shortest distance between the lines;
# 
# &emsp; (c) &emsp; find the distance between the point $P = (0, -1, 3)$ and $\ell_1$.
# ````
# 
# ````{admonition} Exercise 4.5
# A plane has the equation $3x - 2y + z = 10$. Identify the normal to the plane and find the co-ordinates of 2 points on the plane having $z = 2$.
# ````
# 
# ````{admonition} Exercise 4.6
# Find the point where the line $\ell:(1 + 2t, 2 + t, -1 + 4t)$ meets the plane $6x - y - 4z = 3$. 
# ````
# 
# ````{admonition} Exercise 4.7
# :class: note
# :name: ex4.7
# Consider the diagram below that shows a plane that passes through the point $\mathbf{p}$ and has normal vector $\mathbf{n}$ and the point with position $\mathbf{q}$ not on the plane. 
# 
# ```{figure} ../Images/point_plane_distance.png
# ```
# 
# Using the [geometric definition of a dot product](dot-product-definition) derive an expression for calculating the shortest distance between a point and a plane. Use your expression to find the shortest distance from the point $(2, 4, -3)$ to the plane $6x - y - 4z = 3$.
# ````
# 
# ``````
# 