# Generated by Django 4.0.8 on 2023-09-27 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gene', '0002_gene_primary_transcript'),
        ('variant', '0004_rename_genename_genebassvariant_gene_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genebassvariant',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='variant.genebasscategory'),
        ),
        migrations.AlterField(
            model_name='genebassvariant',
            name='gene_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gene.gene'),
        ),
        migrations.AlterField(
            model_name='genebassvariant',
            name='phenocode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='variant.variantphenocode'),
        ),
    ]
