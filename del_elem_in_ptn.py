def del_elem_in_ptn(del_element, pattern):
    output = []
    for i in range(len(pattern)):
        output.append([])
        for j in range(len(pattern[i])):
            if pattern[i][j] != del_element:
                output[i].append(pattern[i][j])
    for i in range(len(output)):
        if not output[len(output)-i-1]:
            del output[len(output)-i-1]
    return output