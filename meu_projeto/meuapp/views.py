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
from django.views.decorators.http import require_http_methods
import datetime

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

@require_http_methods(['GET'])
def exibir_fluxo_caixa(request):

    relatorios_meses = []

    for mes_x in range(1, 13):

        saldo_inicial = 0 if mes_x == 1 else relatorio_mes['saldo_final']       

        saldo_final = round(saldo_inicial - ContasAPagar.objects.obter_soma_total_mes(mes_x) + ContasAReceber.objects.obter_soma_total_mes(mes_x), 2)

        lucro_total = round(saldo_final - saldo_inicial, 2)

        relatorio_mes = {

            "data" : datetime.date(1900, mes_x, 1).strftime('%B'),

            "saldo_inicial" : saldo_inicial,

            "a_pagar" : {
                "soma_total_prevista": ContasAPagar.objects.obter_soma_prevista_mes(mes_x),
                "soma_total_realizada": ContasAPagar.objects.obter_soma_realizada_mes(mes_x),
                "soma_mensal": ContasAPagar.objects.obter_soma_total_mes(mes_x),
                "gastos_por_classificacao": ContasAPagar.objects.obter_gastos_por_classificacao(mes_x),
            },

            "a_receber" : {
                "soma_total_prevista": ContasAReceber.objects.obter_soma_prevista_mes(mes_x),
                "soma_total_recebida": ContasAReceber.objects.obter_soma_realizada_mes(mes_x),
                "soma_mensal": ContasAReceber.objects.obter_soma_total_mes(mes_x),
                "ganhos_por_classificacao": ContasAReceber.objects.obter_gastos_por_classificacao(mes_x),
            },

            "lucro_total": lucro_total,

			"saldo_final" : saldo_final,

        } 

        relatorios_meses.append(relatorio_mes)

    return render(request, 'relatorio/fluxo_caixa.html', {"relatorios_meses" : relatorios_meses})		

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
	

