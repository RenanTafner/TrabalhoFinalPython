from django.db import models
from . import ClassificacaoContasAReceber
from . import FormaPagamentoRecebimento
from django.db.models import Sum

class ContasAReceberManager(models.Manager):
    def obter_contas_a_receber_id(self, idContasAReceber):
        return self.get(id=idContasAReceber)
    
    def obter_todas_contas_a_receber(self):
        return self.all()

    def obter_soma_prevista_mes(self, month):
        soma_prevista_mes = float(ContasAReceber.objects.filter(dataExpectativa__month=month, situacao=False).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma_prevista_mes

    def obter_soma_realizada_mes(self, month):
        soma_realizada_mes = float(ContasAReceber.objects.filter(dataExpectativa__month=month, situacao=True).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma_realizada_mes

    def obter_soma_total_mes(self, month):
        soma_total_mes = float(ContasAReceber.objects.filter(dataExpectativa__month=month).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma_total_mes

    def obter_gastos_por_classificacao(self, month):

        gastos_object = []

        for id_classificacao_contas_a_receber in range (1,30):
            try:
                soma_total = float(ContasAReceber.objects.filter(classificacaoContasAReceber=id_classificacao_contas_a_receber, dataExpectativa__month=month).aggregate(Sum('valor'))['valor__sum'] or 0)
                gasto_object = {
                'soma_total' : soma_total,
                'classificacao' : ClassificacaoContasAReceber.objects.obter_classificacao_contas_a_receber_id(id_classificacao_contas_a_receber)
                }
                if soma_total > 0:
                    gastos_object.append(gasto_object)
            except:
                pass
  
        return gastos_object


class ContasAReceber(models.Model):
    SITUACAO_CHOICES = [('RO','Recebido'),
					('RR','A Receber')]

    dataExpectativa= models.DateField(null=False)

    dataRecebimento = models.DateField(null=True)

    valor = models.FloatField(null=False)

    descricaoConta = models.CharField(max_length=200,null=False)

    situacao = models.CharField(max_length=2,
			choices=SITUACAO_CHOICES,
			default='PR')

    classificacaoContasAReceber = models.ForeignKey(ClassificacaoContasAReceber,
							on_delete=models.CASCADE,
							null=False)
    formaPagamento = models.ForeignKey(FormaPagamentoRecebimento,
							on_delete=models.CASCADE,
							null=True)

    objects = ContasAReceberManager()




