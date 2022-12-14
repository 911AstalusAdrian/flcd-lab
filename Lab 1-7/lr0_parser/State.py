import itertools
from enum import Enum


class Action(Enum):
    SHIFT = 1
    ACCEPT = 2
    REDUCE = 3
    REDUCE_REDUCE_CONFLICT = 4
    SHIFT_REDUCE_CONFLICT = 5


class State:
    id = itertools.count()

    def __init__(self, closure_items, closure, enhhanced_symbol):
        self.action = None
        self.id = next(self.id)
        self.closure_items = closure_items
        self.closure = closure
        self.set_action(enhhanced_symbol)

    def set_action(self, enhanced_symbol):
        if len(self.closure) == 1 and \
                len(self.closure[0].rhs) == self.closure[0].dot_pos and \
                self.closure[0].lhs == enhanced_symbol:
            self.action = Action.ACCEPT
        elif len(self.closure) == 1 and self.closure[0].dot_pos == len(self.closure[0].rhs):
            self.action = Action.REDUCE
        elif len(self.closure) != 0 and self.check_all_not_dot_end():
            self.action = Action.SHIFT
        else:
            if len(self.closure) > 1 and self.check_all_dot_end():
                self.action = Action.REDUCE_REDUCE_CONFLICT
            else:
                self.action = Action.SHIFT_REDUCE_CONFLICT

    def check_all_not_dot_end(self) -> bool:
        for closure in self.closure:
            if len(closure.rhs) <= closure.dot_pos:
                return False
        return True

    def check_all_dot_end(self) -> bool:
        for closure in self.closure:
            if len(closure.rhs) > closure.dot_pos:
                return False
        return True

    def get_all_symbols_after_dot(self):
        res = []
        for item in self.closure:
            if item.dot_pos < len(item.rhs):
                res.append(item.rhs[item.dot_pos])

        return res

    def __eq__(self, other):
        return self.closure_items == other.closure_items

    def __str__(self):
        result = "s" + str(self.id) + " = closure({"
        for item in self.closure_items:
            result += str(item) + ", "
        result = result[:-2] + "}) = {"
        for item in self.closure:
            result += str(item) + ", "
        result = result[:-2] + "}"
        return result
