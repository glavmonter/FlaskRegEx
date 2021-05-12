

var t = 0;

function bufferKey(e) {
    console.log(e)
    if (e.keyCode < 37 || e.keyCode > 40) {
        if (t !== 0) {
            clearTimeout(t);
        }
        t = setTimeout('checkRegex()', 500)
    }
}


function checkRegex() {
    console.log('checkRegex called')
}

function toggleFlag(flag, button) {
    console.log('Clicked ' + flag);
    flag_input = $('#' + flag);

    if (flag_input.val() == 1) {
        console.log('Set to 0');
        flag_input.val(0);
        $(button).removeClass('checked');
        $(button).mousedown(function () {
            $(button).addClass('checked');
        });
    } else {
        console.log('Set to 1');
        flag_input.val(1);
        $(button).addClass('checked');
        $(button).mousedown(function () {
            $(button).removeClass('checked');
        });
    }
}