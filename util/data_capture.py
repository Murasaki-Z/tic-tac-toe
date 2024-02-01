import csv, ast




def write_csv(data, file_path=None):
    if file_path is None:

        file_path = '/Users/abhi/Desktop/Personal/tic-tac=toe/util/game_data.csv'

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ["X moves", "O moves", "board state", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            
            row["X moves"] = row["X moves"]
            row["O moves"] = row["O moves"]
            row["board state"] = row["board state"]
            writer.writerow(row)

data = [
    {"X moves": "11, 12, 13", "O moves": "21, 22, 23", "board state": "XOXOXOXOX", "result": "X wins"},
    # Add more rows as needed
]


if __name__ == "__main__":
    # Write data to the CSV file
    write_csv(data)
