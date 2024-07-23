from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    number = models.IntegerField(unique=True, verbose_name='Номер телефона')
    insurance_policy_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='номера страхового полиса')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    address = models.TextField(verbose_name='Адрес')
    passport_number = models.CharField(max_length=10, verbose_name='Номер пасспорта')
    passport_series = models.CharField(max_length=10, verbose_name='Серия пасспорта')

    class Meta:
        verbose_name_plural = 'Пациенты'
        verbose_name = 'Пациент'
        ordering = ['-creation_date']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

class Ward(models.Model):
    floor = models.IntegerField(verbose_name='Этаж')
    number = models.CharField(max_length=50, verbose_name='Номер')
    capacity = models.IntegerField(verbose_name='Вмещаемое количество больных')

    class Meta:
        verbose_name_plural = 'Палаты'
        verbose_name = 'Палата'
        ordering = ['-number']

    def __str__(self):
        return f"Floor {self.floor} - Ward {self.number}"

class Stay(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')
    admission_date = models.DateField(verbose_name='Дата поступления')
    diagnosis = models.TextField(verbose_name='Диагноз')
    discharge_date = models.DateField(verbose_name='Дата выписки')
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, verbose_name='Палата')

    class Meta:
        verbose_name_plural = 'Списки амбулаторных периодов пребывания пациентов в больнице'
        verbose_name = 'Список амбулаторных периодов пребывания пациентов в больнице'
        ordering = ['-ward']

    def __str__(self):
        return f"{self.patient} - {self.diagnosis} from {self.admission_date} to {self.discharge_date}"


