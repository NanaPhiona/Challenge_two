from flask import json
import pytest
from app.views.create_red_flag import app
from app.views.delete_specific_red_flag import app
from app.views.edit_specific_red_flag import app
from app.views.get_all_red_flags import app
from app.views.get_specific_red_flag import app


@pytest.fixture
def client():
    with app.app_context():
        app.config['TESTING'] = True
        test_client = app.test_client()
    return test_client


class TestApi:

    def test_create_red_flag(self, client):
        url = '/api/v1/red-flags'
        json_dict = {
            "id": 1,
            "type": "red-flag",
            "status": "resolved",
            "location": "bweyos",
            "comment": "bribery"
        }
        resp = client.post(
            url,
            data=json.dumps(json_dict),
            content_type='application/json'
        )
        assert json_dict in resp.json['data']
        assert resp.status_code == 201

    def test_create_red_flag_no_data(self, client):
        url = '/api/v1/red-flags'
        json_dict = {}
        resp = client.post(
            url,
            data=json.dumps(json_dict),
            content_type='application/json'
        )
        assert resp.status_code == 404

    def test_get_all_red_flags(self, client):
        url = '/api/v1/red-flags'
        resp = client.get(
            url,
            content_type='application/json'
        )
        assert resp.status_code == 200

    def test_get_specific_red_flags(self, client):
        url = '/api/v1/red-flags/1'
        resp = client.get(
            url,
            content_type='application/json'
        )
        assert resp.status_code == 200

    def test_edit_specific_red_flag(self, client):
        url = '/api/v1/red-flags'
        json_dict = {
            "id": 1,
            "type": "red-flag",
            "status": "resolved",
            "location": "bweyos",
            "comment": "bribery"
        }
        resp = client.post(
            url,
            data=json.dumps(json_dict),
            content_type='application/json'
        )

        url2 = '/api/v1/red-flags/1/location'
        json_dict2 = {'location': 'hoima'}
        resp2 = client.patch(
            url2,
            data=json.dumps(json_dict2),
            content_type='application/json'
        )
        assert resp.status_code == 201
        assert resp2.status_code == 204

    def test_edit_specific_comment(self, client):
        url = '/api/v1/red-flags'
        json_dict = {
            "id": 1,
            "type": "red-flag",
            "status": "resolved",
            "location": "bweyos",
            "comment": "bribery"
        }
        resp = client.post(
            url,
            data=json.dumps(json_dict),
            content_type='application/json'
        )

        url = '/api/v1/red-flags/1/comment'
        json_dict2 = {'comment': 'corruption'}
        resp2 = client.patch(
            url,
            data=json.dumps(json_dict2),
            content_type='application/json'

        )
        assert resp.status_code == 201
        assert resp2.status_code == 204

    def test_delete_specific_red_flag(self, client):
        url = '/api/v1/red-flags/1'
        json_dict = {
            "id": 1,
            "type": "red-flag",
            "status": "resolved",
            "location": "bweyos",
            "comment": "bribery"
        }
        resp = client.delete(
            url,
            data=json.dumps(json_dict),
            content_type='application/json'
        )
        assert resp.status_code == 202
