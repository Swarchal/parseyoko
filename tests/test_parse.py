import parseyoko.parse


def test_parse_final_path():
    test_file = "exampleExperiment_K02_T0014F001L01A01Z01C03.tif"
    output = parseyoko.parse_filepath(test_file)
    assert output.well == "K02"
    assert output.channel == 3
    assert output.site == 1
    assert output.filepath == "exampleExperiment_K02_T0014F001L01A01Z01C03.tif"


def test_parse_final_path():
    test_file = "/some/directory/subdirectory/exampleExperiment_K02_T0014F001L01A01Z01C03.tif"
    output = parseyoko.parse_filepath(test_file)
    assert output.well == "K02"
    assert output.channel == 3
    assert output.site == 1
    assert output.filepath == "/some/directory/subdirectory/exampleExperiment_K02_T0014F001L01A01Z01C03.tif"


