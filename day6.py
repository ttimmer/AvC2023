import re
import math
def perform_solution(input):
    input_lines = input.splitlines()
    time_line = input_lines[0]
    distance_line = input_lines[1]
    times =  re.findall(r'\d+', time_line);
    distances =  re.findall(r'\d+', distance_line);
    iset = 0
    totalWins = 1
    win =1
    for set in distances:
        totalWins = win*totalWins
        win =0
        minWin = math.ceil(float(set)/float(times[iset]));
        iTimeleft = int(times[iset])
        while minWin < iTimeleft:
            print(f"{minWin} < {iTimeleft}")
            timelefttotravel = iTimeleft-minWin
            distancelefttotravel = timelefttotravel*minWin
            #print(f"Distance traveled {distancelefttotravel}")
            minWin+=1
            if distancelefttotravel>int(set):
                win+=1
        print(f"{win}Wins for set {iset} makes totalwins{totalWins*win}")
        iset +=1;
    totalWins=win*totalWins
    print(f"Timestamps{times} and Distances {distances}")
    return totalWins
def perform_solution2(input):
    print("not implemented yet")

if __name__ == '__main__':
    input_test = """Time:      7  15   30
    Distance:  9  40  200"""
    solution_test1 = 288
    if (solution_test1== perform_solution(input_test)):
        print("Yay")

    input_actual ="""Time:        47     84     74     67
Distance:   207   1394   1209   1014"""
    print(perform_solution(input_actual))

    input_actual_2 ="""Time:        47847467
Distance:   207139412091014"""
    print(perform_solution(input_actual_2))
