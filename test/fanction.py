def score(usual_score,final_score,bonus_points = 10):
    total_score = float(usual_score) * 0.3 + float(final_score) * 0.6 + bonus_points
    return total_score

def main():
    usual_score = float(input())
    final_score = float(input())
    bonus_point = float(input())
    total_score = score(usual_score,final_score,bonus_point)

    print(total_score)

main()