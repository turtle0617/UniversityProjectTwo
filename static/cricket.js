//第一層字串判斷
module.exports = function cricket(mes, tplayer) {
    var totalplayer = tplayer;
    // console.log(mes);
    if (mes.search("player0") != -1) {

        player(mes.replace("player0", ""), "player0");
    } else if (mes.search("player1") != -1) {
        player(mes.replace("player1", ""), "player1");

    } else if (mes.search("GameOver") != -1) {
        mes = mes.replace("GameOver", "");
        console.log("mes :" + mes);
        console.log("mes :" + ".player" + mes + "Score");
        $("#CRBar").text("Game over");
        for (var i = 15; i < 21; i++) {
            $("#player0_" + i + "block").hide();
            $("#player1_" + i + "block").hide();
            $("#player1_" + i + "block").attr("src", "/static/2.png");
            $("#player1_" + i + "block").attr("src", "/static/2.png");
        }

        $("#player0_Bullblock").hide();
        $("#player1_Bullblock").hide();
        $("#player1_Bullblock").attr("src", "/static/2.png");
        $("#player1_Bullblock").attr("src", "/static/2.png");

        $("#selectmod").show();
        $(".player" + mes + "Score").text(0);
        $("#player" + mes + "Dart").text(0);
        $("#player1Remove").hide();
        $("#player2Remove").hide();
        $("#player3Remove").hide();
    } else if (mes.search("Round") != -1) {
        // console.log("CRBar mes :" + mes);
        $("CRdart").text(0);
        $("#CRBar").text(mes);
    } else {
        $("#CRBar").text(mes);

    }
};
//第二層字串判斷。由於玩家人數無法每次都得知故把id採用變數避免過多一樣的函式很醜！
function player(player, mestext) {
    var id = mestext;
    console.log("mestext : "+mestext);
    $("#" + id + "Remove").hide();
    $("#" + id + "Break").hide();
    if (player.search("score") != -1) {
        $(".CR" + id + "Score").text(player.replace("score", ""));
    } else if (player.search("block") != -1) {
        var aa = player.replace("block","");
        console.log("else if block and mes :"+aa);
        switch (aa) {
            case "15is1.0":
                $("#" + id + "_15block").show();
                console.log("_15_1block.show");
                break;
            case "15is2.0":
                $("#" + id + "_15block").show();
                $("#" + id + "_15block").attr("src", "/static/2.png");
                console.log("_15_2block.show");
                break;
            case "15is3.0":
                $("#" + id + "_15block").show();
                $("#" + id + "_15block").attr("src", "/static/3.png");
                console.log("_15_3block.show");
                break;
            case "16is1.0":
                $("#" + id + "_16block").show();
                console.log("_16_1block.show");
                break;
            case "16is2.0":
                $("#" + id + "_16block").show();
                $("#" + id + "_16block").attr("src", "/static/2.png");
                console.log("_16_2block.show");
                break;
            case "16is3.0":
                $("#" + id + "_16block").show();
                $("#" + id + "_16block").attr("src", "/static/3.png");
                console.log("_16_3block.show");
                break;
            case "17is1.0":
                $("#" + id + "_17block").show();
                console.log("_17_1block.show");
                break;
            case "17is2.0":
                $("#" + id + "_17block").show();
                $("#" + id + "_17block").attr("src", "/static/2.png");
                console.log("_17_2block.show");
                break;
            case "17is3.0":
                $("#" + id + "_17block").show();
                $("#" + id + "_17block").attr("src", "/static/3.png");
                console.log("_17_3block.show");
                break;
            case "18is1.0":
                $("#" + id + "_18block").show();
                console.log("_18_1block.show");
                break;
            case "18is2.0":
                $("#" + id + "_18block").show();
                $("#" + id + "_18block").attr("src", "/static/2.png");
                console.log("_18_2block.show");
                break;
            case "18is3.0":
                $("#" + id + "_18block").show();
                $("#" + id + "_18block").attr("src", "/static/3.png");
                console.log("_18_3block.show");
                break;
            case "19is1.0":
                $("#" + id + "_19block").show();
                console.log("_19_1block.show");
                break;
            case "19is2.0":
                $("#" + id + "_19block").show();
                $("#" + id + "_19block").attr("src", "/static/2.png");
                console.log("_19_2block.show");
                break;
            case "19is3.0":
                $("#" + id + "_19block").show();
                $("#" + id + "_19block").attr("src", "/static/3.png");
                console.log("_19_3block.show");
                break;
            case "20is1.0":
                $("#" + id + "_20block").show();
                console.log("_20_1block.show");
                break;
            case "20is2.0":
                $("#" + id + "_20block").show();
                $("#" + id + "_20block").attr("src", "/static/2.png");
                console.log("_20_2block.show");
                break;
            case "20is3.0":
                $("#" + id + "_20block").show();
                $("#" + id + "_20block").attr("src", "/static/3.png");
                console.log("_20_3block.show");
                break;
            case "50is1.0":
                $("#" + id + "_Bullblock").show();
                console.log("_Bull_1block.show");
                break;
            case "50is2.0":
                $("#" + id + "_Bullblock").show();
                $("#" + id + "_Bullblock").attr("src", "/static/2.png");
                console.log("_Bull_2block.show");
                break;
            case "50is3.0":
                $("#" + id + "_Bullblock").show();
                $("#" + id + "_Bullblock").attr("src", "/static/3.png");
                console.log("_Bull_3block.show");
                break;
        }

    } else if (player.search("dart") != -1) {
        console.log("#" + id + "Dart work");
        console.log(player);
        $(".CRdart").text(player.replace("dartcount", ""));
        // console.log(id + "dartcount" + player.replace(id + "dartcount", ""));
    } else if (player.search("Removing" != -1)) {
        console.log("#" + id + "Remove work");
        console.log(player);
        $("#CRBar").text("Removing Dart ...");
    }
};