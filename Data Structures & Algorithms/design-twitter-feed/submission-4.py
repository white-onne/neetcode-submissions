class Twitter:

    def __init__(self):
        self.feed_cnt = 0
        self.tweet = defaultdict(list) # (usr_idx: [(tweet_id, feed_cnt)]) heapq로 관리
        self.followQ = defaultdict(set) # (usr_idx: [id, id, ...])
    def postTweet(self, userId: int, tweetId: int) -> None:
        # tweetID로 게시글 올리기, tweet_id는 unique
        self.tweet[userId].append((tweetId, self.feed_cnt))
        self.feed_cnt +=1

    def getNewsFeed(self, userId: int) -> list[int]:
        # userID의 10개의 최신 tweetID
        lst = []
        tmp = []
        heapq_lst = []
        # UserID의 피드 먼저 get
        # 넣을 때 heapq의 길이를 10으로 맞춰야 함
        for feedID, cnt in self.tweet[userId]:
            heapq.heappush(heapq_lst, (cnt, feedID))
        for k in self.followQ[userId]:
            for feedID, cnt in self.tweet[k]:
                heapq.heappush(heapq_lst, (cnt, feedID))
        # heap안의 갯수가 10개만 남을 때까지!
        while len(heapq_lst)>10:
            heapq.heappop(heapq_lst)
        # 갯수..를..흠...음...
        while len(heapq_lst):
            tmp.append(heapq.heappop(heapq_lst)[1])
        for i in range(len(tmp)-1, -1, -1):
            lst.append(tmp[i])

        return lst

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.followQ[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.followQ[followerId].discard(followeeId)
