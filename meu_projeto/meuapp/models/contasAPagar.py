from django.db import models
from . import ClassificacaoContasAPagar
from . import FormaPagamentoRecebimento

class ContasAPagarManager(models.Manager):
    def obter_contas_a_pagar_id(self, idContasAPagar):
        return self.get(id=idContasAPagar)

    def obter_todas_contas_a_pagar(self):
        return self.all()

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



