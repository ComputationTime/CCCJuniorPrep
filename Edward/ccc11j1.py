def solve():
    antennas = int(input())
    eyes = int(input())
    output = []
    if antennas >= 3 and eyes <= 4:
        output.append("TroyMartian")
    if antennas <= 6 and eyes >= 2:
        output.append("VladSaturnian")
    if antennas <= 2 and eyes <= 3:
        output.append("GraemeMercurian")
    [print(x) for x in output]

solve()
