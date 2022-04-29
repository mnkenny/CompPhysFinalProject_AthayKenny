## <center> Michelle Athay and Megan Kenny's Computational Physics Final Project


  Here we solve Stoke's 2nd problem: diffusion of heat through a solid object. Specifically, we study how the temperature inside a rotating asteroid changes as it receives heat from the Sun. The simplest equation to describe this problem is the 1D diffusion equation

  
![Screen Shot 2022-04-29 at 1 02 51 PM](https://user-images.githubusercontent.com/70778637/166009685-9d6fa15b-c445-4053-821b-a31024d33d66.png)

Asteroids typically rotate with perdiods between four hours and 24 hours and have diameters ranging from 10m to 500km! We explore different parameter values based on known quantities (or ranges of quantities) but in some cases have to make  guesses for parameters for which we could not find data. 
  
This one-dimensional heat equation is analytically solvable, so we can compare our numerical solutions to analytic ones, which is our primary testing mechanism of our numerical solution. Here is an example of what the diffusion looks like as solved by our numerical algorithm
  
![image](https://user-images.githubusercontent.com/70778637/166007559-bdb98aab-229a-4e19-9c44-7cb6c411be21.png)

for the following parameter values:
  
L (diameter) = 50 m, total time = 50,000 s, incoming temperature = 1 K, &kappa (diffusion coefficient) = 1.5 m^2/s, and <img src="https://render.githubusercontent.com/render/math?math=\omega"> (rotation rate) = 5e-4 Hz.
  
We have added an additional term to the simple (1D) diffusion equation- a radiative loss term- to explore more interesting physics: what happens when the heat can leak out the asteroid. The modified heat/diffusion equation is now no longer analytically solvable, so we rely on thenumerical scheme to illuminate what's going on! 
  
  
  

