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
    sendMsg: function() {
        var msg_input = $("#msg-btn")
        chatObj.socket.send(msg_input.val());
    },
    // 顯示訊息
    showMsg: function(message) {
        mesif(message);
    }
};

function mesif(mes) {
    if (mes.search("Player0") != -1) {
        player0(mes);
    } else if (mes.search("Player1") != -1) {
        player1(mes);

    } else if (mes.search("over") != -1) {
        $("#player0Score").text(0);
        $("#player1Score").text(0);
        $("#player0Dart").text(0);
        $("#player1Dart").text(0);
    } else {
        $("#Bar").text(mes);
    }
};

function player0(player0) {
    if (player0.search("Score") != -1) {
        $("#player0Score").text(player0.replace("Player0Score", ""));
        console.log("Player0Score" + player0.replace("Player0Score", ""));
    } else if (player0.search("dart") != -1) {
        $("#player0Dart").text(player0.replace("Player0dartcount", ""));
        console.log("Player0dartcount" + player0.replace("Player0dartcount", ""));
    }
};

function player1(player1) {
    if (player1.search("Score") != -1) {
        $("#player1Score").text(player1.replace("Player1Score", ""));
        console.log("Player1Score" + player1.replace("Player1Score", ""));
    } else if (player1.search("dart") != -1) {
        $("#player1Dart").text(player1.replace("Player1dartcount", ""));
        console.log("Player1dartcount" + player1.replace("Player1dartcount", ""));
    }
};


$(function() {
    var btn = $("#msg-btn");
    // 綁定按鈕 click 時發送訊息
    btn.click(function() {
        chatObj.sendMsg();
        // btn.hide();
        return false;
    });
    chatObj.init();
});