let config = {
    renderer: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
      default: 'arcade',
      arcade: {
        gravity: { y: 300 },
        debug: false
      }
    },
    scene: {
      preload: preload,
      create: create,
      update: update
    }
  };
  
let game = new Phaser.Game(config);

let bird;
let hasLanded = false;
let cursors;
let hasBumped = false;

let isGameStarted = false;
let messageToPlayer;

function preload () { //fn to bring in imgs for the app e.g. background
    this.load.image('background', 'assets/background.png');
    this.load.image('road', 'assets/road.png');
    this.load.image('column', 'assets/column.png');
    this.load.spritesheet('bird', 'assets/bird.png', { frameWidth: 64, frameHeight: 96 });
}


function create () { //fn to generate elements appearing in game e.g. imgs from preload
    /*background*/
    const background = this.add.image(0, 0, 'background').setOrigin(0, 0); 
    /*road & columns*/
    const roads = this.physics.add.staticGroup();

    const topColumns = this.physics.add.staticGroup({
        key: 'column',
        repeat: 1,
        setXY: { x: 200, y: 0, stepX: 300 }
    })

    const bottomColumns = this.physics.add.staticGroup({
        key: 'column',
        repeat: 1,
        setXY: { x: 350, y: 400, stepX: 300 }
    })

    const road = roads.create(400, 568, 'road').setScale(2).refreshBody();
    
    /*bird*/
    bird = this.physics.add.sprite(0, 50, 'bird').setScale(2);
    bird.setBounce(0.2);
    bird.setCollideWorldBounds(true);

    /*bird lands on road*/
    this.physics.add.overlap(bird, road, () => hasLanded = true, null, this);
    this.physics.add.collider(bird, road);

    /*bird can't pass through columns*/
    this.physics.add.overlap(bird,topColumns, () => hasBunped = true, null, this);
    this.physics.add.overlap(bird, bottomColumns, () => hasBumped = true, null, this);
    this.physics.add.collider(bird,topColumns);
    this.physics.add.collider(bird, bottomColumns);

    /*movement*/
    cursors = this.input.keyboard.createCursorKeys();

    /*message to player*/
    messageToPlayer = this.add.text(0, 0, 'Instructions: Press space bar to start', { fontFamily: '"Comic Sans MS", Times, serif', fontSize: "15px", color: "black", backgroundColor: "white" });
    /*move text to bottom*/
    Phaser.Display.Align.In.BottomCenter(messageToPlayer, background, -30, 50);
}

function update () { //gn used to update "bird" in game e.g. controls, interactions
    /*start gameonly when user press space key*/
    if (cursors.space.isDown && !isGameStarted) {
        isGameStarted = true;
        messageToPlayer.text = 'Instructions: Press the "^" button to stay upright\nAnd don\'t hit the columns or ground';
    }
    /*when game hasn't started, bird at -160 velocity*/
    if (!isGameStarted) {
        bird.setVelocityY(-160);
    }
    /*bird moves upwards*/
    if (cursors.up.isDown && !hasLanded && !hasBumped) {
        bird.setVelocityY(-160);
    }
    /*continues to move if didnt hit road and column*/
    if (!hasLanded && !hasBumped) {
        bird.body.velocity.x = 50;
    } else {
        bird.body.velocity.x = 0;
    }
    /*game starts*/
    if((!hasLanded || !hasBumped) && isGameStarted) {
        bird.body.velocity.x = 50;
    } else {
        bird.body.velocity.x = 0;
    }
    /*stops moving once it hits the road or column*/
    if (hasLanded || hasBumped) {
        messageToPlayer.text = 'Oh no! You crashed!';
    }
    /*when bird reaches far right of screen and falls down gently*/
    if (bird.x > 750) {
        bird.setVelocity(40);
        messageToPlayer.text = 'Congrats! You won!';
    }
}