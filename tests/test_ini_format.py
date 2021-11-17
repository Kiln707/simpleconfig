import pytest

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
"favoriteFruit": "banana"
}

multiLayer_test_data = {'default': {
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
"favoriteFruit": "banana"
},
'section':{
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
"favoriteFruit": "banana"
}}

invalid_test_data = {
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
"favoriteFruit": "banana",
'invalid':[1,2,3]
}

def test_read_ini_format(tmpdir_factory):
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.ini")
    import configparser
    with open(test_data_file, "w") as f:
        parser = configparser.ConfigParser()
        parser.optionxform=str
        data = { 'configuration': test_data }
        parser.read_dict(data)
        parser.write(f)
    from simpleconfig import load_or_create
    config = load_or_create(filepath=test_data_file)
    for k, v in test_data.items():
        print(k, config.valueOf(k, type_=type(v)), "value: %s"%v)
        assert config.valueOf(k, type_=type(v)) == v

def test_create_defaults_ini_format(tmpdir_factory):
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.ini")
    from simpleconfig import load_or_create
    from os import path
    assert not path.exists(str(test_data_file))
    config = load_or_create(filepath=test_data_file, defaults=test_data)
    assert config._data == test_data and path.exists(test_data_file)

def test_create_defaults_loadenv_ini_format(tmpdir_factory):
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.ini")
    from simpleconfig import load_or_create
    import os
    assert not os.path.exists(str(test_data_file))
    config = load_or_create(filepath=test_data_file, defaults=test_data, load_env=True)
    assert config.valueOf('company') == os.environ['company'] and config.valueOf('company') != test_data['company']

def test_read_multilayer_ini_format(tmpdir_factory):
    def test_config(config, testdata):
        for k,v in config._data.items():
            if isinstance(v, dict):
                test_config(config.valueOf(k), testdata[k])
            else:
                assert config.valueOf(k, type_=type(v)) == v

    test_data_file = tmpdir_factory.mktemp("data").join("test_data.ini")
    import configparser
    with open(test_data_file, "w") as f:
        parser = configparser.ConfigParser()
        parser.optionxform=str
        parser.read_dict(multiLayer_test_data)
        parser.write(f)
    from simpleconfig import load_or_create
    config = load_or_create(filepath=test_data_file)
    test_config(config, multiLayer_test_data)

def test_invalid_ini_data(tmpdir_factory):
    from simpleconfig import load_or_create
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.ini")
    pytest.raises(Exception, load_or_create, filepath=test_data_file, data=invalid_test_data)
