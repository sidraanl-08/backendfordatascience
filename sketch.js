//simple game with a sqaure
//everytime sqaure is pressed, it will increase the score 

let x = 100;
let y = 100;
let size = 50;
let score = 0;

function setup(){
    createCanvas(300, 300);
}

function draw(){
    background(200);
    rect(x,y,size,size);

    textSize(16);
    text('Score:' + score , 10, 20);
}

function mousePressed(){
    if (
        mouseX > x && mouseX < x + size &&
        mouseY > y && mouseY < y + size
    ) {
        score++
        x= random(0,250);
        y = random(0,250);
    }
}