/**
 * Created by DLH_PCM on 2018/1/4.
 */

function toPost(url, param) {
    var paramstr = Paramstr(param);
    var data = null;
    $.ajax({
        type: "Post",
        async: false, //改为同步方式
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        // data: paramstr,
        data: {'fav_id': 1, 'fav_type': 2},
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        success: function (json) {
            data = json;
        },
        error: function (err) {
            alert("请求失败，请重试！");
            data = null
        }
    });
    return data;
}

function Paramstr(param) {
    var midparam = {};
    midparam.param = "";
    var key;
    for (key in param)
        midparam.param += "(~,~)" + key + "=" + param[key];
    var str = midparam.param = midparam.param.substring(5, midparam.param.length);
    return str;
}
function num() {
    var mm = Math.random();
    var six = "";
    if (mm > 0.1) {
        six = Math.round(mm * 1000000);
    } else {
        mm += 0.1;
        six = Math.round(mm * 1000000);
    }
    return six;
}
function PageParam(param) {
    var midparam = {};
    midparam.param = "";
    var key;
    for (key in param)
        midparam.param += "(~,~)" + key + "=" + param[key];
    var str = midparam.param = midparam.param.substring(5, midparam.param.length);
    return str;
}

