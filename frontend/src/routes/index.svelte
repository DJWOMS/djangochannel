<style>
    .preview {
        padding: 100px 0 0 0;
        background: #f1f1f1;
    }

    .paper {
        -webkit-box-shadow: 0 2px 1px -1px rgba(0, 0, 0, .2), 0 1px 1px 0 rgba(0, 0, 0, .14), 0 1px 3px 0 rgba(0, 0, 0, .12);
        box-shadow: 0 2px 1px -1px rgba(0, 0, 0, .2), 0 1px 1px 0 rgba(0, 0, 0, .14), 0 1px 3px 0 rgba(0, 0, 0, .12);
    }

    .img-preview {
        width: 100%;
    }

    .one {
        margin: -27px 0 30px -158px;
        padding: 35px 0 3px 42px;
        border: 2px solid #c1d5e1;
    }

    .one-fone {
        max-width: 794px;
        max-height: 800px;
        padding: 55px 100px 10px 35px;
        background: #fff;
    }

    .one-block {
        margin: 0 0 60px 0;
    }

    .one-h2 {
        margin: 0 0 40px 0;
    }

    .one-h3 {
        margin: -4px 0;
        font-size: 34px;
        position: relative;
        z-index: 2;
    }

    .one-h3-top {
        margin: -37px 0 0 0;
    }

    .one-p-fone {
        height: 41px;
        background: #efe16b;
        width: 150px;
        margin: -15px 0 0 -45px;
    }

    .one-p-fone-two {
        background: #c1d5e1;
    }

    .headline-3-text {
        color: #465d81;
        margin: -32px 0 20px 0;
        font-size: 22px;
        line-height: 24px;
    }

    .one-p-text {
        font-size: 16px;
        line-height: 25px;
    }

    .slogan {
        text-align: center;
        font-size: 22px;
    }

    .number {
        padding: 8px 18px;
        border: 1px solid #fdd835;
        width: 50px;
        height: 50px;
        border-radius: 100%;
        font-size: 22px;
        margin: 8px;
        cursor: pointer;
    }

    .bin {
        padding: 8px 13px;
        cursor: pointer;
    }

    .bin-eggs {
        padding: 8px 18px;
    }

    .blocks-courses {
        max-width: 100% !important;
    }

    .two {
        margin: 0 0 15px 0;
        padding: 15px;
    }

    .h1-two {
        font-size: 36px;
        text-align: center;
    }

    /*Блок с курсами*/
    .course-img {
        width: 100%;
    }

    .course-h3 {
        padding: 0 0 0 20px;
        font-size: 18px;
        color: #465d81;
        cursor: pointer;
    }

    .material-icons {
        vertical-align: middle;
    }

    @media (min-width: 480px) {
        h1 {
            font-size: 4em;
        }
    }
</style>

<svelte:head>
    <title>Django channel</title>
    <meta name="description" content="
    Бесплатные курсы django 2 на русском. Обучения программированию на python3. Помощь ментора.">
</svelte:head>

<div class="preview">
    <img class="img-preview" src="img/home/photo.jpg"/>

    <div class="one">
        <div class="one-fone">
            <h2 class="one-h2">Что вы получите</h2>
            <div class="row one-block">
                <h3 class="one-h3">#1</h3>
                <div class="">
                    <div class="one-p-fone"></div>
                    <p class="headline-3-text">Задания курса</p>
                    <p class="one-p-text">Каждый курс — это интерактивный учебник,
                        который содержит статьи,
                        видеоматериалы, тесты, примеры и проекты.</p>
                </div>
            </div>
            <div class="one-block">
                <div class="">
                    <h3 class="one-h3">#2</h3>
                </div>
                <div class="">
                    <div class="one-p-fone one-p-fone-two"></div>
                    <p class="headline-3-text">Сообщество</p>
                    <p class="one-p-text">Общайтесь с другими учащимися: обсуждайте
                        идеи, материалы курса и
                        помогайте друг другу осваивать новые понятия.</p>
                </div>
            </div>
            <div class="one-block">
                <div class="">
                    <h3 class="one-h3">#3</h3>
                </div>
                <div class="">
                    <div class="one-p-fone"></div>
                    <p class="headline-3-text">Помощь ментора</p>
                    <p class="one-p-text">В обучении и понимании материала поможет
                        личный
                        преподаватель.</p>
                </div>
            </div>
            <div class="row one-block">
                <div class="">
                    <h3 class="one-h3">#4</h3>
                </div>
                <div class="">
                    <div class="one-p-fone one-p-fone-two"></div>
                    <p class="headline-3-text">Поддержка</p>
                    <p class="one-p-text">Вы не останетесь одни в изучении материала,
                        вам поможет
                        сообщество или ментор.</p>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="container blocks-courses">
    <div class="">
        <h1 class="h1-two">Планируемые курсы</h1>
    </div>
    <div class="grid-cell paper">
        <img class="course-img" src="img/home/python-base.svg"
             alt="django course">
        <div class="two">
            <h3 class="course-h3" onclick="app.home.click('#block-1')">
                Python – базовый уровень
                <img class="icon-16" src="img/home/down-arrow.svg"
                     alt="django course">
            </h3>
            <hr>
            <ul id="block-1">
                <li>синтаксис</li>
                <li>типы данных</li>
                <li>управляющие конструкции</li>
                <li>встроенные функции</li>
                <li>функции</li>
                <li>модульность</li>
                <li>ООП</li>
                <li>виртуальное окружение</li>
                <li>работа с файлами и форматами</li>
                <li>знакомство с PyCharm</li>
            </ul>
        </div>
    </div>
</div>

<div class="grid-cell paper">
    <img class="course-img" src="img/home/python-standard.svg" alt="django course">
    <div class="two">
        <h3 class="course-h3" onclick="app.home.click('#block-2')">
            Python – средний уровень
            <img class="icon-16" src="img/home/down-arrow.svg" alt="django course">
        </h3>
        <hr>
        <ul id="block-2">
            <li>Метаклассы</li>
            <li>Абстрактные классы (abc)</li>
            <li>Декораторы классов</li>
            <li>Общие аспекты ооп</li>
            <li>Инкапсуляция, наследование, полиморфизм</li>
            <li>Декораторы</li>
            <li>Журналирование и модуль logging</li>
            <li>Модульное тестирование</li>
            <li>Работа с сетью</li>
        </ul>
    </div>
</div>

<div class="grid-cell paper">
    <img class="course-img" src="img/home/django-base.svg" alt="django course">
    <div class="two">
        <h3 class="course-h3" onclick="app.home.click('#block-3')">
            Django – базовый уровень
            <img class="icon-16" src="img/home/down-arrow.svg" alt="django course">
        </h3>
        <hr>
        <ul id="block-3">
            <li>модели</li>
            <li>миграции</li>
            <li>django ORM</li>
            <li>работа с urls</li>
            <li>работа с формами</li>
            <li>шаблонизатор</li>
            <li>django admin</li>
            <li>аутентификация пользователей</li>
            <li>расширения для django</li>
            <li>git</li>
            <li>деплой на сервере</li>
            <li>знакомство с реляционными базами данных</li>
        </ul>
    </div>
</div>

<div class="grid-cell paper">
    <img class="course-img" src="img/home/django-standart.svg" alt="Django – средний уровень">
    <div class="two">
        <h3 class="course-h3" onclick="app.home.click('#block-4')">
            Django – средний уровень
            <img class="icon-16" src="img/home/down-arrow.svg" alt="django course">
        </h3>
        <hr>
        <ul id="block-4">
            <li>Погружениев в ORM</li>
            <li>CVB</li>
            <li>django rest framework</li>
            <li>сериализации</li>
            <li>валидаторы</li>
            <li>OAuth2</li>
        </ul>
    </div>
</div>

