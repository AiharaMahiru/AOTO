# 【情侣记录网站】系统架构说明书

本文档旨在详细描述“情侣记录网站”项目的系统架构、技术选型、模块设计、数据模型和 API 接口，为项目的开发提供清晰的指导。

## 1. 项目概述

*   **项目名称:** 情侣记录网站
*   **核心目标:** 为情侣提供一个私密的线上空间，用于记录和分享彼此的重要时刻、共同回忆和未来计划。

### 1.1. 核心功能 (V1)
1.  **纪念日管理 (Anniversary Management):** 记录、提醒重要的日子。
2.  **照片墙 (Photo Wall):** 上传和展示共同的照片。
3.  **旅行地图 (Travel Map):** 在地图上标记一起走过的地方。
4.  **词云 (Word Cloud):** 通过文字生成独特的情感词云。

### 1.2. 扩展功能 (V2)
1.  **愿望清单 (Wishlist):** 共同创建和管理未来的愿望。
2.  **情侣日记 (Couple's Diary):** 分享和记录日常生活的点滴。

## 2. 技术选型

| 分类 | 技术/框架 | 理由 |
| :--- | :--- | :--- |
| **后端框架** | Flask | 轻量级、灵活、易于上手，适合快速开发和迭代。 |
| **前端框架** | Bootstrap 5 | 提供了丰富的 UI 组件和响应式布局，能快速构建美观的界面。 |
| **数据库** | SQLite | 配置简单，无需独立服务器，非常适合项目初期开发和原型验证。 |
| **API 认证** | JWT (JSON Web Tokens) | 无状态、安全、易于在前后端分离架构中实现。 |

## 3. 系统架构

本系统采用经典的前后端分离架构。

*   **前端 (Client):** 静态的 HTML, CSS, 和 JavaScript 文件，负责用户界面和交互。通过 RESTful API 与后端通信。
*   **后端 (Backend):** 基于 Flask 的 Web 应用，负责处理业务逻辑、用户认证和数据库操作。
*   **数据库 (Database):** 单个 SQLite 文件 (`couple_records.db`)，用于持久化存储所有数据。

### 3.1. 架构图

```mermaid
graph TD
    subgraph 用户设备
        A[浏览器 / Browser]
    end

    subgraph 服务器 / Server
        B[Web 服务器 (如 Gunicorn)] --> C{Flask 应用 / Backend};
        C --> D[SQLite 数据库 / couple_records.db];
    end

    A -- HTTP 请求 (HTML/CSS/JS) --> B;
    A -- RESTful API 调用 (JSON) --> C;
    C -- 数据库查询 (SQLAlchemy ORM) --> D;
```

## 4. 模块划分

### 4.1. 核心模块 (V1)

*   **用户认证模块 (User Authentication):**
    *   **职责:** 处理用户注册、登录、登出。使用 JWT 生成和验证 token。
*   **纪念日管理模块 (Anniversary Management):**
    *   **职责:** 实现纪念日的增、删、改、查 (CRUD)。
*   **照片墙模块 (Photo Wall):**
    *   **职责:** 处理照片上传、存储、元数据管理和展示。
*   **旅行地图模块 (Travel Map):**
    *   **职责:** 记录地理位置坐标和相关信息。
*   **词云模块 (Word Cloud):**
    *   **职责:** 根据用户提交的文本生成词云图像。

### 4.2. 扩展模块 (V2)

*   **愿望清单模块 (Wishlist):**
    *   **职责:** 实现共享愿望清单的增、删、改、查，并可标记完成状态。
*   **情侣日记模块 (Couple's Diary):**
    *   **职责:** 提供一个共享的日记平台，双方可共同记录和查看。

## 5. 数据模型

数据库将包含以下核心表：

### `users` (用户信息表)
*   `id`: INTEGER, 主键
*   `username`: TEXT, 唯一, 非空
*   `password_hash`: TEXT, 非空
*   `partner_id`: INTEGER, 外键关联到 `users.id`

### `anniversaries` (纪念日表)
*   `id`: INTEGER, 主键
*   `user_id`: INTEGER, 外键关联到 `users.id`
*   `title`: TEXT, 非空
*   `date`: DATE, 非空
*   `description`: TEXT

### `photos` (照片信息表)
*   `id`: INTEGER, 主键
*   `user_id`: INTEGER, 外键关联到 `users.id`
*   `file_path`: TEXT, 非空
*   `caption`: TEXT
*   `uploaded_at`: DATETIME, 默认当前时间

### `locations` (旅行地点表)
*   `id`: INTEGER, 主键
*   `user_id`: INTEGER, 外键关联到 `users.id`
*   `name`: TEXT, 非空
*   `latitude`: REAL
*   `longitude`: REAL
*   `visit_date`: DATE

### `word_cloud_texts` (词云文本表)
*   `id`: INTEGER, 主键
*   `user_id`: INTEGER, 外键关联到 `users.id`
*   `content`: TEXT, 非空
*   `created_at`: DATETIME, 默认当前时间

### `wishes` (V2-愿望清单表)
*   `id`: INTEGER, 主键
*   `user_id`: INTEGER, 外键关联到 `users.id`
*   `content`: TEXT, 非空
*   `is_completed`: BOOLEAN, 默认 `False`
*   `created_by`: INTEGER, 外键关联到 `users.id`

### `diaries` (V2-情侣日记表)
*   `id`: INTEGER, 主键
*   `user_id`: INTEGER, 外键关联到 `users.id`
*   `title`: TEXT
*   `content`: TEXT, 非空
*   `date`: DATE, 非空
*   `author_id`: INTEGER, 外键关联到 `users.id`

## 6. API 设计

所有 API 端点都以 `/api` 为前缀。需要认证的接口需在请求头中携带 `Authorization: Bearer <token>`。

| 功能 | HTTP 方法 | 路径 | 描述 |
| :--- | :--- | :--- | :--- |
| **用户管理** | `POST` | `/api/auth/register` | 用户注册 |
| | `POST` | `/api/auth/login` | 用户登录，成功后返回 JWT |
| | `PUT` | `/api/user/profile` | 更新当前用户的个人信息 |
| **纪念日** | `GET` | `/api/anniversaries` | 获取所有纪念日 |
| | `POST` | `/api/anniversaries` | 新增一个纪念日 |
| | `PUT` | `/api/anniversaries/<id>` | 更新指定的纪念日 |
| | `DELETE`| `/api/anniversaries/<id>` | 删除指定的纪念日 |
| **照片墙** | `GET` | `/api/photos` | 获取所有照片信息 |
| | `POST` | `/api/photos` | 上传一张新照片 |
| | `DELETE`| `/api/photos/<id>` | 删除指定的照片 |
| **旅行地图** | `GET` | `/api/locations` | 获取所有旅行地点 |
| | `POST` | `/api/locations` | 添加一个新的旅行地点 |
| **词云** | `POST` | `/api/wordcloud` | 提交文本，生成并返回词云 |
| **愿望清单(V2)** | `GET` | `/api/wishes` | 获取所有愿望 |
| | `POST` | `/api/wishes` | 添加一个新愿望 |
| | `PUT` | `/api/wishes/<id>` | 更新一个愿望（如标记完成）|
| | `DELETE`| `/api/wishes/<id>` | 删除一个愿望 |
| **情侣日记(V2)** | `GET` | `/api/diaries` | 获取日记列表 |
| | `POST` | `/api/diaries` | 写一篇新日记 |
| | `PUT` | `/api/diaries/<id>` | 编辑一篇日记 |