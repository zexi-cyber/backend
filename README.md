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
python manage.py runserver 8000
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
        {
            "name": "华硕",
            "GPU_name": "GeForce RTX 4090",
            "price": "20599.00"
        },
        {
            "name": "技嘉",
            "GPU_name": "GeForce RTX 4090",
            "price": "16998.00"
        },
        {
            "name": "COLORFUL",
            "GPU_name": "GeForce RTX 4090",
            "price": "14999.00"
        },
        {
            "name": "COLORFUL",
            "GPU_name": "GeForce RTX 4090 D",
            "price": "14999.00"
        },
        {
            "name": "NVIDIA",
            "GPU_name": "GeForce RTX 4090",
            "price": "12999.00"
        },
        {
            "name": "华硕",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "12489.00"
        },
        {
            "name": "COLORFUL",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "9599.00"
        },
        {
            "name": "技嘉",
            "GPU_name": "Radeon RX 7900 XTX",
            "price": "9199.00"
        },
        {
            "name": "技嘉",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "8899.00"
        },
        {
            "name": "NVIDIA",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "8099.00"
        },
        {
            "name": "蓝宝石",
            "GPU_name": "Radeon RX 7900 XTX",
            "price": "7699.00"
        }
    ],
    "sql": "\nSELECT data_Brand.name, data_GPU.GPU_name, data_price.price \nFROM data_Price \nJOIN data_GPU ON data_Price.GPU_id = data_GPU.id \nJOIN data_Brand ON data_Price.Brand_id = data_Brand.id \nWHERE data_GPU.type = '发烧级'\nORDER BY data_price.price DESC;"
}
```
### 绘制发烧级显卡的价格图接口
### 请求地址

```
localhost:8080/painting/
```

### 请求方式

```
GET
```

### 返回数据
```
{
    "code": 200,
    "message": [
        {
            "name": "华硕",
            "GPU_name": "GeForce RTX 4090",
            "price": "20599.00"
        },
        {
            "name": "技嘉",
            "GPU_name": "GeForce RTX 4090",
            "price": "16998.00"
        },
        {
            "name": "COLORFUL",
            "GPU_name": "GeForce RTX 4090",
            "price": "14999.00"
        },
        {
            "name": "COLORFUL",
            "GPU_name": "GeForce RTX 4090 D",
            "price": "14999.00"
        },
        {
            "name": "NVIDIA",
            "GPU_name": "GeForce RTX 4090",
            "price": "12999.00"
        },
        {
            "name": "华硕",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "12489.00"
        },
        {
            "name": "COLORFUL",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "9599.00"
        },
        {
            "name": "技嘉",
            "GPU_name": "Radeon RX 7900 XTX",
            "price": "9199.00"
        },
        {
            "name": "技嘉",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "8899.00"
        },
        {
            "name": "NVIDIA",
            "GPU_name": "GeForce RTX 4080 SUPER",
            "price": "8099.00"
        },
        {
            "name": "蓝宝石",
            "GPU_name": "Radeon RX 7900 XTX",
            "price": "7699.00"
        }
    ],
    "sql": "SELECT data_brand.name, data_GPU.GPU_name, data_price.price FROM data_Price JOIN data_GPU ON data_Price.GPU_id = data_GPU.id JOIN data_Brand ON data_Price.Brand_id = data_Brand.id WHERE data_GPU.type = '发烧级' ORDER BY data_price.price DESC;"
}
```

# 状态码

```
200: 请求成功
300: 无相关数据
400: 请求权限不足
500：请求失败
```


