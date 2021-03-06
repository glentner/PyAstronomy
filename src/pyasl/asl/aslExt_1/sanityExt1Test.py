import unittest
from PyAstronomy import pyasl

class SanityOfPyaslExt1(unittest.TestCase):
  
  def setUp(self):
    pass
  
  def tearDown(self):
    pass
  
  def sanity_pizzolatoExample(self):
    """
      Example of Pizzolato 2003 relations
    """
    from PyAstronomy import pyasl
    import matplotlib.pylab as plt
    import numpy as np
    
    p = pyasl.Pizzolato2003()
    
    # Define array of rotation periods [days]
    prot = np.arange(0.2, 30, 0.1)
    
    lx = np.zeros(prot.size)
    lxlbol = np.zeros(prot.size)
    
    # B-V color of star
    bv = 0.7
    
    # Obtain ...
    for i in range(prot.size):
      # ... log10 of X-ray luminosity
      lx[i] = p.log10lxbv(bv, prot[i])[0]
      # ... and log10(Lx/Lbol)
      lxlbol[i] = p.log10lxlbolbv(bv, prot[i])[0]
    
    # Plot result
    plt.subplot(2,1,1)
    plt.plot(prot, lx, 'bp-')
    plt.subplot(2,1,2)
    plt.plot(prot, lxlbol, 'bp-')
#     plt.show()

  def sanity_pizzolato(self):
    """
      Pizzolato 2003 sanity
    """
    from PyAstronomy import pyasl
    import matplotlib.pylab as plt
    import numpy as np
    
    p = pyasl.Pizzolato2003()
    
    x = p.log10lxbv(0.87, 1.0)
    self.assertAlmostEqual(x[0], 29.9, msg="Lx saturation level for b-v=0.87 does not match.", delta=1e-7)
    self.assertAlmostEqual(x[1], 0.3, msg="Lx error for saturation level for b-v=0.87 does not match.", delta=1e-7)
    
    x = p.log10lxlbolmass(1.15, 3.0)
    self.assertAlmostEqual(x[0], -4.1694, msg="Pizzolato relation (m=1.15, pr=3.0) failed (value="+str(x[0])+").", delta=1e-4)
    
  def sanity_expCorrRN_Example1(self):
    """
      Sanity of example 1 for expCorrRN
    """
    import matplotlib.pylab as plt
    from PyAstronomy import pyasl
    
    # Generate 200 exponentially correlated Gaussian
    # random numbers with a decay time of 5
    c1 = pyasl.expCorrRN(200, 5)
    
    # Generate 200 exponentially correlated Gaussian
    # random numbers with decay time 10, mean 4, and
    # standard deviation of 2.3.
    #
    # The results are: The correlated random numbers,
    # the uncorrelated numbers used as input, and the
    # correlated coefficient (exp(-1/tau)).
    c2, g, f = pyasl.expCorrRN(200, 10, mean=4.0, std=2.3, fullOut=True)
    
    plt.subplot(2,1,1)
    plt.plot(range(200), c1, 'bp-')
    plt.subplot(2,1,2)
    plt.plot(range(200), c2, 'bp-')
    plt.plot(range(200), g, 'g.')
#     plt.show()

  def sanity_expCorrRN_Example2(self):
    """
      Sanity of example 2 for expCorrRN
    """
    import numpy as np
    import matplotlib.pylab as plt
    from PyAstronomy import pyasl
    
    # Generate n exponentially correlated Gaussian
    # random numbers with a decay time, tau
    n = 500
    tau = 5.
    c1 = pyasl.expCorrRN(n, tau)
    
    # Obtain autocorrelation function
    ac = np.correlate(c1, c1, mode="full")[n-1:]
    
    # Plot correlated random numbers and autocorrelation
    # function along with exponential model.
    x = np.arange(float(n))
    plt.subplot(2,1,1)
    plt.plot(x, c1, 'bp-')
    plt.subplot(2,1,2)
    plt.plot(x, ac, 'b.')
    plt.plot(x, np.exp(-x/tau)*ac.max(), 'r--')
  #   plt.show()
