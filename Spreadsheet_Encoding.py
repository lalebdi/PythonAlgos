"""
Problem:
 solve the problem of implementing a function that converts a spreadsheet
  column ID (i.e. "A", "B", "C", ..., "Z", "AA", etc.) to the corresponding integer.
"""


def spreadsheet_encode_column(col_str):
    num = 0 # return value'
    count = len(col_str) - 1 # the exponent
    for s in col_str:
        num += 26 ** count * (ord(s) - ord("A") + 1)
        count -= 1
    return num


print(spreadsheet_encode_column("A"))
print(spreadsheet_encode_column("AA"))
print(spreadsheet_encode_column("ZZ"))