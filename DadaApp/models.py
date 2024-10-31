from django.db import models

# Create your models here.

class CapOrder(models.Model):
    PS = models.CharField(max_length=20, unique=True)
    ps_date = models.DateField(blank=True, null=True)
    SST10 = models.CharField(blank=True, null=True)
    style = models.CharField(max_length=20, blank=True, null=True)
    byr_po = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    byr = models.CharField(max_length=50, blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    cap_item = models.CharField(max_length=20, blank=True, null=True)
    cap_type = models.CharField(max_length=20, blank=True, null=True)
    ship_via = models.CharField(max_length=10, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    final_destination = models.CharField(max_length=50, blank=True, null=True)
    embroidery = models.CharField(max_length=50, default='None', blank=True, null=True)
    washing_method = models.CharField(max_length=50, blank=True, null=True)
    c_pattern = models.CharField(max_length=20, blank=True, null=True)
    v_pattern = models.CharField(max_length=20, blank=True, null=True)
    eyelet_number = models.IntegerField(blank=True, null=True)
    eyelet_material = models.CharField(max_length=20, blank=True, null=True)
    c_cutter = models.CharField(max_length=20, blank=True, null=True)
    v_cutter = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    f_mold = models.CharField(max_length=50, blank=True, null=True)
    b_mold = models.CharField(max_length=50, blank=True, null=True)
    visor_rows = models.IntegerField(blank=True, null=True)
    extra_stitch_rows = models.IntegerField(blank=True, null=True)
    first_row_from_brim = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    distance_from_front_end = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    packing = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'cap_orders'
        ordering = ['ps_date']

    def __str__(self):
        return f"{self.PS} - {self.style} - {self.quantity} PCS"



class CapOrderImage(models.Model):
    cap_order = models.ForeignKey(CapOrder, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cap_order_images/')  # Specify the upload directory