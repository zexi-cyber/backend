
from django.shortcuts import render, HttpResponse
from . import models
from django.db.models import Avg,Max,Min,Count,Sum,F ,Q #   引入函数
# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.db import connection
from . import api
import logging

# 引入日志记录器
logger = logging.getLogger(__name__)
@csrf_exempt
def add_query(request):

    if request.method == 'POST':
        # 您的 SQL 查询字符串
        data = json.loads(request.body)
        inputx = data.get('inputx')
        print(inputx)
        sql_query = api.get_sql(inputx)
        print(sql_query)
        try:
            # 获取数据库连接
            with connection.cursor() as cursor:
                # 执行 SQL 查询
                cursor.execute(sql_query)

                # 获取查询结果
                result = cursor.fetchall()

            # 打印结果
            # for row in result:
            #     print("结果：",row[0])  # 假设查询结果的第一列是 price
            # print(result)
            # 将元组转换为集合，自动去除重复的元组
            unique_set = set(result)
            # 将唯一的元组转换回元组形式
            unique_result = tuple(unique_set)
            # print(unique_result)
            return JsonResponse({
                'code': 200,
                'message': unique_result,
                'sql':sql_query,
            })
        except Exception as e:
            # 记录错误日志
            logger.error("数据库查询出错: %s", e)
            # 返回错误信息
            return JsonResponse({
                'code': 500,
                'message': "数据库查询出错,请仔细检查你的查询语言",
            })

    # @csrf_exempt
    # def provide_data1():
    #     if request.method == 'POST':





