import pytest
from django.urls import reverse

# from pypro.aperitivos.views import video
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indices'))


def test_status_code(resp):
    assert resp.status_code == 200


# def test_titulo_video(resp):
#     assert_contains(resp, 'Video aperitivo: inicial')
#
#
# def test_conteudo_video(resp):
#     assert_contains(resp,
#                     '<iframe src="https://player.vimeo.com/video/577177067')
