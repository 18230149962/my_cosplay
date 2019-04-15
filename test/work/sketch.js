var snake;
var pixel_location;
// 大小
var pixel_size = 10;
var shots = [];
var movement = [];
var highscore = 0;
var gameState = 'init';

function setup(){
  createCanvas(500, 500);
  // 蛇速
  frameRate(5);
}

function initGame(){
  background(50, 50, 100);
  var name = '贪吃蛇';
  textSize(50);
  fill(255);
  nameWidht = textWidth(name);
  text(name, (width - nameWidht)/2, height/2 - 40);
  startBtn = createButton('&nbsp; 请开始你的表演 &nbsp;');
  startBtn.position(width/2 - startBtn.width/2, height/2);
  startBtn.mousePressed(startGame);
  noLoop();
}

function startGame(){
  removeElements();
  gameState = 'play';
  snake = new Snake();
  // 食物个数
  setJelloShots(1);
  loop();
}

function runGame(){
  background(50, 50, 100);
  textSize(12);
  fill(255);
  text("score: " + snake.tail.length, 1, 10);
  text("highscore: " + highscore, 1, 24);

  snake.update();
  snake.show();
  snake.checkDeath();

  fill(0, 255, 0, 100);
  for(var i=0;i<shots.length;i++){

    // 自动吃食物
    // if(snake.pos.x == pixel_location.x && snake.pos.y < pixel_location.y && (pixel_location.y - snake.pos.y) < width / 2){
    // movement.push([0, 1])
  // }
    // if(snake.pos.x == pixel_location.x && snake.pos.y > pixel_location.y){
    // movement.push([0, -1])
  // }

    // if(snake.pos.y == pixel_location.y && snake.pos.x < pixel_location.x){
    // movement.push([1, 0])
  // }
    // if(snake.pos.y == pixel_location.y && snake.pos.x > pixel_location.x){
    // movement.push([-1, 0])
  // }

    rect(shots[i].x, shots[i].y, pixel_size, pixel_size);
    if(snake.eat(shots[i])){
      snake.tail.push(createVector(snake.x, snake.y));
      shots.splice(i, 1);
      setJelloShots(1);
      if(snake.tail.length > highscore) highscore = snake.tail.length;
    }
  }
}
    // stop
    // $(document).keydown(function(e){
    // if(!e) var e = window.event;
    // e.keyCode==32 && alert("已暂停, 点击“确定“继续游戏！");
    // });

function endGame(){
  background(50, 50, 100);
  textSize(32);
  var msg = 'GG';
  var score = '您的长度只有 ' + snake.tail.length;
  msgWidht = textWidth(msg);
  scoreWidht = textWidth(score);
  fill(255);
  text(msg, (width - msgWidht)/2, height/2 - 40);
  text(score, (width - scoreWidht)/2, height/2);
  startBtn = createButton('&nbsp; 再来一把 &nbsp;');
  startBtn.position(width/2 - startBtn.width/2, height/2 + 40);
  startBtn.mousePressed(startGame);
  noLoop();
}


function draw(){
  if(gameState == 'init'){
    initGame();
  }
  else if(gameState == 'play'){
    runGame();
  }
  else if(gameState == 'end'){
    endGame();
  }
}

function setJelloShots(num){
  var cols = floor(width / pixel_size);
  var rows = floor(height / pixel_size);
  for(var i=0;i<num;i++){
    var location = createVector(floor(random(cols)), floor(random(rows))).mult(pixel_size);
    while(snake_intersect(location)){
      location = createVector(floor(random(cols)), floor(random(rows))).mult(pixel_size);
    }
    shots.push(location);
  }
}

function snake_intersect(location){
  // auto eat
  // pixel_location = location
  // if(snake.pos.x < location.x){
    // movement.push([1, 0])

  // }
  // if(snake.pos.x > location.x){
    // movement.push([-1, 0])
  // }
  // if(snake.pos.y < location.y){
    // movement.push([0, -1])
  // }
  // if(snake.pos.y > location.y){
    // movement.push([0, 1])
  // }
  var intersect = false;
  if(location.x == snake.pos.x && location.y == snake.pos.y){
    intersect = true;
  }else{
    for(var i=0;i<snake.tail.length;i++){
      if(location.x == snake.tail[i].x && location.y == snake.tail[i].y){
        intersect = true;
        break;
      }
    }
    for(var i=0;i<shots.length;i++){
      if(location.x == shots[i].x && location.y == shots[i].y){
        intersect = true;
        break;
      }
    }
  }
  return intersect;
}

function keyPressed(){
  if(keyCode === DOWN_ARROW){
    movement.push([0, 1]);
  }else if(keyCode === UP_ARROW){
    movement.push([0, -1]);
  }else if(keyCode === LEFT_ARROW){
    movement.push([-1, 0]);
  }else if(keyCode === RIGHT_ARROW){
    movement.push([1, 0]);
  }
}
