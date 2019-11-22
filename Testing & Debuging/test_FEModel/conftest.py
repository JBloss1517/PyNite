# -*- coding: utf-8 -*-
"""
@author: Jeff Bloss
"""

import pytest
from PyNite import FEModel3D


@pytest.fixture
def length():
    # 14ft = 168in
    return 14 * 12


### Fixtures of different configuration

## 2D Beams Configuration
@pytest.fixture
def simple_beam(length):
    SimpleBeam = FEModel3D()

    # Add nodes (14 ft = 168 in apart)
    SimpleBeam.AddNode("N1", 0, 0, 0)
    SimpleBeam.AddNode("N2", length, 0, 0)

    # Add a beam with the following properties:
    # E = 29000 ksi, G = 11400 ksi, Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    SimpleBeam.AddMember("M1", "N1", "N2", E=29000, G=11400, Iy=100, Iz=150, J=250, A=20)

    # Supports: Pin, Pin
    SimpleBeam.DefineSupport("N1", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)
    SimpleBeam.DefineSupport("N2", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)

    return SimpleBeam


@pytest.fixture
def pin_fixed_beam(length):
    PinFixBeam = FEModel3D()

    # Add nodes (14 ft = 168 in apart)
    PinFixBeam.AddNode("N1", 0, 0, 0)
    PinFixBeam.AddNode("N2", length, 0, 0)

    # Add a beam with the following properties:
    # E = 29000 ksi, G = 11400 ksi, Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    PinFixBeam.AddMember("M1", "N1", "N2", E=29000, G=11400, Iy=100, Iz=150, J=250, A=20)

    # Supports: Pin, Fixed
    PinFixBeam.DefineSupport("N1", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)
    PinFixBeam.DefineSupport("N2", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True, SupportRZ=True)

    return PinFixBeam


@pytest.fixture
def two_span_beam(length):
    TwoSpanBeam = FEModel3D()

    # Add nodes (14 ft = 168 in apart)
    TwoSpanBeam.AddNode("N1", 0, 0, 0)
    TwoSpanBeam.AddNode("N2", length, 0, 0)
    TwoSpanBeam.AddNode("N3", length * 2, 0, 0)

    # Add a beam with the following properties:
    # E = 29000 ksi, G = 11400 ksi, Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    TwoSpanBeam.AddMember("M1", "N1", "N2", E=29000, G=11400, Iy=100, Iz=150, J=250, A=20)
    TwoSpanBeam.AddMember("M2", "N2", "N3", E=29000, G=11400, Iy=100, Iz=150, J=250, A=20)

    # Supports: Pin, Roller, Roller
    TwoSpanBeam.DefineSupport("N1", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)
    TwoSpanBeam.DefineSupport("N2", SupportDX=False, SupportDY=True, SupportDZ=True, SupportRX=True)
    TwoSpanBeam.DefineSupport("N3", SupportDX=False, SupportDY=True, SupportDZ=True, SupportRX=True)

    return TwoSpanBeam


@pytest.fixture
def three_span_beam(length):
    ThreeSpanBeam = FEModel3D()

    # Add nodes (14 ft = 168 in apart)
    ThreeSpanBeam.AddNode("N1", 0, 0, 0)
    ThreeSpanBeam.AddNode("N2", length, 0, 0)
    ThreeSpanBeam.AddNode("N3", length * 2, 0, 0)
    ThreeSpanBeam.AddNode("N4", length * 3, 0, 0)

    # Add a beam with the following properties:
    # E = 29000 ksi, G = 11400 ksi, Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    ThreeSpanBeam.AddMember("M1", "N1", "N2", E=29000, G=11400, Iy=100, Iz=150, J=250, A=20)
    ThreeSpanBeam.AddMember("M2", "N2", "N3", E=29000, G=11400, Iy=100, Iz=150, J=250, A=20)
    ThreeSpanBeam.AddMember("M3", "N3", "N4", E=29000, G=11400, Iy=100, Iz=150, J=250, A=20)

    # Supports: Pin, Roller, Roller, Roller
    ThreeSpanBeam.DefineSupport("N1", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)
    ThreeSpanBeam.DefineSupport("N2", SupportDX=False, SupportDY=True, SupportDZ=True, SupportRX=True)
    ThreeSpanBeam.DefineSupport("N3", SupportDX=False, SupportDY=True, SupportDZ=True, SupportRX=True)
    ThreeSpanBeam.DefineSupport("N4", SupportDX=False, SupportDY=True, SupportDZ=True, SupportRX=True)

    return ThreeSpanBeam


## 2D Frames Configuration

@pytest.fixture
def two_member_frame_1():
    # Two member frame with one beam and one column. Column is on right.
    # Frame is taken from Example 16.1 in textbook "Structural Analysis" by R.C. Hibbeler (8th Ed.)
    Frame = FEModel3D()

    Frame.AddNode("N1", X=0, Y=20 * 12, Z=0)
    Frame.AddNode("N2", X=20 * 12, Y=20 * 12, Z=0)
    Frame.AddNode("N3", X=20 * 12, Y=0, Z=0)

    Frame.AddMember("M1", "N1", "N2", E=29000, G=11400, Iy=150, Iz=500, J=2, A=10)
    Frame.AddMember("M2", "N2", "N3", E=29000, G=11400, Iy=150, Iz=500, J=2, A=10)

    # N1: Roller, N3: Fixed
    Frame.DefineSupport("N1", SupportDX=False, SupportDY=True, SupportDZ=True, SupportRX=True)
    Frame.DefineSupport("N3", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True, SupportRZ=True)

    return Frame


@pytest.fixture
def two_member_frame_2():
    # Two member frame with sloping beam up to flat beam. Flat beam is on right.
    # Frame is taken from Example 16.2 in textbook "Structural Analysis" by R.C. Hibbeler (8th Ed.)
    Frame = FEModel3D()

    Frame.AddNode("N1", X=0, Y=0, Z=0)
    Frame.AddNode("N2", X=20 * 12, Y=15 * 12, Z=0)
    Frame.AddNode("N3", X=20 * 12 + 20 * 12, Y=15 * 12, Z=0)

    Frame.AddMember("M1", "N1", "N2", E=29000, G=11400, Iy=150, Iz=600, J=2, A=12)
    Frame.AddMember("M2", "N2", "N3", E=29000, G=11400, Iy=150, Iz=600, J=2, A=12)

    # N1: Fixed, N3: Fixed
    Frame.DefineSupport("N1", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True, SupportRZ=True)
    Frame.DefineSupport("N3", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True, SupportRZ=True)

    return Frame


@pytest.fixture
def three_member_frame_1():
    MomentFrame = FEModel3D()

    # Add nodes (frame is 15 ft wide x 12 ft tall)
    MomentFrame.AddNode("N1", 0, 0, 0)
    MomentFrame.AddNode("N2", 0, 12 * 12, 0)
    MomentFrame.AddNode("N3", 15 * 12, 12 * 12, 0)
    MomentFrame.AddNode("N4", 15 * 12, 0 * 12, 0)

    # Add columns with the following properties:
    # AISC W8x31
    # E = 29000 ksi, G = 11154 ksi, Iy = 37.1 in^4, Iz = 110 in^4, J = 0.536 in^4, A = 9.13 in^2
    MomentFrame.AddMember("M1", "N1", "N2", E=29000, G=11400, Iy=37.1, Iz=110, J=0.536, A=9.13)
    MomentFrame.AddMember("M2", "N4", "N3", E=29000, G=11400, Iy=37.1, Iz=110, J=0.536, A=9.13)
    MomentFrame.AddMember("M3", "N2", "N3", E=29000, G=11400, Iy=37.1, Iz=110, J=0.536, A=9.13)

    # Provide fixed supports at the bases of the columns
    MomentFrame.DefineSupport("N1", True, True, True, True, True, True)
    MomentFrame.DefineSupport("N4", True, True, True, True, True, True)

    return MomentFrame


### 2D Beam fixtures with different load configurations

@pytest.fixture
def simple_beam_pt_load_1(simple_beam, length):
    # Add a point load of 5 kips at the midspan of the beam
    _simple_beam = simple_beam
    _simple_beam.AddMemberPtLoad("M1", "Fy", 5, length / 2)
    _simple_beam.Analyze()

    return _simple_beam


@pytest.fixture
def simple_beam_pt_load_2(simple_beam):
    # Add a point load of 5 kips at 3ft from left edge of beam
    _simple_beam = simple_beam
    _simple_beam.AddMemberPtLoad("M1", "Fy", 5, 3 * 12)
    _simple_beam.Analyze()

    return _simple_beam


@pytest.fixture
def simple_beam_pt_load_3(simple_beam):
    # Add a point load of 5 kips at "i" node using MemberPtLoad function
    _simple_beam = simple_beam
    _simple_beam.AddMemberPtLoad("M1", "Fy", 5, 0 * 12)
    _simple_beam.Analyze()

    return _simple_beam


@pytest.fixture
def simple_beam_dist_load_1(simple_beam, length):
    _simple_beam = simple_beam
    # Add a distributed load of 1 kips per ft (0.083 k/in) along the length of beam
    _simple_beam.AddMemberDistLoad("M1", "Fy", 1 / 12, 1 / 12, 0, length)

    # Analyze the beam
    _simple_beam.Analyze()

    return _simple_beam


@pytest.fixture
def simple_beam_dist_load_2(simple_beam, length):
    _simple_beam = simple_beam
    # Add a tapered distributed load of 0 kips per ft at 0ft and 1k/ft (0.083k/in) at end of beam
    _simple_beam.AddMemberDistLoad("M1", "Fy", 0.0, 1 / 12, 0, length)

    # Analyze the beam
    _simple_beam.Analyze()

    return _simple_beam


@pytest.fixture
def simple_beam_dist_load_3(simple_beam, length):
    # Add a partially distributed load of 1k/ft at 6ft and 1k/ft (0.083k/in) at end of beam
    _simple_beam = simple_beam
    _simple_beam.AddMemberDistLoad("M1", "Fy", 1 / 12, 1 / 12, 6 * 12, length)

    # Analyze the beam
    _simple_beam.Analyze()

    return _simple_beam


@pytest.fixture
def pin_fix_beam_pt_load_1(pin_fixed_beam, length):
    # Add a point load of 5 kips at the midspan of the beam
    _pin_fixed_beam = pin_fixed_beam
    _pin_fixed_beam.AddMemberPtLoad("M1", "Fy", 5, length / 2)
    _pin_fixed_beam.Analyze()

    return _pin_fixed_beam


@pytest.fixture
def pin_fix_beam_pt_load_2(pin_fixed_beam):
    # Add a point load of 5 kips at 3ft from left edge of beam
    _pin_fixed_beam = pin_fixed_beam
    _pin_fixed_beam.AddMemberPtLoad("M1", "Fy", 5, 3 * 12)
    _pin_fixed_beam.Analyze()

    return _pin_fixed_beam


@pytest.fixture
def pin_fix_beam_pt_load_3(pin_fixed_beam):
    # Add a point load of 5 kips at "i" node using MemberPtLoad function
    _pin_fixed_beam = pin_fixed_beam
    _pin_fixed_beam.AddMemberPtLoad("M1", "Fy", 5, 0 * 12)
    _pin_fixed_beam.Analyze()

    return _pin_fixed_beam


@pytest.fixture
def pin_fix_beam_dist_load_1(pin_fixed_beam, length):
    # Add a distributed load of 1 kips per ft (0.083 k/in) along the length of beam
    _pin_fixed_beam = pin_fixed_beam
    _pin_fixed_beam.AddMemberDistLoad("M1", "Fy", 1 / 12, 1 / 12, 0, length)

    # Analyze the beam
    _pin_fixed_beam.Analyze()

    return _pin_fixed_beam


@pytest.fixture
def two_span_beam_pt_load_1(two_span_beam, length):
    # Add a pt load of 5 kips at mid span of span 1 ("M1")
    _two_span_beam = two_span_beam
    _two_span_beam.AddMemberPtLoad("M1", "Fy", 5, length / 2)
    # Analyze the beam
    _two_span_beam.Analyze()

    return _two_span_beam


@pytest.fixture
def two_span_beam_pt_load_2(two_span_beam, length):
    # Add a pt load of 5 kips at 3ft from left end of span 1 ("M1")
    _two_span_beam = two_span_beam
    _two_span_beam.AddMemberPtLoad("M1", "Fy", 5, 3 * 12)
    # Analyze the beam
    _two_span_beam.Analyze()

    return _two_span_beam


@pytest.fixture
def two_span_beam_dist_load_1(two_span_beam, length):
    # Add a distributed load of 1 kips per ft (0.083 k/in) along the left span ("M1")
    _two_span_beam = two_span_beam
    _two_span_beam.AddMemberDistLoad("M1", "Fy", 1 / 12, 1 / 12, 0, length)
    # Analyze the beam
    _two_span_beam.Analyze()

    return _two_span_beam


@pytest.fixture
def three_span_beam_dist_load_1(three_span_beam, length):
    # Add a distributed load of 1 kips per ft (0.083 k/in) along all spans
    _three_span_beam = three_span_beam
    _three_span_beam.AddMemberDistLoad("M1", "Fy", 1 / 12, 1 / 12, 0, length)
    _three_span_beam.AddMemberDistLoad("M2", "Fy", 1 / 12, 1 / 12, 0, length)
    _three_span_beam.AddMemberDistLoad("M3", "Fy", 1 / 12, 1 / 12, 0, length)
    # Analyze the beam
    _three_span_beam.Analyze()

    return _three_span_beam


@pytest.fixture
def three_span_beam_dist_load_2(three_span_beam, length):
    # Add a distributed load of 1 kips per ft (0.083 k/in) along spans M1 and M2 only
    _three_span_beam = three_span_beam
    _three_span_beam.AddMemberDistLoad("M1", "Fy", 1 / 12, 1 / 12, 0, length)
    _three_span_beam.AddMemberDistLoad("M2", "Fy", 1 / 12, 1 / 12, 0, length)

    # Analyze the beam
    _three_span_beam.Analyze()

    return _three_span_beam


@pytest.fixture
def three_span_beam_dist_load_3(three_span_beam, length):
    # Add a distributed load of 1 kips per ft (0.083 k/in) along spans M1 and M3 only
    _three_span_beam = three_span_beam
    _three_span_beam.AddMemberDistLoad("M1", "Fy", 1 / 12, 1 / 12, 0, length)
    _three_span_beam.AddMemberDistLoad("M3", "Fy", 1 / 12, 1 / 12, 0, length)

    # Analyze the beam
    _three_span_beam.Analyze()

    return _three_span_beam


## 2D frame fixtures with different load configurations

@pytest.fixture
def two_member_frame_1_lat_load(two_member_frame_1):
    # Add a 5 kip point load at top of column
    _two_member_frame = two_member_frame_1
    _two_member_frame.AddNodeLoad("N2", "FX", 5.0)

    # Analyze the frame
    _two_member_frame.Analyze()

    return _two_member_frame


@pytest.fixture
def two_member_frame_2_dist_load(two_member_frame_2):
    # Add a distributed load of 3 kips per ft (0.25 k/in) along horizontal beam only
    _two_member_frame = two_member_frame_2
    _two_member_frame.AddMemberDistLoad("M2", "Fy", 3 / 12, 3 / 12, 0, 20 * 12)

    # Analyze the frame
    _two_member_frame.Analyze()

    return _two_member_frame


@pytest.fixture
def three_member_frame_1_joint_load_1(three_member_frame_1):
    # Add a nodal lateral load of 50 kips at the left side of the frame
    _three_member_frame_1 = three_member_frame_1
    _three_member_frame_1.AddNodeLoad("N2", "FX", 50)

    # Analyze the frame
    _three_member_frame_1.Analyze()

    return _three_member_frame_1


@pytest.fixture
def three_member_frame_1_joint_load_2(three_member_frame_1):
    # Add a nodal lateral load of 50 kips at the left side of the frame
    # Adds axial load of 25 kips at top of each column
    _three_member_frame_1 = three_member_frame_1
    _three_member_frame_1.AddNodeLoad("N2", "FX", 50)
    _three_member_frame_1.AddNodeLoad("N2", "FY", -25)
    _three_member_frame_1.AddNodeLoad("N3", "FY", -25)

    # Analyze the frame
    _three_member_frame_1.Analyze()

    return _three_member_frame_1


@pytest.fixture
def three_member_frame_1_joint_load_3(three_member_frame_1):
    # Add a nodal moment of -1250 kip-in at the top left side of the frame
    _three_member_frame_1 = three_member_frame_1
    _three_member_frame_1.AddNodeLoad("N2", "MZ", -1250)

    # Analyze the frame
    _three_member_frame_1.Analyze()

    return _three_member_frame_1
