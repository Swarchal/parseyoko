import os
from collections import namedtuple


def parse_filepath(filepath):
    """
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20
    T|0|0|0|1|F|0|0|6|L|0 |1 |A |0 |4 |Z |0 |1 |C |0 |2
    ------------------------------------------------------
    example:
        >>> filepath = "test_N22_T0001F006L01A04Z01C02.tif"
        >>> parse_filepath(filepath)
        ("well": "N22",
         "site": 6,
         "z": 1
         "channel": 2,
         "filepath: "test_N22_T0001F006L01A04Z01C02.tif")
    """
    final_path = filepath.split(os.path.sep)[-1]
    output = namedtuple("Yoko", ["well", "site", "z", "channel", "filepath"])
    *_, well, rest = final_path.split("_")
    rest = rest.replace(".tif", "")
    site = int(rest[6:9])
    z = int(rest[16:18])
    channel = int(rest[-2:])
    return output(well, site, z, channel, filepath)


def clean_paths(paths):
    """
    remove unwanted files
    WARNING: likely to break as it makes a lot of assumptions
    """
    output = []
    for p in paths:
        final_path = p.split(os.sep)[-1]
        if p.endswith(".tif") and len(final_path.split("_")) == 3 and "#" not in p:
            output.append(p)
    assert len(output) >= 1
    return output

