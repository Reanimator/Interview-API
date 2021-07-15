from django.db import models
from django.utils import timezone


class Interviews(models.Model):
    """Модель для опросов"""
    name = models.CharField("Название опроса", max_length=50)
    start_date = models.DateField("Дата старта")
    end_date = models.DateField("Дата окончания")
    about = models.TextField("Описание")

    def save(self, *args, **kwargs):
        if not self.id:
            self.start_date = timezone.now()
        return super(Interviews, self).save(*args, **kwargs)


class Questions(models.Model):
    """Модель для вопросов"""
    TYPE = [
        ('text', 'ответ текстом'),
        ('1var', 'ответ с выбором одного варианта'),
        ('mvar', 'ответ с выбором нескольких вариантов'),
    ]
    interview = models.ForeignKey(Interviews, on_delete=models.CASCADE)
    question = models.TextField("Текст вопроса")
    question_type = models.CharField(
        "Тип вопроса",
        max_length=4,
        choices=TYPE,
        default='text')
    text_answer = models.TextField("Ответ текстом", blank=True)

    var_answer_1 = models.TextField(
        "Первый ответ на вопрос с выбором одного варианта", blank=True)
    var_answer_2 = models.TextField(
        "Второй ответ на вопрос с выбором одного варианта", blank=True)
    var_answer_3 = models.TextField(
        "Третий ответ на вопрос с выбором одного варианта", blank=True)
    var_answer_4 = models.TextField(
        "Четвертый ответ на вопрос с выбором одного варианта", blank=True)
    var_answer_correct = models.CharField(
        "Номер правильного ответа на вопрос",
        max_length=1,
        blank=True,
        default='0')

    mvar_answer_1 = models.TextField(
        "Первый ответ на вопрос с выбором нескольких вариантов", blank=True)
    mvar_answer_2 = models.TextField(
        "Второй ответ на вопрос с выбором нескольких вариантов", blank=True)
    mvar_answer_3 = models.TextField(
        "Третий ответ на вопрос с выбором нескольких вариантов", blank=True)
    mvar_answer_4 = models.TextField(
        "Четвертый ответ на вопрос с выбором нескольких вариантов", blank=True)
    # Хранение по принципу битового соответствия, например 0101 - правильный
    # ответ 2 и 4
    mvar_answer_correct = models.CharField(
        "Номер правильного ответа на вопрос",
        max_length=4,
        blank=True,
        default='0000')
