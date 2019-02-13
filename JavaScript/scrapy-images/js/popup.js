$(function(){
    // 给各按钮注册事件
    $("#copy").click(function(){
        // console.log("点击了复制按钮");
        var query = { active: true, currentWindow: true };
        chrome.tabs.query(query, function(tabs) {
            let tab = tabs[0];
            alert(`点击了复制按钮,当前tab ID为：${tab.id},url为：${tab.url}`);
        });
    });

    $("#scrapy").click(function(){
        // console.log("点击了爬取图片按钮");
        var query = {active: true, currentWindow: true};
        // 获取chrome的当前标签页
        chrome.tabs.query(query, function(tabs){
            var currentTab = tabs[0];
            // 发送一个消息出去
            var info = {
                job: "scrapy", 
                url: currentTab.url,
            }
            chrome.tabs.sendMessage(currentTab.id, info, null, function(response){
                // 这个回调函数接收返回值
                // alert(response.title);
                // alert(response.results);
                var results = response.results;
                for(var i=0; i <= results.length; i++){
                    // alert(results[i]);
                    var span1 = $("<span></span>").text(results[i]);
                    var img1 = $("<img />").attr("src", results[i]);
                    // alert(img1)
                    $(".images").append(span1, img1);
                }
            });
        });
    });

    $("#show").click(function(){
        console.log("点击了查看图片按钮");
    });
});

