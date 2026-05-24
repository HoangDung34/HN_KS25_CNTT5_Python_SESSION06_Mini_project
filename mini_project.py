qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:
    print("--- QUẢN LÝ KHO ---")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    while True:
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))

            if 1 <= choice <= 5:
                break
            else:
                print("Vui lòng chọn từ 1 -> 5 !!!")

        except:
            print("Vui lòng nhập đúng định dạng số !!!")

    # 1. XEM BÁO CÁO
    if choice == 1:
        print("--- BÁO CÁO TỒN KHO ---")

        print(f"Laptop: {qty_laptop}",  end="")
        for i in range(qty_laptop):
            print("*", end="")
        print()

        print(f"Phone: {qty_phone}", end="")
        for i in range(qty_phone):
            print("*", end="")
        print()

        print(f"Tablet: {qty_tablet}", end="")
        for i in range(qty_tablet):
            print("*", end="")
        print()

    # 2. NHẬP KHO
    elif choice == 2:
        print("--- NHẬP KHO ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        while True:
            try:
                product = int(input("Chọn mặt hàng cần nhập: "))

                if 1 <= product <= 3:
                    break
                else:
                    print("Mặt hàng phải từ 1 -> 3 !!!")

            except:
                print("Vui lòng nhập đúng định dạng số !!!")

        while True:
            try:
                quantity = int(input("Nhập số lượng cần nhập: "))

                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại !!!")
                    continue

                break

            except:
                print("Vui lòng nhập đúng định dạng số !!!")

        if product == 1:
            qty_laptop += quantity
            print("Nhập kho Laptop thành công!")

        elif product == 2:
            qty_phone += quantity
            print("Nhập kho Phone thành công!")

        elif product == 3:
            qty_tablet += quantity
            print("Nhập kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

    # 3. XUẤT KHO
    elif choice == 3:
        print("--- XUẤT KHO ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        while True:
            try:
                product = int(input("Chọn mặt hàng cần xuất: "))

                if 1 <= product <= 3:
                    break
                else:
                    print("Mặt hàng phải từ 1 -> 3 !!!")

            except:
                print("Vui lòng nhập đúng định dạng số !!!")

        while True:
            try:
                quantity = int(input("Nhập số lượng cần xuất: "))

                if quantity < 0:
                    print("Số lượng không hợp lệ !!!")
                    continue

                break

            except:
                print("Vui lòng nhập đúng định dạng số !!!")

        if product == 1:
            if quantity > qty_laptop:
                print("Không đủ hàng!")
            else:
                qty_laptop -= quantity
                print("Xuất kho Laptop thành công!")

        elif product == 2:
            if quantity > qty_phone:
                print("Không đủ hàng!")
            else:
                qty_phone -= quantity
                print("Xuất kho Phone thành công!")

        elif product == 3:
            if quantity > qty_tablet:
                print("Không đủ hàng!")
            else:
                qty_tablet -= quantity
                print("Xuất kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

    # 4. CẢNH BÁO TỒN THẤP
    elif choice == 4:
        print("--- CẢNH BÁO TỒN KHO THẤP ---")

        if qty_laptop < 10:
            print("[CẢNH BÁO] Laptop sắp hết")

        if qty_phone < 10:
            print("[CẢNH BÁO] Phone sắp hết")

        if qty_tablet < 10:
            print("[CẢNH BÁO] Tablet sắp hết")

    # 5. THOÁT
    elif choice == 5:
        print("Đã thoát chương trình !!!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập từ 1 -> 5 !!!")
