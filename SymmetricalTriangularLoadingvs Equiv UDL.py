
#### EXAMPLE 1
"""  CASE - SIMPLY SUPPORTED BEAM: SYMMETRICAL TRIANGULAR LOADING : Equivalent UDL  = (2/3)*peakDL   Page 17"""
"""  all examples based on the book: Structural Engineering Art and Approximation by Hugh Morrison-Manchester UK"""

class EquivalentUDL():      ####CASE 1: Equivalent UDL
    ### CONNECTORS
    def __init__(self,span,UDL,youngModulus,momentOfInertia):
        self.span  = span                       ####Span in meters
        self.UDL =UDL                           ###  UDL in kN.m
        self.youngModulus = youngModulus        #### E in N/mm^2
        self.momentOfInertia = momentOfInertia  ## I in mm^4

    ### METHODOLOGY

    def MaxShearLoad(self):
        return (1/3)*self.UDL*self.span
    def MaxBendingMoment(self):
        return (1/12)*(self.UDL*self.span**2)
    def MaxDeflection(self):
        return (1e12)*(5/576)*(self.UDL*self.span**4)/(self.youngModulus*self.momentOfInertia)


class SymmetricalTriangularDL():          # CASE 2 - ACTUAL STRUCTURE
     ### CONNECTORS
    def __init__(self, span, PeakDL, youngModulus, momentOfInertia):
        self.span = span                        ####Span in meters
        self.PeakDL = PeakDL                    ### Triangular Distributed load in kN.m
        self.youngModulus = youngModulus        #### E in N/mm^2
        self.momentOfInertia = momentOfInertia  ## I in mm^4

     ### METHODOLOGY

    def MaxShearLoad(self):
       return (1/4)*self.PeakDL*self.span

    def MaxBendingMoment(self):
        return (1 / 12) * (self.PeakDL*self.span **2 )

    def MaxDeflection(self):
        return (1e12) * (1 / 120) * (self.PeakDL * self.span ** 4) / (self.youngModulus * self.momentOfInertia)


    ### OUTPUT

x =EquivalentUDL(3,4,210000,12600000)

x.span = 7.8                           ### in m.
x.UDL = 16                          ### in kN.m
print(x.MaxShearLoad())              #### in kN
print(x.MaxBendingMoment())          ### kN.m
print(x.MaxDeflection())             ### in mm


y =SymmetricalTriangularDL(3,4,210000,12600000)

y.span = 7.8                           ### in m.
y.PeakDL = 16                       ### in kN
print(y.MaxShearLoad())              #### in kN
print(y.MaxBendingMoment())          ### kN.m
print(y.MaxDeflection())             #### in mm