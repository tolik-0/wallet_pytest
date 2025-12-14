from typing import Dict, List


TowerState = Dict[str, List[int]]


def create_game(disks: int) -> TowerState:
    """Create initial state for the Tower of Hanoi puzzle."""
    if disks <= 0:
        raise ValueError("Number of disks must be positive.")
    return {"A": list(range(disks, 0, -1)), "B": [], "C": []}


def draw_towers(towers: TowerState) -> None:
    """Print current tower state in a simple text form."""
    max_height = max(len(stack) for stack in towers.values())
    pegs = ("A", "B", "C")
    print()
    for level in range(max_height, 0, -1):
        row_parts = []
        for peg in pegs:
            stack = towers[peg]
            if len(stack) >= level:
                disk = stack[level - 1]
                row_parts.append(f"{disk:^5}")
            else:
                row_parts.append("  |  ")
        print(" ".join(row_parts))
    print("  A     B     C\n")


def is_valid_move(towers: TowerState, from_peg: str, to_peg: str) -> bool:
    """Return True if move from from_peg to to_peg is legal."""
    if from_peg == to_peg:
        return False
    if from_peg not in towers or to_peg not in towers:
        return False
    if not towers[from_peg]:
        return False
    if not towers[to_peg]:
        return True
    return towers[from_peg][-1] < towers[to_peg][-1]


def make_move(towers: TowerState, from_peg: str, to_peg: str) -> None:
    """Execute one legal move between pegs."""
    if not is_valid_move(towers, from_peg, to_peg):
        raise ValueError("Illegal move.")
    disk = towers[from_peg].pop()
    towers[to_peg].append(disk)


def is_solved(towers: TowerState, disks: int) -> bool:
    """Check whether puzzle is solved (all disks on peg C)."""
    return towers["C"] == list(range(disks, 0, -1))


def ask_move() -> tuple[str, str]:
    """Ask user for move in the form 'A C'."""
    move = input("Enter move (from to), for example 'A C', or Q to quit: ").strip()
    if move.upper() == "Q":
        return ("Q", "Q")
    parts = move.split()
    if len(parts) != 2:
        raise ValueError("Move must have two peg labels, for example 'A C'.")
    return parts[0].upper(), parts[1].upper()


def main() -> None:
    """Run interactive Tower of Hanoi game in console."""
    try:
        disks_str = input("Enter number of disks (default 3): ").strip() or "3"
        disks = int(disks_str)
    except ValueError:
        print("Invalid number, using 3 disks.")
        disks = 3

    towers = create_game(disks)

    while True:
        draw_towers(towers)
        if is_solved(towers, disks):
            print("Congratulations! You solved the puzzle.")
            break

        try:
            from_peg, to_peg = ask_move()
            if from_peg == "Q":
                print("Game aborted by user.")
                break
            make_move(towers, from_peg, to_peg)
        except ValueError as error:
            print(f"Error: {error}")
            continue


if __name__ == "__main__":
    main()


"""Interactive Tower of Hanoi game in console."""