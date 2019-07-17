function getJsonKeys(jsonObject){
    var keys = [];
    for(var key in jsonObject){
        keys.push(key);
    }
    
    return keys;
}

function makeAjaxCall(ajaxUrl, ajaxCallType, parameters){
    console.log("Going to make ajax call ", ajaxUrl, ajaxCallType, parameters);
    jQuery.ajax({
        url:ajaxUrl,
        data:JSON.stringify(parameters),
        type:ajaxCallType,
        contentType: 'application/json;charset=UTF-8',
        success:function(data){
            alert(data);
        }
    });
}