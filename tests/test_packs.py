import kpn_senml


def test_from_json_single_bn():
    pack = kpn_senml.SenmlPack("foobar")
    json_data = '[{"n":"name_1","bn":"foobar","v":1.2},'\
            '{"n":"name_2","v":-0.1}]'
    pack.from_json(json_data)
    assert len(list(pack)) == 2


def test_from_json_multiple_bn():
    pack = kpn_senml.SenmlPack("multi-dev")
    json_data = '[{"n":"name_1","bn":"dev_1","v":1.2},'\
            '{"n":"name_2","v":-0.1},'\
            '{"n":"name_1","bn":"dev_2","v":1.5},'\
            '{"n":"name_2","v":-0.3}]'
    pack.from_json(json_data)
    assert len(list(pack)) == 2
    for dev_pack in pack:
        assert type(dev_pack) == kpn_senml.SenmlPack
        assert len(list(dev_pack)) == 2
    

def test_from_json_reads_bt_single_bn():
    pack = kpn_senml.SenmlPack("foobar")
    bt_value = 1668000265
    json_data = f'[{{"n":"name_1","bn":"foobar","bt":{bt_value},"v":1.2}},'\
            '{"n":"name_2","v":-0.1}]'
    pack.from_json(json_data)
    assert pack.base_time == bt_value
    assert len(list(pack)) == 2


def test_from_json_reads_bt_multiple_bn():
    pack = kpn_senml.SenmlPack("multi-dev")
    bt_values = [1668000265, 1668000266]
    json_data = f'[{{"n":"name_1","bn":"dev_1","bt":{bt_values[0]},"v":1.2}},'\
            '{"n":"name_2","v":-0.1},'\
            f'{{"n":"name_1","bn":"dev_2","bt":{bt_values[1]},"v":1.5}},'\
            '{"n":"name_2","v":-0.3}]'
    pack.from_json(json_data)
    assert pack.base_time == None
    assert len(list(pack)) == 2
    for i, dev_pack in enumerate(pack):
        assert type(dev_pack) == kpn_senml.SenmlPack
        assert dev_pack.base_time == bt_values[i]
        assert len(list(dev_pack)) == 2
