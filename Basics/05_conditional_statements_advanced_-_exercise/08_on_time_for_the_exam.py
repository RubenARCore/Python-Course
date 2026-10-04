exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

diff = arrival_time - exam_time

if diff == 0:
    print("On time")

elif diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        print(f"{hours}:{minutes:02d} hours after the start")

else:
    diff = abs(diff)

    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    else:
        print("Early")
        if diff < 60:
            print(f"{diff} minutes before the start")
        else:
            hours = diff // 60
            minutes = diff % 60
            print(f"{hours}:{minutes:02d} hours before the start")