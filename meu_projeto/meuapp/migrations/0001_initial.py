# Generated by Django 3.2.4 on 2021-06-24 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoContasAPagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoClassificacao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificacaoContasAReceber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoClassificacao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamentoRecebimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoFormaPagamentoRecebimento', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ContasAReceber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataExpectativa', models.DateField()),
                ('dataRecebimento', models.DateField(null=True)),
                ('valor', models.FloatField()),
                ('descricaoConta', models.CharField(max_length=200)),
                ('situacao', models.CharField(choices=[('RO', 'Recebido'), ('RR', 'A Receber')], default='PR', max_length=2)),
                ('classificacaoContasAPagar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.classificacaocontasareceber')),
                ('formaPagamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meuapp.formapagamentorecebimento')),
            ],
        ),
        migrations.CreateModel(
            name='ContasAPagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateField()),
                ('dataPagamento', models.DateField(null=True)),
                ('valor', models.FloatField()),
                ('descricaoConta', models.CharField(max_length=200)),
                ('situacao', models.CharField(choices=[('PO', 'Pago'), ('PR', 'A Pagar')], default='PR', max_length=2)),
                ('classificacaoContasAPagar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.classificacaocontasapagar')),
                ('formaPagamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meuapp.formapagamentorecebimento')),
            ],
        ),
    ]