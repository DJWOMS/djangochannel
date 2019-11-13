<script>
    export let segment;
</script>

<header>
    <a class="a-logo" href="/"><img class="logo" src="img/logo.svg" alt=""></a>
    <nav>
        <ul>
            <li><a class='{segment === undefined ? "selected" : ""}' href='.'>Главная</a></li>
            <li><a href="/">Курсы</a></li>
            <li><a rel=prefetch class='{segment === "blog" ? "selected" : ""}' href='blog'>Статьи</a></li>
            <li><a href="/">Форум</a></li>
            <li><a rel=prefetch href="community">Сообщества</a></li>
            <li><a href="/">Задания</a></li>
            <li><a href="/">Тесты</a></li>
        </ul>
    </nav>
    <ul class="last">
        <li class="li-message">
            <a href="/"><img class="message"
                             src="img/icons/message.svg" alt=""></a>
            <span class="counter">0</span>
        </li>
        <li><a href="login">Вход</a></li>
    </ul>
</header>
<!--<nav>-->
<!--    <ul>-->
<!--        <li><a class='{segment === undefined ? "selected" : ""}' href='.'>home</a></li>-->
<!--        <li><a class='{segment === "about" ? "selected" : ""}' href='about'>about</a></li>-->

<!--        &lt;!&ndash; for the blog link, we're using rel=prefetch so that Sapper prefetches-->
<!--             the blog data when we hover over the link or tap it on a touchscreen &ndash;&gt;-->
<!--        <li><a rel=prefetch class='{segment === "blog" ? "selected" : ""}' href='blog'>blog</a></li>-->
<!--    </ul>-->
<!--</nav>-->


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

    /*.selected {*/
    /*    position: relative;*/
    /*    display: inline-block;*/
    /*}*/

    /*.selected::after {*/
    /*    position: absolute;*/
    /*    content: '';*/
    /*    width: calc(100% - 1em);*/
    /*    height: 2px;*/
    /*    background-color: rgb(255, 62, 0);*/
    /*    display: block;*/
    /*    bottom: -1px;*/
    /*}*/
</style>
