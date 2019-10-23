<header>
    <a class="a-logo" href="/"><img class="logo" src="../assets/img/logo.svg"></a>
    <nav>
        <ul>
            <li><a href="#">Главная</a></li>
            <li><a href="#">Курсы</a></li>
            <li><a href="#">Статьи</a></li>
            <li><a href="#">Форум</a></li>
            <li><a href="#">Сообщества</a></li>
            <li><a href="#">Задания</a></li>
            <li><a href="#">Тесты</a></li>
        </ul>
    </nav>
    <ul class="last">
        <li class="li-message">
            <a href="#"><img class="message"
                             src="../../assets/img/icons/message.svg"></a>
            <span class="counter">0</span>
        </li>
        <li><a href="/login" use:link>Вход</a></li>
    </ul>
</header>

<script>
    import {link} from 'svelte-spa-router'


</script>

<style>
    header {
        display: grid;
        grid-template-columns: 1fr 4fr 1fr;
        grid-auto-rows: auto;
        grid-area: nav;
        align-items: center;
        background-color: var(--nav-color);
    }

    ul {
        margin: 0;
        padding: 0;
    }

    ul li {
        list-style: none;
    }

    nav ul {
        display: grid;
        grid-auto-flow: column;
        grid-column-gap: 20px;
        justify-content: start;
        align-content: center;
    }

    ul li a {
        text-decoration: none;
        color: #fff;
        padding: 18px 0;
        position: relative;
        transition: all 0.5s cubic-bezier(0.4, 0, 1, 1);
    }

    .last {
        display: grid;
        grid-auto-flow: column;
        grid-column-gap: 20px;
        justify-content: center;
        align-content: center;

    }

    nav ul li a:hover {
        border-bottom: 2px solid;
    }

    /*nav ul li a:after {*/
    /*    content: '';*/
    /*    position: absolute;*/
    /*    border-bottom: 2px solid;*/
    /*    left: -300px;*/
    /*    width: 100%;*/
    /*    transition: left 0.5s cubic-bezier(0.4, 0, 1, 1);*/
    /*}*/
    /*nav ul li a:after:hover {*/
    /*    left: 0;*/
    /*}*/
    .a-logo {
        justify-self: center;
    }

    .logo {
        width: 136px;
        height: 42px;
    }

    .message {
        width: 26px;
        height: 18px;
        position: relative;
    }

    .li-message {
        position: relative;
    }

    .counter {
        position: absolute;
        color: #fff;
        font-size: 12px;
        width: 20px;
        height: 20px;
        background-color: var(--count);
        top: -10px;
        right: -5px;
        border-radius: 50%;
        text-align: center;
        line-height: 20px;
    }
</style>