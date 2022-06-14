import pytest
from Pet.src.Extract.first import *

class TestGetDataFromAPI(object):
	@pytest.mark.xfail
	def test_none_api():
		assert get_data_from_api() == None
