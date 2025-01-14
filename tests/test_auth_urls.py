import pytest


class TestAuthUrls:
    @pytest.mark.django_db(transaction=True)
    def test_auth_urls(self, client):
        urls = ['/auth/login/', '/auth/logout/', '/auth/signup/']
        for url in urls:
            try:
                method = getattr(
                    client, 'get' if url != '/auth/logout/' else 'post'
                )
                response = method(url)
            except Exception as e:
                pytest.fail(
                    f'Страница `{url}` работает неправильно. Ошибка: `{e}`'
                )
            assert response.status_code != 404, (
                f'Страница `{url}` не найдена, проверьте этот адрес в *urls.py*'
            )
            assert response.status_code == 200, (
                f'Ошибка {response.status_code} при открытиии `{url}`. Проверьте ее view-функцию'
            )
