var cookie = document.querySelector('.cookie');

function hide(message){
    cookie.remove();

}


var highFirst = document.querySelector ('.highs1');
var lowFirst = document.querySelector ('.lows1');
var highSec = document.querySelector('.highs2');
var LowSec = document.querySelector('.lows2');
var highThird = document.querySelector('.highs3');
var LowThird = document.querySelector('.lows3');
var highLast = document.querySelector ('.highs4');
var lowLast = document.querySelector ('.lows4');

function change(last){
    highFirst.innerText = '75°';
    lowFirst.innerText = '65°';
    highSec.innerText = '80°';
    LowSec.innerText = '66°';
    highThird.innerText = '69°';
    LowThird.innerText = '61°';
    highLast.innerText = '78°';
    lowLast.innerText = '70°';
}
