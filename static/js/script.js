// set csrf token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    // console.log(csrftoken);
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

$(".need_auth").submit(function (e) {
    e.preventDefault();
    var url = $(this).attr('action');
    var data = $(this).serialize();
    $.ajax({
        url: url,
        type: "POST",
        data: data,
        success: (response) => {
            window.location = response.location;
        },
        error: (response) => {
            if (response.status === 400) {
                $('.error-li').text(response.responseJSON.form.errors[0])
                $('.error-user').text(response.responseJSON.form.fields.username.errors)
                $('.error-email').text(response.responseJSON.form.fields.email.errors)
                $('.error-password1').text(response.responseJSON.form.fields.password1.errors)
                $('.error-password2').text(response.responseJSON.form.fields.password2.errors)
            }
        }
    });
});

// Меню в блоге
$(function () {
    var Accordion = function (el, multiple) {
        this.el = el || {};
        // more then one submenu open?
        this.multiple = multiple || false;

        var dropdownlink = this.el.find('.dropdownlink');
        dropdownlink.on('click',
            {el: this.el, multiple: this.multiple},
            this.dropdown);
    };

    Accordion.prototype.dropdown = function (e) {
        var $el = e.data.el,
            $this = $(this),
            //this is the ul.submenuItems
            $next = $this.next();

        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            //show only one menu at the same time
            $el.find('.submenuItems').not($next).slideUp().parent().removeClass('open');
        }
    }

    var accordion = new Accordion($('.accordion-menu'), false);
})

function mouseImg (id) {
    let $img = $('#'+id);
    $img.mousemove(function (e) {
        move(e.pageX, e.pageY, $img);
    }).mouseout(function (e) {
        resetTransform($img);
    });
}

function move(x, y, $img) {
    // обертка с доп свойствами

    $img.addClass('card-active');

    // центр карточки
    let xser = $img.offset().left + $img.width() / 2;
    let yser = $img.offset().top + $img.height() / 2;

    // координаты мыши относительно центра карточки
    let otnX = x - xser;
    let otnY = y - yser;

    // вычисляем % - на каком расстоянии мышь от середины до края, центр = 0%
    let raznX = otnX / $img.width() * 100 * 2;
    let raznY = otnY / $img.height() * 100 * 2;

    // на сколько градусов нужно повернуть (100% = 6deg)
    let trX = raznY / 100 * 20 * -1;
    let trY = raznX / 100 * 20;

    // окруление
    trX = Math.round(trX * 1000) / 1000;
    trY = Math.round(trY * 1000) / 1000;

    // в css
    $img.css('transform', 'rotateY(' + trY + 'deg) rotateX(' + trX + 'deg) rotateZ(0deg) scale3d(1, 1, 1)');
}

function resetTransform($img) {
    $img.removeClass('card-active');
    $img.css('transform', 'rotateY(0deg) rotateX(0deg) rotateZ(0deg) scale(1)');
}
