# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

# from datetime import datetime

# n = int(input())

# # marking each meessage with time stamp
# chats = {input(): datetime.now() for i in range(n)}

# # sorting the messages based on the time stamp
# sorted_chats = sorted(chats.items(), key=lambda x: x[1], reverse=True)

# # printing chats (recent to old)
# for chat in sorted_chats:
#     print(chat[0])

from collections import defaultdict

n = int(input())
chats = [input() for i in range(n)]

# used to memorize printed chats
printed = defaultdict(bool)
# looping through the chats from recent to old
for chat in chats[::-1]:
    if printed.get(chat) is None:
        print(chat)
        printed[chat] = True