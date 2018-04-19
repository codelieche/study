const { injectBabelPlugin } = require('react-app-rewired');
const rewireLess = require('react-app-rewire-less');

module.exports = function override(config, env) {
    // do stuff with the webpack config...
    // config = injectBabelPlugin(['import', { libraryName: 'antd', libraryDirectory: 'es', style: true }], config);
    config = injectBabelPlugin(['import', { libraryName: 'antd', style: true }], config);

    config = rewireLess.withLoaderOptions({
        // 修改antd的主色调：antd2.x->3.0: 组件主色由 『#108EE9』 改为 『#1890FF』
        modifyVars: {
            "@primary-color": "#108EE9",
            "@font-size-base": '13px',
        },
    })(config, env);

    return config;
};