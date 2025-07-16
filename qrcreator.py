# Developed by Audrise
# Uploaded to github as: https://github.com/Audrise/simpleqr

try:
    from time import sleep
    from sys import stdout
    from datetime import datetime
    from pystyle import *
    import qrcode

except Exception as e:
    print(f" [!] {e}")

dred = Col.dark_red
yellow = Col.yellow
orange = Col.orange
black = Col.black
green = Col.green
cyan = Col.cyan
res = Col.reset
red = Col.red

lightb = Col.StaticMIX((Col.light_blue, Col.blue, Col.light_blue))
purpled = Col.StaticMIX((Col.purple, Col.blue, Col.purple))
purple = Col.StaticMIX((Col.purple, Col.blue, Col.purple))
blued = Col.StaticMIX((Col.black, Col.blue, Col.dark_gray))
red2 = Col.StaticMIX((Col.red, Col.dark_red, Col.red))

logo = r"""
 ██████╗ ██████╗      ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔═══██╗██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║██████╔╝    ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝
██║▄▄ ██║██╔══██╗    ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝██║  ██║    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚══▀▀═╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                    By Audrise
"""

def animation(s):
    result = ""
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(0.006)
    return result

def normal(text, symbol = '!'):
    col1 = purple
    col2 = res
    return f" {Col.Symbol(symbol, col2, col1, '[', ']')} {col2}{text}"

def error(text, symbol = '!'):
    col1 = red
    col2 = res
    return f" {Col.Symbol(symbol, col2, col1, '[', ']')} {col2}{text}"

def success(text, symbol = '!'):
    col1 = green
    col2 = res
    return f" {Col.Symbol(symbol, col2, col1, '[', ']')} {col2}{text}"

def create_qr(link):
    try:
        now = datetime.now()
        date = now.strftime("%H%M%S")

        bordersize = input(animation(normal(f"Enter the border size {purple}[{lightb}Press enter for default{purple}] {purple}->{lightb} ", '?')))

        if bordersize == "":
            bordersize = 2

        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=bordersize, # You can customize the qr style here
        )

        qr.add_data(link)
        qr.make(fit=True)

        mk_img = qr.make_image(fill_color="black", back_color="white")

        qrname = input(animation(normal(f"Enter the QR name {purple}[{lightb}Press enter for skip{purple}] {purple}->{lightb} ", '?')))

        if qrname == "":
                randd = f"{date}.png"
                mk_img.save(randd)
                animation(success(f"{green}QR Code has been created and saved as {red}'{randd}'{res}"))
                Cursor.ShowCursor()
                print()
                exit()

        else:
            mk_img.save(qrname)
            animation(success(f"{green}QR Code has been created and saved as {red}'{qrname}'{res}"))
            Cursor.ShowCursor()
            print()
            exit()

    except KeyboardInterrupt:
        print()
        print(error(f"{red}Stopping All Process{res}\n"))
        sleep(1)
        System.Clear()
        Cursor.ShowCursor()
        exit()

    except Exception as e:
        animation(error(f"{red}Error: {e}{res}\n"))
        Cursor.ShowCursor()
        exit()

def main():
    try:
        Cursor.HideCursor()
        System.Clear()
        System.Size(100, 35)
        System.Title("QR Creator")
        print(Colorate.Diagonal(Col.DynamicMIX((blued, purpled)), Center.XCenter(logo)))
        print()

        while True:
            link = input(normal(f"Enter the URL {purple}->{lightb} ", '?'))

            if link == "":
                animation(error(f"{red}URL cannot be empty!", '!'))
                sleep(1)
                System.Clear()
                print(Colorate.Diagonal(Col.DynamicMIX((blued, purpled)), Center.XCenter(logo)))
                print()

            else:
                break
        create_qr(link)

    except KeyboardInterrupt:
        print()
        print(error(f"{red}Stopping All Process{res}\n"))
        sleep(1)
        System.Clear()
        Cursor.ShowCursor()
        exit()

    except Exception as e:
        animation(error(f"{red}Error: {e}{res}\n"))
        Cursor.ShowCursor()
        exit()

if __name__ == '__main__':
    main()
