# vacation calendar more elegant version!!

d = input("enter day of the year:")

if d >= "2024.12.24" and d <= "2025.01.02":
    print(f"This day belongs to Christmas vacation '24 : {d:}")
else:
    if d >= "2025.04.18" and d <= "2025.04.21":
        print(f"This day belongs to Easter vacation : {d}")
    else:
        if d > "2025.08.08" and d <= "2025.08.19":
            print(f"This day belongs to summer vacation : {d}")
        else:
            if d >= "2025.12.24" and d <= "2026.01.02":
                print(f"This day belongs to Christmas vacation '25 : {d}")
            else:
                if d >= "2025.07.14" and d <= "2025.07.25":
                    print("this is my extra private vacation ;-P")
                else:
                    print("It is a working day :-( ")
