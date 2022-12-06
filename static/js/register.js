// register.onclick = function(data) {console.log('asdfsdf'), console.log(data)}
// document.forms['form'].submit()
function register(data) {
    let form = document.forms['form']
    let name = document.getElementById('name').value
    let passwordOne = document.getElementById('passwordOne').value
    let passwordTwo = document.getElementById('passwordTwo').value
    if (name === '') {
        alert('field name can\'t be empty')
    }
    else if (passwordOne !== passwordTwo) {
        alert('passwords must match')
    }
    else {
        form.submit()
    }
}