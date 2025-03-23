import math

class Vector:
    def __init__(self, *components):
        """Initialize the vector with given components."""
        if len(components) == 1 and hasattr(components[0], '__iter__'):
            self.components = tuple(components[0])
        else:
            self.components = components

    def __repr__(self):
        """String representation of the vector."""
        return f"Vector({', '.join(map(str, self.components))})"

    def __getitem__(self, index):
        """Access vector components by index."""
        return self.components[index]

    def __add__(self, other):
        """Add two vectors."""
        self._check_dimension(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        """Subtract two vectors."""
        self._check_dimension(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        """Dot product or scalar multiplication."""
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise ValueError("Unsupported operation with type: " + str(type(other)))

    def __rmul__(self, other):
        """Allow scalar multiplication from the left."""
        return self * other

    def _check_dimension(self, other):
        """Check if two vectors have the same dimension."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension.")

    def length(self):
        """Compute the length of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def magnitude(self):
        """Return the magnitude of the vector."""
        return self.length()  # You can also directly return the length

    def normalize(self):
        """Return the unit vector."""
        mag = self.length()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))

# Example Usage
if __name__ == "__main__":
    # Create vectors
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    # Print the vector
    print(v1)          # Output: Vector(1, 2, 3)

    # Addition
    v3 = v1 + v2
    print(v3)         # Output: Vector(5, 7, 9)

    # Subtraction
    v4 = v2 - v1
    print(v4)         # Output: Vector(3, 3, 3)

    # Dot product
    dot_product = v1 * v2
    print(dot_product) # Output: 32

    # Scalar multiplication
    v5 = 3 * v1
    print(v5)         # Output: Vector(3, 6, 9)

    # Magnitude
    print(v1.magnitude())  # Output: 3.7416573867739413

    # Normalization
    v_unit = v1.normalize()
    print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)