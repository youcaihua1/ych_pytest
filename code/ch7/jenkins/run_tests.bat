@echo off
setlocal enabledelayedexpansion

REM 替换为您的实际路径
set top_path=D:\img\python\project
set code_path=%top_path%\code
set venv_path=%top_path%\venv

REM 解析位置参数
set tasks_proj_dir=%code_path%\%1
set start_tests_dir=%code_path%\%2
set results_dir=%3

REM 设置UTF-8环境变量（模拟Linux的locale）
chcp 65001 > nul
set PYTHONIOENCODING=utf-8

REM 激活虚拟环境
call %venv_path%\Scripts\activate.bat

REM 安装项目
pip install -e "%tasks_proj_dir%"

REM 运行测试
cd /d "%start_tests_dir%"
pytest --junitxml="%results_dir%\results.xml"