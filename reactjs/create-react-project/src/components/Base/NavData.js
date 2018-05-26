var navData = [
    {
        icon: 'desktop',
        key: 'front',
        title: '前端开发',
        subs: [
            {
                slug: '/front/html',
                icon: 'right',
                title: 'Html/CSS',
            },
            {
                slug: '/front/js',
                icon: 'right',
                title: 'JavaScritp',
            },
            {
                slug: '/front/react',
                icon: 'right',
                title: 'React.js',
            },
            {
                slug: '/front/vue',
                icon: 'right',
                title: 'Vue.js',
            }
        ]
    },
    {
        icon: 'global',
        key: 'backend',
        title: '后端开发',
        subs: [
            {
                slug: '/backend/python',
                icon: 'right',
                title: 'Python'
            },
            {
                slug: '/backend/django',
                icon: 'right',
                title: 'Django'
            },
            {
                slug: '/backend/golang',
                icon: 'right',
                title: 'Golang'
            },
            {
                slug: '/backend/java',
                icon: 'right',
                title: 'Java'
            }
        ]
    },
    {
        icon: 'database',
        key: 'database',
        title: '数据库',
        subs: [
            {
                slug: '/database/mysql',
                icon: 'right',
                title: 'MySQL'
            },
            {
                slug: '/database/redis',
                icon: 'right',
                title: 'Redis'
            },
            {
                slug: '/database/mongodb',
                icon: 'right',
                title: 'MongoDB'
            },
        ]
    },
    {
        icon: 'cloud',
        key: 'cloud',
        title: '容器技术',
        subs: [
            {
                slug: '/cloud/docker',
                icon: 'right',
                title: 'Docker'
            },
            {
                slug: '/cloud/kubernetes',
                icon: 'right',
                title: 'Kubernetes'
            },
            {
                slug: '/cloud/jenkinx',
                icon: 'right',
                title: 'Jenkin X'
            }
        ]
    },
    {
        icon: 'team',
        key: 'user',
        title: '用户中心',
        subs: [
            {
                slug: '/user/group',
                icon: 'usergroup-add',
                title: '分组',
            },
            {
                slug: '/user/list',
                icon: 'user',
                title: '所有用户',
            },
            {
                slug: '/user/message',
                icon: 'message',
                title: '消息中心',
            },
            {
                slug: '/user/login',
                icon: 'user',
                title: '登陆',
            },
            {
                slug: '/user/logout',
                icon: 'logout',
                title: '退出',
            },
        ]
    },
    {
        icon: "question-circle-o",
        key: "help",
        title: "帮助中心",
        url: "/help",
    },
    {
        icon: "home",
        key: "test",
        title: "测试页面",
        url: "/test",
    }
]

export default navData;