from rest_framework import serializers
from .models.classificacaoContasAPagar import ClassificacaoContasAPagar
from .models.classificacaoContasAReceber import ClassificacaoContasAReceber
from .models.contasAPagar import ContasAPagar
from .models.contasAReceber import ContasAReceber
from .models.formaPagamentoRecebimento import FormaPagamentoRecebimento


class ClassificacaoContasAPagarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassificacaoContasAPagar
        fields = ('id','descricaoClassificacao')

class ClassificacaoContasAReceberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassificacaoContasAReceber
        fields = ('id','descricaoClassificacao')
       
class ContasAPagarSerializer(serializers.HyperlinkedModelSerializer):

       class Meta:
        model = ContasAPagar
        fields = ('id','dataVencimento', 'dataPagamento', 'valor', 'descricaoConta', 'situacao', 'formaPagamento', 'classificacaoContasAPagar')

class ContasAReceberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContasAReceber
        fields = ('id','dataExpectativa', 'dataRecebimento', 'valor', 'descricaoConta', 'situacao', 'formaPagamento', 'classificacaoContasAReceber')
        
class FormaPagamentoRecebimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormaPagamentoRecebimento
        fields = ('id','descricaoFormaPagamentoRecebimento')
        
        