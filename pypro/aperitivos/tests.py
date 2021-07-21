import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('inicial',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.tivulo)


def test_conteudo_video(resp):
    assert_contains(resp,
                    '<iframe src="https://player.vimeo.com/video/577177067"')
