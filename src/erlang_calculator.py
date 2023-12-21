from decimal import Decimal
import matplotlib.pyplot as plt


def erlangB(A, N):
    invB = 1.0
    for i in range(1, N + 1):
        invB = 1 + (i / A) * invB
    return Decimal(1 / invB)


def erlangC(A, N):
    P = float(erlangB(A, N))  # Convert P to float
    L = (A * P) / (N - A + (A * P))
    return Decimal(L)


def plot_erlang(A_values, N, results, user_A, user_result, calculation_type):
    plt.figure(figsize=(8, 4))
    plt.plot(A_values, results, 'o-', label=f'Erlang {calculation_type} (Probability)')
    plt.plot(user_A, user_result, 'ro', label='Your Point')
    plt.annotate(f'{user_result:.5f}', (user_A, user_result), textcoords="offset points", xytext=(10, -10), ha='center')
    plt.title(f'Erlang {calculation_type} values')
    plt.xlabel('Traffic load (Erlangs)')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    print("Erlang B and C Calculator")
    calculation_type = input("Choose calculation (B/C): ").upper()

    while calculation_type not in ["B", "C"]:
        print("Invalid choice. Please enter 'B' for Erlang B or 'C' for Erlang C.")
        calculation_type = input("Choose calculation (B/C): ").upper()

    A_user = float(input("Enter your traffic load (in Erlangs): "))
    N = int(input("Enter the number of servers: "))

    A_values = [float(i) for i in range(1, N + 5)]  # Creating a range of traffic loads
    results = []

    for A in A_values:
        if calculation_type == "B":
            results.append(float(erlangB(A, N)))
        elif calculation_type == "C":
            results.append(float(erlangC(A, N)))

    user_result = float(erlangB(A_user, N)) if calculation_type == "B" else float(erlangC(A_user, N))
    plot_erlang(A_values, N, results, A_user, user_result, calculation_type)


if __name__ == "__main__":
    main()
