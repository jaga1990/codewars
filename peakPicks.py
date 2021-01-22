def pick_peaks(arr):
    #arr = [0, 1, 2, 5, 1, 0]
    length = len(arr)
    peak = {"pos": [], "peaks": []}
    marker = 0
    for i in range(length):
        if i==0: 
            next
        elif i==length-1:
            exit
        else:
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]: 
                peak["pos"].append(i)
                peak["peaks"].append(arr[i])
            elif arr[i]>arr[i-1] and arr[i]==arr[i+1]:
                marker=1
                position=i
            elif arr[i]==arr[i-1] and arr[i]>arr[i+1] and marker==1:
                peak["pos"].append(position)
                peak["peaks"].append(arr[i])
                marker=0
    return peak
pick_peaks([1, 2, 2, 2, 2])


# #Best solution:
# def pick_peaks(arr):
#     pos = []
#     prob_peak = False
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             prob_peak = i
#         elif arr[i] < arr[i-1] and prob_peak:
#             pos.append(prob_peak)
#             prob_peak = False
#     return {'pos':pos, 'peaks':[arr[i] for i in pos]}