var c01 = require('./c01.js');
var countup = require('./countup.js');
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
    sendMsg: function(gamemode, InOut) {
        // console.log($("#howmany option:selected").val() + gamemode);
        totalplayer = $("#howmany option:selected").val();
        chatObj.socket.send($("#howmany option:selected").val() + " " + gamemode + " " + InOut);
        // console.log($("#howmany option:selected").val() + " " + gamemode+ " "  + InOut);

    },
    // 顯示訊息
    showMsg: function(message) {
        if (message.search("c01") != -1) {
            c01(message.replace("c01", ""), totalplayer)
            console.log(message);
        } else if (message.search("countup") != -1) {
            countup(message.replace("countup", ""), totalplayer);
            console.log(message);

        }
        // countup(message);

    }
};

//Countup 按鈕觸發

$(function() {
    $('#countup').click(function() {
        // console.log('clicked2', this.id);
        $("#Scoreshow").show();
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

        chatObj.sendMsg(this.id, "");
        return false;
    });
    chatObj.init();
});

//01Game 按鈕觸發
$(function() {
    var mod = 0;
    $('#301,#501,#701').click(function() {
        $("#InOutchoice").show();
        $("#selectmod").hide();
        mod = this.id;
        totalplayer = $("#howmany option:selected").val();
        switch (totalplayer) {
            case "1":
                // console.log(totalplayer);
                $("#cplayer0").show()
                $("#cplayer1").hide()
                $("#cplayer2").hide()
                $("#cplayer3").hide()
                break;
            case "2":
                // console.log(totalplayer);
                $("#cplayer0").show()
                $("#cplayer1").show()
                $("#cplayer2").hide()
                $("#cplayer3").hide()
                break;
            case "3":
                // console.log(totalplayer);
                $("#cplayer0").show()
                $("#cplayer1").show()
                $("#cplayer2").show()
                $("#cplayer3").hide()
                break;
            case "4":
                // console.log(totalplayer);
                $("#cplayer0").show()
                $("#cplayer1").show()
                $("#cplayer2").show()
                $("#cplayer3").show()
                break;
        };
    });

    $('#cplayer0In,#cplayer0Out,#cplayer1In,#cplayer1Out,#cplayer2In,#cplayer2Out,#cplayer3In,#cplayer3Out').click(function() {
        var $this = $(this);
        if ($this.val() == "Open") {
            $this.text('Double');
            $this.val("Double");
            $this.attr('class', "btn btn-warning")
                // console.log($this.val());
        } else if ($this.val() == "Double") {
            $this.text('Master');
            $this.val("Master");
            $this.attr('class', "btn btn-danger")
                // console.log($this.val());
        } else if ($this.val() == "Master") {
            $this.text('Open');
            $this.val("Open")
            $this.attr('class', "btn btn-dark")
                // console.log($this.val());
        }
    });
    $("#InOutback").click(function() {
        $("#InOutchoice").hide();
        $("#selectmod").show();
    });
    $("#InOutGO").click(function() {
        totalplayer = $("#howmany option:selected").val();
        $("#Scoreshow").show();
        $("#InOutchoice").hide();
        // $("#selectmod").hide();
        // console.log(totalplayer + mod);
        switch (totalplayer) {
            case "1":
                InOut = "player0" + $("#cplayer0In").val() + "and" + $("#cplayer0Out").val();
                $(".player0Score").text(mod);
                $(".player1Score").text(mod);
                $(".player2Score").text(mod);
                $(".player3Score").text(mod);
                chatObj.sendMsg(mod, InOut);
                break;
            case "2":
                InOut = "player0" + $("#cplayer0In").val() + "and" + $("#cplayer0Out").val() + "/" +
                    "player1" + $("#cplayer1In").val() + "and" + $("#cplayer1Out").val();
                $(".player0Score").text(mod);
                $(".player1Score").text(mod);
                $(".player2Score").text(mod);
                $(".player3Score").text(mod);
                chatObj.sendMsg(mod, InOut);
                break;
            case "3":
                InOut = "player0" + $("#cplayer0In").val() + "and" + $("#cplayer0Out").val() + "/" +
                    "player1" + $("#cplayer1In").val() + "and" + $("#cplayer1Out").val() + "/" +
                    "player2" + $("#cplayer2In").val() + "and" + $("#cplayer2Out").val();
                $(".player0Score").text(mod);
                $(".player1Score").text(mod);
                $(".player2Score").text(mod);
                $(".player3Score").text(mod);
                chatObj.sendMsg(mod, InOut);
                break;
            case "4":
                InOut = "player0" + $("#cplayer0In").val() + "and" + $("#cplayer0Out").val() + "/" +
                    "player1" + $("#cplayer1In").val() + "and" + $("#cplayer1Out").val() + "/" +
                    "player2" + $("#cplayer2In").val() + "and" + $("#cplayer2Out").val() + "/" +
                    "player3" + $("#cplayer3In").val() + "and" + $("#cplayer3Out").val();
                $(".player0Score").text(mod);
                $(".player1Score").text(mod);
                $(".player2Score").text(mod);
                $(".player3Score").text(mod);
                chatObj.sendMsg(mod, InOut);
                break;
        }
    });
    chatObj.init();
});