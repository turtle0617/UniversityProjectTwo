var c01=require('./c01.js');
var totalplayer;
var chatObj = {
    host: location.host,
    socket: null,
    // 開啟一個 WebSocket 連線，並設定相關動作
    init: function() {
        var url = "ws://" + chatObj.host + "/socket";
        chatObj.socket = new WebSocket(url);
        chatObj.socket.onmessage = function(event) {
                // console.log(event);
                chatObj.showMsg(event.data);
            },
            chatObj.socket.onclose = function(event) {
                console.log("on close");
            },
            chatObj.socket.onerror = function(event) {
                console.log("on error");
            }
    },
    // 發送訊息至 Server 端
    sendMsg: function(gamemode) {
        console.log($("#howmany option:selected").val() +gamemode);
        totalplayer = $("#howmany option:selected").val();
        chatObj.socket.send($("#howmany option:selected").val() + " " + gamemode);

    },
    // 顯示訊息
    showMsg: function(message) {
        if (message.search("c01") != -1){
            c01(message.replace("c01",""),totalplayer)
            console.log(message);
        }else if(message.search("countup") != -1){
            countup(message.replace("countup",""));
            console.log(message);

        }
        // countup(message);

    }
};
$(function() {
    $('#301,#501,#701,#countup').click(function() {
        console.log('clicked2', this.id);
        $("#selectmod").hide();
        $("#player0btn").hide();
        $("#player1btn").hide();
        $("#player2btn").hide();
        $("#player3btn").hide();
        $(".player0Score").text($(this).val());
        $(".player1Score").text($(this).val());
        $(".player2Score").text($(this).val());
        $(".player3Score").text($(this).val());
        $("#player0Dart").text(0);
        $("#player1Dart").text(0);
        $("#player2Dart").text(0);
        $("#player3Dart").text(0);

        chatObj.sendMsg(this.id);
        return false;
    });

    chatObj.init();
});

//if button is countup 
// $(function() {
//     var btn01 = $("#msg-301");
//     btn01.click(function() {
//         $("#player0btn").hide();
//         $("#player1btn").hide();
//         $("#player2btn").hide();
//         $("#player3btn").hide();
//         $(".player0Score").text(0);
//         $(".player1Score").text(0);
//         $(".player2Score").text(0);
//         $(".player3Score").text(0);
//         $("#player0Dart").text(0);
//         $("#player1Dart").text(0);
//         $("#player2Dart").text(0);
//         $("#player3Dart").text(0);
//         chatObj.sendMsg();
//         // btn.hide();
//         return false;
//     });

//     chatObj.init();
// });

//第一層字串判斷
function countup(mes) {

    if (mes.search("player0") != -1) {
        if (totalplayer == 1) {
            $("#player0").show();
            $("#player1").hide();
            $("#player2").hide();
            $("#player3").hide();
            $("#player0btn").hide();
            $("#player1btn").hide();
            $("#player2btn").hide();
            $("#player3btn").hide();
        } else if (totalplayer == 2) {
            $("#player0").show();
            $("#player1").hide();
            $("#player2").hide();
            $("#player3").hide();
            $("#player0btn").hide();
            $("#player1btn").show();
            $("#player2btn").hide();
            $("#player3btn").hide();
        } else if (totalplayer == 3) {
            $("#player0").show();
            $("#player1").hide();
            $("#player2").hide();
            $("#player3").hide();
            $("#player0btn").hide();
            $("#player1btn").show();
            $("#player2btn").show();
            $("#player3btn").hide();
        } else if (totalplayer == 4) {
            $("#player0").show();
            $("#player1").hide();
            $("#player2").hide();
            $("#player3").hide();
            $("#player0btn").hide();
            $("#player1btn").show();
            $("#player2btn").show();
            $("#player3btn").show();
        }

        player(mes, "player0");
    } else if (mes.search("player1") != -1) {
        if (totalplayer == 2) {
            $("#player0").hide();
            $("#player1").show();
            $("#player2").hide();
            $("#player3").hide();
            $("#player0btn").show();
            $("#player1btn").hide();
            $("#player2btn").hide();
            $("#player3btn").hide();
        } else if (totalplayer == 3) {
            $("#player0").hide();
            $("#player1").show();
            $("#player2").hide();
            $("#player3").hide();
            $("#player0btn").show();
            $("#player1btn").hide();
            $("#player2btn").show();
            $("#player3btn").hide();
        } else if (totalplayer == 4) {
            $("#player0").hide();
            $("#player1").show();
            $("#player2").hide();
            $("#player3").hide();
            $("#player0btn").show();
            $("#player1btn").hide();
            $("#player2btn").show();
            $("#player3btn").show();
        }
        player(mes, "player1");

    } else if (mes.search("player2") != -1) {
        if (totalplayer == 3) {
            $("#player0").hide();
            $("#player1").hide();
            $("#player2").show();
            $("#player3").hide();
            $("#player0btn").show();
            $("#player1btn").show();
            $("#player2btn").hide();
            $("#player3btn").hide();
        } else if (totalplayer == 4) {
            $("#player0").hide();
            $("#player1").hide();
            $("#player2").show();
            $("#player3").hide();
            $("#player0btn").show();
            $("#player1btn").show();
            $("#player2btn").hide();
            $("#player3btn").show();
        }
        player(mes, "player2");

    } else if (mes.search("player3") != -1) {
        $("#player3").show();
        $("#player0").hide();
        $("#player1").hide();
        $("#player2").hide();
        $("#player3btn").hide();
        $("#player1btn").show();
        $("#player2btn").show();
        $("#player0btn").show();
        player(mes, "player3");

    } else if (mes.search("GameOver") != -1) {
        $("#Bar").text("Game over");
        // $("#player0Score").text(0);
        // $("#player1Score").text(0);
        // $("#player0Dart").text(0);
        // $("#player1Dart").text(0);
        $("#player0Remove").hide();
        $("#player1Remove").hide();
        $("#player2Remove").hide();
        $("#player3Remove").hide();
        $("#selectmod").show();

    } else if (mes.search("Round") != -1) {
        // console.log("Bar mes :" + mes);
        $("#Bar").text(mes);
    } else {
        $("#Bar").text(mes);

    }
};
//第二層字串判斷。由於玩家人數無法每次都得知故把id採用變數避免過多一樣的函式很醜！
function player(player, mestext) {
    var id = mestext;
    // console.log("var player is: " + id);
    $("#" + id + "Remove").hide();
    if (player.search("Score") != -1) {
        // console.log("#" + id + "Score work");
        $("." + id + "Score").text(player.replace(id + "Score", ""));
        // console.log(id + "Score" + player.replace(id + "Score", ""));
    } else if (player.search("dart") != -1) {
        // console.log("#" + id + "Dart work");
        $("#" + id + "Dart").text(player.replace(id + "dartcount", ""));
        // console.log(id + "dartcount" + player.replace(id + "dartcount", ""));
    } else if (player.search("Removing" != -1)) {
        // console.log("#" + id + "Remove work");
        $("#" + id + "Remove").show();
    }
};


//jqueryID都採用字串形式
// function player1(player1,mestext) {
//     $("#player1Remove").hide();
//     if (player1.search("Score") != -1) {
//         $("#player1Score").text(player1.replace("player1Score", ""));
//         console.log("Player1Score" + player1.replace("player1Score", ""));
//     } else if (player1.search("dart") != -1) {
//         $("#player1Dart").text(player1.replace("player1dartcount", ""));
//         console.log("player1dartcount" + player1.replace("player1dartcount", ""));
//     } else if (player1.search("Removing" != -1)) {
//         $("#player1Remove").show();
//     }
// };