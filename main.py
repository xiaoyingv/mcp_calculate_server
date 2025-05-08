# 计算器mcp

import ast
import operator
from mcp.server.fastmcp import FastMCP


# 初始化 MCP 服务器
mcp = FastMCP("CalculatorServer")

# 支持的运算符映射
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,  # 负号
    ast.UAdd: operator.pos   # 正号
}

def evaluate(node: ast.AST) -> float:
    """
    递归计算 AST 节点表达式
    """
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        else:
            raise TypeError(f"不支持的常量类型: {type(node.value)}")

    elif isinstance(node, ast.UnaryOp):
        op_func = OPERATORS[type(node.op)]
        return op_func(evaluate(node.operand))

    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        op_func = OPERATORS[type(node.op)]
        return op_func(left, right)

    else:
        raise TypeError(f"不支持的表达式类型: {type(node)}")

def safe_calculate(expression: str) -> str:
    """
    安全地解析并计算表达式字符串
    :param expression: 数学表达式字符串（如 "5+3"）
    :return: 格式化结果或错误信息
    """
    try:
        # 解析表达式为 AST
        node = ast.parse(expression, mode='eval').body
        result = evaluate(node)
        return f"🧮 计算结果：{expression} = {result:.2f}"
    except SyntaxError as e:
        return f"❌ 表达式语法错误：{str(e)}"
    except KeyError as e:
        return f"❌ 不支持的运算符：{str(e)}"
    except ZeroDivisionError:
        return "❌ 错误：除数不能为零"
    except Exception as e:
        return f"⚠️ 计算错误：{str(e)}"

@mcp.tool()
async def perform_calculation(expression: str) -> str:
    """
    计算器 MCP ：接收数学表达式字符串并返回计算结果
    :param expression: 数学表达式字符串（如 "5+3"）
    :return: 计算结果（格式化结果或错误信息）
    """
    return safe_calculate(expression)

def main():
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')

if __name__ == "__main__":
   main()

