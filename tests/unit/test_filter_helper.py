from api.models._smart_data_deid import (
    _vision_filter,
    _pressure_filter,
    _filter_vis_pres_range,
)
from api.keywords import KEYWORDS


def test_filter_vis_pres_range(app):
    with app.app_context():
        res = _filter_vis_pres_range(
            KEYWORDS["left_pressure"], (None, 10), vision=False,
        )
        assert res == [64656, 66166]

        res = _filter_vis_pres_range(KEYWORDS["left_pressure"], (10, 10), vision=False,)
        assert res == [64656, 66166]

        res = _filter_vis_pres_range(
            KEYWORDS["left_pressure"], (None, None), vision=False
        )
        assert len(res) != 0


def test_vision_filter():
    data = [
        (20676, "20/20"),
        (20676, "20/20"),
        (20676, "20/20"),
        (20676, "20/20-1"),
        (20676, "20/20-2"),
        (20676, "20/20"),
        (36440, "20/25-2"),
        (36440, "20/25-3"),
        (36440, "20/20-2"),
        (36440, "20/25"),
        (36440, "20/20"),
        (36440, "20/60+2"),
        (36440, "20/400"),
        (50765, "20/250"),
        (50765, "20/30"),
        (50765, "20/40-2"),
        (50765, "20/150"),
        (50765, "20/40-"),
        (50765, "20/30"),
        (50765, "20/40-1"),
        (50765, "20/50-"),
        (50765, "20/125"),
        (50765, "20/50-2"),
        (50765, "20/20"),
        (50765, "20/60"),
        (50765, "20/30"),
        (64656, "20/60-2"),
        (66172, "20/20-3"),
        (66172, "20/40"),
        (66172, "20/30+2"),
        (66172, "20/40+2"),
        (66172, "20/30-2"),
        (66172, "20/40-2"),
        (66172, "20/20"),
        (66172, "20/40"),
        (66475, "20/20"),
        (66475, "20/25+"),
        (66475, "20/30"),
        (66475, "20/20"),
    ]

    res = _vision_filter(data, None, None)
    assert len(res) == len(data)
    res = _vision_filter(data, 20, 40)
    for v in res:
        assert 20 <= int(v[1].split("/")[1].split("-")[0].split("+")[0]) <= 40


def test_pressure_filter():
    data = [
        (20676, "14"),
        (20676, "14"),
        (20676, "14"),
        (20676, "14"),
        (20676, "15"),
        (20676, "14"),
        (36440, "17"),
        (36440, "22"),
        (36440, "17"),
        (36440, "15"),
        (36440, "18"),
        (36440, "17"),
        (36440, "17"),
        (36440, "18"),
        (36440, "21"),
        (36440, "23"),
        (36440, "28"),
        (36440, "19"),
        (36440, "17"),
        (36440, "20"),
        (36440, "15"),
        (36440, "20"),
        (36440, "24"),
        (36440, "16"),
        (36440, "21"),
        (36440, "19"),
        (36440, "19"),
        (36440, "17"),
        (36440, "17"),
        (36440, "17"),
        (36440, "19"),
        (36440, "16"),
        (36440, "18"),
        (36440, "13"),
        (36440, "21"),
        (36440, "17"),
        (36440, "16"),
        (36440, "17"),
        (36440, "18"),
        (36440, "17"),
        (36440, "19"),
        (36440, "17"),
        (36440, "17"),
        (36440, "20"),
        (36440, "14"),
        (36440, "19"),
        (36440, "17"),
        (36440, "21"),
        (36440, "16"),
        (36440, "16"),
        (36440, "21"),
        (36440, "18"),
        (36440, "21"),
        (36440, "19"),
        (36440, "16"),
        (36440, "18"),
        (36440, "16"),
        (36440, "18"),
        (36440, "18"),
        (36440, "18"),
        (36440, "17"),
        (36440, "16"),
        (36440, "18"),
        (36440, "20"),
        (36440, "20"),
        (36440, "18"),
        (36440, "21"),
        (36440, "18"),
        (36440, "17"),
        (36440, "19"),
        (36440, "19"),
        (36440, "15"),
        (36440, "19"),
        (36440, "17"),
        (36440, "18"),
        (36440, "18"),
        (36440, "19"),
        (36440, "20"),
        (36440, "17"),
        (36440, "22"),
        (36440, "19"),
        (36440, "20"),
        (36440, "17"),
        (36440, "18"),
        (36440, "14"),
        (36440, "20"),
        (36440, "20"),
        (36440, "20"),
        (36440, "18"),
        (36440, "22"),
        (36440, "21"),
        (36440, "22"),
        (36440, "19"),
        (36440, "19"),
        (36440, "18"),
        (36440, "20"),
        (36440, "24"),
        (36440, "22"),
        (36440, "17"),
        (36440, "21"),
    ]
    res = _pressure_filter(data, None, None)
    assert len(res) == len(data)
    res = _pressure_filter(data, 12, 10)
    for v in res:
        assert 10 <= v[1] <= 12

    data = [(1, "-1"), (1, "12345")]
    res = _pressure_filter(data, None, None)
    assert len(res) == 0
