from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'classificacao-contas-pagar', views.ClassificacaoContasAPagarViewSet)
router.register(r'classificacao-contas-receber', views.ClassificacaoContasAReceberViewSet)
router.register(r'contas-pagar', views.ContasAPagarViewSet)
router.register(r'contas-receber', views.ContasAReceberViewSet)
router.register(r'forma-pagamento', views.FormaPagamentoRecebimentoViewSet)

urlpatterns = [
	path('relatorio', views.relatorio, name='relatorio'),
	path('relpagar/<str:dtInit>/<str:dtEnd>', views.relpagar, name='relpagar'),
	path('relreceber/<str:dtInit>/<str:dtEnd>', views.relreceber, name='relreceber'),
	path('exibir_fluxo_caixa', views.exibir_fluxo_caixa, name='exibir_fluxo_caixa'),
	path('', include(router.urls)),
	path('api-auth/', 
		include('rest_framework.urls',
				namespace='rest_framework')
		)
]
