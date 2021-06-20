from django.db import models

class ClassificacaoContasAPagarManager(models.Manager):
    def obter_classificacao_contas_a_pagar_id(self, idClassificacaoContasAPagar):
        return self.get(id=idClassificacaoContasAPagar)

    def obter_todas_classificacao_contas_a_pagar(self):
        return self.all()

class ClassificacaoContasAPagar(models.Model):
    descricaoClassificacao = models.CharField(max_length=200,null=False)

    objects = ClassificacaoContasAPagarManager()
