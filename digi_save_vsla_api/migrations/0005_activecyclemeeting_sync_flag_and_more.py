# Generated by Django 4.2.7 on 2023-11-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_save_vsla_api', '0004_alter_users_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activecyclemeeting',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='assignedpositions',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='constitutiontable',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cyclemeeting',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cycleschedules',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cyclestartmeeting',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='fines',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupcyclestatus',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupfees',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupform',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='grouplink',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupmembers',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='loanapplications',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='loandisbursement',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='loanpayments',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='loans',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='meeting',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='membershares',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='positions',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='reversedtransactions',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='savingsaccount',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='shareout',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='shares',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='social',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='socialfundapplications',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='users',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='welfareaccount',
            name='sync_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='constitutionFiles',
            field=models.BinaryField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='hasConstitution',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='offersLoans',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='selectedCollateralRequirements',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='constitutiontable',
            name='usesGroupShares',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='numberOfCycles',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='partnerID',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
