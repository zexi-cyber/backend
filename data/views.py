from django.shortcuts import render, HttpResponse
from . import models
from django.db.models import Avg, Max, Min, Count, Sum, F, Q  #   引入函数
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
        # 解析请求体中的数据
        data = json.loads(request.body)
        inputx = data.get('inputx')
        sql_query = api.get_sql(inputx)
        print(sql_query)
        try:
            # 获取数据库连接
            with connection.cursor() as cursor:
                # 执行 SQL 查询
                cursor.execute(sql_query)

                # 获取查询结果的列名
                column_names = [desc[0] for desc in cursor.description]

                # 转换查询结果为字典列表
                result = [
                    dict(zip(column_names, row))
                    for row in cursor.fetchall()
                ]
            print(result)
            return JsonResponse({
                'code': 200,
                'message': result,
                'sql': sql_query,
            })
        except Exception as e:
            # 记录错误日志
            logger.error("数据库查询出错: %s", e)
            # 返回错误信息
            return JsonResponse({
                'code': 500,
                'message': "数据库查询出错,请仔细检查你的查询语言",
            })

@csrf_exempt
def provide_data1(request):
    if request.method == 'GET':
        sql_query = ("""SELECT data_brand.name, data_GPU.GPU_name, data_price.price FROM data_Price JOIN data_GPU ON data_Price.GPU_id = data_GPU.id JOIN data_Brand ON data_Price.Brand_id = data_Brand.id WHERE data_GPU.type = '发烧级' ORDER BY data_price.price DESC;"""
                     )
        print(sql_query)
        try:
            # 获取数据库连接
            with connection.cursor() as cursor:
                # 执行 SQL 查询
                cursor.execute(sql_query)

                # 获取查询结果的列名
                column_names = [desc[0] for desc in cursor.description]

                # 转换查询结果为字典列表
                result = [
                    dict(zip(column_names, row))
                    for row in cursor.fetchall()
                ]

            return JsonResponse({
                'code': 200,
                'message': result,
                'sql': sql_query,
            })
        except Exception as e:
            # 记录错误日志
            logger.error("数据库查询出错: %s", e)
            # 返回错误信息
            return JsonResponse({
                'code': 500,
                'message': "数据库查询出错,请仔细检查你的查询语言",
            })