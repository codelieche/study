// 监听消息
// chrome.runtime.onMessageExternal.addListener
chrome.extension.onMessage.addListener(function(request, sender, sendResponse){
    if(request.job === "copy"){
        alert("收到了copy的消息");
    }

    if(request.job === "scrapy"){
        // alert("收到了scrapy的消息");
        // alert(sender);
        // alert(sendResponse);
        
        var results = ScrapyImages(request.url);

        let response = {
            title: "scrapy job response",
            results: results
        };
        // alert(response.results);
        sendResponse(response);
    }

    if(request.job === "show"){
        alert("收到了show的消息");
    }
});



function ScrapyImages(url){
    var results = [];
    $("img").each(function(){
        // alert($(this).text());
        var imageSrc = $(this).attr("src");
        // 判断图片地址是否需要加host
        if(imageSrc && (! imageSrc.startsWith("http")) ){
            if(imageSrc.startsWith("//")){
                imageSrc = imageSrc.replace("//", "http://");
            }else if(imageSrc.startsWith("data")){
                // 无需处理
            }else{
                var re = new RegExp("(htt.*?:\/\/.*?)\/.*");
                var host = re.exec(url)[1];
                imageSrc = host + imageSrc;
            }
            
        }
        // 判断元素是否在数组中
        if(results.indexOf(imageSrc) < 0){
            results.push(imageSrc);
        }
    });

    return results;
}
