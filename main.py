# 计算器mcp
# 添加了幂运算支持，放宽计算结果小数位数限制，并增强了错误处理能力。

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
    ast.Pow: operator.pow,  # 新增幂运算符
    ast.USub: operator.neg,  # 负号
    ast.UAdd: operator.pos  # 正号
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

        # 特殊处理幂运算的错误情况
        if type(node.op) is ast.Pow:
            if left == 0 and right < 0:
                raise ZeroDivisionError("零的负数次幂未定义")
            if left < 0 and not right.is_integer():
                raise ValueError("负数的非整数次幂未定义")

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

        # 根据结果类型选择合适的格式化方式
        if isinstance(result, int) or (isinstance(result, float) and result.is_integer()):
            # 整数或整数浮点数直接显示整数部分
            return f"🧮 计算结果：{expression} = {int(result)}"
        else:
            # 浮点数显示时保留最多15位有效数字，并去除末尾多余的零
            formatted = f"{result:.15g}"  # 使用 g 格式自动处理大数
            if '.' in formatted:
                formatted = formatted.rstrip('0').rstrip('.')
            return f"🧮 计算结果：{expression} = {formatted}"
    except SyntaxError as e:
        return f"❌ 表达式语法错误：{str(e)}"
    except KeyError as e:
        return f"❌ 不支持的运算符：{str(e)}"
    except ZeroDivisionError:
        return "❌ 错误：除数不能为零"
    except ValueError as e:
        return f"❌ 错误：{str(e)}"
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
