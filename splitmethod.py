def split_method(product_upc):
    upc_end = product_upc[-1]
    upc_length = len(product_upc)
    if upc_length == 13:
        if upc_length == 13 and product_upc[0] != '0' and product_upc[11:13].isalpha():  # 2A
            folder = product_upc[:6]
            file_base = product_upc[6:12]
            print(f"{product_upc}({upc_length}) Folder:{folder} File Base:{file_base}")

        elif product_upc[0:2] == '00' and upc_end.isalpha():  # 002652081134S 1A
            folder = product_upc[2:7]
            file_base = product_upc[7:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0:2] == '00' and upc_end.isnumeric():  # 0026520811345 1B
            folder = product_upc[2:8]
            file_base = product_upc[8:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0] == '0' and product_upc[1] != '0' and upc_end.isalpha():  # 082652081122S 1C
            folder = product_upc[1:7]
            file_base = product_upc[7:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base


        elif product_upc[0] == '0' and product_upc[1] != '0' and upc_end.isnumeric():  # 0826520811221 1D
            folder = product_upc[1:8]
            file_base = product_upc[8:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        else:  # 123456789123S or 1234567891234 1E
            folder = product_upc[:7]
            file_base = product_upc[7:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

    if upc_length == 12:
        if product_upc[0] != '0' and upc_end.isalpha():  # 2B
            folder = product_upc[1:6]
            file_base = product_upc[6:]
            print(f"{product_upc}({upc_length}) Folder:{folder} File Base:{file_base}")

        if product_upc[0:2] == '00' and upc_end.isalpha():  # 00265208113S 1F
            folder = product_upc[1:6]
            file_base = product_upc[6:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0:2] == '00' and upc_end.isnumeric():  # 002652081134 1G
            folder = product_upc[2:7]
            file_base = product_upc[7:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0] == '0' and product_upc[1] != '0' and upc_end.isalpha():  # 08265208112S 1H
            folder = product_upc[1:6]
            file_base = product_upc[6:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0] == '0' and product_upc[1] != '0' and upc_end.isnumeric():  # 082652081121 1I
            folder = product_upc[1:7]
            file_base = product_upc[7:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base


        elif product_upc[0] != '0' and upc_end.isalpha():  # 12345678912S 1J
            folder = product_upc[:6]
            file_base = product_upc[6:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0] != '0' and upc_end.isnumeric():  # 12345678912S 1K
            folder = product_upc[:7]
            file_base = product_upc[7:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

    if upc_length == 11:
        if product_upc[0] == '0' and upc_end.isnumeric():  # 00265208112 or 08265208112 1N
            folder = product_upc[1:6]
            file_base = product_upc[6:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif upc_end.isalpha():  # 1234567891S or 0826520811S or 0026520811S 1L
            folder = product_upc[:5]
            file_base = product_upc[5:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0] != '0' and upc_end.isnumeric():  # 1M
            folder = product_upc[:6]
            file_base = product_upc[6:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        else:  # 12345678912 1O
            folder = product_upc[:6]
            file_base = product_upc[6:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base


    if upc_length == 10:  # 002652081S or 082652081S or 123456789S 1P
        if upc_end.isalpha():
            folder = product_upc[:4]
            file_base = product_upc[4:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif upc_end.isnumeric() and product_upc[0:2] == '00':  # 0026520811 1Q
            folder = product_upc[:5]
            file_base = product_upc[5:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif product_upc[0] == '0' and product_upc[1] != '0' and upc_end.isnumeric():  # 0826520811 1R
            folder = product_upc[:5]
            file_base = product_upc[5:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        else:  # 1234567891 1S
            folder = product_upc[:5]
            file_base = product_upc[5:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

    if upc_length == 9:
        if upc_end.isalpha():  # 00265208S or 08265208S or 12345678S 1T
            folder = product_upc[:5]
            file_base = product_upc[5:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        else:  # 002652088 or 082652088 or 123456789 1X
            folder = product_upc[:4]
            file_base = product_upc[4:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

    if upc_length == 8:
        if upc_end.isalpha():  # 0026520S or 0826520S or 1234567S 1Y
            folder = product_upc[:2]
            file_base = product_upc[2:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        elif upc_end.isnumeric():  # 00265208 or 08265208 or 12345678 1Z
            folder = product_upc[:5]
            file_base = product_upc[5:]
            print(f"{product_upc}({len(product_upc)}) Folder:{folder} File Base:{file_base}")
            return folder, file_base

        else:
            print("No match logic (1).")