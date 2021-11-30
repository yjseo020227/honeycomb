function hello(){
    const h1 = document.querySelector('h1')
    if (h1.innerHTML === 'This is the dashboard'){
        h1.innerHTML = "This is your real estate dashboard";
    }
    else{
        h1.innerHTML = "This is the dashboard";
    }
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = hello;
})