<p align="center">
    <a href="https://djangochannel.com" target="_blank" rel="noopener noreferrer">
        <img width="100" src="docs/_static/logo.png" title="djangochannel">
    </a>
</p>

<h2 align="center">Django Channel</h2>

[![Join the chat at https://gitter.im/djangochannel/community](https://badges.gitter.im/djangochannel/community.svg)](https://gitter.im/djangochannel/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/DJWOMS/djangochannel.svg?branch=master)](https://travis-ci.org/DJWOMS/djangochannel)
[![Coverage Status](https://coveralls.io/repos/github/DJWOMS/djangochannel/badge.svg?branch=master)](https://coveralls.io/github/DJWOMS/djangochannel?branch=master)

[Сайт](https://djangochannel.com)

### Описание проекта:
Проект призван помочь людям в обучении программированию, веб разработке и английскому языку.
В обучении и понимании материала поможет сообщество и личный преподаватель.
Вы можете найти себе товарища или группу людей для совместного обучения и выполнения задач.
Отслеживайте личный прогресс обучения и получайте награды за любую активность.

- Геймификация позволяет повысить вовлеченность в процесс обучения 
- Задания которые можно выполнять лично и группами
- Онлайн курсы это интерактивный учебник, который содержит статьи, видеоматериалы, тесты, примеры и проекты.
- Статьи 
- Форум
- Сообщества
- Тесты

### Инструменты разработки

**Стек:**
- Python >= 3.7
- Django >= 2
- PostgreSQL
- Angular

**Как работаем:**
- Все предложения и найденные ошибки добавляются в виде Issues на GitHub всеми желающими
- Обсуждаем фичи в чатах Slack и Telegram
- Над вехами работаем в рамках Trello
- Макеты разрабатываются в Figma
- Пулреквесты по таскам предлагаются всеми желающими, в комментариях к таскам люди пишут что начали делать и когда планируют закончить.
- Пул реквесты обсуждаются командой и сливаются в мастер.

**Ссылки**:
- [Сайт](https://djangochannel.com)
- [Канал Youtube](https://www.youtube.com/channel/UC_hPYclmFCIENpMUHpPY8FQ?view_as=subscriber)
- [Доска в Trello](https://trello.com/b/EZzcxWb1/djangochannel)
- [Ошибки/Вопросы/Предложения](https://github.com/DJWOMS/djangochannel/issues)
- [Задачи GitHub](https://github.com/DJWOMS/djangochannel/projects/1)
- [Дизайн экранов в Figma](https://www.figma.com/file/NuuLxaWVtab9X3GjiieTT3/DS-groups?node-id=94%3A80)
- [Рабочий чат Slack](https://goo-gl.su/DemLTTGJ)
- [Telegram](https://t.me/trueDjangoChannel)
- [Группа в VK](https://vk.com/djangochannel)
- [Поддержать проект](https://donatepay.ru/don/186076)

**Как стать членом команды**:
- Иметь время на проект
- Иметь мотивацию сделать Мир лучше
- Иметь необходимые навыки (если вы ничего не умеете, можно помогать с пиаром)
- Прочитать манифест (Вы его читаете=)
- Сделать пулл реквест, который будет смержен в основной проект и пообщаться с текущей командой (голос/переписка)
- [Прочитать и создать свои Issues](https://github.com/DJWOMS/djangochannel/issues) (вопросы, предложения)

*Создать Issues можно и тем, кто не хочет работать с нами над проектом, а просто хочет задать вопросы и дать нам совет*

## Разработка

##### 1) Сделать форк репозитория и поставить звездочку)

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 4) Активировать виртуальное окружение

##### 5) В папке `DS` файл `local_settings.py-example` переименовать в `local_settings.py` и прописать конект к базе

##### 6) Устанавливить зависимости:

    pip install -r req.txt

##### 7) Выполнить команду для выполнения миграций

    python manage.py deploy
    
##### 8) Создать суперпользователя

    python manage.py createsuperuser
    
##### 9) Запустить сервер

    python manage.py runserver


### Синхронизировать с основной веткой репозитория проекта, когда она изменилась:


##### 1. Добавить удалённый репозиторий

    git remote add название_ветки_на_локальной_машине https://github.com/DJWOMS/djangochannel

##### 2. Проверить добавилась ли ссылка

    git remote -v

##### 3. Синхронизируем с основной веткой на своей машине

    git pull название_ветки_на_локальной_машине develop

##### 4. Внесенные изменения добавляем в ветку в своем репозитории и пушим в свой удаленный репозиторий

    git add .

    git commit -m "четкое_и_понятное_описание_проделанной_работы""

    git push

##### 5. Сделать пулл реквест в основной ветке Django Channel в develop branch

##### Разработка осуществляется через ветку develop

## Команда

[DJWOMS](https://github.com/DJWOMS) 

## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2019-present, DJWOMS - Omelchenko Michael



