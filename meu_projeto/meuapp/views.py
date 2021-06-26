from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import viewsets
from .serializers import ClassificacaoContasAPagarSerializer, ClassificacaoContasAReceberSerializer, ContasAPagarSerializer, ContasAReceberSerializer, FormaPagamentoRecebimentoSerializer
from .models.classificacaoContasAPagar import ClassificacaoContasAPagar
from .models.classificacaoContasAReceber import ClassificacaoContasAReceber
from .models.contasAPagar import ContasAPagar
from .models.contasAReceber import ContasAReceber
from .models.formaPagamentoRecebimento import FormaPagamentoRecebimento

def relatorio(request):
	
	dados = {'pessoas': {id:1},
		'msg': "Esta é uma mensagem fora do modelo"}
	
	return render(request, 'relatorio/index.html', dados)

def relpagar(request, dtInit, dtEnd):
	print(dtInit,dtEnd)
	contas = ContasAPagar.objects.filter(dataVencimento__gte=dtInit,dataVencimento__lte=dtEnd)
	contas_json = []
	for c in contas:
		pdic = {
			'id': c.id,
			'dataVencimento': c.dataVencimento,
			'dataPagamento': c.dataPagamento,
			'valor': c.valor,
			'descricaoConta': c.descricaoConta,
			'situacao': c.situacao,
			'classificacaoContasAPagar': c.classificacaoContasAPagar,
			'formaPagamento': c.formaPagamento
		}

		if c.classificacaoContasAPagar:
        	 pdic['classificacaoContasAPagar'] = model_to_dict(c.classificacaoContasAPagar)

		if c.formaPagamento:
        	 pdic['formaPagamento']	= model_to_dict(c.formaPagamento)
	    
		contas_json.append(pdic)
    
	
	payload = {
		'pagar': contas_json
	}

	return JsonResponse(payload)


def relreceber(request, dtInit, dtEnd):
	contas = ContasAReceber.objects.filter(dataExpectativa__gte=dtInit,dataExpectativa__lte=dtEnd)
	contas_json = []
	for c in contas:
		pdic = {
				'id': c.id,
				'dataExpectativa': c.dataExpectativa,
				'dataRecebimento': c.dataRecebimento,
				'valor': c.valor,
				'descricaoConta': c.descricaoConta,
				'situacao': c.situacao,
				'classificacaoContasAReceber': c.classificacaoContasAReceber,
				'formaPagamento': c.formaPagamento
		}
		if c.classificacaoContasAReceber:
        	 pdic['classificacaoContasAReceber'] = model_to_dict(c.classificacaoContasAReceber)

		if c.formaPagamento:
        	 pdic['formaPagamento']	= model_to_dict(c.formaPagamento)
		
		contas_json.append(pdic)
    
	
	payload = {
		'receber': contas_json
	}

	return JsonResponse(payload)

class ClassificacaoContasAPagarViewSet(viewsets.ModelViewSet):
	queryset = ClassificacaoContasAPagar.objects.all().order_by('descricaoClassificacao')
	serializer_class = ClassificacaoContasAPagarSerializer

class ClassificacaoContasAReceberViewSet(viewsets.ModelViewSet):
	queryset = ClassificacaoContasAReceber.objects.all().order_by('descricaoClassificacao')
	serializer_class = ClassificacaoContasAReceberSerializer

class ContasAPagarViewSet(viewsets.ModelViewSet):
	queryset = ContasAPagar.objects.all().order_by('descricaoConta')
	serializer_class = ContasAPagarSerializer

class ContasAReceberViewSet(viewsets.ModelViewSet):
	queryset = ContasAReceber.objects.all().order_by('descricaoConta')
	serializer_class = ContasAReceberSerializer

class FormaPagamentoRecebimentoViewSet(viewsets.ModelViewSet):
	queryset = FormaPagamentoRecebimento.objects.all().order_by('descricaoFormaPagamentoRecebimento')
	serializer_class = FormaPagamentoRecebimentoSerializer
	

