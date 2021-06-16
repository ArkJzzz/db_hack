import random

from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation


def fix_marks(schoolkid):
    Mark.objects.filter(
            schoolkid=schoolkid, 
            points__in=[2, 3],
        ).update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, subject_title):
    commendation_texts = [
        'Молодец!'
        'Отлично!',
        'Хорошо!',  
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    lessons = Lesson.objects.filter(
            year_of_study=6, 
            group_letter='А', 
            subject__title=subject_title,
        ).order_by('?')
    if not lessons:
        return print('Предмет не найден, проверьте правильность написания и повторите запрос')
    
    lesson = lessons.first()
    Commendation.objects.create(
            text=random.choice(commendation_texts),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,
        )


def find_schoolkid(name):
    try: 
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько учеников, уточните запрос')
    except Schoolkid.DoesNotExist:
        print('Ученика с таким именем не найдено, уточните запрос')


if __name__ == '__main__':
    print('Этот скрипт не предназначен для запуска напрямую')
