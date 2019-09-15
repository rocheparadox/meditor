function getJsonKeys(jsonObject){
    var keys = [];
    for(var key in jsonObject){
        keys.push(key);
    }

    return keys;
}

function makeAjaxCall(ajaxUrl, ajaxCallType, parameters){
    //console.log("Going to make ajax call ", ajaxUrl, ajaxCallType, parameters);
    jQuery.ajax({
        url:ajaxUrl,
        data:JSON.stringify(parameters),
        type:ajaxCallType,
        contentType: 'application/json;charset=UTF-8',
        success:function(data){
            //console.log("From ajax methiod success function  " + data)
            return data;
        }
    });
}

function makeAjaxCall(ajaxUrl, ajaxCallType, parameters, isAsync){
   // console.log("Going to make ajax call ", ajaxUrl, ajaxCallType, parameters);
    var response;
    jQuery.ajax({
        url:ajaxUrl,
        data:JSON.stringify(parameters),
        type:ajaxCallType,
        contentType: 'application/json;charset=UTF-8',
        async: isAsync,
        success:function(data){
            //console.log("From ajax methiod success function  " + data)
            response = data;
        }

    });

    return response;
}

function getJsonKeys(jsonObject){
    var keys = [];
    for(var key in jsonObject){
        keys.push(key);
    }

    return keys;
}
