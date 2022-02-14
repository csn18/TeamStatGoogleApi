function example(argument) {
    let width = document.getElementById('access').value;
    document.getElementById('progress').style.width = width + "px";
    document.getElementById('progress').innerHTML = width;
    document.getElementById('progress2').style.width = (width - 10) + "px";
    document.getElementById('progress2').innerHTML = width;
}
