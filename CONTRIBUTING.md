# CONTRIBUTING.md

## 欢迎贡献 👋

感谢您有兴趣为 Calculator MCP Server 项目贡献！本指南将帮助您了解如何有效地参与项目开发。

## 贡献方式

### 1. 报告问题
- 在 [Issues 页面](https://github.com/xiaoyingv/mcp_calculate_server/issues) 搜索是否已有类似问题
- 新建 issue 并清晰描述：
  - 问题现象
  - 重现步骤
  - 期望行为
  - 环境信息 (Python 版本等)

### 2. 提交代码 (Pull Request)
1. Fork 本仓库
2. 创建新分支: `git checkout -b feature/your-feature-name`
3. 实现功能/修复问题
4. 添加测试用例
5. 提交代码: `git commit -m "描述变更内容"`
6. 推送到您的仓库: `git push origin feature/your-feature-name`
7. 创建 Pull Request 到主仓库的 `main` 分支

## 开发环境设置

### 前置要求
- Python 3.13+
- pip
- Git

### 安装步骤
```bash
# 克隆仓库
git clone https://github.com/xiaoyingv/mcp_calculate_server.git
cd mcp_calculate_server

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows: venv\Scripts\activate
# Unix/macOS: source venv/bin/activate

# 安装依赖
pip install -e .[dev]
```

## 代码规范

### 编码风格
- 遵循 PEP 8 规范
- 使用 4 空格缩进
- 保持函数长度合理（建议不超过 50 行）
- 使用类型注解

### 测试要求
- 新增功能必须包含单元测试
- 修改现有代码需更新相关测试
- 测试覆盖率不应低于 90%
- 运行测试：
  ```bash
  pytest --cov=mcp_calculate_server
  ```

### 代码格式化
在提交前运行：
```bash
black .  # 自动格式化代码
flake8   # 静态检查
```

## 文档要求
- 新增功能需更新 README.md 文档
- 公共 API 必须包含 docstring
- 复杂逻辑需添加注释说明

## 评审流程
1. PR 提交后会自动运行 CI 测试
2. 维护者将在 3 个工作日内进行评审
3. 可能需要修改或讨论
4. 通过评审后将被合并到主分支

## 功能开发指南
### 新增运算符支持
1. 在 `ast_parser.py` 的 `ALLOWED_NODES` 添加新节点类型
2. 在 `expression_evaluator.py` 实现对应的 `visit_NodeType` 方法
3. 添加测试用例到 `test_expression_evaluator.py`

### 错误处理增强
1. 在 `expression_evaluator.py` 捕获特定异常
2. 返回用户友好的错误信息
3. 添加对应的错误测试用例

## 行为准则
请遵守 [贡献者公约](https://www.contributor-covenant.org/)，保持专业友好的沟通氛围。

## 许可证说明
所有贡献将遵循项目的 [MIT 许可证](LICENSE)。

---

感谢您的贡献！🎉 如有任何问题，请通过 Issues 与我们联系。