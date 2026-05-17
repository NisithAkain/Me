
import numpy as np

# -----------------------------
# 1. Create a simple vector
# -----------------------------
x = np.array([1, 2, 3])
print("x =", x)
print("x shape =", x.shape)   # (3,)  <-- 1D vector


# -----------------------------
# 2. Turn it into a ROW vector
# -----------------------------
x_row = x.reshape(1, 3)
print("\nRow vector:")
print(x_row)
print("Row shape =", x_row.shape)   # (1, 3)


# -----------------------------
# 3. Turn it into a COLUMN vector
# -----------------------------
x_col = x.reshape(3, 1)
print("\nColumn vector:")
print(x_col)
print("Column shape =", x_col.shape)   # (3, 1)


# -----------------------------
# 4. Create a 2×3 matrix
# -----------------------------
A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("\nMatrix A:")
print(A)
print("A shape =", A.shape)   # (2, 3)


# -----------------------------
# 5. Slicing rows and columns
# -----------------------------
print("\nFirst row of A:", A[0])        # row 0
print("Second column of A:", A[:, 1])  # column 1
print("Block A[0:2, 0:2]:")
print(A[0:2, 0:2])                     # top-left 2×2 block


# -----------------------------
# 6. Matrix multiplication
# -----------------------------
# Make a column vector that matches A's columns (3×1)
v = np.array([1, 2, 3]).reshape(3, 1)

print("\nv =")
print(v)
print("v shape =", v.shape)

result = A @ v
print("\nA @ v =")
print(result)
print("Result shape =", result.shape)   # (2, 1)
