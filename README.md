<center> ## Michelle Athay and Megan Kenny's Computational Physics Final Project

Here we solve Stoke's 2nd problem: diffusion of heat through a solid object. Specifically, we study how the temperature inside a rotating asteroid changes as it receives heat from the Sun. The simplest equation to describe this problem is the 1D diffusion equation

## $\frac{\partial T}{\partial t} = \kappa \frac{\partial^{2} T}{\partial z^{2}} $,

where $\kappa$ is the diffusion coefficient, describing how quickly the heat transfer takes place. The temperature at the surface can be described as $ T(t, 0) = T_{0}cos(\omega t)$ and appropriate constants $\omega$ and $\kappa$ as well as appropriate boundary conditions can be chosen. Asteroids typically rotate with perdiods between four hours and 24 hours and have diameters ranging from 10m to 500km! We explore different parameter values based on known quantities (or ranges of quantities) but in some cases have to make  guesses for parameters for which we could not find data. 
  
This one-dimensional heat equation is analytically solvable, so we can compare our numerical solutions to analytic ones, which is our primary testing mechanism of our numerical solution. Here is an example of what the diffusion looks like as solved by our numerical algorithm
  
![image](https://user-images.githubusercontent.com/70778637/166007559-bdb98aab-229a-4e19-9c44-7cb6c411be21.png)

for the following parameter values:
  
L (diameter) = 50 m, total time = 50,000 s, incoming temperature = 1 K, $\kappa$ (diffusion coefficient) = 1.5 m$^{2}$/s, and omega (rotation rate) = 5e-4 Hz.
  
We have added an additional term to the simple (1D) diffusion equation- a radiative loss term- to explore more interesting physics: what happens when the heat can leak out the asteroid. The modified heat/diffusion equation is now no longer analytically solvable, so we rely on thenumerical scheme to illuminate what's going on! 
  
  
  
>>>>>>> 4befde755f0aafd055392f96243b22a5c57ebd5d
