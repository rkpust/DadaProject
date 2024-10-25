from django.db import models

# Create your models here.

class CapOrder(models.Model):
    ps_number = models.CharField(max_length=20)
    ps_date = models.DateField(null=True)
    style = models.CharField(max_length=20, null=True)
    byr_po_number = models.CharField(max_length=20, null=True)
    quantity = models.IntegerField(null=True)
    byr = models.CharField(max_length=50, null=True)
    ship_date = models.DateField(null=True)
    cap_item = models.CharField(max_length=20, null=True)
    cap_type = models.CharField(max_length=20, null=True)
    ship_via = models.CharField(max_length=10, null=True)
    destination = models.CharField(max_length=50, null=True)
    final_destination = models.CharField(max_length=50, null=True)
    embroidery = models.CharField(max_length=50, default='None', null=True)
    washing_method = models.CharField(max_length=50, null=True)
    c_pattern = models.CharField(max_length=20, null=True)
    v_pattern = models.CharField(max_length=20, null=True)
    eyelet_number = models.IntegerField(null=True)
    eyelet_material = models.CharField(max_length=20, null=True)
    c_cutter = models.CharField(max_length=20, null=True)
    v_cutter = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=50, null=True)
    f_mold = models.CharField(max_length=50, null=True)
    b_mold = models.CharField(max_length=50, null=True)
    visor_rows = models.IntegerField(null=True)
    extra_stitch_rows = models.IntegerField(null=True)
    first_row_from_brim = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    distance_from_front_end = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    packing = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.style} - {self.quantity} PCS"

