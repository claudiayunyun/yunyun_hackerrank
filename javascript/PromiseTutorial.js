function setup(){
    delay()
    .then(() => console.log('Hello World'))
    .catch((err) => console.log(err));
}

function delay(time) {
    return new Promise((resolve, reject) => {
        if(isNaN(time)) {
            reject(new Error('delay requires a valie number'))
        } else {
            setTimeout(resolve, time);
        } 
    });
}