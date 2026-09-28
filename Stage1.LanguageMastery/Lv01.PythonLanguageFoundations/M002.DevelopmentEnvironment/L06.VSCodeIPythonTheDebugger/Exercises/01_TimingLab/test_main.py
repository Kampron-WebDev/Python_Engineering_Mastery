# Run with:  python -m pytest
import time


def test_build_functions_agree(main):
    assert main.build_with_plus(4) == "0,1,2,3"
    assert main.build_with_join(4) == "0,1,2,3"
    assert main.build_with_plus(0) == main.build_with_join(0) == ""
    assert main.build_with_plus(1000) == main.build_with_join(1000)


def test_time_per_call_is_an_average(main):
    per_call = main.time_per_call(lambda: time.sleep(0.002), number=10)
    assert 0.0015 < per_call < 0.05


def test_fastest_picks_the_clearly_faster_one(main):
    candidates = {
        "slow": lambda: sum(range(20_000)),
        "fast": lambda: 42,
    }
    assert main.fastest(candidates, number=50) == "fast"
