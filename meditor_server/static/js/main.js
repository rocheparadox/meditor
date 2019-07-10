function getJsonKeys(jsonObject){
    var keys = [];
    for(var key in jsonObject){
        keys.push(key);
    }
    
    return keys;
}