from decimal import Decimal


def erlangB(A, N):
    invB = 1.0
    for i in range(1, N + 1):
        invB = 1 + (i / A) * invB
    return Decimal(1 / invB)


def erlangC(A, N):
    P = erlangB(A, N)
    L = (A * P) / (N - A + (A * P))
    return Decimal(L)


def main():
    print("Erlang B and C Calculator")
    A = float(input("Enter traffic load (in Erlangs): "))
    N = int(input("Enter the number of servers: "))

    print("\nCalculating...")
    B = erlangB(A, N)
    C = erlangC(A, N)

    print(f"Erlang B (Blocking Probability): {B:.5f}")
    print(f"Erlang C (Delay Probability): {C:.5f}")


if __name__ == "__main__":
    main()
