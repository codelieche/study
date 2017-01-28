#coding:utf8
# from fabric.contrib.files import append, exists, sed
from fabric.api import env, run
from fabric.context_managers import cd

from deploy_jobs import _create_directory_structure_if_necessary
from deploy_jobs import _get_latest_source
from deploy_jobs import _update_settings
from deploy_jobs import _update_virtualenv
from deploy_jobs import _update_static_files
from deploy_jobs import _update_database

env.user = 'happy'
env.hosts = ['192.168.0.121']
SITE_NAME = 'test.tdd.staging.codelieche.com'

def deploy():

    SERVER_ADDRESS = 'test.tdd.staging.codelieche.com'
    site_folder = '/home/%s/sites/%s' % (env.user, SERVER_ADDRESS)
    # site_folder = '/data/www/%s' %(SERVER_ADDRESS)
    source_folder = site_folder + '/source'

    # 第1步: 创建目录结构
    _create_directory_structure_if_necessary(site_folder)
    return
    # 第2步：拉取最新源码
    _get_latest_source(source_folder)
    # 第3步：修改项目配置信息
    _update_settings(source_folder, SITE_NAME)
    # 第4步: 更新虚拟环境
    _update_virtualenv(source_folder)
    # 第5步：更新静态文件
    _update_static_files(source_folder)
    # 第6步：更新数据库
    _update_database(source_folder)


def deploy_settings():
    run('sudo supervisorctl status codelieche')
    site_folder = '/home/%s/sites/%s' % (env.user, SITE_NAME)
    source_folder = site_folder + '/source'
    # 第一步：写入nginx的配置
    with cd(source_folder):
        # 进入source_folder
        run('pwd')
        run('sed "s/SITENAME/%s/g" deploy_tools/nginx.template.conf |'\
            ' sed "s/USERNAME/happy/g" | sudo tee /etc/nginx/sites-enabled/%s' % (
                SITE_NAME,SITE_NAME))
    # 第二步: 写入gunicorn执行脚本
    with cd(source_folder):
        # 进入source_folder
        run('sed "s/SITENAME/%s/g" deploy_tools/gunicorn-run.template.sh |'\
            ' sed "s/USERNAME/happy/g" | tee ../run.sh' % (
                SITE_NAME,))
        # 修改run.sh的权限
        run('chmod +x ../run.sh')

    # 第三步：添加supervisor配置
    with cd(source_folder):
        # 进入source_folder
        run('sed "s/SITENAME/%s/g" deploy_tools/gunicorn-supervisor.template.conf |'\
            ' sed "s/USERNAME/happy/g" | sudo tee /etc/supervisor/conf.d/tdd_django.conf' % (
                SITE_NAME,))

def reload():
    run('sudo supervisorctl restart tdd_django')

def hello():
    print('Hello fab!')
