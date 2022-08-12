import types


# class NodeVisitor:
#     def visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)
#
#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
#
#
# class Evaluator(NodeVisitor):
#     def visit_Number(self, node):
#         return node.value
#
#     def visit_Add(self, node):
#         return self.visit(node.left) + self.visit(node.right)
#
#     def visit_Sub(self, node):
#         return self.visit(node.left) - self.visit(node.right)
#
#     def visit_Mul(self, node):
#         return self.visit(node.left) * self.visit(node.right)
#
#     def visit_Div(self, node):
#         return self.visit(node.left) / self.visit(node.right)
#
#     def visit_Negate(self, node):
#         return -node.operand
#
#
# e = Evaluator()
# print(e.visit(4))
#
#
# class StackCode(NodeVisitor):
#     def generate_code(self, node):
#         self.instructions = []
#         self.visit(node)
#         return self.instructions
#
#     def visit_Number(self, node):
#         self.instructions.append(('PUSH', node.value))
#
#     def binop(self, node, instruction):
#         self.visit(node.left)
#         self.visit(node.right)
#         self.instructions.append((instruction,))
#
#     def visit_Add(self, node):
#         self.binop(node, 'ADD')
#
#     def visit_Sub(self, node):
#         self.binop(node, 'SUB')
#
#     def visit_Mul(self, node):
#         self.binop(node, 'MUL')
#
#     def visit_Div(self, node):
#         self.binop(node, 'DIV')
#
#     def unaryop(self, node, instruction):
#         self.visit(node.operand)
#         self.instructions.append((instruction,))
#
#     def visit_Negate(self, node):
#         self.unaryop(node, 'NEG')
#
#
# s = StackCode()
# s.generate_code(s)

# Visitor Pattern Without Recursion

class Node:
    pass


class NodeVisitor:
    def visit(self, node):

        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
