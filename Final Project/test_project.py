from project import min_ll, max_ll,player_move, check_who_won

import pytest

def test_min_ll():
    assert min_ll([['x', 'x', 'o', 'o', 'x', 'x', 'o', ' ', 'o', 1], ['x', 'x', 'o', 'o', 'x', 'x', ' ', 'o', 'o', 0]]) == ['x', 'x', 'o', 'o', 'x', 'x', ' ', 'o', 'o', 0]

def test_max_ll():
    assert max_ll([['o', 'x', 'x', 'x', 'x', ' ', ' ', 'o', 'o', -1], ['o', 'x', 'x', ' ', 'x', 'x', ' ', 'o', 'o', -1], ['o', 'x', 'x', ' ', 'x', ' ', 'x', 'o', 'o', 1]])==['o', 'x', 'x', ' ', 'x', ' ', 'x', 'o', 'o', 1]
    
def test_player_move():
    with pytest.raises(TypeError):
        player_move()
        
def test_x_won():
    assert check_who_won(['x', 'x', 'x', ' ', 'o', 'o', 'o', 'x', 'o', ' '] )==1
    assert check_who_won(['x', 'o', 'o', 'x', ' ', 'x', 'x', 'o', 'o', ' '] )==1
    assert check_who_won(['x', 'o', 'o', 'o', 'x', 'o', 'o', 'x', 'x', ' '] )==1
    
def test_draw():
    assert check_who_won(['x', 'x', 'o', 'o', 'x', 'x', 'x', 'o', 'o', 0] )==0
    
def test_o_won():
    assert check_who_won(['o', 'o', 'o', ' ', 'x', 'x', 'x', 'o', 'x', ' '] )==-1
    assert check_who_won(['o', 'o', 'o', ' ', 'x', 'x', 'x', 'o', 'x', ' '] )==-1
    assert check_who_won(['o', 'o', 'o', ' ', 'x', 'x', 'x', 'o', 'x', ' '] )==-1