from src.math_operations import add,sub
def tets_add():
    assert add(5,4)==9
    assert add(2,3)==5
def test_sub():
    assert sub(3,1)==2
    assert sub(5,2)==3
    assert sub(8,6)==2