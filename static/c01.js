//第一層字串判斷
module.exports = function c01(mes, tplayer) {
    var totalplayer = tplayer;
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
        $("#selectmod").show();
        
        // $("#player0Score").text(0);
        // $("#player1Score").text(0);
        // $("#player0Dart").text(0);
        // $("#player1Dart").text(0);
        $("#player0Remove").hide();
        $("#player1Remove").hide();
        $("#player2Remove").hide();
        $("#player3Remove").hide();
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
    // console.log("player is: " + id);
    // console.log($("#" + id + "Remove").hide());
    $("#" + id + "Remove").hide();

    if (player.search("Score") != -1) {
        // console.log("#" + id + "Score work");
        $("." + id + "Score").text(player.replace(id + "Score", ""));
        // console.log(id + "Score" + player.replace(id + "Score", ""));
    } else if (player.search("Break") != -1) {
        $("." + id + "Score").text(player.replace(id + "Score", ""));
    } else if (player.search("dart") != -1) {
        // console.log("#" + id + "Dart work");
        $("#" + id + "Dart").text(player.replace(id + "dartcount", ""));
        // console.log(id + "dartcount" + player.replace(id + "dartcount", ""));
    } else if (player.search("Removing" != -1)) {
        // console.log("#" + id + "Remove work");
        $("#" + id + "Remove").show();
    }
};
