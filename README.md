
# Calculator MCP Server 🧮

[![PyPI version](https://badge.fury.io/py/mcp-calculate-server.svg)](https://pypi.org/project/mcp-calculate-server/)
[![License](https://img.shields.io/pypi/l/mcp-calculate-server.svg)](https://pypi.org/project/mcp-calculate-server/)
[![Python Version](https://img.shields.io/pypi/pyversions/mcp-calculate-server.svg)](https://pypi.org/project/mcp-calculate-server/)

基于 Python AST 的安全表达式计算器 MCP 服务，支持基础数学运算和错误防护机制。

## 功能特性

- ✅ 支持加减乘除四则运算（`+`, `-`, `*`, `/`）
- ✅ 支持幂运算（`**`）
- ✅ 支持正负号处理（`+5`, `-3`）
- ✅ 智能格式化计算结果：
  - 整数结果直接显示整数
  - 小数结果保留最多15位有效数字
  - 自动去除末尾多余的零
- ⚠️ 安全防护：
  - 拦截代码注入风险（通过 AST 解析而非 `eval`）
  - 除零错误防护
  - 语法错误提示
  - 类型安全检查
  - 幂运算安全检查

## 安装方式

```bash
pip install mcp-calculate-server
```

## 快速使用

```python
from mcp.server.fastmcp import FastMCP

# 启动计算器服务
calculator = FastMCP("CalculatorServer")
calculator.run(transport='stdio')
```

## API 接口

### `perform_calculation(expression: str) -> str`

接收数学表达式字符串，返回格式化结果或错误信息

```python
>>> perform_calculation("5+3")
"🧮 计算结果：5+3 = 8"

>>> perform_calculation("10/3")
"🧮 计算结果：10/3 = 3.333333333333333"

>>> perform_calculation("10**20")
"🧮 计算结果：10**20 = 100000000000000000000"

>>> perform_calculation("2**3")
"🧮 计算结果：2**3 = 8"

>>> perform_calculation("10/0")
"❌ 错误：除数不能为零"

>>> perform_calculation("0**-1")
"❌ 错误：零的负数次幂未定义"

>>> perform_calculation("(-1)**0.5")
"❌ 错误：负数的非整数次幂未定义"
```

## 支持的运算符

| 操作符 | 说明 | 示例  |
| ------ | ---- | ----- |
| +      | 加法 | `3+4` |
| -      | 减法 | `5-2` |
| *      | 乘法 | `6*7` |
| /      | 除法 | `8/2` |
| **     | 幂运算 | `2**3` |
| -x     | 取负 | `-5`  |
| +x     | 取正 | `+3`  |

## 错误码说明

| 错误类型 | 示例输出 |
|----------|----------|
| 语法错误 | `❌ 表达式语法错误：unexpected EOF` |
| 不支持的运算符 | `❌ 不支持的运算符：Mod` |
| 除零错误 | `❌ 错误：除数不能为零` |
| 非法操作数类型 | `TypeError: 不支持的常量类型` |
| 零的负数次幂 | `❌ 错误：零的负数次幂未定义` |
| 负数的非整数次幂 | `❌ 错误：负数的非整数次幂未定义` |

## 依赖环境

- Python 3.13+
- `mcp-server` 库（自动安装）

## 开源协议

MIT License，详情见 [LICENSE](https://github.com/xiaoyingv/mcp_calculate_server/blob/main/LICENSE)

## 源码地址

GitHub: https://github.com/xiaoyingv/mcp_calculate_server

## 贡献指南

欢迎提交 PR 和报告 issue，提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)
