# 情侣记录网站 (Couple's Record Website)

这是一个使用 Flask 构建的 Web 应用程序，旨在帮助情侣记录和管理他们的特殊日子和共同的记忆。

## 功能特性

*   用户认证与管理
*   纪念日记录与提醒
*   （以及其他未来功能...）

## 技术栈

*   **后端:** Flask
*   **数据库:** SQLAlchemy, Flask-Migrate
*   **前端:** HTML, CSS, JavaScript

## 安装与设置

请按照以下步骤在本地环境中设置和运行项目。

### 1. 克隆仓库

```bash
git clone <your-repository-url>
cd <project-directory>
```

### 2. 创建并激活虚拟环境

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

使用 pip 安装所有必需的 Python 包：

```bash
pip install -r requirements.txt
```

### 4. 数据库设置

本项目使用 Flask-Migrate 管理数据库迁移。

a. **(首次设置)** 如果 `.flaskenv` 文件不存在，请创建一个，并添加以下内容以指定 Flask 应用的入口：

```
FLASK_APP=run.py
```

b. **应用数据库迁移**

运行以下命令来创建或更新数据库表结构：

```bash
flask db upgrade
```

如果这是第一次初始化，您可能需要先运行 `flask db init` 和 `flask db migrate`。

## 运行应用

完成以上所有设置后，使用以下命令启动开发服务器：

```bash
python run.py
```

应用将在 `http://127.0.0.1:5000` 上运行。

## 项目结构

```
.
├── app/                  # 主要应用模块
│   ├── static/           # 静态文件 (CSS, JS)
│   ├── templates/        # HTML 模板
│   ├── __init__.py       # 应用工厂
│   ├── models.py         # 数据库模型
│   ├── routes.py         # 路由定义
│   └── anniversary_routes.py # 纪念日相关路由
├── migrations/           # 数据库迁移脚本
├── .flaskenv             # Flask 环境变量
├── config.py             # 配置文件
├── development_checklist.md # 开发流程清单
├── requirements.txt      # Python 依赖
└── run.py                # 应用启动脚本