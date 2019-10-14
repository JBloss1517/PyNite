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


@pytest.fixture
def simple_beam(length):
    SimpleBeam = FEModel3D()

    # Add nodes (14 ft = 168 in apart)
    SimpleBeam.AddNode("N1", 0, 0, 0)
    SimpleBeam.AddNode("N2", length, 0, 0)

    # Add a beam with the following properties:
    # E = 29000 ksi, G = 11400 ksi, Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    SimpleBeam.AddMember("M1", "N1", "N2", 29000, 11400, 100, 150, 250, 20)

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
    PinFixBeam.AddMember("M1", "N1", "N2", 29000, 11400, 100, 150, 250, 20)

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
    TwoSpanBeam.AddMember("M1", "N1", "N2", 29000, 11400, 100, 150, 250, 20)
    TwoSpanBeam.AddMember("M2", "N2", "N3", 29000, 11400, 100, 150, 250, 20)

    # Supports: Pin, Pin, Pin
    TwoSpanBeam.DefineSupport("N1", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)
    TwoSpanBeam.DefineSupport("N2", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)
    TwoSpanBeam.DefineSupport("N3", SupportDX=True, SupportDY=True, SupportDZ=True, SupportRX=True)

    return TwoSpanBeam


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
