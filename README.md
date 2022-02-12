# Kalmanfilter

## model:
the state of the robot is 
$$
\textbf{x} = \begin{bmatrix} x \\ v \\ \end{bmatrix}
$$

to predict the next state :
$$
x(k+1) = x(k) + vT + 0.5aT^2 \\
v(k+1) = v(k) + aT
$$
can be written to:
$$
\textbf{x(k+1)} = F\textbf{x(k)}
                = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$