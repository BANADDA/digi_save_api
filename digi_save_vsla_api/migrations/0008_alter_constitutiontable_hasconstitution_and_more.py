# Generated by Django 4.2.7 on 2023-11-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_save_vsla_api', '0007_alter_groupprofile_countryoforigin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constitutiontable',
            name='hasConstitution',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='interestMethod',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='interestRate',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='loanTerms',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='maxLoanAmount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='maxSharesPerMember',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='minSharesRequired',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='offersLoans',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='registrationFee',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='shareValue',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='usesGroupShares',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
