# Generated by Django 5.2.3 on 2025-07-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do produto.', max_length=200)),
                ('descricao', models.TextField(blank=True, help_text='Descrição detalhada do produto.', null=True)),
                ('quantidade', models.IntegerField(default=0, help_text='Quantidade atual em estoque.')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, help_text='Preço unitário do produto.', max_digits=10, null=True)),
                ('data_entrada', models.DateTimeField(auto_now_add=True, help_text='Data em que o produto foi registrado.')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, help_text='Última vez que as informações do produto foram atualizadas.')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
    ]
