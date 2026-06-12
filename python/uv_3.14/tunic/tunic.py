import pyperclip


def main():
    x_offsest = 10
    y_offset = -5

    x_1 = 0 + x_offsest
    x_2 = 40 + x_offsest
    x_3 = 80 + x_offsest
    y_1 = 15 + y_offset
    y_2 = 40 + y_offset
    y_3 = 60 + y_offset
    y_4 = 75 + y_offset
    y_5 = 90 + y_offset
    y_6 = 110 + y_offset
    y_7 = 130 + y_offset

    cx = 40 + x_offsest
    cy = 145 + y_offset

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 165">
    <g stroke-width="10" stroke="black" stroke-linecap="round">
        <line id="1" x1="{x_2}" y1="{y_1}" x2="{x_3}" y2="{y_2}"/>
        <line id="2" x1="{x_3}" y1="{y_6}" x2="{x_3}" y2="{y_5}"/>
        <line id="2b" x1="{x_3}" y1="{y_2}" x2="{x_3}" y2="{y_4}"/>
        <line id="3" x1="{x_2}" y1="{y_7}" x2="{x_3}" y2="{y_6}"/>
        <line id="4" x1="{x_1}" y1="{y_6}" x2="{x_2}" y2="{y_7}"/>
        <line id="5" x1="{x_1}" y1="{y_2}" x2="{x_1}" y2="{y_4}"/>
        <line id="5b" x1="{x_1}" y1="{y_6}" x2="{x_1}" y2="{y_5}"/>
        <line id="6" x1="{x_1}" y1="{y_2}" x2="{x_2}" y2="{y_1}"/>
        <line id="7" x1="{x_2}" y1="{y_1}" x2="{x_2}" y2="70"/>
        <line id="8" x1="{x_2}" y1="{y_3}" x2="{x_3}" y2="{y_2}"/>
        <line id="9" x1="{x_2}" y1="{y_5}" x2="{x_3}" y2="{y_6}"/>
        <line id="10" x1="{x_2}" y1="{y_5}" x2="{x_2}" y2="{y_7}"/>
        <line id="11" x1="{x_1}" y1="{y_6}" x2="{x_2}" y2="{y_5}"/>
        <line id="12" x1="{x_1}" y1="{y_2}" x2="{x_2}" y2="{y_3}"/>
        <line id="13" x1="{x_1}" y1="{y_4}" x2="{x_3}" y2="{y_4}"/>
        <line id="14" x1="{x_2}" y1="{y_3}" x2="{x_2}" y2="70"/>
        <circle cx="{cx}" cy="{cy}" r="15" fill="transparent"/>
    </g>
</svg>
    """
    print(svg)
    pyperclip.copy(svg)


if __name__ == "__main__":
    main()
