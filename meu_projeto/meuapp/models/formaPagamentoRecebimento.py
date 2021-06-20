from django.db import models

class FormaPagamentoRecebimentoManager(models.Manager):
    def obter_forma_pagamento_recebimento_id(self, idFormaPagamentoRecebimento):
        return self.get(id=idFormaPagamentoRecebimento)

    def obter_todas_forma_pagamento_recebimento(self):
        return self.all()

class FormaPagamentoRecebimento(models.Model):
    descricaoFormaPagamentoRecebimento = models.CharField(max_length=200,null=False)

    objects = FormaPagamentoRecebimentoManager()