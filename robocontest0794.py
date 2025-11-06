vazn,boy=map(int,input().split())
TVI=(10000*vazn)/pow(boy,2)
if 1<=vazn<=300 and 1<=boy<=300:
    if TVI<16:
        print("Yuqori vazn yetishmasligi")
    elif 16<=TVI<18.5:
        print("Vazn yetishmasligi")
    elif 18.5<=TVI<=25:
        print("Ideal vazn")
    elif 25<TVI<=30:
        print("Ortiqcha vazn")
    elif 30<TVI<=35:
        print("Semizlikning I darajasi")
    elif 35<TVI<=40:
        print("Semizlikning II darajasi")
    elif 40<TVI:
        print("Semizlikning III darajasi")
else:
    print(ValueError)   