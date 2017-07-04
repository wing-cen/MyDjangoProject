/**
 * Created by wing on 2017/6/23.
 */

var Wing = {
    AJAX: function (option) {
        $.ajax({
            type: option.type,
            url: option.url,
            data: option.data,
            contentType: option.contentType,
            processData: option.processData,
            dataType: option.datatype,
            timeout: option.timeout,
            async: option.async,
            success: option.suc,
            error: option.err
        });
    },
    checkBrowserVer: function(){

    },

    getVersion:function(){
        var version  = new Date().getTime();
        return version;
    },
    Data:{},
}

checkInputEnum = {
    "checkRight" : 3,
    "checkPassword" : 2,
    "checkUserName" : 1
}


