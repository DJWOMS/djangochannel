<script>
    let username = '';
    let password = '';

    async function submit(event) {
        // const response = await post(`auth/login`, {username, password});
        const r = await fetch(`http://127.0.0.1:8000/auth/token/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify({"username": username, "password": password})
        }).then(r => {
            if (r.user) {
                //$session.user = response.user;
                // goto('/');
                console.log(r)
            }
        }).catch(r => {
            // TODO handle network errors
            console.log(r)
            errors = r.errors;
        })


    }
</script>

<svelte:head>
    <title>Войти</title>
</svelte:head>

<main class="main">
    <h1>Войти</h1>
    <form class="login-form" on:submit|preventDefault={submit}>
        <input type="text" name="username" bind:value="{username}" placeholder="Логин">
        <input type="password" name="password" bind:value="{password}" placeholder="Пароль">
        <button type="submit" disabled='{!username || !password}'>Войти</button>
    </form>
    <p class="login-text">Проект призван помочь людям в обучении программированию,
        веб разработке и английскому языку.
        В обучении и понимании материала поможет сообщество и личный преподаватель.
        Вы можете найти себе товарища или группу людей для совместного обучения и выполнения
        задач.
        Отслеживайте личный прогресс обучения и получайте награды за любую активность.
    </p>
</main>

<style>
    h1 {
        background-color: #fff;
        line-height: unset;
        grid-column: 1 / -1;
        text-align: center;
        margin: 0;
    }

    .main {
        display: grid;
        grid-template-columns: minmax(0, 240px) 2fr 1fr minmax(0, 240px);
        grid-template-rows: 60px repeat(auto-fit, 150px);
        grid-area: main;
        grid-column-gap: 15px;
    }

    .login-form {
        grid-column: 2 / 3;
    }

    .login-text {
        grid-column: 3 / 4;
    }
</style>
