/**
 * Created by wing on 2017/6/30.
 */
$(function () {
    Data = {};
    _version = new Date().getTime();

    var getLoginParms = function () {//封装数据
        Data.name = $("#username").val();
        Data.password = $("#password").val();
        Data.code = $("#checkNum").val();
    }

    $("#submit_btn").click(function () {
        if (checkUserInput() == "err") {
            return;
        }
        $("#login-mask").css("display", "block");
        setTimeout(function () {
        }, 5000);

        getLoginParms();//刷新data数据

        Wing.AJAX({
            type: "POST",
            data: Data,
            dataType: "JSON",
            url: "/UserLogin?" + _version,

            suc: function success(data) {
                if (data.statue == 1) {//密码错误
                    $("#login-mask").css("display", "none");
                    showInfo("密码错误!");
                } else if (data.statue == 2) {//用户名错误
                    $("#login-mask").css("display", "none");
                    showInfo("用户名错误!");
                } else if (data.statue == 3) { //验证码错误
                    $("#login-mask").css("display", "none");
                    $("#randomNums").click();
                    showInfo("验证码错误!");
                } else if (data.statue == 4) {//用户已经登录
                    $("#login-mask").css("display", "none");
                    showInfo("你已经登录啦!");

                    setTimeout(function () {
                        $("#container").empty();
                        $.get("main.html", function (result) {
                            console.log(result);
                            $("#container").html(result);
                        });
                    }, 2500)
                } else {//登录成功
                    setTimeout(function () {
                        $("#container").empty();
                        $("#container").html(data);
                        $.getScript("{% static 'js/main.js' %}");
                        $("#login-mask").css("display", "none");
                    }, 2000)

                }
            },
            err: function (data) {
                showInfo("ERROR");
            }
        })
    });

    function checkInput(Idata, name) {
        Wing.AJAX({
            type: "POST",
            data: Idata,
            dataType: "JSON",
            url: "/checkInput?" + _version,
            suc: function success(data) {
                if (data.statue == 5) {
                    $("#" + name + "_ERR").hide();
                    $("#" + name + "_OK").fadeIn(1);
                } else {
                    $("#" + name + "_OK").hide();
                    $("#" + name + "_ERR").fadeIn(1);
                }
            },
            err: function (data) {

            }
        })
    }

    $(".wing-input").keyup(function (e) {
        var inputName = $(this).attr("id");
        var _data = {};
        var name;
        switch (inputName) {
            case "username":
                _data = {"name": $(this).val()};
                _data.flag = 1;
                name = "name";
                break;

            case "password":
                _data = {"password": $(this).val()};
                name = "pwd";
                _data.flag = 2;
                break;
        }
        checkInput(_data, name);
    });

    function checkUserInput(e) {
        if ($("#username").val() == "" || $("#password").val() == "" || $("#checkNum").val() == "") {
            showInfo("请输入数据");
            return "err";
        }
    }

    function showInfo(info) {
        $("#show-info").html(info);
        $("#Err-info").stop().fadeIn(1).fadeOut(3500);
    }

    $(".wing-input").focus(function(){
        $(this).siblings().css("color","#428fff")
    }).blur(function () {
        $(this).siblings().css("color","#000")
    });

    function refresh_check_code(ths) {
        ths.src += '?';
        //src后面加问好会自动刷新验证码img的src#
    }

    $("#randomNums").click(function () {
        refresh_check_code(this);
        $("#checkNum").val("");
    });

    //click enter login
    $("body").keydown(function (e) {
        if (e.keyCode == 13) {
            $("#submit_btn").click();
        }
    });

    //  $(window).close(function(){
    //      alert(12);
    //     Wing.AJAX({
    //         type: "POST",
    //         data: {"name":Data.name},
    //         dataType: "JSON",
    //         url: "/loginout?" + _version,
    //         suc: function success(data) {
    //             console.log("OK");
    //         },
    //         err: function (data) {
    //
    //         }
    //     })
    // });

});