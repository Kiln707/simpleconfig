test_data = {
"_id": "5973782bdb9a930533b05cb2",
"isActive": True,
"balance": 1446.35,
"age": 32,
"eyeColor": "green",
"name": "Logan Keller",
"gender": "male",
"company": "ARTIQ",
"email": "logankeller@artiq.com",
"phone": "+1 (952) 533-2258",
"friends": [
  {
    "id": 0,
    "name": "Colon Salazar"
  },
  {
    "id": 1,
    "name": "French Mcneil"
  },
  {
    "id": 2,
    "name": "Carol Martin"
  }
],
"favoriteFruit": "banana"
}

def test_read_json_format(tmpdir_factory):
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.json")
    import json
    with open(test_data_file, "w") as f:
        f.write(json.dumps(test_data))
    from simpleconfig import load_or_create
    config = load_or_create(filepath=test_data_file)
    assert config._data == test_data

def test_create_defaults_json_format(tmpdir_factory):
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.json")
    from simpleconfig import load_or_create
    from os import path
    import json
    assert not path.exists(str(test_data_file))
    config = load_or_create(filepath=test_data_file, defaults=test_data)
    assert config._data == test_data and path.exists(test_data_file)
    with open(test_data_file) as f:
        assert config._data == json.loads(f.read())

def test_create_defaults_loadenv_json_format(tmpdir_factory):
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.json")
    from simpleconfig import load_or_create
    import os
    assert not os.path.exists(str(test_data_file))
    config = load_or_create(filepath=test_data_file, defaults=test_data, load_env=True)
    assert config.valueOf('company') == os.environ['company'] and config.valueOf('company') != test_data['company']
