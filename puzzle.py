from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
from logic import *
knowledge0 = And(
    # A is either a knight or a knave (but not both)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),  # A cannot be both a knight and a knave
    # If A is a knight, their statement ("I am both a knight and a knave") is true
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave, their statement is false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
from logic import *
knowledge1 = And(
    # A is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # If A is a knight, then A's statement must be true (A and B are both knaves)
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, then A's statement must be false (at least one of them is not a knave)
    Implication(AKnave, Or(AKnight, BKnight))
)
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
from logic import *
knowledge2 = And(
    # A is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # If A is a knight, A and B are the same
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, A and B are different
    Implication(AKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knight, A and B are different
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave, A and B are the same
    Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
from logic import *
knowledge3 = And(
    # A, B, C are either knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    
    # If A is a knight, then A must be telling the truth
    Implication(AKnight, AKnight),
    Implication(AKnave, Not(AKnight)),
    
    # B says that A said "I am a knave"
    Implication(BKnight, Implication(AKnight, AKnave)),
    Implication(BKnave, Not(Implication(AKnight, AKnave))),
    
    # B also says that C is a knave
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    
    # C says A is a knight
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
