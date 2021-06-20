from django.db import models
from . import ClassificacaoContasAReceber
from . import FormaPagamentoRecebimento

class ContasAReceberManager(models.Manager):
    def obter_contas_a_receber_id(self, idContasAReceber):
        return self.get(id=idContasAReceber)
    
    def obter_todas_contas_a_receber(self):
        return self.all()

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

    classificacaoContasAPagar = models.ForeignKey(ClassificacaoContasAReceber,
							on_delete=models.CASCADE,
							null=False)
    formaPagamento = models.ForeignKey(FormaPagamentoRecebimento,
							on_delete=models.CASCADE,
							null=True)

    objects = ContasAReceberManager()




