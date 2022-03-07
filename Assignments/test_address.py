from address import extract_city, extract_state, extract_zipcode
    
import pytest

def test_city():
    assert extract_city('690 Sugarwood Ct., Galt, CA 95632') == 'Galt'



def test_state():
    assert extract_state('690 Sugarwood Ct., Galt, CA 95632') == 'CA'

def test_zipcode():
    assert extract_zipcode('690 Sugarwood Ct., Galt, CA 95632') == '95632'
    
    
    
    
    
    
    
    
    
    




pytest.main(["-v", "--tb=line", "-rN", __file__])