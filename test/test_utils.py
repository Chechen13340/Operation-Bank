from app.utils import executed_operations, last_five_operations, sort_time_operation, convert_date, convert_from, \
    convert_to, display_information


def test_get_operations(list_get_operations):
    assert isinstance(list_get_operations, list)


def test_executed_operations():
    test_ex = executed_operations()
    assert isinstance(test_ex, list)
    for i in test_ex:
        assert i['state'] == 'EXECUTED'


def test_last_five_operations():
    test_five = last_five_operations()
    assert isinstance(test_five, list)
    assert len(test_five) == 5


def test_sort_time_operation():
    test_sort_time = sort_time_operation()
    assert test_sort_time


def test_convert_date(ISO_time):
    test_conv_date = convert_date(ISO_time)
    assert test_conv_date


def test_convert_from(list_get_operations):
    for i in list_get_operations:
        assert convert_from(i.get('from'))


def test_convert_to(list_get_operations):
    for i in list_get_operations:
        assert convert_to(i['to'])


def test_display_information():
    assert display_information()
    assert isinstance(display_information(), list)
