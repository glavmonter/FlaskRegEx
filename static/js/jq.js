let t = 0;
let badregex = false;


function bufferKey(e) {
    if (e.keyCode < 37 || e.keyCode > 40) {
        if (t !== 0) {
            clearTimeout(t);
        }
        t = setTimeout('checkRegex()', 500)
    }
}


function checkRegex() {
    console.log('checkRegex called');
    let regex = $('#regex').val();
    let test_string = $('#test_string').val();
    let flags = {'ignorecase': $('#ignorecase').val(),
                 'multiline': $('#multiline').val(),
                 'dotall': $('#dotall').val(),
                 'verbose': $('#verbose').val()};

    const url = '/api/re';

    $.ajax({
        url: url,
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({'regex': regex, 'flags': flags, 'test_string': test_string}),
        success: handleCheckRegex,
        error: reportError
    });
}


function handleCheckRegex(data) {
    console.log(data);
    let error_code = data['result']
    console.log('error_code: ' + error_code)
}

function reportError(error) {
    console.log('Error in process regex: ' + error);
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


function highlight(object) {
    if (badregex != true) {
        object.css('backgroundColor', '#ffffe0');
    }
}


function unhighlight(object) {
    if (badregex != true) {
        object.css('backgroundColor', '#ffffff');
    }
}
