<style>
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

<div class="row preview">
    <div class="col-sm-12 col-md-12 col-lg-6 col-xl-6">
        <img class="img-preview" src="img/home/photo.jpg"/>
    </div>
    <div class="col-sm-12 col-md-12 col-lg-6 col-xl-6">
        <div class="one">
            <div class="one-fone">
                <h2 class="one-h2">Что вы получите</h2>
            <div class="row one-block">
            <div class="col-1">
                <div>
                    <h3 class="one-h3">#1</h3>
                </div>
            </div>
                <div class="col-10">
                    <div class="one-p-fone"></div>
                    <p class="headline-3-text">Задания курса</p>
                    <p class="one-p-text">Каждый курс — это интерактивный учебник,
                        который содержит статьи,
                        видеоматериалы, тесты, примеры и проекты.</p>
                </div>
            </div>
            <div class="row one-block">
            <div class="col-1">
                <div>
                    <h3 class="one-h3">#2</h3>
                </div>
            </div>
                <div class="col-10">
                    <div class="one-p-fone one-p-fone-two"></div>
                    <p class="headline-3-text">Сообщество</p>
                    <p class="one-p-text">Общайтесь с другими учащимися: обсуждайте
                        идеи, материалы курса и
                        помогайте друг другу осваивать новые понятия.</p>
                </div>
            </div>
                <div class="row one-block">
                    <div class="col-1">
                        <div>
                            <h3 class="one-h3">#3</h3>
                        </div>
                    </div>
                    <div class="col-10">
                        <div class="one-p-fone"></div>
                        <p class="headline-3-text">Помощь ментора</p>
                        <p class="one-p-text">В обучении и понимании материала поможет
                            личный
                            преподаватель.</p>
                    </div>
                </div>
            <div class="row one-block">
            <div class="col-1">
                <div>
                    <h3 class="one-h3">#4</h3>
                </div>
            </div>
                <div class="col-10">
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
</div>
<div class="container blocks-courses">
    <div class="row ">
        <div class="col-12">
            <!--<h1 class="h1-two">Идет набор на курсы</h1>-->
            <h1 class="h1-two">Планируемые курсы</h1>
        </div>
    </div>
    <div class="row justify-content-center">
        <div class="col-sm-12 col-md-6 col-lg-6 col-xl-5">
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
        <div class="col-sm-12 col-md-6 col-lg-6 col-xl-5">
            <div class="grid-cell paper">
                <img class="course-img" src="img/home/python-standard.svg"
                     alt="django course">
                <div class="two">
                    <h3 class="course-h3" onclick="app.home.click('#block-2')">
                        Python – средний уровень
                        <img class="icon-16" src="img/home/down-arrow.svg"
                             alt="django course">
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
        </div>
        <div class="col-sm-12 col-md-6 col-lg-6 col-xl-5">
            <div class="grid-cell paper">
                <img class="course-img" src="img/home/django-base.svg"
                     alt="django course">
                <div class="two">
                    <h3 class="course-h3" onclick="app.home.click('#block-3')">
                        Django – базовый уровень
                        <img class="icon-16" src="img/home/down-arrow.svg"
                             alt="django course">
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
        </div>
        <div class="col-sm-12 col-md-6 col-lg-6 col-xl-5">
            <div class="grid-cell paper">
                <img class="course-img" src="img/home/django-standart.svg"
                     alt="Django – средний уровень">
                <div class="two">
                    <h3 class="course-h3" onclick="app.home.click('#block-4')">
                        Django – средний уровень
                        <img class="icon-16" src="img/home/down-arrow.svg"
                             alt="django course">
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
        </div>
    </div>
</div>
