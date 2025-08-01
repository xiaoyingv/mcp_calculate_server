# Calculator MCP Server 🧮

[![PyPI version](https://badge.fury.io/py/mcp-calculate-server.svg)](https://pypi.org/project/mcp-calculate-server/)
[![License](https://img.shields.io/pypi/l/mcp-calculate-server.svg)](https://github.com/xiaoyingv/mcp_calculate_server/blob/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/mcp-calculate-server.svg)](https://pypi.org/project/mcp-calculate-server/)

基于 Python AST 的安全表达式计算器 MCP 服务，支持基础数学运算和错误防护机制。

## 功能特性

- ✅ 支持加减乘除四则运算（`+`, `-`, `*`, `/`）
- ✅ 支持正负号处理（`+5`, `-3`）
- ✅ 自动格式化计算结果（保留两位小数）
- ⚠️ 安全防护：
  - 拦截代码注入风险（通过 AST 解析而非 `eval`）
  - 除零错误防护
  - 语法错误提示
  - 类型安全检查

## 安装方式

```bash
pip install mcp-calculate-server
```

## 快速使用

```
{
  "mcpServers": {
    "calculate_mcp": {
      "command": "uvx",
      "args": ["mcp_calculate_server"]
      }
    }
  }
```

## API 接口

### `perform_calculation(expression: str) -> str`

接收数学表达式字符串，返回格式化结果或错误信息

```python
>>> perform_calculation("5+3")
"🧮 计算结果：5+3 = 8.00"

>>> perform_calculation("10/0")
"❌ 错误：除数不能为零"

>>> perform_calculation("2**3")
"❌ 不支持的运算符：Power"
```

## 支持的运算符

| 操作符 | 说明 | 示例  |
| ------ | ---- | ----- |
| +      | 加法 | `3+4` |
| -      | 减法 | `5-2` |
| *      | 乘法 | `6*7` |
| /      | 除法 | `8/2` |
| -x     | 取负 | `-5`  |
| +x     | 取正 | `+3`  |

## 错误码说明

| 错误类型       | 示例输出                           |
| -------------- | ---------------------------------- |
| 语法错误       | `❌ 表达式语法错误：unexpected EOF` |
| 不支持的运算符 | `❌ 不支持的运算符：Mod`            |
| 除零错误       | `❌ 错误：除数不能为零`             |
| 非法操作数类型 | `TypeError: 不支持的常量类型`      |

## 依赖环境

- Python 3.13+
- `mcp-server` 库（自动安装）

## 开源协议

MIT License，详情见 [LICENSE](https://github.com/xiaoyingv/mcp_calculate_server/blob/main/LICENSE)

## 源码地址

GitHub: https://github.com/xiaoyingv/mcp_calculate_server

## 贡献指南

欢迎提交 PR 和报告 issue，提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)

