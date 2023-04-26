import pytest
from lib.to_do_task import *


def test_no_to_do():
    with pytest.raises(Exception) as e:
        result = to_do("Reminder: You are amazing!")
    error_message = str(e.value)
    assert error_message == "This does not have a TODO"

def test_to_do():
    result = to_do("#TODO: To do the laundry!")
    assert result == "#TODO: To do the laundry!"