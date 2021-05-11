

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
