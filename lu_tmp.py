import numpy as np


def LUFact(A):  # LU Factorization
    n = len(A)
    L = np.eye(n)
    U = np.zeros(A.shape)
    U[0, :] = A[0, :]
    L[1:, 0] = A[1:, 0] / U[0, 0]
    for r in range(1, n):
        lt = L[r, :r].reshape(r, 1)
        U[r, r:] = A[r, r:] - np.sum(lt * U[:r, r:], axis=0)
        print("\n#U%d:" % (r))
        print(U)
        if r == n - 1:
            continue
        ut = U[:r, r].reshape(r, 1)
        L[r + 1 :, r] = (A[r + 1 :, r] - np.sum(ut * L[r + 1 :, :r].T, axis=0)) / U[
            r, r
        ]
        print("\n#L%d:" % (r))
        print(L)
    return L, U


def Doolittle(A):  # LU Factorization---Doolittle
    n = len(A)
    LU = A.copy()
    LU[1:, 0] = LU[1:, 0] / LU[0, 0]
    for r in range(1, n):
        lt = LU[r, :r].reshape(r, 1)
        LU[r, r:] = LU[r, r:] - np.sum(lt * LU[:r, r:], axis=0)
        print("\n#U%d:" % (r))
        print(LU)
        if r == n - 1:
            continue
        ut = LU[:r, r].reshape(r, 1)
        LU[r + 1 :, r] = (LU[r + 1 :, r] - np.sum(ut * LU[r + 1 :, :r].T, axis=0)) / LU[
            r, r
        ]
        print("\n#L%d:" % (r))
        print(LU)
    U = np.triu(LU)
    L = np.tril(LU) - np.diag(np.diag(LU)) + np.eye(n)
    return LU, L, U


def solveLineq(L, U, b):
    # Ly = b
    rows = len(b)
    y = np.zeros(rows)
    y[0] = b[0] / L[0, 0]
    for k in range(1, rows):
        y[k] = (b[k] - np.sum(L[k, :k] * y[:k])) / L[k, k]
    # Ux = y (back substitution)
    x = np.zeros(rows)
    k = rows - 1
    x[k] = y[k] / U[k, k]
    for k in range(rows - 2, -1, -1):
        x[k] = (y[k] - np.sum(x[k + 1 :] * U[k, k + 1 :])) / U[k, k]
    return x


if __name__ == "__main__":
    A = np.array(
        [
            [2.0, 5.0, 7.0, 9.0, 1.0],
            [4.0, 18.0, 20.0, 23.0, 9.0],
            [6.0, 87.0, 76.0, 80.0, 75.0],
            [8.0, 60.0, 64.0, 112.0, 95.0],
            [2.0, 29.0, 32.0, 89.0, 97.0],
        ],
        dtype="float",
    )
    b = np.array([[74.0, 237.0, 1103.0, 1243.0, 997.0]], dtype="float").T
    La, Ua = LUFact(A)
    x = solveLineq(La, Ua, b)
    print(np.dot(A, x))  # x = [1. 2. 3. 4. 5.]
