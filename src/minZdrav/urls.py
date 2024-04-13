from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from logRegisPages.views import  registration, activate, user_login, user_logout, CustomPasswordResetView, CustomPasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from minZdrav.download import download_file
from news.views import post_new
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('static_pages.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    
    
]
urlpatterns += i18n_patterns(
    path('news/', include('news.urls')), #Новости
    path('new-news/', post_new, name = 'new_new'), #Новые новости
    path('med-services/', include('medServices.urls')), #Медицинские услуги (пока что)
    path('rules/', include('info_page.urls')), #Правила санатория
    path('viewSovet/', include('viewSovet.urls')), #Наблюдательный совет
    path('contacts/', include('contact_pages.urls')), #контакты
    path('histories/', include('history_legends.urls')), #История и легенды
    path('ceo-info/', include('ceoInfo.urls')), #О руководителе
    path('vacancies/', include('vacancies.urls')), #Вакансии
    path('organization-structure/', include('orgStruct.urls')), #Организационная структура
    path('rights-acts/', include('ProvActs.urls')), #Правовые акты (Надо будет убрать)
    path('workers-info/', include('workersInfo.urls')), #Информация о сотрудниках
    path('anticorruption/', include('antiCorruptions.urls')), #Противодействие коррупции
    path('about/', include('aboutPage.urls')),    #О НИИ
    path('reviews/', include('reviewsBlog.urls')), #Отзывы
    path('advertisement/', include('advertisement.urls')), #Объявления
    path('appeal/', include('appeal.urls')), #Обращения
    path('login/', user_login, name = 'login'), #Авторизация
    path('logout/', user_logout, name = 'logout'), #Выход
    path('registration/', registration, name = 'registr'), #Регистрация
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'), #Забыли пароль
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #страница с текстом об отправке ссылке на сброс пароля
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'), #
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('download/<str:file_name>/', download_file, name='download_file'), #Скачивание файлов
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'), #страница активации аккаунта

    path('gobmp/', TemplateView.as_view(template_name='dopPages/gobmp.html'), name='gobmp'), #получение услуг по ГОБМП
    path('scientific-developments/', TemplateView.as_view(template_name='dopPages/scientificDev.html'), name='sci-dev'), #Научные достижения
    path('plans/', TemplateView.as_view(template_name='dopPages/plans.html'), name='plans'), #Планы
    path('quality-management-standard/', TemplateView.as_view(template_name='dopPages/managment_standart.html'), name='managment_standart'), #Стандарты менеджмента качества
    path('strategic-development/', TemplateView.as_view(template_name='dopPages/strategic_development.html'), name='srategic-dev'), #Стратегическое развитие
    path('ceo-blog/', include('ceoblog.urls')),
    path('achievments/', TemplateView.as_view(template_name='dopPages/Achievments.html'), name='achievments'),
    path('people/', include('people.urls')),
    path('uvo/', TemplateView.as_view(template_name='dopPages/UVO.html'), name='uvo'),
    path('schedule-of-childrens-shifts/', TemplateView.as_view(template_name='dopPages/kidsSchedule.html'), name='kidsSchedule'),
    path('media-galery/', TemplateView.as_view(template_name='dopPages/mediagallery.html'), name='mediagallery'),
    path('strategic-partners/', TemplateView.as_view(template_name='dopPages/strategicPartners.html'), name='strategic_partners'),
    path('ethics-regulations/', TemplateView.as_view(template_name='dopPages/ethicsRegulations.html'), name='ethicsRegulations'),
    path('labor-protection/', TemplateView.as_view(template_name='dopPages/laborProtection.html'), name='laborProtection'),
    path('leisure/', TemplateView.as_view(template_name='dopPages/leisure.html'), name='leisure'),
    path('transit/', TemplateView.as_view(template_name='dopPages/transit.html'), name='transit'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)