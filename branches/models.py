from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название филиала")
    cadastral_file = models.FileField(upload_to='branches/cadastral/', blank=True, null=True)
    rent_contract = models.FileField(upload_to='branches/rent_contracts/', blank=True, null=True)
    license = models.FileField(upload_to='branches/licenses/', blank=True, null=True)
    guvohnoma = models.FileField(upload_to='branches/guvohnoma/', blank=True, null=True)
    gpp_certificate = models.FileField(upload_to='branches/gpp_certificates/', blank=True, null=True)
    sop = models.FileField(upload_to='branches/sop/', blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='employees', verbose_name="Филиал")
    full_name = models.CharField(max_length=200, verbose_name="ФИО сотрудника")
    order_file = models.FileField(upload_to='employees/orders/', blank=True, null=True)
    labor_contract = models.FileField(upload_to='employees/labor_contracts/', blank=True, null=True)
    job_instruction = models.FileField(upload_to='employees/job_instructions/', blank=True, null=True)
    medical_book = models.FileField(upload_to='employees/medical_books/', blank=True, null=True)
    gpp_certificate = models.FileField(upload_to='employees/gpp_certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.branch.name})"

