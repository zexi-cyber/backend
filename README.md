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
        'NAME': '', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1
        'PORT': 3306, # 端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '', # 数据库密码吗
    }
}
```
4.若数据库发生改变
```
python manage.py makemigrations data
python manage.py migrate data
```


## 运行
进后端文件夹
```
cd backend
```
在8000端口运行后端
```
python manage.py runserver 
```
## 大模型查询接口

### 请求地址

```
localhost:8080/query/
```

### 请求方式

```
POST
```

### 数据格式
```
{
	"inputx": "七彩虹所生产得所有型号显卡得价格，按价格大小排降序"
}
```

### 返回数据
```
{
    "code": 200,
    "message": [
        [
            "10449.00"
        ],
        [
            "3499.00"
        ],
        [
            "14999.00"
        ],
        [
            "9599.00"
        ],
        [
            "1199.00"
        ],
        [
            "5499.00"
        ]
    ],
    "sql": " SELECT data_price.price FROM data_Price JOIN data_GPU ON data_Price.GPU_id = data_gpu.id JOIN data_Brand ON
     data_Price.Brand_id = data_brand.id WHERE data_Brand.name = 'COLORFUL' ORDER BY data_price.price DESC; "
```
### 绘制发烧级显卡的价格图接口
### 请求地址

```
localhost:8080/painting/
```

### 请求方式

```
POST
```

### 数据格式
```
{
	"inputx": ""无输入
}
```

### 返回数据
```
{
   {
    "code": 200,
    "message": [
        [
            "Radeon RX 7900 XTX",
            "7699.00"
        ],
        [
            "GeForce RTX 4080 SUPER",
            "8099.00"
        ],
        [
            "GeForce RTX 4090",
            "14999.00"
        ],
        [
            "GeForce RTX 4080 SUPER",
            "8899.00"
        ],
        [
            "GeForce RTX 4090",
            "16998.00"
        ],
        [
            "GeForce RTX 4080 SUPER",
            "12489.00"
        ],
        [
            "GeForce RTX 4090",
            "12999.00"
        ],
        [
            "GeForce RTX 4080 SUPER",
            "9599.00"
        ],
        [
            "Radeon RX 7900 XTX",
            "9199.00"
        ],
        [
            "GeForce RTX 4090 D",
            "14999.00"
        ],
        [
            "GeForce RTX 4090",
            "20599.00"
        ]
    ],
    "sql": "SELECT data_GPU.GPU_name, data_price.price FROM data_Price JOIN data_GPU ON data_Price.GPU_id = data_gpu.id WHERE data_GPU.type = '发烧级' ORDER BY data_price.price DESC; "
}
    "sql": " SELECT data_price.price FROM data_Price JOIN data_GPU ON data_Price.GPU_id = data_gpu.id JOIN data_Brand ON
     data_Price.Brand_id = data_brand.id WHERE data_Brand.name = 'COLORFUL' ORDER BY data_price.price DESC; "
```


