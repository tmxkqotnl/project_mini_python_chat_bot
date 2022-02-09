import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import platform

# set plt attrs
def set_plt() -> None:
    ## set plt minus font
    plt.rcParams["axes.unicode_minus"] = False
    
    ## set font
    system_name: str = platform.system()
    if system_name == "Windows":
        # Windows
        plt.rc("font", family="Malgun Gothic")
    elif system_name == "Darwin":
        # Mac
        plt.rc("font", family="AppleGothic")
    elif system_name == "Linux":
        # Linux
        path = "/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf"
        font_name = font_manager.FontProperties(fname=path, size=12)
        plt.rc("font", family=font_name)
    else:
        print("Not support")