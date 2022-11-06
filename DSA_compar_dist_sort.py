# import time
# import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def comp_sort(ar):
    c = [0 for i in range(len(ar))]
    b = [0 for i in range(len(ar))]
    st = time.time()
    for i in range(0, len(ar)):
        for j in range(i + 1, len(ar)):
            if ar[i] < ar[j]:
                c[j] = c[j] + 1
                if i != 0:
                    yield b
                    continue
            else:
                c[i] = c[i] + 1
                if i != 0:
                    yield b
                    continue
        b[c[i]] = ar[i]
        ar[i] = 0
        yield ar
        yield b
    et = time.time()
    print(b, "\n {:.2f}".format(et - st), " seconds.")


def dist_sort(ar, l_B, d_arr):
    b_arr = [0 for i in range(len(ar))]
    n = len(ar)
    st = time.time()
    for i in range(n - 1, -1, -1):
        j_ind = ar[i] - l_B
        d_arr[j_ind] = d_arr[j_ind] - 1
        b_arr[d_arr[j_ind]] = ar[i]
        ar[i] = 0
        yield ar
        yield b_arr
    et = time.time()
    print(b, "\n {:.2f}".format(et - st), " seconds.")
    #print("\n", b_arr)


if __name__ == "__main__":
    ch = "0"
    while True:
        N = int(input("\nEnter number of integers: "))
        lb = int(input("Enter lower bound: "))
        ub = int(input("Enter upper bound: "))

        ch = input("\n1.Comparison sorting\n2.Distribution sorting\n3.Exit\nEnter your choice: ")
        arr = list(np.random.randint(lb, ub, N))
        if ch == "1":
            generator = comp_sort(arr)

            b = [0 for i in range(N)]
            title = "comparison counting sort"

            fig, (ay, ax) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 1]})
            fig.set_size_inches(16, 6)

            ay.set_title("before sorting")
            bar_rects1 = ay.bar(range(N), arr, align="edge", color='green', edgecolor='black')
            ay.set_xlim(-1, N + 1)
            ay.set_ylim(min(arr) - 1, max(arr) + 1)

            ax.set_title("after sorting")
            bar_rects = ax.bar(range(N), b, align="edge", color=(0.9, 0.7, 0.1, 0.5), edgecolor='green')
            ax.set_xlim(-1, N + 1)
            ax.set_ylim(min(arr) - 1, max(arr) + 1)
            text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
            iteration = [0]
            cnt = 0
            s = 1
            le = len(arr)


            def update_fig(gen, barrects1, barrects2, it):
                global cnt, arr, le, s
                Num = int(((len(arr) + 1) * len(arr)) / 2)
                flag = 0
                if s == 0:
                    time.sleep(1)
                x = zip(barrects1, barrects2, gen)
                if it[0] < Num:
                    it[0] += 1
                    text.set_text("# of operations: {}".format(it[0]))
                for i, j, k in x:
                    cnt += 1
                    if it[0] == 1:
                        i.set_height(k)
                        flag = 1
                        continue
                    if it[0] < s:
                        j.set_height(k)
                    elif it[0] == s and s != (Num + 1):
                        i.set_height(k)
                        flag = 2
                #print(i, " --- ", j, " --- ", k, " -- count : ", cnt, " -- iter : ", it[0], " -- s : ", s)
                if flag == 1:
                    s = le + 1
                    le -= 1
                elif flag == 2:
                    s += le
                    le -= 1
                if it[0] == (Num + 1):
                    j.set_height(k)


            anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects1, bar_rects, iteration),
                                           frames=generator
                                           , interval=0, repeat=False)

            plt.show()
        elif ch == "2":

            b = [0 for i in range(len(arr))]
            # initialize frequency
            d = [0 for i in range(0, (ub - lb + 1))]  # 0-n index
            # compute frequency of each item
            for i in range(0, len(arr)):
                j = arr[i] - lb
                d[j] = d[j] + 1
            # compute sum of accumulated frequencies
            for i in range(1, (ub - lb + 1)):
                d[i] = d[i] + d[i - 1]

            generator = dist_sort(arr, lb, d)

            b = [0 for i in range(N)]

            fig, (ax, ay) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 1]})
            fig.set_size_inches(16, 6)

            ax.set_title("before sorting")
            bar_rects1 = ax.bar(range(N), arr, align="edge", color='green', edgecolor='black')
            ax.set_xlim(-1, N + 1)
            ax.set_ylim(min(arr) - 1, max(arr) + 1)

            ay.set_title("after sorting")
            bar_rects = ay.bar(range(N), b, align="edge", color=(0.9, 0.7, 0.1, 0.5), edgecolor='green')
            ay.set_xlim(-1, N + 1)
            ay.set_ylim(min(arr) - 1, max(arr) + 1)
            text = ay.text(0.02, 0.95, "", transform=ay.transAxes)

            iteration = [0]
            cnt = 0
            s = 1
            le = len(arr)


            def update_fig(xyz, br_1, br_2, it):
                it[0] += 1
                if it[0] % 2 == 0:
                    text.set_text("# of operations: {}".format(int(it[0] / 2)))
                x = zip(br_1, br_2, xyz)
                for rect1, rect, val in x:
                    # print(rect, "---", val, " --- ", it[0])
                    if it[0] % 2 == 1:
                        rect1.set_height(val)
                    else:
                        rect.set_height(val)


            anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects1, bar_rects, iteration),
                                           frames=generator
                                           , interval=0, repeat=False)

            plt.show()
        elif ch == "3":
            break
        else:
            print("\nInvalid input")
