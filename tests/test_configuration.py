def random_str(stringLength=8):
    import random, string
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def random_dict(length=1):
    import random
    return { random_str():random_str() for i in range(length) }


def test_construct_basic_configuration():
    from simpleconfig import Configuration
    configuration_obj = Configuration()
    assert configuration_obj is not None


def test_pass_defaults_return_correct_data():
    from simpleconfig import Configuration
    data = { 'test': 'test' }
    configuration_obj = Configuration(defaults=data)
    assert configuration_obj.valueOf('test') == data['test']


def test_configuration_get():
    from simpleconfig import Configuration
    data = { 'test': 'test' }
    configuration_obj = Configuration(defaults=data)
    assert configuration_obj['test'] == data['test']


def test_configuration_str():
    from simpleconfig import Configuration
    configuration_obj = Configuration()
    assert str(configuration_obj) == "<Configuration data: {} >"


def test_configuration_repr():
    from simpleconfig import Configuration
    configuration_obj = Configuration()
    assert repr(configuration_obj) == "<Configuration data: {} >"


def test_configuration_defaults_set():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    for key, value in data.items():
        assert configuration_obj[key] == value


def test_configuration_items():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    assert data.items() == configuration_obj.items()


def test_configuration_valueOf_defaults_value_exists():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    rand_default_val = random_str()
    for key, value in data.items():
        assert data[key] == configuration_obj.valueOf(key, default=rand_default_val)


def test_configuration_valueOf_default_value_not_exists():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    rand_default_val = random_str()
    assert rand_default_val == configuration_obj.valueOf('non', default=rand_default_val)


def test_configuration_valueOf_type():
    from simpleconfig import Configuration
    data = {'test':'1'}
    configuration_obj = Configuration(defaults=data)
    assert isinstance(configuration_obj.valueOf('test', type_=int), int)


def test_configuration_valueOf_default_type():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    rand_default_val = random_str()
    assert isinstance(configuration_obj.valueOf('non', default='1', type_=int), int)


def test_configuration_valueOf_returns_config():
    from simpleconfig import Configuration
    import random
    data = {'test': random_dict(random.randrange(50)) }
    configuration_obj = Configuration(defaults=data)
    assert isinstance(configuration_obj.valueOf('test'), Configuration)


def test_configuration_valueOf_returns_dict_with_type():
    from simpleconfig import Configuration
    import random
    data = {'test': random_dict(random.randrange(50)) }
    configuration_obj = Configuration(defaults=data)
    assert isinstance(configuration_obj.valueOf('test', type_=dict), dict)


def test_configuration_iters():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    for key in configuration_obj:
        assert key in data


def test_configuration_immutable_1():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    rand_default_key = random_str()
    configuration_obj[rand_default_key] = 'test'
    assert rand_default_key not in configuration_obj


def test_configuration_immutable_2():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    rand_default_key = random_str()
    configuration_obj[rand_default_key] = 'test'
    assert configuration_obj.valueOf(rand_default_key) is None


def test_configuration_empty_reload():
    from simpleconfig import Configuration
    data = { 'test': 'test' }
    configuration_obj = Configuration(defaults=data)
    obj_tmp = configuration_obj
    configuration_obj.reload()
    assert obj_tmp is configuration_obj


def test_configuration_remove_immutable_1():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    rand_default_key = random_str()
    for k in configuration_obj:
        configuration_obj.remove(k)
        assert k in configuration_obj


def test_configuration_remove_immutable_2():
    from simpleconfig import Configuration
    import random
    data = random_dict(random.randrange(50))
    configuration_obj = Configuration(defaults=data)
    rand_default_key = random_str()
    for k in configuration_obj:
        del configuration_obj[k]
        assert k in configuration_obj
