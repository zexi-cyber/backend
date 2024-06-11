
import dashscope
dashscope.api_key=" sk-cf95d70110f54c8ab799a58965bebb12"

from dashscope import Generation
import re

def get_response(messages):
    response = Generation.call(model="qwen-max",
                               messages=messages,
                               # 将输出设置为"message"格式
                               result_format='message')
    return response
def get_sql(inputx):
    m = """
    from django.db import models

    class Brand(models.Model):
        name = models.CharField(max_length=256)
        stablish_time = models.DateField()
        ceo = models.CharField(max_length=256)
        brand_detail = models.OneToOneField("BrandDetail", on_delete=models.CASCADE)

    class BrandDetail(models.Model):
        headquarters = models.CharField(max_length=256)
        founder = models.CharField(max_length=256)
        market_ocp = models.DecimalField(max_digits=10, decimal_places=2)

    class GPU(models.Model):
        GPU_name = models.CharField(max_length=256)
        type = models.CharField(max_length=256)
        frequency = models.DecimalField(max_digits=10, decimal_places=2)
        power_dissipation = models.DecimalField(max_digits=10, decimal_places=2)
        VRAM_cap = models.DecimalField(max_digits=10, decimal_places=2)
        VRAM_type = models.CharField(max_length=256)
        publish_time = models.DateField()
            class Price(models.Model):
        Brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
        GPU = models.ForeignKey("GPU", on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        因为是用的Django架构中的data app中的models.py文件创建的，所以每张表前都会有“data_”前缀，你在使用这些表名的时候一定要加上
        这里我再给你一些提示data_Brand表通过外键brand_detail_id和data_branddetail表一对一连接，所以你在使用JOIN连接这两张表的时候要使用
        brand_detail_id=data_branddetail.id作为连接条件，而data_Price表通过外键GPU_id和data_gpu连接，所以你在使用JOIN连接这两张表的时候要使用
        data_price.GPU_id=data_gpu.id作为连接条件,同理data_Price表通过外键Brand_id和data_brand连接，所以你在使用JOIN连接这两张表的时候要使用
        data_price.Brand_id=data_brand.id作为连接条件
        NVIDIA的中文名叫英伟达，COLORFUL的中文名叫做七彩虹，Intel的中文名叫英特尔，MOORE_THREADS的中文名叫做摩尔线程，AMD没有中文名。剩余的几家厂商都是中文名，
        他们分别是：华硕、技嘉、蓝宝石。
        在查询AMD、华硕、技嘉、蓝宝石这几家厂商（Brand）时，不要用英文或者拼音去替代他们本来的名称。
        下面是一些显卡名称（GPU_name）的简称
        GeForce RTX 4090简称4090;  GeForce RTX 4090 D简称 4090 D;  Radeon RX 7900 XTX简称 7900XTX； 
        GeForce RTX 4080 SUPER简称 4080 SUPER; GeForce RTX 4080简称 4080; Radeon RX 7900 XT简称 7900XT 
        GeForce RTX 4070简称 4070; Radeon RX 6950 XT简称 6950 XT; GeForce RTX 3060简称 3060; GTX 1650简称 1650
        Radeon RX 6650 XT简称 6650 XT; Radeon RX 6500 XT简称 6500 XT 
        你在写SQL语句的时候不能用简写 ，4090和4090 D完全不是一码事，查询4090有关信息的时候不要出现4090D
        比如查询4090的均价时，这样写：
        SELECT AVG(data_price.price) AS average_price
        FROM data_Price
        JOIN data_GPU ON data_Price.GPU_id = data_gpu.id
        WHERE data_GPU.GPU_name = 'GeForce RTX 4090' 
        不要写：
        SELECT AVG(data_price.price) AS average_price
        FROM data_Price
        JOIN data_GPU ON data_Price.GPU_id = data_gpu.id
        WHERE data_GPU.GPU_name = 'GeForce RTX 4090' OR data_GPU.GPU_name = 'GeForce RTX 4090 D'
        如果我这样问：七彩虹生产的4090的价格。那你就转换成：
        ```sql SELECT data_price.price FROM data_Price JOIN data_GPU ON data_Price.GPU_id = data_gpu.id JOIN data_Brand ON data_Price.Brand_id = data_brand.id WHERE data_GPU.GPU_name = 'GeForce RTX 4090' AND data_Brand.name = 'COLORFUL'; ```

    就行
        如果我说某个型号的显卡，比如：4090.没有限制是那家厂商的4090.那么请默认是全部厂商的4090
    再添加一个需求：你在写sql语句的时候就不要换行了比如，你原来可能写成：
    ```sql
        SELECT data_price.price
    FROM data_Price
    JOIN data_GPU ON data_Price.GPU_id = data_gpu.id
    JOIN data_Brand ON data_Price.Brand_id = data_brand.id
    WHERE data_GPU.GPU_name = 'GeForce RTX 4090'
    AND data_Brand.name = 'COLORFUL';
    ```
    但是我要你写成：
    ```sql SELECT data_price.price FROM data_Price JOIN data_GPU ON data_Price.GPU_id = data_gpu.id JOIN data_Brand ON data_Price.Brand_id = data_brand.id WHERE data_GPU.GPU_name = 'GeForce RTX 4090' AND data_Brand.name = 'COLORFUL'; ```
        很简单就是把你原来写的换行符改成空格就行
    注意发烧级，中端级和入门级都不能写成英文
        """
    messages = [{'role': 'system', 'content': 'You are a helpful assistant who masters'
                                              ' how to translate the natural language into '
                                              'SQL which is specified for MySQL.Now i will provide you with the structure '
                                              'of my database containing my tables by giving you the class define.'
                                              '' + m}]

    # 您可以自定义设置对话轮数，当前为3
    for i in range(1):
        # user_input = input("请输入：")
        user_input = inputx
        messages.append({'role': 'user', 'content': user_input})
        assistant_output = get_response(messages).output.choices[0]['message']['content']
        messages.append({'role': 'assistant', 'content': assistant_output})
        # print(f'用户输入：{user_input}')
        # print(f'模型输出：{assistant_output}')
        # print('\n')
    # 假设这是你想要提取的 SQL 语句
    sql_statement = assistant_output

    # 定义正则表达式来匹配整个 SQL 语句
    pattern = r"(.*) SELECT (.*?) .*"

    # 使用 findall 方法来查找所有匹配的 SQL 语句
    matches = re.findall(r"```sql(.+?)```", sql_statement, re.DOTALL)
    # print(matches)
    # 打印匹配结果
    # 假设这是您想要替换的列表
    sql_string = "".join(matches)

    lines = sql_string.splitlines()

    # 使用列表推导式对每行进行替换操作
    # 注意这里我们添加了一个条件来检查行是否为空
    processed_lines = [line.replace('\n', ';') if line.endswith('\n') else line.replace('\n', ' ') for line in lines]

    # 将替换后的行合并成一个单一的字符串
    processed_sql_string = '\n'.join(processed_lines)

    # 打印处理后的 SQL 字符串
    # print(processed_sql_string)
    return processed_sql_string
if __name__ == '__main__':
    get_sql()




