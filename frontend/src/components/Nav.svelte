<nav>
    <ul>
        <a href="#"><img class="logo" src="../assets/img/logo.svg"></a>
        <li><a href="#">Главная</a></li>
        <li><a href="#">Курсы</a></li>
        <li><a href="#">Статьи</a></li>
        <li><a href="#">Форум</a></li>
        <li><a href="#">Сообщества</a></li>
        <li><a href="#">Задания</a></li>
        <li><a href="#">Тесты</a></li>
        <li class="last">
            <ul>
                <li class="li-message">
                    <a href="#"><img class="message" src="../../assets/img/icons/message.svg"></a>
                    <span class="counter">0</span>
                </li>
                <li><a href="/login" use:link>Вход</a></li>
            </ul>
        </li>
    </ul>
</nav>

<script>
    import {link} from 'svelte-spa-router'


</script>

<style>
    nav {
    display: flex;
    grid-area: nav;
    background-color: var(--nav-color);
}

nav ul {
    display: flex;
    width: 100%;
    align-items: center;
    margin: 0;
    padding: 0;
}

nav ul li {
    list-style: none;
    padding: 0 0 0 20px;
}

nav ul .last {
    margin: 0 35px 0 auto;
}

nav ul li a {
    text-decoration: none;
    color: #fff;
    padding: 18px 0;
    position: relative;
    transition: all 0.5s cubic-bezier(0.4, 0, 1, 1);
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