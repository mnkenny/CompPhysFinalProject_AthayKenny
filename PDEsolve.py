import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.special import erfc

class pde_solver():
    """
    Class function containing various algorithms to solve the diffusion of heat through an asteroid
    
    Arguments:
    -----
    * zp: non-dimensional total length
    * dz: dimenional spatial step
    * zc:charachteristic length scae for non-dimensionalization
    * cf:cfl condition fraction --> dt = cf*(dx^2/(2*kappa))
    * tp: non-dimensional total time
    * kappa:diffusion coeffecient
    * omegap: frequency
    * T0: initial condition 
    * mu: physical characteristics constant
    * k_th: thermal conductivity 

    Contains:
    -----
    * numerical(): Solves the pde for sinusoidal boundary
    * numerical_const(): Solves the pde for constant boundary
    * numerical_plus_radiative(): Solves the pde for sinusoidal boundaries acounting for radiative loss
    * analytic(): Analytic solution for sinusoidal boundary and infinite size 
    * analytic_const(): Analytic solution for const boundary and infinite size 
    """    

    def __init__(self,zp,dz,zc,cf,tp,kappa,omegap, T0,mu,k_th):
    
        self.k_th=k_th
        self.kappa=kappa
        self.cf=cf
        self.T0=T0
        self.mu=mu      
        
        self.zc=zc        
        self.dz=dz
        self.dzp=self.dz/self.zc
        self.z=np.arange(0,zp*self.zc,self.dz)
        self.Nz = len(self.z)
        self.zp=np.linspace(0,zp,self.Nz)

        self.tc=self.zc**2/self.kappa
        self.dt=self.cf*self.dz**2/(2*self.kappa) # Define timestep to satisfy stability req't
        self.dtp=self.dt/self.tc
        self.t=np.arange(0,tp*self.tc,self.dt)
        self.Nt=len(self.t)
        self.tp=np.linspace(0,tp,self.Nt) 
        
        self.w=omegap
        self.wc=1/self.tc
        self.wp=self.w/self.wc

        self.r = self.kappa*self.dt/(self.dz**2) # Diffusion condition
        self.d=self.mu*self.kappa/self.k_th # radiative loss term
        
        print("Step size: dt = {:.2e}".format(self.dt))
        self.T_sol=None
        self.T=None
        self.T_rad=None
        self.T_const=None
        self.T_sol=None
        self.T_const_sol=None
    def numerical(self,double=True):
        """
        Function to compute, with centered finite differences, the temperature evolution in an asteroid 
        rotating in space. Boundary conditions are,
        T(t,z=0) = T0*cos(w*t).
        and
        T(t,z=z_max) = 0 -- double = False
        T(t,z=z_max) = -T0*cos(w*t) --double = True
        
        Args:
        -----
        * double: True or False, default is True. Toggle for using 1 or 2 non-zero oscillatng boundary 
        conditions

        Updates:
        -----
        * T: the temperature profiles in 1-D at every time step. T is an NtxNz array
        """  
        self.T=np.zeros((self.Nt, self.Nz))

        # Insert boundary conditionsself.T0/2-
        self.T[:,0] =self.T0*np.cos(self.w*self.t)
        if double:
            self.T[:,-1] = -self.T0*np.cos(self.w*self.t)
        for i in range(1, self.Nt):
            # Compute T at inner mesh points
            self.T[i,1:-1] =  self.T[i-1,1:-1] + self.r * (self.T[i-1,2:] - 2*self.T[i-1,1:-1] + 
                                                           self.T[i-1,:-2]) 

  

    def numerical_const(self):
        """
        Function to compute, with centered finite differences, the temperature evolution in 1-D from
        a constant heat source. Boundary conditions are,
        T(t,z=0) = T0.
        and
        T(t,z=z_max) = 0

        Args:
        -----
        None

        Updates:
        -----
        * T_const: the temperature profiles in 1-D at every time step. T_const is an NtxNz array
        """
        self.T_const=np.zeros((self.Nt, self.Nz))
        self.T_const[:,0] = self.T0
        for i in range(1, self.Nt):
            # Compute u at inner mesh points
            self.T_const[i,1:-1] =  self.T_const[i-1,1:-1] + self.r * (self.T_const[i-1,2:] - 2*self.T_const[i-1,1:-1] +
                                                                       self.T_const[i-1,:-2]) 
        
        
    def numerical_plus_radiative(self, double=True):
        """
        Function to compute the modified diffusion equation, that with a radiative loss term, describing an 
        asteroid which can lose heat at its boundary to its surroundings.

        Args:
        -----
        * double: True or False, default is True. Toggle for using 1 or 2 non-zero oscillatng boundary 
            conditions

        Updates:
        -----
        *T_rad: the temperature profiles in 1-D at every time step. T_rad is an NtxNz array
        """
        self.T_rad=np.zeros((self.Nt, self.Nz))
        str_len = 0
        
        # Insert boundary conditions
        self.T_rad[:,0] =self.T0*np.cos(self.w*self.t)
        if double:
            self.T_rad[:,-1] =-self.T0*np.cos(self.w*self.t)
            for i in range(1, self.Nt):
                
                # Compute u at inner mesh points :
                self.T_rad[i,1:-1] =  self.T_rad[i-1,1:-1] + self.r * (self.T_rad[i-1,2:] - 2*self.T_rad[i-1,1:-1] +
                                                                       self.T_rad[i-1,:-2]) 
                
                #Update boundary Temperature if source temperature is less than temp. at inner cell
                if self.T_rad[i,-1]<self.T_rad[i,-2]:
                    self.T_rad[i,-1]=self.T_rad[i,-2]-self.d*(self.T_rad[i,-2]**4-self.T_rad[i,-1]**4) 
                if self.T_rad[i,0]<self.T_rad[i,1]:
                    self.T_rad[i,0]=self.T_rad[i,1]-self.d*(self.T_rad[i,1]**4-self.T_rad[i,0]**4)
        else:
            for i in range(1, self.Nt):
                
                # Compute u at inner mesh points
                self.T_rad[i,1:-1] =  self.T_rad[i-1,1:-1] + self.r *(self.T_rad[i-1,2:] - 2*self.T_rad[i-1,1:-1] +
                                                                      self.T_rad[i-1,:-2]) 
                
                #Update boundary Temperature if source temperature is less than temp. at inner cell
                self.T_rad[i,-1]=self.T_rad[i,-2]-self.d*(self.T_rad[i,-2]**4)
 
    def analytic(self):
        """
        Function for the analytic solution to the temperature evolution in 1-D from
        an oscillating heat source. Boundary conditions are,
        T(t,z=0) = T0*cos(w*t).
        and
        T(t,z=z_max) = 0

        Args:
        -----
        None

        Updates:
        -----
        * T_sol: the analytic temperature profiles in 1-D at every time step. T_sol is an NtxNz array
        """
        from scipy import special
        t_a=self.t.reshape(self.Nt,1)
        z_a=self.z.reshape(1,self.Nz)
        self.k =np.sqrt(self.w/(2*self.kappa))
        self.T_sol=np.zeros((self.Nt, self.Nz))
        for i in range(1, self.Nt): 
            self.T_sol[i]=(np.exp(-self.k*self.z)*self.T0*np.cos(self.k*self.z-self.w*self.t[i]))
   
        
    def analytic_const(self):
        """
        Function for the analytic solution to the the temperature evolution in 1-D from
        a constant heat source. Boundary conditions are,
        T(t,z=0) = T0.
        and
        T(t,z=z_max) = 0

        Args:
        -----
        None

        Updates:
        -----
        * T_const_sol: the analytictemperature profiles in 1-D at every time step. T_const_sol is an NtxNz array
        """
        from scipy import special
        self.T_const_sol=np.zeros((self.Nt, self.Nz))
        for i in range(1, self.Nt):
            self.T_const_sol[i]=self.T0*special.erfc(self.z/(2*np.sqrt(self.kappa*self.t[i])))