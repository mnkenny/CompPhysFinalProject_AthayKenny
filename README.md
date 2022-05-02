## <center> Michelle Athay and Megan Kenny's Computational Physics Final Project


  Here we solve Stoke's 2nd problem: diffusion of heat through a solid object. Specifically, we study how the temperature inside a rotating asteroid changes as it receives heat from the Sun. The simplest equation to describe this problem is the 1D diffusion equation. This one-dimensional heat equation is analytically solvable, so we can compare our numerical solutions to analytic ones, which is our primary testing mechanism of our numerical solution. Here is an example of what the diffusion looks like as solved by our numerical algorithm for the case of a constant heat source (first plot) and a sinusoidal/oscillating heat source:
  
![image](https://user-images.githubusercontent.com/70778637/166294874-61ad4117-47a4-4f6d-abae-6b5961690ca2.png)
  
![image](https://user-images.githubusercontent.com/70778637/166294930-83f7743b-69b5-418a-9344-8d7a100dfb9c.png)

Both of these plots are in the (main) Python notebook with descriptions and explanations. There inclusion here is to give a sneak peak of what's to come!
  
Additionally, we have added another to the simple (1D) diffusion equation- a radiative loss term- to explore more interesting physics: what happens when the heat can leak out the asteroid at the boundaries. The modified heat/diffusion equation is now no longer analytically solvable, so we rely on thenumerical scheme to illuminate what's going on! 
  
### <center> Directions for exploration and evaluation:
  
  The main code is located in "PDEsolve.py". Please run the file "MAINFILE_AsteroidPDESolver.ipynb", which calls the functions in the .py file. Included in the notebook are testing, visualization of results, and descriptions/analysis of the results.

