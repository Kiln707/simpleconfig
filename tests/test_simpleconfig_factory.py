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


def test_create_configuration():
    from simpleconfig import load_or_create, Configuration
    config = load_or_create(defaults=test_data)
    assert isinstance(config, Configuration)


def test_create_settings_auto_save():
    from simpleconfig import load_or_create, Settings
    config = load_or_create(defaults=test_data, auto_save=True)
    assert isinstance(config, Settings)


def test_create_settings_updatable():
    from simpleconfig import load_or_create, Settings
    config = load_or_create(defaults=test_data, updatable=True)
    assert isinstance(config, Settings)


def test_create_configuration_no_path():
    from simpleconfig import load_or_create
    config = load_or_create(defaults=test_data)
    assert config._data == test_data


def test_exception_creation_empty():
    from simpleconfig import load_or_create
    pytest.raises(Exception, load_or_create)


def test_remove_and_insert_formatter():
    from simpleconfig import _formatters, remove_formatter, JSON_Formatter, NoFormatterError, add_formatter
    assert isinstance(_formatters.get_formatter('test.json'), JSON_Formatter)
    remove_formatter('json')
    with pytest.raises(NoFormatterError) as e:
        _formatters.get_formatter('test.json')
    add_formatter('json', JSON_Formatter)
    assert isinstance(_formatters.get_formatter('test.json'), JSON_Formatter)


def test_exception_no_formatter():
    from simpleconfig import get_formatter
    pytest.raises(Exception, get_formatter, 'test.abc')


def test_env_loading():
    from simpleconfig import load_or_create
    config = load_or_create(defaults=test_data, load_env=True)
    import os
    assert config.valueOf('company') == os.environ['company'] and config.valueOf('company') != test_data['company']


def test_save_config_no_location():
    from simpleconfig import load_or_create, save
    config = load_or_create(defaults=test_data)
    assert not save(config)


def get_formatter():
    from simpleconfig import get_formatter
    formatter = get_formatter('/etc/somedir/somefile.json')
    assert formatter