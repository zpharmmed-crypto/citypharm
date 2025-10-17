from django.db import models

def upload_to_branches(instance, filename):
    return f"branches/{instance.name}/{filename}"

def upload_to_employees(instance, filename):
    return f"employees/{instance.branch.name}/{instance.full_name}/{filename}"

class Branch(models.Model):
    name = models.CharField("Название филиала", max_length=255)
    address = models.CharField("Адрес", max_length=255, blank=True, null=True)
    cadastral_doc = models.FileField("Кадастр", upload_to=upload_to_branches, blank=True, null=True)
    rent_contract = models.FileField("Договор аренды", upload_to=upload_to_branches, blank=True, null=True)
    license = models.FileField("Лицензия", upload_to=upload_to_branches, blank=True, null=True)
    guvohnoma = models.FileField("Гувохнома", upload_to=upload_to_branches, blank=True, null=True)
    gpp_certificate = models.FileField("GPP сертификат", upload_to=upload_to_branches, blank=True, null=True)
    sop_doc = models.FileField("СОП", upload_to=upload_to_branches, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="employees", verbose_name="Филиал")
    full_name = models.CharField("ФИО сотрудника", max_length=255)
    position = models.CharField("Должность", max_length=255, blank=True, null=True)
    order_doc = models.FileField("Приказ", upload_to=upload_to_employees, blank=True, null=True)
    meh_doc = models.FileField("Мехнат шартнома", upload_to=upload_to_employees, blank=True, null=True)
    instruction_doc = models.FileField("Должностная инструкция", upload_to=upload_to_employees, blank=True, null=True)
    med_book = models.FileField("Мед книжка", upload_to=upload_to_employees, blank=True, null=True)
    gpp_certificate = models.FileField("GPP сертификат", upload_to=upload_to_employees, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.branch.name})"
