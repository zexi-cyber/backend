## data-copilot back

1. 安装python3.9
2. 命令行输入 
```
pip install -r requirements.txt
```
3. 修改settings.py中的数据库配置
```
DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'data_copilot', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1
        'PORT': 3306, # 端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'root', # 数据库密码吗
    }
}
```
## 运行

```
python manage.py runserver 
```
