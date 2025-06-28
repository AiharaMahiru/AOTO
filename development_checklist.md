# 新功能开发流程清单 (Development Checklist)

本清单旨在为【情侣记录网站】项目的所有新功能开发提供一个标准、统一的流程指导。请在开发新功能时遵循以下步骤，确保代码质量和团队协作效率。

**功能模块名称:** _________________

---

## 0. 开始开发前 (Before Development)

- [ ] **创建功能分支:** 从主开发分支 (`main` 或 `develop`) 创建一个新的功能分支。
  - *命名规范:* `feature/your-feature-name` (例如: `feature/anniversary-management`)
  - *示例命令:* `git checkout -b feature/anniversary-management main`

## 1. 后端开发 (Backend Development)

- [ ] **数据库模型:** 在 [`app/models.py`](app/models.py:1) 中定义新功能所需的数据库模型。
- [ ] **数据库迁移 (生成):** 运行 `flask db migrate -m "Add [feature_name] model"` 生成迁移脚本。
- [ ] **数据库迁移 (应用):** 运行 `flask db upgrade` 将变更应用到数据库。
- [ ] **API 逻辑:** 在 [`app/routes.py`](app/routes.py:1) 或新的蓝图文件中，实现新功能的 API 路由和业务逻辑。
- [ ] **(可选) 单元测试:** 为后端逻辑编写单元测试，确保代码质量。

## 2. 前端开发 (Frontend Development)

- [ ] **HTML 模板:** 在 [`app/templates/`](app/templates/) 目录下创建新功能的 HTML 模板文件。
- [ ] **CSS 样式:** 在 [`app/static/css/`](app/static/css/) 目录下编写或更新 CSS 样式。
- [ ] **JavaScript 交互:** 在 [`app/static/js/`](app/static/js/) 目录下编写 JavaScript 代码，实现前端交互逻辑。

## 3. 集成与测试 (Integration & Testing)

- [ ] **前后端联调:** 连接前后端接口，确保数据正确传递和渲染。
- [ ] **功能测试:** 在浏览器中完整测试新功能，包括所有交互、边界情况和响应式表现。
- [ ] **最终确认:** 确认功能符合需求，没有明显 Bug。

## 4. 完成开发与代码审查 (Review & Merge)

- [ ] **推送至远程仓库:** 将功能分支推送到远程仓库。
  - *示例命令:* `git push origin feature/anniversary-management`
- [ ] **创建合并请求 (Pull Request):** 在代码托管平台（如 GitHub, GitLab）上创建一个合并请求，目标分支为主开发分支。
- [ ] **指定审查者:** 指定至少一名团队成员进行代码审查 (Code Review)。
- [ ] **通过自动化检查:** 确保所有 CI/CD 自动化检查（如测试、代码风格检查）都已通过。
- [ ] **解决审查问题:** 根据审查意见修改代码，直至所有问题都已解决。

## 5. 合并与清理 (Merge & Cleanup)

- [ ] **合并代码:** 将通过审查的合并请求合入主开发分支。
- [ ] **删除功能分支:** 删除已合并的本地和远程功能分支。
  - *示例命令 (本地):* `git branch -d feature/anniversary-management`
  - *示例命令 (远程):* `git push origin --delete feature/anniversary-management`