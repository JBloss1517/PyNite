# Example of a simply supported beam with a point load.
# Units used in this example are inches, and kips

# Import `FEModel3D` from `PyNite`
from PyNite import FEModel3D

# Create a new finite element model
SimpleBeam = FEModel3D()

# Add nodes (14 ft = 168 in apart)
SimpleBeam.AddNode("N1", 0, 0, 0)
SimpleBeam.AddNode("N2", 168, 0, 0)

# Add a beam with the following properties:
# E = 29000 ksi, G = 11400 ksi, Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
SimpleBeam.AddMember("M1", "N1", "N2", 29000, 11400, 100, 150, 250, 20)

# Provide simple supports
SimpleBeam.DefineSupport("N1", True, True, True, True, False, False)
SimpleBeam.DefineSupport("N2", True, True, True, True, False, False)

# Add a point load of 5 kips at the midspan of the beam
SimpleBeam.AddMemberPtLoad("M1", "Fy", 5, 7 * 12)

# Analyze the beam
SimpleBeam.Analyze()

# Print the shear, moment, and deflection diagrams
SimpleBeam.GetMember("M1").PlotShear("Fy")
SimpleBeam.GetMember("M1").PlotMoment("Mz")
SimpleBeam.GetMember("M1").PlotDeflection("dy")

# Print reactions at each end of the beam
print("Left Support Reaction: {Rxn:.2f} kip".format(Rxn = SimpleBeam.GetNode("N1").RxnFY))
print("Right Support Reacton: {Rxn:.2f} kip".format(Rxn = SimpleBeam.GetNode("N2").RxnFY))