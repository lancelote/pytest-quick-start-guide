import os


def test_empty(tmpdir):
    assert os.path.isdir(tmpdir)
    assert os.listdir(tmpdir) == []


def write_json(fn, data):
    pass


def test_save_curves(tmpdir):
    data = dict(status_code=200, values=[225, 300])
    fn = tmpdir.join('some_file.json)')
    write_json(fn, data)
    assert fn.read() == '{"status_code": 200, "values": [255, 300]}'
