import pytest


## Expected Results are derived from ASCE STEEL CONSTRUCTION MANUAL 14TH ED.
@pytest.mark.parametrize("test_beam, expected", [
    (pytest.lazy_fixture("simple_beam_pt_load_1"),
     [(0.0, round(5 / 2, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(5 / 2, 2), 0.0, 0.0, 0.0, 0.0)]),
    (pytest.lazy_fixture("simple_beam_pt_load_2"),
     [(0.0, round(5 * 11 / 14, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(5 * 3 / 14, 2), 0.0, 0.0, 0.0, 0.0)]),
    (pytest.lazy_fixture("simple_beam_pt_load_3"),
     [(0.0, round(5, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(0, 2), 0.0, 0.0, 0.0, 0.0)]),

    (pytest.lazy_fixture("simple_beam_dist_load_1"),
     [(0.0, round(1 * 14 / 2, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(1 * 14 / 2, 2), 0.0, 0.0, 0.0, 0.0)]),
    (pytest.lazy_fixture("simple_beam_dist_load_2"),
     [(0.0, round(7 / 3, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(2 * 7 / 3, 2), 0.0, 0.0, 0.0, 0.0)]),
    (pytest.lazy_fixture("simple_beam_dist_load_3"),
     [(0.0, round(1 * (14 - 6) ** 2 / (2 * 14), 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round((1 * (14 - 6) / (2 * 14)) * (2 * 14 - (14 - 6)), 2), 0.0, 0.0, 0.0, 0.0)]),

    (pytest.lazy_fixture("pin_fix_beam_pt_load_1"),
     [(0.0, round(5 * 5 / 16, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(11 * 5 / 16, 2), 0.0, 0.0, 0.0, round(-(3 * 5 * 14 * 12 / 16), 2))]),
    (pytest.lazy_fixture("pin_fix_beam_pt_load_2"),
     [(0.0, round((5 * (14 - 3) ** 2 / (2 * 14 ** 3)) * (3 + 2 * 14), 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round((5 * 3 / (2 * 14 ** 3)) * (3 * 14 ** 2 - 3 ** 2), 2), 0.0, 0.0, 0.0,
       round(-((5 * 3 * 12 * ((14 - 3) * 12)) / (2 * (14 * 12) ** 2) * ((3 + 14) * 12)), 2))]),
    (pytest.lazy_fixture("pin_fix_beam_pt_load_3"),
     [(0.0, round(5, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)]),

    (pytest.lazy_fixture("pin_fix_beam_dist_load_1"),
     [(0.0, round(3 * 1 * 14 / 8, 2), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(5 * 1 * 14 / 8, 2), 0.0, 0.0, 0.0, round(-(1 / 12 * (14 * 12) ** 2 / 8)))]),
])
def test_1_span_beam_supports(test_beam, expected):
    # reactions at each end of the beam
    rxn_1_X = round(test_beam.GetNode("N1").RxnFX, 2)
    rxn_1_Y = round(test_beam.GetNode("N1").RxnFY, 2)
    rxn_1_Z = round(test_beam.GetNode("N1").RxnFZ, 2)
    rxn_1_MX = round(test_beam.GetNode("N1").RxnMX, 2)
    rxn_1_MY = round(test_beam.GetNode("N1").RxnMY, 2)
    rxn_1_MZ = round(test_beam.GetNode("N1").RxnMZ, 2)
    rxn_1 = (rxn_1_X, rxn_1_Y, rxn_1_Z, rxn_1_MX, rxn_1_MY, rxn_1_MZ)

    rxn_2_X = round(test_beam.GetNode("N2").RxnFX, 2)
    rxn_2_Y = round(test_beam.GetNode("N2").RxnFY, 2)
    rxn_2_Z = round(test_beam.GetNode("N2").RxnFZ, 2)
    rxn_2_MX = round(test_beam.GetNode("N2").RxnMX, 2)
    rxn_2_MY = round(test_beam.GetNode("N2").RxnMY, 2)
    rxn_2_MZ = round(test_beam.GetNode("N2").RxnMZ, 2)
    rxn_2 = (rxn_2_X, rxn_2_Y, rxn_2_Z, rxn_2_MX, rxn_2_MY, rxn_2_MZ)

    assert [rxn_1, rxn_2] == expected


## Expected Results are derived from ASCE STEEL CONSTRUCTION MANUAL 14TH ED.
# Accurate to only 1 decimal place
@pytest.mark.parametrize("test_beam, expected", [
    (pytest.lazy_fixture("two_span_beam_pt_load_1"),
     [(0.0, round(13 / 32 * 5, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(11 / 16 * 5, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(-3 / 32 * 5, 1), 0.0, 0.0, 0.0, 0.0)]),
    (pytest.lazy_fixture("two_span_beam_pt_load_2"),
     [(0.0, round(5 * (14 - 3) / (4 * 14 ** 3) * (4 * 14 ** 2 - 3 * (14 + 3)), 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(5 * 3 / (2 * 14 ** 3) * (2 * 14 ** 2 + (14 - 3) * (14 + 3)), 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(-(5 * 3 * (14 - 3) / (4 * 14 ** 3) * (14 + 3)), 1), 0.0, 0.0, 0.0, 0.0)]),

    (pytest.lazy_fixture("two_span_beam_dist_load_1"),
     [(0.0, round(7 / 16 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(5 / 8 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(-1 / 16 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0)]),
])
def test_2_span_beam_supports(test_beam, expected):
    # reactions at each end of the beam
    rxn_1_X = round(test_beam.GetNode("N1").RxnFX, 1)
    rxn_1_Y = round(test_beam.GetNode("N1").RxnFY, 1)
    rxn_1_Z = round(test_beam.GetNode("N1").RxnFZ, 1)
    rxn_1_MX = round(test_beam.GetNode("N1").RxnMX, 1)
    rxn_1_MY = round(test_beam.GetNode("N1").RxnMY, 1)
    rxn_1_MZ = round(test_beam.GetNode("N1").RxnMZ, 1)
    rxn_1 = (rxn_1_X, rxn_1_Y, rxn_1_Z, rxn_1_MX, rxn_1_MY, rxn_1_MZ)

    rxn_2_X = round(test_beam.GetNode("N2").RxnFX, 1)
    rxn_2_Y = round(test_beam.GetNode("N2").RxnFY, 1)
    rxn_2_Z = round(test_beam.GetNode("N2").RxnFZ, 1)
    rxn_2_MX = round(test_beam.GetNode("N2").RxnMX, 1)
    rxn_2_MY = round(test_beam.GetNode("N2").RxnMY, 1)
    rxn_2_MZ = round(test_beam.GetNode("N2").RxnMZ, 1)
    rxn_2 = (rxn_2_X, rxn_2_Y, rxn_2_Z, rxn_2_MX, rxn_2_MY, rxn_2_MZ)

    rxn_3_X = round(test_beam.GetNode("N3").RxnFX, 1)
    rxn_3_Y = round(test_beam.GetNode("N3").RxnFY, 1)
    rxn_3_Z = round(test_beam.GetNode("N3").RxnFZ, 1)
    rxn_3_MX = round(test_beam.GetNode("N3").RxnMX, 1)
    rxn_3_MY = round(test_beam.GetNode("N3").RxnMY, 1)
    rxn_3_MZ = round(test_beam.GetNode("N3").RxnMZ, 1)
    rxn_3 = (rxn_3_X, rxn_3_Y, rxn_3_Z, rxn_3_MX, rxn_3_MY, rxn_3_MZ)

    assert [rxn_1, rxn_2, rxn_3] == expected


## Expected Results are derived from ASCE STEEL CONSTRUCTION MANUAL 14TH ED.
# Accurate to only 1 decimal place
@pytest.mark.parametrize("test_beam, expected", [
    (pytest.lazy_fixture("three_span_beam_dist_load_1"),
     [(0.0, round(0.40 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(1.10 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(1.10 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(0.40 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0)]),
    (pytest.lazy_fixture("three_span_beam_dist_load_2"),
     [(0.0, round(0.383 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(1.20 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(0.45 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(-0.033 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0)]),
    (pytest.lazy_fixture("three_span_beam_dist_load_3"),
     [(0.0, round(0.450 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(0.550 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(0.550 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0),
      (0.0, round(0.450 * 1 / 12 * 14 * 12, 1), 0.0, 0.0, 0.0, 0.0)]),
])
def test_3_span_beam_supports(test_beam, expected):
    # reactions at each end of the beam
    rxn_1_X = round(test_beam.GetNode("N1").RxnFX, 1)
    rxn_1_Y = round(test_beam.GetNode("N1").RxnFY, 1)
    rxn_1_Z = round(test_beam.GetNode("N1").RxnFZ, 1)
    rxn_1_MX = round(test_beam.GetNode("N1").RxnMX, 1)
    rxn_1_MY = round(test_beam.GetNode("N1").RxnMY, 1)
    rxn_1_MZ = round(test_beam.GetNode("N1").RxnMZ, 1)
    rxn_1 = (rxn_1_X, rxn_1_Y, rxn_1_Z, rxn_1_MX, rxn_1_MY, rxn_1_MZ)

    rxn_2_X = round(test_beam.GetNode("N2").RxnFX, 1)
    rxn_2_Y = round(test_beam.GetNode("N2").RxnFY, 1)
    rxn_2_Z = round(test_beam.GetNode("N2").RxnFZ, 1)
    rxn_2_MX = round(test_beam.GetNode("N2").RxnMX, 1)
    rxn_2_MY = round(test_beam.GetNode("N2").RxnMY, 1)
    rxn_2_MZ = round(test_beam.GetNode("N2").RxnMZ, 1)
    rxn_2 = (rxn_2_X, rxn_2_Y, rxn_2_Z, rxn_2_MX, rxn_2_MY, rxn_2_MZ)

    rxn_3_X = round(test_beam.GetNode("N3").RxnFX, 1)
    rxn_3_Y = round(test_beam.GetNode("N3").RxnFY, 1)
    rxn_3_Z = round(test_beam.GetNode("N3").RxnFZ, 1)
    rxn_3_MX = round(test_beam.GetNode("N3").RxnMX, 1)
    rxn_3_MY = round(test_beam.GetNode("N3").RxnMY, 1)
    rxn_3_MZ = round(test_beam.GetNode("N3").RxnMZ, 1)
    rxn_3 = (rxn_3_X, rxn_3_Y, rxn_3_Z, rxn_3_MX, rxn_3_MY, rxn_3_MZ)

    rxn_4_X = round(test_beam.GetNode("N4").RxnFX, 1)
    rxn_4_Y = round(test_beam.GetNode("N4").RxnFY, 1)
    rxn_4_Z = round(test_beam.GetNode("N4").RxnFZ, 1)
    rxn_4_MX = round(test_beam.GetNode("N4").RxnMX, 1)
    rxn_4_MY = round(test_beam.GetNode("N4").RxnMY, 1)
    rxn_4_MZ = round(test_beam.GetNode("N4").RxnMZ, 1)
    rxn_4 = (rxn_4_X, rxn_4_Y, rxn_4_Z, rxn_4_MX, rxn_4_MY, rxn_4_MZ)
    assert [rxn_1, rxn_2, rxn_3, rxn_4] == expected
