from ..Schrodinger_cat import *

def test_schrodinger_cat():
    """
    testing schrodinger_cat function
    :return:
    """
    is_dead, is_alive = schrodinger_cat()
    assert (is_dead and is_alive is True) or ((is_dead or is_alive) is False) ## (True and True) or (False and False)
