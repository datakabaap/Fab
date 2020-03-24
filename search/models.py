from __future__ import unicode_literals
from pymongo import *
from mongoengine import *
from djongo import models
import django_filters



class Search(models.Model):
    id = models.CharField
    For_Sale = models.CharField(max_length=500, null=True)
    Old_Catalog = models.CharField(max_length=500, null=True)
    Final_Catalog = models.CharField(max_length=500, null=True)
    Peptide = models.CharField(max_length=500, null=True)
    Target_Name = models.CharField(max_length=500, null=True)
    Accession_No = models.CharField(max_length=500, null=True)
    Synonym = models.CharField(max_length=500, null=True)
    MW = models.CharField(max_length=500, null=True)
    CR_Theoritical = models.CharField(max_length=500, null=True)
    CR_Experimental = models.CharField(max_length=500, null=True)
    Category = models.CharField(max_length=500, null=True)
    Peptide_Sequence = models.CharField(max_length=500, null=True)
    Peptide_Position = models.CharField(max_length=500, null=True)
    Peptide_Lot_No = models.CharField(max_length=500, null=True)
    Host = models.CharField(max_length=500, null=True)
    FREEZER_BOX = models.CharField(max_length=500, null=True)
    Peptide_Used = models.CharField(max_length=500, null=True)
    ORIGIN = models.CharField(max_length=500, null=True)
    Retrnd_Conj_F_No = models.CharField(max_length=500, null=True)
    No_Tubes = models.CharField(max_length=500, null=True)
    Rabbit_1 = models.CharField(max_length=500, null=True)
    Rabbit_2 = models.CharField(max_length=500, null=True)
    EXTD_Rabbit_1 = models.CharField(max_length=500, null=True)
    EXTD_Rabbit_2 = models.CharField(max_length=500, null=True)
    SRM_Rb_1 = models.CharField(max_length=500, null=True)
    SRM_Rb_2 = models.CharField(max_length=500, null=True)
    No_Bottle_Rb1 = models.CharField(max_length=500, null=True)
    No_Bottle_Rb2 = models.CharField(max_length=500, null=True)
    SRM_BOX_No = models.CharField(max_length=500, null=True)
    SRM_FRZR_No = models.CharField(max_length=500, null=True)
    TB_BOX_No = models.CharField(max_length=500, null=True)
    TB_FRZR_No = models.CharField(max_length=500, null=True)
    NOT_in_Location = models.CharField(max_length=500, null=True)
    COMNT_n_LotNo = models.CharField(max_length=500, null=True)
    SPCL_Notes = models.CharField(max_length=500, null=True)
    PURFN_PROTN_A_RABT_1 = models.CharField(max_length=500, null=True)
    PURFN_PROTN_A_RABT_2 = models.CharField(max_length=500, null=True)
    AFFNTY_PURFN_RABBT_1 = models.CharField(max_length=500, null=True)
    AFFNTY_PURFN_RABBT_2 = models.CharField(max_length=500, null=True)
    ANTBDY_PROTN_A_RABBT_1 = models.CharField(max_length=500, null=True)
    ANTBDY_PROTN_A_RABBT_1_LOT_No = models.CharField(max_length=500, null=True)
    ANTBDY_PROTN_A_RABBT_2 = models.CharField(max_length=500, null=True)
    ANTBDY_PROTN_A_RABBT_2_LOT_No = models.CharField(max_length=500, null=True)
    AFFINITY_PURIFIED_RABBIT_1 = models.CharField(max_length=500, null=True)
    AFFINITY_PURIFIED_RABBIT_1_LOT_No = models.CharField(max_length=500, null=True)
    AFFINITY_PURIFIED_RABBIT_2 = models.CharField(max_length=500, null=True)
    AFFINITY_PURIFIED_RABBIT_2_LOT_No = models.CharField(max_length=500, null=True)
    PRODUCT_LOCATION_BOX = models.CharField(max_length=500, null=True)
    PRODUCT_LOCATION_FRZR = models.CharField(max_length=500, null=True)
    PRODUCT_LOCATION_2015_18_INVTRY = models.CharField(max_length=500, null=True)
    PRODUCT_LOCATION_SMPLR_PACK = models.CharField(max_length=500, null=True)
    CNJGTS_FITC_SMPL_PACK = models.CharField(max_length=500, null=True)
    CNJGTS_FITC_RABBIT_No = models.CharField(max_length=500, null=True)
    CNJGTS_FITC_TUBES_LOCTN_1 = models.CharField(max_length=500, null=True)
    CNJGTS_FITC_TUBES_LOCTN_2 = models.CharField(max_length=500, null=True)
    CNJGTS_FITC_TUBES_DATE = models.CharField(max_length=500, null=True)
    CNJGTS_BIOTIN_LOCTN = models.CharField(max_length=500, null=True)
    CNJGTS_BIOTIN_LOCTN_FITC_Biotin = models.CharField(max_length=500, null=True)
    WB_CONTRL_TUBES_No = models.CharField(max_length=500, null=True)
    WB_CONTRL_LOCTN_BOX_FRZR = models.CharField(max_length=500, null=True)
    COLMN_NAME =models.CharField(max_length=500, null=True)
    COLMN_LOCTN_BOX_No = models.CharField(max_length=500, null=True)
    COLMN_DATE = models.CharField(max_length=500, null=True)
    REMARKS = models.CharField(max_length=500, null=True)
    ESP_NOTES = models.CharField(max_length=500, null=True)
    LOT_No = models.CharField(max_length=500, null=True)
    ALL_PRDCT_LOT_No_2 = models.CharField(max_length=500, null=True)
    PRDTS_3 = models.CharField(max_length=500, null=True)
    Column49 = models.CharField(max_length=500, null=True)

    def __str__(self, *args, **kwargs):
        return self.Old_Catalog






























































