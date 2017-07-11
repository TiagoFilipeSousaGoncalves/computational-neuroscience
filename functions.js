function hideseek() {
            var x = document.getElementById('myDIV');
            if (x.style.display === 'none') {
                x.style.display = 'block';
            } else {
                x.style.display = 'none';
            }
        }

 function videoseek() {
            var x = document.getElementById('myVideo');
            if (x.style.display === 'none') {
                x.style.display = 'block';
            } else {
                x.style.display = 'none';
            }
        }

  // host of the server
    var host = 'localhost';
    var nodejs_port = '4000';

    var socket = io(host + ':' + nodejs_port);
    var canvas = document.getElementById('bodyCanvas');
    var ctx = canvas.getContext('2d');
    var canvas2 = document.getElementById('rectangle');
    var ctx2 = canvas2.getContext('2d');
    var color = "Red";
    var colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#00ffff', '#ff00ff'];
    var ind = 0;
    var tab = new Array();
    var write = 0;
    var rect = 1;



    // handstate circle size
    var HANDSIZE = 20;

    // closed hand state color
    var HANDCLOSEDCOLOR = "red";

    // open hand state color
    var HANDOPENCOLOR = "green";

    // lasso hand state color
    var HANDLASSOCOLOR = "blue";

    

    function updateHandState(handState, jointPoint) {
        switch (handState) {
            case 3:
                drawHand(jointPoint, HANDCLOSEDCOLOR);
                if ((jointPoint.depthX * 512) >= 362 && (jointPoint.depthX * 512) <= 462 && (jointPoint.depthY * 424) >= 50 && (jointPoint.depthY * 424) <= 150) {
                    color = "Green";


                    //Timer Function
                    var count = 4;
                    var counter = setInterval(timer, 1000); //Runs every second (1000ms=1s)
                    function timer() {
                        count = count - 1;
                        while (count == 0) {
                            document.getElementById("timer").style.color = 'green'
                            document.getElementById("timer").innerHTML = "Begin!"
                            return;
                        }
                        while (count < 0) {
                            clearInterval(counter);
                            document.getElementById("timer").innerHTML = ""
                            return;
                        }
                        document.getElementById("timer").style.color = 'red'
                        document.getElementById("timer").innerHTML = count;
                    }
                }
                break;

            case 2:
                drawHand(jointPoint, HANDOPENCOLOR);
                color = "red";
                break;

            case 4:
                drawHand(jointPoint, HANDLASSOCOLOR);
                color = "red";
                break;
            default:
                color = "red";
        }
    }

    function drawHand(jointPoint, handColor) {
        // draw semi transparent hand cicles
        ctx.globalAlpha = 0.75;
        ctx.beginPath();
        ctx.fillStyle = handColor;
        ctx.arc(jointPoint.depthX * 512, jointPoint.depthY * 424, HANDSIZE, 0, Math.PI * 2, true);
        ctx.fill();
        ctx.closePath();
        ctx.globalAlpha = 1;
    }

    socket.on('bodyFrame', function (bodyFrame) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (rect == 1) {
            ctx.strokeStyle = color;
            ctx.strokeRect(362, 50, 100, 100);
        }
        var index = 0
        bodyFrame.bodies.forEach(function (body) {
            if (body.tracked) {
                for (var jointType in body.joints) {
                    var joint = body.joints[jointType];
                    ctx.fillStyle = colors[index];
                    ctx.fillRect(joint.depthX * 512, joint.depthY * 424, 10, 10);
                }
                //draw hand states
                updateHandState(body.leftHandState, body.joints[7]);
                updateHandState(body.rightHandState, body.joints[11]);
                index++;
                if (write == 1) {
                    rect = 0;
                    color = "White";
                    tab[ind] = body;
                    console.log(tab[ind]);
                    ind++;
                }
            }
        });
    });

    function myFunction() {
            write = 0;
            msgObject = {
                'user_name': "Clement",//name.val().trim(),
                'message': "Clement",//"Clement"//msg.val().trim()
                'data' : tab
            };

            socket.emit('message', msgObject);
            ind = 0;
            tab = new Array();
    }

    function myFunction2() {

        write = 1;
    }
    //Session Time Function
    var sec = 0;
    var min = 0;
    var hour = 0;
    var ncounter = setInterval(telapsed, 1000);
    function telapsed() {
            sec = sec + 1;
            if (sec == 60) {
                sec = 0;
                min = min + 1;
            }
            else if (min == 60) {
                sec = 1;
                min = 0;
                hour = hour + 1;
            }
            if (sec < 10 && min < 10 && hour < 10) {
                document.getElementById("telapsed").value = "0" + hour + ":" + "0" + min + ":" + "0" + sec;
            }
            else if (min < 10 && hour < 10) {
                document.getElementById("telapsed").value = "0" + hour + ":" + "0" + min + ":" + sec;
            }
            else if (hour < 10) {
                document.getElementById("telapsed").value = "0" + hour + ":" + min + ":" + sec;
            }
        }