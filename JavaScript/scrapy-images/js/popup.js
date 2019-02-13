function scrapyTabImages(showImages, openNewTab){
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
                if(response && response.results){
                    var results = response.results;
                    
                    // 是否在popup页面显示图片
                    if(showImages){
                        for(var i=0; i <= results.length; i++){
                            // alert(results[i]);
                            var span1 = $("<span></span>").text(results[i]);
                            var img1 = $("<img />").attr("src", results[i]);
                            // alert(img1)
                            $(".images").append(span1, img1);
                        };
                    }
                    
                    // 把results传给background的Page
                    var background = chrome.extension.getBackgroundPage();
                    background.results = results;

                    // 是否打开新的页面查看图片
                    if(openNewTab){
                      // 跳转到查看页面
                      chrome.tabs.create({"url": "pages/show.html"});
                    }
                   

                }else{
                    var msg = $("<span></span>").text("返回的结果不规范！");
                    $(".images").append(msg);
                }
            });
        });
}


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
        scrapyTabImages(true, false);
    });

    $("#show").click(function(){
        // console.log("点击了查看图片按钮");
        scrapyTabImages(false, true);

        // chrome.tabs.create({"url": "pages/show.html"});

    });
});

