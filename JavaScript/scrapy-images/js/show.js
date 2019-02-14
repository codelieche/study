$(function(){
    // 获取到background的Page
    var background = chrome.extension.getBackgroundPage();
    var results = [];
    if(background){
        results = background.results;
    }else{
        var msg = $("<span></span>").text("获取background为空");
        $(".images").append(msg);
    }
    // alert(results);
    if(results && results.length > 0){
        // 对数组去重操作: 在scrapy中去重，后续就不用去重了
        // $.unique(results.sort());

        for(var i=0; i <= results.length; i++){
            // alert(results[i]);
            // var span1 = $("<span contenteditable='true'></span>").text(results[i]);
            var span1 = $("<span></span>").text(results[i]);
            var img1 = $("<img />").attr("src", results[i]);
            // alert(img1)
            $(".images").append(span1, img1);
        };
    }else{
        var msg = $("<span></span>").text("图片为空");
        $(".images").append(msg);
    }

});