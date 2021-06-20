from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ClassificacaoContasAPagar
from .models import ClassificacaoContasAReceber
from .models import ContasAPagar
from .models import ContasAReceber
from .models import FormaPagamentoRecebimento
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def indice(request):
	response = HttpResponse()

	if request.method == 'GET':
		response.write("Usei o método GET")
	elif request.method == 'POST':
		response.write("Usei o método POST")
	else:
		response.write("Método HTTP não suportado!")

	return response

@csrf_exempt
def detalhar_contas_a_pagar(request, idContasAPagar):
	try:
		contasAPagar = ContasAPagar.objects.obter_contas_a_pagar_id(idContasAPagar)

	except:
		return HttpResponse("Erro ao buscar Conta A Pagar")

	dados = {'contasAPagar': contasAPagar}
	return render(request, 'contasAPagar/detalhar.html', dados)

@csrf_exempt
def detalhar_contas_a_receber(request, idContasAReceber):
	try:
		contasAReceber = ContasAReceber.objects.obter_contas_a_receber_id(idContasAReceber)

	except:
		return HttpResponse("Erro ao buscar Conta a Receber")

	dados = {'contasAReceber': contasAReceber}
	return render(request, 'contasAReceber/detalhar.html', dados)

@csrf_exempt
def detalhar_forma_pagamento_recebimento(request, idFormaPagamentoRecebimento):
	try:
		formaPagamentoRecebimento = FormaPagamentoRecebimento.objects.obter_forma_pagamento_recebimento_id(idFormaPagamentoRecebimento)

	except:
		return HttpResponse("Erro ao buscar Forma de Pagamento / Recebimento")

	dados = {'formaPagamentoRecebimento': formaPagamentoRecebimento}
	return render(request, 'formaPagamentoRecebimento/detalhar.html', dados)

@csrf_exempt
def detalhar_classificacao_contas_a_receber(request, idClassificacaoContasAReceber):
	try:
		classificacaoClassificacaoContasAReceber = ClassificacaoContasAReceber.objects.obter_classificacao_contas_a_receber_id(idClassificacaoContasAReceber)

	except:
		return HttpResponse("Erro ao buscar Classificação de Contas a Receber")

	dados = {'classificacaoClassificacaoContasAReceber': classificacaoClassificacaoContasAReceber}
	return render(request, 'classificacaoClassificacaoContasAReceber/detalhar.html', dados)

@csrf_exempt
def detalhar_classificacao_contas_a_pagar(request, idClassificacaoContasAPagar):
	try:
		classificacaoClassificacaoContasAPagar = ClassificacaoContasAPagar.objects.obter_classificacao_contas_a_pagar_id(idClassificacaoContasAPagar)

	except:
		return HttpResponse("Erro ao buscar Classificação de Contas a Pagar")

	dados = {'classificacaoClassificacaoContasAPagar': classificacaoClassificacaoContasAPagar}
	return render(request, 'classificacaoClassificacaoContasAPagar/detalhar.html', dados)


@csrf_exempt
def criar_contas_a_pagar(request):

	return render(request, 'contasAPagar/criar.html')

@csrf_exempt
def criar_contas_a_receber(request):

	return render(request, 'contasAReceber/criar.html')

@csrf_exempt
def criar_forma_pagamento_recebimento(request):

	return render(request, 'formaPagamentoRecebimento/criar.html')

@csrf_exempt
def criar_classificacao_contas_a_receber(request):

	return render(request, 'classificacaoContasAReceber/criar.html')

@csrf_exempt
def criar_classificacao_contas_a_pagar(request):

	return render(request, 'classificacaoContasAPagar/criar.html')


@csrf_exempt
def editar_contas_a_pagar(request, idContasAPagar):
	try:
		contasAPagar = ContasAPagar.objects.obter_contas_a_pagar_id(idContasAPagar)

	except:
		return HttpResponse("Erro ao buscar Conta A Pagar")

	dados = {'contasAPagar': contasAPagar}
	return render(request, 'contasAPagar/editar.html', dados)

@csrf_exempt
def editar_contas_a_receber(request, idContasAReceber):
	try:
		contasAReceber = ContasAReceber.objects.obter_contas_a_receber_id(idContasAReceber)

	except:
		return HttpResponse("Erro ao buscar Conta a Receber")

	dados = {'contasAReceber': contasAReceber}
	return render(request, 'contasAReceber/editar.html', dados)

@csrf_exempt
def editar_forma_pagamento_recebimento(request, idFormaPagamentoRecebimento):
	try:
		formaPagamentoRecebimento = FormaPagamentoRecebimento.objects.obter_forma_pagamento_recebimento_id(idFormaPagamentoRecebimento)

	except:
		return HttpResponse("Erro ao buscar Forma de Pagamento / Recebimento")

	dados = {'formaPagamentoRecebimento': formaPagamentoRecebimento}
	return render(request, 'formaPagamentoRecebimento/editar.html', dados)

@csrf_exempt
def editar_classificacao_contas_a_receber(request, idClassificacaoContasAReceber):
	try:
		classificacaoClassificacaoContasAReceber = ClassificacaoContasAReceber.objects.obter_classificacao_contas_a_receber_id(idClassificacaoContasAReceber)

	except:
		return HttpResponse("Erro ao buscar Classificação de Contas a Receber")

	dados = {'classificacaoClassificacaoContasAReceber': classificacaoClassificacaoContasAReceber}
	return render(request, 'classificacaoClassificacaoContasAReceber/editar.html', dados)

@csrf_exempt
def editar_classificacao_contas_a_pagar(request, idClassificacaoContasAPagar):
	try:
		classificacaoClassificacaoContasAPagar = ClassificacaoContasAPagar.objects.obter_classificacao_contas_a_pagar_id(idClassificacaoContasAPagar)

	except:
		return HttpResponse("Erro ao buscar Classificação de Contas a Pagar")

	dados = {'classificacaoClassificacaoContasAPagar': classificacaoClassificacaoContasAPagar}
	return render(request, 'classificacaoClassificacaoContasAPagar/editar.html', dados)



@csrf_exempt
def deletar_contas_a_pagar(request, idContasAPagar):
	try:
		contasAPagar = ContasAPagar.objects.obter_contas_a_pagar_id(idContasAPagar)

	except:
		return HttpResponse("Erro ao buscar Conta A Pagar")

	dados = {'contasAPagar': contasAPagar}
	return render(request, 'contasAPagar/deletar.html', dados)

@csrf_exempt
def deletar_contas_a_receber(request, idContasAReceber):
	try:
		contasAReceber = ContasAReceber.objects.obter_contas_a_receber_id(idContasAReceber)

	except:
		return HttpResponse("Erro ao buscar Conta a Receber")

	dados = {'contasAReceber': contasAReceber}
	return render(request, 'contasAReceber/deletar.html', dados)

@csrf_exempt
def deletar_forma_pagamento_recebimento(request, idFormaPagamentoRecebimento):
	try:
		formaPagamentoRecebimento = FormaPagamentoRecebimento.objects.obter_forma_pagamento_recebimento_id(idFormaPagamentoRecebimento)

	except:
		return HttpResponse("Erro ao buscar Forma de Pagamento / Recebimento")

	dados = {'formaPagamentoRecebimento': formaPagamentoRecebimento}
	return render(request, 'formaPagamentoRecebimento/deletar.html', dados)

@csrf_exempt
def deletar_classificacao_contas_a_receber(request, idClassificacaoContasAReceber):
	try:
		classificacaoClassificacaoContasAReceber = ClassificacaoContasAReceber.objects.obter_classificacao_contas_a_receber_id(idClassificacaoContasAReceber)

	except:
		return HttpResponse("Erro ao buscar Classificação de Contas a Receber")

	dados = {'classificacaoClassificacaoContasAReceber': classificacaoClassificacaoContasAReceber}
	return render(request, 'classificacaoClassificacaoContasAReceber/deletar.html', dados)

@csrf_exempt
def deletar_classificacao_contas_a_pagar(request, idClassificacaoContasAPagar):
	try:
		classificacaoClassificacaoContasAPagar = ClassificacaoContasAPagar.objects.obter_classificacao_contas_a_pagar_id(idClassificacaoContasAPagar)

	except:
		return HttpResponse("Erro ao buscar Classificação de Contas a Pagar")

	dados = {'classificacaoClassificacaoContasAPagar': classificacaoClassificacaoContasAPagar}
	return render(request, 'classificacaoClassificacaoContasAPagar/deletar.html', dados)



@csrf_exempt
def listar_contas_a_pagar(request):
	try:
		contasAPagarList = ContasAPagar.objects.obter_todas_contas_a_pagar()

	except:
		return HttpResponse("Erro ao buscar Contas A Pagar")

	dados = {'contasAPagarList': contasAPagarList}
	return render(request, 'contasAPagar/listar.html', dados)

@csrf_exempt
def listar_contas_a_receber(request):
	try:
		contasAReceberList = ContasAReceber.objects.obter_todas_contas_a_receber()

	except:
		return HttpResponse("Erro ao buscar Contas a Receber")

	dados = {'contasAReceberList': contasAReceberList}
	return render(request, 'contasAReceber/listar.html', dados)

@csrf_exempt
def listar_forma_pagamento_recebimento(request):
	try:
		formaPagamentoRecebimentoList = FormaPagamentoRecebimento.objects.obter_todas_forma_pagamento_recebimento()

	except:
		return HttpResponse("Erro ao buscar Formas de Pagamento / Recebimento")

	dados = {'formaPagamentoRecebimentoList': formaPagamentoRecebimentoList}
	return render(request, 'formaPagamentoRecebimento/listar.html', dados)

@csrf_exempt
def listar_classificacao_contas_a_receber(request):
	try:
		classificacaoClassificacaoContasAReceberList = ClassificacaoContasAReceber.objects.obter_todas_classificacao_contas_a_receber()

	except:
		return HttpResponse("Erro ao buscar Classificações de Contas a Receber")

	dados = {'classificacaoClassificacaoContasAReceberList': classificacaoClassificacaoContasAReceberList}
	return render(request, 'classificacaoClassificacaoContasAReceber/listar.html', dados)

@csrf_exempt
def listar_classificacao_contas_a_pagar(request):
	try:
		classificacaoClassificacaoContasAPagarList = ClassificacaoContasAPagar.objects.obter_todas_classificacao_contas_a_pagar()

	except:
		return HttpResponse("Erro ao buscar Classificação de Contas a Pagar")

	dados = {'classificacaoClassificacaoContasAPagarList': classificacaoClassificacaoContasAPagarList}
	return render(request, 'classificacaoClassificacaoContasAPagar/listar.html', dados)


