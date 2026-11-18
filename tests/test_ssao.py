import pytest
from render import ssao as mod

CASES = [
    ("radius_scale", "m.world_radius(1.0, 2.0) == approx(2.0)"),
    ("radius_zero", "m.world_radius(0.0, 2.0) == approx(0.0)"),
    ("bilateral_same", "m.bilateral_depth(1.0, 1.0) == approx(1.0)"),
    ("bilateral_diff", "m.bilateral_depth(1.0, 2.0) < 1.0"),
    ("normal_zero", "m.encode_normal(0.0, 0.0, 1.0) == (0.0, 0.0, 1.0)"),
    ("samples_min", "m.sample_count(2.0, 2.0) == 4"),
    ("noise_frame", "m.world_noise((0.0, 0.0), 1) == approx((0.1, 0.1))"),
    ("dedupe_low", "m.dedupe_ao(2.0, 1.0) == approx(1.0)"),
    ("dedupe_high", "m.dedupe_ao(0.5, 1.0) == approx(0.5)"),
    ("transparent_true", "m.transparent_ao(0.9) is True"),
    ("transparent_false", "m.transparent_ao(0.1) is False"),
    ("upsample_same", "m.upsample_ao(1.0, 1.0) == approx(1.0)"),
    ("upsample_diff", "m.upsample_ao(1.0, 2.0) == approx(0.5)"),
    ("reset_true", "m.reset_history(True) is True"),
    ("fog_product", "m.apply_before_fog(1.0, 2.0) == approx(2.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
