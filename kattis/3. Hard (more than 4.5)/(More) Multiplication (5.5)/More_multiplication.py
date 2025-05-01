#Accepted - 0.07s

A, B = input().split()
while int(A) + int(B) > 0:

    result = str(int(A) * int(B))
    leng_result = len(result)

    leng_hor = len(A) - 1
    horizontal_line = "+--"
    horizontal_line += "-" * (leng_hor * 4 + 5)
    horizontal_line += "+"
    print(horizontal_line)

    current_line = "|   "
    for char in A:
        current_line += f"{char}   "
    current_line += "|"
    print(current_line)

    internal_line = "| "
    for char in A:
        internal_line += "+---"
    internal_line += "+ |"
    print(internal_line)

    results_list = []
    for charB in B:
        temp_list = [str(int(charB) * int(charA)) for charA in A]
        results_list.append(temp_list)

    bar = False
    track = 0
    for i in range(len(B)):
        if bar:
            current_line = "|/|"
        else:
            current_line = "| |"
        for j in range(len(A)):
            if len(results_list[i][j]) > 1:
                current_line += f"{results_list[i][j][0]} /|"
            else:
                current_line += "0 /|"
        current_line += " |"
        print(current_line)

        current_line = "| |"
        for j in range(len(A)):
            current_line += " / |"
        current_line += f"{B[i]}|"
        print(current_line)

        if len(A) + len(B) - i <= len(result):
            current_line = f"|{result[track]}|"
            track += 1
            bar = True
        else:
            current_line = "| |"
        for j in range(len(A)):
            if len(results_list[i][j]) == 1:
                current_line += f"/ {results_list[i][j][0]}|"
            else:
                current_line += f"/ {results_list[i][j][1]}|"
        current_line += " |"
        print(current_line)

        print(internal_line)
       
    if bar:
        current_line = "|/ "
    else:
        current_line = "|  "
    for j in range(len(A) - 1):        
        current_line += f"{result[track]} / "
        track += 1
    current_line += f"{result[track]}    |"
    print(current_line)
    
    print(horizontal_line)
    A, B = input().split()
