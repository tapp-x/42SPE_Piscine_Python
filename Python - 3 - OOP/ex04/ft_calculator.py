class calculator:
    """class that is able to do calculations (dot product,
    addition, sub-traction) of 2 vectors."""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Perform a dotproduct operation between two vectors."""
        vec_res = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product: {vec_res}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Perform an addition operation between two vectors."""
        vec_res = [V1[i] + V2[i] for i in range(len(V1))]
        for i in range(len(vec_res)):
            vec_res[i] = float(vec_res[i])
        print(f"Add vector is: {vec_res}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Perform a subtraction operation between two vectors."""
        vec_res = [V1[i] - V2[i] for i in range(len(V1))]
        for i in range(len(vec_res)):
            vec_res[i] = float(vec_res[i])
        print(f"Sous vector is: {vec_res}")
