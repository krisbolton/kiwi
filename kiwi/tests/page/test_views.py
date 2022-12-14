from flask import url_for

from lib.tests import assert_status_with_message

class TestPage(object):
	def test_home_page_status(self, client):
		response = client.get(url_for('page.home'))
		assert response.status_code == 200

	def test_privacy_page_status(self, client):
		response = client.get(url_for('page.privacy'))
		assert response.status_code == 200

	def test_terms_page_status(self, client):
		response = client.get(url_for('page.terms'))
		assert response.status_code == 200

	def test_courses_page_status(self, client):
		response = client.get(url_for('page.courses'))
		assert response.status_code == 200

	def test_library_page_status(self, client):
		response = client.get(url_for('page.library'))
		assert response.status_code == 200

	def test_community_page_status(self, client):
		response = client.get(url_for('page.community'))
		assert response.status_code == 200

	def test_404_page(self, client):
		response = client.get('/nonexistantpage')
		assert_status_with_message(404,response, 'Error 404')
