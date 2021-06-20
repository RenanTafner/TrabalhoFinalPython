from django.urls import include, path
from rest_framework import routers
from . import views



urlpatterns = [
	path('', views.indice, name='indice'),

	path('contasAPagar/detalhar/<int:idContasAPagar>', views.detalhar_contas_a_pagar, name='detalhar_contas_a_pagar'),
	path('contasAPagar/listar', views.listar_contas_a_pagar, name='listar_contas_a_pagar'),
	path('contasAPagar/deletar/<int:idContasAPagar>', views.deletar_contas_a_pagar, name='deletar_contas_a_pagar'),
	path('contasAPagar/criar/', views.criar_contas_a_pagar, name='criar_contas_a_pagar'),
	path('contasAPagar/editar/<int:idContasAPagar>', views.editar_contas_a_pagar, name='editar_contas_a_pagar'),

	path('contasAReceber/detalhar/<int:idContasAReceber>', views.detalhar_contas_a_receber, name='detalhar_contas_a_receber'),
	path('contasAReceber/listar', views.listar_contas_a_receber, name='listar_contas_a_receber'),
	path('contasAReceber/deletar/<int:idContasAReceber>', views.deletar_contas_a_receber, name='deletar_contas_a_receber'),
	path('contasAReceber/criar/', views.criar_contas_a_receber, name='criar_contas_a_receber'),
	path('contasAReceber/editar/<int:idContasAReceber>', views.editar_contas_a_receber, name='editar_contas_a_receber'),

	path('formaPagamentoRecebimento/detalhar/<int:idFormaPagamentoRecebimento>', views.detalhar_forma_pagamento_recebimento, name='detalhar_forma_pagamento_recebimento'),
	path('formaPagamentoRecebimento/listar', views.listar_forma_pagamento_recebimento, name='listar_forma_pagamento_recebimento'),
	path('formaPagamentoRecebimento/deletar/<int:idFormaPagamentoRecebimento>', views.deletar_forma_pagamento_recebimento, name='deletar_forma_pagamento_recebimento'),
	path('formaPagamentoRecebimento/criar/', views.criar_forma_pagamento_recebimento, name='criar_forma_pagamento_recebimento'),
	path('formaPagamentoRecebimento/editar/<int:idFormaPagamentoRecebimento>', views.editar_forma_pagamento_recebimento, name='editar_forma_pagamento_recebimento'),

	path('classificacaoContasAReceber/detalhar/<int:idClassificacaoContasAReceber>', views.detalhar_classificacao_contas_a_receber, name='detalhar_classificacao_contas_a_receber'),
	path('classificacaoContasAReceber/listar', views.listar_classificacao_contas_a_receber, name='listar_classificacao_contas_a_receber'),
	path('classificacaoContasAReceber/deletar/<int:idClassificacaoContasAReceber>', views.deletar_classificacao_contas_a_receber, name='deletar_classificacao_contas_a_receber'),
	path('classificacaoContasAReceber/criar/', views.criar_classificacao_contas_a_receber, name='criar_classificacao_contas_a_receber'),
	path('classificacaoContasAReceber/editar/<int:idClassificacaoContasAReceber>', views.editar_classificacao_contas_a_receber, name='editar_classificacao_contas_a_receber'),

	path('classificacaoContasAPagar/detalhar/<int:idClassificacaoContasAPagar>', views.detalhar_classificacao_contas_a_pagar, name='detalhar_classificacao_contas_a_pagar'),
	path('classificacaoContasAPagar/listar', views.listar_classificacao_contas_a_pagar, name='listar_classificacao_contas_a_pagar'),
	path('classificacaoContasAPagar/deletar/<int:idClassificacaoContasAPagar>', views.deletar_classificacao_contas_a_pagar, name='deletar_classificacao_contas_a_pagar'),
	path('classificacaoContasAPagar/criar/', views.criar_classificacao_contas_a_pagar, name='criar_classificacao_contas_a_pagar'),
	path('classificacaoContasAPagar/editar/<int:idClassificacaoContasAPagar>', views.editar_classificacao_contas_a_pagar, name='editar_classificacao_contas_a_pagar'),


]
