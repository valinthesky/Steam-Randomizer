import time

bars = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

def animation():
    i = 0

    while True:
        print(bars[i % len(bars)], end="\r")
        time.sleep(.1)
        i += 1
        if i == 18:
            break