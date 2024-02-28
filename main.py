def adjacency_list_to_matrix(adj_list):
    # Extract the keys (nodes) and sort them to maintain a consistent order
    # nodes = sorted(adj_list.keys())
    nodes = adj_list.keys()
    # Create a mapping of node to index
    node_to_index = {node: index for index, node in enumerate(nodes)}

    # Initialize the adjacency matrix with zeros
    size = len(nodes)
    adj_matrix = [[0] * size for _ in range(size)]

    # Populate the adjacency matrix based on the adjacency list
    for node, neighbors in adj_list.items():
        node_index = node_to_index[node]
        for neighbor in neighbors:
            neighbor_index = node_to_index[neighbor]
            adj_matrix[node_index][neighbor_index] = 1  # Set to 1 where nodes are connected

    return adj_matrix

if __name__ == '__main__':

    adjacent_list = {
    "WA": [
        "ID",
        "OR"
    ],
    "DE": [
        "MD",
        "PA",
        "NJ"
    ],
    "DC": [
        "MD",
        "VA"
    ],
    "WI": [
        "MI",
        "MN",
        "IA",
        "IL"
    ],
    "WV": [
        "OH",
        "PA",
        "MD",
        "VA",
        "KY"
    ],
    "HI": [

    ],
    "FL": [
        "AL",
        "GA"
    ],
    "WY": [
        "MT",
        "SD",
        "NE",
        "CO",
        "UT",
        "ID"
    ],
    "NH": [
        "VT",
        "ME",
        "MA"
    ],
    "NJ": [
        "DE",
        "PA",
        "NY"
    ],
    "NM": [
        "AZ",
        "UT",
        "CO",
        "OK",
        "TX"
    ],
    "TX": [
        "NM",
        "OK",
        "AR",
        "LA"
    ],
    "LA": [
        "TX",
        "AR",
        "MS"
    ],
    "NC": [
        "VA",
        "TN",
        "GA",
        "SC"
    ],
    "ND": [
        "MN",
        "SD",
        "MT"
    ],
    "NE": [
        "SD",
        "IA",
        "MO",
        "KS",
        "CO",
        "WY"
    ],
    "TN": [
        "KY",
        "VA",
        "NC",
        "GA",
        "AL",
        "MS",
        "AR",
        "MO"
    ],
    "NY": [
        "NJ",
        "PA",
        "VT",
        "MA",
        "CT"
    ],
    "PA": [
        "NY",
        "NJ",
        "DE",
        "MD",
        "WV",
        "OH"
    ],
    "CA": [
        "OR",
        "NV",
        "AZ"
    ],
    "NV": [
        "ID",
        "UT",
        "AZ",
        "CA",
        "OR"
    ],
    "VA": [
        "NC",
        "TN",
        "KY",
        "WV",
        "MD",
        "DC"
    ],
    "CO": [
        "WY",
        "NE",
        "KS",
        "OK",
        "NM",
        "AZ",
        "UT"
    ],
    "AK": [

    ],
    "AL": [
        "MS",
        "TN",
        "GA",
        "FL"
    ],
    "AR": [
        "MO",
        "TN",
        "MS",
        "LA",
        "TX",
        "OK"
    ],
    "VT": [
        "NY",
        "NH",
        "MA"
    ],
    "IL": [
        "IN",
        "KY",
        "MO",
        "IA",
        "WI"
    ],
    "GA": [
        "FL",
        "AL",
        "TN",
        "NC",
        "SC"
    ],
    "IN": [
        "MI",
        "OH",
        "KY",
        "IL"
    ],
    "IA": [
        "MN",
        "WI",
        "IL",
        "MO",
        "NE",
        "SD"
    ],
    "OK": [
        "KS",
        "MO",
        "AR",
        "TX",
        "NM",
        "CO"
    ],
    "AZ": [
        "CA",
        "NV",
        "UT",
        "CO",
        "NM"
    ],
    "ID": [
        "MT",
        "WY",
        "UT",
        "NV",
        "OR",
        "WA"
    ],
    "CT": [
        "NY",
        "MA",
        "RI"
    ],
    "ME": [
        "NH"
    ],
    "MD": [
        "VA",
        "WV",
        "PA",
        "DC",
        "DE"
    ],
    "MA": [
        "RI",
        "CT",
        "NY",
        "NH",
        "VT"
    ],
    "OH": [
        "PA",
        "WV",
        "KY",
        "IN",
        "MI"
    ],
    "UT": [
        "ID",
        "WY",
        "CO",
        "NM",
        "AZ",
        "NV"
    ],
    "MO": [
        "IA",
        "IL",
        "KY",
        "TN",
        "AR",
        "OK",
        "KS",
        "NE"
    ],
    "MN": [
        "WI",
        "IA",
        "SD",
        "ND"
    ],
    "MI": [
        "WI",
        "IN",
        "OH"
    ],
    "RI": [
        "CT",
        "MA"
    ],
    "KS": [
        "NE",
        "MO",
        "OK",
        "CO"
    ],
    "MT": [
        "ND",
        "SD",
        "WY",
        "ID"
    ],
    "MS": [
        "LA",
        "AR",
        "TN",
        "AL"
    ],
    "SC": [
        "GA",
        "NC"
    ],
    "KY": [
        "IN",
        "OH",
        "WV",
        "VA",
        "TN",
        "MO",
        "IL"
    ],
    "OR": [
        "CA",
        "NV",
        "ID",
        "WA"
    ],
    "SD": [
        "ND",
        "MN",
        "IA",
        "NE",
        "WY",
        "MT"
    ]
}

    name_list = adjacent_list.keys()
    # Use a list comprehension to format each element with double quotes
    formatted_list = ', '.join([f'"{item}"' for item in name_list])
    # Print the formatted list surrounded by square brackets to mimic list output
    print(f'{formatted_list}')
    print("")

    adjacency_matrix = adjacency_list_to_matrix(adjacent_list)
    print("{", end="")
    for idx, itr in enumerate(adjacency_matrix):
        print("{" if idx == 0 else " {", end="")
        for i, value in enumerate(itr):
            end_char = ", " if i < len(itr) - 1 else ""
            print(value, end=end_char)
        print("}", end="")
        if idx < len(adjacency_matrix) - 1:
            print(",\n", end="")
    print("}")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
