/**
 * 用户验证相关的函数
 */

export function CheckLogined({ history, match, location }) {
    // 首先get访问，判断是否成功登陆了
    //  如果登陆了，就返回true，没登陆
    const url = "http://127.0.0.1:8080/api/v1/account/login";
    fetch(url, { credentials: 'include' })
        .then(response => response.json())
        .then(data => {
            if (data.logined) {
                return true;
            } else {
                // 没有登陆的话，就跳转去login页面
                history.push("/user/login?next=" + location.pathname);
            }
        });
}

export default CheckLogined;
