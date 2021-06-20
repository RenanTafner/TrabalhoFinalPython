from django.db import models

class ClassificacaoContasAReceberManager(models.Manager):
    def obter_classificacao_contas_a_receber_id(self, idClassificacaoContasAReceber):
        return self.get(id=idClassificacaoContasAReceber)

    def obter_todas_classificacao_contas_a_receber(self):
        return self.all()

class ClassificacaoContasAReceber(models.Model):
    descricaoClassificacao = models.CharField(max_length=200,null=False)

    objects = ClassificacaoContasAReceberManager()
