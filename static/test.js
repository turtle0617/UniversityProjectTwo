var totalplayer;


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

        return false;
    });
    $('#CR').click(function() {
        // console.log('clicked2', this.id);
        $("#cricket").show();
        $("#Scoreshow").hide();
        $("#selectmod").hide();
        

        return false;
    });
});

//01Game 按鈕觸發
$(function() {
    var mod = 0;
    $('#301,#501,#701').click(function() {
        $("#InOutchoice").show();
        $("#cricket").hide();
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
            $this.attr('class', "btn btn-secondary")
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
        $("#cricket").hide();
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
                break;
            case "2":
                InOut = "player0" + $("#cplayer0In").val() + "and" + $("#cplayer0Out").val() + "/" +
                    "player1" + $("#cplayer1In").val() + "and" + $("#cplayer1Out").val();
                $(".player0Score").text(mod);
                $(".player1Score").text(mod);
                $(".player2Score").text(mod);
                $(".player3Score").text(mod);
                break;
            case "3":
                InOut = "player0" + $("#cplayer0In").val() + "and" + $("#cplayer0Out").val() + "/" +
                    "player1" + $("#cplayer1In").val() + "and" + $("#cplayer1Out").val() + "/" +
                    "player2" + $("#cplayer2In").val() + "and" + $("#cplayer2Out").val();
                $(".player0Score").text(mod);
                $(".player1Score").text(mod);
                $(".player2Score").text(mod);
                $(".player3Score").text(mod);
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
                break;
        }
    });
});