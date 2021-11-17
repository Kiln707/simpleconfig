from mock import Mock


def random_str(stringLength=8):
    import random, string
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def random_dict(length=1):
    import random
    return { random_str():random_str() for i in range(length) }


def test_construct_basic_settings():
    from simpleconfig import Settings
    settings_obj = Settings()
    assert settings_obj is not None


def test_pass_defaults_return_correct_data():
    from simpleconfig import Settings
    data = { 'test': 'test' }
    settings_obj = Settings(defaults=data)
    assert settings_obj.valueOf('test') == data['test']


def test_settings_get():
    from simpleconfig import Settings
    data = { 'test': 'test' }
    settings_obj = Settings(defaults=data)
    assert settings_obj['test'] == data['test']


def test_settings_str():
    from simpleconfig import Settings
    settings_obj = Settings()
    assert str(settings_obj) == "<Settings data: {} >"


def test_settings_repr():
    from simpleconfig import Settings
    settings_obj = Settings()
    assert repr(settings_obj) == "<Settings data: {} >"


def test_settings_defaults_set():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    for key, value in data.items():
        assert settings_obj[key] == value


def test_settings_items():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    assert data.items() == settings_obj.items()


def test_settings_valueOf_defaults_value_exists():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    rand_default_val = random_str()
    for key, value in data.items():
        assert data[key] == settings_obj.valueOf(key, default=rand_default_val)


def test_settings_valueOf_default_value_not_exists():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    rand_default_val = random_str()
    assert rand_default_val == settings_obj.valueOf('non', default=rand_default_val)


def test_settings_valueOf_type():
    from simpleconfig import Settings
    data = {'test':'1'}
    settings_obj = Settings(defaults=data)
    assert isinstance(settings_obj.valueOf('test', type_=int), int)


def test_settings_valueOf_default_type():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    rand_default_val = random_str()
    assert isinstance(settings_obj.valueOf('non', default='1', type_=int), int)


def test_settings_valueOf_returns_config():
    from simpleconfig import Configuration, Settings
    import random
    data = {'test': random_dict(random.randrange(50)) }
    settings_obj = Settings(defaults=data)
    assert isinstance(settings_obj.valueOf('test'), Configuration)


def test_settings_valueOf_returns_dict_with_type():
    from simpleconfig import Settings
    import random
    data = {'test': random_dict(random.randrange(50)) }
    settings_obj = Settings(defaults=data)
    assert isinstance(settings_obj.valueOf('test', type_=dict), dict)


def test_settings_iters():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    for key in settings_obj:
        assert key in data


def test_settings_is_mutable_1():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    rand_default_key = random_str()
    settings_obj[rand_default_key] = 'test'
    assert rand_default_key in settings_obj


def test_settings_is_mutable_2():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    rand_default_key = random_str()
    settings_obj[rand_default_key] = 'test'
    assert settings_obj.valueOf(rand_default_key) == 'test'


def test_settings_empty_reload():
    from simpleconfig import Settings
    data = { 'test': 'test' }
    settings_obj = Settings(defaults=data)
    obj_tmp = settings_obj
    settings_obj.reload()
    assert obj_tmp is settings_obj


def test_settings_remove_1():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    rand_default_key = random_str()
    settings_obj[rand_default_key] = 'test'
    assert rand_default_key in settings_obj
    settings_obj.remove(rand_default_key)
    assert rand_default_key not in settings_obj


def test_settings_remove_1():
    from simpleconfig import Settings
    import random
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    rand_default_key = random_str()
    settings_obj[rand_default_key] = 'test'
    assert rand_default_key in settings_obj
    del settings_obj[rand_default_key]
    assert rand_default_key not in settings_obj


def test_settings_notify_set():
    from simpleconfig import Settings
    import random

    def test_func(*args, **kwargs):
        pass
    mock_func = Mock(spec=test_func)
    data = random_dict(random.randrange(50))
    settings_obj = Settings(defaults=data)
    settings_obj.on_update.connect(mock_func)
    settings_obj._data_loaded = True
    rand_default_key = random_str()
    settings_obj[rand_default_key] = 'test'
    mock_func.assert_called_once_with(settings_obj, action='set', key=rand_default_key, new_value='test', old_value=None)


def test_settings_notify_update():
    from simpleconfig import Settings
    import random

    def test_func(*args, **kwargs):
        pass
    mock_func = Mock(spec=test_func)
    data = random_dict(random.randrange(50))
    rand_default_key = random_str()
    data[rand_default_key] = 'test'
    settings_obj = Settings(defaults=data)
    settings_obj.on_update.connect(mock_func)
    settings_obj._data_loaded = True
    settings_obj[rand_default_key] = 'test1'
    mock_func.assert_called_once_with(settings_obj, action='updated', key=rand_default_key,
                                      old_value='test', new_value='test1')


def test_settings_notify_remove():
    from simpleconfig import Settings
    import random

    def test_func(*args, **kwargs):
        pass
    mock_func = Mock(spec=test_func)
    data = random_dict(random.randrange(50))
    rand_default_key = random_str()
    data[rand_default_key] = 'test'
    settings_obj = Settings(defaults=data)
    settings_obj.on_update.connect(mock_func)
    settings_obj._data_loaded = True
    settings_obj.remove(rand_default_key)
    mock_func.assert_called_once_with(settings_obj, action='removed',
                                      key=rand_default_key, old_value='test', new_value=None)


def test_create_defaults_json_format(tmpdir_factory):
    test_data_file = tmpdir_factory.mktemp("data").join("test_data.json")
    from simpleconfig import load_or_create, create_settings
    import random, json
    data = random_dict(random.randrange(50))
    rand_default_key = random_str()
    data[rand_default_key] = 'test'
    settings_obj = load_or_create(filepath=test_data_file, defaults=data, auto_save=True)
    settings_obj._data_loaded = True
    with open(test_data_file) as f:
        assert settings_obj._data == json.loads(f.read())
    settings_obj.setValue(rand_default_key, 'randomstring')
    with open(test_data_file) as f:
        assert settings_obj._data == json.loads(f.read())
