<footer>
    <a href="#"><img class="footer-logo" src="../assets/img/logo.svg"></a>
    <span>Django Channel © 2018-2019</span>
    <div>
        <a href="#"><img class="github" src="../assets/img/icons/github.svg"></a>
        <a href="#"><img class="youtube" src="../assets/img/icons/youtube.svg"></a>
        <a href="#"><img class="vk" src="../assets/img/icons/vk.svg"></a>
    </div>
</footer>

<style>
    footer {
        grid-area: footer;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        align-items: center;
        justify-items: center;
        background-color: var(--nav-color);
        color: #fff;
    }

    .footer-logo {
        opacity: 0.1;
    }

    .github, .vk {
        color: #fff;
        width: 21px;
        height: 21px;
    }

    .youtube {
        color: #fff;
        width: 24px;
        height: 21px;
        margin: 0 25px 0 25px;
    }
</style>