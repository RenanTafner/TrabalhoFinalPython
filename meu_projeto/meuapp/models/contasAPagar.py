from django.db import models
from . import ClassificacaoContasAPagar
from . import FormaPagamentoRecebimento
from django.db.models import Sum

class ContasAPagarManager(models.Manager):
    def obter_contas_a_pagar_id(self, idContasAPagar):
        return self.get(id=idContasAPagar)

    def obter_todas_contas_a_pagar(self):
        return self.all()

    def obter_soma_prevista_mes(self, month):
        soma_prevista_mes = float(ContasAPagar.objects.filter(dataVencimento__month=month, situacao=False).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma_prevista_mes

    def obter_soma_realizada_mes(self, month):
        soma_realizada_mes = float(ContasAPagar.objects.filter(dataVencimento__month=month, situacao=True).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma_realizada_mes

    def obter_soma_total_mes(self, month):
        soma_total_mes = float(ContasAPagar.objects.filter(dataVencimento__month=month).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma_total_mes

    def obter_gastos_por_classificacao(self, month):

        gastos_object = []

        for id_classificacao_contas_a_pagar in range (1,30):
            try:
                soma_total = float(ContasAPagar.objects.filter(classificacaoContasAPagar=id_classificacao_contas_a_pagar, dataVencimento__month=month).aggregate(Sum('valor'))['valor__sum'] or 0)
                gasto_object = {
                'soma_total' : soma_total,
                'classificacao' : ClassificacaoContasAPagar.objects.obter_classificacao_contas_a_pagar_id(id_classificacao_contas_a_pagar)
                }
                if soma_total > 0:
                    gastos_object.append(gasto_object)
            except:
                pass
        return gastos_object

class ContasAPagar(models.Model):
    SITUACAO_CHOICES = [('PO','Pago'),
					('PR','A Pagar')]
                

    dataVencimento = models.DateField(null=False)

    dataPagamento = models.DateField(null=True)

    valor = models.FloatField(null=False)

    descricaoConta = models.CharField(max_length=200,null=False)

    situacao = models.CharField(max_length=2,
			choices=SITUACAO_CHOICES,
			default='PR')

    classificacaoContasAPagar = models.ForeignKey(ClassificacaoContasAPagar,on_delete=models.CASCADE,null=True)
    formaPagamento = models.ForeignKey(FormaPagamentoRecebimento,on_delete=models.CASCADE,null=True)

    objects = ContasAPagarManager()



