from heapq import heapify, heappop, heappush

class Twitter:

    def __init__(self):
        self._followers = defaultdict(set)
        self._tweets = defaultdict(list)
        self._count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._tweets[userId].append((self._count, tweetId))
        self._count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follower_tweets_queue = [(*self._tweets[followee][-1], -1, followee) for followee in self._followers[userId] if followee in self._tweets]
        
        if userId in self._tweets:
            follower_tweets_queue.append((*self._tweets[userId][-1], -1, userId))

        heapify(follower_tweets_queue)

        most_recent_tweets = []

        for _ in range(10):
            if len(follower_tweets_queue) == 0:
                break

            _, tweet_id, curr_ind, followee = heappop(follower_tweets_queue)

            most_recent_tweets.append(tweet_id)

            if curr_ind != -len(self._tweets[followee]):
                next_ind = curr_ind - 1
                heappush(follower_tweets_queue, (*self._tweets[followee][next_ind], next_ind, followee))

        return most_recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self._followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)