# django default
from django.urls import path
from django.conf.urls import url
from .djangoapps.test import views as TestViews
from .djangoapps.main import views as MainViews

urlpatterns = [
    # 테스트 페이지 작성 시 아래 URL을 사용해주세요!
    url('^$', MainViews.test, name='test'),
    url('^test/view$', TestViews.test_view, name='test_view'),

    ]
