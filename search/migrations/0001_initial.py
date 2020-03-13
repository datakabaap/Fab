# Generated by Django 2.2.9 on 2020-02-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('For_Sale', models.CharField(max_length=500)),
                ('Old_Catalog', models.CharField(max_length=500)),
                ('Final_Catalog', models.CharField(max_length=500)),
                ('Peptide', models.CharField(max_length=500)),
                ('Target_Name', models.CharField(max_length=500)),
                ('Accession_No', models.CharField(max_length=500)),
                ('Synonym', models.CharField(max_length=500)),
                ('MW', models.CharField(max_length=500)),
                ('CR_Theoritical', models.CharField(max_length=500)),
                ('CR_Experimental', models.CharField(max_length=500)),
                ('Category', models.CharField(max_length=500)),
                ('Peptide_Sequence', models.CharField(max_length=500)),
                ('Peptide_Position', models.CharField(max_length=500)),
                ('Peptide_Lot_No', models.CharField(max_length=500)),
                ('Host', models.CharField(max_length=500)),
                ('FREEZER_BOX', models.CharField(max_length=500)),
                ('Peptide_Used', models.CharField(max_length=500)),
                ('ORIGIN', models.CharField(max_length=500)),
                ('Retrnd_Conj_F_No', models.CharField(max_length=500)),
                ('No_Tubes', models.CharField(max_length=500)),
                ('Rabbit_1', models.CharField(max_length=500)),
                ('Rabbit_2', models.CharField(max_length=500)),
                ('EXTD_Rabbit_1', models.CharField(max_length=500)),
                ('EXTD_Rabbit_2', models.CharField(max_length=500)),
                ('SRM_Rb_1', models.CharField(max_length=500)),
                ('No_Bottle_Rb1', models.CharField(max_length=500)),
                ('No_Bottle_Rb2', models.CharField(max_length=500)),
                ('SRM_BOX_No', models.CharField(max_length=500)),
                ('SRM_FRZR_No', models.CharField(max_length=500)),
                ('TB_BOX_No', models.CharField(max_length=500)),
                ('TB_FRZR_No', models.CharField(max_length=500)),
                ('NOT_in_Location', models.CharField(max_length=500)),
                ('COMNT_n_LotNo', models.CharField(max_length=500)),
                ('SPCL_Notes', models.CharField(max_length=500)),
                ('PURFN_PROTN_A_RABT_1', models.CharField(max_length=500)),
                ('PURFN_PROTN_A_RABT_2', models.CharField(max_length=500)),
                ('AFFNTY_PURFN_RABBT_1', models.CharField(max_length=500)),
                ('AFFNTY_PURFN_RABBT_2', models.CharField(max_length=500)),
                ('ANTBDY_PROTN_A_RABBT_1', models.CharField(max_length=500)),
                ('ANTBDY_PROTN_A_RABBT_1_LOT_No', models.CharField(max_length=500)),
                ('ANTBDY_PROTN_A_RABBT_2', models.CharField(max_length=500)),
                ('AFFINITY_PURIFIED_RABBIT_1', models.CharField(max_length=500)),
                ('AFFINITY_PURIFIED_RABBIT_1_LOT_No', models.CharField(max_length=500)),
                ('AFFINITY_PURIFIED_RABBIT_2', models.CharField(max_length=500)),
                ('AFFINITY_PURIFIED_RABBIT_2_LOT_No', models.CharField(max_length=500)),
                ('PRODUCT_LOCATION_BOX', models.CharField(max_length=500)),
                ('PRODUCT_LOCATION_FRZR', models.CharField(max_length=500)),
                ('PRODUCT_LOCATION_2015_18_INVTRY', models.CharField(max_length=500)),
                ('PRODUCT_LOCATION_SMPLR_PACK', models.CharField(max_length=500)),
                ('CNJGTS_FITC_SMPL_PACK', models.CharField(max_length=500)),
                ('CNJGTS_FITC_RABBIT_No', models.CharField(max_length=500)),
                ('CNJGTS_FITC_TUBES_LOCTN_1', models.CharField(max_length=500)),
                ('CNJGTS_FITC_TUBES_LOCTN_2', models.CharField(max_length=500)),
                ('CNJGTS_FITC_TUBES_DATE', models.CharField(max_length=500)),
                ('CNJGTS_BIOTIN_LOCTN', models.CharField(max_length=500)),
                ('CNJGTS_BIOTIN_LOCTN_FITC_Biotin', models.CharField(max_length=500)),
                ('WB_CONTRL_TUBES_No', models.CharField(max_length=500)),
                ('WB_CONTRL_LOCTN_BOX_FRZR', models.CharField(max_length=500)),
                ('COLMN_NAME', models.CharField(max_length=500)),
                ('COLMN_LOCTN_BOX_No', models.CharField(max_length=500)),
                ('COLMN_DATE', models.CharField(max_length=500)),
                ('REMARKS', models.CharField(max_length=500)),
                ('ESP_NOTES', models.CharField(max_length=500)),
                ('LOT_No', models.CharField(max_length=500)),
                ('ALL_PRDCT_LOT_No_2', models.CharField(max_length=500)),
                ('PRDTS_3', models.CharField(max_length=500)),
                ('Column49', models.CharField(max_length=500)),
            ],
        ),
    ]