#!/usr/bin/env python

from stringmatch import match

def test_match():
    m = match('hello', 'world')
    print('Cost is: %s', m.cost)
    assert m.cost > 0

    m = match('hello', 'hello')
    print('Cost is: %s', m.cost)
    assert m.cost == 0

if __name__ == '__main__':
    import pytest
    pytest.main(__file__)
