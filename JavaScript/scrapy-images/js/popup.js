$(function(){
    // 给各按钮注册事件
    $("#copy").click(function(){
        console.log("点击了复制按钮");
        var query = { active: true, currentWindow: true };
        chrome.tabs.query(query, function(tabs) {
            let tab = tabs[0];
            // for(var i in tab){
            //     alert(i);
            // }
            alert("点击了复制按钮,当前tab ID为：" + tab.id);
        });
    });

    $("#scrapy").click(function(){
        console.log("点击了爬取图片按钮");
    });
    $("#show").click(function(){
        console.log("点击了查看图片按钮");
    });
});

